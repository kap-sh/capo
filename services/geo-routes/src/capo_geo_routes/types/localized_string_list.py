"""Generated from Smithy shape ``com.amazonaws.georoutes#LocalizedStringList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.localized_string

LocalizedStringList: TypeAlias = list[
    "capo_geo_routes.types.localized_string.LocalizedString"
]


# --- restJson1 ser/de ---
def serialize_json(value: LocalizedStringList) -> list:
    import capo_geo_routes.types.localized_string

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.localized_string.serialize_json(item))
    return out


def deserialize_json(data: list) -> LocalizedStringList:
    import capo_geo_routes.types.localized_string

    out: LocalizedStringList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.localized_string.deserialize_json(item))
    return out


def redact_sensitive(value: LocalizedStringList) -> list[Any]:
    import capo_geo_routes.types.localized_string

    return [
        capo_geo_routes.types.localized_string.redact_sensitive(item) for item in value
    ]
