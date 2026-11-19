"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedRebootWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.failed_workspace_change_request

FailedRebootWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.failed_workspace_change_request.FailedWorkspaceChangeRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedRebootWorkspaceRequests) -> list:
    import capo_workspaces.types.failed_workspace_change_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.failed_workspace_change_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedRebootWorkspaceRequests:
    import capo_workspaces.types.failed_workspace_change_request

    out: FailedRebootWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.failed_workspace_change_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedRebootWorkspaceRequests) -> list:
    import capo_workspaces.types.failed_workspace_change_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.failed_workspace_change_request.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> FailedRebootWorkspaceRequests:
    import capo_workspaces.types.failed_workspace_change_request

    out: FailedRebootWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.failed_workspace_change_request.deserialize_cbor(item)
        )
    return out
