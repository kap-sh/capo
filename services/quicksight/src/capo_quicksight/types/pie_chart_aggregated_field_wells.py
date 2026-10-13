"""Generated from Smithy shape ``com.amazonaws.quicksight#PieChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list
    import capo_quicksight.types.small_multiples_dimension_field_list


class PieChartAggregatedFieldWells(TypedDict, closed=True):
    category: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category (group/color) field wells of a pie chart.</p>"""
    values: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a pie chart. Values are aggregated based on categories.</p>"""
    small_multiples: NotRequired[
        "capo_quicksight.types.small_multiples_dimension_field_list.SmallMultiplesDimensionFieldList"
    ]
    """<p>The small multiples field well of a pie chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PieChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_quicksight.types.dimension_field_list

        out["Category"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["category"]
        )
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["Values"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    if "small_multiples" in value:
        import capo_quicksight.types.small_multiples_dimension_field_list

        out["SmallMultiples"] = (
            capo_quicksight.types.small_multiples_dimension_field_list.serialize_json(
                value["small_multiples"]
            )
        )
    return out


def deserialize_json(data: dict) -> PieChartAggregatedFieldWells:
    out: PieChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        import capo_quicksight.types.dimension_field_list

        out["category"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Category"]
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    if data.get("SmallMultiples") is not None:
        import capo_quicksight.types.small_multiples_dimension_field_list

        out["small_multiples"] = (
            capo_quicksight.types.small_multiples_dimension_field_list.deserialize_json(
                data["SmallMultiples"]
            )
        )
    return out


def redact_sensitive(value: PieChartAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "category" in value:
        import capo_quicksight.types.dimension_field_list

        out["category"] = capo_quicksight.types.dimension_field_list.redact_sensitive(
            value["category"]
        )
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.redact_sensitive(
            value["values"]
        )
    if "small_multiples" in value:
        import capo_quicksight.types.small_multiples_dimension_field_list

        out["small_multiples"] = (
            capo_quicksight.types.small_multiples_dimension_field_list.redact_sensitive(
                value["small_multiples"]
            )
        )
    return out
