"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.grid_layout_canvas_size_options
    import capo_quicksight.types.grid_layout_element_list


class GridLayoutConfiguration(TypedDict, closed=True):
    elements: "capo_quicksight.types.grid_layout_element_list.GridLayoutElementList"
    """<p>The elements that are included in a grid layout.</p>"""
    canvas_size_options: NotRequired[
        "capo_quicksight.types.grid_layout_canvas_size_options.GridLayoutCanvasSizeOptions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.grid_layout_element_list

    out["Elements"] = capo_quicksight.types.grid_layout_element_list.serialize_json(
        value["elements"]
    )
    if "canvas_size_options" in value:
        import capo_quicksight.types.grid_layout_canvas_size_options

        out["CanvasSizeOptions"] = (
            capo_quicksight.types.grid_layout_canvas_size_options.serialize_json(
                value["canvas_size_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> GridLayoutConfiguration:
    out: GridLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Elements") is not None:
        import capo_quicksight.types.grid_layout_element_list

        out["elements"] = (
            capo_quicksight.types.grid_layout_element_list.deserialize_json(
                data["Elements"]
            )
        )
    else:
        out["elements"] = []
    if data.get("CanvasSizeOptions") is not None:
        import capo_quicksight.types.grid_layout_canvas_size_options

        out["canvas_size_options"] = (
            capo_quicksight.types.grid_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    return out
