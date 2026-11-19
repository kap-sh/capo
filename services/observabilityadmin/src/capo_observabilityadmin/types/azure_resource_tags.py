"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_resource_tag_key
    import capo_observabilityadmin.types.azure_resource_tag_value

AzureResourceTags: TypeAlias = dict[
    "capo_observabilityadmin.types.azure_resource_tag_key.AzureResourceTagKey",
    "capo_observabilityadmin.types.azure_resource_tag_value.AzureResourceTagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AzureResourceTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AzureResourceTags:
    out: AzureResourceTags = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
