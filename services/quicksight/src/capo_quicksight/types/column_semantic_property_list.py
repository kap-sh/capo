"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSemanticPropertyList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_semantic_property

ColumnSemanticPropertyList: TypeAlias = list[
    "capo_quicksight.types.column_semantic_property.ColumnSemanticProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSemanticPropertyList) -> list:
    import capo_quicksight.types.column_semantic_property

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_semantic_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnSemanticPropertyList:
    import capo_quicksight.types.column_semantic_property

    out: ColumnSemanticPropertyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.column_semantic_property.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ColumnSemanticPropertyList) -> list[Any]:
    import capo_quicksight.types.column_semantic_property

    return [
        capo_quicksight.types.column_semantic_property.redact_sensitive(item)
        for item in value
    ]
