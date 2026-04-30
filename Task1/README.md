# 🏔️ Operation: CloudScale Nepal Rescue Mission
## 📉 The Situation
It is 4:30 PM on a Friday. You just received an urgent Slack message from the CTO.

One of our junior developers, Ramesh, has just left the company for a "better opportunity." He was working on our core Nepal Weather Utility, which is supposed to provide live data for our high-end trekking agency partners.

The problem? Ramesh wrote the code as a single, messy "spaghetti" script. Everest Treks Ltd. wants to import our weather logic into their new mobile app today, but they can't because:

The code starts an infinite loop and asks for user input immediately—you can't use it as a library.

The API URL is hardcoded directly in the logic.

The logic and the UI are so tangled that you can't get the temperature calculation without the script printing a bunch of unorganized text to the console.

### 🎯 Your Mission
You have been tasked to "clean the mess." You need to take Ramesh's weather_script.py and turn it into a professional, modular Python package that a high-end client would actually trust.

### 🛠️ The Technical "Orders"
To satisfy the CTO and keep our clients happy, your refactored solution must meet these professional standards:

The "Safety Net" (Enums): CloudScale only has a license to provide data for 8 specific cities. You must use a Python Enum to store these cities and their coordinates. If a user asks for a city we don't own, reject it immediately with a clean error message.

The "Secret Box" (.env): Remove all hardcoded URLs. Use a .env file and python-dotenv. We don't want our infrastructure details leaked!

The "Surgical Split" (Modularity): Break the script into a package named weather/:

- models.py: The Enums and city data structures.

- client.py: The logic for handling network requests.

- processor.py: The pure logic (C to F conversion) and report data formatting.

- The "Bridge" (main.py): This is your entry point. It should use argparse to handle inputs.

No More Talking Back: Replace all input() calls. Our partners want to run this from a terminal command or a script, not an interactive chat box.



### 🏆 Scoring Rubric (20 Points)
<img width="921" height="495" alt="image" src="https://github.com/user-attachments/assets/2cb02bd5-e399-4eaa-a1a8-ef187cfce32a" />


### Getting Started
Review the "Legacy" code in weather_script.py.

#### Install requirements: pip install requests python-dotenv.

#### Start splitting the logic. Remember: Ramesh is gone, the clock is ticking, and the CTO is watching!

#### 💡 Pro-Tip for Success
A good engineer builds code that other engineers love to use. If I run from weather.processor import convert_c_to_f, I should be able to convert temperatures in my own script without your whole program running.

#### 🛑 Appendix: The Legacy Code (weather_script.py)
For reference, this is the code you are destroying to build something better.



# 💻 Phase 2: Professional Workflow (Setup)

# 🌤️ Weather CLI Tool

A modular, production-ready command-line weather application built in Python. Fetches and processes weather data for supported cities with clean architecture, proper dependency management, and automated testing.

---

## 📁 Project Structure

```
weather-cli/
├── weather/
│   ├── __init__.py
│   ├── client.py          # API communication layer
│   └── processor.py       # Data processing & transformation
├── main.py                # CLI entry point
├── test_suite.py          # Automated test runner
├── requirements.txt       # Pinned dependencies
└── README.md
```

---

## 💻 Phase 2: Environment Setup

### Prerequisites

- Python **3.9+** installed on your system
- `pip` available in your PATH

---

### 🐧 Linux / 🍎 macOS

**1. Create the virtual environment**
```bash
python3 -m venv venv
```

**2. Activate the virtual environment**
```bash
source venv/bin/activate
```

**3. Confirm activation** — your terminal prompt should show `(venv)`
```bash
which python
# Expected: /path/to/project/venv/bin/python
```

**4. Deactivate when done**
```bash
deactivate
```

---

### 🪟 Windows

**1. Create the virtual environment**
```cmd
python -m venv venv
```

**2. Activate the virtual environment**

- **Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

- **PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

> ⚠️ If you encounter a PowerShell execution policy error, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**3. Confirm activation** — your prompt should show `(venv)`
```cmd
where python
# Expected: C:\path\to\project\venv\Scripts\python.exe
```

**4. Deactivate when done**
```cmd
deactivate
```

---

## 📦 Dependency Management

All dependencies are **pinned to exact versions** in `requirements.txt` to guarantee reproducibility across environments.

### ✅ Correct — Pinned versions
```
requests==2.31.0
```

### ❌ Incorrect — Unpinned versions
```
requests
```

> Unpinned dependencies risk silent breaking changes when libraries release updates.

---

### Installing Dependencies

With your virtual environment **activated**, run:

```bash
pip install -r requirements.txt
```

**Verify installation**
```bash
pip list
```

**Freeze current environment** (if adding new packages)
```bash
pip freeze > requirements.txt
```

---

## 🚀 Phase 3: Execution & Testing

The application runs entirely as a **command-line tool** — no interactive input required.

### Running the Application

**With a supported city:**
```bash
python main.py Kathmandu
```

**Expected output:**
```
✅ Weather for Kathmandu:
   Temperature : 22°C
   Condition   : Partly Cloudy
   Humidity    : 65%
```

---

**With an unsupported city:**
```bash
python main.py London
```

**Expected output:**
```
❌ Error: 'London' is not a supported city.
   Supported cities: Kathmandu, ...
```

> The system returns a clear, descriptive error message for any city not defined in the supported cities Enum.

---

## 🧪 Phase 4: Automation — Test Suite

`test_suite.py` automates weather data fetching and processing across **all supported cities** and exports structured results.

### What it does

- Imports `weather.client` and `weather.processor` directly
- Iterates over every city defined in the supported cities `Enum`
- Fetches and processes weather data for each city
- Saves all results to **`weather_output.json`**

### Running the Test Suite

```bash
python test_suite.py
```

**Expected output:**
```
Running weather test suite...
  ✅ Kathmandu — OK
  ✅ [city]    — OK
  ...
Results saved → weather_output.json
```

### Output Format — `weather_output.json`

```json
{
  "Kathmandu": {
    "temperature": 22,
    "condition": "Partly Cloudy",
    "humidity": 65,
    "fetched_at": "2025-04-30T10:30:00Z"
  }
}
```

---

## 🎯 Design Principles

| Principle | Implementation |
|---|---|
| **Modular architecture** | `client.py` handles I/O, `processor.py` handles logic |
| **Environment isolation** | Virtual environment per project |
| **Reproducible builds** | All dependencies pinned in `requirements.txt` |
| **CLI-first** | No interactive prompts — arguments only |
| **Automation-ready** | `test_suite.py` runs all cities end-to-end |
| **Clear error handling** | Unsupported cities return descriptive messages |

---

## 🔧 Development Workflow

```bash
# 1. Clone the repository
git clone 
cd weather-cli

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate          # Linux/macOS
# venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python main.py Kathmandu

# 5. Run the test suite
python test_suite.py
```

---

## 📄 License

This project is intended for evaluation and educational purposes.
