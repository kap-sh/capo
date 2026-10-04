"""Generated from Smithy shape ``com.amazonaws.quicksight#HierarchyFilterDropDownControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.commit_mode
    import capo_quicksight.types.control_sort_configuration_list
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.hierarchy_filter_drop_down_control_display_options
    import capo_quicksight.types.sheet_control_list_type
    import capo_quicksight.types.sheet_control_title
    import capo_quicksight.types.short_restrictive_resource_id


class HierarchyFilterDropDownControl(TypedDict, closed=True):
    filter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>HierarchyFilterDropDownControl</code>.</p>"""
    source_filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The source filter ID of the <code>HierarchyFilterDropDownControl</code>. This must be the <code>FilterId</code> of a <code>HierarchyFilter</code>.</p>"""
    title: NotRequired["capo_quicksight.types.sheet_control_title.SheetControlTitle"]
    """<p>The title of the <code>HierarchyFilterDropDownControl</code>.</p>"""
    display_options: NotRequired[
        "capo_quicksight.types.hierarchy_filter_drop_down_control_display_options.HierarchyFilterDropDownControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "capo_quicksight.types.sheet_control_list_type.SheetControlListType"
    ]
    """<p>The type of the <code>HierarchyFilterDropDownControl</code>. Choose one of the following options:</p> <ul> <li> <p> <code>MULTI_SELECT</code>: The user can select multiple entries from a dropdown menu.</p> </li> <li> <p> <code>SINGLE_SELECT</code>: The user can select a single entry from a dropdown menu.</p> </li> </ul>"""
    commit_mode: NotRequired["capo_quicksight.types.commit_mode.CommitMode"]
    """<p>The visibility configuration of the Apply button on a <code>HierarchyFilterDropDownControl</code>.</p>"""
    control_sort_configurations: NotRequired[
        "capo_quicksight.types.control_sort_configuration_list.ControlSortConfigurationList"
    ]
    """<p>The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyFilterDropDownControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["SourceFilterId"] = value["source_filter_id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "display_options" in value:
        import capo_quicksight.types.hierarchy_filter_drop_down_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.hierarchy_filter_drop_down_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import capo_quicksight.types.sheet_control_list_type

        out["Type"] = capo_quicksight.types.sheet_control_list_type.serialize_json(
            value["type"]
        )
    if "commit_mode" in value:
        import capo_quicksight.types.commit_mode

        out["CommitMode"] = capo_quicksight.types.commit_mode.serialize_json(
            value["commit_mode"]
        )
    if "control_sort_configurations" in value:
        import capo_quicksight.types.control_sort_configuration_list

        out["ControlSortConfigurations"] = (
            capo_quicksight.types.control_sort_configuration_list.serialize_json(
                value["control_sort_configurations"]
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


def deserialize_json(data: dict) -> HierarchyFilterDropDownControl:
    out: HierarchyFilterDropDownControl = {}  # type: ignore[typeddict-item]
    if data.get("FilterControlId") is not None:
        out["filter_control_id"] = data["FilterControlId"]
    else:
        raise DeserializationError(
            "HierarchyFilterDropDownControl.filter_control_id required"
        )
    if data.get("SourceFilterId") is not None:
        out["source_filter_id"] = data["SourceFilterId"]
    else:
        raise DeserializationError(
            "HierarchyFilterDropDownControl.source_filter_id required"
        )
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("DisplayOptions") is not None:
        import capo_quicksight.types.hierarchy_filter_drop_down_control_display_options

        out["display_options"] = (
            capo_quicksight.types.hierarchy_filter_drop_down_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.sheet_control_list_type

        out["type"] = capo_quicksight.types.sheet_control_list_type.deserialize_json(
            data["Type"]
        )
    if data.get("CommitMode") is not None:
        import capo_quicksight.types.commit_mode

        out["commit_mode"] = capo_quicksight.types.commit_mode.deserialize_json(
            data["CommitMode"]
        )
    if data.get("ControlSortConfigurations") is not None:
        import capo_quicksight.types.control_sort_configuration_list

        out["control_sort_configurations"] = (
            capo_quicksight.types.control_sort_configuration_list.deserialize_json(
                data["ControlSortConfigurations"]
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
