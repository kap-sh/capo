"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputLambdaProcessorDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.resource_arn
    import capo_kinesis_analytics_v2.types.role_arn


class InputLambdaProcessorDescription(TypedDict, closed=True):
    resource_arn: "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The ARN of the Amazon Lambda function that is used to preprocess the records in the stream.</p> <note> <p>To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda">Example ARNs: Amazon Lambda</a> </p> </note>"""
    role_arn: NotRequired["capo_kinesis_analytics_v2.types.role_arn.RoleARN"]
    """<p>The ARN of the IAM role that is used to access the Amazon Lambda function.</p> <note> <p>Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLambdaProcessorDescription) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputLambdaProcessorDescription:
    out: InputLambdaProcessorDescription = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError(
            "InputLambdaProcessorDescription.resource_arn required"
        )
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    return out
