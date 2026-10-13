"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerMapConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_map_layer_list
    import capo_quicksight.types.geospatial_map_state
    import capo_quicksight.types.geospatial_map_style
    import capo_quicksight.types.legend_options
    import capo_quicksight.types.visual_interaction_options


class GeospatialLayerMapConfiguration(TypedDict, closed=True):
    legend: NotRequired["capo_quicksight.types.legend_options.LegendOptions"]
    map_layers: NotRequired[
        "capo_quicksight.types.geospatial_map_layer_list.GeospatialMapLayerList"
    ]
    """<p>The geospatial layers to visualize on the map.</p>"""
    map_state: NotRequired[
        "capo_quicksight.types.geospatial_map_state.GeospatialMapState"
    ]
    """<p>The map state properties for the map.</p>"""
    map_style: NotRequired[
        "capo_quicksight.types.geospatial_map_style.GeospatialMapStyle"
    ]
    """<p>The map style properties for the map.</p>"""
    interactions: NotRequired[
        "capo_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerMapConfiguration) -> dict:
    out: dict = {}
    if "legend" in value:
        import capo_quicksight.types.legend_options

        out["Legend"] = capo_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "map_layers" in value:
        import capo_quicksight.types.geospatial_map_layer_list

        out["MapLayers"] = (
            capo_quicksight.types.geospatial_map_layer_list.serialize_json(
                value["map_layers"]
            )
        )
    if "map_state" in value:
        import capo_quicksight.types.geospatial_map_state

        out["MapState"] = capo_quicksight.types.geospatial_map_state.serialize_json(
            value["map_state"]
        )
    if "map_style" in value:
        import capo_quicksight.types.geospatial_map_style

        out["MapStyle"] = capo_quicksight.types.geospatial_map_style.serialize_json(
            value["map_style"]
        )
    if "interactions" in value:
        import capo_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            capo_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerMapConfiguration:
    out: GeospatialLayerMapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Legend") is not None:
        import capo_quicksight.types.legend_options

        out["legend"] = capo_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if data.get("MapLayers") is not None:
        import capo_quicksight.types.geospatial_map_layer_list

        out["map_layers"] = (
            capo_quicksight.types.geospatial_map_layer_list.deserialize_json(
                data["MapLayers"]
            )
        )
    if data.get("MapState") is not None:
        import capo_quicksight.types.geospatial_map_state

        out["map_state"] = capo_quicksight.types.geospatial_map_state.deserialize_json(
            data["MapState"]
        )
    if data.get("MapStyle") is not None:
        import capo_quicksight.types.geospatial_map_style

        out["map_style"] = capo_quicksight.types.geospatial_map_style.deserialize_json(
            data["MapStyle"]
        )
    if data.get("Interactions") is not None:
        import capo_quicksight.types.visual_interaction_options

        out["interactions"] = (
            capo_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out


def redact_sensitive(value: GeospatialLayerMapConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "map_layers" in value:
        import capo_quicksight.types.geospatial_map_layer_list

        out["map_layers"] = (
            capo_quicksight.types.geospatial_map_layer_list.redact_sensitive(
                value["map_layers"]
            )
        )
    return out
