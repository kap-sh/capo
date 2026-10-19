"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#TagStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.resource_tags
    import capo_kinesis_video.types.stream_name


class TagStreamInput(TypedDict, closed=True):
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the resource that you want to add the tag or tags to.</p>"""
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream that you want to add the tag or tags to.</p>"""
    tags: "capo_kinesis_video.types.resource_tags.ResourceTags"
    """<p>A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagStreamInput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import capo_kinesis_video.types.resource_tags

    out["Tags"] = capo_kinesis_video.types.resource_tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagStreamInput:
    out: TagStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("Tags") is not None:
        import capo_kinesis_video.types.resource_tags

        out["tags"] = capo_kinesis_video.types.resource_tags.deserialize_json(
            data["Tags"]
        )
    else:
        out["tags"] = {}
    return out
