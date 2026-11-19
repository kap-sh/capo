"""Generated from Smithy shape ``com.amazonaws.directoryservice#SelectiveAuth``."""

from typing import Literal, TypeAlias, cast

SelectiveAuth: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectiveAuth) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SelectiveAuth:
    return cast(SelectiveAuth, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SelectiveAuth) -> str:
    return value


def deserialize_cbor(data: str) -> SelectiveAuth:
    return cast(SelectiveAuth, data)
