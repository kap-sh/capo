"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeResultItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.geocode_result_item

GeocodeResultItemList: TypeAlias = list[
    "capo_geo_places.types.geocode_result_item.GeocodeResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeResultItemList) -> list:
    import capo_geo_places.types.geocode_result_item

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.geocode_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> GeocodeResultItemList:
    import capo_geo_places.types.geocode_result_item

    out: GeocodeResultItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.geocode_result_item.deserialize_json(item))
    return out


def redact_sensitive(value: GeocodeResultItemList) -> list[Any]:
    import capo_geo_places.types.geocode_result_item

    return [
        capo_geo_places.types.geocode_result_item.redact_sensitive(item)
        for item in value
    ]
