"""Generated from Smithy shape ``com.amazonaws.location#MapConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.country_code3
    import capo_location.types.custom_layer_list
    import capo_location.types.map_style


class MapConfiguration(TypedDict, closed=True):
    style: "capo_location.types.map_style.MapStyle"
    """<p>Specifies the map style selected from an available data provider.</p> <p>Valid <a href="https://docs.aws.amazon.com/location/previous/developerguide/esri.html">Esri map styles</a>:</p> <ul> <li> <p> <code>VectorEsriDarkGrayCanvas</code> – The Esri Dark Gray Canvas map style. A vector basemap with a dark gray, neutral background with minimal colors, labels, and features that's designed to draw attention to your thematic content. </p> </li> <li> <p> <code>RasterEsriImagery</code> – The Esri Imagery map style. A raster basemap that provides one meter or better satellite and aerial imagery in many parts of the world and lower resolution satellite imagery worldwide. </p> </li> <li> <p> <code>VectorEsriLightGrayCanvas</code> – The Esri Light Gray Canvas map style, which provides a detailed vector basemap with a light gray, neutral background style with minimal colors, labels, and features that's designed to draw attention to your thematic content. </p> </li> <li> <p> <code>VectorEsriTopographic</code> – The Esri Light map style, which provides a detailed vector basemap with a classic Esri map style.</p> </li> <li> <p> <code>VectorEsriStreets</code> – The Esri Street Map style, which provides a detailed vector basemap for the world symbolized with a classic Esri street map style. The vector tile layer is similar in content and style to the World Street Map raster map.</p> </li> <li> <p> <code>VectorEsriNavigation</code> – The Esri Navigation map style, which provides a detailed basemap for the world symbolized with a custom navigation map style that's designed for use during the day in mobile devices.</p> </li> </ul> <p>Valid <a href="https://docs.aws.amazon.com/location/previous/developerguide/HERE.html">HERE Technologies map styles</a>:</p> <ul> <li> <p> <code>VectorHereContrast</code> – The HERE Contrast (Berlin) map style is a high contrast detailed base map of the world that blends 3D and 2D rendering.</p> <note> <p>The <code>VectorHereContrast</code> style has been renamed from <code>VectorHereBerlin</code>. <code>VectorHereBerlin</code> has been deprecated, but will continue to work in applications that use it.</p> </note> </li> <li> <p> <code>VectorHereExplore</code> – A default HERE map style containing a neutral, global map and its features including roads, buildings, landmarks, and water features. It also now includes a fully designed map of Japan.</p> </li> <li> <p> <code>VectorHereExploreTruck</code> – A global map containing truck restrictions and attributes (e.g. width / height / HAZMAT) symbolized with highlighted segments and icons on top of HERE Explore to support use cases within transport and logistics.</p> </li> <li> <p> <code>RasterHereExploreSatellite</code> – A global map containing high resolution satellite imagery.</p> </li> <li> <p> <code>HybridHereExploreSatellite</code> – A global map displaying the road network, street names, and city labels over satellite imagery. This style will automatically retrieve both raster and vector tiles, and your charges will be based on total tiles retrieved.</p> <note> <p>Hybrid styles use both vector and raster tiles when rendering the map that you see. This means that more tiles are retrieved than when using either vector or raster tiles alone. Your charges will include all tiles retrieved.</p> </note> </li> </ul> <p>Valid <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps map styles</a>:</p> <ul> <li> <p> <code>VectorGrabStandardLight</code> – The Grab Standard Light map style provides a basemap with detailed land use coloring, area names, roads, landmarks, and points of interest covering Southeast Asia.</p> </li> <li> <p> <code>VectorGrabStandardDark</code> – The Grab Standard Dark map style provides a dark variation of the standard basemap covering Southeast Asia.</p> </li> </ul> <note> <p>Grab provides maps only for countries in Southeast Asia, and is only available in the Asia Pacific (Singapore) Region (<code>ap-southeast-1</code>). For more information, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area">GrabMaps countries and area covered</a>.</p> </note> <p>Valid <a href="https://docs.aws.amazon.com/location/previous/developerguide/open-data.html">Open Data map styles</a>:</p> <ul> <li> <p> <code>VectorOpenDataStandardLight</code> – The Open Data Standard Light map style provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.</p> </li> <li> <p> <code>VectorOpenDataStandardDark</code> – Open Data Standard Dark is a dark-themed map style that provides a detailed basemap for the world suitable for website and mobile application use. The map includes highways major roads, minor roads, railways, water features, cities, parks, landmarks, building footprints, and administrative boundaries.</p> </li> <li> <p> <code>VectorOpenDataVisualizationLight</code> – The Open Data Visualization Light map style is a light-themed style with muted colors and fewer features that aids in understanding overlaid data.</p> </li> <li> <p> <code>VectorOpenDataVisualizationDark</code> – The Open Data Visualization Dark map style is a dark-themed style with muted colors and fewer features that aids in understanding overlaid data.</p> </li> </ul>"""
    political_view: NotRequired["capo_location.types.country_code3.CountryCode3"]
    """<p>Specifies the political view for the style. Leave unset to not use a political view, or, for styles that support specific political views, you can choose a view, such as <code>IND</code> for the Indian view.</p> <p>Default is unset.</p> <note> <p>Not all map resources or styles support political view styles. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/map-concepts.html#political-views">Political views</a> for more information.</p> </note>"""
    custom_layers: NotRequired["capo_location.types.custom_layer_list.CustomLayerList"]
    """<p>Specifies the custom layers for the style. Leave unset to not enable any custom layer, or, for styles that support custom layers, you can enable layer(s), such as POI layer for the VectorEsriNavigation style. Default is <code>unset</code>.</p> <note> <p>Not all map resources or styles support custom layers. See Custom Layers for more information.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: MapConfiguration) -> dict:
    out: dict = {}
    out["Style"] = value["style"]
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "custom_layers" in value:
        import capo_location.types.custom_layer_list

        out["CustomLayers"] = capo_location.types.custom_layer_list.serialize_json(
            value["custom_layers"]
        )
    return out


def deserialize_json(data: dict) -> MapConfiguration:
    out: MapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Style") is not None:
        out["style"] = data["Style"]
    else:
        raise DeserializationError("MapConfiguration.style required")
    if data.get("PoliticalView") is not None:
        out["political_view"] = data["PoliticalView"]
    if data.get("CustomLayers") is not None:
        import capo_location.types.custom_layer_list

        out["custom_layers"] = capo_location.types.custom_layer_list.deserialize_json(
            data["CustomLayers"]
        )
    return out
