"""Generated from Smithy shape ``com.amazonaws.workspaces#RebootWorkspacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.reboot_workspace_requests


class RebootWorkspacesRequest(TypedDict, closed=True):
    reboot_workspace_requests: (
        "capo_workspaces.types.reboot_workspace_requests.RebootWorkspaceRequests"
    )
    """<p>The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootWorkspacesRequest) -> dict:
    out: dict = {}
    import capo_workspaces.types.reboot_workspace_requests

    out["RebootWorkspaceRequests"] = (
        capo_workspaces.types.reboot_workspace_requests.serialize_aws_json_1_1(
            value["reboot_workspace_requests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RebootWorkspacesRequest:
    out: RebootWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("RebootWorkspaceRequests") is not None:
        import capo_workspaces.types.reboot_workspace_requests

        out["reboot_workspace_requests"] = (
            capo_workspaces.types.reboot_workspace_requests.deserialize_aws_json_1_1(
                data["RebootWorkspaceRequests"]
            )
        )
    else:
        out["reboot_workspace_requests"] = []
    return out
