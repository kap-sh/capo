"""Generated from Smithy shape ``com.amazonaws.geoplaces#CrossReferenceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.cross_reference

CrossReferenceList: TypeAlias = list[
    "capo_geo_places.types.cross_reference.CrossReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossReferenceList) -> list:
    import capo_geo_places.types.cross_reference

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.cross_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossReferenceList:
    import capo_geo_places.types.cross_reference

    out: CrossReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.cross_reference.deserialize_json(item))
    return out


def redact_sensitive(value: CrossReferenceList) -> list[Any]:
    import capo_geo_places.types.cross_reference

    return [
        capo_geo_places.types.cross_reference.redact_sensitive(item) for item in value
    ]
