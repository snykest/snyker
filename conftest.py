"""
Configuration for pytest fixtures
"""

import pytest  # type: ignore
from chalice import Chalice  # type: ignore

from app import app as chalice_app


@pytest.fixture
def app() -> Chalice:
    """Return the application for testing"""
    return chalice_app
