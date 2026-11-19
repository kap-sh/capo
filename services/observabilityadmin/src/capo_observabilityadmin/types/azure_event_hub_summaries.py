"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureEventHubSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_event_hub_summary

AzureEventHubSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.azure_event_hub_summary.AzureEventHubSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureEventHubSummaries) -> list:
    import capo_observabilityadmin.types.azure_event_hub_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.azure_event_hub_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AzureEventHubSummaries:
    import capo_observabilityadmin.types.azure_event_hub_summary

    out: AzureEventHubSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_event_hub_summary.deserialize_json(item)
        )
    return out
