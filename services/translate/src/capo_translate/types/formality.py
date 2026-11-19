"""Generated from Smithy shape ``com.amazonaws.translate#Formality``."""

from typing import Literal, TypeAlias, cast

Formality: TypeAlias = Literal[
    "FORMAL",
    "INFORMAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Formality) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Formality:
    return cast(Formality, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Formality) -> str:
    return value


def deserialize_cbor(data: str) -> Formality:
    return cast(Formality, data)
