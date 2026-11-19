"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociationErrorCode``."""

from typing import Literal, TypeAlias, cast

AssociationErrorCode: TypeAlias = Literal[
    "ValidationError.InsufficientDiskSpace",
    "ValidationError.InsufficientMemory",
    "ValidationError.UnsupportedOperatingSystem",
    "DeploymentError.InternalServerError",
    "DeploymentError.WorkspaceUnreachable",
    "ValidationError.ApplicationOldVersionExists",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationErrorCode:
    return cast(AssociationErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociationErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> AssociationErrorCode:
    return cast(AssociationErrorCode, data)
