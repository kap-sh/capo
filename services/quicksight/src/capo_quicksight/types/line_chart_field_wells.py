"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.line_chart_aggregated_field_wells


class LineChartFieldWells(TypedDict, closed=True):
    line_chart_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.line_chart_aggregated_field_wells.LineChartAggregatedFieldWells"
    ]
    """<p>The field well configuration of a line chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartFieldWells) -> dict:
    out: dict = {}
    if "line_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.line_chart_aggregated_field_wells

        out["LineChartAggregatedFieldWells"] = (
            capo_quicksight.types.line_chart_aggregated_field_wells.serialize_json(
                value["line_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineChartFieldWells:
    out: LineChartFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("LineChartAggregatedFieldWells") is not None:
        import capo_quicksight.types.line_chart_aggregated_field_wells

        out["line_chart_aggregated_field_wells"] = (
            capo_quicksight.types.line_chart_aggregated_field_wells.deserialize_json(
                data["LineChartAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: LineChartFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "line_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.line_chart_aggregated_field_wells

        out["line_chart_aggregated_field_wells"] = (
            capo_quicksight.types.line_chart_aggregated_field_wells.redact_sensitive(
                value["line_chart_aggregated_field_wells"]
            )
        )
    return out
