"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#PutDefaultEncryptionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.encryption_type
    import capo_iot_managed_integrations.types.kms_key_arn


class PutDefaultEncryptionConfigurationRequest(TypedDict, closed=True):
    encryption_type: (
        "capo_iot_managed_integrations.types.encryption_type.EncryptionType"
    )
    """<p>The type of encryption used for the encryption configuration.</p>"""
    kms_key_arn: NotRequired[
        "capo_iot_managed_integrations.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Key Amazon Resource Name (ARN) of the AWS KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDefaultEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.encryption_type

    out["encryptionType"] = (
        capo_iot_managed_integrations.types.encryption_type.serialize_json(
            value["encryption_type"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> PutDefaultEncryptionConfigurationRequest:
    out: PutDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        import capo_iot_managed_integrations.types.encryption_type

        out["encryption_type"] = (
            capo_iot_managed_integrations.types.encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    else:
        import typing

        out["encryption_type"] = typing.cast(
            "capo_iot_managed_integrations.types.encryption_type.EncryptionType", ""
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
