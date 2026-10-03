"""Generated from Smithy shape ``com.amazonaws.transcribe#StartCallAnalyticsJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.call_analytics_job_name
    import capo_transcribe.types.call_analytics_job_settings
    import capo_transcribe.types.channel_definitions
    import capo_transcribe.types.data_access_role_arn
    import capo_transcribe.types.kms_key_id
    import capo_transcribe.types.media
    import capo_transcribe.types.tag_list
    import capo_transcribe.types.uri


class StartCallAnalyticsJobRequest(TypedDict, closed=True):
    call_analytics_job_name: (
        "capo_transcribe.types.call_analytics_job_name.CallAnalyticsJobName"
    )
    """<p>A unique name, chosen by you, for your Call Analytics job.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a <code>ConflictException</code> error.</p>"""
    media: "capo_transcribe.types.media.Media"
    """<p>Describes the Amazon S3 location of the media file you want to use in your Call Analytics request.</p>"""
    output_location: NotRequired["capo_transcribe.types.uri.Uri"]
    """<p>The Amazon S3 location where you want your Call Analytics transcription output stored. You can use any of the following formats to specify the output location:</p> <ol> <li> <p>s3://DOC-EXAMPLE-BUCKET</p> </li> <li> <p>s3://DOC-EXAMPLE-BUCKET/my-output-folder/</p> </li> <li> <p>s3://DOC-EXAMPLE-BUCKET/my-output-folder/my-call-analytics-job.json</p> </li> </ol> <p>Unless you specify a file name (option 3), the name of your output file has a default value that matches the name you specified for your transcription job using the <code>CallAnalyticsJobName</code> parameter.</p> <p>You can specify a KMS key to encrypt your output using the <code>OutputEncryptionKMSKeyId</code> parameter. If you do not specify a KMS key, Amazon Transcribe uses the default Amazon S3 key for server-side encryption.</p> <p>If you do not specify <code>OutputLocation</code>, your transcript is placed in a service-managed Amazon S3 bucket and you are provided with a URI to access your transcript.</p>"""
    output_encryption_kms_key_id: NotRequired[
        "capo_transcribe.types.kms_key_id.KMSKeyId"
    ]
    """<p>The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your Call Analytics output.</p> <p>KMS key ARNs have the format <code>arn:partition:kms:region:account:key/key-id</code>. For example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN"> KMS key ARNs</a>.</p> <p>If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).</p> <p>Note that the role making the request and the role specified in the <code>DataAccessRoleArn</code> request parameter (if present) must have permission to use the specified KMS key.</p>"""
    data_access_role_arn: NotRequired[
        "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>"""
    settings: NotRequired[
        "capo_transcribe.types.call_analytics_job_settings.CallAnalyticsJobSettings"
    ]
    """<p>Specify additional optional settings in your request, including content redaction; allows you to apply custom language models, vocabulary filters, and custom vocabularies to your Call Analytics job.</p>"""
    tags: NotRequired["capo_transcribe.types.tag_list.TagList"]
    """<p>Adds one or more custom tags, each in the form of a key:value pair, to a new call analytics job at the time you start this new job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html">Tagging resources</a>.</p>"""
    channel_definitions: NotRequired[
        "capo_transcribe.types.channel_definitions.ChannelDefinitions"
    ]
    """<p>Makes it possible to specify which speaker is on which channel. For example, if your agent is the first participant to speak, you would set <code>ChannelId</code> to <code>0</code> (to indicate the first channel) and <code>ParticipantRole</code> to <code>AGENT</code> (to indicate that it's the agent speaking).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCallAnalyticsJobRequest) -> dict:
    out: dict = {}
    out["CallAnalyticsJobName"] = value["call_analytics_job_name"]
    import capo_transcribe.types.media

    out["Media"] = capo_transcribe.types.media.serialize_aws_json_1_1(value["media"])
    if "output_location" in value:
        out["OutputLocation"] = value["output_location"]
    if "output_encryption_kms_key_id" in value:
        out["OutputEncryptionKMSKeyId"] = value["output_encryption_kms_key_id"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "settings" in value:
        import capo_transcribe.types.call_analytics_job_settings

        out["Settings"] = (
            capo_transcribe.types.call_analytics_job_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "tags" in value:
        import capo_transcribe.types.tag_list

        out["Tags"] = capo_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "channel_definitions" in value:
        import capo_transcribe.types.channel_definitions

        out["ChannelDefinitions"] = (
            capo_transcribe.types.channel_definitions.serialize_aws_json_1_1(
                value["channel_definitions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCallAnalyticsJobRequest:
    out: StartCallAnalyticsJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("CallAnalyticsJobName") is not None:
        out["call_analytics_job_name"] = data["CallAnalyticsJobName"]
    else:
        raise DeserializationError(
            "StartCallAnalyticsJobRequest.call_analytics_job_name required"
        )
    if data.get("Media") is not None:
        import capo_transcribe.types.media

        out["media"] = capo_transcribe.types.media.deserialize_aws_json_1_1(
            data["Media"]
        )
    else:
        raise DeserializationError("StartCallAnalyticsJobRequest.media required")
    if data.get("OutputLocation") is not None:
        out["output_location"] = data["OutputLocation"]
    if data.get("OutputEncryptionKMSKeyId") is not None:
        out["output_encryption_kms_key_id"] = data["OutputEncryptionKMSKeyId"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if data.get("Settings") is not None:
        import capo_transcribe.types.call_analytics_job_settings

        out["settings"] = (
            capo_transcribe.types.call_analytics_job_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if data.get("Tags") is not None:
        import capo_transcribe.types.tag_list

        out["tags"] = capo_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ChannelDefinitions") is not None:
        import capo_transcribe.types.channel_definitions

        out["channel_definitions"] = (
            capo_transcribe.types.channel_definitions.deserialize_aws_json_1_1(
                data["ChannelDefinitions"]
            )
        )
    return out
