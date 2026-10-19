"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.amazon_resource_name
    import capo_pinpoint_sms_voice_v2.types.non_empty_tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_pinpoint_sms_voice_v2.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_pinpoint_sms_voice_v2.types.non_empty_tag_list.NonEmptyTagList"
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_pinpoint_sms_voice_v2.types.non_empty_tag_list

    out["Tags"] = (
        capo_pinpoint_sms_voice_v2.types.non_empty_tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_pinpoint_sms_voice_v2.types.non_empty_tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.non_empty_tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    else:
        out["tags"] = []
    return out
