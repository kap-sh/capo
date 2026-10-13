"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_data_source_item
    import capo_quicksight.types.geospatial_layer_definition
    import capo_quicksight.types.geospatial_layer_join_definition
    import capo_quicksight.types.geospatial_layer_type
    import capo_quicksight.types.layer_custom_action_list
    import capo_quicksight.types.string
    import capo_quicksight.types.tooltip_options
    import capo_quicksight.types.visibility


class GeospatialLayerItem(TypedDict, closed=True):
    layer_id: "capo_quicksight.types.string.String"
    """<p>The ID of the layer.</p>"""
    layer_type: NotRequired[
        "capo_quicksight.types.geospatial_layer_type.GeospatialLayerType"
    ]
    """<p>The layer type.</p>"""
    data_source: NotRequired[
        "capo_quicksight.types.geospatial_data_source_item.GeospatialDataSourceItem"
    ]
    """<p>The data source for the layer.</p>"""
    label: NotRequired["capo_quicksight.types.string.String"]
    """<p>The label that is displayed for the layer.</p>"""
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The state of visibility for the layer.</p>"""
    layer_definition: NotRequired[
        "capo_quicksight.types.geospatial_layer_definition.GeospatialLayerDefinition"
    ]
    """<p>The definition properties for a layer.</p>"""
    tooltip: NotRequired["capo_quicksight.types.tooltip_options.TooltipOptions"]
    join_definition: NotRequired[
        "capo_quicksight.types.geospatial_layer_join_definition.GeospatialLayerJoinDefinition"
    ]
    """<p>The join definition properties for a layer.</p>"""
    actions: NotRequired[
        "capo_quicksight.types.layer_custom_action_list.LayerCustomActionList"
    ]
    """<p>A list of custom actions for a layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerItem) -> dict:
    out: dict = {}
    out["LayerId"] = value["layer_id"]
    if "layer_type" in value:
        import capo_quicksight.types.geospatial_layer_type

        out["LayerType"] = capo_quicksight.types.geospatial_layer_type.serialize_json(
            value["layer_type"]
        )
    if "data_source" in value:
        import capo_quicksight.types.geospatial_data_source_item

        out["DataSource"] = (
            capo_quicksight.types.geospatial_data_source_item.serialize_json(
                value["data_source"]
            )
        )
    if "label" in value:
        out["Label"] = value["label"]
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "layer_definition" in value:
        import capo_quicksight.types.geospatial_layer_definition

        out["LayerDefinition"] = (
            capo_quicksight.types.geospatial_layer_definition.serialize_json(
                value["layer_definition"]
            )
        )
    if "tooltip" in value:
        import capo_quicksight.types.tooltip_options

        out["Tooltip"] = capo_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "join_definition" in value:
        import capo_quicksight.types.geospatial_layer_join_definition

        out["JoinDefinition"] = (
            capo_quicksight.types.geospatial_layer_join_definition.serialize_json(
                value["join_definition"]
            )
        )
    if "actions" in value:
        import capo_quicksight.types.layer_custom_action_list

        out["Actions"] = capo_quicksight.types.layer_custom_action_list.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerItem:
    out: GeospatialLayerItem = {}  # type: ignore[typeddict-item]
    if data.get("LayerId") is not None:
        out["layer_id"] = data["LayerId"]
    else:
        raise DeserializationError("GeospatialLayerItem.layer_id required")
    if data.get("LayerType") is not None:
        import capo_quicksight.types.geospatial_layer_type

        out["layer_type"] = (
            capo_quicksight.types.geospatial_layer_type.deserialize_json(
                data["LayerType"]
            )
        )
    if data.get("DataSource") is not None:
        import capo_quicksight.types.geospatial_data_source_item

        out["data_source"] = (
            capo_quicksight.types.geospatial_data_source_item.deserialize_json(
                data["DataSource"]
            )
        )
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if data.get("LayerDefinition") is not None:
        import capo_quicksight.types.geospatial_layer_definition

        out["layer_definition"] = (
            capo_quicksight.types.geospatial_layer_definition.deserialize_json(
                data["LayerDefinition"]
            )
        )
    if data.get("Tooltip") is not None:
        import capo_quicksight.types.tooltip_options

        out["tooltip"] = capo_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if data.get("JoinDefinition") is not None:
        import capo_quicksight.types.geospatial_layer_join_definition

        out["join_definition"] = (
            capo_quicksight.types.geospatial_layer_join_definition.deserialize_json(
                data["JoinDefinition"]
            )
        )
    if data.get("Actions") is not None:
        import capo_quicksight.types.layer_custom_action_list

        out["actions"] = (
            capo_quicksight.types.layer_custom_action_list.deserialize_json(
                data["Actions"]
            )
        )
    return out


def redact_sensitive(value: GeospatialLayerItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "join_definition" in value:
        import capo_quicksight.types.geospatial_layer_join_definition

        out["join_definition"] = (
            capo_quicksight.types.geospatial_layer_join_definition.redact_sensitive(
                value["join_definition"]
            )
        )
    if "actions" in value:
        import capo_quicksight.types.layer_custom_action_list

        out["actions"] = (
            capo_quicksight.types.layer_custom_action_list.redact_sensitive(
                value["actions"]
            )
        )
    return out
