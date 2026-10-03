"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DisassociateKmsKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.resource_identifier


class DisassociateKmsKeyRequest(TypedDict, closed=True):
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p> <p>In your <code>DisassociateKmsKey</code> operation, you must specify either the <code>resourceIdentifier</code> parameter or the <code>logGroup</code> parameter, but you can't specify both.</p>"""
    resource_identifier: NotRequired[
        "capo_cloudwatch_logs.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>Specifies the target for this operation. You must specify one of the following:</p> <ul> <li> <p>Specify the ARN of a log group to stop having CloudWatch Logs use the KMS key to encrypt log events that are ingested and stored by that log group. After you run this operation, CloudWatch Logs encrypts ingested log events with the default CloudWatch Logs method. The log group ARN must be in the following format. Replace <i>REGION</i> and <i>ACCOUNT_ID</i> with your Region and account ID.</p> <p> <code>arn:aws:logs:<i>REGION</i>:<i>ACCOUNT_ID</i>:log-group:<i>LOG_GROUP_NAME</i> </code> </p> </li> <li> <p>Specify the following ARN to stop using this key to encrypt the results of future <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html">StartQuery</a> operations in this account. Replace <i>REGION</i> and <i>ACCOUNT_ID</i> with your Region and account ID.</p> <p> <code>arn:aws:logs:<i>REGION</i>:<i>ACCOUNT_ID</i>:query-result:*</code> </p> </li> </ul> <p>In your <code>DisssociateKmsKey</code> operation, you must specify either the <code>resourceIdentifier</code> parameter or the <code>logGroup</code> parameter, but you can't specify both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateKmsKeyRequest) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "resource_identifier" in value:
        out["resourceIdentifier"] = value["resource_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateKmsKeyRequest:
    out: DisassociateKmsKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    return out
