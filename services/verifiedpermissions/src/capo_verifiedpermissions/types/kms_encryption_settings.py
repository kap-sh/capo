"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#KmsEncryptionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.encryption_context
    import capo_verifiedpermissions.types.kms_key


class KmsEncryptionSettings(TypedDict, closed=True):
    key: "capo_verifiedpermissions.types.kms_key.KmsKey"
    """<p>The customer-managed KMS key <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a>, alias or ID to be used for encryption processes. </p> <p>Users can provide the full KMS key ARN, a KMS key alias, or a KMS key ID, but it will be mapped to the full KMS key ARN after policy store creation, and referenced when encrypting child resources. </p>"""
    encryption_context: NotRequired[
        "capo_verifiedpermissions.types.encryption_context.EncryptionContext"
    ]
    """<p>User-defined, additional context to be added to encryption processes. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsEncryptionSettings) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "encryption_context" in value:
        import capo_verifiedpermissions.types.encryption_context

        out["encryptionContext"] = (
            capo_verifiedpermissions.types.encryption_context.serialize_aws_json_1_0(
                value["encryption_context"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsEncryptionSettings:
    out: KmsEncryptionSettings = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("KmsEncryptionSettings.key required")
    if data.get("encryptionContext") is not None:
        import capo_verifiedpermissions.types.encryption_context

        out["encryption_context"] = (
            capo_verifiedpermissions.types.encryption_context.deserialize_aws_json_1_0(
                data["encryptionContext"]
            )
        )
    return out
