"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureSubscriptionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_subscription_summary

AzureSubscriptionSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.azure_subscription_summary.AzureSubscriptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureSubscriptionSummaries) -> list:
    import capo_observabilityadmin.types.azure_subscription_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.azure_subscription_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AzureSubscriptionSummaries:
    import capo_observabilityadmin.types.azure_subscription_summary

    out: AzureSubscriptionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_subscription_summary.deserialize_json(
                item
            )
        )
    return out
