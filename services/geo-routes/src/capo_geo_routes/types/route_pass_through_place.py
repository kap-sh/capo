"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePassThroughPlace``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.position23
    import capo_geo_routes.types.sensitive_integer


class RoutePassThroughPlace(TypedDict, closed=True):
    original_position: NotRequired["capo_geo_routes.types.position23.Position23"]
    """<p>Position provided in the request.</p>"""
    position: "capo_geo_routes.types.position23.Position23"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    waypoint_index: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Index of the waypoint in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePassThroughPlace) -> dict:
    out: dict = {}
    if "original_position" in value:
        import capo_geo_routes.types.position23

        out["OriginalPosition"] = capo_geo_routes.types.position23.serialize_json(
            value["original_position"]
        )
    import capo_geo_routes.types.position23

    out["Position"] = capo_geo_routes.types.position23.serialize_json(value["position"])
    if "waypoint_index" in value:
        out["WaypointIndex"] = value["waypoint_index"]
    return out


def deserialize_json(data: dict) -> RoutePassThroughPlace:
    out: RoutePassThroughPlace = {}  # type: ignore[typeddict-item]
    if data.get("OriginalPosition") is not None:
        import capo_geo_routes.types.position23

        out["original_position"] = capo_geo_routes.types.position23.deserialize_json(
            data["OriginalPosition"]
        )
    if data.get("Position") is not None:
        import capo_geo_routes.types.position23

        out["position"] = capo_geo_routes.types.position23.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RoutePassThroughPlace.position required")
    if data.get("WaypointIndex") is not None:
        out["waypoint_index"] = data["WaypointIndex"]
    return out


def redact_sensitive(value: RoutePassThroughPlace) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "original_position" in value:
        out["original_position"] = "*** Sensitive Data Redacted ***"
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    if "waypoint_index" in value:
        out["waypoint_index"] = "*** Sensitive Data Redacted ***"
    return out
