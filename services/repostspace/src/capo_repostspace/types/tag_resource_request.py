"""Generated from Smithy shape ``com.amazonaws.repostspace#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_repostspace.types.arn
    import capo_repostspace.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_repostspace.types.arn.Arn"
    """<p>The ARN of the resource that the tag is associated with.</p>"""
    tags: "capo_repostspace.types.tags.Tags"
    """<p>The list of tag keys and values that must be associated with the resource. You can associate tag keys only, tags (key and values) only, or a combination of tag keys and tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_repostspace.types.tags

    out["tags"] = capo_repostspace.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_repostspace.types.tags

        out["tags"] = capo_repostspace.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
