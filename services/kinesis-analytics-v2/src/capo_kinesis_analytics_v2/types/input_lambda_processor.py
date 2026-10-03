"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputLambdaProcessor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.resource_arn


class InputLambdaProcessor(TypedDict, closed=True):
    resource_arn: "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The ARN of the Amazon Lambda function that operates on records in the stream.</p> <note> <p>To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda">Example ARNs: Amazon Lambda</a> </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLambdaProcessor) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputLambdaProcessor:
    out: InputLambdaProcessor = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("InputLambdaProcessor.resource_arn required")
    return out
