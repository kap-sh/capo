"""Generated from Smithy shape ``com.amazonaws.quicksight#LookbackWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.lookback_window_size_unit
    import capo_quicksight.types.positive_long
    import capo_quicksight.types.string


class LookbackWindow(TypedDict, closed=True):
    column_name: "capo_quicksight.types.string.String"
    """<p>The name of the lookback window column.</p>"""
    size: "capo_quicksight.types.positive_long.PositiveLong"
    """<p>The lookback window column size.</p>"""
    size_unit: "capo_quicksight.types.lookback_window_size_unit.LookbackWindowSizeUnit"
    """<p>The size unit that is used for the lookback window column. Valid values for this structure are <code>HOUR</code>, <code>DAY</code>, and <code>WEEK</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LookbackWindow) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    out["Size"] = value["size"]
    import capo_quicksight.types.lookback_window_size_unit

    out["SizeUnit"] = capo_quicksight.types.lookback_window_size_unit.serialize_json(
        value["size_unit"]
    )
    return out


def deserialize_json(data: dict) -> LookbackWindow:
    out: LookbackWindow = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if data.get("SizeUnit") is not None:
        import capo_quicksight.types.lookback_window_size_unit

        out["size_unit"] = (
            capo_quicksight.types.lookback_window_size_unit.deserialize_json(
                data["SizeUnit"]
            )
        )
    else:
        import typing

        out["size_unit"] = typing.cast(
            "capo_quicksight.types.lookback_window_size_unit.LookbackWindowSizeUnit", ""
        )
    return out
