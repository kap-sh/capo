"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureEventHubTier``."""

from typing import Literal, TypeAlias, cast

AzureEventHubTier: TypeAlias = Literal[
    "Standard",
    "Premium",
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureEventHubTier) -> str:
    return value


def deserialize_json(data: str) -> AzureEventHubTier:
    return cast(AzureEventHubTier, data)
