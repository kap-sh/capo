"""Generated from Smithy shape ``com.amazonaws.ivs#StreamKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn
    import capo_ivs.types.stream_key_arn
    import capo_ivs.types.stream_key_value
    import capo_ivs.types.tags


class StreamKey(TypedDict, closed=True):
    arn: NotRequired["capo_ivs.types.stream_key_arn.StreamKeyArn"]
    """<p>Stream-key ARN.</p>"""
    value: NotRequired["capo_ivs.types.stream_key_value.StreamKeyValue"]
    """<p>Stream-key value.</p>"""
    channel_arn: NotRequired["capo_ivs.types.channel_arn.ChannelArn"]
    """<p>Channel ARN for the stream.</p>"""
    tags: NotRequired["capo_ivs.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamKey) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "value" in value:
        out["value"] = value["value"]
    if "channel_arn" in value:
        out["channelArn"] = value["channel_arn"]
    if "tags" in value:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StreamKey:
    out: StreamKey = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    if data.get("tags") is not None:
        import capo_ivs.types.tags

        out["tags"] = capo_ivs.types.tags.deserialize_json(data["tags"])
    return out
