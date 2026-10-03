"""Generated from Smithy shape ``com.amazonaws.keyspaces#EncryptionSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.encryption_type
    import capo_keyspaces.types.kms_key_arn


class EncryptionSpecification(TypedDict, closed=True):
    type: "capo_keyspaces.types.encryption_type.EncryptionType"
    """<p>The encryption option specified for the table. You can choose one of the following KMS keys (KMS keys):</p> <ul> <li> <p> <code>type:AWS_OWNED_KMS_KEY</code> - This key is owned by Amazon Keyspaces. </p> </li> <li> <p> <code>type:CUSTOMER_MANAGED_KMS_KEY</code> - This key is stored in your account and is created, owned, and managed by you. This option requires the <code>kms_key_identifier</code> of the KMS key in Amazon Resource Name (ARN) format as input. </p> </li> </ul> <p>The default is <code>type:AWS_OWNED_KMS_KEY</code>. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html">Encryption at rest</a> in the <i>Amazon Keyspaces Developer Guide</i>.</p>"""
    kms_key_identifier: NotRequired["capo_keyspaces.types.kms_key_arn.kmsKeyARN"]
    """<p>The Amazon Resource Name (ARN) of the customer managed KMS key, for example <code>kms_key_identifier:ARN</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionSpecification) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionSpecification:
    out: EncryptionSpecification = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("EncryptionSpecification.type required")
    if data.get("kmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    return out
