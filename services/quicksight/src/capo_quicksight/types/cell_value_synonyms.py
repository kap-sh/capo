"""Generated from Smithy shape ``com.amazonaws.quicksight#CellValueSynonyms``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.cell_value_synonym

CellValueSynonyms: TypeAlias = list[
    "capo_quicksight.types.cell_value_synonym.CellValueSynonym"
]


# --- restJson1 ser/de ---
def serialize_json(value: CellValueSynonyms) -> list:
    import capo_quicksight.types.cell_value_synonym

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.cell_value_synonym.serialize_json(item))
    return out


def deserialize_json(data: list) -> CellValueSynonyms:
    import capo_quicksight.types.cell_value_synonym

    out: CellValueSynonyms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.cell_value_synonym.deserialize_json(item))
    return out


def redact_sensitive(value: CellValueSynonyms) -> list[Any]:
    import capo_quicksight.types.cell_value_synonym

    return [
        capo_quicksight.types.cell_value_synonym.redact_sensitive(item)
        for item in value
    ]
