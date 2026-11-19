"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureSubscriptionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_subscription_id

AzureSubscriptionIdList: TypeAlias = list[
    "capo_observabilityadmin.types.azure_subscription_id.AzureSubscriptionId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureSubscriptionIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AzureSubscriptionIdList:
    return [item for item in data if item is not None]
