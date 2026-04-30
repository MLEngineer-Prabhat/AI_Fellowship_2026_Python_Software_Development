# 🌐 Problem 2: The Cloud-Native Weather Engine

## 📉 The Situation: From Script to Service

The CTO is impressed with your refactor of Ramesh's code! But there's a catch: **Everest Treks Ltd.** wants a **Live API** they can call from their mobile app.

Your mission: Wrap your modular weather package into a **FastAPI Microservice**. It must be **Cloud-Native**, meaning it is:

- 🔍 **Observable** — structured logging
- 📈 **Scalable** — dynamic port binding
- 🔒 **Strictly typed** — enforced via Pydantic

---

## 🎯 The Mission

> Build a **production-ready FastAPI service** that is **Twelve-Factor App** compliant and uses **Strict Schema Validation**.

---

## 🛠️ Technical Constraints — The CTO's "Must-Haves"

### ⚙️ Factor VII — Port Binding

Your startup command **must not hardcode** `port 8000`. Use the `uvicorn` CLI to bind the port **dynamically**.

### 📋 Factor X — Dev/Prod Parity (Logging Level)

Use the `logging` module — **no `print()` statements**. The log level **must be configurable** via a `LOG_LEVEL` environment variable.

### 🔒 Strict Pydantic Enforcement

| Requirement | Rule |
|---|---|
| **Request Models** | Define a `BaseModel` for all incoming JSON |
| **Response Models** | Use `response_model` parameter in every decorator |
| **No "Naked" Dicts** | Every endpoint must return a **Pydantic object** or a **list of Pydantic objects** |

### 📝 Strict Documentation

Every **function** and **API route** must include a professional **Docstring** with:
- `Summary`
- `Args`
- `Returns`

---

## 🏗️ API Design & Schema Requirements

| Endpoint | Method | Purpose | Response Model |
|---|---|---|---|
| `/health` | `GET` | Health Check | `HealthResponse` — `status: str` |
| `/metrics` | `GET` | Monitoring | `MetricsResponse` — `total_requests: int` |
| `/process` | `POST` | Weather Logic | `WeatherResponse` — `city, temp_c, temp_f, status` |

> ⚠️ **Validation Rule:** If a city is **not** in your `Enum`, catch the `KeyError` and return a **`400 Bad Request`** using `HTTPException`.

---

## 📋 Scoring Rubric — 35 Points

| Criteria | Points | Requirement |
|---|---|---|
| **Port Binding** | 5 | App successfully starts on a custom port via CLI |
| **Log Level Config** | 5 | `LOG_LEVEL` in `.env` correctly toggles `DEBUG` vs `INFO` logs |
| **Pydantic Schemas** | 10 | Full use of `BaseModel` for both Request and Response validation |
| **Observability** | 5 | `/health` and `/metrics` (request counter) are functional |
| **Logic & Validation** | 10 | `/process` uses the `Enum` and returns `400` for invalid cities |

---

## 📝 Pydantic & Docstring Standard

> **Students must follow this exact pattern for the `/process` endpoint.**

### Schema Definitions

```python
class WeatherRequest(BaseModel):
    city: str

class WeatherResponse(BaseModel):
    city: str
    temp_c: float
    temp_f: float
    status: str
```

### Endpoint Implementation

```python
@app.post("/process", response_model=WeatherResponse)
async def process_weather(payload: WeatherRequest):
    """
    Validates city input and retrieves current weather data.

    Args:
        payload (WeatherRequest): A Pydantic model containing the city name.

    Returns:
        WeatherResponse: A validated Pydantic model containing the processed report.

    Raises:
        HTTPException: 400 error if the city is not supported.
    """
    # Your logic here...
```

---

## 🧪 The Final Boss: Automation Challenge

Create `test_suite.py`. It **must**:

1. Loop through **all 8 cities** in your `Enum`
2. Make a `POST` request to your FastAPI server for each city
3. Collect all responses and store them in **`weather_output.json`**

### Expected Output — `weather_output.json`

```json
{
  "Kathmandu": {
    "city": "Kathmandu",
    "temp_c": 22.0,
    "temp_f": 71.6,
    "status": "Partly Cloudy"
  }
}
```

---

## 💻 Professional Workflow

### 📦 Dependencies

Ensure the following are listed with **pinned versions** in `requirements.txt`:

```
fastapi==<version>
uvicorn==<version>
pydantic==<version>
python-dotenv==<version>
requests==<version>
```

### 🚀 Startup Command

Run on **port 8080** with **auto-reload** enabled:

```bash
uvicorn main:app --reload --port 8080
```

> 💡 **Pro Tip:** The port must **never** be hardcoded inside `main.py`. Always bind it from the CLI or an environment variable to stay Twelve-Factor compliant.

---

## 🎯 Design Principles

| Principle | Implementation |
|---|---|
| **Port Binding** | Dynamic port via `uvicorn` CLI — no hardcoded values |
| **Configurable Logging** | `LOG_LEVEL` env variable controls verbosity |
| **Strict Typing** | Pydantic `BaseModel` on all inputs and outputs |
| **Observability** | `/health` and `/metrics` endpoints for monitoring |
| **Clean Error Handling** | `HTTPException` with `400` for unsupported cities |
| **Automation-Ready** | `test_suite.py` runs all cities and exports JSON |

---

## 📄 License

This project is intended for evaluation and educational purposes.
