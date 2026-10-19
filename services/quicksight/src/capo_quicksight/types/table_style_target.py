"""Generated from Smithy shape ``com.amazonaws.quicksight#TableStyleTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.styled_cell_type


class TableStyleTarget(TypedDict, closed=True):
    cell_type: "capo_quicksight.types.styled_cell_type.StyledCellType"
    """<p>The cell type of the table style target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableStyleTarget) -> dict:
    out: dict = {}
    import capo_quicksight.types.styled_cell_type

    out["CellType"] = capo_quicksight.types.styled_cell_type.serialize_json(
        value["cell_type"]
    )
    return out


def deserialize_json(data: dict) -> TableStyleTarget:
    out: TableStyleTarget = {}  # type: ignore[typeddict-item]
    if data.get("CellType") is not None:
        import capo_quicksight.types.styled_cell_type

        out["cell_type"] = capo_quicksight.types.styled_cell_type.deserialize_json(
            data["CellType"]
        )
    else:
        import typing

        out["cell_type"] = typing.cast(
            "capo_quicksight.types.styled_cell_type.StyledCellType", ""
        )
    return out
