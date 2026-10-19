"""Generated from Smithy shape ``com.amazonaws.workspaces#StandbyWorkspace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.data_replication
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.volume_encryption_key
    import capo_workspaces.types.workspace_id


class StandbyWorkspace(TypedDict, closed=True):
    primary_workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the standby WorkSpace.</p>"""
    volume_encryption_key: NotRequired[
        "capo_workspaces.types.volume_encryption_key.VolumeEncryptionKey"
    ]
    """<p>The volume encryption key of the standby WorkSpace.</p>"""
    directory_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for the standby WorkSpace.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags associated with the standby WorkSpace.</p>"""
    data_replication: NotRequired[
        "capo_workspaces.types.data_replication.DataReplication"
    ]
    """<p>Indicates whether data replication is enabled, and if enabled, the type of data replication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StandbyWorkspace) -> dict:
    out: dict = {}
    out["PrimaryWorkspaceId"] = value["primary_workspace_id"]
    if "volume_encryption_key" in value:
        out["VolumeEncryptionKey"] = value["volume_encryption_key"]
    out["DirectoryId"] = value["directory_id"]
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "data_replication" in value:
        import capo_workspaces.types.data_replication

        out["DataReplication"] = (
            capo_workspaces.types.data_replication.serialize_aws_json_1_1(
                value["data_replication"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StandbyWorkspace:
    out: StandbyWorkspace = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryWorkspaceId") is not None:
        out["primary_workspace_id"] = data["PrimaryWorkspaceId"]
    else:
        out["primary_workspace_id"] = ""
    if data.get("VolumeEncryptionKey") is not None:
        out["volume_encryption_key"] = data["VolumeEncryptionKey"]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("DataReplication") is not None:
        import capo_workspaces.types.data_replication

        out["data_replication"] = (
            capo_workspaces.types.data_replication.deserialize_aws_json_1_1(
                data["DataReplication"]
            )
        )
    return out
