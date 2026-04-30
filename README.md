# 📚 Student Resource Guide
## Nepal Weather CLI & Cloud-Native FastAPI — Upskilling Toolkit

> **Professor's Note:** Every link below has been verified. Work through these resources **in order** — start with the foundational Python topics, then move to FastAPI and Pydantic, and finish with the Twelve-Factor methodology. Do not skip sections.

---

## 🗺️ Learning Roadmap

```
Python Fundamentals → Enums & Typing → argparse & logging
       ↓
python-dotenv & Environment Variables
       ↓
Pydantic v2 (BaseModel, Validation, Response Models)
       ↓
FastAPI (Routes, HTTP Methods, HTTPException)
       ↓
Uvicorn (ASGI Server, Port Binding)
       ↓
Twelve-Factor App Methodology
```

---

## 🐍 Section 1: Python Fundamentals You Must Know

These are the Python standard library tools used directly in both assignments. Read these **before** touching any framework.

---

### 📖 `argparse` — CLI Argument Parsing

> **Why it matters:** Replaces all `input()` calls in Task 1. This is how professional CLI tools accept arguments.

| Resource | Type | Link |
|---|---|---|
| Official `argparse` Documentation | 📄 Docs | https://docs.python.org/3/library/argparse.html |
| `argparse` Tutorial (Gentle Introduction) | 📄 Tutorial | https://docs.python.org/3/howto/argparse.html |

**What to focus on:**
- `ArgumentParser()` — creating the parser
- `add_argument()` — adding positional and optional arguments
- `parse_args()` — reading values from the terminal

---

### 📖 `logging` — Professional Logging Module

> **Why it matters:** Task 2 requires you to replace all `print()` with `logging`. The `LOG_LEVEL` environment variable controls verbosity — a core Twelve-Factor requirement.

| Resource | Type | Link |
|---|---|---|
| Official `logging` Documentation | 📄 Docs | https://docs.python.org/3/library/logging.html |
| Logging HOWTO — Basic & Advanced | 📄 Guide | https://docs.python.org/3/howto/logging.html |
| Logging Cookbook (Practical Examples) | 📄 Cookbook | https://docs.python.org/3/howto/logging-cookbook.html |

**What to focus on:**
- `logging.basicConfig(level=...)` — configuring log level
- `logging.getLogger(__name__)` — module-level loggers
- The difference between `DEBUG`, `INFO`, `WARNING`, `ERROR`
- Reading log level from an environment variable using `os.getenv()`

---

### 📖 Python `Enum` — Safe City Validation

> **Why it matters:** Both tasks require an `Enum` to store the 8 supported cities. If a city isn't in the `Enum`, the app must reject it immediately.

| Resource | Type | Link |
|---|---|---|
| Official `enum` Documentation | 📄 Docs | https://docs.python.org/3/library/enum.html |

**What to focus on:**
- Defining an `Enum` class
- Accessing members by name: `CityEnum['Kathmandu']`
- Catching `KeyError` when an invalid city is passed

---

## 🔐 Section 2: Environment Variables & `.env` Files

> **Why it matters:** Hardcoded URLs are a security risk and violate Twelve-Factor Factor III (Config). You must store all config in environment variables loaded from a `.env` file.

---

### 📖 `python-dotenv`

| Resource | Type | Link |
|---|---|---|
| Official GitHub Repository & README | 📄 Docs | https://github.com/theskumar/python-dotenv |
| PyPI Package Page | 📄 Reference | https://pypi.org/project/python-dotenv/ |

**What to focus on:**
- Creating a `.env` file at the project root
- Using `load_dotenv()` at the top of your application
- Reading variables with `os.getenv("VARIABLE_NAME")`
- **Never committing `.env` to Git** — add it to `.gitignore`

**Quick Example:**
```python
from dotenv import load_dotenv
import os

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")  # default to INFO
```

---

## ✅ Section 3: Pydantic v2 — Data Validation

> **Why it matters:** Every request and response in Task 2 must be a Pydantic `BaseModel`. No raw dicts are allowed. Pydantic is also what FastAPI uses internally for all its validation.

