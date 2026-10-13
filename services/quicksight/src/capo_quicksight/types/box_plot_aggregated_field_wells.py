"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.box_plot_dimension_field_list
    import capo_quicksight.types.box_plot_measure_field_list


class BoxPlotAggregatedFieldWells(TypedDict, closed=True):
    group_by: NotRequired[
        "capo_quicksight.types.box_plot_dimension_field_list.BoxPlotDimensionFieldList"
    ]
    """<p>The group by field well of a box plot chart. Values are grouped based on group by fields.</p>"""
    values: NotRequired[
        "capo_quicksight.types.box_plot_measure_field_list.BoxPlotMeasureFieldList"
    ]
    """<p>The value field well of a box plot chart. Values are aggregated based on group by fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotAggregatedFieldWells) -> dict:
    out: dict = {}
    if "group_by" in value:
        import capo_quicksight.types.box_plot_dimension_field_list

        out["GroupBy"] = (
            capo_quicksight.types.box_plot_dimension_field_list.serialize_json(
                value["group_by"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.box_plot_measure_field_list

        out["Values"] = (
            capo_quicksight.types.box_plot_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> BoxPlotAggregatedFieldWells:
    out: BoxPlotAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("GroupBy") is not None:
        import capo_quicksight.types.box_plot_dimension_field_list

        out["group_by"] = (
            capo_quicksight.types.box_plot_dimension_field_list.deserialize_json(
                data["GroupBy"]
            )
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.box_plot_measure_field_list

        out["values"] = (
            capo_quicksight.types.box_plot_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out


def redact_sensitive(value: BoxPlotAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "group_by" in value:
        import capo_quicksight.types.box_plot_dimension_field_list

        out["group_by"] = (
            capo_quicksight.types.box_plot_dimension_field_list.redact_sensitive(
                value["group_by"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.box_plot_measure_field_list

        out["values"] = (
            capo_quicksight.types.box_plot_measure_field_list.redact_sensitive(
                value["values"]
            )
        )
    return out
