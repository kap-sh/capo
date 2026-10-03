"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#Properties``."""

from typing_extensions import NotRequired, TypedDict


class Properties(TypedDict, closed=True):
    eo_cloud_cover: NotRequired["float"]
    """<p>Estimate of cloud cover.</p>"""
    view_off_nadir: NotRequired["float"]
    """<p>The angle from the sensor between nadir (straight down) and the scene center. Measured in degrees (0-90).</p>"""
    view_sun_azimuth: NotRequired["float"]
    """<p>The sun azimuth angle. From the scene center point on the ground, this is the angle between truth north and the sun. Measured clockwise in degrees (0-360).</p>"""
    view_sun_elevation: NotRequired["float"]
    """<p>The sun elevation angle. The angle from the tangent of the scene center point to the sun. Measured from the horizon in degrees (-90-90). Negative values indicate the sun is below the horizon, e.g. sun elevation of -10° means the data was captured during <a href="https://www.timeanddate.com/astronomy/different-types-twilight.html">nautical twilight</a>.</p>"""
    platform: NotRequired["str"]
    """<p>Platform property. Platform refers to the unique name of the specific platform the instrument is attached to. For satellites it is the name of the satellite, eg. landsat-8 (Landsat-8), sentinel-2a.</p>"""
    landsat_cloud_cover_land: NotRequired["float"]
    """<p>Land cloud cover for Landsat Data Collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Properties) -> dict:
    out: dict = {}
    if "eo_cloud_cover" in value:
        out["EoCloudCover"] = (
            "NaN"
            if value["eo_cloud_cover"] != value["eo_cloud_cover"]
            else "Infinity"
            if value["eo_cloud_cover"] == float("inf")
            else "-Infinity"
            if value["eo_cloud_cover"] == float("-inf")
            else value["eo_cloud_cover"]
        )
    if "view_off_nadir" in value:
        out["ViewOffNadir"] = (
            "NaN"
            if value["view_off_nadir"] != value["view_off_nadir"]
            else "Infinity"
            if value["view_off_nadir"] == float("inf")
            else "-Infinity"
            if value["view_off_nadir"] == float("-inf")
            else value["view_off_nadir"]
        )
    if "view_sun_azimuth" in value:
        out["ViewSunAzimuth"] = (
            "NaN"
            if value["view_sun_azimuth"] != value["view_sun_azimuth"]
            else "Infinity"
            if value["view_sun_azimuth"] == float("inf")
            else "-Infinity"
            if value["view_sun_azimuth"] == float("-inf")
            else value["view_sun_azimuth"]
        )
    if "view_sun_elevation" in value:
        out["ViewSunElevation"] = (
            "NaN"
            if value["view_sun_elevation"] != value["view_sun_elevation"]
            else "Infinity"
            if value["view_sun_elevation"] == float("inf")
            else "-Infinity"
            if value["view_sun_elevation"] == float("-inf")
            else value["view_sun_elevation"]
        )
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "landsat_cloud_cover_land" in value:
        out["LandsatCloudCoverLand"] = (
            "NaN"
            if value["landsat_cloud_cover_land"] != value["landsat_cloud_cover_land"]
            else "Infinity"
            if value["landsat_cloud_cover_land"] == float("inf")
            else "-Infinity"
            if value["landsat_cloud_cover_land"] == float("-inf")
            else value["landsat_cloud_cover_land"]
        )
    return out


def deserialize_json(data: dict) -> Properties:
    out: Properties = {}  # type: ignore[typeddict-item]
    if data.get("EoCloudCover") is not None:
        out["eo_cloud_cover"] = float(data["EoCloudCover"])
    if data.get("ViewOffNadir") is not None:
        out["view_off_nadir"] = float(data["ViewOffNadir"])
    if data.get("ViewSunAzimuth") is not None:
        out["view_sun_azimuth"] = float(data["ViewSunAzimuth"])
    if data.get("ViewSunElevation") is not None:
        out["view_sun_elevation"] = float(data["ViewSunElevation"])
    if data.get("Platform") is not None:
        out["platform"] = data["Platform"]
    if data.get("LandsatCloudCoverLand") is not None:
        out["landsat_cloud_cover_land"] = float(data["LandsatCloudCoverLand"])
    return out