---

### 📖 Official Documentation

| Resource | Type | Link |
|---|---|---|
| Pydantic v2 Official Docs (Latest) | 📄 Docs | https://docs.pydantic.dev/latest/ |
| Pydantic GitHub Repository | 💻 Source | https://github.com/pydantic/pydantic |
| PyPI Package Page | 📦 Package | https://pypi.org/project/pydantic/ |

---

### 🎥 Video Tutorials

| Resource | Channel | Link |
|---|---|---|
| **Pydantic Tutorial — Solving Python's Biggest Problem** (11 min) | Mr. P Solver | https://www.youtube.com/watch?v=XIdQ6gO3Anc |
| **FastAPI + Pydantic Full Tutorial** — covers `BaseModel`, `response_model` | Tech with Tim | https://www.youtube.com/watch?v=cbASjoZZGIw |

---

### 📌 Key Concepts to Master in Pydantic

| Concept | What You Need to Know |
|---|---|
| `BaseModel` | How to define a schema class |
| Type hints | `str`, `float`, `int`, `Optional` |
| `ValidationError` | What happens when bad data is passed |
| Model instantiation | `WeatherRequest(city="Kathmandu")` |
| `.model_dump()` | Serializing a model to a dict |

**Assignment-specific pattern to study:**
```python
from pydantic import BaseModel

class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    temp_c: float
    temp_f: float
    status: str
```

---

## ⚡ Section 4: FastAPI — Building the API

> **Why it matters:** Task 2 requires you to wrap your weather logic inside a FastAPI service with three endpoints: `/health`, `/metrics`, and `/process`.

---

### 📖 Official Documentation

| Resource | Type | Link |
|---|---|---|
| FastAPI Official Documentation | 📄 Docs | https://fastapi.tiangolo.com/ |
| FastAPI Tutorial — User Guide | 📄 Tutorial | https://fastapi.tiangolo.com/tutorial/ |
| FastAPI — Request Body (POST) | 📄 Docs | https://fastapi.tiangolo.com/tutorial/body/ |
| FastAPI — Response Model | 📄 Docs | https://fastapi.tiangolo.com/tutorial/response-model/ |
| FastAPI — HTTP Exceptions | 📄 Docs | https://fastapi.tiangolo.com/tutorial/handling-errors/ |
| FastAPI GitHub Repository | 💻 Source | https://github.com/fastapi/fastapi |

---

### 🎥 Video Tutorials

| Resource | Channel | Duration | Link |
|---|---|---|---|
| **FastAPI Course for Beginners** | freeCodeCamp | ~1 hr | https://www.youtube.com/watch?v=tLKKmouUams |
| **Python FastAPI Tutorial** | Tech with Tim | ~58 min | https://www.youtube.com/watch?v=cbASjoZZGIw |
| **How to Create a Python API with FastAPI** | Tech with Tim | Full | https://www.classcentral.com/course/youtube-how-to-create-a-python-api-with-fastapi-full-tutorial-293449 |

---

### 📌 Key FastAPI Concepts for Your Assignment

| Concept | Where It's Used |
|---|---|
| `@app.get("/health")` | `/health` endpoint |
| `@app.get("/metrics")` | `/metrics` endpoint |
| `@app.post("/process", response_model=WeatherResponse)` | `/process` endpoint |
| `HTTPException(status_code=400, detail="...")` | Invalid city handling |
| `async def` route functions | All endpoints |
| Docstrings with `Args`, `Returns`, `Raises` | All endpoints (required) |

---

## 🦄 Section 5: Uvicorn — The ASGI Server

> **Why it matters:** You must start your FastAPI app using the `uvicorn` CLI — not by hardcoding a port in `main.py`. This is how Twelve-Factor Factor VII (Port Binding) is implemented.

---

### 📖 Official Documentation

| Resource | Type | Link |
|---|---|---|
| Uvicorn Official Documentation | 📄 Docs | https://uvicorn.dev/ |
| Uvicorn Settings Reference | 📄 Reference | https://www.uvicorn.org/settings/ |
| Uvicorn Deployment Guide | 📄 Guide | https://www.uvicorn.org/deployment/ |
| PyPI Package Page | 📦 Package | https://pypi.org/project/uvicorn/ |

