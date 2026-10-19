"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterDropDownControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.cascading_control_configuration
    import capo_quicksight.types.commit_mode
    import capo_quicksight.types.control_sort_configuration_list
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.drop_down_control_display_options
    import capo_quicksight.types.filter_selectable_values
    import capo_quicksight.types.sheet_control_list_type
    import capo_quicksight.types.sheet_control_title
    import capo_quicksight.types.short_restrictive_resource_id


class FilterDropDownControl(TypedDict, closed=True):
    filter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>FilterDropDownControl</code>.</p>"""
    title: "capo_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>FilterDropDownControl</code>.</p>"""
    source_filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The source filter ID of the <code>FilterDropDownControl</code>.</p>"""
    display_options: NotRequired[
        "capo_quicksight.types.drop_down_control_display_options.DropDownControlDisplayOptions"
    ]
    """<p>The display options of the <code>FilterDropDownControl</code>.</p>"""
    type: NotRequired[
        "capo_quicksight.types.sheet_control_list_type.SheetControlListType"
    ]
    """<p>The type of the <code>FilterDropDownControl</code>. Choose one of the following options:</p> <ul> <li> <p> <code>MULTI_SELECT</code>: The user can select multiple entries from a dropdown menu.</p> </li> <li> <p> <code>SINGLE_SELECT</code>: The user can select a single entry from a dropdown menu.</p> </li> </ul>"""
    selectable_values: NotRequired[
        "capo_quicksight.types.filter_selectable_values.FilterSelectableValues"
    ]
    """<p>A list of selectable values that are used in a control.</p>"""
    cascading_control_configuration: NotRequired[
        "capo_quicksight.types.cascading_control_configuration.CascadingControlConfiguration"
    ]
    """<p>The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.</p>"""
    commit_mode: NotRequired["capo_quicksight.types.commit_mode.CommitMode"]
    """<p>The visibility configuration of the Apply button on a <code>FilterDropDownControl</code>.</p>"""
    control_sort_configurations: NotRequired[
        "capo_quicksight.types.control_sort_configuration_list.ControlSortConfigurationList"
    ]
    """<p>The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterDropDownControl) -> dict:
    out: dict = {}
    out["FilterControlId"] = value["filter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceFilterId"] = value["source_filter_id"]
    if "display_options" in value:
        import capo_quicksight.types.drop_down_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.drop_down_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import capo_quicksight.types.sheet_control_list_type

        out["Type"] = capo_quicksight.types.sheet_control_list_type.serialize_json(
            value["type"]
        )
    if "selectable_values" in value:
        import capo_quicksight.types.filter_selectable_values

        out["SelectableValues"] = (
            capo_quicksight.types.filter_selectable_values.serialize_json(
                value["selectable_values"]
            )
        )
    if "cascading_control_configuration" in value:
        import capo_quicksight.types.cascading_control_configuration

        out["CascadingControlConfiguration"] = (
            capo_quicksight.types.cascading_control_configuration.serialize_json(
                value["cascading_control_configuration"]
            )
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


def deserialize_json(data: dict) -> FilterDropDownControl:
    out: FilterDropDownControl = {}  # type: ignore[typeddict-item]
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
        import capo_quicksight.types.drop_down_control_display_options

        out["display_options"] = (
            capo_quicksight.types.drop_down_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.sheet_control_list_type

        out["type"] = capo_quicksight.types.sheet_control_list_type.deserialize_json(
            data["Type"]
        )
    if data.get("SelectableValues") is not None:
        import capo_quicksight.types.filter_selectable_values

        out["selectable_values"] = (
            capo_quicksight.types.filter_selectable_values.deserialize_json(
                data["SelectableValues"]
            )
        )
    if data.get("CascadingControlConfiguration") is not None:
        import capo_quicksight.types.cascading_control_configuration

        out["cascading_control_configuration"] = (
            capo_quicksight.types.cascading_control_configuration.deserialize_json(
                data["CascadingControlConfiguration"]
            )
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
