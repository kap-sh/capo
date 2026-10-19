"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterTextAreaControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.sheet_control_title
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.text_area_control_delimiter
    import capo_quicksight.types.text_area_control_display_options


class FilterTextAreaControl(TypedDict, closed=True):
    filter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>FilterTextAreaControl</code>.</p>"""
    title: "capo_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>FilterTextAreaControl</code>.</p>"""
    source_filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The source filter ID of the <code>FilterTextAreaControl</code>.</p>"""
    delimiter: NotRequired[
        "capo_quicksight.types.text_area_control_delimiter.TextAreaControlDelimiter"
    ]
    """<p>The delimiter that is used to separate the lines in text.</p>"""
    display_options: NotRequired[
        "capo_quicksight.types.text_area_control_display_options.TextAreaControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterTextAreaControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceFilterId"] = value["source_filter_id"]
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "display_options" in value:
        import capo_quicksight.types.text_area_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.text_area_control_display_options.serialize_json(
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


def deserialize_json(data: dict) -> FilterTextAreaControl:
    out: FilterTextAreaControl = {}  # type: ignore[typeddict-item]
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
    if data.get("Delimiter") is not None:
        out["delimiter"] = data["Delimiter"]
    if data.get("DisplayOptions") is not None:
        import capo_quicksight.types.text_area_control_display_options

        out["display_options"] = (
            capo_quicksight.types.text_area_control_display_options.deserialize_json(
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
