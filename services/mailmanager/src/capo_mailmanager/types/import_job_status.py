"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportJobStatus``."""

from typing import Literal, TypeAlias, cast

ImportJobStatus: TypeAlias = Literal[
    "CREATED",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImportJobStatus:
    return cast(ImportJobStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImportJobStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ImportJobStatus:
    return cast(ImportJobStatus, data)
