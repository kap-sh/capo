"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerJoinDefinition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_layer_color_field
    import capo_quicksight.types.string
    import capo_quicksight.types.unaggregated_field


class GeospatialLayerJoinDefinition(TypedDict, closed=True):
    shape_key_field: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of the field or property in the geospatial data source.</p>"""
    dataset_key_field: NotRequired[
        "capo_quicksight.types.unaggregated_field.UnaggregatedField"
    ]
    color_field: NotRequired[
        "capo_quicksight.types.geospatial_layer_color_field.GeospatialLayerColorField"
    ]
    """<p>The geospatial color field for the join definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerJoinDefinition) -> dict:
    out: dict = {}
    if "shape_key_field" in value:
        out["ShapeKeyField"] = value["shape_key_field"]
    if "dataset_key_field" in value:
        import capo_quicksight.types.unaggregated_field

        out["DatasetKeyField"] = (
            capo_quicksight.types.unaggregated_field.serialize_json(
                value["dataset_key_field"]
            )
        )
    if "color_field" in value:
        import capo_quicksight.types.geospatial_layer_color_field

        out["ColorField"] = (
            capo_quicksight.types.geospatial_layer_color_field.serialize_json(
                value["color_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerJoinDefinition:
    out: GeospatialLayerJoinDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ShapeKeyField") is not None:
        out["shape_key_field"] = data["ShapeKeyField"]
    if data.get("DatasetKeyField") is not None:
        import capo_quicksight.types.unaggregated_field

        out["dataset_key_field"] = (
            capo_quicksight.types.unaggregated_field.deserialize_json(
                data["DatasetKeyField"]
            )
        )
    if data.get("ColorField") is not None:
        import capo_quicksight.types.geospatial_layer_color_field

        out["color_field"] = (
            capo_quicksight.types.geospatial_layer_color_field.deserialize_json(
                data["ColorField"]
            )
        )
    return out


def redact_sensitive(value: GeospatialLayerJoinDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dataset_key_field" in value:
        import capo_quicksight.types.unaggregated_field

        out["dataset_key_field"] = (
            capo_quicksight.types.unaggregated_field.redact_sensitive(
                value["dataset_key_field"]
            )
        )
    if "color_field" in value:
        import capo_quicksight.types.geospatial_layer_color_field

        out["color_field"] = (
            capo_quicksight.types.geospatial_layer_color_field.redact_sensitive(
                value["color_field"]
            )
        )
    return out
