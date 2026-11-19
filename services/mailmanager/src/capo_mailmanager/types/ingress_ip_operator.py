"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpOperator``."""

from typing import Literal, TypeAlias, cast

IngressIpOperator: TypeAlias = Literal[
    "CIDR_MATCHES",
    "NOT_CIDR_MATCHES",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressIpOperator:
    return cast(IngressIpOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressIpOperator) -> str:
    return value


def deserialize_cbor(data: str) -> IngressIpOperator:
    return cast(IngressIpOperator, data)
