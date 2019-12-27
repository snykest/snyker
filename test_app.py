"""
Unit tests for Chalice application
"""
# pylint: disable=C0116
# Don't require docstrings for tests
import os
from http import HTTPStatus

from pytest_chalice.handlers import RequestHandler  # type: ignore


def test_index(client: RequestHandler, ssm) -> None:
    ssm.put_parameter(Name="/snyker/VALUE", Value="Gareth", Type="SecureString")
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"hello": "Gareth"}


def test_mp() -> None:
    assert os.getenv("AWS_ACCESS_KEY_ID") == "testing"
