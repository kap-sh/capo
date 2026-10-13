"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapDimensionFieldList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field

FilledMapDimensionFieldList: TypeAlias = list[
    "capo_quicksight.types.dimension_field.DimensionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapDimensionFieldList) -> list:
    import capo_quicksight.types.dimension_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.dimension_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilledMapDimensionFieldList:
    import capo_quicksight.types.dimension_field

    out: FilledMapDimensionFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.dimension_field.deserialize_json(item))
    return out


def redact_sensitive(value: FilledMapDimensionFieldList) -> list[Any]:
    import capo_quicksight.types.dimension_field

    return [
        capo_quicksight.types.dimension_field.redact_sensitive(item) for item in value
    ]
