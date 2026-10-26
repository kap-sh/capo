"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EncryptionSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.kms_encryption_settings


class _EncryptionSettings_kmsEncryptionSettings(TypedDict, closed=True):
    kmsEncryptionSettings: (
        "capo_verifiedpermissions.types.kms_encryption_settings.KmsEncryptionSettings"
    )


class _EncryptionSettings_default(TypedDict, closed=True):
    default: "None"


EncryptionSettings: TypeAlias = (
    _EncryptionSettings_kmsEncryptionSettings
    | _EncryptionSettings_default
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionSettings) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EncryptionSettings: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "kmsEncryptionSettings" in value:
        import capo_verifiedpermissions.types.kms_encryption_settings

        return {
            "kmsEncryptionSettings": capo_verifiedpermissions.types.kms_encryption_settings.serialize_aws_json_1_0(
                value["kmsEncryptionSettings"]
            )
        }
    elif "default" in value:
        return {"default": {}}
    else:
        raise SerializationError("EncryptionSettings: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EncryptionSettings:
    if data.get("kmsEncryptionSettings") is not None:
        import capo_verifiedpermissions.types.kms_encryption_settings

        return {
            "kmsEncryptionSettings": capo_verifiedpermissions.types.kms_encryption_settings.deserialize_aws_json_1_0(
                data["kmsEncryptionSettings"]
            )
        }
    elif data.get("default") is not None:
        return {"default": None}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EncryptionSettings: no recognized variant key")