---

### 📌 The Startup Command You Must Use

```bash
# ✅ Correct — port bound dynamically via CLI (Twelve-Factor compliant)
uvicorn main:app --reload --port 8080

# ❌ Wrong — hardcoding the port inside main.py violates Factor VII
uvicorn.run(app, port=8000)  # never do this in production
```

**Key CLI flags to understand:**

| Flag | Purpose |
|---|---|
| `--reload` | Auto-restart on code changes (development only) |
| `--port` | Dynamically bind to a port number |
| `--host` | Bind to a host address (`0.0.0.0` for all interfaces) |
| `--log-level` | Set logging verbosity from the command line |

---

## 🌍 Section 6: The Twelve-Factor App Methodology

> **Why it matters:** This is the core philosophy behind **both assignments**. Every architectural decision — `.env` files, port binding, logging levels, no `input()` calls — traces back to one of the twelve factors.

---

### 📖 Official & Reference Resources

| Resource | Type | Link |
|---|---|---|
| **The Twelve-Factor App** — Official Website | 📄 Manifesto | https://12factor.net/ |
| Twelve-Factor — Open Source Repo (Community) | 💻 GitHub | https://github.com/twelve-factor/twelve-factor |
| Red Hat — Illustrated Guide to 12 Factor Apps | 📄 Article | https://www.redhat.com/en/blog/12-factor-app |
| Wikipedia — Twelve-Factor App Methodology | 📄 Overview | https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology |
| DEV Community — Beginner's Guide | 📄 Article | https://dev.to/cadienvan/the-twelve-factor-app-methodology-a-beginners-guide-12m5 |

---

### 📌 The Three Factors Directly Tested in Your Assignments

| Factor | Principle | How It Appears in Your Code |
|---|---|---|
| **Factor III — Config** | Store config in environment variables | API URL and `LOG_LEVEL` in `.env`, loaded via `python-dotenv` |
| **Factor VII — Port Binding** | Export services via port binding | `uvicorn main:app --port 8080` — never hardcoded |
| **Factor X — Dev/Prod Parity** | Keep dev and production as similar as possible | `LOG_LEVEL=DEBUG` in dev, `LOG_LEVEL=INFO` in prod — same codebase |
| **Factor XI — Logs** | Treat logs as event streams | Use `logging` module, never `print()` |

---

### 🎥 Video — Twelve-Factor Explained

| Resource | Channel | Link |
|---|---|---|
| **What is the 12-Factor App?** | IBM Technology | https://www.youtube.com/watch?v=REbM4BDeua0 |

---

## 📦 Section 7: Python Package & Dependency Management

> **Why it matters:** Task 1 requires you to build a proper Python `package` (the `weather/` directory). Task 2 adds new dependencies that must be pinned.

---

### 📖 Virtual Environments & `pip`

| Resource | Type | Link |
|---|---|---|
| Official `venv` Documentation | 📄 Docs | https://docs.python.org/3/library/venv.html |
| pip User Guide | 📄 Guide | https://pip.pypa.io/en/stable/user_guide/ |
| Python Packaging — Official Guide | 📄 Guide | https://packaging.python.org/en/latest/tutorials/packaging-projects/ |

---

### 📌 Pinned `requirements.txt` for This Project

```
# Task 1 dependencies
requests==2.32.3
python-dotenv==1.1.0

# Task 2 additional dependencies
fastapi==0.115.6
uvicorn==0.34.0
pydantic==2.11.4
```

> ⚠️ **Always pin to exact versions.** Unpinned dependencies can break your project silently when a library releases an update.

---

## 🔧 Section 8: Additional Tools & References

---

### 📖 `requests` Library — Making HTTP Calls

> Used in `client.py` (Task 1) and `test_suite.py` (both tasks) to fetch weather data and call your FastAPI endpoints.

