"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceOSUserMode``."""

from typing import Literal, TypeAlias, cast

WorkspaceOSUserMode: TypeAlias = Literal[
    "LOCAL_USER",
    "DOMAIN_JOIN",
    "ENTRA_JOIN",
    "SELF_MANAGED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceOSUserMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceOSUserMode:
    return cast(WorkspaceOSUserMode, data)
