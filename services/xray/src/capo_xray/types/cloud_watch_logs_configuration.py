"""Generated from Smithy shape ``com.amazonaws.xray#CloudWatchLogsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.kms_key_id


class CloudWatchLogsConfiguration(TypedDict, closed=True):
    spans_log_group_kms_key_id: NotRequired["capo_xray.types.kms_key_id.KmsKeyId"]
    """<p> The ARN of an AWS Key Management Service (AWS KMS) key that you create and manage, in the same account and Region, used to encrypt the <code>aws/spans</code> log group. Key IDs and alias ARNs are not supported. </p> <p> X-Ray applies the key only when it creates <code>aws/spans</code>. If the account already has an <code>aws/spans</code> log group, X-Ray fails the request with an <code>InvalidRequestException</code> and does not change the log group. To enable Transaction Search with the existing log group as it is, call <code>UpdateTraceSegmentDestination</code> again without <code>SpansLogGroupKmsKeyId</code>. To set or change the key of the existing log group, use the CloudWatch Logs <code>AssociateKmsKey</code> operation. </p> <p> You need <code>kms:DescribeKey</code> permission on the key, and the key policy must allow CloudWatch Logs to use the key. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html">Encrypt log data in CloudWatch Logs using AWS Key Management Service</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsConfiguration) -> dict:
    out: dict = {}
    if "spans_log_group_kms_key_id" in value:
        out["SpansLogGroupKmsKeyId"] = value["spans_log_group_kms_key_id"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogsConfiguration:
    out: CloudWatchLogsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SpansLogGroupKmsKeyId") is not None:
        out["spans_log_group_kms_key_id"] = data["SpansLogGroupKmsKeyId"]
    return out
