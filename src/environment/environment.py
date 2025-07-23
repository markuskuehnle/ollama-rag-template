import logging
import sys
from pathlib import Path

from src.config import AppConfig
from src.environment.ollama import start_ollama

# Get the project root directory (parent of src)
project_root = Path(__file__).parent.parent.parent
app_config = AppConfig(str(project_root / "config" / "application.conf"))


FORMAT = "[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)s]: %(message)s"
logging.basicConfig(stream=sys.stdout, format=FORMAT, level=logging.INFO)

logger = logging.getLogger(__name__)

curr_dir = str(Path(__file__).parent)


def setup_environment():
    try:
        logger.info("Setup test environment")

        # 1. Start the embedding model with ollama
        ollama_embedding = start_ollama(
            model_name=app_config.embedding_llm.model_name,
            port=11434,
            cache_dir="ollama_cache_embedding",
            container_name="ollama-embedding",
        )

        # 2. Start the generative model with ollama
        ollama_generative = start_ollama(
            model_name=app_config.generative_llm.model_name,
            port=11435,
            cache_dir="ollama_cache_generative",
            container_name="ollama-generative",
        )

        return ollama_embedding, ollama_generative
    except Exception as e:
        logger.error(f"Error setting up environment: {e}")
        raise e


def teardown_environment():
    logging.info("Tearing down the test environment, nothing do to")
