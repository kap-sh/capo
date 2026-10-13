"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_measure_field_list
    import capo_quicksight.types.pivot_table_dimension_list


class PivotTableAggregatedFieldWells(TypedDict, closed=True):
    rows: NotRequired[
        "capo_quicksight.types.pivot_table_dimension_list.PivotTableDimensionList"
    ]
    """<p>The rows field well for a pivot table. Values are grouped by rows fields.</p>"""
    columns: NotRequired[
        "capo_quicksight.types.pivot_table_dimension_list.PivotTableDimensionList"
    ]
    """<p>The columns field well for a pivot table. Values are grouped by columns fields.</p>"""
    values: NotRequired[
        "capo_quicksight.types.pivot_measure_field_list.PivotMeasureFieldList"
    ]
    """<p>The values field well for a pivot table. Values are aggregated based on rows and columns fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableAggregatedFieldWells) -> dict:
    out: dict = {}
    if "rows" in value:
        import capo_quicksight.types.pivot_table_dimension_list

        out["Rows"] = capo_quicksight.types.pivot_table_dimension_list.serialize_json(
            value["rows"]
        )
    if "columns" in value:
        import capo_quicksight.types.pivot_table_dimension_list

        out["Columns"] = (
            capo_quicksight.types.pivot_table_dimension_list.serialize_json(
                value["columns"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.pivot_measure_field_list

        out["Values"] = capo_quicksight.types.pivot_measure_field_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> PivotTableAggregatedFieldWells:
    out: PivotTableAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Rows") is not None:
        import capo_quicksight.types.pivot_table_dimension_list

        out["rows"] = capo_quicksight.types.pivot_table_dimension_list.deserialize_json(
            data["Rows"]
        )
    if data.get("Columns") is not None:
        import capo_quicksight.types.pivot_table_dimension_list

        out["columns"] = (
            capo_quicksight.types.pivot_table_dimension_list.deserialize_json(
                data["Columns"]
            )
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.pivot_measure_field_list

        out["values"] = capo_quicksight.types.pivot_measure_field_list.deserialize_json(
            data["Values"]
        )
    return out


def redact_sensitive(value: PivotTableAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rows" in value:
        import capo_quicksight.types.pivot_table_dimension_list

        out["rows"] = capo_quicksight.types.pivot_table_dimension_list.redact_sensitive(
            value["rows"]
        )
    if "columns" in value:
        import capo_quicksight.types.pivot_table_dimension_list

        out["columns"] = (
            capo_quicksight.types.pivot_table_dimension_list.redact_sensitive(
                value["columns"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.pivot_measure_field_list

        out["values"] = capo_quicksight.types.pivot_measure_field_list.redact_sensitive(
            value["values"]
        )
    return out
