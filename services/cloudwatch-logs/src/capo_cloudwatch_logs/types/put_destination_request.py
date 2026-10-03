"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.destination_name
    import capo_cloudwatch_logs.types.role_arn
    import capo_cloudwatch_logs.types.tags
    import capo_cloudwatch_logs.types.target_arn


class PutDestinationRequest(TypedDict, closed=True):
    destination_name: "capo_cloudwatch_logs.types.destination_name.DestinationName"
    """<p>A name for the destination.</p>"""
    target_arn: "capo_cloudwatch_logs.types.target_arn.TargetArn"
    """<p>The ARN of an Amazon Kinesis stream to which to deliver matching log events.</p>"""
    role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of an IAM role that grants CloudWatch Logs permissions to call the Amazon Kinesis <code>PutRecord</code> operation on the destination stream.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDestinationRequest) -> dict:
    out: dict = {}
    out["destinationName"] = value["destination_name"]
    out["targetArn"] = value["target_arn"]
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDestinationRequest:
    out: PutDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("destinationName") is not None:
        out["destination_name"] = data["destinationName"]
    else:
        raise DeserializationError("PutDestinationRequest.destination_name required")
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("PutDestinationRequest.target_arn required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("PutDestinationRequest.role_arn required")
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