| Resource | Type | Link |
|---|---|---|
| Requests Official Documentation | 📄 Docs | https://requests.readthedocs.io/en/latest/ |
| PyPI Package Page | 📦 Package | https://pypi.org/project/requests/ |

---

### 📖 `json` Module — Writing `weather_output.json`

> Used in `test_suite.py` to save structured results.

| Resource | Type | Link |
|---|---|---|
| Official `json` Module Documentation | 📄 Docs | https://docs.python.org/3/library/json.html |

---

### 📖 Python Type Hints — Writing Professional Code

> Used throughout both assignments for Pydantic models and function signatures.

| Resource | Type | Link |
|---|---|---|
| Official `typing` Module Documentation | 📄 Docs | https://docs.python.org/3/library/typing.html |
| PEP 484 — Type Hints Specification | 📄 PEP | https://peps.python.org/pep-0484/ |

---

### 📖 Python Docstrings — Professional Documentation Standard

> Every function and API route requires a docstring with `Summary`, `Args`, `Returns`, and `Raises`.

| Resource | Type | Link |
|---|---|---|
| PEP 257 — Docstring Conventions | 📄 PEP | https://peps.python.org/pep-0257/ |
| Google-Style Python Docstrings Guide | 📄 Guide | https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings |

**Required format for all your functions:**
```python
def convert_c_to_f(temp_c: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        temp_c (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (temp_c * 9 / 5) + 32
```

---

## 🧪 Section 9: Testing Your Work

---

### 📖 Testing FastAPI Endpoints Manually

FastAPI includes an **interactive documentation UI** you can use to test your endpoints without writing any code:

| Tool | URL (when server is running) | Purpose |
|---|---|---|
| **Swagger UI** | `http://127.0.0.1:8080/docs` | Interactive API testing |
| **ReDoc** | `http://127.0.0.1:8080/redoc` | Clean API reference |

---

### 📖 `pytest` — Writing Automated Tests (Bonus)

| Resource | Type | Link |
|---|---|---|
| Official `pytest` Documentation | 📄 Docs | https://docs.pytest.org/en/stable/ |
| FastAPI Testing Guide | 📄 Docs | https://fastapi.tiangolo.com/tutorial/testing/ |

---

## 📋 Quick-Reference Checklist

Use this checklist before submitting your assignments:

### ✅ Task 1 Checklist
- [ ] `weather/models.py` contains an `Enum` with all 8 cities
- [ ] `weather/client.py` handles all HTTP requests — no logic in `main.py`
- [ ] `weather/processor.py` contains `convert_c_to_f()` — importable independently
- [ ] `main.py` uses `argparse` — zero `input()` calls anywhere
- [ ] API URL is in `.env`, loaded via `python-dotenv`
- [ ] `requirements.txt` has pinned versions
- [ ] `test_suite.py` iterates all cities and saves `weather_output.json`

### ✅ Task 2 Checklist
- [ ] `/health` returns a `HealthResponse` Pydantic model
- [ ] `/metrics` returns a `MetricsResponse` with `total_requests` counter
- [ ] `/process` accepts a `WeatherRequest` and returns a `WeatherResponse`
- [ ] Invalid cities return `HTTPException(status_code=400)`
- [ ] All routes use `response_model=` in the decorator
- [ ] All functions have full docstrings (Summary, Args, Returns, Raises)
- [ ] `logging` module used — zero `print()` calls
- [ ] `LOG_LEVEL` is read from `.env`
- [ ] App started with `uvicorn main:app --reload --port 8080`
- [ ] Port is **never** hardcoded in `main.py`

---

## 🎓 Professor's Final Advice

> **Read the official documentation first.** The FastAPI and Pydantic docs are exceptionally well-written with runnable examples on every page. You will find the answer to 90% of your questions there before needing to search anywhere else.

> **Build incrementally.** Get `/health` working first. Then `/metrics`. Then `/process`. Test each one in Swagger UI before moving on.

> **Understand, don't copy.** Every line of code you write should be something you can explain out loud. If you can't explain it, you don't own it yet.

---

*Resource guide prepared for: Nepal Weather CLI & Cloud-Native FastAPI Assignments*
*All links verified as of April 2026*
