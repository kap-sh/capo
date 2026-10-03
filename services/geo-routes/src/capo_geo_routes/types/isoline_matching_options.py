"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineMatchingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.matching_strategy
    import capo_geo_routes.types.sensitive_string


class IsolineMatchingOptions(TypedDict, closed=True):
    name_hint: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The expected street name near the point. Helps disambiguate matching when multiple roads are within range.</p>"""
    on_road_threshold: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The maximum distance in meters that a point can be from a road while still being considered "on" that road. Points further than this distance require explicit matching.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    radius: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The maximum distance in meters to search for roads to match to. Points with no roads within this radius will fail to match. The roads that are considered within this radius are determined by the specified <code>Strategy</code> </p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    strategy: NotRequired["capo_geo_routes.types.matching_strategy.MatchingStrategy"]
    """<p>Determines how points are matched to the road network. <code>MatchAny</code> finds the nearest viable road segment, while <code>MatchMostSignificantRoad</code> prioritizes major roads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineMatchingOptions) -> dict:
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


def deserialize_json(data: dict) -> IsolineMatchingOptions:
    out: IsolineMatchingOptions = {}  # type: ignore[typeddict-item]
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
