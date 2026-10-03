"""Generated from Smithy shape ``com.amazonaws.cloudtrail#UpdateTrailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.string


class UpdateTrailResponse(TypedDict, closed=True):
    name: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the name of the trail.</p>"""
    s3_bucket_name: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the name of the Amazon S3 bucket designated for publishing log files.</p>"""
    s3_key_prefix: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files">Finding Your IAM Log Files</a>.</p>"""
    sns_topic_name: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>This field is no longer in use. Use <code>SnsTopicARN</code>.</p>"""
    sns_topic_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The following is the format of a topic ARN.</p> <p> <code>arn:aws:sns:us-east-2:123456789012:MyTopic</code> </p>"""
    include_global_service_events: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail is publishing events from global services such as IAM to the log files. Setting this value to <code>true</code> only delivers global service events to the trail if the trail is multi-Region or if the trail's home Region is the partition leader Region (for example, us-east-1).</p>"""
    is_multi_region_trail: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail exists in one Region or in all Regions.</p>"""
    trail_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the trail that was updated. The following is the format of a trail ARN.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>"""
    log_file_validation_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether log file integrity validation is enabled.</p>"""
    cloud_watch_logs_log_group_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs are delivered.</p>"""
    cloud_watch_logs_role_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.</p>"""
    kms_key_id: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the KMS key ID that encrypts the logs and digest files delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.</p> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p>"""
    is_organization_trail: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail is an organization trail.</p>"""
    recursive_logging: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether recursive logging is enabled for the trail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrailResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    if "sns_topic_name" in value:
        out["SnsTopicName"] = value["sns_topic_name"]
    if "sns_topic_arn" in value:
        out["SnsTopicARN"] = value["sns_topic_arn"]
    if "include_global_service_events" in value:
        out["IncludeGlobalServiceEvents"] = value["include_global_service_events"]
    if "is_multi_region_trail" in value:
        out["IsMultiRegionTrail"] = value["is_multi_region_trail"]
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "log_file_validation_enabled" in value:
        out["LogFileValidationEnabled"] = value["log_file_validation_enabled"]
    if "cloud_watch_logs_log_group_arn" in value:
        out["CloudWatchLogsLogGroupArn"] = value["cloud_watch_logs_log_group_arn"]
    if "cloud_watch_logs_role_arn" in value:
        out["CloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "is_organization_trail" in value:
        out["IsOrganizationTrail"] = value["is_organization_trail"]
    if "recursive_logging" in value:
        out["RecursiveLogging"] = value["recursive_logging"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrailResponse:
    out: UpdateTrailResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    if data.get("SnsTopicName") is not None:
        out["sns_topic_name"] = data["SnsTopicName"]
    if data.get("SnsTopicARN") is not None:
        out["sns_topic_arn"] = data["SnsTopicARN"]
    if data.get("IncludeGlobalServiceEvents") is not None:
        out["include_global_service_events"] = data["IncludeGlobalServiceEvents"]
    if data.get("IsMultiRegionTrail") is not None:
        out["is_multi_region_trail"] = data["IsMultiRegionTrail"]
    if data.get("TrailARN") is not None:
        out["trail_arn"] = data["TrailARN"]
    if data.get("LogFileValidationEnabled") is not None:
        out["log_file_validation_enabled"] = data["LogFileValidationEnabled"]
    if data.get("CloudWatchLogsLogGroupArn") is not None:
        out["cloud_watch_logs_log_group_arn"] = data["CloudWatchLogsLogGroupArn"]
    if data.get("CloudWatchLogsRoleArn") is not None:
        out["cloud_watch_logs_role_arn"] = data["CloudWatchLogsRoleArn"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("IsOrganizationTrail") is not None:
        out["is_organization_trail"] = data["IsOrganizationTrail"]
    if data.get("RecursiveLogging") is not None:
        out["recursive_logging"] = data["RecursiveLogging"]
    return out
