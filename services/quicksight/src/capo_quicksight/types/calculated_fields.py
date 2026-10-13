"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedFields``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.calculated_field

CalculatedFields: TypeAlias = list[
    "capo_quicksight.types.calculated_field.CalculatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedFields) -> list:
    import capo_quicksight.types.calculated_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.calculated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> CalculatedFields:
    import capo_quicksight.types.calculated_field

    out: CalculatedFields = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.calculated_field.deserialize_json(item))
    return out


def redact_sensitive(value: CalculatedFields) -> list[Any]:
    import capo_quicksight.types.calculated_field

    return [
        capo_quicksight.types.calculated_field.redact_sensitive(item) for item in value
    ]
