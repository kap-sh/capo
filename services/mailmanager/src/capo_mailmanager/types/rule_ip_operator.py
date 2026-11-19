"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIpOperator``."""

from typing import Literal, TypeAlias, cast

RuleIpOperator: TypeAlias = Literal[
    "CIDR_MATCHES",
    "NOT_CIDR_MATCHES",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleIpOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleIpOperator:
    return cast(RuleIpOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleIpOperator) -> str:
    return value


def deserialize_cbor(data: str) -> RuleIpOperator:
    return cast(RuleIpOperator, data)
