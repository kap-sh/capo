"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EncryptionState``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.kms_encryption_state


class EncryptionStateKmsEncryptionStateMember(TypedDict, closed=True):
    kmsEncryptionState: (
        "capo_verifiedpermissions.types.kms_encryption_state.KmsEncryptionState"
    )


class EncryptionStateDefaultMember(TypedDict, closed=True):
    default: "None"


EncryptionState: TypeAlias = (
    EncryptionStateKmsEncryptionStateMember
    | EncryptionStateDefaultMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionState) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EncryptionState: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "kmsEncryptionState" in value:
        import capo_verifiedpermissions.types.kms_encryption_state

        return {
            "kmsEncryptionState": capo_verifiedpermissions.types.kms_encryption_state.serialize_aws_json_1_0(
                value["kmsEncryptionState"]
            )
        }
    elif "default" in value:
        return {"default": {}}
    else:
        raise SerializationError("EncryptionState: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EncryptionState:
    if data.get("kmsEncryptionState") is not None:
        import capo_verifiedpermissions.types.kms_encryption_state

        return {
            "kmsEncryptionState": capo_verifiedpermissions.types.kms_encryption_state.deserialize_aws_json_1_0(
                data["kmsEncryptionState"]
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
        raise DeserializationError("EncryptionState: no recognized variant key")
