"""Generated from Smithy shape ``com.amazonaws.quicksight#PieChartFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pie_chart_aggregated_field_wells


class PieChartFieldWells(TypedDict, closed=True):
    pie_chart_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.pie_chart_aggregated_field_wells.PieChartAggregatedFieldWells"
    ]
    """<p>The field well configuration of a pie chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PieChartFieldWells) -> dict:
    out: dict = {}
    if "pie_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.pie_chart_aggregated_field_wells

        out["PieChartAggregatedFieldWells"] = (
            capo_quicksight.types.pie_chart_aggregated_field_wells.serialize_json(
                value["pie_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> PieChartFieldWells:
    out: PieChartFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("PieChartAggregatedFieldWells") is not None:
        import capo_quicksight.types.pie_chart_aggregated_field_wells

        out["pie_chart_aggregated_field_wells"] = (
            capo_quicksight.types.pie_chart_aggregated_field_wells.deserialize_json(
                data["PieChartAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: PieChartFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pie_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.pie_chart_aggregated_field_wells

        out["pie_chart_aggregated_field_wells"] = (
            capo_quicksight.types.pie_chart_aggregated_field_wells.redact_sensitive(
                value["pie_chart_aggregated_field_wells"]
            )
        )
    return out
