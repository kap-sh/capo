"""Generated from Smithy shape ``com.amazonaws.geomaps#GetTileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_maps.types.api_key
    import capo_geo_maps.types.sensitive_string
    import capo_geo_maps.types.tile_additional_feature_list
    import capo_geo_maps.types.tileset


class GetTileRequest(TypedDict, closed=True):
    additional_features: NotRequired[
        "capo_geo_maps.types.tile_additional_feature_list.TileAdditionalFeatureList"
    ]
    """<p>A list of optional additional parameters such as map styles that can be requested for each result. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p>"""
    tileset: "capo_geo_maps.types.tileset.Tileset"
    """<p>Specifies the desired tile set. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>vector.basemap</code> value.</p> <p>Valid Values: <code>raster.satellite | vector.basemap | vector.traffic | raster.dem</code> </p>"""
    z: "capo_geo_maps.types.sensitive_string.SensitiveString"
    """<p>The zoom value for the map tile.</p>"""
    x: "capo_geo_maps.types.sensitive_string.SensitiveString"
    """<p>The X axis value for the map tile.</p>"""
    y: "capo_geo_maps.types.sensitive_string.SensitiveString"
    """<p>The Y axis value for the map tile.</p>"""
    key: NotRequired["capo_geo_maps.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTileRequest:
    out: GetTileRequest = {}  # type: ignore[typeddict-item]
    return out
