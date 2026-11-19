"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderState``."""

from typing import Literal, TypeAlias, cast

ImageBuilderState: TypeAlias = Literal[
    "PENDING",
    "UPDATING_AGENT",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "REBOOTING",
    "SNAPSHOTTING",
    "DELETING",
    "FAILED",
    "UPDATING",
    "PENDING_QUALIFICATION",
    "PENDING_SYNCING_APPS",
    "SYNCING_APPS",
    "PENDING_IMAGE_IMPORT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageBuilderState:
    return cast(ImageBuilderState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImageBuilderState) -> str:
    return value


def deserialize_cbor(data: str) -> ImageBuilderState:
    return cast(ImageBuilderState, data)
