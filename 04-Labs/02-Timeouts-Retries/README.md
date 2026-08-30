---
title: "Lab 02 — Timeouts and Retries"
type: lab
status: completed
topic: distributed-systems
difficulty: intermediate
tags:
  - lab
  - distributed-systems
  - retries
  - reliability
created: 2026-08-30
updated: 2026-08-30
---

# Lab 02 — Timeouts and Retries

!!! example "This lab is the worked example for the vault"
    It shows the expected shape: one question, a prediction written **before**
    the run, raw observations, and an honest verdict on the prediction. The
    **Actual Result** section is left for you to fill in — that is the part
    that cannot be pre-written.

## Goal

> **Does adding retries make a saturated dependency recover faster, or does it
> make the outage worse?**

Specifically: with a downstream service at capacity, compare client-side
strategies — no retry, fixed-interval retry, exponential backoff, and
exponential backoff with full jitter — on client success rate, client p99
latency, and offered load at the server.

## Concepts

- [Timeouts and Retries](../../03-Concepts/Distributed-Systems/Fundamentals/Timeouts%20and%20Retries.md)
- [Latency and Throughput](../../03-Concepts/Distributed-Systems/Fundamentals/Latency%20and%20Throughput.md)
- [Partial Failure](../../03-Concepts/Distributed-Systems/Fundamentals/Partial%20Failure.md)
- [Idempotency](../../03-Concepts/Distributed-Systems/Fundamentals/Idempotency.md)

## Prerequisites

- [ ] Python 3.11+ or Go 1.22+
- [ ] A load generator (`hey`, `wrk`, `vegeta`, or a short script)
- [ ] Read the AWS Builders' Library article on timeouts, retries and backoff

## Architecture

```mermaid
flowchart LR
    LG[Load generator<br/>fixed arrival rate] --> C[Client<br/>retry policy under test]
    C --> S["Server<br/>concurrency limit = 10<br/>service time = 100 ms"]
    S --> M[Metrics:<br/>offered load, success rate,<br/>p50/p99 latency]
```

The server is deliberately capacity-limited: 10 concurrent slots, 100 ms of
work per request, so its ceiling is ~100 req/s. Drive it at ~150 req/s and it
is saturated by construction. That is the point — this lab is about behaviour
past the knee.

## Setup

```bash
mkdir -p lab02 && cd lab02
python3 -m venv .venv && source .venv/bin/activate
pip install fastapi uvicorn httpx
```

`server.py` — a dependency with a hard concurrency limit:

```python
import asyncio
from fastapi import FastAPI, Response

app = FastAPI()
SLOTS = asyncio.Semaphore(10)      # capacity: 10 concurrent
SERVICE_TIME = 0.100                # 100 ms of work
offered = 0                         # every arrival, including retries

@app.get("/work")
async def work():
    global offered
    offered += 1
    if SLOTS.locked():
        return Response(status_code=503)   # shed load rather than queue
    async with SLOTS:
        await asyncio.sleep(SERVICE_TIME)
        return {"ok": True}

@app.get("/stats")
async def stats():
    return {"offered": offered}
```

```bash
uvicorn server:app --port 8000
```

`client.py` — the four strategies:

```python
import asyncio, random, time, statistics, sys
import httpx

STRATEGY = sys.argv[1]            # none | fixed | backoff | jitter
RATE     = 150                    # requests/second offered by users
DURATION = 30                     # seconds
MAX_ATTEMPTS = 4
TIMEOUT  = 0.5                    # ~p99 of a healthy server

def delay(attempt: int) -> float:
    if STRATEGY == "fixed":
        return 0.100
    if STRATEGY == "backoff":
        return 0.100 * (2 ** attempt)
    if STRATEGY == "jitter":
        return random.uniform(0, min(20.0, 0.100 * (2 ** attempt)))
    return 0.0

async def one_user_request(client, latencies, results):
    start = time.perf_counter()
    attempts = 1 if STRATEGY == "none" else MAX_ATTEMPTS
    for attempt in range(attempts):
        try:
            r = await client.get("http://localhost:8000/work", timeout=TIMEOUT)
            if r.status_code == 200:
                results.append("ok")
                latencies.append(time.perf_counter() - start)
                return
        except httpx.TimeoutException:
            pass
        if attempt < attempts - 1:
            await asyncio.sleep(delay(attempt))
    results.append("fail")
    latencies.append(time.perf_counter() - start)

async def main():
    latencies, results = [], []
    async with httpx.AsyncClient() as client:
        tasks = []
        for _ in range(RATE * DURATION):
            tasks.append(asyncio.create_task(
                one_user_request(client, latencies, results)))
            await asyncio.sleep(1 / RATE)
        await asyncio.gather(*tasks)
        stats = (await client.get("http://localhost:8000/stats")).json()

    ok = results.count("ok")
    latencies.sort()
    print(f"strategy       : {STRATEGY}")
    print(f"user requests  : {len(results)}")
    print(f"success rate   : {100 * ok / len(results):.1f}%")
    print(f"p50 latency    : {latencies[len(latencies)//2]*1000:.0f} ms")
    print(f"p99 latency    : {latencies[int(len(latencies)*0.99)]*1000:.0f} ms")
    print(f"offered load   : {stats['offered']} "
          f"({stats['offered']/len(results):.2f}x amplification)")

asyncio.run(main())
```

