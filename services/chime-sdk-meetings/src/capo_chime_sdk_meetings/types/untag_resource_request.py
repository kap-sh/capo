"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.amazon_resource_name
    import capo_chime_sdk_meetings.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_chime_sdk_meetings.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the resource that you're removing tags from.</p>"""
    tag_keys: "capo_chime_sdk_meetings.types.tag_key_list.TagKeyList"
    """<p>The tag keys being removed from the resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_chime_sdk_meetings.types.tag_key_list

    out["TagKeys"] = capo_chime_sdk_meetings.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_chime_sdk_meetings.types.tag_key_list

        out["tag_keys"] = capo_chime_sdk_meetings.types.tag_key_list.deserialize_json(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
