"""Generated from Smithy shape ``com.amazonaws.geoplaces#ParsedQuerySecondaryAddressComponentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.parsed_query_secondary_address_component

ParsedQuerySecondaryAddressComponentList: TypeAlias = list[
    "capo_geo_places.types.parsed_query_secondary_address_component.ParsedQuerySecondaryAddressComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParsedQuerySecondaryAddressComponentList) -> list:
    import capo_geo_places.types.parsed_query_secondary_address_component

    out: list = []
    for item in value:
        out.append(
            capo_geo_places.types.parsed_query_secondary_address_component.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ParsedQuerySecondaryAddressComponentList:
    import capo_geo_places.types.parsed_query_secondary_address_component

    out: ParsedQuerySecondaryAddressComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.parsed_query_secondary_address_component.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ParsedQuerySecondaryAddressComponentList) -> list[Any]:
    import capo_geo_places.types.parsed_query_secondary_address_component

    return [
        capo_geo_places.types.parsed_query_secondary_address_component.redact_sensitive(
            item
        )
        for item in value
    ]
