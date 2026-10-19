"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterSliderControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.double
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.sheet_control_title
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.slider_control_display_options


class ParameterSliderControl(TypedDict, closed=True):
    parameter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>ParameterSliderControl</code>.</p>"""
    title: "capo_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>ParameterSliderControl</code>.</p>"""
    source_parameter_name: "capo_quicksight.types.parameter_name.ParameterName"
    """<p>The source parameter name of the <code>ParameterSliderControl</code>.</p>"""
    display_options: NotRequired[
        "capo_quicksight.types.slider_control_display_options.SliderControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    maximum_value: "capo_quicksight.types.double.Double"
    """<p>The larger value that is displayed at the right of the slider.</p>"""
    minimum_value: "capo_quicksight.types.double.Double"
    """<p>The smaller value that is displayed at the left of the slider.</p>"""
    step_size: "capo_quicksight.types.double.Double"
    """<p>The number of increments that the slider bar is divided into.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSliderControl) -> dict:
    out: dict = {}
    out["ParameterControlId"] = value["parameter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceParameterName"] = value["source_parameter_name"]
    if "display_options" in value:
        import capo_quicksight.types.slider_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.slider_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    out["MaximumValue"] = (
        "NaN"
        if value.get("maximum_value", 0) != value.get("maximum_value", 0)
        else "Infinity"
        if value.get("maximum_value", 0) == float("inf")
        else "-Infinity"
        if value.get("maximum_value", 0) == float("-inf")
        else value.get("maximum_value", 0)
    )
    out["MinimumValue"] = (
        "NaN"
        if value.get("minimum_value", 0) != value.get("minimum_value", 0)
        else "Infinity"
        if value.get("minimum_value", 0) == float("inf")
        else "-Infinity"
        if value.get("minimum_value", 0) == float("-inf")
        else value.get("minimum_value", 0)
    )
    out["StepSize"] = (
        "NaN"
        if value.get("step_size", 0) != value.get("step_size", 0)
        else "Infinity"
        if value.get("step_size", 0) == float("inf")
        else "-Infinity"
        if value.get("step_size", 0) == float("-inf")
        else value.get("step_size", 0)
    )
    if "control_title_format_text" in value:
        import capo_quicksight.types.control_title_format_text

        out["ControlTitleFormatText"] = (
            capo_quicksight.types.control_title_format_text.serialize_json(
                value["control_title_format_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParameterSliderControl:
    out: ParameterSliderControl = {}  # type: ignore[typeddict-item]
    if data.get("ParameterControlId") is not None:
        out["parameter_control_id"] = data["ParameterControlId"]
    else:
        out["parameter_control_id"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("SourceParameterName") is not None:
        out["source_parameter_name"] = data["SourceParameterName"]
    else:
        out["source_parameter_name"] = ""
    if data.get("DisplayOptions") is not None:
        import capo_quicksight.types.slider_control_display_options

        out["display_options"] = (
            capo_quicksight.types.slider_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if data.get("MaximumValue") is not None:
        out["maximum_value"] = float(data["MaximumValue"])
    else:
        out["maximum_value"] = 0
    if data.get("MinimumValue") is not None:
        out["minimum_value"] = float(data["MinimumValue"])
    else:
        out["minimum_value"] = 0
    if data.get("StepSize") is not None:
        out["step_size"] = float(data["StepSize"])
    else:
        out["step_size"] = 0
    if data.get("ControlTitleFormatText") is not None:
        import capo_quicksight.types.control_title_format_text

        out["control_title_format_text"] = (
            capo_quicksight.types.control_title_format_text.deserialize_json(
                data["ControlTitleFormatText"]
            )
        )
    return out
