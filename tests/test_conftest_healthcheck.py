import pytest
import requests
from typing import Dict, Any


def test_conftest_setup_and_ollama_healthcheck():
    """Test that conftest.py properly sets up Ollama containers and they respond to healthchecks."""
    
    # Test healthcheck for generative model (port 11435)
    generative_healthcheck_response = requests.get("http://127.0.0.1:11435/api/tags")
    assert generative_healthcheck_response.status_code == 200
    
    generative_models: Dict[str, Any] = generative_healthcheck_response.json()
    assert "models" in generative_models
    
    # Verify the generative model is available
    generative_model_names = [model["name"] for model in generative_models["models"]]
    assert "llama3.1:8b" in generative_model_names 