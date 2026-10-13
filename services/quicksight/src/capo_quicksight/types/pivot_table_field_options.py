"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableFieldOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_table_data_path_option_list
    import capo_quicksight.types.pivot_table_field_collapse_state_option_list
    import capo_quicksight.types.pivot_table_field_option_list


class PivotTableFieldOptions(TypedDict, closed=True):
    selected_field_options: NotRequired[
        "capo_quicksight.types.pivot_table_field_option_list.PivotTableFieldOptionList"
    ]
    """<p>The selected field options for the pivot table field options.</p>"""
    data_path_options: NotRequired[
        "capo_quicksight.types.pivot_table_data_path_option_list.PivotTableDataPathOptionList"
    ]
    """<p>The data path options for the pivot table field options.</p>"""
    collapse_state_options: NotRequired[
        "capo_quicksight.types.pivot_table_field_collapse_state_option_list.PivotTableFieldCollapseStateOptionList"
    ]
    """<p>The collapse state options for the pivot table field options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableFieldOptions) -> dict:
    out: dict = {}
    if "selected_field_options" in value:
        import capo_quicksight.types.pivot_table_field_option_list

        out["SelectedFieldOptions"] = (
            capo_quicksight.types.pivot_table_field_option_list.serialize_json(
                value["selected_field_options"]
            )
        )
    if "data_path_options" in value:
        import capo_quicksight.types.pivot_table_data_path_option_list

        out["DataPathOptions"] = (
            capo_quicksight.types.pivot_table_data_path_option_list.serialize_json(
                value["data_path_options"]
            )
        )
    if "collapse_state_options" in value:
        import capo_quicksight.types.pivot_table_field_collapse_state_option_list

        out["CollapseStateOptions"] = (
            capo_quicksight.types.pivot_table_field_collapse_state_option_list.serialize_json(
                value["collapse_state_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableFieldOptions:
    out: PivotTableFieldOptions = {}  # type: ignore[typeddict-item]
    if data.get("SelectedFieldOptions") is not None:
        import capo_quicksight.types.pivot_table_field_option_list

        out["selected_field_options"] = (
            capo_quicksight.types.pivot_table_field_option_list.deserialize_json(
                data["SelectedFieldOptions"]
            )
        )
    if data.get("DataPathOptions") is not None:
        import capo_quicksight.types.pivot_table_data_path_option_list

        out["data_path_options"] = (
            capo_quicksight.types.pivot_table_data_path_option_list.deserialize_json(
                data["DataPathOptions"]
            )
        )
    if data.get("CollapseStateOptions") is not None:
        import capo_quicksight.types.pivot_table_field_collapse_state_option_list

        out["collapse_state_options"] = (
            capo_quicksight.types.pivot_table_field_collapse_state_option_list.deserialize_json(
                data["CollapseStateOptions"]
            )
        )
    return out


def redact_sensitive(value: PivotTableFieldOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_path_options" in value:
        import capo_quicksight.types.pivot_table_data_path_option_list

        out["data_path_options"] = (
            capo_quicksight.types.pivot_table_data_path_option_list.redact_sensitive(
                value["data_path_options"]
            )
        )
    if "collapse_state_options" in value:
        import capo_quicksight.types.pivot_table_field_collapse_state_option_list

        out["collapse_state_options"] = (
            capo_quicksight.types.pivot_table_field_collapse_state_option_list.redact_sensitive(
                value["collapse_state_options"]
            )
        )
    return out
