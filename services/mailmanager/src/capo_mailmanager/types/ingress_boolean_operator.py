"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressBooleanOperator``."""

from typing import Literal, TypeAlias, cast

IngressBooleanOperator: TypeAlias = Literal[
    "IS_TRUE",
    "IS_FALSE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressBooleanOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressBooleanOperator:
    return cast(IngressBooleanOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressBooleanOperator) -> str:
    return value


def deserialize_cbor(data: str) -> IngressBooleanOperator:
    return cast(IngressBooleanOperator, data)
