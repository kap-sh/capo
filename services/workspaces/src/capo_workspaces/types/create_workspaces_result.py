"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.failed_create_workspace_requests
    import capo_workspaces.types.workspace_list


class CreateWorkspacesResult(TypedDict, closed=True):
    failed_requests: NotRequired[
        "capo_workspaces.types.failed_create_workspace_requests.FailedCreateWorkspaceRequests"
    ]
    """<p>Information about the WorkSpaces that could not be created.</p>"""
    pending_requests: NotRequired["capo_workspaces.types.workspace_list.WorkspaceList"]
    """<p>Information about the WorkSpaces that were created.</p> <p>Because this operation is asynchronous, the identifier returned is not immediately available for use with other operations. For example, if you call <a>DescribeWorkspaces</a> before the WorkSpace is created, the information returned can be incomplete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import capo_workspaces.types.failed_create_workspace_requests

        out["FailedRequests"] = (
            capo_workspaces.types.failed_create_workspace_requests.serialize_aws_json_1_1(
                value["failed_requests"]
            )
        )
    if "pending_requests" in value:
        import capo_workspaces.types.workspace_list

        out["PendingRequests"] = (
            capo_workspaces.types.workspace_list.serialize_aws_json_1_1(
                value["pending_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspacesResult:
    out: CreateWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedRequests") is not None:
        import capo_workspaces.types.failed_create_workspace_requests

        out["failed_requests"] = (
            capo_workspaces.types.failed_create_workspace_requests.deserialize_aws_json_1_1(
                data["FailedRequests"]
            )
        )
    if data.get("PendingRequests") is not None:
        import capo_workspaces.types.workspace_list

        out["pending_requests"] = (
            capo_workspaces.types.workspace_list.deserialize_aws_json_1_1(
                data["PendingRequests"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import capo_workspaces.types.failed_create_workspace_requests

        out["FailedRequests"] = (
            capo_workspaces.types.failed_create_workspace_requests.serialize_cbor(
                value["failed_requests"]
            )
        )
    if "pending_requests" in value:
        import capo_workspaces.types.workspace_list

        out["PendingRequests"] = capo_workspaces.types.workspace_list.serialize_cbor(
            value["pending_requests"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateWorkspacesResult:
    out: CreateWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedRequests") is not None:
        import capo_workspaces.types.failed_create_workspace_requests

        out["failed_requests"] = (
            capo_workspaces.types.failed_create_workspace_requests.deserialize_cbor(
                data["FailedRequests"]
            )
        )
    if data.get("PendingRequests") is not None:
        import capo_workspaces.types.workspace_list

        out["pending_requests"] = capo_workspaces.types.workspace_list.deserialize_cbor(
            data["PendingRequests"]
        )
    return out
