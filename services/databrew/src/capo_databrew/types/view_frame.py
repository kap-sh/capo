"""Generated from Smithy shape ``com.amazonaws.databrew#ViewFrame``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.analytics_mode
    import capo_databrew.types.column_range
    import capo_databrew.types.hidden_column_list
    import capo_databrew.types.row_range
    import capo_databrew.types.start_column_index
    import capo_databrew.types.start_row_index


class ViewFrame(TypedDict, closed=True):
    start_column_index: "capo_databrew.types.start_column_index.StartColumnIndex"
    """<p>The starting index for the range of columns to return in the view frame.</p>"""
    column_range: NotRequired["capo_databrew.types.column_range.ColumnRange"]
    """<p>The number of columns to include in the view frame, beginning with the <code>StartColumnIndex</code> value and ignoring any columns in the <code>HiddenColumns</code> list.</p>"""
    hidden_columns: NotRequired[
        "capo_databrew.types.hidden_column_list.HiddenColumnList"
    ]
    """<p>A list of columns to hide in the view frame.</p>"""
    start_row_index: NotRequired["capo_databrew.types.start_row_index.StartRowIndex"]
    """<p>The starting index for the range of rows to return in the view frame.</p>"""
    row_range: NotRequired["capo_databrew.types.row_range.RowRange"]
    """<p>The number of rows to include in the view frame, beginning with the <code>StartRowIndex</code> value.</p>"""
    analytics: NotRequired["capo_databrew.types.analytics_mode.AnalyticsMode"]
    """<p>Controls if analytics computation is enabled or disabled. Enabled by default.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewFrame) -> dict:
    out: dict = {}
    out["StartColumnIndex"] = value["start_column_index"]
    if "column_range" in value:
        out["ColumnRange"] = value["column_range"]
    if "hidden_columns" in value:
        import capo_databrew.types.hidden_column_list

        out["HiddenColumns"] = capo_databrew.types.hidden_column_list.serialize_json(
            value["hidden_columns"]
        )
    if "start_row_index" in value:
        out["StartRowIndex"] = value["start_row_index"]
    if "row_range" in value:
        out["RowRange"] = value["row_range"]
    if "analytics" in value:
        import capo_databrew.types.analytics_mode

        out["Analytics"] = capo_databrew.types.analytics_mode.serialize_json(
            value["analytics"]
        )
    return out


def deserialize_json(data: dict) -> ViewFrame:
    out: ViewFrame = {}  # type: ignore[typeddict-item]
    if data.get("StartColumnIndex") is not None:
        out["start_column_index"] = data["StartColumnIndex"]
    else:
        out["start_column_index"] = 0
    if data.get("ColumnRange") is not None:
        out["column_range"] = data["ColumnRange"]
    if data.get("HiddenColumns") is not None:
        import capo_databrew.types.hidden_column_list

        out["hidden_columns"] = capo_databrew.types.hidden_column_list.deserialize_json(
            data["HiddenColumns"]
        )
    if data.get("StartRowIndex") is not None:
        out["start_row_index"] = data["StartRowIndex"]
    if data.get("RowRange") is not None:
        out["row_range"] = data["RowRange"]
    if data.get("Analytics") is not None:
        import capo_databrew.types.analytics_mode

        out["analytics"] = capo_databrew.types.analytics_mode.deserialize_json(
            data["Analytics"]
        )
    return out
