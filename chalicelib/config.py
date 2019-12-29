"""
Helpers for configuration management with AWS Systems Manager Parameter store
"""

import boto3  # type: ignore
from botocore.exceptions import ClientError  # type: ignore


class ParameterStoreConfig(dict):
    """
    A facade for accessing prefixed configuration variables from
    AWS Systems Manager Parameter Store
    """

    def __init__(self, prefix: str):
        dict.__init__(self, {})
        self.client = boto3.client("ssm")
        self.prefix = prefix

    def get(self, key):
        name = f"/{self.prefix}/{key}"
        response = self.client.get_parameters(Names=[name], WithDecryption=True)
        try:
            return response["Parameters"][0]["Value"]
        except IndexError:
            raise KeyError

    def __contains__(self, name: object) -> bool:
        if not isinstance(name, str):
            return False
        try:
            self.get(name)
            return True
        except (KeyError, ClientError):
            return False

    def __getitem__(self, name: str) -> str:
        return self.get(name)

    def __setitem__(self, key: str, value: str):
        raise NotImplementedError()  # pragma: no cover

    def __delitem__(self, name: str):
        raise NotImplementedError()  # pragma: no cover
