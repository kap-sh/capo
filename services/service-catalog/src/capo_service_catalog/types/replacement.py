"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Replacement``."""

from typing import Literal, TypeAlias, cast

Replacement: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "CONDITIONAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Replacement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Replacement:
    return cast(Replacement, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Replacement) -> str:
    return value


def deserialize_cbor(data: str) -> Replacement:
    return cast(Replacement, data)
