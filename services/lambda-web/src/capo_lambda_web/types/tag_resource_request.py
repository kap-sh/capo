"""Generated from Smithy shape ``com.amazonaws.lambdaweb#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.resource_arn
    import capo_lambda_web.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource: "capo_lambda_web.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web function.</p>"""
    tags: "capo_lambda_web.types.tags.Tags"
    """<p>A map of tag keys and values to add to the web function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_lambda_web.types.tags

    out["Tags"] = capo_lambda_web.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_lambda_web.types.tags

        out["tags"] = capo_lambda_web.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
