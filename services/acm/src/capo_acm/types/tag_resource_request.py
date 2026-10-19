"""Generated from Smithy shape ``com.amazonaws.acm#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_acm.types.arn.Arn"
    """<p>The ARN of the ACM resource to which the tag is to be applied.</p>"""
    tags: "capo_acm.types.tag_list.TagList"
    """<p>The key-value pair that defines the tag to apply.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_acm.types.tag_list

    out["Tags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_acm.types.tag_list

        out["tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = []
    return out
