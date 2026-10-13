"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboChartFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.combo_chart_aggregated_field_wells


class ComboChartFieldWells(TypedDict, closed=True):
    combo_chart_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.combo_chart_aggregated_field_wells.ComboChartAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a combo chart. Combo charts only have aggregated field wells. Columns in a combo chart are aggregated by category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboChartFieldWells) -> dict:
    out: dict = {}
    if "combo_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.combo_chart_aggregated_field_wells

        out["ComboChartAggregatedFieldWells"] = (
            capo_quicksight.types.combo_chart_aggregated_field_wells.serialize_json(
                value["combo_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComboChartFieldWells:
    out: ComboChartFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("ComboChartAggregatedFieldWells") is not None:
        import capo_quicksight.types.combo_chart_aggregated_field_wells

        out["combo_chart_aggregated_field_wells"] = (
            capo_quicksight.types.combo_chart_aggregated_field_wells.deserialize_json(
                data["ComboChartAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: ComboChartFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "combo_chart_aggregated_field_wells" in value:
        import capo_quicksight.types.combo_chart_aggregated_field_wells

        out["combo_chart_aggregated_field_wells"] = (
            capo_quicksight.types.combo_chart_aggregated_field_wells.redact_sensitive(
                value["combo_chart_aggregated_field_wells"]
            )
        )
    return out
