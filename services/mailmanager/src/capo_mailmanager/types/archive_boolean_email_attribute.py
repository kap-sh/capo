"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveBooleanEmailAttribute``."""

from typing import Literal, TypeAlias, cast

ArchiveBooleanEmailAttribute: TypeAlias = Literal["HAS_ATTACHMENTS",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveBooleanEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveBooleanEmailAttribute:
    return cast(ArchiveBooleanEmailAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArchiveBooleanEmailAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> ArchiveBooleanEmailAttribute:
    return cast(ArchiveBooleanEmailAttribute, data)
