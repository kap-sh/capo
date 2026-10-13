"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringFilterStaticValueList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_string_filter_static_value

DataSetStringFilterStaticValueList: TypeAlias = list[
    "capo_quicksight.types.data_set_string_filter_static_value.DataSetStringFilterStaticValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringFilterStaticValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> DataSetStringFilterStaticValueList:
    return [item for item in data if item is not None]


def redact_sensitive(value: DataSetStringFilterStaticValueList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
