"""Generated from Smithy shape ``com.amazonaws.snowball#ServiceName``."""

from typing import Literal, TypeAlias, cast

ServiceName: TypeAlias = Literal[
    "KUBERNETES",
    "EKS_ANYWHERE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceName:
    return cast(ServiceName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceName) -> str:
    return value


def deserialize_cbor(data: str) -> ServiceName:
    return cast(ServiceName, data)
