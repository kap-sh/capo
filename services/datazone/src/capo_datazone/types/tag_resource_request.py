"""Generated from Smithy shape ``com.amazonaws.datazone#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to be tagged in Amazon DataZone.</p>"""
    tags: "capo_datazone.types.tags.Tags"
    """<p>Specifies the tags for the <code>TagResource</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_datazone.types.tags

    out["tags"] = capo_datazone.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_datazone.types.tags

        out["tags"] = capo_datazone.types.tags.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
