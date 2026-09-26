"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.taggable_resource
    import capo_lambda_microvms.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource: "capo_lambda_microvms.types.taggable_resource.TaggableResource"
    """<p>The ARN of the resource to tag.</p>"""
    tags: "capo_lambda_microvms.types.tags.Tags"
    """<p>The key-value pairs of tags to add to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_lambda_microvms.types.tags

    out["Tags"] = capo_lambda_microvms.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_lambda_microvms.types.tags

        out["tags"] = capo_lambda_microvms.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
