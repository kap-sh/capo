"""Generated from Smithy shape ``com.amazonaws.translate#Directionality``."""

from typing import Literal, TypeAlias, cast

Directionality: TypeAlias = Literal[
    "UNI",
    "MULTI",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Directionality) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Directionality:
    return cast(Directionality, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Directionality) -> str:
    return value


def deserialize_cbor(data: str) -> Directionality:
    return cast(Directionality, data)
