"""Generated from Smithy shape ``com.amazonaws.workspaces#StopWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.failed_stop_workspace_requests


class StopWorkspacesResult(TypedDict, closed=True):
    failed_requests: NotRequired[
        "capo_workspaces.types.failed_stop_workspace_requests.FailedStopWorkspaceRequests"
    ]
    """<p>Information about the WorkSpaces that could not be stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import capo_workspaces.types.failed_stop_workspace_requests

        out["FailedRequests"] = (
            capo_workspaces.types.failed_stop_workspace_requests.serialize_aws_json_1_1(
                value["failed_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopWorkspacesResult:
    out: StopWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedRequests") is not None:
        import capo_workspaces.types.failed_stop_workspace_requests

        out["failed_requests"] = (
            capo_workspaces.types.failed_stop_workspace_requests.deserialize_aws_json_1_1(
                data["FailedRequests"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import capo_workspaces.types.failed_stop_workspace_requests

        out["FailedRequests"] = (
            capo_workspaces.types.failed_stop_workspace_requests.serialize_cbor(
                value["failed_requests"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StopWorkspacesResult:
    out: StopWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedRequests") is not None:
        import capo_workspaces.types.failed_stop_workspace_requests

        out["failed_requests"] = (
            capo_workspaces.types.failed_stop_workspace_requests.deserialize_cbor(
                data["FailedRequests"]
            )
        )
    return out
