"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerColorField``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_layer_dimension_field_list
    import capo_quicksight.types.geospatial_layer_measure_field_list


class GeospatialLayerColorField(TypedDict, closed=True):
    color_dimensions_fields: NotRequired[
        "capo_quicksight.types.geospatial_layer_dimension_field_list.GeospatialLayerDimensionFieldList"
    ]
    """<p>A list of color dimension fields.</p>"""
    color_values_fields: NotRequired[
        "capo_quicksight.types.geospatial_layer_measure_field_list.GeospatialLayerMeasureFieldList"
    ]
    """<p>A list of color measure fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerColorField) -> dict:
    out: dict = {}
    if "color_dimensions_fields" in value:
        import capo_quicksight.types.geospatial_layer_dimension_field_list

        out["ColorDimensionsFields"] = (
            capo_quicksight.types.geospatial_layer_dimension_field_list.serialize_json(
                value["color_dimensions_fields"]
            )
        )
    if "color_values_fields" in value:
        import capo_quicksight.types.geospatial_layer_measure_field_list

        out["ColorValuesFields"] = (
            capo_quicksight.types.geospatial_layer_measure_field_list.serialize_json(
                value["color_values_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerColorField:
    out: GeospatialLayerColorField = {}  # type: ignore[typeddict-item]
    if data.get("ColorDimensionsFields") is not None:
        import capo_quicksight.types.geospatial_layer_dimension_field_list

        out["color_dimensions_fields"] = (
            capo_quicksight.types.geospatial_layer_dimension_field_list.deserialize_json(
                data["ColorDimensionsFields"]
            )
        )
    if data.get("ColorValuesFields") is not None:
        import capo_quicksight.types.geospatial_layer_measure_field_list

        out["color_values_fields"] = (
            capo_quicksight.types.geospatial_layer_measure_field_list.deserialize_json(
                data["ColorValuesFields"]
            )
        )
    return out


def redact_sensitive(value: GeospatialLayerColorField) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "color_dimensions_fields" in value:
        import capo_quicksight.types.geospatial_layer_dimension_field_list

        out["color_dimensions_fields"] = (
            capo_quicksight.types.geospatial_layer_dimension_field_list.redact_sensitive(
                value["color_dimensions_fields"]
            )
        )
    if "color_values_fields" in value:
        import capo_quicksight.types.geospatial_layer_measure_field_list

        out["color_values_fields"] = (
            capo_quicksight.types.geospatial_layer_measure_field_list.redact_sensitive(
                value["color_values_fields"]
            )
        )
    return out
