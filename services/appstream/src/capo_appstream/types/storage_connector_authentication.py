"""Generated from Smithy shape ``com.amazonaws.appstream#StorageConnectorAuthentication``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether users' cloud storage authentication persists across streaming sessions.</p>"""
StorageConnectorAuthentication: TypeAlias = Literal[
    "FORCE_REAUTHENTICATION",
    "REUSE_CREDENTIALS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnectorAuthentication) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageConnectorAuthentication:
    return cast(StorageConnectorAuthentication, data)
