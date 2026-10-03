"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AssociateKmsKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.resource_identifier


class AssociateKmsKeyRequest(TypedDict, closed=True):
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p> <p>In your <code>AssociateKmsKey</code> operation, you must specify either the <code>resourceIdentifier</code> parameter or the <code>logGroup</code> parameter, but you can't specify both.</p>"""
    kms_key_id: "capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"
    """<p>The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data. This must be a symmetric KMS key. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms">Amazon Resource Names</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Using Symmetric and Asymmetric Keys</a>.</p>"""
    resource_identifier: NotRequired[
        "capo_cloudwatch_logs.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>Specifies the target for this operation. You must specify one of the following:</p> <ul> <li> <p>Specify the following ARN to have future <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html">GetQueryResults</a> operations in this account encrypt the results with the specified KMS key. Replace <i>REGION</i> and <i>ACCOUNT_ID</i> with your Region and account ID.</p> <p> <code>arn:aws:logs:<i>REGION</i>:<i>ACCOUNT_ID</i>:query-result:*</code> </p> </li> <li> <p>Specify the ARN of a log group to have CloudWatch Logs use the KMS key to encrypt log events that are ingested and stored by that log group. The log group ARN must be in the following format. Replace <i>REGION</i> and <i>ACCOUNT_ID</i> with your Region and account ID.</p> <p> <code>arn:aws:logs:<i>REGION</i>:<i>ACCOUNT_ID</i>:log-group:<i>LOG_GROUP_NAME</i> </code> </p> </li> </ul> <p>In your <code>AssociateKmsKey</code> operation, you must specify either the <code>resourceIdentifier</code> parameter or the <code>logGroup</code> parameter, but you can't specify both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateKmsKeyRequest) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    out["kmsKeyId"] = value["kms_key_id"]
    if "resource_identifier" in value:
        out["resourceIdentifier"] = value["resource_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateKmsKeyRequest:
    out: AssociateKmsKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError("AssociateKmsKeyRequest.kms_key_id required")
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    return out
