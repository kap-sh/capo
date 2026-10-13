"""Generated from Smithy shape ``com.amazonaws.quicksight#PhysicalTableMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.physical_table
    import capo_quicksight.types.physical_table_id

PhysicalTableMap: TypeAlias = dict[
    "capo_quicksight.types.physical_table_id.PhysicalTableId",
    "capo_quicksight.types.physical_table.PhysicalTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PhysicalTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.physical_table

        out[key] = capo_quicksight.types.physical_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PhysicalTableMap:
    out: PhysicalTableMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_quicksight.types.physical_table

        out[key] = capo_quicksight.types.physical_table.deserialize_json(value)
    return out


def redact_sensitive(value: PhysicalTableMap) -> dict[str, Any]:
    import capo_quicksight.types.physical_table

    return {
        key: capo_quicksight.types.physical_table.redact_sensitive(item)
        for key, item in value.items()
    }
