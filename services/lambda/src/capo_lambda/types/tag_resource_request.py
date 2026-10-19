"""Generated from Smithy shape ``com.amazonaws.lambda#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.taggable_resource
    import capo_lambda.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource: "capo_lambda.types.taggable_resource.TaggableResource"
    """<p>The resource's Amazon Resource Name (ARN).</p>"""
    tags: "capo_lambda.types.tags.Tags"
    """<p>A list of tags to apply to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_lambda.types.tags

    out["Tags"] = capo_lambda.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_lambda.types.tags

        out["tags"] = capo_lambda.types.tags.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
