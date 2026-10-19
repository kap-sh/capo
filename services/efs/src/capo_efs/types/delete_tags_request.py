"""Generated from Smithy shape ``com.amazonaws.efs#DeleteTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.file_system_id
    import capo_efs.types.tag_keys


class DeleteTagsRequest(TypedDict, closed=True):
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system whose tags you want to delete (String).</p>"""
    tag_keys: "capo_efs.types.tag_keys.TagKeys"
    """<p>A list of tag keys to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTagsRequest) -> dict:
    out: dict = {}
    import capo_efs.types.tag_keys

    out["TagKeys"] = capo_efs.types.tag_keys.serialize_json(value["tag_keys"])
    return out


def deserialize_json(data: dict) -> DeleteTagsRequest:
    out: DeleteTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TagKeys") is not None:
        import capo_efs.types.tag_keys

        out["tag_keys"] = capo_efs.types.tag_keys.deserialize_json(data["TagKeys"])
    else:
        out["tag_keys"] = []
    return out
