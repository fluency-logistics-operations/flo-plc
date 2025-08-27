# Fluency Logistics Operations (FLO)

## Public Layer Client (PLC)

### FLO PLC

```python
from FluencyLogisticsOperations import FLO

flo = FLO()  # uses $FLO_BASE_URL (default https://fluency-logistics-operations.io) and $FLO_TOKEN
item = flo.client.resource("abc123").get()
items = flo.client.resource.list(limit=100, created_after="2025-08-01")
```

- Sends `POST /rpc` with `Content-Type: application/x-www-form-urlencoded`
- Body: `method=client.resource(abc123).get()` (identifier unquoted)
- Returns: `pandas.DataFrame`

- Sends `POST /rpc` with `Content-Type: application/x-www-form-urlencoded`
- Body: `method=client.resource.list(limit=100, created_after=\"2025-08-01\")`
- Returns: `pandas.DataFrame`

Env vars: `FLO_BASE_URL`, `FLO_TOKEN`

---

> No one knows the future save they see it in a dream and speak it forth into being.

— braden@bradenkeith.io

---
