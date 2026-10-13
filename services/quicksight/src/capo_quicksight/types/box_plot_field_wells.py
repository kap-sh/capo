"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.box_plot_aggregated_field_wells


class BoxPlotFieldWells(TypedDict, closed=True):
    box_plot_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.box_plot_aggregated_field_wells.BoxPlotAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a box plot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotFieldWells) -> dict:
    out: dict = {}
    if "box_plot_aggregated_field_wells" in value:
        import capo_quicksight.types.box_plot_aggregated_field_wells

        out["BoxPlotAggregatedFieldWells"] = (
            capo_quicksight.types.box_plot_aggregated_field_wells.serialize_json(
                value["box_plot_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> BoxPlotFieldWells:
    out: BoxPlotFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("BoxPlotAggregatedFieldWells") is not None:
        import capo_quicksight.types.box_plot_aggregated_field_wells

        out["box_plot_aggregated_field_wells"] = (
            capo_quicksight.types.box_plot_aggregated_field_wells.deserialize_json(
                data["BoxPlotAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: BoxPlotFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "box_plot_aggregated_field_wells" in value:
        import capo_quicksight.types.box_plot_aggregated_field_wells

        out["box_plot_aggregated_field_wells"] = (
            capo_quicksight.types.box_plot_aggregated_field_wells.redact_sensitive(
                value["box_plot_aggregated_field_wells"]
            )
        )
    return out
