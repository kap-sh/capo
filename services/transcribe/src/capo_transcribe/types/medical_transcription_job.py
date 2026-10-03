"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalTranscriptionJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.date_time
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.language_code
    import capo_transcribe.types.media
    import capo_transcribe.types.media_format
    import capo_transcribe.types.medical_content_identification_type
    import capo_transcribe.types.medical_media_sample_rate_hertz
    import capo_transcribe.types.medical_transcript
    import capo_transcribe.types.medical_transcription_setting
    import capo_transcribe.types.specialty
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.transcription_job_name
    import capo_transcribe.types.transcription_job_status
    import capo_transcribe.types.type


class MedicalTranscriptionJob(TypedDict, closed=True):
    medical_transcription_job_name: NotRequired[
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the medical transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    transcription_job_status: NotRequired[
        "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Provides the status of the specified medical transcription job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>"""
    language_code: NotRequired["capo_transcribe.types.language_code.LanguageCode"]
    """<p>The language code used to create your medical transcription job. US English (<code>en-US</code>) is the only supported language for medical transcriptions.</p>"""
    media_sample_rate_hertz: NotRequired[
        "capo_transcribe.types.medical_media_sample_rate_hertz.MedicalMediaSampleRateHertz"
    ]
    """<p>The sample rate, in hertz, of the audio track in your input media file.</p>"""
    media_format: NotRequired["capo_transcribe.types.media_format.MediaFormat"]
    """<p>The format of the input media file.</p>"""
    media: NotRequired["capo_transcribe.types.media.Media"]
    transcript: NotRequired[
        "capo_transcribe.types.medical_transcript.MedicalTranscript"
    ]
    """<p>Provides you with the Amazon S3 URI you can use to access your transcript.</p>"""
    start_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified medical transcription job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    creation_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified medical transcription job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified medical transcription job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:33:13.922000-07:00</code> represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>TranscriptionJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job request failed.</p> <p>The <code>FailureReason</code> field contains one of the following values:</p> <ul> <li> <p> <code>Unsupported media format</code>.</p> <p>The media format specified in <code>MediaFormat</code> isn't valid. Refer to refer to the <code>MediaFormat</code> parameter for a list of supported formats.</p> </li> <li> <p> <code>The media format provided does not match the detected media format</code>.</p> <p>The media format specified in <code>MediaFormat</code> doesn't match the format of the input file. Check the media format of your media file and correct the specified value.</p> </li> <li> <p> <code>Invalid sample rate for audio file</code>.</p> <p>The sample rate specified in <code>MediaSampleRateHertz</code> isn't valid. The sample rate must be between 16,000 and 48,000 hertz.</p> </li> <li> <p> <code>The sample rate provided does not match the detected sample rate</code>.</p> <p>The sample rate specified in <code>MediaSampleRateHertz</code> doesn't match the sample rate detected in your input media file. Check the sample rate of your media file and correct the specified value.</p> </li> <li> <p> <code>Invalid file size: file size too large</code>.</p> <p>The size of your media file is larger than what Amazon Transcribe can process. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe">Service quotas</a>.</p> </li> <li> <p> <code>Invalid number of channels: number of channels too large</code>.</p> <p>Your audio contains more channels than Amazon Transcribe is able to process. For more information, refer to <a href="https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe">Service quotas</a>.</p> </li> </ul>"""
    settings: NotRequired[
        "capo_transcribe.types.medical_transcription_setting.MedicalTranscriptionSetting"
    ]
    """<p>Provides information on any additional settings that were included in your request. Additional settings include channel identification, alternative transcriptions, speaker partitioning, custom vocabularies, and custom vocabulary filters.</p>"""
    content_identification_type: NotRequired[
        "capo_transcribe.types.medical_content_identification_type.MedicalContentIdentificationType"
    ]
    """<p>Indicates whether content identification was enabled for your transcription request.</p>"""
    specialty: NotRequired["capo_transcribe.types.specialty.Specialty"]
    """<p>Describes the medical specialty represented in your media.</p>"""
    type: NotRequired["capo_transcribe.types.type.Type"]
    """<p>Indicates whether the input media is a dictation or a conversation, as specified in the <code>StartMedicalTranscriptionJob</code> request.</p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>The tags, each in the form of a key:value pair, assigned to the specified medical transcription job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalTranscriptionJob) -> dict:
    out: dict = {}
    if "medical_transcription_job_name" in value:
        out["MedicalTranscriptionJobName"] = value["medical_transcription_job_name"]
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
        import capo_transcribe.types.medical_transcript

        out["Transcript"] = (
            capo_transcribe.types.medical_transcript.serialize_aws_json_1_1(
                value["transcript"]
            )
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
        import capo_transcribe.types.medical_transcription_setting

        out["Settings"] = (
            capo_transcribe.types.medical_transcription_setting.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "content_identification_type" in value:
        import capo_transcribe.types.medical_content_identification_type

        out["ContentIdentificationType"] = (
            capo_transcribe.types.medical_content_identification_type.serialize_aws_json_1_1(
                value["content_identification_type"]
            )
        )
    if "specialty" in value:
        import capo_transcribe.types.specialty

        out["Specialty"] = capo_transcribe.types.specialty.serialize_aws_json_1_1(
            value["specialty"]
        )
    if "type" in value:
        import capo_transcribe.types.type

        out["Type"] = capo_transcribe.types.type.serialize_aws_json_1_1(value["type"])
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalTranscriptionJob:
    out: MedicalTranscriptionJob = {}  # type: ignore[typeddict-item]
    if data.get("MedicalTranscriptionJobName") is not None:
        out["medical_transcription_job_name"] = data["MedicalTranscriptionJobName"]
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
        import capo_transcribe.types.medical_transcript

        out["transcript"] = (
            capo_transcribe.types.medical_transcript.deserialize_aws_json_1_1(
                data["Transcript"]
            )
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
        import capo_transcribe.types.medical_transcription_setting

        out["settings"] = (
            capo_transcribe.types.medical_transcription_setting.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if data.get("ContentIdentificationType") is not None:
        import capo_transcribe.types.medical_content_identification_type

        out["content_identification_type"] = (
            capo_transcribe.types.medical_content_identification_type.deserialize_aws_json_1_1(
                data["ContentIdentificationType"]
            )
        )
    if data.get("Specialty") is not None:
        import capo_transcribe.types.specialty

        out["specialty"] = capo_transcribe.types.specialty.deserialize_aws_json_1_1(
            data["Specialty"]
        )
    if data.get("Type") is not None:
        import capo_transcribe.types.type

        out["type"] = capo_transcribe.types.type.deserialize_aws_json_1_1(data["Type"])
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
