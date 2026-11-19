"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureEventHubConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_event_hub_configuration

AzureEventHubConfigurationList: TypeAlias = list[
    "capo_observabilityadmin.types.azure_event_hub_configuration.AzureEventHubConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureEventHubConfigurationList) -> list:
    import capo_observabilityadmin.types.azure_event_hub_configuration

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.azure_event_hub_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AzureEventHubConfigurationList:
    import capo_observabilityadmin.types.azure_event_hub_configuration

    out: AzureEventHubConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_event_hub_configuration.deserialize_json(
                item
            )
        )
    return out
