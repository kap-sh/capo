"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#LambdaOutputUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.resource_arn
    import capo_kinesis_analytics.types.role_arn


class LambdaOutputUpdate(TypedDict, closed=True):
    resource_arn_update: NotRequired[
        "capo_kinesis_analytics.types.resource_arn.ResourceARN"
    ]
    """<p>Amazon Resource Name (ARN) of the destination Lambda function.</p> <note> <p>To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda">Example ARNs: AWS Lambda</a> </p> </note>"""
    role_arn_update: NotRequired["capo_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function on your behalf. You need to grant the necessary permissions to this role. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaOutputUpdate) -> dict:
    out: dict = {}
    if "resource_arn_update" in value:
        out["ResourceARNUpdate"] = value["resource_arn_update"]
    if "role_arn_update" in value:
        out["RoleARNUpdate"] = value["role_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaOutputUpdate:
    out: LambdaOutputUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARNUpdate") is not None:
        out["resource_arn_update"] = data["ResourceARNUpdate"]
    if data.get("RoleARNUpdate") is not None:
        out["role_arn_update"] = data["RoleARNUpdate"]
    return out
