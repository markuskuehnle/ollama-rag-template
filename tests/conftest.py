import pytest
from src.environment.environment import (
    setup_environment,
    teardown_environment,
)


@pytest.fixture(scope="session", autouse=True)
def setup():
    setup_environment()

    yield
    teardown_environment()