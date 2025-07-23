# Dockerized Ollama Template

A comprehensive template for running Ollama in Docker containers with automated testing and local development support. This project provides a complete setup for RAG (Retrieval-Augmented Generation) applications with both embedding and generative models.

## Quick Start

### Prerequisites
- Python 3.10+
- Docker
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/markuskuehnle/ollama-rag-template
   cd dockerized-ollama-template
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Run tests (Docker-based):**
   ```bash
   python3 -m pytest --capture=no tests
   ```

## Project Structure

```
dockerized-ollama-template/
├── config/
│   ├── application.conf          # Configuration
├── src/                          # Source code
│   ├── __init__.py
│   ├── config.py                 # Configuration management
│   └── environment/              # Environment setup
│       ├── __init__.py
│       ├── environment.py        # Container orchestration
│       └── ollama.py             # Ollama container management
├── config/
│   └── application.conf          # HOCON configuration file
├── tests/
│   ├── conftest.py               # Pytest fixtures
│   └── test_conftest_healthcheck.py  # Health check tests
├── notebooks/                    # Jupyter notebooks
│   ├── 01_dockerized_ollama.ipynb    # Docker-based setup
│   └── 02_local_ollama.ipynb         # Local Ollama setup
├── src/data/                     # Model cache directories
│   ├── ollama_cache_embedding/
│   └── ollama_cache_generative/
└── pyproject.toml                # Project configuration
```

## Configuration

The project uses HOCON configuration in `config/application.conf`:

```hocon
embedding_llm {
    url = "http://127.0.0.1:11434"
    model_name = "mxbai-embed-large:latest"
    api_type = "ollama"
    vector_length = 1024
}

generative_llm {
    url = "http://127.0.0.1:11435"
    model_name = "llama3.1:8b"
}
```

### Models
- **Embedding Model**: `mxbai-embed-large:latest` - Creates vector embeddings for document retrieval
- **Generative Model**: `llama3.1:8b` - Generates text responses

## Docker-Based Setup (Recommended)

### Automated Testing
The test suite automatically manages Docker containers:

```bash
# Run all tests
python3 -m pytest --capture=no tests

# Run specific test
python3 -m pytest tests/test_conftest_healthcheck.py -v
```

### How it works
1. **Container Setup**: `tests/conftest.py` automatically starts two Ollama containers
2. **Health Checks**: Tests verify both containers are running and models are available
3. **Cleanup**: Containers are automatically stopped after tests complete

### Container Details
- **Embedding Container**: `ollama-embedding` on port 11434
- **Generative Container**: `ollama-generative` on port 11435
- **Memory**: 8GB per container
- **Image**: `ollama/ollama:0.5.13`

## Local Development

### Option 1: Docker-Based Notebook
Use `notebooks/01_dockerized_ollama.ipynb` for Docker-based development:

```python
# The notebook automatically:
# 1. Sets up Docker containers
# 2. Loads configuration
# 3. Tests both models
# 4. Provides example usage
```

### Option 2: Local Ollama Setup
Use `notebooks/02_local_ollama.ipynb` for local Ollama installation:

**Prerequisites:**
```bash
# Install Ollama locally
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama service
ollama serve
```

**Usage:**
```python
# The notebook automatically:
# 1. Checks if Ollama is running
# 2. Pulls required models
# 3. Tests both embedding and generation
# 4. Provides chat functionality
```

## Testing

### Test Structure
- **`conftest.py`**: Session-scoped fixtures for container lifecycle
- **`test_conftest_healthcheck.py`**: Verifies container setup and model availability

### Running Tests
```bash
# Run with verbose output
python3 -m pytest --capture=no tests

# Run specific test
python3 -m pytest tests/test_conftest_healthcheck.py -v -s

# Run with coverage
python3 -m pytest --cov=src tests/
```

## Notebook Examples

### 01_dockerized_ollama.ipynb
**Purpose**: Docker-based development environment
- Automatic container management
- Isolated environment
- No local Ollama installation required
- Perfect for CI/CD and reproducible environments

### 02_local_ollama.ipynb
**Purpose**: Local development with Ollama
- Uses local Ollama installation
- Faster startup (no Docker overhead)
- Direct access to local models
- Good for development and experimentation

## Development

### Adding New Models
1. Update `config/application.conf` with new model names
2. Modify `src/environment/environment.py` if additional containers needed
3. Update tests to verify new models

### Customizing Configuration
- Edit `config/application.conf` for model changes
- Modify `src/config.py` for new configuration fields
- Update container settings in `src/environment/ollama.py`

### Extending Functionality
- Add new endpoints in `src/`
- Create additional notebooks for specific use cases
- Extend test coverage for new features

## Troubleshooting

### Common Issues

**Container fails to start:**
```bash
# Check Docker is running
docker ps

# Check available memory (containers need 8GB each)
docker system info
```

**Import errors:**
```bash
# Ensure you're in the virtual environment
source .venv/bin/activate

# Check Python path includes src
python -c "import src.config; print('OK')"
```

**Model pull fails:**
```bash
# Check internet connection
# Verify model names in config/application.conf
# Check Ollama logs: docker logs <container-name>
```

---

**Happy coding! 🚀**

