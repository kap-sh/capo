"""Generated from Smithy shape ``com.amazonaws.odb#EncryptionKeyConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError, SerializationError
from capo_odb.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_odb.types.aws_encryption_key_configuration_input


class EncryptionKeyConfigurationInputAwsEncryptionKeyMember(TypedDict, closed=True):
    awsEncryptionKey: "capo_odb.types.aws_encryption_key_configuration_input.AwsEncryptionKeyConfigurationInput"


EncryptionKeyConfigurationInput: TypeAlias = (
    EncryptionKeyConfigurationInputAwsEncryptionKeyMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionKeyConfigurationInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EncryptionKeyConfigurationInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "awsEncryptionKey" in value:
        import capo_odb.types.aws_encryption_key_configuration_input

        return {
            "awsEncryptionKey": capo_odb.types.aws_encryption_key_configuration_input.serialize_aws_json_1_0(
                value["awsEncryptionKey"]
            )
        }
    else:
        raise SerializationError("EncryptionKeyConfigurationInput: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EncryptionKeyConfigurationInput:
    if data.get("awsEncryptionKey") is not None:
        import capo_odb.types.aws_encryption_key_configuration_input

        return {
            "awsEncryptionKey": capo_odb.types.aws_encryption_key_configuration_input.deserialize_aws_json_1_0(
                data["awsEncryptionKey"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "EncryptionKeyConfigurationInput: no recognized variant key"
        )
