"""Generated from Smithy shape ``com.amazonaws.quicksight#TableInlineVisualization``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_bars_options
    import capo_quicksight.types.sparklines_options


class TableInlineVisualization(TypedDict, closed=True):
    data_bars: NotRequired["capo_quicksight.types.data_bars_options.DataBarsOptions"]
    """<p>The configuration of the inline visualization of the data bars within a chart.</p>"""
    sparklines: NotRequired[
        "capo_quicksight.types.sparklines_options.SparklinesOptions"
    ]
    """<p>The configuration of the inline visualization of the sparklines within a chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableInlineVisualization) -> dict:
    out: dict = {}
    if "data_bars" in value:
        import capo_quicksight.types.data_bars_options

        out["DataBars"] = capo_quicksight.types.data_bars_options.serialize_json(
            value["data_bars"]
        )
    if "sparklines" in value:
        import capo_quicksight.types.sparklines_options

        out["Sparklines"] = capo_quicksight.types.sparklines_options.serialize_json(
            value["sparklines"]
        )
    return out


def deserialize_json(data: dict) -> TableInlineVisualization:
    out: TableInlineVisualization = {}  # type: ignore[typeddict-item]
    if data.get("DataBars") is not None:
        import capo_quicksight.types.data_bars_options

        out["data_bars"] = capo_quicksight.types.data_bars_options.deserialize_json(
            data["DataBars"]
        )
    if data.get("Sparklines") is not None:
        import capo_quicksight.types.sparklines_options

        out["sparklines"] = capo_quicksight.types.sparklines_options.deserialize_json(
            data["Sparklines"]
        )
    return out


def redact_sensitive(value: TableInlineVisualization) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sparklines" in value:
        import capo_quicksight.types.sparklines_options

        out["sparklines"] = capo_quicksight.types.sparklines_options.redact_sensitive(
            value["sparklines"]
        )
    return out
