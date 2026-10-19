"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspaceCreationPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.workspace_creation_properties


class ModifyWorkspaceCreationPropertiesRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    workspace_creation_properties: "capo_workspaces.types.workspace_creation_properties.WorkspaceCreationProperties"
    """<p>The default properties for creating WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspaceCreationPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_workspaces.types.workspace_creation_properties

    out["WorkspaceCreationProperties"] = (
        capo_workspaces.types.workspace_creation_properties.serialize_aws_json_1_1(
            value["workspace_creation_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspaceCreationPropertiesRequest:
    out: ModifyWorkspaceCreationPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("WorkspaceCreationProperties") is not None:
        import capo_workspaces.types.workspace_creation_properties

        out["workspace_creation_properties"] = (
            capo_workspaces.types.workspace_creation_properties.deserialize_aws_json_1_1(
                data["WorkspaceCreationProperties"]
            )
        )
    else:
        raise DeserializationError(
            "ModifyWorkspaceCreationPropertiesRequest.workspace_creation_properties required"
        )
    return out
