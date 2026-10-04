"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.filter_cross_sheet_control
    import capo_quicksight.types.filter_date_time_picker_control
    import capo_quicksight.types.filter_drop_down_control
    import capo_quicksight.types.filter_list_control
    import capo_quicksight.types.filter_relative_date_time_control
    import capo_quicksight.types.filter_slider_control
    import capo_quicksight.types.filter_text_area_control
    import capo_quicksight.types.filter_text_field_control
    import capo_quicksight.types.hierarchy_filter_drop_down_control
    import capo_quicksight.types.hierarchy_filter_list_control


class FilterControl(TypedDict, closed=True):
    date_time_picker: NotRequired[
        "capo_quicksight.types.filter_date_time_picker_control.FilterDateTimePickerControl"
    ]
    """<p>A control from a date filter that is used to specify date and time.</p>"""
    list: NotRequired["capo_quicksight.types.filter_list_control.FilterListControl"]
    """<p>A control to display a list of buttons or boxes. This is used to select either a single value or multiple values.</p>"""
    dropdown: NotRequired[
        "capo_quicksight.types.filter_drop_down_control.FilterDropDownControl"
    ]
    """<p>A control to display a dropdown list with buttons that are used to select a single value.</p>"""
    text_field: NotRequired[
        "capo_quicksight.types.filter_text_field_control.FilterTextFieldControl"
    ]
    """<p>A control to display a text box that is used to enter a single entry.</p>"""
    text_area: NotRequired[
        "capo_quicksight.types.filter_text_area_control.FilterTextAreaControl"
    ]
    """<p>A control to display a text box that is used to enter multiple entries.</p>"""
    slider: NotRequired[
        "capo_quicksight.types.filter_slider_control.FilterSliderControl"
    ]
    """<p>A control to display a horizontal toggle bar. This is used to change a value by sliding the toggle.</p>"""
    relative_date_time: NotRequired[
        "capo_quicksight.types.filter_relative_date_time_control.FilterRelativeDateTimeControl"
    ]
    """<p>A control from a date filter that is used to specify the relative date.</p>"""
    cross_sheet: NotRequired[
        "capo_quicksight.types.filter_cross_sheet_control.FilterCrossSheetControl"
    ]
    """<p>A control from a filter that is scoped across more than one sheet. This represents your filter control on a sheet</p>"""
    hierarchy_list: NotRequired[
        "capo_quicksight.types.hierarchy_filter_list_control.HierarchyFilterListControl"
    ]
    """<p>A control from a hierarchy filter that displays the hierarchy as a list. You can expand a value to see and select the values beneath it, and select either a single value or multiple values.</p>"""
    hierarchy_dropdown: NotRequired[
        "capo_quicksight.types.hierarchy_filter_drop_down_control.HierarchyFilterDropDownControl"
    ]
    """<p>A control from a hierarchy filter that displays the hierarchy as a dropdown list. You can expand a value to see and select the values beneath it, and select either a single value or multiple values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterControl) -> dict:
    out: dict = {}
    if "date_time_picker" in value:
        import capo_quicksight.types.filter_date_time_picker_control

        out["DateTimePicker"] = (
            capo_quicksight.types.filter_date_time_picker_control.serialize_json(
                value["date_time_picker"]
            )
        )
    if "list" in value:
        import capo_quicksight.types.filter_list_control

        out["List"] = capo_quicksight.types.filter_list_control.serialize_json(
            value["list"]
        )
    if "dropdown" in value:
        import capo_quicksight.types.filter_drop_down_control

        out["Dropdown"] = capo_quicksight.types.filter_drop_down_control.serialize_json(
            value["dropdown"]
        )
    if "text_field" in value:
        import capo_quicksight.types.filter_text_field_control

        out["TextField"] = (
            capo_quicksight.types.filter_text_field_control.serialize_json(
                value["text_field"]
            )
        )
    if "text_area" in value:
        import capo_quicksight.types.filter_text_area_control

        out["TextArea"] = capo_quicksight.types.filter_text_area_control.serialize_json(
            value["text_area"]
        )
    if "slider" in value:
        import capo_quicksight.types.filter_slider_control

        out["Slider"] = capo_quicksight.types.filter_slider_control.serialize_json(
            value["slider"]
        )
    if "relative_date_time" in value:
        import capo_quicksight.types.filter_relative_date_time_control

        out["RelativeDateTime"] = (
            capo_quicksight.types.filter_relative_date_time_control.serialize_json(
                value["relative_date_time"]
            )
        )
    if "cross_sheet" in value:
        import capo_quicksight.types.filter_cross_sheet_control

        out["CrossSheet"] = (
            capo_quicksight.types.filter_cross_sheet_control.serialize_json(
                value["cross_sheet"]
            )
        )
    if "hierarchy_list" in value:
        import capo_quicksight.types.hierarchy_filter_list_control

        out["HierarchyList"] = (
            capo_quicksight.types.hierarchy_filter_list_control.serialize_json(
                value["hierarchy_list"]
            )
        )
    if "hierarchy_dropdown" in value:
        import capo_quicksight.types.hierarchy_filter_drop_down_control

        out["HierarchyDropdown"] = (
            capo_quicksight.types.hierarchy_filter_drop_down_control.serialize_json(
                value["hierarchy_dropdown"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterControl:
    out: FilterControl = {}  # type: ignore[typeddict-item]
    if data.get("DateTimePicker") is not None:
        import capo_quicksight.types.filter_date_time_picker_control

        out["date_time_picker"] = (
            capo_quicksight.types.filter_date_time_picker_control.deserialize_json(
                data["DateTimePicker"]
            )
        )
    if data.get("List") is not None:
        import capo_quicksight.types.filter_list_control

        out["list"] = capo_quicksight.types.filter_list_control.deserialize_json(
            data["List"]
        )
    if data.get("Dropdown") is not None:
        import capo_quicksight.types.filter_drop_down_control

        out["dropdown"] = (
            capo_quicksight.types.filter_drop_down_control.deserialize_json(
                data["Dropdown"]
            )
        )
    if data.get("TextField") is not None:
        import capo_quicksight.types.filter_text_field_control

        out["text_field"] = (
            capo_quicksight.types.filter_text_field_control.deserialize_json(
                data["TextField"]
            )
        )
    if data.get("TextArea") is not None:
        import capo_quicksight.types.filter_text_area_control

        out["text_area"] = (
            capo_quicksight.types.filter_text_area_control.deserialize_json(
                data["TextArea"]
            )
        )
    if data.get("Slider") is not None:
        import capo_quicksight.types.filter_slider_control

        out["slider"] = capo_quicksight.types.filter_slider_control.deserialize_json(
            data["Slider"]
        )
    if data.get("RelativeDateTime") is not None:
        import capo_quicksight.types.filter_relative_date_time_control

        out["relative_date_time"] = (
            capo_quicksight.types.filter_relative_date_time_control.deserialize_json(
                data["RelativeDateTime"]
            )
        )
    if data.get("CrossSheet") is not None:
        import capo_quicksight.types.filter_cross_sheet_control

        out["cross_sheet"] = (
            capo_quicksight.types.filter_cross_sheet_control.deserialize_json(
                data["CrossSheet"]
            )
        )
    if data.get("HierarchyList") is not None:
        import capo_quicksight.types.hierarchy_filter_list_control

        out["hierarchy_list"] = (
            capo_quicksight.types.hierarchy_filter_list_control.deserialize_json(
                data["HierarchyList"]
            )
        )
    if data.get("HierarchyDropdown") is not None:
        import capo_quicksight.types.hierarchy_filter_drop_down_control

        out["hierarchy_dropdown"] = (
            capo_quicksight.types.hierarchy_filter_drop_down_control.deserialize_json(
                data["HierarchyDropdown"]
            )
        )
    return out
