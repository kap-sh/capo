"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputLambdaProcessorDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.resource_arn
    import capo_kinesis_analytics.types.role_arn


class InputLambdaProcessorDescription(TypedDict, closed=True):
    resource_arn: NotRequired["capo_kinesis_analytics.types.resource_arn.ResourceARN"]
    """<p>The ARN of the <a href="https://docs.aws.amazon.com/lambda/">AWS Lambda</a> function that is used to preprocess the records in the stream.</p>"""
    role_arn: NotRequired["capo_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>The ARN of the IAM role that is used to access the AWS Lambda function.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLambdaProcessorDescription) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputLambdaProcessorDescription:
    out: InputLambdaProcessorDescription = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    return out
