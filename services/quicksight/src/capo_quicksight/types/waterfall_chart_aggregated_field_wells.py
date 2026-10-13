"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list


class WaterfallChartAggregatedFieldWells(TypedDict, closed=True):
    categories: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category field wells of a waterfall visual.</p>"""
    values: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a waterfall visual.</p>"""
    breakdowns: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The breakdown field wells of a waterfall visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "categories" in value:
        import capo_quicksight.types.dimension_field_list

        out["Categories"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["categories"]
        )
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["Values"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    if "breakdowns" in value:
        import capo_quicksight.types.dimension_field_list

        out["Breakdowns"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["breakdowns"]
        )
    return out


def deserialize_json(data: dict) -> WaterfallChartAggregatedFieldWells:
    out: WaterfallChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Categories") is not None:
        import capo_quicksight.types.dimension_field_list

        out["categories"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Categories"]
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    if data.get("Breakdowns") is not None:
        import capo_quicksight.types.dimension_field_list

        out["breakdowns"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Breakdowns"]
        )
    return out


def redact_sensitive(value: WaterfallChartAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "categories" in value:
        import capo_quicksight.types.dimension_field_list

        out["categories"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["categories"]
        )
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.redact_sensitive(
            value["values"]
        )
    if "breakdowns" in value:
        import capo_quicksight.types.dimension_field_list

        out["breakdowns"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["breakdowns"]
        )
    return out
