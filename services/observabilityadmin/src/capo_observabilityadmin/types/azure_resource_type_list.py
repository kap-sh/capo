"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_resource_type

AzureResourceTypeList: TypeAlias = list[
    "capo_observabilityadmin.types.azure_resource_type.AzureResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> AzureResourceTypeList:
    return [item for item in data if item is not None]
