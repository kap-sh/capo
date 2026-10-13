"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapMeasureFieldList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.measure_field

TreeMapMeasureFieldList: TypeAlias = list[
    "capo_quicksight.types.measure_field.MeasureField"
]


# --- restJson1 ser/de ---
def serialize_json(value: TreeMapMeasureFieldList) -> list:
    import capo_quicksight.types.measure_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.measure_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> TreeMapMeasureFieldList:
    import capo_quicksight.types.measure_field

    out: TreeMapMeasureFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.measure_field.deserialize_json(item))
    return out


def redact_sensitive(value: TreeMapMeasureFieldList) -> list[Any]:
    import capo_quicksight.types.measure_field

    return [
        capo_quicksight.types.measure_field.redact_sensitive(item) for item in value
    ]
