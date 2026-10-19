"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signaling channel from which you want to remove tags.</p>"""
    tag_key_list: "capo_kinesis_video.types.tag_key_list.TagKeyList"
    """<p>A list of the keys of the tags that you want to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_kinesis_video.types.tag_key_list

    out["TagKeyList"] = capo_kinesis_video.types.tag_key_list.serialize_json(
        value["tag_key_list"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeyList") is not None:
        import capo_kinesis_video.types.tag_key_list

        out["tag_key_list"] = capo_kinesis_video.types.tag_key_list.deserialize_json(
            data["TagKeyList"]
        )
    else:
        out["tag_key_list"] = []
    return out
