"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityType``."""

from typing import Literal, TypeAlias, cast

EntityType: TypeAlias = Literal[
    "PERSON",
    "LOCATION",
    "ORGANIZATION",
    "COMMERCIAL_ITEM",
    "EVENT",
    "DATE",
    "QUANTITY",
    "TITLE",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityType:
    return cast(EntityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityType) -> str:
    return value


def deserialize_cbor(data: str) -> EntityType:
    return cast(EntityType, data)
