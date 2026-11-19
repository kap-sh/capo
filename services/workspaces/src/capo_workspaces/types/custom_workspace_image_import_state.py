"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomWorkspaceImageImportState``."""

from typing import Literal, TypeAlias, cast

CustomWorkspaceImageImportState: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "PROCESSING_SOURCE_IMAGE",
    "IMAGE_TESTING_START",
    "UPDATING_OPERATING_SYSTEM",
    "IMAGE_COMPATIBILITY_CHECKING",
    "IMAGE_TESTING_GENERALIZATION",
    "CREATING_TEST_INSTANCE",
    "INSTALLING_COMPONENTS",
    "GENERALIZING",
    "VALIDATING",
    "PUBLISHING",
    "COMPLETED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomWorkspaceImageImportState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomWorkspaceImageImportState:
    return cast(CustomWorkspaceImageImportState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomWorkspaceImageImportState) -> str:
    return value


def deserialize_cbor(data: str) -> CustomWorkspaceImageImportState:
    return cast(CustomWorkspaceImageImportState, data)
