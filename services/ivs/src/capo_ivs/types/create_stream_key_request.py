"""Generated from Smithy shape ``com.amazonaws.ivs#CreateStreamKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn
    import capo_ivs.types.tags


class CreateStreamKeyRequest(TypedDict, closed=True):
    channel_arn: "capo_ivs.types.channel_arn.ChannelArn"
    """<p>ARN of the channel for which to create the stream key.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamKeyRequest) -> dict:
    out: dict = {}
    out["channelArn"] = value["channel_arn"]
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateStreamKeyRequest:
    out: CreateStreamKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    else:
        raise DeserializationError("CreateStreamKeyRequest.channel_arn required")
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    return out
