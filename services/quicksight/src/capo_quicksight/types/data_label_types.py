"""Generated from Smithy shape ``com.amazonaws.quicksight#DataLabelTypes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_label_type

DataLabelTypes: TypeAlias = list["capo_quicksight.types.data_label_type.DataLabelType"]


# --- restJson1 ser/de ---
def serialize_json(value: DataLabelTypes) -> list:
    import capo_quicksight.types.data_label_type

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.data_label_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataLabelTypes:
    import capo_quicksight.types.data_label_type

    out: DataLabelTypes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.data_label_type.deserialize_json(item))
    return out


def redact_sensitive(value: DataLabelTypes) -> list[Any]:
    import capo_quicksight.types.data_label_type

    return [
        capo_quicksight.types.data_label_type.redact_sensitive(item) for item in value
    ]
