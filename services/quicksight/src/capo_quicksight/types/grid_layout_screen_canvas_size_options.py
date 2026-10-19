"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutScreenCanvasSizeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pixel_length
    import capo_quicksight.types.resize_option


class GridLayoutScreenCanvasSizeOptions(TypedDict, closed=True):
    resize_option: "capo_quicksight.types.resize_option.ResizeOption"
    """<p>This value determines the layout behavior when the viewport is resized.</p> <ul> <li> <p> <code>FIXED</code>: A fixed width will be used when optimizing the layout. In the Quick Sight console, this option is called <code>Classic</code>.</p> </li> <li> <p> <code>RESPONSIVE</code>: The width of the canvas will be responsive and optimized to the view port. In the Quick Sight console, this option is called <code>Tiled</code>.</p> </li> </ul>"""
    optimized_view_port_width: NotRequired[
        "capo_quicksight.types.pixel_length.PixelLength"
    ]
    """<p>The width that the view port will be optimized for when the layout renders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutScreenCanvasSizeOptions) -> dict:
    out: dict = {}
    import capo_quicksight.types.resize_option

    out["ResizeOption"] = capo_quicksight.types.resize_option.serialize_json(
        value["resize_option"]
    )
    if "optimized_view_port_width" in value:
        out["OptimizedViewPortWidth"] = value["optimized_view_port_width"]
    return out


def deserialize_json(data: dict) -> GridLayoutScreenCanvasSizeOptions:
    out: GridLayoutScreenCanvasSizeOptions = {}  # type: ignore[typeddict-item]
    if data.get("ResizeOption") is not None:
        import capo_quicksight.types.resize_option

        out["resize_option"] = capo_quicksight.types.resize_option.deserialize_json(
            data["ResizeOption"]
        )
    else:
        import typing

        out["resize_option"] = typing.cast(
            "capo_quicksight.types.resize_option.ResizeOption", ""
        )
    if data.get("OptimizedViewPortWidth") is not None:
        out["optimized_view_port_width"] = data["OptimizedViewPortWidth"]
    return out
