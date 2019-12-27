"""
Unit tests for Chalice application
"""
# pylint: disable=C0116
from http import HTTPStatus

from pytest_chalice.handlers import RequestHandler  # type: ignore


def test_index(client: RequestHandler) -> None:
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json == {"hello": "Gareth"}
