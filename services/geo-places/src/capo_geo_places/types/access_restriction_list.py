"""Generated from Smithy shape ``com.amazonaws.geoplaces#AccessRestrictionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.access_restriction

AccessRestrictionList: TypeAlias = list[
    "capo_geo_places.types.access_restriction.AccessRestriction"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessRestrictionList) -> list:
    import capo_geo_places.types.access_restriction

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.access_restriction.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessRestrictionList:
    import capo_geo_places.types.access_restriction

    out: AccessRestrictionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.access_restriction.deserialize_json(item))
    return out


def redact_sensitive(value: AccessRestrictionList) -> list[Any]:
    import capo_geo_places.types.access_restriction

    return [
        capo_geo_places.types.access_restriction.redact_sensitive(item)
        for item in value
    ]
