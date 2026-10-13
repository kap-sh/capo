"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.funnel_chart_aggregated_field_wells


class FunnelChartFieldWells(TypedDict, closed=True):
    funnel_chart_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.funnel_chart_aggregated_field_wells.FunnelChartAggregatedFieldWells"
    ]
    """<p>The field well configuration of a <code>FunnelChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartFieldWells) -> dict:
    out: dict = {}
    if "funnel_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.funnel_chart_aggregated_field_wells

        out["FunnelChartAggregatedFieldWells"] = (
            capo_quicksight.types.funnel_chart_aggregated_field_wells.serialize_json(
                value["funnel_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunnelChartFieldWells:
    out: FunnelChartFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("FunnelChartAggregatedFieldWells") is not None:
        import capo_quicksight.types.funnel_chart_aggregated_field_wells

        out["funnel_chart_aggregated_field_wells"] = (
            capo_quicksight.types.funnel_chart_aggregated_field_wells.deserialize_json(
                data["FunnelChartAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: FunnelChartFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "funnel_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.funnel_chart_aggregated_field_wells

        out["funnel_chart_aggregated_field_wells"] = (
            capo_quicksight.types.funnel_chart_aggregated_field_wells.redact_sensitive(
                value["funnel_chart_aggregated_field_wells"]
            )
        )
    return out
