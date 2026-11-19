"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureEventHubConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_event_hub_partition_count
    import capo_observabilityadmin.types.azure_event_hub_tier


class AzureEventHubConfiguration(TypedDict, closed=True):
    tier: "capo_observabilityadmin.types.azure_event_hub_tier.AzureEventHubTier"
    """<p>The Event Hubs namespace tier.</p>"""
    partition_count: "capo_observabilityadmin.types.azure_event_hub_partition_count.AzureEventHubPartitionCount"
    """<p>The number of partitions in each Event Hub. The Standard tier allows 1–32 partitions and the Premium tier allows 1–100. On the Standard tier, you can't change this value after the setup creates the Event Hub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureEventHubConfiguration) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.azure_event_hub_tier

    out["Tier"] = capo_observabilityadmin.types.azure_event_hub_tier.serialize_json(
        value["tier"]
    )
    out["PartitionCount"] = value["partition_count"]
    return out


def deserialize_json(data: dict) -> AzureEventHubConfiguration:
    out: AzureEventHubConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Tier") is not None:
        import capo_observabilityadmin.types.azure_event_hub_tier

        out["tier"] = (
            capo_observabilityadmin.types.azure_event_hub_tier.deserialize_json(
                data["Tier"]
            )
        )
    else:
        import typing

        out["tier"] = typing.cast(
            "capo_observabilityadmin.types.azure_event_hub_tier.AzureEventHubTier", ""
        )
    if data.get("PartitionCount") is not None:
        out["partition_count"] = data["PartitionCount"]
    else:
        out["partition_count"] = 0
    return out
