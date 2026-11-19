"""Generated from Smithy shape ``com.amazonaws.snowball#RemoteManagement``."""

from typing import Literal, TypeAlias, cast

RemoteManagement: TypeAlias = Literal[
    "INSTALLED_ONLY",
    "INSTALLED_AUTOSTART",
    "NOT_INSTALLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteManagement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemoteManagement:
    return cast(RemoteManagement, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemoteManagement) -> str:
    return value


def deserialize_cbor(data: str) -> RemoteManagement:
    return cast(RemoteManagement, data)
