"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressStringOperator``."""

from typing import Literal, TypeAlias, cast

IngressStringOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressStringOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressStringOperator:
    return cast(IngressStringOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressStringOperator) -> str:
    return value


def deserialize_cbor(data: str) -> IngressStringOperator:
    return cast(IngressStringOperator, data)
