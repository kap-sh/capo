"""Generated from Smithy shape ``com.amazonaws.efs#CreateTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.file_system_id
    import capo_efs.types.tags


class CreateTagsRequest(TypedDict, closed=True):
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.</p>"""
    tags: "capo_efs.types.tags.Tags"
    """<p>An array of <code>Tag</code> objects to add. Each <code>Tag</code> object is a key-value pair. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTagsRequest) -> dict:
    out: dict = {}
    import capo_efs.types.tags

    out["Tags"] = capo_efs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTagsRequest:
    out: CreateTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_efs.types.tags

        out["tags"] = capo_efs.types.tags.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
