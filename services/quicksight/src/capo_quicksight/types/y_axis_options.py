"""Generated from Smithy shape ``com.amazonaws.quicksight#YAxisOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.single_y_axis_option


class YAxisOptions(TypedDict, closed=True):
    y_axis: "capo_quicksight.types.single_y_axis_option.SingleYAxisOption"
    """<p>The Y axis type to be used in the chart.</p> <p>If you choose <code>PRIMARY_Y_AXIS</code>, the primary Y Axis is located on the leftmost vertical axis of the chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: YAxisOptions) -> dict:
    out: dict = {}
    import capo_quicksight.types.single_y_axis_option

    out["YAxis"] = capo_quicksight.types.single_y_axis_option.serialize_json(
        value["y_axis"]
    )
    return out


def deserialize_json(data: dict) -> YAxisOptions:
    out: YAxisOptions = {}  # type: ignore[typeddict-item]
    if data.get("YAxis") is not None:
        import capo_quicksight.types.single_y_axis_option

        out["y_axis"] = capo_quicksight.types.single_y_axis_option.deserialize_json(
            data["YAxis"]
        )
    else:
        import typing

        out["y_axis"] = typing.cast(
            "capo_quicksight.types.single_y_axis_option.SingleYAxisOption", ""
        )
    return out
