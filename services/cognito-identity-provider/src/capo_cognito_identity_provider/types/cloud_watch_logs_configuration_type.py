"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CloudWatchLogsConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type


class CloudWatchLogsConfigurationType(TypedDict, closed=True):
    log_group_arn: NotRequired["capo_cognito_identity_provider.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (arn) of a CloudWatch Logs log group where your user pool sends logs. The log group must not be encrypted with Key Management Service and must be in the same Amazon Web Services account as your user pool.</p> <p>To send logs to log groups with a resource policy of a size greater than 5120 characters, configure a log group with a path that starts with <code>/aws/vendedlogs</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html">Enabling logging from certain Amazon Web Services services</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLogsConfigurationType) -> dict:
    out: dict = {}
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLogsConfigurationType:
    out: CloudWatchLogsConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("LogGroupArn") is not None:
        out["log_group_arn"] = data["LogGroupArn"]
    return out
