"""Generated from Smithy shape ``com.amazonaws.location#MapConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.country_code3_or_empty
    import capo_location.types.custom_layer_list


class MapConfigurationUpdate(TypedDict, closed=True):
    political_view: NotRequired[
        "capo_location.types.country_code3_or_empty.CountryCode3OrEmpty"
    ]
    """<p>Specifies the political view for the style. Set to an empty string to not use a political view, or, for styles that support specific political views, you can choose a view, such as <code>IND</code> for the Indian view.</p> <note> <p>Not all map resources or styles support political view styles. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/map-concepts.html#political-views">Political views</a> for more information.</p> </note>"""
    custom_layers: NotRequired["capo_location.types.custom_layer_list.CustomLayerList"]
    """<p>Specifies the custom layers for the style. Leave unset to not enable any custom layer, or, for styles that support custom layers, you can enable layer(s), such as POI layer for the VectorEsriNavigation style. Default is <code>unset</code>.</p> <note> <p>Not all map resources or styles support custom layers. See Custom Layers for more information.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: MapConfigurationUpdate) -> dict:
    out: dict = {}
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "custom_layers" in value:
        import capo_location.types.custom_layer_list

        out["CustomLayers"] = capo_location.types.custom_layer_list.serialize_json(
            value["custom_layers"]
        )
    return out


def deserialize_json(data: dict) -> MapConfigurationUpdate:
    out: MapConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("PoliticalView") is not None:
        out["political_view"] = data["PoliticalView"]
    if data.get("CustomLayers") is not None:
        import capo_location.types.custom_layer_list

        out["custom_layers"] = capo_location.types.custom_layer_list.deserialize_json(
            data["CustomLayers"]
        )
    return out
