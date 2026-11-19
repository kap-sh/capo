"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_scope_item

AzureSources: TypeAlias = list[
    "capo_observabilityadmin.types.azure_scope_item.AzureScopeItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureSources) -> list:
    import capo_observabilityadmin.types.azure_scope_item

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.azure_scope_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AzureSources:
    import capo_observabilityadmin.types.azure_scope_item

    out: AzureSources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_scope_item.deserialize_json(item)
        )
    return out
