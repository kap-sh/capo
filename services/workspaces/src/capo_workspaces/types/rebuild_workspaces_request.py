"""Generated from Smithy shape ``com.amazonaws.workspaces#RebuildWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.rebuild_workspace_requests


class RebuildWorkspacesRequest(TypedDict, closed=True):
    rebuild_workspace_requests: (
        "capo_workspaces.types.rebuild_workspace_requests.RebuildWorkspaceRequests"
    )
    """<p>The WorkSpace to rebuild. You can specify a single WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebuildWorkspacesRequest) -> dict:
    out: dict = {}
    import capo_workspaces.types.rebuild_workspace_requests

    out["RebuildWorkspaceRequests"] = (
        capo_workspaces.types.rebuild_workspace_requests.serialize_aws_json_1_1(
            value["rebuild_workspace_requests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RebuildWorkspacesRequest:
    out: RebuildWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("RebuildWorkspaceRequests") is not None:
        import capo_workspaces.types.rebuild_workspace_requests

        out["rebuild_workspace_requests"] = (
            capo_workspaces.types.rebuild_workspace_requests.deserialize_aws_json_1_1(
                data["RebuildWorkspaceRequests"]
            )
        )
    else:
        out["rebuild_workspace_requests"] = []
    return out
