"""Generated from Smithy shape ``com.amazonaws.storagegateway#BandwidthRateLimitInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.bandwidth_download_rate_limit
    import capo_storage_gateway.types.bandwidth_upload_rate_limit
    import capo_storage_gateway.types.days_of_week
    import capo_storage_gateway.types.hour_of_day
    import capo_storage_gateway.types.minute_of_hour


class BandwidthRateLimitInterval(TypedDict, closed=True):
    start_hour_of_day: "capo_storage_gateway.types.hour_of_day.HourOfDay"
    """<p> The hour of the day to start the bandwidth rate limit interval. </p>"""
    start_minute_of_hour: "capo_storage_gateway.types.minute_of_hour.MinuteOfHour"
    """<p> The minute of the hour to start the bandwidth rate limit interval. The interval begins at the start of that minute. To begin an interval exactly at the start of the hour, use the value <code>0</code>. </p>"""
    end_hour_of_day: "capo_storage_gateway.types.hour_of_day.HourOfDay"
    """<p> The hour of the day to end the bandwidth rate limit interval. </p>"""
    end_minute_of_hour: "capo_storage_gateway.types.minute_of_hour.MinuteOfHour"
    """<p> The minute of the hour to end the bandwidth rate limit interval. </p> <important> <p> The bandwidth rate limit interval ends at the end of the minute. To end an interval at the end of an hour, use the value <code>59</code>. </p> </important>"""
    days_of_week: "capo_storage_gateway.types.days_of_week.DaysOfWeek"
    """<p> The days of the week component of the bandwidth rate limit interval, represented as ordinal numbers from 0 to 6, where 0 represents Sunday and 6 represents Saturday. </p>"""
    average_upload_rate_limit_in_bits_per_sec: NotRequired[
        "capo_storage_gateway.types.bandwidth_upload_rate_limit.BandwidthUploadRateLimit"
    ]
    """<p> The average upload rate limit component of the bandwidth rate limit interval, in bits per second. This field does not appear in the response if the upload rate limit is not set. </p> <note> <p>For Tape Gateway and Volume Gateway, the minimum value is <code>51200</code>.</p> <p>This field is required for S3 File Gateway, and the minimum value is <code>104857600</code>.</p> </note>"""
    average_download_rate_limit_in_bits_per_sec: NotRequired[
        "capo_storage_gateway.types.bandwidth_download_rate_limit.BandwidthDownloadRateLimit"
    ]
    """<p> The average download rate limit component of the bandwidth rate limit interval, in bits per second. This field does not appear in the response if the download rate limit is not set. </p> <note> <p>S3 File Gateway does not support this feature.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BandwidthRateLimitInterval) -> dict:
    out: dict = {}
    out["StartHourOfDay"] = value["start_hour_of_day"]
    out["StartMinuteOfHour"] = value["start_minute_of_hour"]
    out["EndHourOfDay"] = value["end_hour_of_day"]
    out["EndMinuteOfHour"] = value["end_minute_of_hour"]
    import capo_storage_gateway.types.days_of_week

    out["DaysOfWeek"] = capo_storage_gateway.types.days_of_week.serialize_aws_json_1_1(
        value["days_of_week"]
    )
    if "average_upload_rate_limit_in_bits_per_sec" in value:
        out["AverageUploadRateLimitInBitsPerSec"] = value[
            "average_upload_rate_limit_in_bits_per_sec"
        ]
    if "average_download_rate_limit_in_bits_per_sec" in value:
        out["AverageDownloadRateLimitInBitsPerSec"] = value[
            "average_download_rate_limit_in_bits_per_sec"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> BandwidthRateLimitInterval:
    out: BandwidthRateLimitInterval = {}  # type: ignore[typeddict-item]
    if data.get("StartHourOfDay") is not None:
        out["start_hour_of_day"] = data["StartHourOfDay"]
    else:
        out["start_hour_of_day"] = 0
    if data.get("StartMinuteOfHour") is not None:
        out["start_minute_of_hour"] = data["StartMinuteOfHour"]
    else:
        out["start_minute_of_hour"] = 0
    if data.get("EndHourOfDay") is not None:
        out["end_hour_of_day"] = data["EndHourOfDay"]
    else:
        out["end_hour_of_day"] = 0
    if data.get("EndMinuteOfHour") is not None:
        out["end_minute_of_hour"] = data["EndMinuteOfHour"]
    else:
        out["end_minute_of_hour"] = 0
    if data.get("DaysOfWeek") is not None:
        import capo_storage_gateway.types.days_of_week

        out["days_of_week"] = (
            capo_storage_gateway.types.days_of_week.deserialize_aws_json_1_1(
                data["DaysOfWeek"]
            )
        )
    else:
        out["days_of_week"] = []
    if data.get("AverageUploadRateLimitInBitsPerSec") is not None:
        out["average_upload_rate_limit_in_bits_per_sec"] = data[
            "AverageUploadRateLimitInBitsPerSec"
        ]
    if data.get("AverageDownloadRateLimitInBitsPerSec") is not None:
        out["average_download_rate_limit_in_bits_per_sec"] = data[
            "AverageDownloadRateLimitInBitsPerSec"
        ]
    return out
