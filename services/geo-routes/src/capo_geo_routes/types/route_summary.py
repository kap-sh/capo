"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_toll_summary


class RouteSummary(TypedDict, closed=True):
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the route.</p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the route.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    tolls: NotRequired["capo_geo_routes.types.route_toll_summary.RouteTollSummary"]
    """<p>Toll summary for the complete route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSummary) -> dict:
    out: dict = {}
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "tolls" in value:
        import capo_geo_routes.types.route_toll_summary

        out["Tolls"] = capo_geo_routes.types.route_toll_summary.serialize_json(
            value["tolls"]
        )
    return out


def deserialize_json(data: dict) -> RouteSummary:
    out: RouteSummary = {}  # type: ignore[typeddict-item]
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("Tolls") is not None:
        import capo_geo_routes.types.route_toll_summary

        out["tolls"] = capo_geo_routes.types.route_toll_summary.deserialize_json(
            data["Tolls"]
        )
    return out


def redact_sensitive(value: RouteSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "tolls" in value:
        import capo_geo_routes.types.route_toll_summary

        out["tolls"] = capo_geo_routes.types.route_toll_summary.redact_sensitive(
            value["tolls"]
        )
    return out
