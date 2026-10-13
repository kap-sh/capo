"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerParameterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.integer_parameter

IntegerParameterList: TypeAlias = list[
    "capo_quicksight.types.integer_parameter.IntegerParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegerParameterList) -> list:
    import capo_quicksight.types.integer_parameter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.integer_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntegerParameterList:
    import capo_quicksight.types.integer_parameter

    out: IntegerParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.integer_parameter.deserialize_json(item))
    return out


def redact_sensitive(value: IntegerParameterList) -> list[Any]:
    import capo_quicksight.types.integer_parameter

    return [
        capo_quicksight.types.integer_parameter.redact_sensitive(item) for item in value
    ]
