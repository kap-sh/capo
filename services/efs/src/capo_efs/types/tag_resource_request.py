"""Generated from Smithy shape ``com.amazonaws.efs#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.resource_id
    import capo_efs.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_id: "capo_efs.types.resource_id.ResourceId"
    """<p>The ID specifying the EFS resource that you want to create a tag for.</p>"""
    tags: "capo_efs.types.tags.Tags"
    """<p>An array of <code>Tag</code> objects to add. Each <code>Tag</code> object is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_efs.types.tags

    out["Tags"] = capo_efs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_efs.types.tags

        out["tags"] = capo_efs.types.tags.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
