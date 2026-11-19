"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportDataType``."""

from typing import Literal, TypeAlias, cast

ImportDataType: TypeAlias = Literal[
    "CSV",
    "JSON",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportDataType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImportDataType:
    return cast(ImportDataType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImportDataType) -> str:
    return value


def deserialize_cbor(data: str) -> ImportDataType:
    return cast(ImportDataType, data)
