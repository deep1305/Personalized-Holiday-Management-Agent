# 🌴 Personalized Holiday Management Agent

An AI-powered holiday planning assistant that generates personalized destination options, itineraries, budget splits, and practical travel cautions using a two-agent workflow.

It supports a hybrid model strategy:
- **Local development** -> Ollama (Gemma4)
- **Cloud deployment (Render)** -> OpenAI models

## 🔗 Repository

- GitHub: [deep1305/Personalized-Holiday-Management-Agent](https://github.com/deep1305/Personalized-Holiday-Management-Agent.git)

## 🌟 Features

- **Multi-Agent Planning Flow**: Planner + Researcher agents collaborate in sequence
- **Personalized Itineraries**: Destination options based on budget, trip duration, and preferences
- **Research Validation Layer**: Adds weather/visa uncertainty cautions and booking heuristics
- **FastAPI Web App**: Clean browser UI with form-based input
- **Modern Frontend UX**:
  - Markdown-rendered AI output
  - Copy and download plan buttons
  - Dark mode toggle with persistence
- **Environment-Aware LLM Selection**:
  - Local -> Ollama
  - Render -> OpenAI

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Agent Framework**: AutoGen AgentChat (`autogen-agentchat`)
- **Model Providers**:
  - Ollama (`autogen-ext[ollama]`)
  - OpenAI (`autogen-ext[openai]`)
- **Templating**: Jinja2
- **Frontend**: HTML, CSS, vanilla JavaScript
- **Language**: Python 3.12+

## 📁 Project Structure

```text
Personalized-Holiday-Management-Agent/
├── app.py
├── main.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── Personalized_Holiday_Management/
    ├── agents/
    │   ├── planner.py
    │   └── researcher.py
    ├── teams/
    │   └── holiday_team.py
    ├── models/
    │   ├── __init__.py       # model selector (auto/openai/ollama)
    │   ├── gpt_model.py
    │   └── ollama_model.py
    ├── config/
    │   └── settings.py
    └── utils/
        └── utils.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- For local LLM mode: Ollama installed and running
- For cloud mode: OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/deep1305/Personalized-Holiday-Management-Agent.git
   cd "Personalized-Holiday-Management-Agent"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   # Required for cloud/OpenAI mode
   OPENAI_API_KEY=your_openai_api_key

   # Optional model override
   OPENAI_MODEL=gpt-4o-mini

   # Local Ollama settings (defaults shown)
   OLLAMA_BASE_URL=http://localhost:11434
   OLLAMA_MODEL=gemma4:26b-a4b-it-q4_K_M

   # Optional provider control: auto | ollama | openai
   MODEL_PROVIDER=auto
   ```

## 💡 Model Selection Behavior

The app chooses model provider from `MODEL_PROVIDER`:

- `MODEL_PROVIDER=ollama` -> always Ollama
- `MODEL_PROVIDER=openai` -> always OpenAI
- `MODEL_PROVIDER=auto` (default):
  - **Render detected** -> OpenAI
  - **Local environment** -> Ollama

This behavior is implemented in `Personalized_Holiday_Management/models/__init__.py`.

## ▶️ Run the App

### Web UI (recommended)

```bash
python -m uvicorn app:app --reload
```

Open: `http://127.0.0.1:8000`

### CLI quick test

```bash
python main.py
```

## 🧪 Quick Test Input

Use this in the web form:

- Month: `June`
- Duration: `7`
- Group Size: `2`
- Budget: `CAD 3000`
- Preferences: `mountains + sea, easy pace`
- Notes: `vegetarian food preferred`

Expected behavior:
- `holiday_planner` responds first
- `holiday_researcher` validates and finalizes
- final output includes `TERMINATE`

## ☁️ Render Deployment

Create a **Web Service** on Render (not Static Site), then use:

- **Build Command**
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command**
  ```bash
  uvicorn app:app --host 0.0.0.0 --port $PORT
  ```

### Render Environment Variables

Minimum:

```env
OPENAI_API_KEY=your_openai_api_key
```

Recommended explicit setup:

```env
MODEL_PROVIDER=openai
OPENAI_MODEL=gpt-4o-mini
OPENAI_API_KEY=your_openai_api_key
```

## 📊 How It Works

1. **User Input**: Trip constraints submitted via UI (`/plan-trip`)
2. **Planner Agent**: Proposes destination options, itineraries, and budget split
3. **Researcher Agent**: Adds validation, cautions, and booking-window heuristics
4. **Termination Condition**: Team stops when `TERMINATE` appears
5. **UI Rendering**: Output shown as markdown with copy/download actions

## 🙏 Notes

- Ollama is ideal for local/offline-ish development.
- Render cannot host local Ollama by default, so cloud mode should use OpenAI.
- During `--reload`, in-flight requests may be interrupted if files change.

---

**Built for practical, personalized holiday planning.**
