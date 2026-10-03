"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.amazon_resource_name
    import capo_cloudwatch_logs.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_cloudwatch_logs.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the CloudWatch Logs resource that you're removing tags from.</p> <p>The ARN format of a log group is <code>arn:aws:logs:<i>Region</i>:<i>account-id</i>:log-group:<i>log-group-name</i> </code> </p> <p>The ARN format of a destination is <code>arn:aws:logs:<i>Region</i>:<i>account-id</i>:destination:<i>destination-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html">CloudWatch Logs resources and operations</a>.</p>"""
    tag_keys: "capo_cloudwatch_logs.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_cloudwatch_logs.types.tag_key_list

    out["tagKeys"] = capo_cloudwatch_logs.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UntagResourceRequest.resource_arn required")
    if data.get("tagKeys") is not None:
        import capo_cloudwatch_logs.types.tag_key_list

        out["tag_keys"] = (
            capo_cloudwatch_logs.types.tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
