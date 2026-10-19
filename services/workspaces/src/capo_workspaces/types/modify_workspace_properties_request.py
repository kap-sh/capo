"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspacePropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.data_replication
    import capo_workspaces.types.workspace_id
    import capo_workspaces.types.workspace_properties


class ModifyWorkspacePropertiesRequest(TypedDict, closed=True):
    workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""
    workspace_properties: NotRequired[
        "capo_workspaces.types.workspace_properties.WorkspaceProperties"
    ]
    """<p>The properties of the WorkSpace.</p>"""
    data_replication: NotRequired[
        "capo_workspaces.types.data_replication.DataReplication"
    ]
    """<p>Indicates the data replication status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspacePropertiesRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    if "workspace_properties" in value:
        import capo_workspaces.types.workspace_properties

        out["WorkspaceProperties"] = (
            capo_workspaces.types.workspace_properties.serialize_aws_json_1_1(
                value["workspace_properties"]
            )
        )
    if "data_replication" in value:
        import capo_workspaces.types.data_replication

        out["DataReplication"] = (
            capo_workspaces.types.data_replication.serialize_aws_json_1_1(
                value["data_replication"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspacePropertiesRequest:
    out: ModifyWorkspacePropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("WorkspaceProperties") is not None:
        import capo_workspaces.types.workspace_properties

        out["workspace_properties"] = (
            capo_workspaces.types.workspace_properties.deserialize_aws_json_1_1(
                data["WorkspaceProperties"]
            )
        )
    if data.get("DataReplication") is not None:
        import capo_workspaces.types.data_replication

        out["data_replication"] = (
            capo_workspaces.types.data_replication.deserialize_aws_json_1_1(
                data["DataReplication"]
            )
        )
    return out
