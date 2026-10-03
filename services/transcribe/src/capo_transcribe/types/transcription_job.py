"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptionJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.boolean
    import capo_transcribe.types.content_redaction
    import capo_transcribe.types.date_time
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.identified_language_score
    import capo_transcribe.types.job_execution_settings
    import capo_transcribe.types.language_code
    import capo_transcribe.types.language_code_list
    import capo_transcribe.types.language_id_settings_map
    import capo_transcribe.types.language_options
    import capo_transcribe.types.media
    import capo_transcribe.types.media_format
    import capo_transcribe.types.media_sample_rate_hertz
    import capo_transcribe.types.model_settings
    import capo_transcribe.types.settings
    import capo_transcribe.types.subtitles_output
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.toxicity_detection
    import capo_transcribe.types.transcript
    import capo_transcribe.types.transcription_job_name
    import capo_transcribe.types.transcription_job_status


class TranscriptionJob(TypedDict, closed=True):
    transcription_job_name: NotRequired[
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    transcription_job_status: NotRequired[
        "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Provides the status of the specified transcription job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code> (or <code>RedactedTranscriptFileUri</code>, if you requested transcript redaction). If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code used to create your transcription job. This parameter is used with single-language identification. For multi-language identification requests, refer to the plural version of this parameter, <code>LanguageCodes</code>.</p>"""
    media_sample_rate_hertz: NotRequired[
        "capo_transcribe.types.media_sample_rate_hertz.MediaSampleRateHertz"
    ]
    """<p>The sample rate, in hertz, of the audio track in your input media file.</p>"""
    media_format: NotRequired["capo_transcribe.types.media_format.MediaFormat"]
    """<p>The format of the input media file.</p>"""
    media: NotRequired["capo_transcribe.types.media.Media"]
    """<p>Provides the Amazon S3 location of the media file you used in your request.</p>"""
    transcript: NotRequired["capo_transcribe.types.transcript.Transcript"]
    """<p>Provides you with the Amazon S3 URI you can use to access your transcript.</p>"""
    start_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified transcription job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    creation_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified transcription job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified transcription job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:33:13.922000-07:00</code> represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>TranscriptionJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job request failed.</p> <p>The <code>FailureReason</code> field contains one of the following values:</p> <ul> <li> <p> <code>Unsupported media format</code>.</p> <p>The media format specified in <code>MediaFormat</code> isn't valid. Refer to refer to the <code>MediaFormat</code> parameter for a list of supported formats.</p> </li> <li> <p> <code>The media format provided does not match the detected media format</code>.</p> <p>The media format specified in <code>MediaFormat</code> doesn't match the format of the input file. Check the media format of your media file and correct the specified value.</p> </li> <li> <p> <code>Invalid sample rate for audio file</code>.</p> <p>The sample rate specified in <code>MediaSampleRateHertz</code> isn't valid. The sample rate must be between 8,000 and 48,000 hertz.</p> </li> <li> <p> <code>The sample rate provided does not match the detected sample rate</code>.</p> <p>The sample rate specified in <code>MediaSampleRateHertz</code> doesn't match the sample rate detected in your input media file. Check the sample rate of your media file and correct the specified value.</p> </li> <li> <p> <code>Invalid file size: file size too large</code>.</p> <p>The size of your media file is larger than what Amazon Transcribe can process. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe">Service quotas</a>.</p> </li> <li> <p> <code>Invalid number of channels: number of channels too large</code>.</p> <p>Your audio contains more channels than Amazon Transcribe is able to process. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe">Service quotas</a>.</p> </li> </ul>"""
    settings: NotRequired["capo_transcribe.types.settings.Settings"]
    """<p>Provides information on any additional settings that were included in your request. Additional settings include channel identification, alternative transcriptions, speaker partitioning, custom vocabularies, and custom vocabulary filters.</p>"""
    model_settings: NotRequired["capo_transcribe.types.model_settings.ModelSettings"]
    """<p>Provides information on the custom language model you included in your request.</p>"""
    job_execution_settings: NotRequired[
        "capo_transcribe.types.job_execution_settings.JobExecutionSettings"
    ]
    """<p>Provides information about how your transcription job was processed. This parameter shows if your request was queued and what data access role was used.</p>"""
    content_redaction: NotRequired[
        "capo_transcribe.types.content_redaction.ContentRedaction"
    ]
    """<p>Indicates whether redaction was enabled in your transcript.</p>"""
    identify_language: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Indicates whether automatic language identification was enabled (<code>TRUE</code>) for the specified transcription job.</p>"""
    identify_multiple_languages: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Indicates whether automatic multi-language identification was enabled (<code>TRUE</code>) for the specified transcription job.</p>"""
    language_options: NotRequired[
        "capo_transcribe.types.language_options.LanguageOptions"
    ]
    """<p>Provides the language codes you specified in your request.</p>"""
    identified_language_score: NotRequired[
        "capo_transcribe.types.identified_language_score.IdentifiedLanguageScore"
    ]
    """<p>The confidence score associated with the language identified in your media file.</p> <p>Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.</p>"""
    language_codes: NotRequired[
        "capo_transcribe.types.language_code_list.LanguageCodeList"
    ]
    """<p>The language codes used to create your transcription job. This parameter is used with multi-language identification. For single-language identification requests, refer to the singular version of this parameter, <code>LanguageCode</code>.</p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>The tags, each in the form of a key:value pair, assigned to the specified transcription job.</p>"""
    subtitles: NotRequired["capo_transcribe.types.subtitles_output.SubtitlesOutput"]
    """<p>Indicates whether subtitles were generated with your transcription.</p>"""
    language_id_settings: NotRequired[
        "capo_transcribe.types.language_id_settings_map.LanguageIdSettingsMap"
    ]
    """<p>Provides the name and language of all custom language models, custom vocabularies, and custom vocabulary filters that you included in your request.</p>"""
    toxicity_detection: NotRequired[
        "capo_transcribe.types.toxicity_detection.ToxicityDetection"
    ]
    """<p>Provides information about the toxicity detection settings applied to your transcription.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranscriptionJob) -> dict:
    out: dict = {}
    if "transcription_job_name" in value:
        out["TranscriptionJobName"] = value["transcription_job_name"]
    if "transcription_job_status" in value:
        import capo_transcribe.types.transcription_job_status

        out["TranscriptionJobStatus"] = (
            capo_transcribe.types.transcription_job_status.serialize_aws_json_1_1(
                value["transcription_job_status"]
            )
        )
    if "language_code" in value:
        import capo_transcribe.types.language_code

        out["LanguageCode"] = (
            capo_transcribe.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "media_sample_rate_hertz" in value:
        out["MediaSampleRateHertz"] = value["media_sample_rate_hertz"]
    if "media_format" in value:
        import capo_transcribe.types.media_format

        out["MediaFormat"] = capo_transcribe.types.media_format.serialize_aws_json_1_1(
            value["media_format"]
        )
    if "media" in value:
        import capo_transcribe.types.media

        out["Media"] = capo_transcribe.types.media.serialize_aws_json_1_1(
            value["media"]
        )
    if "transcript" in value:
        import capo_transcribe.types.transcript

        out["Transcript"] = capo_transcribe.types.transcript.serialize_aws_json_1_1(
            value["transcript"]
        )
    if "start_time" in value:
        import capo_transcribe.types.date_time

        out["StartTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "creation_time" in value:
        import capo_transcribe.types.date_time

        out["CreationTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "completion_time" in value:
        import capo_transcribe.types.date_time

        out["CompletionTime"] = capo_transcribe.types.date_time.serialize_aws_json_1_1(
            value["completion_time"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "settings" in value:
        import capo_transcribe.types.settings

        out["Settings"] = capo_transcribe.types.settings.serialize_aws_json_1_1(
            value["settings"]
        )
    if "model_settings" in value:
        import capo_transcribe.types.model_settings

        out["ModelSettings"] = (
            capo_transcribe.types.model_settings.serialize_aws_json_1_1(
                value["model_settings"]
            )
        )
    if "job_execution_settings" in value:
        import capo_transcribe.types.job_execution_settings

        out["JobExecutionSettings"] = (
            capo_transcribe.types.job_execution_settings.serialize_aws_json_1_1(
                value["job_execution_settings"]
            )
        )
    if "content_redaction" in value:
        import capo_transcribe.types.content_redaction

        out["ContentRedaction"] = (
            capo_transcribe.types.content_redaction.serialize_aws_json_1_1(
                value["content_redaction"]
            )
        )
    if "identify_language" in value:
        out["IdentifyLanguage"] = value["identify_language"]
    if "identify_multiple_languages" in value:
        out["IdentifyMultipleLanguages"] = value["identify_multiple_languages"]
    if "language_options" in value:
        import capo_transcribe.types.language_options

        out["LanguageOptions"] = (
            capo_transcribe.types.language_options.serialize_aws_json_1_1(
                value["language_options"]
            )
        )
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
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "subtitles" in value:
        import capo_transcribe.types.subtitles_output

        out["Subtitles"] = (
            capo_transcribe.types.subtitles_output.serialize_aws_json_1_1(
                value["subtitles"]
            )
        )
    if "language_id_settings" in value:
        import capo_transcribe.types.language_id_settings_map

        out["LanguageIdSettings"] = (
            capo_transcribe.types.language_id_settings_map.serialize_aws_json_1_1(
                value["language_id_settings"]
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


def deserialize_aws_json_1_1(data: dict) -> TranscriptionJob:
    out: TranscriptionJob = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptionJobName") is not None:
        out["transcription_job_name"] = data["TranscriptionJobName"]
    if data.get("TranscriptionJobStatus") is not None:
        import capo_transcribe.types.transcription_job_status

        out["transcription_job_status"] = (
            capo_transcribe.types.transcription_job_status.deserialize_aws_json_1_1(
                data["TranscriptionJobStatus"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.language_code

        out["language_code"] = (
            capo_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("MediaSampleRateHertz") is not None:
        out["media_sample_rate_hertz"] = data["MediaSampleRateHertz"]
    if data.get("MediaFormat") is not None:
        import capo_transcribe.types.media_format

        out["media_format"] = (
            capo_transcribe.types.media_format.deserialize_aws_json_1_1(
                data["MediaFormat"]
            )
        )
    if data.get("Media") is not None:
        import capo_transcribe.types.media

        out["media"] = capo_transcribe.types.media.deserialize_aws_json_1_1(
            data["Media"]
        )
    if data.get("Transcript") is not None:
        import capo_transcribe.types.transcript

        out["transcript"] = capo_transcribe.types.transcript.deserialize_aws_json_1_1(
            data["Transcript"]
        )
    if data.get("StartTime") is not None:
        import capo_transcribe.types.date_time

        out["start_time"] = capo_transcribe.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("CreationTime") is not None:
        import capo_transcribe.types.date_time

        out["creation_time"] = capo_transcribe.types.date_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("CompletionTime") is not None:
        import capo_transcribe.types.date_time

        out["completion_time"] = (
            capo_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("Settings") is not None:
        import capo_transcribe.types.settings

        out["settings"] = capo_transcribe.types.settings.deserialize_aws_json_1_1(
            data["Settings"]
        )
    if data.get("ModelSettings") is not None:
        import capo_transcribe.types.model_settings

        out["model_settings"] = (
            capo_transcribe.types.model_settings.deserialize_aws_json_1_1(
                data["ModelSettings"]
            )
        )
    if data.get("JobExecutionSettings") is not None:
        import capo_transcribe.types.job_execution_settings

        out["job_execution_settings"] = (
            capo_transcribe.types.job_execution_settings.deserialize_aws_json_1_1(
                data["JobExecutionSettings"]
            )
        )
    if data.get("ContentRedaction") is not None:
        import capo_transcribe.types.content_redaction

        out["content_redaction"] = (
            capo_transcribe.types.content_redaction.deserialize_aws_json_1_1(
                data["ContentRedaction"]
            )
        )
    if data.get("IdentifyLanguage") is not None:
        out["identify_language"] = data["IdentifyLanguage"]
    if data.get("IdentifyMultipleLanguages") is not None:
        out["identify_multiple_languages"] = data["IdentifyMultipleLanguages"]
    if data.get("LanguageOptions") is not None:
        import capo_transcribe.types.language_options

        out["language_options"] = (
            capo_transcribe.types.language_options.deserialize_aws_json_1_1(
                data["LanguageOptions"]
            )
        )
    if data.get("IdentifiedLanguageScore") is not None:
        out["identified_language_score"] = float(data["IdentifiedLanguageScore"])
    if data.get("LanguageCodes") is not None:
        import capo_transcribe.types.language_code_list

        out["language_codes"] = (
            capo_transcribe.types.language_code_list.deserialize_aws_json_1_1(
                data["LanguageCodes"]
            )
        )
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Subtitles") is not None:
        import capo_transcribe.types.subtitles_output

        out["subtitles"] = (
            capo_transcribe.types.subtitles_output.deserialize_aws_json_1_1(
                data["Subtitles"]
            )
        )
    if data.get("LanguageIdSettings") is not None:
        import capo_transcribe.types.language_id_settings_map

        out["language_id_settings"] = (
            capo_transcribe.types.language_id_settings_map.deserialize_aws_json_1_1(
                data["LanguageIdSettings"]
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
