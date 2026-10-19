"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterDateTimePickerControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.commit_mode
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.date_time_picker_control_display_options
    import capo_quicksight.types.sheet_control_date_time_picker_type
    import capo_quicksight.types.sheet_control_title
    import capo_quicksight.types.short_restrictive_resource_id


class FilterDateTimePickerControl(TypedDict, closed=True):
    filter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>FilterDateTimePickerControl</code>.</p>"""
    title: "capo_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>FilterDateTimePickerControl</code>.</p>"""
    source_filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The source filter ID of the <code>FilterDateTimePickerControl</code>.</p>"""
    display_options: NotRequired[
        "capo_quicksight.types.date_time_picker_control_display_options.DateTimePickerControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "capo_quicksight.types.sheet_control_date_time_picker_type.SheetControlDateTimePickerType"
    ]
    """<p>The type of the <code>FilterDropDownControl</code>. Choose one of the following options:</p> <ul> <li> <p> <code>MULTI_SELECT</code>: The user can select multiple entries from a dropdown menu.</p> </li> <li> <p> <code>SINGLE_SELECT</code>: The user can select a single entry from a dropdown menu.</p> </li> </ul>"""
    commit_mode: NotRequired["capo_quicksight.types.commit_mode.CommitMode"]
    """<p>The visibility configurationof the Apply button on a <code>DateTimePickerControl</code>.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterDateTimePickerControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceFilterId"] = value["source_filter_id"]
    if "display_options" in value:
        import capo_quicksight.types.date_time_picker_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.date_time_picker_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import capo_quicksight.types.sheet_control_date_time_picker_type

        out["Type"] = (
            capo_quicksight.types.sheet_control_date_time_picker_type.serialize_json(
                value["type"]
            )
        )
    if "commit_mode" in value:
        import capo_quicksight.types.commit_mode

        out["CommitMode"] = capo_quicksight.types.commit_mode.serialize_json(
            value["commit_mode"]
        )
    if "control_title_format_text" in value:
        import capo_quicksight.types.control_title_format_text

        out["ControlTitleFormatText"] = (
            capo_quicksight.types.control_title_format_text.serialize_json(
                value["control_title_format_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterDateTimePickerControl:
    out: FilterDateTimePickerControl = {}  # type: ignore[typeddict-item]
    if data.get("FilterControlId") is not None:
        out["filter_control_id"] = data["FilterControlId"]
    else:
        out["filter_control_id"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("SourceFilterId") is not None:
        out["source_filter_id"] = data["SourceFilterId"]
    else:
        out["source_filter_id"] = ""
    if data.get("DisplayOptions") is not None:
        import capo_quicksight.types.date_time_picker_control_display_options

        out["display_options"] = (
            capo_quicksight.types.date_time_picker_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.sheet_control_date_time_picker_type

        out["type"] = (
            capo_quicksight.types.sheet_control_date_time_picker_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("CommitMode") is not None:
        import capo_quicksight.types.commit_mode

        out["commit_mode"] = capo_quicksight.types.commit_mode.deserialize_json(
            data["CommitMode"]
        )
    if data.get("ControlTitleFormatText") is not None:
        import capo_quicksight.types.control_title_format_text

        out["control_title_format_text"] = (
            capo_quicksight.types.control_title_format_text.deserialize_json(
                data["ControlTitleFormatText"]
            )
        )
    return out
