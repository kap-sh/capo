"""Generated from Smithy shape ``com.amazonaws.deadline#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.string
    import capo_deadline.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_deadline.types.string.String"
    """The ARN of the resource to apply tags to."""
    tags: NotRequired["capo_deadline.types.tags.Tags"]
    """Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings."""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.deserialize_json(data["tags"])
    return out
