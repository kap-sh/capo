"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.manifest_azure_resource_id

AzureResourceIdList: TypeAlias = list[
    "capo_observabilityadmin.types.manifest_azure_resource_id.ManifestAzureResourceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureResourceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AzureResourceIdList:
    return [item for item in data if item is not None]
