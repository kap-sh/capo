"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#KmsEncryptionState``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.encryption_context
    import capo_verifiedpermissions.types.kms_key


class KmsEncryptionState(TypedDict, closed=True):
    key: "capo_verifiedpermissions.types.kms_key.KmsKey"
    """<p>The customer-managed KMS key <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> being used for encryption processes. </p>"""
    encryption_context: (
        "capo_verifiedpermissions.types.encryption_context.EncryptionContext"
    )
    """<p>User-defined, additional context added to encryption processes. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsEncryptionState) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_verifiedpermissions.types.encryption_context

    out["encryptionContext"] = (
        capo_verifiedpermissions.types.encryption_context.serialize_aws_json_1_0(
            value["encryption_context"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> KmsEncryptionState:
    out: KmsEncryptionState = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("KmsEncryptionState.key required")
    if data.get("encryptionContext") is not None:
        import capo_verifiedpermissions.types.encryption_context

        out["encryption_context"] = (
            capo_verifiedpermissions.types.encryption_context.deserialize_aws_json_1_0(
                data["encryptionContext"]
            )
        )
    else:
        raise DeserializationError("KmsEncryptionState.encryption_context required")
    return out
