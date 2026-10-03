"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.date_time
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.medical_scribe_job_status
    import capo_transcribe.types.medical_scribe_language_code
    import capo_transcribe.types.transcription_job_name


class MedicalScribeJobSummary(TypedDict, closed=True):
    medical_scribe_job_name: NotRequired[
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the Medical Scribe job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    creation_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Medical Scribe job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    start_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time your Medical Scribe job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Medical Scribe job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a Medical Scribe job that finished processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    language_code: NotRequired[
        "capo_transcribe.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The language code used to create your Medical Scribe job. US English (<code>en-US</code>) is the only supported language for Medical Scribe jobs. </p>"""
    medical_scribe_job_status: NotRequired[
        "capo_transcribe.types.medical_scribe_job_status.MedicalScribeJobStatus"
    ]
    """<p>Provides the status of the specified Medical Scribe job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>MedicalScribeOutput</code> If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your Medical Scribe job failed.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>MedicalScribeJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job failed. See also: <a href="https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html">Common Errors</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeJobSummary) -> dict:
    out: dict = {}
    if "medical_scribe_job_name" in value:
        out["MedicalScribeJobName"] = value["medical_scribe_job_name"]
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
        import capo_transcribe.types.medical_scribe_language_code

        out["LanguageCode"] = (
            capo_transcribe.types.medical_scribe_language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "medical_scribe_job_status" in value:
        import capo_transcribe.types.medical_scribe_job_status

        out["MedicalScribeJobStatus"] = (
            capo_transcribe.types.medical_scribe_job_status.serialize_aws_json_1_1(
                value["medical_scribe_job_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribeJobSummary:
    out: MedicalScribeJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("MedicalScribeJobName") is not None:
        out["medical_scribe_job_name"] = data["MedicalScribeJobName"]
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
        import capo_transcribe.types.medical_scribe_language_code

        out["language_code"] = (
            capo_transcribe.types.medical_scribe_language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("MedicalScribeJobStatus") is not None:
        import capo_transcribe.types.medical_scribe_job_status

        out["medical_scribe_job_status"] = (
            capo_transcribe.types.medical_scribe_job_status.deserialize_aws_json_1_1(
                data["MedicalScribeJobStatus"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    return out
