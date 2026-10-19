"""Generated from Smithy shape ``com.amazonaws.workspaces#StopWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.stop_workspace_requests


class StopWorkspacesRequest(TypedDict, closed=True):
    stop_workspace_requests: (
        "capo_workspaces.types.stop_workspace_requests.StopWorkspaceRequests"
    )
    """<p>The WorkSpaces to stop. You can specify up to 25 WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopWorkspacesRequest) -> dict:
    out: dict = {}
    import capo_workspaces.types.stop_workspace_requests

    out["StopWorkspaceRequests"] = (
        capo_workspaces.types.stop_workspace_requests.serialize_aws_json_1_1(
            value["stop_workspace_requests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopWorkspacesRequest:
    out: StopWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("StopWorkspaceRequests") is not None:
        import capo_workspaces.types.stop_workspace_requests

        out["stop_workspace_requests"] = (
            capo_workspaces.types.stop_workspace_requests.deserialize_aws_json_1_1(
                data["StopWorkspaceRequests"]
            )
        )
    else:
        out["stop_workspace_requests"] = []
    return out
