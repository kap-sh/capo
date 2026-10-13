"""Generated from Smithy shape ``com.amazonaws.geoplaces#ParsedQueryComponentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.parsed_query_component

ParsedQueryComponentList: TypeAlias = list[
    "capo_geo_places.types.parsed_query_component.ParsedQueryComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParsedQueryComponentList) -> list:
    import capo_geo_places.types.parsed_query_component

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.parsed_query_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParsedQueryComponentList:
    import capo_geo_places.types.parsed_query_component

    out: ParsedQueryComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.parsed_query_component.deserialize_json(item))
    return out


def redact_sensitive(value: ParsedQueryComponentList) -> list[Any]:
    import capo_geo_places.types.parsed_query_component

    return [
        capo_geo_places.types.parsed_query_component.redact_sensitive(item)
        for item in value
    ]
