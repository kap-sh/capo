"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialGradientColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_gradient_step_color_list
    import capo_quicksight.types.geospatial_null_data_settings
    import capo_quicksight.types.opacity
    import capo_quicksight.types.visibility


class GeospatialGradientColor(TypedDict, closed=True):
    step_colors: "capo_quicksight.types.geospatial_gradient_step_color_list.GeospatialGradientStepColorList"
    """<p>A list of gradient step colors for the gradient.</p>"""
    null_data_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The state of visibility for null data.</p>"""
    null_data_settings: NotRequired[
        "capo_quicksight.types.geospatial_null_data_settings.GeospatialNullDataSettings"
    ]
    """<p>The null data visualization settings.</p>"""
    default_opacity: NotRequired["capo_quicksight.types.opacity.Opacity"]
    """<p>The default opacity for the gradient color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialGradientColor) -> dict:
    out: dict = {}
    import capo_quicksight.types.geospatial_gradient_step_color_list

    out["StepColors"] = (
        capo_quicksight.types.geospatial_gradient_step_color_list.serialize_json(
            value["step_colors"]
        )
    )
    if "null_data_visibility" in value:
        import capo_quicksight.types.visibility

        out["NullDataVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["null_data_visibility"]
        )
    if "null_data_settings" in value:
        import capo_quicksight.types.geospatial_null_data_settings

        out["NullDataSettings"] = (
            capo_quicksight.types.geospatial_null_data_settings.serialize_json(
                value["null_data_settings"]
            )
        )
    if "default_opacity" in value:
        out["DefaultOpacity"] = (
            "NaN"
            if value["default_opacity"] != value["default_opacity"]
            else "Infinity"
            if value["default_opacity"] == float("inf")
            else "-Infinity"
            if value["default_opacity"] == float("-inf")
            else value["default_opacity"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialGradientColor:
    out: GeospatialGradientColor = {}  # type: ignore[typeddict-item]
    if data.get("StepColors") is not None:
        import capo_quicksight.types.geospatial_gradient_step_color_list

        out["step_colors"] = (
            capo_quicksight.types.geospatial_gradient_step_color_list.deserialize_json(
                data["StepColors"]
            )
        )
    else:
        out["step_colors"] = []
    if data.get("NullDataVisibility") is not None:
        import capo_quicksight.types.visibility

        out["null_data_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["NullDataVisibility"]
        )
    if data.get("NullDataSettings") is not None:
        import capo_quicksight.types.geospatial_null_data_settings

        out["null_data_settings"] = (
            capo_quicksight.types.geospatial_null_data_settings.deserialize_json(
                data["NullDataSettings"]
            )
        )
    if data.get("DefaultOpacity") is not None:
        out["default_opacity"] = float(data["DefaultOpacity"])
    return out
