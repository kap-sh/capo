"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceState``."""

from typing import Literal, TypeAlias, cast

WorkspaceState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "IMPAIRED",
    "UNHEALTHY",
    "REBOOTING",
    "STARTING",
    "REBUILDING",
    "RESTORING",
    "MAINTENANCE",
    "ADMIN_MAINTENANCE",
    "TERMINATING",
    "TERMINATED",
    "SUSPENDED",
    "UPDATING",
    "STOPPING",
    "STOPPED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceState:
    return cast(WorkspaceState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceState) -> str:
    return value


def deserialize_cbor(data: str) -> WorkspaceState:
    return cast(WorkspaceState, data)
