"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceFilterName``."""

from typing import Literal, TypeAlias, cast

ServiceFilterName: TypeAlias = Literal[
    "NAMESPACE_ID",
    "RESOURCE_OWNER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceFilterName:
    return cast(ServiceFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> ServiceFilterName:
    return cast(ServiceFilterName, data)
