"""Generated from Smithy shape ``com.amazonaws.geoplaces#OpeningHoursComponentsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.opening_hours_components

OpeningHoursComponentsList: TypeAlias = list[
    "capo_geo_places.types.opening_hours_components.OpeningHoursComponents"
]


# --- restJson1 ser/de ---
def serialize_json(value: OpeningHoursComponentsList) -> list:
    import capo_geo_places.types.opening_hours_components

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.opening_hours_components.serialize_json(item))
    return out


def deserialize_json(data: list) -> OpeningHoursComponentsList:
    import capo_geo_places.types.opening_hours_components

    out: OpeningHoursComponentsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_places.types.opening_hours_components.deserialize_json(item)
        )
    return out


def redact_sensitive(value: OpeningHoursComponentsList) -> list[Any]:
    import capo_geo_places.types.opening_hours_components

    return [
        capo_geo_places.types.opening_hours_components.redact_sensitive(item)
        for item in value
    ]
