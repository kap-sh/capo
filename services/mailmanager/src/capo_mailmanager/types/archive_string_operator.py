"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveStringOperator``."""

from typing import Literal, TypeAlias, cast

ArchiveStringOperator: TypeAlias = Literal["CONTAINS",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveStringOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveStringOperator:
    return cast(ArchiveStringOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArchiveStringOperator) -> str:
    return value


def deserialize_cbor(data: str) -> ArchiveStringOperator:
    return cast(ArchiveStringOperator, data)
