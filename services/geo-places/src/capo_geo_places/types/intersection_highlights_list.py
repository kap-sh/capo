"""Generated from Smithy shape ``com.amazonaws.geoplaces#IntersectionHighlightsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.highlight_list

IntersectionHighlightsList: TypeAlias = list[
    "capo_geo_places.types.highlight_list.HighlightList"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntersectionHighlightsList) -> list:
    import capo_geo_places.types.highlight_list

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.highlight_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntersectionHighlightsList:
    import capo_geo_places.types.highlight_list

    out: IntersectionHighlightsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.highlight_list.deserialize_json(item))
    return out


def redact_sensitive(value: IntersectionHighlightsList) -> list[Any]:
    import capo_geo_places.types.highlight_list

    return [
        capo_geo_places.types.highlight_list.redact_sensitive(item) for item in value
    ]