## Experiment

Restart the server between runs so the `offered` counter resets.

```bash
for s in none fixed backoff jitter; do
  curl -s localhost:8000/stats > /dev/null      # server restarted here
  python client.py "$s"
  echo "---"
done
```

## Failure Injection

The failure is **saturation**, not a crash — deliberately, because saturation
is the case where retries do damage. Offered user load (150 req/s) exceeds
server capacity (~100 req/s) for the whole run.

Optional extensions:

```bash
# Add latency so timeouts fire on requests that would have succeeded
sudo dnctl pipe 1 config delay 300ms          # macOS
sudo tc qdisc add dev lo root netem delay 300ms   # Linux

# Or make the server slow instead of shedding: raise SERVICE_TIME to 400 ms
```

## Expected Result

Written before running. Predictions:

1. **`none`** — success rate around 65% (capacity ÷ offered load). p99 stays
   near 100 ms because failures fail fast. Amplification 1.0x.
2. **`fixed`** — the worst. Amplification approaching 4x drives offered load to
   ~600 req/s against a 100 req/s server, so success rate falls **below** the
   no-retry case. This is the counter-intuitive result and the point of the lab.
3. **`backoff`** — better than fixed; spacing lets the server drain. Success
   rate above `none`, p99 much worse (a request may wait 100+200+400 ms).
4. **`jitter`** — best success rate and the smoothest offered load, because
   clients stop retrying in synchronised waves.

Ranking predicted: `jitter` > `backoff` > `none` > `fixed` on success rate;
`none` best on p99 by a wide margin.

## Observations

<!-- Paste raw output here. Do not summarise yet. -->

```text
strategy       :
user requests  :
success rate   :
p50 latency    :
p99 latency    :
offered load   :
```

| Strategy | Success rate | p50 | p99 | Offered load | Amplification |
| --- | --- | --- | --- | --- | --- |
| none |  |  |  |  |  |
| fixed |  |  |  |  |  |
| backoff |  |  |  |  |  |
| jitter |  |  |  |  |  |

## Actual Result

<!-- Fill in after the run. State plainly whether each prediction held. -->

- Prediction 1 (`none` ≈ 65%):
- Prediction 2 (`fixed` worse than `none`):
- Prediction 3 (`backoff` better, p99 worse):
- Prediction 4 (`jitter` best):

## Lessons Learned

<!-- Especially: where the prediction was wrong, and why. -->

Questions to answer here:

- [ ] At what offered-load multiple does retrying stop helping?
- [ ] What would a 10% retry budget have done to the `fixed` case?
- [ ] The timeout was 500 ms. What happens at 200 ms, and why?
- [ ] Where would a circuit breaker have changed the outcome?

## Related Concepts

- [Timeouts and Retries](../../03-Concepts/Distributed-Systems/Fundamentals/Timeouts%20and%20Retries.md)
- [Latency and Throughput](../../03-Concepts/Distributed-Systems/Fundamentals/Latency%20and%20Throughput.md)
- [Load Balancing](../../03-Concepts/Cloud/Networking/Load%20Balancing.md)

## Cleanup

```bash
# Stop uvicorn (Ctrl-C), then:
deactivate
# Remove any traffic shaping that was added:
sudo dnctl -q flush                      # macOS
sudo tc qdisc del dev lo root            # Linux
```

Nothing in this lab is billable — it runs entirely on localhost.
