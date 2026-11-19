"""Generated from Smithy shape ``com.amazonaws.workspaces#StartWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.failed_start_workspace_requests


class StartWorkspacesResult(TypedDict, closed=True):
    failed_requests: NotRequired[
        "capo_workspaces.types.failed_start_workspace_requests.FailedStartWorkspaceRequests"
    ]
    """<p>Information about the WorkSpaces that could not be started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import capo_workspaces.types.failed_start_workspace_requests

        out["FailedRequests"] = (
            capo_workspaces.types.failed_start_workspace_requests.serialize_aws_json_1_1(
                value["failed_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWorkspacesResult:
    out: StartWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedRequests") is not None:
        import capo_workspaces.types.failed_start_workspace_requests

        out["failed_requests"] = (
            capo_workspaces.types.failed_start_workspace_requests.deserialize_aws_json_1_1(
                data["FailedRequests"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import capo_workspaces.types.failed_start_workspace_requests

        out["FailedRequests"] = (
            capo_workspaces.types.failed_start_workspace_requests.serialize_cbor(
                value["failed_requests"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StartWorkspacesResult:
    out: StartWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedRequests") is not None:
        import capo_workspaces.types.failed_start_workspace_requests

        out["failed_requests"] = (
            capo_workspaces.types.failed_start_workspace_requests.deserialize_cbor(
                data["FailedRequests"]
            )
        )
    return out
