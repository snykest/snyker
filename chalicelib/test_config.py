"""
Unit tests for Chalice application
"""
# pylint: disable=C0115,C0116,R0201
# Don't require docstrings for tests
# Allow test classes

import pytest  # type: ignore

from .config import ParameterStoreConfig


class TestConfig:
    @pytest.fixture
    def config(self, ssm):
        ssm.put_parameter(Name="/snyker/VALUE", Value="Gareth", Type="SecureString")
        return ParameterStoreConfig("snyker")

    def test_contains(self, config) -> None:
        assert "VALUE" in config

    def test_contains_false(self, config) -> None:
        assert not "MISSING" in config

    def test_contains_not_string(self, config) -> None:
        assert not {} in config
