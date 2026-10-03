"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputLambdaProcessor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.resource_arn
    import capo_kinesis_analytics.types.role_arn


class InputLambdaProcessor(TypedDict, closed=True):
    resource_arn: "capo_kinesis_analytics.types.resource_arn.ResourceARN"
    """<p>The ARN of the <a href="https://docs.aws.amazon.com/lambda/">AWS Lambda</a> function that operates on records in the stream.</p> <note> <p>To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda">Example ARNs: AWS Lambda</a> </p> </note>"""
    role_arn: "capo_kinesis_analytics.types.role_arn.RoleARN"
    """<p>The ARN of the IAM role that is used to access the AWS Lambda function.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLambdaProcessor) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputLambdaProcessor:
    out: InputLambdaProcessor = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("InputLambdaProcessor.resource_arn required")
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("InputLambdaProcessor.role_arn required")
    return out
