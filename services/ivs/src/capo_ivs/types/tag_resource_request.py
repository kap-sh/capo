"""Generated from Smithy shape ``com.amazonaws.ivs#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.resource_arn
    import capo_ivs.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_ivs.types.resource_arn.ResourceArn"
    """<p>ARN of the resource for which tags are to be added or updated. The ARN must be URL-encoded.</p>"""
    tags: "capo_ivs.types.tags.Tags"
    """<p>Array of tags to be added or updated. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_ivs.types.tags

    out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
