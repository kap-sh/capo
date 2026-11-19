"""Generated from Smithy shape ``com.amazonaws.appstream#Permission``."""

from typing import Literal, TypeAlias, cast

Permission: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Permission) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Permission:
    return cast(Permission, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Permission) -> str:
    return value


def deserialize_cbor(data: str) -> Permission:
    return cast(Permission, data)
