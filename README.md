# agent-learn-1

A small learning project for experimenting with [LangChain](https://python.langchain.com/) and LLM-backed agents, using [DeepInfra](https://deepinfra.com/) as the model provider.

## Overview

The current example (`src/agent_learn_1/app.py`) sets up a DeepInfra chat model (`openai/gpt-oss-20b`) and sends it a short English-to-French translation conversation.

## Requirements

- Python >= 3.14
- A [DeepInfra](https://deepinfra.com/) API key

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Create a `.env` file in the project root with your DeepInfra API key:

   ```
   DEEPINFRA_API_TOKEN=your_api_key_here
   ```

## Usage

Run the app with:

```bash
uv run agent-learn-1
```

## Project Structure

```
pyproject.toml
README.md
src/
    agent_learn_1/
        __init__.py
        app.py
```
