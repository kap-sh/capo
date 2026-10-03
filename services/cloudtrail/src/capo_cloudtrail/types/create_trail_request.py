"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateTrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.string
    import capo_cloudtrail.types.tags_list


class CreateTrailRequest(TypedDict, closed=True):
    name: "capo_cloudtrail.types.string.String"
    """<p>Specifies the name of the trail. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul>"""
    s3_bucket_name: "capo_cloudtrail.types.string.String"
    """<p>Specifies the name of the Amazon S3 bucket designated for publishing log files. For information about bucket naming rules, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html">Bucket naming rules</a> in the <i>Amazon Simple Storage Service User Guide</i>. </p>"""
    s3_key_prefix: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files">Finding Your CloudTrail Log Files</a>. The maximum length is 200 characters.</p>"""
    sns_topic_name: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the name or ARN of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.</p>"""
    include_global_service_events: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail is publishing events from global services such as IAM to the log files. Setting this value to <code>true</code> only delivers global service events to the trail if the trail is multi-Region or if the trail's home Region is the partition leader Region (for example, us-east-1).</p>"""
    is_multi_region_trail: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail is created in the current Region or in all Regions. The default is false, which creates a trail only in the Region where you are signed in. As a best practice, consider creating trails that log events in all Regions.</p>"""
    enable_log_file_validation: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether log file integrity validation is enabled. The default is false.</p> <note> <p>When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail does not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.</p> </note>"""
    cloud_watch_logs_log_group_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. You must use a log group that exists in your account.</p> <p>Not required unless you specify <code>CloudWatchLogsRoleArn</code>.</p>"""
    cloud_watch_logs_role_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group. You must use a role that exists in your account.</p>"""
    kms_key_id: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the KMS key ID to use to encrypt the logs and digest files delivered by CloudTrail. The value can be an alias name prefixed by <code>alias/</code>, a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</p> <p>CloudTrail also supports KMS multi-Region keys. For more information about multi-Region keys, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html">Using multi-Region keys</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>Examples:</p> <ul> <li> <p> <code>alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:alias/MyAliasName</code> </p> </li> <li> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p> </li> <li> <p> <code>12345678-1234-1234-1234-123456789012</code> </p> </li> </ul>"""
    is_organization_trail: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail is created for all accounts in an organization in Organizations, or only for the current Amazon Web Services account. The default is false, and cannot be true unless the call is made on behalf of an Amazon Web Services account that is the management account or delegated administrator account for an organization in Organizations.</p>"""
    tags_list: NotRequired["capo_cloudtrail.types.tags_list.TagsList"]
    recursive_logging: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether recursive logging is enabled for the trail. If you set <code>RecursiveLogging</code> to <code>false</code>, CloudTrail suppresses events generated by CloudTrail when it delivers log files to your trail's destinations, including Amazon S3 and CloudWatch Logs. The default value is <code>true</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrailRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    if "sns_topic_name" in value:
        out["SnsTopicName"] = value["sns_topic_name"]
    if "include_global_service_events" in value:
        out["IncludeGlobalServiceEvents"] = value["include_global_service_events"]
    if "is_multi_region_trail" in value:
        out["IsMultiRegionTrail"] = value["is_multi_region_trail"]
    if "enable_log_file_validation" in value:
        out["EnableLogFileValidation"] = value["enable_log_file_validation"]
    if "cloud_watch_logs_log_group_arn" in value:
        out["CloudWatchLogsLogGroupArn"] = value["cloud_watch_logs_log_group_arn"]
    if "cloud_watch_logs_role_arn" in value:
        out["CloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "is_organization_trail" in value:
        out["IsOrganizationTrail"] = value["is_organization_trail"]
    if "tags_list" in value:
        import capo_cloudtrail.types.tags_list

        out["TagsList"] = capo_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags_list"]
        )
    if "recursive_logging" in value:
        out["RecursiveLogging"] = value["recursive_logging"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrailRequest:
    out: CreateTrailRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateTrailRequest.name required")
    if data.get("S3BucketName") is not None:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        raise DeserializationError("CreateTrailRequest.s3_bucket_name required")
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    if data.get("SnsTopicName") is not None:
        out["sns_topic_name"] = data["SnsTopicName"]
    if data.get("IncludeGlobalServiceEvents") is not None:
        out["include_global_service_events"] = data["IncludeGlobalServiceEvents"]
    if data.get("IsMultiRegionTrail") is not None:
        out["is_multi_region_trail"] = data["IsMultiRegionTrail"]
    if data.get("EnableLogFileValidation") is not None:
        out["enable_log_file_validation"] = data["EnableLogFileValidation"]
    if data.get("CloudWatchLogsLogGroupArn") is not None:
        out["cloud_watch_logs_log_group_arn"] = data["CloudWatchLogsLogGroupArn"]
    if data.get("CloudWatchLogsRoleArn") is not None:
        out["cloud_watch_logs_role_arn"] = data["CloudWatchLogsRoleArn"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("IsOrganizationTrail") is not None:
        out["is_organization_trail"] = data["IsOrganizationTrail"]
    if data.get("TagsList") is not None:
        import capo_cloudtrail.types.tags_list

        out["tags_list"] = capo_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["TagsList"]
        )
    if data.get("RecursiveLogging") is not None:
        out["recursive_logging"] = data["RecursiveLogging"]
    return out
