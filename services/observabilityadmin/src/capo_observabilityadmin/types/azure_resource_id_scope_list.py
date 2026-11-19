"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceIdScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_resource_id_scope

AzureResourceIdScopeList: TypeAlias = list[
    "capo_observabilityadmin.types.azure_resource_id_scope.AzureResourceIdScope"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureResourceIdScopeList) -> list:
    import capo_observabilityadmin.types.azure_resource_id_scope

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.azure_resource_id_scope.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AzureResourceIdScopeList:
    import capo_observabilityadmin.types.azure_resource_id_scope

    out: AzureResourceIdScopeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_resource_id_scope.deserialize_json(item)
        )
    return out
