"""Generated from Smithy shape ``com.amazonaws.amp#CreateWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.kms_key_arn
    import capo_amp.types.tag_map
    import capo_amp.types.workspace_arn
    import capo_amp.types.workspace_id
    import capo_amp.types.workspace_status


class CreateWorkspaceResponse(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The unique ID for the new workspace.</p>"""
    arn: "capo_amp.types.workspace_arn.WorkspaceArn"
    """<p>The ARN for the new workspace.</p>"""
    status: "capo_amp.types.workspace_status.WorkspaceStatus"
    """<p>The current status of the new workspace. Immediately after you create the workspace, the status is usually <code>CREATING</code>.</p>"""
    tags: NotRequired["capo_amp.types.tag_map.TagMap"]
    """<p>The list of tag keys and values that are associated with the workspace.</p>"""
    kms_key_arn: NotRequired["capo_amp.types.kms_key_arn.KmsKeyArn"]
    """<p>(optional) If the workspace was created with a customer managed KMS key, the ARN for the key used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceResponse) -> dict:
    out: dict = {}
    out["workspaceId"] = value["workspace_id"]
    out["arn"] = value["arn"]
    import capo_amp.types.workspace_status

    out["status"] = capo_amp.types.workspace_status.serialize_json(value["status"])
    if "tags" in value:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateWorkspaceResponse:
    out: CreateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("workspaceId") is not None:
        out["workspace_id"] = data["workspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_amp.types.workspace_status

        out["status"] = capo_amp.types.workspace_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateWorkspaceResponse.status required")
    if data.get("tags") is not None:
        import capo_amp.types.tag_map

        out["tags"] = capo_amp.types.tag_map.deserialize_json(data["tags"])
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
