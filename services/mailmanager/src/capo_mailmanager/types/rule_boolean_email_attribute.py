"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleBooleanEmailAttribute``."""

from typing import Literal, TypeAlias, cast

RuleBooleanEmailAttribute: TypeAlias = Literal[
    "READ_RECEIPT_REQUESTED",
    "TLS",
    "TLS_WRAPPED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleBooleanEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleBooleanEmailAttribute:
    return cast(RuleBooleanEmailAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleBooleanEmailAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> RuleBooleanEmailAttribute:
    return cast(RuleBooleanEmailAttribute, data)
