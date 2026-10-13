"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.funnel_chart_dimension_field_list
    import capo_quicksight.types.funnel_chart_measure_field_list


class FunnelChartAggregatedFieldWells(TypedDict, closed=True):
    category: NotRequired[
        "capo_quicksight.types.funnel_chart_dimension_field_list.FunnelChartDimensionFieldList"
    ]
    """<p>The category field wells of a funnel chart. Values are grouped by category fields.</p>"""
    values: NotRequired[
        "capo_quicksight.types.funnel_chart_measure_field_list.FunnelChartMeasureFieldList"
    ]
    """<p>The value field wells of a funnel chart. Values are aggregated based on categories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_quicksight.types.funnel_chart_dimension_field_list

        out["Category"] = (
            capo_quicksight.types.funnel_chart_dimension_field_list.serialize_json(
                value["category"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.funnel_chart_measure_field_list

        out["Values"] = (
            capo_quicksight.types.funnel_chart_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunnelChartAggregatedFieldWells:
    out: FunnelChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        import capo_quicksight.types.funnel_chart_dimension_field_list

        out["category"] = (
            capo_quicksight.types.funnel_chart_dimension_field_list.deserialize_json(
                data["Category"]
            )
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.funnel_chart_measure_field_list

        out["values"] = (
            capo_quicksight.types.funnel_chart_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out


def redact_sensitive(value: FunnelChartAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "category" in value:
        import capo_quicksight.types.funnel_chart_dimension_field_list

        out["category"] = (
            capo_quicksight.types.funnel_chart_dimension_field_list.redact_sensitive(
                value["category"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.funnel_chart_measure_field_list

        out["values"] = (
            capo_quicksight.types.funnel_chart_measure_field_list.redact_sensitive(
                value["values"]
            )
        )
    return out
