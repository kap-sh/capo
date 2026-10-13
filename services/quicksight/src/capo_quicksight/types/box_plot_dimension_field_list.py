"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotDimensionFieldList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field

BoxPlotDimensionFieldList: TypeAlias = list[
    "capo_quicksight.types.dimension_field.DimensionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotDimensionFieldList) -> list:
    import capo_quicksight.types.dimension_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.dimension_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> BoxPlotDimensionFieldList:
    import capo_quicksight.types.dimension_field

    out: BoxPlotDimensionFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.dimension_field.deserialize_json(item))
    return out


def redact_sensitive(value: BoxPlotDimensionFieldList) -> list[Any]:
    import capo_quicksight.types.dimension_field

    return [
        capo_quicksight.types.dimension_field.redact_sensitive(item) for item in value
    ]
