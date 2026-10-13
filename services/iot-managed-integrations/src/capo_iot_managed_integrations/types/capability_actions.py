"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityActions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_action

CapabilityActions: TypeAlias = list[
    "capo_iot_managed_integrations.types.capability_action.CapabilityAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityActions) -> list:
    import capo_iot_managed_integrations.types.capability_action

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.capability_action.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CapabilityActions:
    import capo_iot_managed_integrations.types.capability_action

    out: CapabilityActions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.capability_action.deserialize_json(item)
        )
    return out


def redact_sensitive(value: CapabilityActions) -> list[Any]:
    import capo_iot_managed_integrations.types.capability_action

    return [
        capo_iot_managed_integrations.types.capability_action.redact_sensitive(item)
        for item in value
    ]
