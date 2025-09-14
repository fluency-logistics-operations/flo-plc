
# Fluency Logistics Operations (FLO)

[![PyPI version](https://img.shields.io/pypi/v/FluencyLogisticsOperations)](https://pypi.org/project/FluencyLogisticsOperations/) [![Python versions](https://img.shields.io/pypi/pyversions/FluencyLogisticsOperations)](https://pypi.org/project/FluencyLogisticsOperations/) [![License](https://img.shields.io/pypi/l/FluencyLogisticsOperations)](https://github.com/fluency-logistics-operations/flo-plc/blob/main/LICENSE)

**FLO** is a Python library and ecosystem that streamlines **enterprise data integration**. It provides a **centralized configuration plane** (MUI), a **remote execution engine** (RES), and **scoped access tokens** (AAT) to manage integrations securely and consistently. Together, these components enable teams to fetch and manipulate enterprise data using simple **dot-notation calls**, returning **pandas DataFrames** that are *schema-consistent* and **ready to query**.

---

## 🔑 Ecosystem Highlights

- **Centralized Configuration (MUI)** — Define client-resource profiles (methods, auth flows, extraction rules) once.
- **Scoped Access (AAT)** — Grant apps/team tokens with limited, role-based scopes across multiple clients/resources.
- **Remote Execution (RES)** — Execute requests centrally, injecting configuration and security at runtime.
- **DataFrame I/O** — Results return as ready-to-use **pandas DataFrames**, reducing parsing boilerplate.
- **Governance Built-In** — Team-based organization, reproducible requests, and auditable access.

---

## 📦 Installation

```bash
pip install FluencyLogisticsOperations
```

> Requires Python 3.8+ (see supported versions badge above).

---

## ⚙️ Configure Environment

Set credentials and server URL via environment variables (recommended) or pass explicitly to `FLO()`.

- **`FLO_URL`** — FLO **Remote Execution Server (RES)** URL.  
  Default: `https://res.fluency-logistics-operations.io`
- **`FLO_AAT`** — FLO **API Access Token (AAT)**.  
  Generate via the **Minimal User Interface (MUI)**: <https://mui.fluency-logistics-operations.io/aat>  
  AATs define which clients/resources this app can call (scoped access).

Example:

```bash
export FLO_URL="https://res.fluency-logistics-operations.io"
export FLO_AAT="your_access_token_here"
```

You can also pass the token in code:

```python
from FluencyLogisticsOperations import FLO
flo = FLO(aat="your_access_token_here")  # or FLO(aat=lambda: "token")
```

---

## 🚀 Quick Start

```python
from FluencyLogisticsOperations import FLO

# Uses $FLO_URL and $FLO_AAT (configured in MUI)
flo = FLO()

# Fetch a single Client Resource Item (CRI)
# "abc123" is a resource configured in the MUI with its own method/auth/extraction rules
item = flo.client.resource("abc123").get()

# Fetch multiple CRI with filters
items = flo.client.resource.list(limit=100, created_after="2025-08-01")

print(item.head())
print(items.head())
```

Your code stays light — the RES applies the profile logic and returns clean DataFrames.

---

## 🧭 How FLO Works

FLO **bridges the gap** between your app and enterprise APIs:

1. **Define Profiles (MUI):** Configure clients, auth, and extraction once.
2. **Issue Token (AAT):** Grant apps scoped access to those profiles.
3. **Call FLO:** Use simple dot-notation calls from Python.
4. **RES Executes:** Centralized engine injects configuration, authenticates, and proxies the request.
5. **Return DataFrame:** You get schema-consistent data or perform updates — **DF in/out**.

---

## 🔩 Wire-Level Behavior

FLO serializes your method calls into an RPC-style request, sends them to RES, and materializes the response as a DataFrame.

**Example:**

```python
flo.client.resource("abc123").get()
```
```
POST /rpc
Content-Type: application/x-www-form-urlencoded
source=client
target=resource(abc123)
method=get
kwargs={}
```

RES handles auth, transforms the response according to the profile’s extraction rules, and returns a DataFrame.

---

## 🧩 Benefits for Teams & Data Engineers

- **Reduce Boilerplate:** Centralized profiles eliminate repetitive client code.
- **Consistent Schemas:** DataFrames always match configured extraction rules.
- **Scoped Security:** AATs limit access to only necessary resources/methods per workflow.
- **Centralized Governance:** Team-based control and auditing limit exposure and support compliance.
- **Rapid Onboarding:** New apps can be built quickly by referencing existing profiles.

---

## 📜 License

Apache 2.0 — open and permissive. See [LICENSE](https://github.com/fluency-logistics-operations/flo-plc/blob/main/LICENSE).

---

## 🔒 Proprietary Components Notice

The **Remote Execution Server (RES)** and **Minimal User Interface (MUI)** referenced in this README are **proprietary systems** operated by **Fluency Logistics Operations LLC**.  
This repository contains only the **public client library**, licensed under Apache 2.0.  

Use of the RES and MUI is governed by separate commercial terms.  
Reverse engineering, duplication, or redistribution of these components without a written license agreement is prohibited.

---

**Contact:** flo@fluency-logistics-operations.io

> “No one knows the future save they see it in a dream and speak it forth into being.”  
> — braden@bradenkeith.io
