"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.tag_key_list
    import capo_workspaces_instances.types.workspace_instance_id


class UntagResourceRequest(TypedDict, closed=True):
    workspace_instance_id: (
        "capo_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>Unique identifier of the WorkSpace Instance to untag.</p>"""
    tag_keys: "capo_workspaces_instances.types.tag_key_list.TagKeyList"
    """<p>Keys of tags to be removed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    import capo_workspaces_instances.types.tag_key_list

    out["TagKeys"] = (
        capo_workspaces_instances.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceInstanceId") is not None:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        out["workspace_instance_id"] = ""
    if data.get("TagKeys") is not None:
        import capo_workspaces_instances.types.tag_key_list

        out["tag_keys"] = (
            capo_workspaces_instances.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
