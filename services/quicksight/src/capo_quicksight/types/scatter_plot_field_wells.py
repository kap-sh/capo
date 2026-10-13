"""Generated from Smithy shape ``com.amazonaws.quicksight#ScatterPlotFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.scatter_plot_categorically_aggregated_field_wells
    import capo_quicksight.types.scatter_plot_unaggregated_field_wells


class ScatterPlotFieldWells(TypedDict, closed=True):
    scatter_plot_categorically_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.scatter_plot_categorically_aggregated_field_wells.ScatterPlotCategoricallyAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a scatter plot. The x and y-axes of scatter plots with aggregated field wells are aggregated by category, label, or both.</p>"""
    scatter_plot_unaggregated_field_wells: NotRequired[
        "capo_quicksight.types.scatter_plot_unaggregated_field_wells.ScatterPlotUnaggregatedFieldWells"
    ]
    """<p>The unaggregated field wells of a scatter plot. The x and y-axes of these scatter plots are unaggregated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScatterPlotFieldWells) -> dict:
    out: dict = {}
    if "scatter_plot_categorically_aggregated_field_wells" in value:
        import capo_quicksight.types.scatter_plot_categorically_aggregated_field_wells

        out["ScatterPlotCategoricallyAggregatedFieldWells"] = (
            capo_quicksight.types.scatter_plot_categorically_aggregated_field_wells.serialize_json(
                value["scatter_plot_categorically_aggregated_field_wells"]
            )
        )
    if "scatter_plot_unaggregated_field_wells" in value:
        import capo_quicksight.types.scatter_plot_unaggregated_field_wells

        out["ScatterPlotUnaggregatedFieldWells"] = (
            capo_quicksight.types.scatter_plot_unaggregated_field_wells.serialize_json(
                value["scatter_plot_unaggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScatterPlotFieldWells:
    out: ScatterPlotFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("ScatterPlotCategoricallyAggregatedFieldWells") is not None:
        import capo_quicksight.types.scatter_plot_categorically_aggregated_field_wells

        out["scatter_plot_categorically_aggregated_field_wells"] = (
            capo_quicksight.types.scatter_plot_categorically_aggregated_field_wells.deserialize_json(
                data["ScatterPlotCategoricallyAggregatedFieldWells"]
            )
        )
    if data.get("ScatterPlotUnaggregatedFieldWells") is not None:
        import capo_quicksight.types.scatter_plot_unaggregated_field_wells

        out["scatter_plot_unaggregated_field_wells"] = (
            capo_quicksight.types.scatter_plot_unaggregated_field_wells.deserialize_json(
                data["ScatterPlotUnaggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: ScatterPlotFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "scatter_plot_categorically_aggregated_field_wells" in value:
        import capo_quicksight.types.scatter_plot_categorically_aggregated_field_wells

        out["scatter_plot_categorically_aggregated_field_wells"] = (
            capo_quicksight.types.scatter_plot_categorically_aggregated_field_wells.redact_sensitive(
                value["scatter_plot_categorically_aggregated_field_wells"]
            )
        )
    if "scatter_plot_unaggregated_field_wells" in value:
        import capo_quicksight.types.scatter_plot_unaggregated_field_wells

        out["scatter_plot_unaggregated_field_wells"] = (
            capo_quicksight.types.scatter_plot_unaggregated_field_wells.redact_sensitive(
                value["scatter_plot_unaggregated_field_wells"]
            )
        )
    return out
