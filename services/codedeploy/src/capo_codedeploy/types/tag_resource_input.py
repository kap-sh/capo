"""Generated from Smithy shape ``com.amazonaws.codedeploy#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.arn
    import capo_codedeploy.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_codedeploy.types.arn.Arn"
    """<p> The ARN of a resource, such as a CodeDeploy application or deployment group. </p>"""
    tags: "capo_codedeploy.types.tag_list.TagList"
    """<p> A list of tags that <code>TagResource</code> associates with a resource. The resource is identified by the <code>ResourceArn</code> input parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_codedeploy.types.tag_list

    out["Tags"] = capo_codedeploy.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
