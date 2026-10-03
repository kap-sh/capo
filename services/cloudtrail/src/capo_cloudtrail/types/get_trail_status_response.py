"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetTrailStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.string


class GetTrailStatusResponse(TypedDict, closed=True):
    is_logging: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Whether the CloudTrail trail is currently logging Amazon Web Services API calls.</p>"""
    latest_delivery_error: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver log files to the designated bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html">Error Responses</a> in the Amazon S3 API Reference. </p> <note> <p>This error occurs only when there is a problem with the destination S3 bucket, and does not occur for requests that time out. To resolve the issue, fix the <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html">bucket policy</a> so that CloudTrail can write to the bucket; or create a new bucket and call <code>UpdateTrail</code> to specify the new bucket.</p> </note>"""
    latest_notification_error: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Displays any Amazon SNS error that CloudTrail encountered when attempting to send a notification. For more information about Amazon SNS errors, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/welcome.html">Amazon SNS Developer Guide</a>. </p>"""
    latest_delivery_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Specifies the date and time that CloudTrail last delivered log files to an account's Amazon S3 bucket.</p>"""
    latest_notification_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Specifies the date and time of the most recent Amazon SNS notification that CloudTrail has written a new log file to an account's Amazon S3 bucket.</p>"""
    start_logging_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Specifies the most recent date and time when CloudTrail started recording API calls for an Amazon Web Services account.</p>"""
    stop_logging_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Specifies the most recent date and time when CloudTrail stopped recording API calls for an Amazon Web Services account.</p>"""
    latest_cloud_watch_logs_delivery_error: NotRequired[
        "capo_cloudtrail.types.string.String"
    ]
    """<p>Displays any CloudWatch Logs error that CloudTrail encountered when attempting to deliver logs to CloudWatch Logs.</p>"""
    latest_cloud_watch_logs_delivery_time: NotRequired[
        "capo_cloudtrail.types.date.Date"
    ]
    """<p>Displays the most recent date and time when CloudTrail delivered logs to CloudWatch Logs.</p>"""
    latest_digest_delivery_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>Specifies the date and time that CloudTrail last delivered a digest file to an account's Amazon S3 bucket.</p>"""
    latest_digest_delivery_error: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver a digest file to the designated bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html">Error Responses</a> in the Amazon S3 API Reference. </p> <note> <p>This error occurs only when there is a problem with the destination S3 bucket, and does not occur for requests that time out. To resolve the issue, fix the <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html">bucket policy</a> so that CloudTrail can write to the bucket; or create a new bucket and call <code>UpdateTrail</code> to specify the new bucket.</p> </note>"""
    latest_delivery_attempt_time: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>This field is no longer in use.</p>"""
    latest_notification_attempt_time: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>This field is no longer in use.</p>"""
    latest_notification_attempt_succeeded: NotRequired[
        "capo_cloudtrail.types.string.String"
    ]
    """<p>This field is no longer in use.</p>"""
    latest_delivery_attempt_succeeded: NotRequired[
        "capo_cloudtrail.types.string.String"
    ]
    """<p>This field is no longer in use.</p>"""
    time_logging_started: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>This field is no longer in use.</p>"""
    time_logging_stopped: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>This field is no longer in use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTrailStatusResponse) -> dict:
    out: dict = {}
    if "is_logging" in value:
        out["IsLogging"] = value["is_logging"]
    if "latest_delivery_error" in value:
        out["LatestDeliveryError"] = value["latest_delivery_error"]
    if "latest_notification_error" in value:
        out["LatestNotificationError"] = value["latest_notification_error"]
    if "latest_delivery_time" in value:
        import capo_cloudtrail.types.date

        out["LatestDeliveryTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["latest_delivery_time"]
        )
    if "latest_notification_time" in value:
        import capo_cloudtrail.types.date

        out["LatestNotificationTime"] = (
            capo_cloudtrail.types.date.serialize_aws_json_1_1(
                value["latest_notification_time"]
            )
        )
    if "start_logging_time" in value:
        import capo_cloudtrail.types.date

        out["StartLoggingTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["start_logging_time"]
        )
    if "stop_logging_time" in value:
        import capo_cloudtrail.types.date

        out["StopLoggingTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["stop_logging_time"]
        )
    if "latest_cloud_watch_logs_delivery_error" in value:
        out["LatestCloudWatchLogsDeliveryError"] = value[
            "latest_cloud_watch_logs_delivery_error"
        ]
    if "latest_cloud_watch_logs_delivery_time" in value:
        import capo_cloudtrail.types.date

        out["LatestCloudWatchLogsDeliveryTime"] = (
            capo_cloudtrail.types.date.serialize_aws_json_1_1(
                value["latest_cloud_watch_logs_delivery_time"]
            )
        )
    if "latest_digest_delivery_time" in value:
        import capo_cloudtrail.types.date

        out["LatestDigestDeliveryTime"] = (
            capo_cloudtrail.types.date.serialize_aws_json_1_1(
                value["latest_digest_delivery_time"]
            )
        )
    if "latest_digest_delivery_error" in value:
        out["LatestDigestDeliveryError"] = value["latest_digest_delivery_error"]
    if "latest_delivery_attempt_time" in value:
        out["LatestDeliveryAttemptTime"] = value["latest_delivery_attempt_time"]
    if "latest_notification_attempt_time" in value:
        out["LatestNotificationAttemptTime"] = value["latest_notification_attempt_time"]
    if "latest_notification_attempt_succeeded" in value:
        out["LatestNotificationAttemptSucceeded"] = value[
            "latest_notification_attempt_succeeded"
        ]
    if "latest_delivery_attempt_succeeded" in value:
        out["LatestDeliveryAttemptSucceeded"] = value[
            "latest_delivery_attempt_succeeded"
        ]
    if "time_logging_started" in value:
        out["TimeLoggingStarted"] = value["time_logging_started"]
    if "time_logging_stopped" in value:
        out["TimeLoggingStopped"] = value["time_logging_stopped"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTrailStatusResponse:
    out: GetTrailStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("IsLogging") is not None:
        out["is_logging"] = data["IsLogging"]
    if data.get("LatestDeliveryError") is not None:
        out["latest_delivery_error"] = data["LatestDeliveryError"]
    if data.get("LatestNotificationError") is not None:
        out["latest_notification_error"] = data["LatestNotificationError"]
    if data.get("LatestDeliveryTime") is not None:
        import capo_cloudtrail.types.date

        out["latest_delivery_time"] = (
            capo_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["LatestDeliveryTime"]
            )
        )
    if data.get("LatestNotificationTime") is not None:
        import capo_cloudtrail.types.date

        out["latest_notification_time"] = (
            capo_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["LatestNotificationTime"]
            )
        )
    if data.get("StartLoggingTime") is not None:
        import capo_cloudtrail.types.date

        out["start_logging_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["StartLoggingTime"]
        )
    if data.get("StopLoggingTime") is not None:
        import capo_cloudtrail.types.date

        out["stop_logging_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["StopLoggingTime"]
        )
    if data.get("LatestCloudWatchLogsDeliveryError") is not None:
        out["latest_cloud_watch_logs_delivery_error"] = data[
            "LatestCloudWatchLogsDeliveryError"
        ]
    if data.get("LatestCloudWatchLogsDeliveryTime") is not None:
        import capo_cloudtrail.types.date

        out["latest_cloud_watch_logs_delivery_time"] = (
            capo_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["LatestCloudWatchLogsDeliveryTime"]
            )
        )
    if data.get("LatestDigestDeliveryTime") is not None:
        import capo_cloudtrail.types.date

        out["latest_digest_delivery_time"] = (
            capo_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["LatestDigestDeliveryTime"]
            )
        )
    if data.get("LatestDigestDeliveryError") is not None:
        out["latest_digest_delivery_error"] = data["LatestDigestDeliveryError"]
    if data.get("LatestDeliveryAttemptTime") is not None:
        out["latest_delivery_attempt_time"] = data["LatestDeliveryAttemptTime"]
    if data.get("LatestNotificationAttemptTime") is not None:
        out["latest_notification_attempt_time"] = data["LatestNotificationAttemptTime"]
    if data.get("LatestNotificationAttemptSucceeded") is not None:
        out["latest_notification_attempt_succeeded"] = data[
            "LatestNotificationAttemptSucceeded"
        ]
    if data.get("LatestDeliveryAttemptSucceeded") is not None:
        out["latest_delivery_attempt_succeeded"] = data[
            "LatestDeliveryAttemptSucceeded"
        ]
    if data.get("TimeLoggingStarted") is not None:
        out["time_logging_started"] = data["TimeLoggingStarted"]
    if data.get("TimeLoggingStopped") is not None:
        out["time_logging_stopped"] = data["TimeLoggingStopped"]
    return out
