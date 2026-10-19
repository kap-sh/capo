"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterListControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.cascading_control_configuration
    import capo_quicksight.types.control_sort_configuration_list
    import capo_quicksight.types.control_title_format_text
    import capo_quicksight.types.list_control_display_options
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.parameter_selectable_values
    import capo_quicksight.types.sheet_control_list_type
    import capo_quicksight.types.sheet_control_title
    import capo_quicksight.types.short_restrictive_resource_id


class ParameterListControl(TypedDict, closed=True):
    parameter_control_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>ParameterListControl</code>.</p>"""
    title: "capo_quicksight.types.sheet_control_title.SheetControlTitle"
    """<p>The title of the <code>ParameterListControl</code>.</p>"""
    source_parameter_name: "capo_quicksight.types.parameter_name.ParameterName"
    """<p>The source parameter name of the <code>ParameterListControl</code>.</p>"""
    display_options: NotRequired[
        "capo_quicksight.types.list_control_display_options.ListControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "capo_quicksight.types.sheet_control_list_type.SheetControlListType"
    ]
    """<p>The type of <code>ParameterListControl</code>.</p>"""
    selectable_values: NotRequired[
        "capo_quicksight.types.parameter_selectable_values.ParameterSelectableValues"
    ]
    """<p>A list of selectable values that are used in a control.</p>"""
    cascading_control_configuration: NotRequired[
        "capo_quicksight.types.cascading_control_configuration.CascadingControlConfiguration"
    ]
    """<p>The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.</p>"""
    control_sort_configurations: NotRequired[
        "capo_quicksight.types.control_sort_configuration_list.ControlSortConfigurationList"
    ]
    """<p>The sort configuration for the values displayed in the control. Only one sort configuration can be applied per control.</p>"""
    control_title_format_text: NotRequired[
        "capo_quicksight.types.control_title_format_text.ControlTitleFormatText"
    ]
    """<p>The title text format configuration for the control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterListControl) -> dict:
    out: dict = {}
    out["ParameterControlId"] = value["parameter_control_id"]
    out["Title"] = value.get("title", "")
    out["SourceParameterName"] = value["source_parameter_name"]
    if "display_options" in value:
        import capo_quicksight.types.list_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.list_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import capo_quicksight.types.sheet_control_list_type

        out["Type"] = capo_quicksight.types.sheet_control_list_type.serialize_json(
            value["type"]
        )
    if "selectable_values" in value:
        import capo_quicksight.types.parameter_selectable_values

        out["SelectableValues"] = (
            capo_quicksight.types.parameter_selectable_values.serialize_json(
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


def deserialize_json(data: dict) -> ParameterListControl:
    out: ParameterListControl = {}  # type: ignore[typeddict-item]
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
        import capo_quicksight.types.list_control_display_options

        out["display_options"] = (
            capo_quicksight.types.list_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.sheet_control_list_type

        out["type"] = capo_quicksight.types.sheet_control_list_type.deserialize_json(
            data["Type"]
        )
    if data.get("SelectableValues") is not None:
        import capo_quicksight.types.parameter_selectable_values

        out["selectable_values"] = (
            capo_quicksight.types.parameter_selectable_values.deserialize_json(
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
