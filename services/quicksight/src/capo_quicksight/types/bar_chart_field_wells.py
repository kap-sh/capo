"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.bar_chart_aggregated_field_wells


class BarChartFieldWells(TypedDict, closed=True):
    bar_chart_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.bar_chart_aggregated_field_wells.BarChartAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a bar chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarChartFieldWells) -> dict:
    out: dict = {}
    if "bar_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.bar_chart_aggregated_field_wells

        out["BarChartAggregatedFieldWells"] = (
            capo_quicksight.types.bar_chart_aggregated_field_wells.serialize_json(
                value["bar_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> BarChartFieldWells:
    out: BarChartFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("BarChartAggregatedFieldWells") is not None:
        import capo_quicksight.types.bar_chart_aggregated_field_wells

        out["bar_chart_aggregated_field_wells"] = (
            capo_quicksight.types.bar_chart_aggregated_field_wells.deserialize_json(
                data["BarChartAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: BarChartFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bar_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.bar_chart_aggregated_field_wells

        out["bar_chart_aggregated_field_wells"] = (
            capo_quicksight.types.bar_chart_aggregated_field_wells.redact_sensitive(
                value["bar_chart_aggregated_field_wells"]
            )
        )
    return out
