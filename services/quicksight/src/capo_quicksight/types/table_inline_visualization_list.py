"""Generated from Smithy shape ``com.amazonaws.quicksight#TableInlineVisualizationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.table_inline_visualization

TableInlineVisualizationList: TypeAlias = list[
    "capo_quicksight.types.table_inline_visualization.TableInlineVisualization"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableInlineVisualizationList) -> list:
    import capo_quicksight.types.table_inline_visualization

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.table_inline_visualization.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TableInlineVisualizationList:
    import capo_quicksight.types.table_inline_visualization

    out: TableInlineVisualizationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.table_inline_visualization.deserialize_json(item)
        )
    return out


def redact_sensitive(value: TableInlineVisualizationList) -> list[Any]:
    import capo_quicksight.types.table_inline_visualization

    return [
        capo_quicksight.types.table_inline_visualization.redact_sensitive(item)
        for item in value
    ]
