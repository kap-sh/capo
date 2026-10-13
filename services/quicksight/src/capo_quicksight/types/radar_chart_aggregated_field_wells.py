"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.radar_chart_category_field_list
    import capo_quicksight.types.radar_chart_color_field_list
    import capo_quicksight.types.radar_chart_values_field_list


class RadarChartAggregatedFieldWells(TypedDict, closed=True):
    category: NotRequired[
        "capo_quicksight.types.radar_chart_category_field_list.RadarChartCategoryFieldList"
    ]
    """<p>The aggregated field well categories of a radar chart.</p>"""
    color: NotRequired[
        "capo_quicksight.types.radar_chart_color_field_list.RadarChartColorFieldList"
    ]
    """<p>The color that are assigned to the aggregated field wells of a radar chart.</p>"""
    values: NotRequired[
        "capo_quicksight.types.radar_chart_values_field_list.RadarChartValuesFieldList"
    ]
    """<p>The values that are assigned to the aggregated field wells of a radar chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_quicksight.types.radar_chart_category_field_list

        out["Category"] = (
            capo_quicksight.types.radar_chart_category_field_list.serialize_json(
                value["category"]
            )
        )
    if "color" in value:
        import capo_quicksight.types.radar_chart_color_field_list

        out["Color"] = (
            capo_quicksight.types.radar_chart_color_field_list.serialize_json(
                value["color"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.radar_chart_values_field_list

        out["Values"] = (
            capo_quicksight.types.radar_chart_values_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> RadarChartAggregatedFieldWells:
    out: RadarChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        import capo_quicksight.types.radar_chart_category_field_list

        out["category"] = (
            capo_quicksight.types.radar_chart_category_field_list.deserialize_json(
                data["Category"]
            )
        )
    if data.get("Color") is not None:
        import capo_quicksight.types.radar_chart_color_field_list

        out["color"] = (
            capo_quicksight.types.radar_chart_color_field_list.deserialize_json(
                data["Color"]
            )
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.radar_chart_values_field_list

        out["values"] = (
            capo_quicksight.types.radar_chart_values_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out


def redact_sensitive(value: RadarChartAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "category" in value:
        import capo_quicksight.types.radar_chart_category_field_list

        out["category"] = (
            capo_quicksight.types.radar_chart_category_field_list.redact_sensitive(
                value["category"]
            )
        )
    if "color" in value:
        import capo_quicksight.types.radar_chart_color_field_list

        out["color"] = (
            capo_quicksight.types.radar_chart_color_field_list.redact_sensitive(
                value["color"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.radar_chart_values_field_list

        out["values"] = (
            capo_quicksight.types.radar_chart_values_field_list.redact_sensitive(
                value["values"]
            )
        )
    return out
