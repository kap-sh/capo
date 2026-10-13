"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.radar_chart_aggregated_field_wells


class RadarChartFieldWells(TypedDict, closed=True):
    radar_chart_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.radar_chart_aggregated_field_wells.RadarChartAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a radar chart visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartFieldWells) -> dict:
    out: dict = {}
    if "radar_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.radar_chart_aggregated_field_wells

        out["RadarChartAggregatedFieldWells"] = (
            capo_quicksight.types.radar_chart_aggregated_field_wells.serialize_json(
                value["radar_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> RadarChartFieldWells:
    out: RadarChartFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("RadarChartAggregatedFieldWells") is not None:
        import capo_quicksight.types.radar_chart_aggregated_field_wells

        out["radar_chart_aggregated_field_wells"] = (
            capo_quicksight.types.radar_chart_aggregated_field_wells.deserialize_json(
                data["RadarChartAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: RadarChartFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "radar_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.radar_chart_aggregated_field_wells

        out["radar_chart_aggregated_field_wells"] = (
            capo_quicksight.types.radar_chart_aggregated_field_wells.redact_sensitive(
                value["radar_chart_aggregated_field_wells"]
            )
        )
    return out
