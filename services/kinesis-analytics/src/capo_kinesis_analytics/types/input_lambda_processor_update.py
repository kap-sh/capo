"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputLambdaProcessorUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.resource_arn
    import capo_kinesis_analytics.types.role_arn


class InputLambdaProcessorUpdate(TypedDict, closed=True):
    resource_arn_update: NotRequired[
        "capo_kinesis_analytics.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the new <a href="https://docs.aws.amazon.com/lambda/">AWS Lambda</a> function that is used to preprocess the records in the stream.</p> <note> <p>To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda">Example ARNs: AWS Lambda</a> </p> </note>"""
    role_arn_update: NotRequired["capo_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>The ARN of the new IAM role that is used to access the AWS Lambda function.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLambdaProcessorUpdate) -> dict:
    out: dict = {}
    if "resource_arn_update" in value:
        out["ResourceARNUpdate"] = value["resource_arn_update"]
    if "role_arn_update" in value:
        out["RoleARNUpdate"] = value["role_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputLambdaProcessorUpdate:
    out: InputLambdaProcessorUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARNUpdate") is not None:
        out["resource_arn_update"] = data["ResourceARNUpdate"]
    if data.get("RoleARNUpdate") is not None:
        out["role_arn_update"] = data["RoleARNUpdate"]
    return out
