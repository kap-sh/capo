"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.terminate_workspace_requests


class TerminateWorkspacesRequest(TypedDict, closed=True):
    terminate_workspace_requests: (
        "capo_workspaces.types.terminate_workspace_requests.TerminateWorkspaceRequests"
    )
    """<p>The WorkSpaces to terminate. You can specify up to 25 WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspacesRequest) -> dict:
    out: dict = {}
    import capo_workspaces.types.terminate_workspace_requests

    out["TerminateWorkspaceRequests"] = (
        capo_workspaces.types.terminate_workspace_requests.serialize_aws_json_1_1(
            value["terminate_workspace_requests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateWorkspacesRequest:
    out: TerminateWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("TerminateWorkspaceRequests") is not None:
        import capo_workspaces.types.terminate_workspace_requests

        out["terminate_workspace_requests"] = (
            capo_workspaces.types.terminate_workspace_requests.deserialize_aws_json_1_1(
                data["TerminateWorkspaceRequests"]
            )
        )
    else:
        out["terminate_workspace_requests"] = []
    return out
