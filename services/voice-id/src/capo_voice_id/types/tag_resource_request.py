"""Generated from Smithy shape ``com.amazonaws.voiceid#TagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.amazon_resource_name
    import capo_voice_id.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_voice_id.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Voice ID resource you want to tag.</p>"""
    tags: "capo_voice_id.types.tag_list.TagList"
    """<p>The list of tags to assign to the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_voice_id.types.tag_list

    out["Tags"] = capo_voice_id.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_voice_id.types.tag_list

        out["tags"] = capo_voice_id.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out


def redact_sensitive(value: TagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_voice_id.types.tag_list

        out["tags"] = capo_voice_id.types.tag_list.redact_sensitive(value["tags"])
    return out
