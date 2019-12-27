"""
Configuration for pytest fixtures
"""

# pylint: disable=C0415
# Allow inports outside toplevel to ensure mocked AWS environment vars are used

import boto3  # type: ignore
import pytest  # type: ignore
from chalice import Chalice  # type: ignore
from moto import mock_ssm  # type: ignore


@pytest.fixture
def app() -> Chalice:
    """Return the application for testing"""
    from app import app as chalice_app

    return chalice_app


@pytest.fixture(autouse=True)
def mocked_aws_credentials(monkeypatch):
    """Mocked AWS Credentials for moto."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch.setenv("AWS_SECURITY_TOKEN", "testing")
    monkeypatch.setenv("AWS_SESSION_TOKEN", "testing")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "eu-west-1")

    boto3.setup_default_session()


@pytest.fixture(scope="function")
def ssm():
    """Mock for AWS Systems Manager"""
    with mock_ssm():
        yield boto3.client("ssm")
