"""Generated from Smithy shape ``com.amazonaws.glue#PutDataCatalogExportConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.export_encryption_configuration
    import capo_glue.types.export_setting
    import capo_glue.types.hash_string


class PutDataCatalogExportConfigurationInput(TypedDict, closed=True):
    export_setting: "capo_glue.types.export_setting.ExportSetting"
    """<p>The export setting for the data catalog. Specify <code>ENABLED</code> to start exporting catalog metadata to S3 Tables, or <code>DISABLED</code> to stop exporting. This field is required.</p>"""
    encryption_configuration: NotRequired[
        "capo_glue.types.export_encryption_configuration.ExportEncryptionConfiguration"
    ]
    """<p>The encryption configuration for the exported data. If not specified, the default encryption settings are used.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDataCatalogExportConfigurationInput) -> dict:
    out: dict = {}
    import capo_glue.types.export_setting

    out["ExportSetting"] = capo_glue.types.export_setting.serialize_aws_json_1_1(
        value["export_setting"]
    )
    if "encryption_configuration" in value:
        import capo_glue.types.export_encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_glue.types.export_encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDataCatalogExportConfigurationInput:
    out: PutDataCatalogExportConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("ExportSetting") is not None:
        import capo_glue.types.export_setting

        out["export_setting"] = capo_glue.types.export_setting.deserialize_aws_json_1_1(
            data["ExportSetting"]
        )
    else:
        import typing

        out["export_setting"] = typing.cast(
            "capo_glue.types.export_setting.ExportSetting", ""
        )
    if data.get("EncryptionConfiguration") is not None:
        import capo_glue.types.export_encryption_configuration

        out["encryption_configuration"] = (
            capo_glue.types.export_encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
