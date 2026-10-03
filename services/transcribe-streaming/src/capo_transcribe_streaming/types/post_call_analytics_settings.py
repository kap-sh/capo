"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#PostCallAnalyticsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.content_redaction_output
    import capo_transcribe_streaming.types.string


class PostCallAnalyticsSettings(TypedDict, closed=True):
    output_location: "capo_transcribe_streaming.types.string.String"
    """<p>The Amazon S3 location where you want your Call Analytics post-call transcription output stored. You can use any of the following formats to specify the output location:</p> <ol> <li> <p>s3://DOC-EXAMPLE-BUCKET</p> </li> <li> <p>s3://DOC-EXAMPLE-BUCKET/my-output-folder/</p> </li> <li> <p>s3://DOC-EXAMPLE-BUCKET/my-output-folder/my-call-analytics-job.json</p> </li> </ol>"""
    data_access_role_arn: "capo_transcribe_streaming.types.string.String"
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p>"""
    content_redaction_output: NotRequired[
        "capo_transcribe_streaming.types.content_redaction_output.ContentRedactionOutput"
    ]
    """<p>Specify whether you want only a redacted transcript or both a redacted and an unredacted transcript. If you choose redacted and unredacted, two JSON files are generated and stored in the Amazon S3 output location you specify.</p> <p>Note that to include <code>ContentRedactionOutput</code> in your request, you must enable content redaction (<code>ContentRedactionType</code>).</p>"""
    output_encryption_kms_key_id: NotRequired[
        "capo_transcribe_streaming.types.string.String"
    ]
    """<p>The KMS key you want to use to encrypt your Call Analytics post-call output.</p> <p>If using a key located in the <b>current</b> Amazon Web Services account, you can specify your KMS key in one of four ways:</p> <ol> <li> <p>Use the KMS key ID itself. For example, <code>1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Use an alias for the KMS key ID. For example, <code>alias/ExampleAlias</code>.</p> </li> <li> <p>Use the Amazon Resource Name (ARN) for the KMS key ID. For example, <code>arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Use the ARN for the KMS key alias. For example, <code>arn:aws:kms:region:account-ID:alias/ExampleAlias</code>.</p> </li> </ol> <p>If using a key located in a <b>different</b> Amazon Web Services account than the current Amazon Web Services account, you can specify your KMS key in one of two ways:</p> <ol> <li> <p>Use the ARN for the KMS key ID. For example, <code>arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Use the ARN for the KMS key alias. For example, <code>arn:aws:kms:region:account-ID:alias/ExampleAlias</code>.</p> </li> </ol> <p>Note that the role making the request must have permission to use the specified KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostCallAnalyticsSettings) -> dict:
    out: dict = {}
    out["OutputLocation"] = value["output_location"]
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "content_redaction_output" in value:
        import capo_transcribe_streaming.types.content_redaction_output

        out["ContentRedactionOutput"] = (
            capo_transcribe_streaming.types.content_redaction_output.serialize_json(
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
        import capo_transcribe_streaming.types.content_redaction_output

        out["content_redaction_output"] = (
            capo_transcribe_streaming.types.content_redaction_output.deserialize_json(
                data["ContentRedactionOutput"]
            )
        )
    if data.get("OutputEncryptionKMSKeyId") is not None:
        out["output_encryption_kms_key_id"] = data["OutputEncryptionKMSKeyId"]
    return out
