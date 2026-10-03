"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#PostCallAnalyticsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.content_redaction_output
    import capo_chime_sdk_media_pipelines.types.string


class PostCallAnalyticsSettings(TypedDict, closed=True):
    output_location: "capo_chime_sdk_media_pipelines.types.string.String"
    """<p>The URL of the Amazon S3 bucket that contains the post-call data.</p>"""
    data_access_role_arn: "capo_chime_sdk_media_pipelines.types.string.String"
    """<p>The ARN of the role used by Amazon Web Services Transcribe to upload your post call analysis. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html">Post-call analytics with real-time transcriptions</a> in the <i>Amazon Transcribe Developer Guide</i>.</p>"""
    content_redaction_output: NotRequired[
        "capo_chime_sdk_media_pipelines.types.content_redaction_output.ContentRedactionOutput"
    ]
    """<p>The content redaction output settings for a post-call analysis task.</p>"""
    output_encryption_kms_key_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.string.String"
    ]
    """<p>The ID of the KMS (Key Management Service) key used to encrypt the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostCallAnalyticsSettings) -> dict:
    out: dict = {}
    out["OutputLocation"] = value["output_location"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "content_redaction_output" in value:
        import capo_chime_sdk_media_pipelines.types.content_redaction_output

        out["ContentRedactionOutput"] = (
            capo_chime_sdk_media_pipelines.types.content_redaction_output.serialize_json(
                value["content_redaction_output"]
            )
        )
    if "output_encryption_kms_key_id" in value:
        out["OutputEncryptionKMSKeyId"] = value["output_encryption_kms_key_id"]
    return out


def deserialize_json(data: dict) -> PostCallAnalyticsSettings:
    out: PostCallAnalyticsSettings = {}  # type: ignore[typeddict-item]
    if data.get("OutputLocation") is not None:
        out["output_location"] = data["OutputLocation"]
    else:
        raise DeserializationError("PostCallAnalyticsSettings.output_location required")
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "PostCallAnalyticsSettings.data_access_role_arn required"
        )
    if data.get("ContentRedactionOutput") is not None:
        import capo_chime_sdk_media_pipelines.types.content_redaction_output

        out["content_redaction_output"] = (
            capo_chime_sdk_media_pipelines.types.content_redaction_output.deserialize_json(
                data["ContentRedactionOutput"]
            )
        )
    if data.get("OutputEncryptionKMSKeyId") is not None:
        out["output_encryption_kms_key_id"] = data["OutputEncryptionKMSKeyId"]
    return out
