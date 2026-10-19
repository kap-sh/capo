"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.amazon_resource_arn
    import capo_lookoutequipment.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_lookoutequipment.types.amazon_resource_arn.AmazonResourceArn"
    """<p>The Amazon Resource Name (ARN) of the specific resource to which the tag should be associated. </p>"""
    tags: "capo_lookoutequipment.types.tag_list.TagList"
    """<p>The tag or tags to be associated with a specific resource. Both the tag key and value are specified. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_lookoutequipment.types.tag_list

    out["Tags"] = capo_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_lookoutequipment.types.tag_list

        out["tags"] = capo_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
