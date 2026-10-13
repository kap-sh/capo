"""Generated from Smithy shape ``com.amazonaws.quicksight#HeatMapDimensionFieldList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field

HeatMapDimensionFieldList: TypeAlias = list[
    "capo_quicksight.types.dimension_field.DimensionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: HeatMapDimensionFieldList) -> list:
    import capo_quicksight.types.dimension_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.dimension_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> HeatMapDimensionFieldList:
    import capo_quicksight.types.dimension_field

    out: HeatMapDimensionFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.dimension_field.deserialize_json(item))
    return out


def redact_sensitive(value: HeatMapDimensionFieldList) -> list[Any]:
    import capo_quicksight.types.dimension_field

    return [
        capo_quicksight.types.dimension_field.redact_sensitive(item) for item in value
    ]
