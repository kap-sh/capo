"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticTableMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_entity_resource_id
    import capo_quicksight.types.semantic_table

SemanticTableMap: TypeAlias = dict[
    "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId",
    "capo_quicksight.types.semantic_table.SemanticTable",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SemanticTableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.semantic_table

        out[key] = capo_quicksight.types.semantic_table.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SemanticTableMap:
    out: SemanticTableMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_quicksight.types.semantic_table

        out[key] = capo_quicksight.types.semantic_table.deserialize_json(value)
    return out


def redact_sensitive(value: SemanticTableMap) -> dict[str, Any]:
    import capo_quicksight.types.semantic_table

    return {
        key: capo_quicksight.types.semantic_table.redact_sensitive(item)
        for key, item in value.items()
    }
