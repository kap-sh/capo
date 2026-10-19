"""Generated from Smithy shape ``com.amazonaws.voiceid#UntagResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.amazon_resource_name
    import capo_voice_id.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_voice_id.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Voice ID resource you want to remove tags from.</p>"""
    tag_keys: "capo_voice_id.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys you want to remove from the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_voice_id.types.tag_key_list

    out["TagKeys"] = capo_voice_id.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_voice_id.types.tag_key_list

        out["tag_keys"] = capo_voice_id.types.tag_key_list.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out


def redact_sensitive(value: UntagResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_keys" in value:
        import capo_voice_id.types.tag_key_list

        out["tag_keys"] = capo_voice_id.types.tag_key_list.redact_sensitive(
            value["tag_keys"]
        )
    return out
