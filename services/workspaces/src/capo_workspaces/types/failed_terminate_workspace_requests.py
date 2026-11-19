"""Generated from Smithy shape ``com.amazonaws.workspaces#FailedTerminateWorkspaceRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.failed_workspace_change_request

FailedTerminateWorkspaceRequests: TypeAlias = list[
    "capo_workspaces.types.failed_workspace_change_request.FailedWorkspaceChangeRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedTerminateWorkspaceRequests) -> list:
    import capo_workspaces.types.failed_workspace_change_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.failed_workspace_change_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedTerminateWorkspaceRequests:
    import capo_workspaces.types.failed_workspace_change_request

    out: FailedTerminateWorkspaceRequests = []
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
def serialize_cbor(value: FailedTerminateWorkspaceRequests) -> list:
    import capo_workspaces.types.failed_workspace_change_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.failed_workspace_change_request.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> FailedTerminateWorkspaceRequests:
    import capo_workspaces.types.failed_workspace_change_request

    out: FailedTerminateWorkspaceRequests = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.failed_workspace_change_request.deserialize_cbor(item)
        )
    return out
