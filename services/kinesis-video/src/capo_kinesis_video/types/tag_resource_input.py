"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signaling channel to which you want to add tags.</p>"""
    tags: "capo_kinesis_video.types.tag_list.TagList"
    """<p>A list of tags to associate with the specified signaling channel. Each tag is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_kinesis_video.types.tag_list

    out["Tags"] = capo_kinesis_video.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_kinesis_video.types.tag_list

        out["tags"] = capo_kinesis_video.types.tag_list.deserialize_json(data["Tags"])
    else:
        out["tags"] = []
    return out
