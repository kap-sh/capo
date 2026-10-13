"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingListDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.managed_thing_summary

ManagedThingListDefinition: TypeAlias = list[
    "capo_iot_managed_integrations.types.managed_thing_summary.ManagedThingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingListDefinition) -> list:
    import capo_iot_managed_integrations.types.managed_thing_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.managed_thing_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ManagedThingListDefinition:
    import capo_iot_managed_integrations.types.managed_thing_summary

    out: ManagedThingListDefinition = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.managed_thing_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ManagedThingListDefinition) -> list[Any]:
    import capo_iot_managed_integrations.types.managed_thing_summary

    return [
        capo_iot_managed_integrations.types.managed_thing_summary.redact_sensitive(item)
        for item in value
    ]
