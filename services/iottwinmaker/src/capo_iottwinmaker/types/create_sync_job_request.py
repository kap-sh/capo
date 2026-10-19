"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateSyncJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.role_arn
    import capo_iottwinmaker.types.sync_source
    import capo_iottwinmaker.types.tag_map


class CreateSyncJobRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The workspace ID.</p>"""
    sync_source: "capo_iottwinmaker.types.sync_source.SyncSource"
    """<p>The sync source.</p> <note> <p>Currently the only supported syncSoource is <code>SITEWISE </code>.</p> </note>"""
    sync_role: "capo_iottwinmaker.types.role_arn.RoleArn"
    """<p>The SyncJob IAM role. This IAM role is used by the SyncJob to read from the syncSource, and create, update, or delete the corresponding resources.</p>"""
    tags: NotRequired["capo_iottwinmaker.types.tag_map.TagMap"]
    """<p>The SyncJob tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSyncJobRequest) -> dict:
    out: dict = {}
    out["syncRole"] = value["sync_role"]
    if "tags" in value:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSyncJobRequest:
    out: CreateSyncJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("syncRole") is not None:
        out["sync_role"] = data["syncRole"]
    else:
        out["sync_role"] = ""
    if data.get("tags") is not None:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    return out
