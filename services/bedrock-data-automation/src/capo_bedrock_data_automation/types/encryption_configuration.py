"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.kms_encryption_context
    import capo_bedrock_data_automation.types.kms_key_id


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: "capo_bedrock_data_automation.types.kms_key_id.KmsKeyId"
    kms_encryption_context: NotRequired[
        "capo_bedrock_data_automation.types.kms_encryption_context.KmsEncryptionContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    out["kmsKeyId"] = value["kms_key_id"]
    if "kms_encryption_context" in value:
        import capo_bedrock_data_automation.types.kms_encryption_context

        out["kmsEncryptionContext"] = (
            capo_bedrock_data_automation.types.kms_encryption_context.serialize_json(
                value["kms_encryption_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        out["kms_key_id"] = ""
    if data.get("kmsEncryptionContext") is not None:
        import capo_bedrock_data_automation.types.kms_encryption_context

        out["kms_encryption_context"] = (
            capo_bedrock_data_automation.types.kms_encryption_context.deserialize_json(
                data["kmsEncryptionContext"]
            )
        )
    return out
