"""Generated from Smithy shape ``com.amazonaws.pi#ContextType``."""

from typing import Literal, TypeAlias, cast

ContextType: TypeAlias = Literal[
    "CAUSAL",
    "CONTEXTUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContextType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContextType:
    return cast(ContextType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContextType) -> str:
    return value


def deserialize_cbor(data: str) -> ContextType:
    return cast(ContextType, data)
