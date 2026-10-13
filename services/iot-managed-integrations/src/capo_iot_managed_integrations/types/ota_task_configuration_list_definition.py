"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskConfigurationListDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.ota_task_configuration_summary

OtaTaskConfigurationListDefinition: TypeAlias = list[
    "capo_iot_managed_integrations.types.ota_task_configuration_summary.OtaTaskConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskConfigurationListDefinition) -> list:
    import capo_iot_managed_integrations.types.ota_task_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.ota_task_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OtaTaskConfigurationListDefinition:
    import capo_iot_managed_integrations.types.ota_task_configuration_summary

    out: OtaTaskConfigurationListDefinition = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.ota_task_configuration_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: OtaTaskConfigurationListDefinition) -> list[Any]:
    import capo_iot_managed_integrations.types.ota_task_configuration_summary

    return [
        capo_iot_managed_integrations.types.ota_task_configuration_summary.redact_sensitive(
            item
        )
        for item in value
    ]
