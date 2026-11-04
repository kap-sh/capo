"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.bearer_token_authentication_enabled
    import capo_cloudwatch_logs.types.data_protection_status
    import capo_cloudwatch_logs.types.days
    import capo_cloudwatch_logs.types.deletion_protection_enabled
    import capo_cloudwatch_logs.types.filter_count
    import capo_cloudwatch_logs.types.inherited_properties
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.log_group_class
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.stored_bytes
    import capo_cloudwatch_logs.types.timestamp


class LogGroup(TypedDict, closed=True):
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p>"""
    creation_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""
    retention_in_days: NotRequired["capo_cloudwatch_logs.types.days.Days"]
    metric_filter_count: NotRequired[
        "capo_cloudwatch_logs.types.filter_count.FilterCount"
    ]
    """<p>The number of metric filters.</p>"""
    arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the log group. This version of the ARN includes a trailing <code>:*</code> after the log group name. </p> <p>Use this version to refer to the ARN in IAM policies when specifying permissions for most API actions. The exception is when specifying permissions for <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html">TagResource</a>, <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html">UntagResource</a>, and <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html">ListTagsForResource</a>. The permissions for those three actions require the ARN version that doesn't include a trailing <code>:*</code>.</p>"""
    stored_bytes: NotRequired["capo_cloudwatch_logs.types.stored_bytes.StoredBytes"]
    """<p>The number of bytes stored.</p>"""
    kms_key_id: NotRequired["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data.</p>"""
    data_protection_status: NotRequired[
        "capo_cloudwatch_logs.types.data_protection_status.DataProtectionStatus"
    ]
    """<p>Displays whether this log group has a protection policy, or whether it had one in the past. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html">PutDataProtectionPolicy</a>.</p>"""
    inherited_properties: NotRequired[
        "capo_cloudwatch_logs.types.inherited_properties.InheritedProperties"
    ]
    """<p>Displays all the properties that this log group has inherited from account-level settings.</p>"""
    log_group_class: NotRequired[
        "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
    ]
    """<p>This specifies the log group class for this log group. There are three classes:</p> <ul> <li> <p>The <code>Standard</code> log class supports all CloudWatch Logs features.</p> </li> <li> <p>The <code>Infrequent Access</code> log class supports a subset of CloudWatch Logs features and incurs lower costs.</p> </li> <li> <p>Use the <code>Delivery</code> log class only for delivering Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.</p> </li> </ul> <p>For details about the features supported by the Standard and Infrequent Access classes, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html">Log classes</a> </p>"""
    log_group_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the log group. This version of the ARN doesn't include a trailing <code>:*</code> after the log group name. </p> <p>Use this version to refer to the ARN in the following situations:</p> <ul> <li> <p>In the <code>logGroupIdentifier</code> input field in many CloudWatch Logs APIs.</p> </li> <li> <p>In the <code>resourceArn</code> field in tagging APIs</p> </li> <li> <p>In IAM policies, when specifying permissions for <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html">TagResource</a>, <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html">UntagResource</a>, and <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html">ListTagsForResource</a>.</p> </li> </ul>"""
    deletion_protection_enabled: NotRequired[
        "capo_cloudwatch_logs.types.deletion_protection_enabled.DeletionProtectionEnabled"
    ]
    """<p>Indicates whether deletion protection is enabled for this log group. When enabled, deletion protection blocks all deletion operations until it is explicitly disabled.</p>"""
    bearer_token_authentication_enabled: NotRequired[
        "capo_cloudwatch_logs.types.bearer_token_authentication_enabled.BearerTokenAuthenticationEnabled"
    ]
    """<p>Indicates whether bearer token authentication is enabled for this log group. When enabled, bearer token authentication is allowed on operations until it is explicitly disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroup) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "retention_in_days" in value:
        out["retentionInDays"] = value["retention_in_days"]
    if "metric_filter_count" in value:
        out["metricFilterCount"] = value["metric_filter_count"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "stored_bytes" in value:
        out["storedBytes"] = value["stored_bytes"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "data_protection_status" in value:
        import capo_cloudwatch_logs.types.data_protection_status

        out["dataProtectionStatus"] = (
            capo_cloudwatch_logs.types.data_protection_status.serialize_aws_json_1_1(
                value["data_protection_status"]
            )
        )
    if "inherited_properties" in value:
        import capo_cloudwatch_logs.types.inherited_properties

        out["inheritedProperties"] = (
            capo_cloudwatch_logs.types.inherited_properties.serialize_aws_json_1_1(
                value["inherited_properties"]
            )
        )
    if "log_group_class" in value:
        import capo_cloudwatch_logs.types.log_group_class

        out["logGroupClass"] = (
            capo_cloudwatch_logs.types.log_group_class.serialize_aws_json_1_1(
                value["log_group_class"]
            )
        )
    if "log_group_arn" in value:
        out["logGroupArn"] = value["log_group_arn"]
    if "deletion_protection_enabled" in value:
        out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "bearer_token_authentication_enabled" in value:
        out["bearerTokenAuthenticationEnabled"] = value[
            "bearer_token_authentication_enabled"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> LogGroup:
    out: LogGroup = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("creationTime") is not None:
        out["creation_time"] = data["creationTime"]
    if data.get("retentionInDays") is not None:
        out["retention_in_days"] = data["retentionInDays"]
    if data.get("metricFilterCount") is not None:
        out["metric_filter_count"] = data["metricFilterCount"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("storedBytes") is not None:
        out["stored_bytes"] = data["storedBytes"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("dataProtectionStatus") is not None:
        import capo_cloudwatch_logs.types.data_protection_status

        out["data_protection_status"] = (
            capo_cloudwatch_logs.types.data_protection_status.deserialize_aws_json_1_1(
                data["dataProtectionStatus"]
            )
        )
    if data.get("inheritedProperties") is not None:
        import capo_cloudwatch_logs.types.inherited_properties

        out["inherited_properties"] = (
            capo_cloudwatch_logs.types.inherited_properties.deserialize_aws_json_1_1(
                data["inheritedProperties"]
            )
        )
    if data.get("logGroupClass") is not None:
        import capo_cloudwatch_logs.types.log_group_class

        out["log_group_class"] = (
            capo_cloudwatch_logs.types.log_group_class.deserialize_aws_json_1_1(
                data["logGroupClass"]
            )
        )
    if data.get("logGroupArn") is not None:
        out["log_group_arn"] = data["logGroupArn"]
    if data.get("deletionProtectionEnabled") is not None:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    if data.get("bearerTokenAuthenticationEnabled") is not None:
        out["bearer_token_authentication_enabled"] = data[
            "bearerTokenAuthenticationEnabled"
        ]
    return out
