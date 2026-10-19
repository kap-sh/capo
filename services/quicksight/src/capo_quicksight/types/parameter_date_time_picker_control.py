"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterDateTimePickerControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.date_time_picker_control_display_options
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.sheet_control_title
    import capo_quicksight.types.short_restrictive_resource_id


class ParameterDateTimePickerControl(TypedDict, closed=True):
    parameter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>ParameterDateTimePickerControl</code>.</p>"""
    title: "capo_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>ParameterDateTimePickerControl</code>.</p>"""
    source_parameter_name: "capo_quicksight.types.parameter_name.ParameterName"
    """<p>The name of the <code>ParameterDateTimePickerControl</code>.</p>"""
    display_options: NotRequired[
        "capo_quicksight.types.date_time_picker_control_display_options.DateTimePickerControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterDateTimePickerControl) -> dict:
    out: dict = {}
    out["ParameterControlId"] = value["parameter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceParameterName"] = value["source_parameter_name"]
    if "display_options" in value:
        import capo_quicksight.types.date_time_picker_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.date_time_picker_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "control_title_format_text" in value:
        import capo_quicksight.types.control_title_format_text

        out["ControlTitleFormatText"] = (
            capo_quicksight.types.control_title_format_text.serialize_json(
                value["control_title_format_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParameterDateTimePickerControl:
    out: ParameterDateTimePickerControl = {}  # type: ignore[typeddict-item]
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
        import capo_quicksight.types.date_time_picker_control_display_options

        out["display_options"] = (
            capo_quicksight.types.date_time_picker_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if data.get("ControlTitleFormatText") is not None:
        import capo_quicksight.types.control_title_format_text

        out["control_title_format_text"] = (
            capo_quicksight.types.control_title_format_text.deserialize_json(
                data["ControlTitleFormatText"]
            )
        )
    return out
