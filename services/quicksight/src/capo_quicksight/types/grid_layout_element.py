"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.border_radius
    import capo_quicksight.types.grid_layout_element_background_style
    import capo_quicksight.types.grid_layout_element_border_style
    import capo_quicksight.types.grid_layout_element_column_index
    import capo_quicksight.types.grid_layout_element_column_span
    import capo_quicksight.types.grid_layout_element_row_index
    import capo_quicksight.types.grid_layout_element_row_span
    import capo_quicksight.types.layout_element_type
    import capo_quicksight.types.loading_animation
    import capo_quicksight.types.padding
    import capo_quicksight.types.short_restrictive_resource_id


class GridLayoutElement(TypedDict, closed=True):
    element_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>A unique identifier for an element within a grid layout.</p>"""
    element_type: "capo_quicksight.types.layout_element_type.LayoutElementType"
    """<p>The type of element.</p>"""
    column_index: NotRequired[
        "capo_quicksight.types.grid_layout_element_column_index.GridLayoutElementColumnIndex"
    ]
    """<p>The column index for the upper left corner of an element.</p>"""
    column_span: "capo_quicksight.types.grid_layout_element_column_span.GridLayoutElementColumnSpan"
    """<p>The width of a grid element expressed as a number of grid columns.</p>"""
    row_index: NotRequired[
        "capo_quicksight.types.grid_layout_element_row_index.GridLayoutElementRowIndex"
    ]
    """<p>The row index for the upper left corner of an element.</p>"""
    row_span: (
        "capo_quicksight.types.grid_layout_element_row_span.GridLayoutElementRowSpan"
    )
    """<p>The height of a grid element expressed as a number of grid rows.</p>"""
    border_style: NotRequired[
        "capo_quicksight.types.grid_layout_element_border_style.GridLayoutElementBorderStyle"
    ]
    """<p>The border style configuration of a grid layout element.</p>"""
    selected_border_style: NotRequired[
        "capo_quicksight.types.grid_layout_element_border_style.GridLayoutElementBorderStyle"
    ]
    """<p>The border style configuration of a grid layout element. This border style is used when the element is selected.</p>"""
    background_style: NotRequired[
        "capo_quicksight.types.grid_layout_element_background_style.GridLayoutElementBackgroundStyle"
    ]
    """<p>The background style configuration of a grid layout element.</p>"""
    loading_animation: NotRequired[
        "capo_quicksight.types.loading_animation.LoadingAnimation"
    ]
    border_radius: NotRequired["capo_quicksight.types.border_radius.BorderRadius"]
    """<p>The border radius of a grid layout element.</p>"""
    padding: NotRequired["capo_quicksight.types.padding.Padding"]
    """<p>The padding of a grid layout element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutElement) -> dict:
    out: dict = {}
    out["ElementId"] = value["element_id"]
    import capo_quicksight.types.layout_element_type

    out["ElementType"] = capo_quicksight.types.layout_element_type.serialize_json(
        value["element_type"]
    )
    if "column_index" in value:
        out["ColumnIndex"] = value["column_index"]
    out["ColumnSpan"] = value["column_span"]
    if "row_index" in value:
        out["RowIndex"] = value["row_index"]
    out["RowSpan"] = value["row_span"]
    if "border_style" in value:
        import capo_quicksight.types.grid_layout_element_border_style

        out["BorderStyle"] = (
            capo_quicksight.types.grid_layout_element_border_style.serialize_json(
                value["border_style"]
            )
        )
    if "selected_border_style" in value:
        import capo_quicksight.types.grid_layout_element_border_style

        out["SelectedBorderStyle"] = (
            capo_quicksight.types.grid_layout_element_border_style.serialize_json(
                value["selected_border_style"]
            )
        )
    if "background_style" in value:
        import capo_quicksight.types.grid_layout_element_background_style

        out["BackgroundStyle"] = (
            capo_quicksight.types.grid_layout_element_background_style.serialize_json(
                value["background_style"]
            )
        )
    if "loading_animation" in value:
        import capo_quicksight.types.loading_animation

        out["LoadingAnimation"] = (
            capo_quicksight.types.loading_animation.serialize_json(
                value["loading_animation"]
            )
        )
    if "border_radius" in value:
        out["BorderRadius"] = value["border_radius"]
    if "padding" in value:
        out["Padding"] = value["padding"]
    return out


def deserialize_json(data: dict) -> GridLayoutElement:
    out: GridLayoutElement = {}  # type: ignore[typeddict-item]
    if data.get("ElementId") is not None:
        out["element_id"] = data["ElementId"]
    else:
        out["element_id"] = ""
    if data.get("ElementType") is not None:
        import capo_quicksight.types.layout_element_type

        out["element_type"] = (
            capo_quicksight.types.layout_element_type.deserialize_json(
                data["ElementType"]
            )
        )
    else:
        import typing

        out["element_type"] = typing.cast(
            "capo_quicksight.types.layout_element_type.LayoutElementType", ""
        )
    if data.get("ColumnIndex") is not None:
        out["column_index"] = data["ColumnIndex"]
    if data.get("ColumnSpan") is not None:
        out["column_span"] = data["ColumnSpan"]
    else:
        out["column_span"] = 0
    if data.get("RowIndex") is not None:
        out["row_index"] = data["RowIndex"]
    if data.get("RowSpan") is not None:
        out["row_span"] = data["RowSpan"]
    else:
        out["row_span"] = 0
    if data.get("BorderStyle") is not None:
        import capo_quicksight.types.grid_layout_element_border_style

        out["border_style"] = (
            capo_quicksight.types.grid_layout_element_border_style.deserialize_json(
                data["BorderStyle"]
            )
        )
    if data.get("SelectedBorderStyle") is not None:
        import capo_quicksight.types.grid_layout_element_border_style

        out["selected_border_style"] = (
            capo_quicksight.types.grid_layout_element_border_style.deserialize_json(
                data["SelectedBorderStyle"]
            )
        )
    if data.get("BackgroundStyle") is not None:
        import capo_quicksight.types.grid_layout_element_background_style

        out["background_style"] = (
            capo_quicksight.types.grid_layout_element_background_style.deserialize_json(
                data["BackgroundStyle"]
            )
        )
    if data.get("LoadingAnimation") is not None:
        import capo_quicksight.types.loading_animation

        out["loading_animation"] = (
            capo_quicksight.types.loading_animation.deserialize_json(
                data["LoadingAnimation"]
            )
        )
    if data.get("BorderRadius") is not None:
        out["border_radius"] = data["BorderRadius"]
    if data.get("Padding") is not None:
        out["padding"] = data["Padding"]
    return out
