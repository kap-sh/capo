"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.call_analytics_job_details
    import capo_transcribe.types.call_analytics_job_name
    import capo_transcribe.types.call_analytics_job_status
    import capo_transcribe.types.date_time
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.language_code


class CallAnalyticsJobSummary(TypedDict, closed=True):
    call_analytics_job_name: NotRequired[
        "capo_transcribe.types.call_analytics_job_name.CallAnalyticsJobName"
    ]
    """<p>The name of the Call Analytics job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    creation_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    start_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time your Call Analytics job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:33:13.922000-07:00</code> represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code used to create your Call Analytics transcription.</p>"""
    call_analytics_job_status: NotRequired[
        "capo_transcribe.types.call_analytics_job_status.CallAnalyticsJobStatus"
    ]
    """<p>Provides the status of your Call Analytics job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code> (or <code>RedactedTranscriptFileUri</code>, if you requested transcript redaction). If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>"""
    call_analytics_job_details: NotRequired[
        "capo_transcribe.types.call_analytics_job_details.CallAnalyticsJobDetails"
    ]
    """<p>Provides detailed information about a call analytics job, including information about skipped analytics features.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>CallAnalyticsJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the Call Analytics job failed. See also: <a href="https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html">Common Errors</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsJobSummary) -> dict:
    out: dict = {}
    if "call_analytics_job_name" in value:
        out["CallAnalyticsJobName"] = value["call_analytics_job_name"]
    if "creation_time" in value:
        import capo_transcribe.types.date_time

        out["CreationTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "start_time" in value:
        import capo_transcribe.types.date_time

        out["StartTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "completion_time" in value:
        import capo_transcribe.types.date_time

        out["CompletionTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["completion_time"]
        )
    if "language_code" in value:
        import capo_transcribe.types.language_code

        out["LanguageCode"] = (
            capo_transcribe.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "call_analytics_job_status" in value:
        import capo_transcribe.types.call_analytics_job_status

        out["CallAnalyticsJobStatus"] = (
            capo_transcribe.types.call_analytics_job_status.serialize_aws_json_1_1(
                value["call_analytics_job_status"]
            )
        )
    if "call_analytics_job_details" in value:
        import capo_transcribe.types.call_analytics_job_details

        out["CallAnalyticsJobDetails"] = (
            capo_transcribe.types.call_analytics_job_details.serialize_aws_json_1_1(
                value["call_analytics_job_details"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CallAnalyticsJobSummary:
    out: CallAnalyticsJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("CallAnalyticsJobName") is not None:
        out["call_analytics_job_name"] = data["CallAnalyticsJobName"]
    if data.get("CreationTime") is not None:
        import capo_transcribe.types.date_time

        out["creation_time"] = capo_transcribe.types.date_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("StartTime") is not None:
        import capo_transcribe.types.date_time

        out["start_time"] = capo_transcribe.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("CompletionTime") is not None:
        import capo_transcribe.types.date_time

        out["completion_time"] = (
            capo_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("CallAnalyticsJobStatus") is not None:
        import capo_transcribe.types.call_analytics_job_status

        out["call_analytics_job_status"] = (
            capo_transcribe.types.call_analytics_job_status.deserialize_aws_json_1_1(
                data["CallAnalyticsJobStatus"]
            )
        )
    if data.get("CallAnalyticsJobDetails") is not None:
        import capo_transcribe.types.call_analytics_job_details

        out["call_analytics_job_details"] = (
            capo_transcribe.types.call_analytics_job_details.deserialize_aws_json_1_1(
                data["CallAnalyticsJobDetails"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    return out
