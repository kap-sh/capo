"""Generated from Smithy shape ``com.amazonaws.amp#DescribeWorkspaceConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.workspace_id


class DescribeWorkspaceConfigurationRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace that you want to retrieve information for. To find the IDs of your workspaces, use the <a href="https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.htm">ListWorkspaces</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceConfigurationRequest:
    out: DescribeWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
