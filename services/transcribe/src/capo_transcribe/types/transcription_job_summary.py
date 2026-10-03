"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.boolean
    import capo_transcribe.types.content_redaction
    import capo_transcribe.types.date_time
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.identified_language_score
    import capo_transcribe.types.language_code
    import capo_transcribe.types.language_code_list
    import capo_transcribe.types.model_settings
    import capo_transcribe.types.output_location_type
    import capo_transcribe.types.toxicity_detection
    import capo_transcribe.types.transcription_job_name
    import capo_transcribe.types.transcription_job_status


class TranscriptionJobSummary(TypedDict, closed=True):
    transcription_job_name: NotRequired[
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    creation_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified transcription job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    start_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time your transcription job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified transcription job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:33:13.922000-07:00</code> represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code used to create your transcription.</p>"""
    transcription_job_status: NotRequired[
        "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Provides the status of your transcription job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code> (or <code>RedactedTranscriptFileUri</code>, if you requested transcript redaction). If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>TranscriptionJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job failed. See also: <a href="https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html">Common Errors</a>.</p>"""
    output_location_type: NotRequired[
        "capo_transcribe.types.output_location_type.OutputLocationType"
    ]
    """<p>Indicates where the specified transcription output is stored.</p> <p>If the value is <code>CUSTOMER_BUCKET</code>, the location is the Amazon S3 bucket you specified using the <code>OutputBucketName</code> parameter in your request. If you also included <code>OutputKey</code> in your request, your output is located in the path you specified in your request.</p> <p>If the value is <code>SERVICE_BUCKET</code>, the location is a service-managed Amazon S3 bucket. To access a transcript stored in a service-managed bucket, use the URI shown in the <code>TranscriptFileUri</code> or <code>RedactedTranscriptFileUri</code> field.</p>"""
    content_redaction: NotRequired[
        "capo_transcribe.types.content_redaction.ContentRedaction"
    ]
    """<p>The content redaction settings of the transcription job.</p>"""
    model_settings: NotRequired["capo_transcribe.types.model_settings.ModelSettings"]
    identify_language: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Indicates whether automatic language identification was enabled (<code>TRUE</code>) for the specified transcription job.</p>"""
    identify_multiple_languages: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Indicates whether automatic multi-language identification was enabled (<code>TRUE</code>) for the specified transcription job.</p>"""
    identified_language_score: NotRequired[
        "capo_transcribe.types.identified_language_score.IdentifiedLanguageScore"
    ]
    """<p>The confidence score associated with the language identified in your media file.</p> <p>Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.</p>"""
    language_codes: NotRequired[
        "capo_transcribe.types.language_code_list.LanguageCodeList"
    ]
    """<p>The language codes used to create your transcription job. This parameter is used with multi-language identification. For single-language identification, the singular version of this parameter, <code>LanguageCode</code>, is present.</p>"""
    toxicity_detection: NotRequired[
        "capo_transcribe.types.toxicity_detection.ToxicityDetection"
    ]
    """<p>Indicates whether toxicity detection was enabled for the specified transcription job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranscriptionJobSummary) -> dict:
    out: dict = {}
    if "transcription_job_name" in value:
        out["TranscriptionJobName"] = value["transcription_job_name"]
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
    if "content_redaction" in value:
        import capo_transcribe.types.content_redaction

        out["ContentRedaction"] = (
            capo_transcribe.types.content_redaction.serialize_aws_json_1_1(
                value["content_redaction"]
            )
        )
    if "model_settings" in value:
        import capo_transcribe.types.model_settings

        out["ModelSettings"] = (
            capo_transcribe.types.model_settings.serialize_aws_json_1_1(
                value["model_settings"]
            )
        )
    if "identify_language" in value:
        out["IdentifyLanguage"] = value["identify_language"]
    if "identify_multiple_languages" in value:
        out["IdentifyMultipleLanguages"] = value["identify_multiple_languages"]
    if "identified_language_score" in value:
        out["IdentifiedLanguageScore"] = (
            "NaN"
            if value["identified_language_score"] != value["identified_language_score"]
            else "Infinity"
            if value["identified_language_score"] == float("inf")
            else "-Infinity"
            if value["identified_language_score"] == float("-inf")
            else value["identified_language_score"]
        )
    if "language_codes" in value:
        import capo_transcribe.types.language_code_list

        out["LanguageCodes"] = (
            capo_transcribe.types.language_code_list.serialize_aws_json_1_1(
                value["language_codes"]
            )
        )
    if "toxicity_detection" in value:
        import capo_transcribe.types.toxicity_detection

        out["ToxicityDetection"] = (
            capo_transcribe.types.toxicity_detection.serialize_aws_json_1_1(
                value["toxicity_detection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranscriptionJobSummary:
    out: TranscriptionJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptionJobName") is not None:
        out["transcription_job_name"] = data["TranscriptionJobName"]
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
    if data.get("ContentRedaction") is not None:
        import capo_transcribe.types.content_redaction

        out["content_redaction"] = (
            capo_transcribe.types.content_redaction.deserialize_aws_json_1_1(
                data["ContentRedaction"]
            )
        )
    if data.get("ModelSettings") is not None:
        import capo_transcribe.types.model_settings

        out["model_settings"] = (
            capo_transcribe.types.model_settings.deserialize_aws_json_1_1(
                data["ModelSettings"]
            )
        )
    if data.get("IdentifyLanguage") is not None:
        out["identify_language"] = data["IdentifyLanguage"]
    if data.get("IdentifyMultipleLanguages") is not None:
        out["identify_multiple_languages"] = data["IdentifyMultipleLanguages"]
    if data.get("IdentifiedLanguageScore") is not None:
        out["identified_language_score"] = float(data["IdentifiedLanguageScore"])
    if data.get("LanguageCodes") is not None:
        import capo_transcribe.types.language_code_list

        out["language_codes"] = (
            capo_transcribe.types.language_code_list.deserialize_aws_json_1_1(
                data["LanguageCodes"]
            )
        )
    if data.get("ToxicityDetection") is not None:
        import capo_transcribe.types.toxicity_detection

        out["toxicity_detection"] = (
            capo_transcribe.types.toxicity_detection.deserialize_aws_json_1_1(
                data["ToxicityDetection"]
            )
        )
    return out
