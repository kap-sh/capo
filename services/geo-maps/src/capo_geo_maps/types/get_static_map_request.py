"""Generated from Smithy shape ``com.amazonaws.geomaps#GetStaticMapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_maps.types.api_key
    import capo_geo_maps.types.color_scheme
    import capo_geo_maps.types.compact_overlay
    import capo_geo_maps.types.country_code
    import capo_geo_maps.types.distance_meters
    import capo_geo_maps.types.geo_json_overlay
    import capo_geo_maps.types.label_size
    import capo_geo_maps.types.language_tag
    import capo_geo_maps.types.map_feature_mode
    import capo_geo_maps.types.position_list_string
    import capo_geo_maps.types.position_string
    import capo_geo_maps.types.scale_bar_unit
    import capo_geo_maps.types.sensitive_float
    import capo_geo_maps.types.sensitive_integer
    import capo_geo_maps.types.static_map_style


class GetStaticMapRequest(TypedDict, closed=True):
    bounding_box: NotRequired[
        "capo_geo_maps.types.position_list_string.PositionListString"
    ]
    """<p>Takes in two pairs of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], denoting south-westerly and north-easterly edges of the image. The underlying area becomes the view of the image. </p> <p>Example: -123.17075,49.26959,-123.08125,49.31429</p>"""
    bounded_positions: NotRequired[
        "capo_geo_maps.types.position_list_string.PositionListString"
    ]
    """<p>Takes in two or more pair of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], with each coordinate separated by a comma. The API will generate an image to encompass all of the provided coordinates. </p> <note> <p>Cannot be used with <code>Zoom</code> and or <code>Radius</code> </p> </note> <p>Example: 97.170451,78.039098,99.045536,27.176178</p>"""
    center: NotRequired["capo_geo_maps.types.position_string.PositionString"]
    """<p>Takes in a pair of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], which becomes the center point of the image. This parameter requires that either zoom or radius is set.</p> <note> <p>Cannot be used with <code>Zoom</code> and or <code>Radius</code> </p> </note> <p>Example: 49.295,-123.108</p>"""
    color_scheme: NotRequired["capo_geo_maps.types.color_scheme.ColorScheme"]
    """<p>Sets the color tone for the map, such as dark and light.</p> <p>Example: <code>Light</code> </p> <p>Default value: <code>Light</code> </p> <note> <p>Valid values for <code>ColorScheme</code> are case sensitive.</p> </note>"""
    compact_overlay: NotRequired["capo_geo_maps.types.compact_overlay.CompactOverlay"]
    """<p>Takes in a string to draw geometries on the image. The input is a comma separated format as follows format: <code>[Lon, Lat]</code> </p> <p>Example: <code>line:-122.407653,37.798557,-122.413291,37.802443;color=%23DD0000;width=7;outline-color=#00DD00;outline-width=5yd|point:-122.40572,37.80004;label=Fog Hill Market;size=large;text-color=%23DD0000;color=#EE4B2B</code> </p> <note> <p>Currently it supports the following geometry types: point, line and polygon. It does not support multiPoint , multiLine and multiPolgyon.</p> </note>"""
    crop_labels: NotRequired["bool"]
    """<p>It is a flag that takes in true or false. It prevents the labels that are on the edge of the image from being cut or obscured.</p>"""
    geo_json_overlay: NotRequired["capo_geo_maps.types.geo_json_overlay.GeoJsonOverlay"]
    """<p>Takes in a string to draw geometries on the image. The input is a valid GeoJSON collection object. </p> <p>Example: <code>{"type":"FeatureCollection","features": [{"type":"Feature","geometry":{"type":"MultiPoint","coordinates": [[-90.076345,51.504107],[-0.074451,51.506892]]},"properties": {"color":"#00DD00"}}]}</code> </p>"""
    height: "capo_geo_maps.types.sensitive_integer.SensitiveInteger"
    """<p>Specifies the height of the map image.</p>"""
    key: NotRequired["capo_geo_maps.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>"""
    label_size: NotRequired["capo_geo_maps.types.label_size.LabelSize"]
    """<p>Overrides the label size auto-calculated by <code>FileName</code>. Takes in one of the values - <code>Small</code> or <code>Large</code>.</p>"""
    language: NotRequired["capo_geo_maps.types.language_tag.LanguageTag"]
    """<p>Specifies the language on the map labels using the BCP 47 language tag, limited to ISO 639-1 two-letter language codes. If the specified language data isn't available for the map image, the labels will default to the regional primary language.</p> <p>Supported codes:</p> <ul> <li> <p> <code>ar</code> </p> </li> <li> <p> <code>as</code> </p> </li> <li> <p> <code>az</code> </p> </li> <li> <p> <code>be</code> </p> </li> <li> <p> <code>bg</code> </p> </li> <li> <p> <code>bn</code> </p> </li> <li> <p> <code>bs</code> </p> </li> <li> <p> <code>ca</code> </p> </li> <li> <p> <code>cs</code> </p> </li> <li> <p> <code>cy</code> </p> </li> <li> <p> <code>da</code> </p> </li> <li> <p> <code>de</code> </p> </li> <li> <p> <code>el</code> </p> </li> <li> <p> <code>en</code> </p> </li> <li> <p> <code>es</code> </p> </li> <li> <p> <code>et</code> </p> </li> <li> <p> <code>eu</code> </p> </li> <li> <p> <code>fi</code> </p> </li> <li> <p> <code>fo</code> </p> </li> <li> <p> <code>fr</code> </p> </li> <li> <p> <code>ga</code> </p> </li> <li> <p> <code>gl</code> </p> </li> <li> <p> <code>gn</code> </p> </li> <li> <p> <code>gu</code> </p> </li> <li> <p> <code>he</code> </p> </li> <li> <p> <code>hi</code> </p> </li> <li> <p> <code>hr</code> </p> </li> <li> <p> <code>hu</code> </p> </li> <li> <p> <code>hy</code> </p> </li> <li> <p> <code>id</code> </p> </li> <li> <p> <code>is</code> </p> </li> <li> <p> <code>it</code> </p> </li> <li> <p> <code>ja</code> </p> </li> <li> <p> <code>ka</code> </p> </li> <li> <p> <code>kk</code> </p> </li> <li> <p> <code>km</code> </p> </li> <li> <p> <code>kn</code> </p> </li> <li> <p> <code>ko</code> </p> </li> <li> <p> <code>ky</code> </p> </li> <li> <p> <code>lt</code> </p> </li> <li> <p> <code>lv</code> </p> </li> <li> <p> <code>mk</code> </p> </li> <li> <p> <code>ml</code> </p> </li> <li> <p> <code>mr</code> </p> </li> <li> <p> <code>ms</code> </p> </li> <li> <p> <code>mt</code> </p> </li> <li> <p> <code>my</code> </p> </li> <li> <p> <code>nl</code> </p> </li> <li> <p> <code>no</code> </p> </li> <li> <p> <code>or</code> </p> </li> <li> <p> <code>pa</code> </p> </li> <li> <p> <code>pl</code> </p> </li> <li> <p> <code>pt</code> </p> </li> <li> <p> <code>ro</code> </p> </li> <li> <p> <code>ru</code> </p> </li> <li> <p> <code>sk</code> </p> </li> <li> <p> <code>sl</code> </p> </li> <li> <p> <code>sq</code> </p> </li> <li> <p> <code>sr</code> </p> </li> <li> <p> <code>sv</code> </p> </li> <li> <p> <code>ta</code> </p> </li> <li> <p> <code>te</code> </p> </li> <li> <p> <code>th</code> </p> </li> <li> <p> <code>tr</code> </p> </li> <li> <p> <code>uk</code> </p> </li> <li> <p> <code>uz</code> </p> </li> <li> <p> <code>vi</code> </p> </li> <li> <p> <code>zh</code> </p> </li> </ul>"""
    padding: NotRequired["capo_geo_maps.types.sensitive_integer.SensitiveInteger"]
    """<p>Applies additional space (in pixels) around overlay feature to prevent them from being cut or obscured.</p> <note> <p>Value for max and min is determined by:</p> <p>Min: <code>1</code> </p> <p>Max: <code>min(height, width)/4</code> </p> </note> <p>Example: <code>100</code> </p>"""
    political_view: NotRequired["capo_geo_maps.types.country_code.CountryCode"]
    """<p>Specifies the political view, using ISO 3166-2 or ISO 3166-3 country code format.</p> <p>The following political views are currently supported:</p> <ul> <li> <p> <code>ARG</code>: Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands</p> </li> <li> <p> <code>EGY</code>: Egypt's view on Bir Tawil</p> </li> <li> <p> <code>IND</code>: India's view on Gilgit-Baltistan</p> </li> <li> <p> <code>KEN</code>: Kenya's view on the Ilemi Triangle</p> </li> <li> <p> <code>MAR</code>: Morocco's view on Western Sahara</p> </li> <li> <p> <code>RUS</code>: Russia's view on Crimea</p> </li> <li> <p> <code>SDN</code>: Sudan's view on the Halaib Triangle</p> </li> <li> <p> <code>SRB</code>: Serbia's view on Kosovo, Vukovar, and Sarengrad Islands</p> </li> <li> <p> <code>SUR</code>: Suriname's view on the Courantyne Headwaters and Lawa Headwaters</p> </li> <li> <p> <code>SYR</code>: Syria's view on the Golan Heights</p> </li> <li> <p> <code>TUR</code>: Turkey's view on Cyprus and Northern Cyprus</p> </li> <li> <p> <code>TZA</code>: Tanzania's view on Lake Malawi</p> </li> <li> <p> <code>URY</code>: Uruguay's view on Rincon de Artigas</p> </li> <li> <p> <code>VNM</code>: Vietnam's view on the Paracel Islands and Spratly Islands</p> </li> </ul>"""
    points_of_interests: NotRequired[
        "capo_geo_maps.types.map_feature_mode.MapFeatureMode"
    ]
    """<p>Determines if the result image will display icons representing points of interest on the map.</p>"""
    radius: NotRequired["capo_geo_maps.types.distance_meters.DistanceMeters"]
    """<p>Used with center parameter, it specifies the zoom of the image where you can control it on a granular level. Takes in any value <code>&gt;= 1</code>. </p> <p>Example: <code>1500</code> </p> <note> <p>Cannot be used with <code>Zoom</code>.</p> </note> <p> <b>Unit</b>: <code>Meters</code> </p> <p/>"""
    file_name: "str"
    """<p>The map scaling parameter to size the image, icons, and labels. It follows the pattern of <code>^map(@2x)?$</code>.</p> <p>Example: <code>map, map@2x</code> </p>"""
    scale_bar_unit: NotRequired["capo_geo_maps.types.scale_bar_unit.ScaleBarUnit"]
    """<p>Displays a scale on the bottom right of the map image with the unit specified in the input. </p> <p>Example: <code>KilometersMiles, Miles, Kilometers, MilesKilometers</code> </p>"""
    style: NotRequired["capo_geo_maps.types.static_map_style.StaticMapStyle"]
    """<p> <code>Style</code> specifies the desired map style.</p>"""
    width: "capo_geo_maps.types.sensitive_integer.SensitiveInteger"
    """<p>Specifies the width of the map image.</p>"""
    zoom: NotRequired["capo_geo_maps.types.sensitive_float.SensitiveFloat"]
    """<p>Specifies the zoom level of the map image.</p> <note> <p>Cannot be used with <code>Radius</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStaticMapRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStaticMapRequest:
    out: GetStaticMapRequest = {}  # type: ignore[typeddict-item]
    return out
