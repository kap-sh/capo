"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterLoggingStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsRedshiftClusterLoggingStatus(TypedDict, closed=True):
    bucket_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the S3 bucket where the log files are stored.</p>"""
    last_failure_message: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The message indicating that the logs failed to be delivered.</p>"""
    last_failure_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The last time when logs failed to be delivered.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    last_successful_delivery_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The last time that logs were delivered successfully.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    logging_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether logging is enabled.</p>"""
    s3_key_prefix: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Provides the prefix applied to the log file names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterLoggingStatus) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "last_failure_message" in value:
        out["LastFailureMessage"] = value["last_failure_message"]
    if "last_failure_time" in value:
        out["LastFailureTime"] = value["last_failure_time"]
    if "last_successful_delivery_time" in value:
        out["LastSuccessfulDeliveryTime"] = value["last_successful_delivery_time"]
    if "logging_enabled" in value:
        out["LoggingEnabled"] = value["logging_enabled"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterLoggingStatus:
    out: AwsRedshiftClusterLoggingStatus = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    if data.get("LastFailureMessage") is not None:
        out["last_failure_message"] = data["LastFailureMessage"]
    if data.get("LastFailureTime") is not None:
        out["last_failure_time"] = data["LastFailureTime"]
    if data.get("LastSuccessfulDeliveryTime") is not None:
        out["last_successful_delivery_time"] = data["LastSuccessfulDeliveryTime"]
    if data.get("LoggingEnabled") is not None:
        out["logging_enabled"] = data["LoggingEnabled"]
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    return out
