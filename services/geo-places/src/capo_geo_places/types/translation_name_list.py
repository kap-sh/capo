"""Generated from Smithy shape ``com.amazonaws.geoplaces#TranslationNameList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.translation_name

TranslationNameList: TypeAlias = list[
    "capo_geo_places.types.translation_name.TranslationName"
]


# --- restJson1 ser/de ---
def serialize_json(value: TranslationNameList) -> list:
    import capo_geo_places.types.translation_name

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.translation_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> TranslationNameList:
    import capo_geo_places.types.translation_name

    out: TranslationNameList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.translation_name.deserialize_json(item))
    return out


def redact_sensitive(value: TranslationNameList) -> list[Any]:
    import capo_geo_places.types.translation_name

    return [
        capo_geo_places.types.translation_name.redact_sensitive(item) for item in value
    ]
