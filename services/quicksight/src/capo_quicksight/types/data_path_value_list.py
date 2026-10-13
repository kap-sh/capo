"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathValueList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_path_value

DataPathValueList: TypeAlias = list[
    "capo_quicksight.types.data_path_value.DataPathValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataPathValueList) -> list:
    import capo_quicksight.types.data_path_value

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.data_path_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataPathValueList:
    import capo_quicksight.types.data_path_value

    out: DataPathValueList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.data_path_value.deserialize_json(item))
    return out


def redact_sensitive(value: DataPathValueList) -> list[Any]:
    import capo_quicksight.types.data_path_value

    return [
        capo_quicksight.types.data_path_value.redact_sensitive(item) for item in value
    ]
