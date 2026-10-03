"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeEncryptionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.kms_encryption_context_map
    import capo_transcribe_streaming.types.kms_key_id


class MedicalScribeEncryptionSettings(TypedDict, closed=True):
    kms_encryption_context: NotRequired[
        "capo_transcribe_streaming.types.kms_encryption_context_map.KMSEncryptionContextMap"
    ]
    """<p>A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context">KMSencryption context </a> and <a href="https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html">Asymmetric keys in KMS </a>. </p>"""
    kms_key_id: "capo_transcribe_streaming.types.kms_key_id.KMSKeyId"
    """<p>The ID of the KMS key you want to use for your streaming session. You can specify its KMS key ID, key Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with <code>"alias/"</code>. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab</p> </li> <li> <p>Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</p> </li> <li> <p> Alias name: alias/ExampleAlias</p> </li> <li> <p> Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias </p> </li> </ul> <p> To get the key ID and key ARN for a KMS key, use the <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html">ListKeys</a> or <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html">DescribeKey</a> KMS API operations. To get the alias name and alias ARN, use <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html">ListKeys</a> API operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeEncryptionSettings) -> dict:
    out: dict = {}
    if "kms_encryption_context" in value:
        import capo_transcribe_streaming.types.kms_encryption_context_map

        out["KmsEncryptionContext"] = (
            capo_transcribe_streaming.types.kms_encryption_context_map.serialize_json(
                value["kms_encryption_context"]
            )
        )
    out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> MedicalScribeEncryptionSettings:
    out: MedicalScribeEncryptionSettings = {}  # type: ignore[typeddict-item]
    if data.get("KmsEncryptionContext") is not None:
        import capo_transcribe_streaming.types.kms_encryption_context_map

        out["kms_encryption_context"] = (
            capo_transcribe_streaming.types.kms_encryption_context_map.deserialize_json(
                data["KmsEncryptionContext"]
            )
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    else:
        raise DeserializationError(
            "MedicalScribeEncryptionSettings.kms_key_id required"
        )
    return out
