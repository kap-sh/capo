"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWaypoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.heading
    import capo_geo_routes.types.position
    import capo_geo_routes.types.route_matching_options
    import capo_geo_routes.types.route_side_of_street_options
    import capo_geo_routes.types.sensitive_boolean


class RouteWaypoint(TypedDict, closed=True):
    avoid_actions_for_distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p> Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    avoid_u_turns: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p> Avoid U-turns for calculation on highways and motorways. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    heading: "capo_geo_routes.types.heading.Heading"
    """<p> GPS Heading at the position. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    matching: NotRequired[
        "capo_geo_routes.types.route_matching_options.RouteMatchingOptions"
    ]
    """<p> Options to configure matching the provided position to the road network. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    pass_through: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p> If the waypoint should not be treated as a stop. If yes, the waypoint is passed through and doesn't split the route into different legs. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    position: "capo_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    side_of_street: NotRequired[
        "capo_geo_routes.types.route_side_of_street_options.RouteSideOfStreetOptions"
    ]
    """<p> Options to configure matching the provided position to a side of the street. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    stop_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p> Duration of the stop. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteWaypoint) -> dict:
    out: dict = {}
    out["AvoidActionsForDistance"] = value.get("avoid_actions_for_distance", 0)
    if "avoid_u_turns" in value:
        out["AvoidUTurns"] = value["avoid_u_turns"]
    out["Heading"] = (
        "NaN"
        if value.get("heading", 0) != value.get("heading", 0)
        else "Infinity"
        if value.get("heading", 0) == float("inf")
        else "-Infinity"
        if value.get("heading", 0) == float("-inf")
        else value.get("heading", 0)
    )
    if "matching" in value:
        import capo_geo_routes.types.route_matching_options

        out["Matching"] = capo_geo_routes.types.route_matching_options.serialize_json(
            value["matching"]
        )
    if "pass_through" in value:
        out["PassThrough"] = value["pass_through"]
    import capo_geo_routes.types.position

    out["Position"] = capo_geo_routes.types.position.serialize_json(value["position"])
    if "side_of_street" in value:
        import capo_geo_routes.types.route_side_of_street_options

        out["SideOfStreet"] = (
            capo_geo_routes.types.route_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    out["StopDuration"] = value.get("stop_duration", 0)
    return out


def deserialize_json(data: dict) -> RouteWaypoint:
    out: RouteWaypoint = {}  # type: ignore[typeddict-item]
    if data.get("AvoidActionsForDistance") is not None:
        out["avoid_actions_for_distance"] = data["AvoidActionsForDistance"]
    else:
        out["avoid_actions_for_distance"] = 0
    if data.get("AvoidUTurns") is not None:
        out["avoid_u_turns"] = data["AvoidUTurns"]
    if data.get("Heading") is not None:
        out["heading"] = float(data["Heading"])
    else:
        out["heading"] = 0
    if data.get("Matching") is not None:
        import capo_geo_routes.types.route_matching_options

        out["matching"] = capo_geo_routes.types.route_matching_options.deserialize_json(
            data["Matching"]
        )
    if data.get("PassThrough") is not None:
        out["pass_through"] = data["PassThrough"]
    if data.get("Position") is not None:
        import capo_geo_routes.types.position

        out["position"] = capo_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteWaypoint.position required")
    if data.get("SideOfStreet") is not None:
        import capo_geo_routes.types.route_side_of_street_options

        out["side_of_street"] = (
            capo_geo_routes.types.route_side_of_street_options.deserialize_json(
                data["SideOfStreet"]
            )
        )
    if data.get("StopDuration") is not None:
        out["stop_duration"] = data["StopDuration"]
    else:
        out["stop_duration"] = 0
    return out
