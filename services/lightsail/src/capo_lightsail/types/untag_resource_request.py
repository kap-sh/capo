"""Generated from Smithy shape ``com.amazonaws.lightsail#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_arn
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the resource from which you are removing a tag.</p>"""
    resource_arn: NotRequired["capo_lightsail.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource from which you want to remove a tag.</p>"""
    tag_keys: "capo_lightsail.types.tag_key_list.TagKeyList"
    """<p>The tag keys to delete from the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    import capo_lightsail.types.tag_key_list

    out["tagKeys"] = capo_lightsail.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("tagKeys") is not None:
        import capo_lightsail.types.tag_key_list

        out["tag_keys"] = capo_lightsail.types.tag_key_list.deserialize_aws_json_1_1(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
