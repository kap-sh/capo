"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultFilterControlOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.default_date_time_picker_control_options
    import capo_quicksight.types.default_filter_drop_down_control_options
    import capo_quicksight.types.default_filter_list_control_options
    import capo_quicksight.types.default_hierarchy_filter_drop_down_control_options
    import capo_quicksight.types.default_hierarchy_filter_list_control_options
    import capo_quicksight.types.default_relative_date_time_control_options
    import capo_quicksight.types.default_slider_control_options
    import capo_quicksight.types.default_text_area_control_options
    import capo_quicksight.types.default_text_field_control_options


class DefaultFilterControlOptions(TypedDict, closed=True):
    default_date_time_picker_options: NotRequired[
        "capo_quicksight.types.default_date_time_picker_control_options.DefaultDateTimePickerControlOptions"
    ]
    """<p>The default options that correspond to the filter control type of a <code>DateTimePicker</code>.</p>"""
    default_list_options: NotRequired[
        "capo_quicksight.types.default_filter_list_control_options.DefaultFilterListControlOptions"
    ]
    """<p>The default options that correspond to the <code>List</code> filter control type.</p>"""
    default_dropdown_options: NotRequired[
        "capo_quicksight.types.default_filter_drop_down_control_options.DefaultFilterDropDownControlOptions"
    ]
    """<p>The default options that correspond to the <code>Dropdown</code> filter control type.</p>"""
    default_text_field_options: NotRequired[
        "capo_quicksight.types.default_text_field_control_options.DefaultTextFieldControlOptions"
    ]
    """<p>The default options that correspond to the <code>TextField</code> filter control type.</p>"""
    default_text_area_options: NotRequired[
        "capo_quicksight.types.default_text_area_control_options.DefaultTextAreaControlOptions"
    ]
    """<p>The default options that correspond to the <code>TextArea</code> filter control type.</p>"""
    default_slider_options: NotRequired[
        "capo_quicksight.types.default_slider_control_options.DefaultSliderControlOptions"
    ]
    """<p>The default options that correspond to the <code>Slider</code> filter control type.</p>"""
    default_relative_date_time_options: NotRequired[
        "capo_quicksight.types.default_relative_date_time_control_options.DefaultRelativeDateTimeControlOptions"
    ]
    """<p>The default options that correspond to the <code>RelativeDateTime</code> filter control type.</p>"""
    default_hierarchy_list: NotRequired[
        "capo_quicksight.types.default_hierarchy_filter_list_control_options.DefaultHierarchyFilterListControlOptions"
    ]
    """<p>The default options that correspond to the <code>HierarchyList</code> filter control type.</p>"""
    default_hierarchy_dropdown: NotRequired[
        "capo_quicksight.types.default_hierarchy_filter_drop_down_control_options.DefaultHierarchyFilterDropDownControlOptions"
    ]
    """<p>The default options that correspond to the <code>HierarchyDropdown</code> filter control type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultFilterControlOptions) -> dict:
    out: dict = {}
    if "default_date_time_picker_options" in value:
        import capo_quicksight.types.default_date_time_picker_control_options

        out["DefaultDateTimePickerOptions"] = (
            capo_quicksight.types.default_date_time_picker_control_options.serialize_json(
                value["default_date_time_picker_options"]
            )
        )
    if "default_list_options" in value:
        import capo_quicksight.types.default_filter_list_control_options

        out["DefaultListOptions"] = (
            capo_quicksight.types.default_filter_list_control_options.serialize_json(
                value["default_list_options"]
            )
        )
    if "default_dropdown_options" in value:
        import capo_quicksight.types.default_filter_drop_down_control_options

        out["DefaultDropdownOptions"] = (
            capo_quicksight.types.default_filter_drop_down_control_options.serialize_json(
                value["default_dropdown_options"]
            )
        )
    if "default_text_field_options" in value:
        import capo_quicksight.types.default_text_field_control_options

        out["DefaultTextFieldOptions"] = (
            capo_quicksight.types.default_text_field_control_options.serialize_json(
                value["default_text_field_options"]
            )
        )
    if "default_text_area_options" in value:
        import capo_quicksight.types.default_text_area_control_options

        out["DefaultTextAreaOptions"] = (
            capo_quicksight.types.default_text_area_control_options.serialize_json(
                value["default_text_area_options"]
            )
        )
    if "default_slider_options" in value:
        import capo_quicksight.types.default_slider_control_options

        out["DefaultSliderOptions"] = (
            capo_quicksight.types.default_slider_control_options.serialize_json(
                value["default_slider_options"]
            )
        )
    if "default_relative_date_time_options" in value:
        import capo_quicksight.types.default_relative_date_time_control_options

        out["DefaultRelativeDateTimeOptions"] = (
            capo_quicksight.types.default_relative_date_time_control_options.serialize_json(
                value["default_relative_date_time_options"]
            )
        )
    if "default_hierarchy_list" in value:
        import capo_quicksight.types.default_hierarchy_filter_list_control_options

        out["DefaultHierarchyList"] = (
            capo_quicksight.types.default_hierarchy_filter_list_control_options.serialize_json(
                value["default_hierarchy_list"]
            )
        )
    if "default_hierarchy_dropdown" in value:
        import capo_quicksight.types.default_hierarchy_filter_drop_down_control_options

        out["DefaultHierarchyDropdown"] = (
            capo_quicksight.types.default_hierarchy_filter_drop_down_control_options.serialize_json(
                value["default_hierarchy_dropdown"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultFilterControlOptions:
    out: DefaultFilterControlOptions = {}  # type: ignore[typeddict-item]
    if data.get("DefaultDateTimePickerOptions") is not None:
        import capo_quicksight.types.default_date_time_picker_control_options

        out["default_date_time_picker_options"] = (
            capo_quicksight.types.default_date_time_picker_control_options.deserialize_json(
                data["DefaultDateTimePickerOptions"]
            )
        )
    if data.get("DefaultListOptions") is not None:
        import capo_quicksight.types.default_filter_list_control_options

        out["default_list_options"] = (
            capo_quicksight.types.default_filter_list_control_options.deserialize_json(
                data["DefaultListOptions"]
            )
        )
    if data.get("DefaultDropdownOptions") is not None:
        import capo_quicksight.types.default_filter_drop_down_control_options

        out["default_dropdown_options"] = (
            capo_quicksight.types.default_filter_drop_down_control_options.deserialize_json(
                data["DefaultDropdownOptions"]
            )
        )
    if data.get("DefaultTextFieldOptions") is not None:
        import capo_quicksight.types.default_text_field_control_options

        out["default_text_field_options"] = (
            capo_quicksight.types.default_text_field_control_options.deserialize_json(
                data["DefaultTextFieldOptions"]
            )
        )
    if data.get("DefaultTextAreaOptions") is not None:
        import capo_quicksight.types.default_text_area_control_options

        out["default_text_area_options"] = (
            capo_quicksight.types.default_text_area_control_options.deserialize_json(
                data["DefaultTextAreaOptions"]
            )
        )
    if data.get("DefaultSliderOptions") is not None:
        import capo_quicksight.types.default_slider_control_options

        out["default_slider_options"] = (
            capo_quicksight.types.default_slider_control_options.deserialize_json(
                data["DefaultSliderOptions"]
            )
        )
    if data.get("DefaultRelativeDateTimeOptions") is not None:
        import capo_quicksight.types.default_relative_date_time_control_options

        out["default_relative_date_time_options"] = (
            capo_quicksight.types.default_relative_date_time_control_options.deserialize_json(
                data["DefaultRelativeDateTimeOptions"]
            )
        )
    if data.get("DefaultHierarchyList") is not None:
        import capo_quicksight.types.default_hierarchy_filter_list_control_options

        out["default_hierarchy_list"] = (
            capo_quicksight.types.default_hierarchy_filter_list_control_options.deserialize_json(
                data["DefaultHierarchyList"]
            )
        )
    if data.get("DefaultHierarchyDropdown") is not None:
        import capo_quicksight.types.default_hierarchy_filter_drop_down_control_options

        out["default_hierarchy_dropdown"] = (
            capo_quicksight.types.default_hierarchy_filter_drop_down_control_options.deserialize_json(
                data["DefaultHierarchyDropdown"]
            )
        )
    return out
