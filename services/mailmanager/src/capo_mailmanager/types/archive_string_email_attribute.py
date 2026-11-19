"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveStringEmailAttribute``."""

from typing import Literal, TypeAlias, cast

ArchiveStringEmailAttribute: TypeAlias = Literal[
    "TO",
    "FROM",
    "CC",
    "SUBJECT",
    "ENVELOPE_TO",
    "ENVELOPE_FROM",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveStringEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveStringEmailAttribute:
    return cast(ArchiveStringEmailAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArchiveStringEmailAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> ArchiveStringEmailAttribute:
    return cast(ArchiveStringEmailAttribute, data)
