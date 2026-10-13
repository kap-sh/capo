"""Generated from Smithy shape ``com.amazonaws.quicksight#LogicalTableMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.logical_table
    import capo_quicksight.types.logical_table_id

LogicalTableMap: TypeAlias = dict[
    "capo_quicksight.types.logical_table_id.LogicalTableId",
    "capo_quicksight.types.logical_table.LogicalTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LogicalTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.logical_table

        out[key] = capo_quicksight.types.logical_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LogicalTableMap:
    out: LogicalTableMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_quicksight.types.logical_table

        out[key] = capo_quicksight.types.logical_table.deserialize_json(value)
    return out


def redact_sensitive(value: LogicalTableMap) -> dict[str, Any]:
    import capo_quicksight.types.logical_table

    return {
        key: capo_quicksight.types.logical_table.redact_sensitive(item)
        for key, item in value.items()
    }
