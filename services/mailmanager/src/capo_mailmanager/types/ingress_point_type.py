"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointType``."""

from typing import Literal, TypeAlias, cast

IngressPointType: TypeAlias = Literal[
    "OPEN",
    "AUTH",
    "MTLS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressPointType:
    return cast(IngressPointType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressPointType) -> str:
    return value


def deserialize_cbor(data: str) -> IngressPointType:
    return cast(IngressPointType, data)
