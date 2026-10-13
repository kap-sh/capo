"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixMatchingOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.matching_strategy
    import capo_geo_routes.types.sensitive_string


class RouteMatrixMatchingOptions(TypedDict, closed=True):
    name_hint: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Attempts to match the provided position to a road similar to the provided name.</p>"""
    on_road_threshold: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>If the distance to a highway/bridge/tunnel/sliproad is within threshold, the waypoint will be snapped to the highway/bridge/tunnel/sliproad.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    radius: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Considers all roads within the provided radius to match the provided destination to. The roads that are considered are determined by the provided Strategy.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    strategy: NotRequired["capo_geo_routes.types.matching_strategy.MatchingStrategy"]
    """<p>Strategy that defines matching of the position onto the road network. MatchAny considers all roads possible, whereas MatchMostSignificantRoad matches to the most significant road.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixMatchingOptions) -> dict:
    out: dict = {}
    if "name_hint" in value:
        out["NameHint"] = value["name_hint"]
    out["OnRoadThreshold"] = value.get("on_road_threshold", 0)
    out["Radius"] = value.get("radius", 0)
    if "strategy" in value:
        import capo_geo_routes.types.matching_strategy

        out["Strategy"] = capo_geo_routes.types.matching_strategy.serialize_json(
            value["strategy"]
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixMatchingOptions:
    out: RouteMatrixMatchingOptions = {}  # type: ignore[typeddict-item]
    if data.get("NameHint") is not None:
        out["name_hint"] = data["NameHint"]
    if data.get("OnRoadThreshold") is not None:
        out["on_road_threshold"] = data["OnRoadThreshold"]
    else:
        out["on_road_threshold"] = 0
    if data.get("Radius") is not None:
        out["radius"] = data["Radius"]
    else:
        out["radius"] = 0
    if data.get("Strategy") is not None:
        import capo_geo_routes.types.matching_strategy

        out["strategy"] = capo_geo_routes.types.matching_strategy.deserialize_json(
            data["Strategy"]
        )
    return out


def redact_sensitive(value: RouteMatrixMatchingOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name_hint" in value:
        out["name_hint"] = "*** Sensitive Data Redacted ***"
    if "on_road_threshold" in value:
        out["on_road_threshold"] = "*** Sensitive Data Redacted ***"
    if "radius" in value:
        out["radius"] = "*** Sensitive Data Redacted ***"
    return out
