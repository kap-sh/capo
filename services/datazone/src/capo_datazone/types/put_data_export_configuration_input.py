"""Generated from Smithy shape ``com.amazonaws.datazone#PutDataExportConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.encryption_configuration


class PutDataExportConfigurationInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The domain ID for which you want to create data export configuration details.</p>"""
    enable_export: "bool"
    """<p>Specifies that the export is to be enabled as part of creating data export configuration details.</p>"""
    encryption_configuration: NotRequired[
        "capo_datazone.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration as part of creating data export configuration details.</p> <p>The KMS key provided here as part of encryptionConfiguration must have the required permissions as described in <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.html">KMS permissions for exporting asset metadata in Amazon SageMaker Unified Studio</a>.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDataExportConfigurationInput) -> dict:
    out: dict = {}
    out["enableExport"] = value["enable_export"]
    if "encryption_configuration" in value:
        import capo_datazone.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_datazone.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutDataExportConfigurationInput:
    out: PutDataExportConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("enableExport") is not None:
        out["enable_export"] = data["enableExport"]
    else:
        raise DeserializationError(
            "PutDataExportConfigurationInput.enable_export required"
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_datazone.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_datazone.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
