"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_region

AzureRegionList: TypeAlias = list[
    "capo_observabilityadmin.types.azure_region.AzureRegion"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> AzureRegionList:
    return [item for item in data if item is not None]
