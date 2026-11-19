"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceFilterName``."""

from typing import Literal, TypeAlias, cast

NamespaceFilterName: TypeAlias = Literal[
    "TYPE",
    "NAME",
    "HTTP_NAME",
    "RESOURCE_OWNER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NamespaceFilterName:
    return cast(NamespaceFilterName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NamespaceFilterName) -> str:
    return value


def deserialize_cbor(data: str) -> NamespaceFilterName:
    return cast(NamespaceFilterName, data)
