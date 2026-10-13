"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineGranularityOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters


class IsolineGranularityOptions(TypedDict, closed=True):
    max_points: NotRequired["int"]
    """<p>The maximum number of points used to define each isoline. Higher values create smoother, more detailed shapes.</p>"""
    max_resolution: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The maximum distance in meters between points along the isoline. Smaller values create more detailed shapes.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineGranularityOptions) -> dict:
    out: dict = {}
    if "max_points" in value:
        out["MaxPoints"] = value["max_points"]
    out["MaxResolution"] = value.get("max_resolution", 0)
    return out


def deserialize_json(data: dict) -> IsolineGranularityOptions:
    out: IsolineGranularityOptions = {}  # type: ignore[typeddict-item]
    if data.get("MaxPoints") is not None:
        out["max_points"] = data["MaxPoints"]
    if data.get("MaxResolution") is not None:
        out["max_resolution"] = data["MaxResolution"]
    else:
        out["max_resolution"] = 0
    return out


def redact_sensitive(value: IsolineGranularityOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "max_resolution" in value:
        out["max_resolution"] = "*** Sensitive Data Redacted ***"
    return out
