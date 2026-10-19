"""Generated from Smithy shape ``com.amazonaws.ecr#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.arn
    import capo_ecr.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_ecr.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the the resource to which to add tags. Currently, the only supported resource is an Amazon ECR repository.</p>"""
    tags: "capo_ecr.types.tag_list.TagList"
    """<p>The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_ecr.types.tag_list

    out["tags"] = capo_ecr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_ecr.types.tag_list

        out["tags"] = capo_ecr.types.tag_list.deserialize_aws_json_1_1(data["tags"])
    else:
        out["tags"] = []
    return out
