"""Generated from Smithy shape ``com.amazonaws.lightsail#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_arn
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the resource to which you are adding tags.</p>"""
    resource_arn: NotRequired["capo_lightsail.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to add a tag.</p>"""
    tags: "capo_lightsail.types.tag_list.TagList"
    """<p>The tag key and optional value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    import capo_lightsail.types.tag_list

    out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
