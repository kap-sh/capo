"""Generated from Smithy shape ``com.amazonaws.quicksight#ColorScale``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.color_fill_type
    import capo_quicksight.types.color_scale_color_list
    import capo_quicksight.types.data_color


class ColorScale(TypedDict, closed=True):
    colors: "capo_quicksight.types.color_scale_color_list.ColorScaleColorList"
    """<p>Determines the list of colors that are applied to the visual.</p>"""
    color_fill_type: "capo_quicksight.types.color_fill_type.ColorFillType"
    """<p>Determines the color fill type.</p>"""
    null_value_color: NotRequired["capo_quicksight.types.data_color.DataColor"]
    """<p>Determines the color that is applied to null values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColorScale) -> dict:
    out: dict = {}
    import capo_quicksight.types.color_scale_color_list

    out["Colors"] = capo_quicksight.types.color_scale_color_list.serialize_json(
        value["colors"]
    )
    import capo_quicksight.types.color_fill_type

    out["ColorFillType"] = capo_quicksight.types.color_fill_type.serialize_json(
        value["color_fill_type"]
    )
    if "null_value_color" in value:
        import capo_quicksight.types.data_color

        out["NullValueColor"] = capo_quicksight.types.data_color.serialize_json(
            value["null_value_color"]
        )
    return out


def deserialize_json(data: dict) -> ColorScale:
    out: ColorScale = {}  # type: ignore[typeddict-item]
    if data.get("Colors") is not None:
        import capo_quicksight.types.color_scale_color_list

        out["colors"] = capo_quicksight.types.color_scale_color_list.deserialize_json(
            data["Colors"]
        )
    else:
        out["colors"] = []
    if data.get("ColorFillType") is not None:
        import capo_quicksight.types.color_fill_type

        out["color_fill_type"] = capo_quicksight.types.color_fill_type.deserialize_json(
            data["ColorFillType"]
        )
    else:
        import typing

        out["color_fill_type"] = typing.cast(
            "capo_quicksight.types.color_fill_type.ColorFillType", ""
        )
    if data.get("NullValueColor") is not None:
        import capo_quicksight.types.data_color

        out["null_value_color"] = capo_quicksight.types.data_color.deserialize_json(
            data["NullValueColor"]
        )
    return out
