"""Generated from Smithy shape ``com.amazonaws.emrserverless#ConfigurationOverrides``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.configuration_list
    import capo_emr_serverless.types.disk_encryption_configuration
    import capo_emr_serverless.types.monitoring_configuration


class ConfigurationOverrides(TypedDict, closed=True):
    application_configuration: NotRequired[
        "capo_emr_serverless.types.configuration_list.ConfigurationList"
    ]
    """<p>The override configurations for the application.</p>"""
    monitoring_configuration: NotRequired[
        "capo_emr_serverless.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>The override configurations for monitoring.</p>"""
    disk_encryption_configuration: NotRequired[
        "capo_emr_serverless.types.disk_encryption_configuration.DiskEncryptionConfiguration"
    ]
    """<p>The override configuration to encrypt local disks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationOverrides) -> dict:
    out: dict = {}
    if "application_configuration" in value:
        import capo_emr_serverless.types.configuration_list

        out["applicationConfiguration"] = (
            capo_emr_serverless.types.configuration_list.serialize_json(
                value["application_configuration"]
            )
        )
    if "monitoring_configuration" in value:
        import capo_emr_serverless.types.monitoring_configuration

        out["monitoringConfiguration"] = (
            capo_emr_serverless.types.monitoring_configuration.serialize_json(
                value["monitoring_configuration"]
            )
        )
    if "disk_encryption_configuration" in value:
        import capo_emr_serverless.types.disk_encryption_configuration

        out["diskEncryptionConfiguration"] = (
            capo_emr_serverless.types.disk_encryption_configuration.serialize_json(
                value["disk_encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationOverrides:
    out: ConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if data.get("applicationConfiguration") is not None:
        import capo_emr_serverless.types.configuration_list

        out["application_configuration"] = (
            capo_emr_serverless.types.configuration_list.deserialize_json(
                data["applicationConfiguration"]
            )
        )
    if data.get("monitoringConfiguration") is not None:
        import capo_emr_serverless.types.monitoring_configuration

        out["monitoring_configuration"] = (
            capo_emr_serverless.types.monitoring_configuration.deserialize_json(
                data["monitoringConfiguration"]
            )
        )
    if data.get("diskEncryptionConfiguration") is not None:
        import capo_emr_serverless.types.disk_encryption_configuration

        out["disk_encryption_configuration"] = (
            capo_emr_serverless.types.disk_encryption_configuration.deserialize_json(
                data["diskEncryptionConfiguration"]
            )
        )
    return out


def redact_sensitive(value: ConfigurationOverrides) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "application_configuration" in value:
        import capo_emr_serverless.types.configuration_list

        out["application_configuration"] = (
            capo_emr_serverless.types.configuration_list.redact_sensitive(
                value["application_configuration"]
            )
        )
    return out
