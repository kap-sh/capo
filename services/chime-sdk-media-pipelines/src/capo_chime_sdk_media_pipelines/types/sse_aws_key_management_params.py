"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SseAwsKeyManagementParams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.string


class SseAwsKeyManagementParams(TypedDict, closed=True):
    aws_kms_key_id: "capo_chime_sdk_media_pipelines.types.string.String"
    """<p>The KMS key you want to use to encrypt your media pipeline output. Decryption is required for concatenation pipeline. If using a key located in the current Amazon Web Services account, you can specify your KMS key in one of four ways:</p> <ul> <li> <p>Use the KMS key ID itself. For example, <code>1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Use an alias for the KMS key ID. For example, <code>alias/ExampleAlias</code>.</p> </li> <li> <p>Use the Amazon Resource Name (ARN) for the KMS key ID. For example, <code>arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Use the ARN for the KMS key alias. For example, <code>arn:aws:kms:region:account-ID:alias/ExampleAlias</code>.</p> </li> </ul> <p>If using a key located in a different Amazon Web Services account than the current Amazon Web Services account, you can specify your KMS key in one of two ways:</p> <ul> <li> <p>Use the ARN for the KMS key ID. For example, <code>arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Use the ARN for the KMS key alias. For example, <code>arn:aws:kms:region:account-ID:alias/ExampleAlias</code>.</p> </li> </ul> <p>If you don't specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).</p> <p>Note that the role specified in the <code>SinkIamRoleArn</code> request parameter must have permission to use the specified KMS key.</p>"""
    aws_kms_encryption_context: NotRequired[
        "capo_chime_sdk_media_pipelines.types.string.String"
    ]
    """<p>Base64-encoded string of a UTF-8 encoded JSON, which contains the encryption context as non-secret key-value pair known as encryption context pairs, that provides an added layer of security for your data. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html">KMS encryption context</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Asymmetric keys in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SseAwsKeyManagementParams) -> dict:
    out: dict = {}
    out["AwsKmsKeyId"] = value["aws_kms_key_id"]
    if "aws_kms_encryption_context" in value:
        out["AwsKmsEncryptionContext"] = value["aws_kms_encryption_context"]
    return out


def deserialize_json(data: dict) -> SseAwsKeyManagementParams:
    out: SseAwsKeyManagementParams = {}  # type: ignore[typeddict-item]
    if data.get("AwsKmsKeyId") is not None:
        out["aws_kms_key_id"] = data["AwsKmsKeyId"]
    else:
        raise DeserializationError("SseAwsKeyManagementParams.aws_kms_key_id required")
    if data.get("AwsKmsEncryptionContext") is not None:
        out["aws_kms_encryption_context"] = data["AwsKmsEncryptionContext"]
    return out
