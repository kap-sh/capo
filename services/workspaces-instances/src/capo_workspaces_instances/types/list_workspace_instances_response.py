"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListWorkspaceInstancesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.next_token
    import capo_workspaces_instances.types.workspace_instances


class ListWorkspaceInstancesResponse(TypedDict, closed=True):
    workspace_instances: (
        "capo_workspaces_instances.types.workspace_instances.WorkspaceInstances"
    )
    """<p>Collection of WorkSpaces Instances returned by the query.</p>"""
    next_token: NotRequired["capo_workspaces_instances.types.next_token.NextToken"]
    """<p>Token for retrieving additional WorkSpaces Instances if the result set is paginated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkspaceInstancesResponse) -> dict:
    out: dict = {}
    import capo_workspaces_instances.types.workspace_instances

    out["WorkspaceInstances"] = (
        capo_workspaces_instances.types.workspace_instances.serialize_aws_json_1_0(
            value["workspace_instances"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkspaceInstancesResponse:
    out: ListWorkspaceInstancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceInstances") is not None:
        import capo_workspaces_instances.types.workspace_instances

        out["workspace_instances"] = (
            capo_workspaces_instances.types.workspace_instances.deserialize_aws_json_1_0(
                data["WorkspaceInstances"]
            )
        )
    else:
        out["workspace_instances"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListWorkspaceInstancesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
