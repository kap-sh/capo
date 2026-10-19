"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#PutDefaultEncryptionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.configuration_status
    import capo_iot_managed_integrations.types.encryption_type
    import capo_iot_managed_integrations.types.kms_key_arn


class PutDefaultEncryptionConfigurationResponse(TypedDict, closed=True):
    configuration_status: (
        "capo_iot_managed_integrations.types.configuration_status.ConfigurationStatus"
    )
    """<p>Provides the status of the default encryption configuration for an Amazon Web Services account.</p>"""
    encryption_type: (
        "capo_iot_managed_integrations.types.encryption_type.EncryptionType"
    )
    """<p>The type of encryption used for the encryption configuration.</p>"""
    kms_key_arn: NotRequired[
        "capo_iot_managed_integrations.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Key Amazon Resource Name (ARN) of the AWS KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDefaultEncryptionConfigurationResponse) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.configuration_status

    out["configurationStatus"] = (
        capo_iot_managed_integrations.types.configuration_status.serialize_json(
            value["configuration_status"]
        )
    )
    import capo_iot_managed_integrations.types.encryption_type

    out["encryptionType"] = (
        capo_iot_managed_integrations.types.encryption_type.serialize_json(
            value["encryption_type"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> PutDefaultEncryptionConfigurationResponse:
    out: PutDefaultEncryptionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("configurationStatus") is not None:
        import capo_iot_managed_integrations.types.configuration_status

        out["configuration_status"] = (
            capo_iot_managed_integrations.types.configuration_status.deserialize_json(
                data["configurationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "PutDefaultEncryptionConfigurationResponse.configuration_status required"
        )
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
