"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceAttribute``."""

from typing import Literal, TypeAlias, cast

ResourceAttribute: TypeAlias = Literal[
    "PROPERTIES",
    "METADATA",
    "CREATIONPOLICY",
    "UPDATEPOLICY",
    "DELETIONPOLICY",
    "TAGS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceAttribute:
    return cast(ResourceAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceAttribute:
    return cast(ResourceAttribute, data)
