"""Generated from Smithy shape ``com.amazonaws.workspaces#RebuildWorkspacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.failed_rebuild_workspace_requests


class RebuildWorkspacesResult(TypedDict, closed=True):
    failed_requests: NotRequired[
        "capo_workspaces.types.failed_rebuild_workspace_requests.FailedRebuildWorkspaceRequests"
    ]
    """<p>Information about the WorkSpace that could not be rebuilt.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebuildWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import capo_workspaces.types.failed_rebuild_workspace_requests

        out["FailedRequests"] = (
            capo_workspaces.types.failed_rebuild_workspace_requests.serialize_aws_json_1_1(
                value["failed_requests"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RebuildWorkspacesResult:
    out: RebuildWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedRequests") is not None:
        import capo_workspaces.types.failed_rebuild_workspace_requests

        out["failed_requests"] = (
            capo_workspaces.types.failed_rebuild_workspace_requests.deserialize_aws_json_1_1(
                data["FailedRequests"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RebuildWorkspacesResult) -> dict:
    out: dict = {}
    if "failed_requests" in value:
        import capo_workspaces.types.failed_rebuild_workspace_requests

        out["FailedRequests"] = (
            capo_workspaces.types.failed_rebuild_workspace_requests.serialize_cbor(
                value["failed_requests"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RebuildWorkspacesResult:
    out: RebuildWorkspacesResult = {}  # type: ignore[typeddict-item]
    if data.get("FailedRequests") is not None:
        import capo_workspaces.types.failed_rebuild_workspace_requests

        out["failed_requests"] = (
            capo_workspaces.types.failed_rebuild_workspace_requests.deserialize_cbor(
                data["FailedRequests"]
            )
        )
    return out
