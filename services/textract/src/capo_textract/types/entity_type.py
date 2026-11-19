"""Generated from Smithy shape ``com.amazonaws.textract#EntityType``."""

from typing import Literal, TypeAlias, cast

EntityType: TypeAlias = Literal[
    "KEY",
    "VALUE",
    "COLUMN_HEADER",
    "TABLE_TITLE",
    "TABLE_FOOTER",
    "TABLE_SECTION_TITLE",
    "TABLE_SUMMARY",
    "STRUCTURED_TABLE",
    "SEMI_STRUCTURED_TABLE",
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
