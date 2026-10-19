"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.encryption_context_map
    import capo_bedrock_data_automation_runtime.types.kms_key_id


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: "capo_bedrock_data_automation_runtime.types.kms_key_id.KMSKeyId"
    """Customer KMS key used for encryption"""
    kms_encryption_context: NotRequired[
        "capo_bedrock_data_automation_runtime.types.encryption_context_map.EncryptionContextMap"
    ]
    """KMS encryption context."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    out["kmsKeyId"] = value["kms_key_id"]
    if "kms_encryption_context" in value:
        import capo_bedrock_data_automation_runtime.types.encryption_context_map

        out["kmsEncryptionContext"] = (
            capo_bedrock_data_automation_runtime.types.encryption_context_map.serialize_aws_json_1_1(
                value["kms_encryption_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        out["kms_key_id"] = ""
    if data.get("kmsEncryptionContext") is not None:
        import capo_bedrock_data_automation_runtime.types.encryption_context_map

        out["kms_encryption_context"] = (
            capo_bedrock_data_automation_runtime.types.encryption_context_map.deserialize_aws_json_1_1(
                data["kmsEncryptionContext"]
            )
        )
    return out
