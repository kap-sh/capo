"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapAggregatedFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.filled_map_dimension_field_list
    import capo_quicksight.types.filled_map_measure_field_list


class FilledMapAggregatedFieldWells(TypedDict, closed=True):
    geospatial: NotRequired[
        "capo_quicksight.types.filled_map_dimension_field_list.FilledMapDimensionFieldList"
    ]
    """<p>The aggregated location field well of the filled map. Values are grouped by location fields.</p>"""
    values: NotRequired[
        "capo_quicksight.types.filled_map_measure_field_list.FilledMapMeasureFieldList"
    ]
    """<p>The aggregated color field well of a filled map. Values are aggregated based on location fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapAggregatedFieldWells) -> dict:
    out: dict = {}
    if "geospatial" in value:
        import capo_quicksight.types.filled_map_dimension_field_list

        out["Geospatial"] = (
            capo_quicksight.types.filled_map_dimension_field_list.serialize_json(
                value["geospatial"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.filled_map_measure_field_list

        out["Values"] = (
            capo_quicksight.types.filled_map_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilledMapAggregatedFieldWells:
    out: FilledMapAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("Geospatial") is not None:
        import capo_quicksight.types.filled_map_dimension_field_list

        out["geospatial"] = (
            capo_quicksight.types.filled_map_dimension_field_list.deserialize_json(
                data["Geospatial"]
            )
        )
    if data.get("Values") is not None:
        import capo_quicksight.types.filled_map_measure_field_list

        out["values"] = (
            capo_quicksight.types.filled_map_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out


def redact_sensitive(value: FilledMapAggregatedFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "geospatial" in value:
        import capo_quicksight.types.filled_map_dimension_field_list

        out["geospatial"] = (
            capo_quicksight.types.filled_map_dimension_field_list.redact_sensitive(
                value["geospatial"]
            )
        )
    if "values" in value:
        import capo_quicksight.types.filled_map_measure_field_list

        out["values"] = (
            capo_quicksight.types.filled_map_measure_field_list.redact_sensitive(
                value["values"]
            )
        )
    return out
