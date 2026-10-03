"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalTranscriptionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.date_time
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.language_code
    import capo_transcribe.types.medical_content_identification_type
    import capo_transcribe.types.output_location_type
    import capo_transcribe.types.specialty
    import capo_transcribe.types.transcription_job_name
    import capo_transcribe.types.transcription_job_status
    import capo_transcribe.types.type


class MedicalTranscriptionJobSummary(TypedDict, closed=True):
    medical_transcription_job_name: NotRequired[
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the medical transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    creation_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified medical transcription job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    start_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time your medical transcription job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified medical transcription job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:33:13.922000-07:00</code> represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code used to create your medical transcription. US English (<code>en-US</code>) is the only supported language for medical transcriptions.</p>"""
    transcription_job_status: NotRequired[
        "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Provides the status of your medical transcription job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>TranscriptionJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job failed. See also: <a href="https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html">Common Errors</a>.</p>"""
    output_location_type: NotRequired[
        "capo_transcribe.types.output_location_type.OutputLocationType"
    ]
    """<p>Indicates where the specified medical transcription output is stored.</p> <p>If the value is <code>CUSTOMER_BUCKET</code>, the location is the Amazon S3 bucket you specified using the <code>OutputBucketName</code> parameter in your request. If you also included <code>OutputKey</code> in your request, your output is located in the path you specified in your request.</p> <p>If the value is <code>SERVICE_BUCKET</code>, the location is a service-managed Amazon S3 bucket. To access a transcript stored in a service-managed bucket, use the URI shown in the <code>TranscriptFileUri</code> field.</p>"""
    specialty: NotRequired["capo_transcribe.types.specialty.Specialty"]
    """<p>Provides the medical specialty represented in your media.</p>"""
    content_identification_type: NotRequired[
        "capo_transcribe.types.medical_content_identification_type.MedicalContentIdentificationType"
    ]
    """<p>Labels all personal health information (PHI) identified in your transcript. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html">Identifying personal health information (PHI) in a transcription</a>.</p>"""
    type: NotRequired["capo_transcribe.types.type.Type"]
    """<p>Indicates whether the input media is a dictation or a conversation, as specified in the <code>StartMedicalTranscriptionJob</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalTranscriptionJobSummary) -> dict:
    out: dict = {}
    if "medical_transcription_job_name" in value:
        out["MedicalTranscriptionJobName"] = value["medical_transcription_job_name"]
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
    if "transcription_job_status" in value:
        import capo_transcribe.types.transcription_job_status

        out["TranscriptionJobStatus"] = (
            capo_transcribe.types.transcription_job_status.serialize_aws_json_1_1(
                value["transcription_job_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "output_location_type" in value:
        import capo_transcribe.types.output_location_type

        out["OutputLocationType"] = (
            capo_transcribe.types.output_location_type.serialize_aws_json_1_1(
                value["output_location_type"]
            )
        )
    if "specialty" in value:
        import capo_transcribe.types.specialty

        out["Specialty"] = capo_transcribe.types.specialty.serialize_aws_json_1_1(
            value["specialty"]
        )
    if "content_identification_type" in value:
        import capo_transcribe.types.medical_content_identification_type

        out["ContentIdentificationType"] = (
            capo_transcribe.types.medical_content_identification_type.serialize_aws_json_1_1(
                value["content_identification_type"]
            )
        )
    if "type" in value:
        import capo_transcribe.types.type

        out["Type"] = capo_transcribe.types.type.serialize_aws_json_1_1(value["type"])
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalTranscriptionJobSummary:
    out: MedicalTranscriptionJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("MedicalTranscriptionJobName") is not None:
        out["medical_transcription_job_name"] = data["MedicalTranscriptionJobName"]
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
    if data.get("TranscriptionJobStatus") is not None:
        import capo_transcribe.types.transcription_job_status

        out["transcription_job_status"] = (
            capo_transcribe.types.transcription_job_status.deserialize_aws_json_1_1(
                data["TranscriptionJobStatus"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("OutputLocationType") is not None:
        import capo_transcribe.types.output_location_type

        out["output_location_type"] = (
            capo_transcribe.types.output_location_type.deserialize_aws_json_1_1(
                data["OutputLocationType"]
            )
        )
    if data.get("Specialty") is not None:
        import capo_transcribe.types.specialty

        out["specialty"] = capo_transcribe.types.specialty.deserialize_aws_json_1_1(
            data["Specialty"]
        )
    if data.get("ContentIdentificationType") is not None:
        import capo_transcribe.types.medical_content_identification_type

        out["content_identification_type"] = (
            capo_transcribe.types.medical_content_identification_type.deserialize_aws_json_1_1(
                data["ContentIdentificationType"]
            )
        )
    if data.get("Type") is not None:
        import capo_transcribe.types.type

        out["type"] = capo_transcribe.types.type.deserialize_aws_json_1_1(data["Type"])
    return out
