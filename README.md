# Dockerized Ollama Template

A template project for running Ollama in Docker containers with automated testing.

## Setup

1. Install dependencies using uv:
   ```bash
   uv sync
   ```

2. Execute tests:
   ```bash
   python3 -m pytest --capture=no tests
   ```

## How it works

The test suite automatically creates Docker containers with Ollama using the configuration in `config/application.conf`. The setup includes:

- **Embedding model**: `mxbai-embed-large:latest` (port 11434)
- **Generative model**: `llama3.1:8b` (port 11435)

The containers are managed by pytest fixtures in `tests/conftest.py` and are automatically started before tests run and cleaned up afterward.

