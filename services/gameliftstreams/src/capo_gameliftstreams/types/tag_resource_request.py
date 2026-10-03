"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.arn
    import capo_gameliftstreams.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_gameliftstreams.types.arn.Arn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> of the Amazon GameLift Streams resource that you want to apply tags to.</p>"""
    tags: "capo_gameliftstreams.types.tags.Tags"
    """<p>A list of tags, in the form of key-value pairs, to assign to the specified Amazon GameLift Streams resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_gameliftstreams.types.tags

    out["Tags"] = capo_gameliftstreams.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_gameliftstreams.types.tags

        out["tags"] = capo_gameliftstreams.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
