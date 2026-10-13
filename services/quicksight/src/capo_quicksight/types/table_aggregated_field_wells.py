"""Generated from Smithy shape ``com.amazonaws.quicksight#TableAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list


class TableAggregatedFieldWells(TypedDict, closed=True):
    group_by: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The group by field well for a pivot table. Values are grouped by group by fields.</p>"""
    values: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The values field well for a pivot table. Values are aggregated based on group by fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableAggregatedFieldWells) -> dict:
    out: dict = {}
    if "group_by" in value:
        import capo_quicksight.types.dimension_field_list

        out["GroupBy"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["group_by"]
        )
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["Values"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> TableAggregatedFieldWells:
    out: TableAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("GroupBy") is not None:
        import capo_quicksight.types.dimension_field_list

        out["group_by"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["GroupBy"]
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    return out


def redact_sensitive(value: TableAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "group_by" in value:
        import capo_quicksight.types.dimension_field_list

        out["group_by"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["group_by"]
        )
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.redact_sensitive(
            value["values"]
        )
    return out
