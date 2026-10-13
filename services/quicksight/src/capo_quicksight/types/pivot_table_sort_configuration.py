"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableSortConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_field_sort_options_list


class PivotTableSortConfiguration(TypedDict, closed=True):
    field_sort_options: NotRequired[
        "capo_quicksight.types.pivot_field_sort_options_list.PivotFieldSortOptionsList"
    ]
    """<p>The field sort options for a pivot table sort configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableSortConfiguration) -> dict:
    out: dict = {}
    if "field_sort_options" in value:
        import capo_quicksight.types.pivot_field_sort_options_list

        out["FieldSortOptions"] = (
            capo_quicksight.types.pivot_field_sort_options_list.serialize_json(
                value["field_sort_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableSortConfiguration:
    out: PivotTableSortConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FieldSortOptions") is not None:
        import capo_quicksight.types.pivot_field_sort_options_list

        out["field_sort_options"] = (
            capo_quicksight.types.pivot_field_sort_options_list.deserialize_json(
                data["FieldSortOptions"]
            )
        )
    return out


def redact_sensitive(value: PivotTableSortConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_sort_options" in value:
        import capo_quicksight.types.pivot_field_sort_options_list

        out["field_sort_options"] = (
            capo_quicksight.types.pivot_field_sort_options_list.redact_sensitive(
                value["field_sort_options"]
            )
        )
    return out
