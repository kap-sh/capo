"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalParameterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.decimal_parameter

DecimalParameterList: TypeAlias = list[
    "capo_quicksight.types.decimal_parameter.DecimalParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DecimalParameterList) -> list:
    import capo_quicksight.types.decimal_parameter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.decimal_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DecimalParameterList:
    import capo_quicksight.types.decimal_parameter

    out: DecimalParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.decimal_parameter.deserialize_json(item))
    return out


def redact_sensitive(value: DecimalParameterList) -> list[Any]:
    import capo_quicksight.types.decimal_parameter

    return [
        capo_quicksight.types.decimal_parameter.redact_sensitive(item) for item in value
    ]
