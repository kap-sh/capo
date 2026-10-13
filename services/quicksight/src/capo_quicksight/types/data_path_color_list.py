"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathColorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_path_color

DataPathColorList: TypeAlias = list[
    "capo_quicksight.types.data_path_color.DataPathColor"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataPathColorList) -> list:
    import capo_quicksight.types.data_path_color

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.data_path_color.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataPathColorList:
    import capo_quicksight.types.data_path_color

    out: DataPathColorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.data_path_color.deserialize_json(item))
    return out


def redact_sensitive(value: DataPathColorList) -> list[Any]:
    import capo_quicksight.types.data_path_color

    return [
        capo_quicksight.types.data_path_color.redact_sensitive(item) for item in value
    ]
