"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.boolean
    import capo_transcribe.types.data_access_role_arn
    import capo_transcribe.types.date_time
    import capo_transcribe.types.failure_reason
    import capo_transcribe.types.media
    import capo_transcribe.types.medical_scribe_channel_definitions
    import capo_transcribe.types.medical_scribe_job_status
    import capo_transcribe.types.medical_scribe_language_code
    import capo_transcribe.types.medical_scribe_output
    import capo_transcribe.types.medical_scribe_settings
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.transcription_job_name


class MedicalScribeJob(TypedDict, closed=True):
    medical_scribe_job_name: NotRequired[
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the Medical Scribe job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    medical_scribe_job_status: NotRequired[
        "capo_transcribe.types.medical_scribe_job_status.MedicalScribeJobStatus"
    ]
    """<p>Provides the status of the specified Medical Scribe job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>MedicalScribeOutput</code> If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your Medical Scribe job failed.</p>"""
    language_code: NotRequired[
        "capo_transcribe.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The language code used to create your Medical Scribe job. US English (<code>en-US</code>) is the only supported language for Medical Scribe jobs. </p>"""
    media: NotRequired["capo_transcribe.types.media.Media"]
    medical_scribe_output: NotRequired[
        "capo_transcribe.types.medical_scribe_output.MedicalScribeOutput"
    ]
    """<p>The location of the output of your Medical Scribe job. <code>ClinicalDocumentUri</code> holds the Amazon S3 URI for the Clinical Document and <code>TranscriptFileUri</code> holds the Amazon S3 URI for the Transcript.</p>"""
    start_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time your Medical Scribe job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    creation_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Medical Scribe job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["capo_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Medical Scribe job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a Medical Scribe job that finished processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    failure_reason: NotRequired["capo_transcribe.types.failure_reason.FailureReason"]
    """<p>If <code>MedicalScribeJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job failed. See also: <a href="https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html">Common Errors</a>.</p>"""
    settings: NotRequired[
        "capo_transcribe.types.medical_scribe_settings.MedicalScribeSettings"
    ]
    """<p>Makes it possible to control how your Medical Scribe job is processed using a <code>MedicalScribeSettings</code> object. Specify <code>ChannelIdentification</code> if <code>ChannelDefinitions</code> are set. Enabled <code>ShowSpeakerLabels</code> if <code>ChannelIdentification</code> and <code>ChannelDefinitions</code> are not set. One and only one of <code>ChannelIdentification</code> and <code>ShowSpeakerLabels</code> must be set. If <code>ShowSpeakerLabels</code> is set, <code>MaxSpeakerLabels</code> must also be set. Use <code>Settings</code> to specify a vocabulary or vocabulary filter or both using <code>VocabularyName</code>, <code>VocabularyFilterName</code>. <code>VocabularyFilterMethod</code> must be specified if <code>VocabularyFilterName</code> is set. </p>"""
    data_access_role_arn: NotRequired[
        "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files, write to the output bucket, and use your KMS key if supplied. If the role that you specify doesn’t have the appropriate permissions your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>"""
    channel_definitions: NotRequired[
        "capo_transcribe.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>Makes it possible to specify which speaker is on which channel. For example, if the clinician is the first participant to speak, you would set <code>ChannelId</code> of the first <code>ChannelDefinition</code> in the list to <code>0</code> (to indicate the first channel) and <code>ParticipantRole</code> to <code>CLINICIAN</code> (to indicate that it's the clinician speaking). Then you would set the <code>ChannelId</code> of the second <code>ChannelDefinition</code> in the list to <code>1</code> (to indicate the second channel) and <code>ParticipantRole</code> to <code>PATIENT</code> (to indicate that it's the patient speaking). </p>"""
    medical_scribe_context_provided: NotRequired[
        "capo_transcribe.types.boolean.Boolean"
    ]
    """<p>Indicates whether the <code>MedicalScribeContext</code> object was provided when the Medical Scribe job was started.</p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>Adds one or more custom tags, each in the form of a key:value pair, to the Medical Scribe job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeJob) -> dict:
    out: dict = {}
    if "medical_scribe_job_name" in value:
        out["MedicalScribeJobName"] = value["medical_scribe_job_name"]
    if "medical_scribe_job_status" in value:
        import capo_transcribe.types.medical_scribe_job_status

        out["MedicalScribeJobStatus"] = (
            capo_transcribe.types.medical_scribe_job_status.serialize_aws_json_1_1(
                value["medical_scribe_job_status"]
            )
        )
    if "language_code" in value:
        import capo_transcribe.types.medical_scribe_language_code

        out["LanguageCode"] = (
            capo_transcribe.types.medical_scribe_language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "media" in value:
        import capo_transcribe.types.media

        out["Media"] = capo_transcribe.types.media.serialize_aws_json_1_1(
            value["media"]
        )
    if "medical_scribe_output" in value:
        import capo_transcribe.types.medical_scribe_output

        out["MedicalScribeOutput"] = (
            capo_transcribe.types.medical_scribe_output.serialize_aws_json_1_1(
                value["medical_scribe_output"]
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
        import capo_transcribe.types.medical_scribe_settings

        out["Settings"] = (
            capo_transcribe.types.medical_scribe_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "channel_definitions" in value:
        import capo_transcribe.types.medical_scribe_channel_definitions

        out["ChannelDefinitions"] = (
            capo_transcribe.types.medical_scribe_channel_definitions.serialize_aws_json_1_1(
                value["channel_definitions"]
            )
        )
    if "medical_scribe_context_provided" in value:
        out["MedicalScribeContextProvided"] = value["medical_scribe_context_provided"]
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribeJob:
    out: MedicalScribeJob = {}  # type: ignore[typeddict-item]
    if data.get("MedicalScribeJobName") is not None:
        out["medical_scribe_job_name"] = data["MedicalScribeJobName"]
    if data.get("MedicalScribeJobStatus") is not None:
        import capo_transcribe.types.medical_scribe_job_status

        out["medical_scribe_job_status"] = (
            capo_transcribe.types.medical_scribe_job_status.deserialize_aws_json_1_1(
                data["MedicalScribeJobStatus"]
            )
        )
    if data.get("LanguageCode") is not None:
        import capo_transcribe.types.medical_scribe_language_code

        out["language_code"] = (
            capo_transcribe.types.medical_scribe_language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if data.get("Media") is not None:
        import capo_transcribe.types.media

        out["media"] = capo_transcribe.types.media.deserialize_aws_json_1_1(
            data["Media"]
        )
    if data.get("MedicalScribeOutput") is not None:
        import capo_transcribe.types.medical_scribe_output

        out["medical_scribe_output"] = (
            capo_transcribe.types.medical_scribe_output.deserialize_aws_json_1_1(
                data["MedicalScribeOutput"]
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
        import capo_transcribe.types.medical_scribe_settings

        out["settings"] = (
            capo_transcribe.types.medical_scribe_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("ChannelDefinitions") is not None:
        import capo_transcribe.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            capo_transcribe.types.medical_scribe_channel_definitions.deserialize_aws_json_1_1(
                data["ChannelDefinitions"]
            )
        )
    if data.get("MedicalScribeContextProvided") is not None:
        out["medical_scribe_context_provided"] = data["MedicalScribeContextProvided"]
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
