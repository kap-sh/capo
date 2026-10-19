"""Generated from Smithy shape ``com.amazonaws.s3files#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.resource_id
    import capo_s3files.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_id: "capo_s3files.types.resource_id.ResourceId"
    """<p>The ID or Amazon Resource Name (ARN) of the resource to add tags to.</p>"""
    tags: "capo_s3files.types.tag_list.TagList"
    """<p>An array of key-value pairs to add as tags to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_s3files.types.tag_list

    out["tags"] = capo_s3files.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_s3files.types.tag_list

        out["tags"] = capo_s3files.types.tag_list.deserialize_json(data["tags"])
    else:
        out["tags"] = []
    return out
