"""Generated from Smithy shape ``com.amazonaws.transcribe#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe.types.kms_encryption_context_map
    import capo_transcribe.types.kms_key_id


class EncryptionConfiguration(TypedDict, closed=True):
    kms_encryption_context: NotRequired[
        "capo_transcribe.types.kms_encryption_context_map.KMSEncryptionContextMap"
    ]
    """<p>A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see <a href="https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context">KMS encryption context</a>.</p>"""
    kms_key: "capo_transcribe.types.kms_key_id.KMSKeyId"
    """<p>The Amazon Resource Name (ARN) of the KMS key you want to use to encrypt your resource artifacts. Only full KMS key ARN format is supported.</p> <p>KMS key ARNs have the format <code>arn:partition:kms:region:account:key/key-id</code>. For example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">KMS key ARNs</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_encryption_context" in value:
        import capo_transcribe.types.kms_encryption_context_map

        out["KMSEncryptionContext"] = (
            capo_transcribe.types.kms_encryption_context_map.serialize_aws_json_1_1(
                value["kms_encryption_context"]
            )
        )
    out["KMSKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KMSEncryptionContext") is not None:
        import capo_transcribe.types.kms_encryption_context_map

        out["kms_encryption_context"] = (
            capo_transcribe.types.kms_encryption_context_map.deserialize_aws_json_1_1(
                data["KMSEncryptionContext"]
            )
        )
    if data.get("KMSKey") is not None:
        out["kms_key"] = data["KMSKey"]
    else:
        raise DeserializationError("EncryptionConfiguration.kms_key required")
    return out
