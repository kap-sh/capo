"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableSortBy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_sort
    import capo_quicksight.types.data_path_sort
    import capo_quicksight.types.field_sort


class PivotTableSortBy(TypedDict, closed=True):
    field: NotRequired["capo_quicksight.types.field_sort.FieldSort"]
    """<p>The field sort (field id, direction) for the pivot table sort by options.</p>"""
    column: NotRequired["capo_quicksight.types.column_sort.ColumnSort"]
    """<p>The column sort (field id, direction) for the pivot table sort by options.</p>"""
    data_path: NotRequired["capo_quicksight.types.data_path_sort.DataPathSort"]
    """<p>The data path sort (data path value, direction) for the pivot table sort by options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableSortBy) -> dict:
    out: dict = {}
    if "field" in value:
        import capo_quicksight.types.field_sort

        out["Field"] = capo_quicksight.types.field_sort.serialize_json(value["field"])
    if "column" in value:
        import capo_quicksight.types.column_sort

        out["Column"] = capo_quicksight.types.column_sort.serialize_json(
            value["column"]
        )
    if "data_path" in value:
        import capo_quicksight.types.data_path_sort

        out["DataPath"] = capo_quicksight.types.data_path_sort.serialize_json(
            value["data_path"]
        )
    return out


def deserialize_json(data: dict) -> PivotTableSortBy:
    out: PivotTableSortBy = {}  # type: ignore[typeddict-item]
    if data.get("Field") is not None:
        import capo_quicksight.types.field_sort

        out["field"] = capo_quicksight.types.field_sort.deserialize_json(data["Field"])
    if data.get("Column") is not None:
        import capo_quicksight.types.column_sort

        out["column"] = capo_quicksight.types.column_sort.deserialize_json(
            data["Column"]
        )
    if data.get("DataPath") is not None:
        import capo_quicksight.types.data_path_sort

        out["data_path"] = capo_quicksight.types.data_path_sort.deserialize_json(
            data["DataPath"]
        )
    return out


def redact_sensitive(value: PivotTableSortBy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_path" in value:
        import capo_quicksight.types.data_path_sort

        out["data_path"] = capo_quicksight.types.data_path_sort.redact_sensitive(
            value["data_path"]
        )
    return out
