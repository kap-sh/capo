"""Generated from Smithy shape ``com.amazonaws.appstream#ExportImageTaskState``."""

from typing import Literal, TypeAlias, cast

ExportImageTaskState: TypeAlias = Literal[
    "EXPORTING",
    "COMPLETED",
    "FAILED",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportImageTaskState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportImageTaskState:
    return cast(ExportImageTaskState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportImageTaskState) -> str:
    return value


def deserialize_cbor(data: str) -> ExportImageTaskState:
    return cast(ExportImageTaskState, data)
