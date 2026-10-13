"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchByAttributeValues``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_medical_imaging.types.search_by_attribute_value

SearchByAttributeValues: TypeAlias = list[
    "capo_medical_imaging.types.search_by_attribute_value.SearchByAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchByAttributeValues) -> list:
    import capo_medical_imaging.types.search_by_attribute_value

    out: list = []
    for item in value:
        out.append(
            capo_medical_imaging.types.search_by_attribute_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchByAttributeValues:
    import capo_medical_imaging.types.search_by_attribute_value

    out: SearchByAttributeValues = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_medical_imaging.types.search_by_attribute_value.deserialize_json(item)
        )
    return out


def redact_sensitive(value: SearchByAttributeValues) -> list[Any]:
    import capo_medical_imaging.types.search_by_attribute_value

    return [
        capo_medical_imaging.types.search_by_attribute_value.redact_sensitive(item)
        for item in value
    ]
