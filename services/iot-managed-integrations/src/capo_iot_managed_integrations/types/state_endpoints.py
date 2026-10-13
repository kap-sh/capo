"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StateEndpoints``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.state_endpoint

StateEndpoints: TypeAlias = list[
    "capo_iot_managed_integrations.types.state_endpoint.StateEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: StateEndpoints) -> list:
    import capo_iot_managed_integrations.types.state_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.state_endpoint.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StateEndpoints:
    import capo_iot_managed_integrations.types.state_endpoint

    out: StateEndpoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.state_endpoint.deserialize_json(item)
        )
    return out


def redact_sensitive(value: StateEndpoints) -> list[Any]:
    import capo_iot_managed_integrations.types.state_endpoint

    return [
        capo_iot_managed_integrations.types.state_endpoint.redact_sensitive(item)
        for item in value
    ]
