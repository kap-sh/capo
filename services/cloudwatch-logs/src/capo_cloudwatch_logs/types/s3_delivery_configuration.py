"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#S3DeliveryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.boolean
    import capo_cloudwatch_logs.types.delivery_suffix_path


class S3DeliveryConfiguration(TypedDict, closed=True):
    suffix_path: NotRequired[
        "capo_cloudwatch_logs.types.delivery_suffix_path.DeliverySuffixPath"
    ]
    """<p>This string allows re-configuring the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path vary by log type. To find the values supported for the suffix path for each log type, use the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html">DescribeConfigurationTemplates</a> operation and check the <code>allowedSuffixPathFields</code> field in the response. For more information about how the destination prefix, suffix path, and Hive-compatible setting determine the Amazon S3 object key, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html#AWS-logs-infrastructure-V2-S3-object-key">Amazon S3 object key for V2 deliveries</a>.</p>"""
    enable_hive_compatible_path: NotRequired[
        "capo_cloudwatch_logs.types.boolean.Boolean"
    ]
    """<p>This parameter causes the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DeliveryConfiguration) -> dict:
    out: dict = {}
    if "suffix_path" in value:
        out["suffixPath"] = value["suffix_path"]
    if "enable_hive_compatible_path" in value:
        out["enableHiveCompatiblePath"] = value["enable_hive_compatible_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DeliveryConfiguration:
    out: S3DeliveryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("suffixPath") is not None:
        out["suffix_path"] = data["suffixPath"]
    if data.get("enableHiveCompatiblePath") is not None:
        out["enable_hive_compatible_path"] = data["enableHiveCompatiblePath"]
    return out
