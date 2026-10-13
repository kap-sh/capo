"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixEntry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_matrix_error_code


class RouteMatrixEntry(TypedDict, closed=True):
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The total distance of travel for the route.</p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>The expected duration of travel for the route.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    error: NotRequired[
        "capo_geo_routes.types.route_matrix_error_code.RouteMatrixErrorCode"
    ]
    """<p>Error code that occurred during calculation of the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixEntry) -> dict:
    out: dict = {}
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "error" in value:
        import capo_geo_routes.types.route_matrix_error_code

        out["Error"] = capo_geo_routes.types.route_matrix_error_code.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixEntry:
    out: RouteMatrixEntry = {}  # type: ignore[typeddict-item]
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("Error") is not None:
        import capo_geo_routes.types.route_matrix_error_code

        out["error"] = capo_geo_routes.types.route_matrix_error_code.deserialize_json(
            data["Error"]
        )
    return out


def redact_sensitive(value: RouteMatrixEntry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    return out
