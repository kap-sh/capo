"""Generated from Smithy shape ``com.amazonaws.shield#Unit``."""

from typing import Literal, TypeAlias, cast

Unit: TypeAlias = Literal[
    "BITS",
    "BYTES",
    "PACKETS",
    "REQUESTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Unit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Unit:
    return cast(Unit, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Unit) -> str:
    return value


def deserialize_cbor(data: str) -> Unit:
    return cast(Unit, data)
