# Demo LangGraph Tutorial

A hands-on walkthrough for building advanced, stateful AI agents using **LangGraph** — from basic chatbot to memory, tools, human-in-the-loop, and time-travel.
It integrates with **LangSmith** for monitoring telemetry data.

---

# Why LangGraph?
LangGraph lets you build stateful, event-driven agents as directed graphs — offering:
- Durable, resumable execution
- Built-in memory and context management
- Human-in-the-loop interaction
- Seamless LangChain & LangSmith integration
- “Time-travel” debugging and observability

---

## ⚡ Getting Started with `uv`

[`uv`](https://github.com/astral-sh/uv) is a super-fast Python package manager. Here's how to set things up using `uv`:

### 1. 📦 Install `uv` (if not already installed)

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Or use the following if you're on macOS with Homebrew
```bash
brew install astral-sh/uv/uv
```

### 2. Clone the repository
```bash
git clone https://github.com/toashishagarwal/demo-langgraph-tutorial.git
cd demo-langgraph-tutorial
```

### 3. Create a virtual environment
```bash
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 4. Install dependencies using uv
```bash
uv pip install -r requirements.txt
```

### 4. OR use following to add dependencies using uv
```bash
uv add langgraph langsmith google-generativeai python-dotenv pillow langchain-google_genai
```

Happy graphing! 🧠🔄📈


