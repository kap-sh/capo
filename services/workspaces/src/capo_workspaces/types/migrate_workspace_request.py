"""Generated from Smithy shape ``com.amazonaws.workspaces#MigrateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.bundle_id
    import capo_workspaces.types.workspace_id


class MigrateWorkspaceRequest(TypedDict, closed=True):
    source_workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace to migrate from.</p>"""
    bundle_id: "capo_workspaces.types.bundle_id.BundleId"
    """<p>The identifier of the target bundle type to migrate the WorkSpace to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrateWorkspaceRequest) -> dict:
    out: dict = {}
    out["SourceWorkspaceId"] = value["source_workspace_id"]
    out["BundleId"] = value["bundle_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MigrateWorkspaceRequest:
    out: MigrateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceWorkspaceId") is not None:
        out["source_workspace_id"] = data["SourceWorkspaceId"]
    else:
        out["source_workspace_id"] = ""
    if data.get("BundleId") is not None:
        out["bundle_id"] = data["BundleId"]
    else:
        out["bundle_id"] = ""
    return out
