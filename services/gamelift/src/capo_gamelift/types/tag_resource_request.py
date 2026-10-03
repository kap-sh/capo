"""Generated from Smithy shape ``com.amazonaws.gamelift#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.amazon_resource_name
    import capo_gamelift.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: NotRequired[
        "capo_gamelift.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that uniquely identifies the Amazon GameLift Servers resource that you want to assign tags to. Amazon GameLift Servers includes resource ARNs in the data object for the resource. You can retrieve the ARN by calling a <code>List</code> or <code>Describe</code> operation for the resource type. </p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of one or more tags to assign to the specified Amazon GameLift Servers resource. Tags are developer-defined and structured as key-value pairs. The maximum tag limit may be lower than stated. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> for tagging limits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
