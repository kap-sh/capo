"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeParameterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.date_time_parameter

DateTimeParameterList: TypeAlias = list[
    "capo_quicksight.types.date_time_parameter.DateTimeParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeParameterList) -> list:
    import capo_quicksight.types.date_time_parameter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.date_time_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DateTimeParameterList:
    import capo_quicksight.types.date_time_parameter

    out: DateTimeParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.date_time_parameter.deserialize_json(item))
    return out


def redact_sensitive(value: DateTimeParameterList) -> list[Any]:
    import capo_quicksight.types.date_time_parameter

    return [
        capo_quicksight.types.date_time_parameter.redact_sensitive(item)
        for item in value
    ]
