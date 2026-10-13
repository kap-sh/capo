"""Generated from Smithy shape ``com.amazonaws.geoplaces#SecondaryAddressComponentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.secondary_address_component

SecondaryAddressComponentList: TypeAlias = list[
    "capo_geo_places.types.secondary_address_component.SecondaryAddressComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecondaryAddressComponentList) -> list:
    import capo_geo_places.types.secondary_address_component

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.secondary_address_component.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecondaryAddressComponentList:
    import capo_geo_places.types.secondary_address_component

    out: SecondaryAddressComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.secondary_address_component.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SecondaryAddressComponentList) -> list[Any]:
    import capo_geo_places.types.secondary_address_component

    return [
        capo_geo_places.types.secondary_address_component.redact_sensitive(item)
        for item in value
    ]
