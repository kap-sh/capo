"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceDirectoryType``."""

from typing import Literal, TypeAlias, cast

WorkspaceDirectoryType: TypeAlias = Literal[
    "SIMPLE_AD",
    "AD_CONNECTOR",
    "CUSTOMER_MANAGED",
    "AWS_IAM_IDENTITY_CENTER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceDirectoryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceDirectoryType:
    return cast(WorkspaceDirectoryType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceDirectoryType) -> str:
    return value


def deserialize_cbor(data: str) -> WorkspaceDirectoryType:
    return cast(WorkspaceDirectoryType, data)
