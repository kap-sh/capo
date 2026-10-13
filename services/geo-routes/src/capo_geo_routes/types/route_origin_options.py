"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteOriginOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.heading
    import capo_geo_routes.types.route_matching_options
    import capo_geo_routes.types.route_side_of_street_options
    import capo_geo_routes.types.sensitive_boolean


class RouteOriginOptions(TypedDict, closed=True):
    avoid_actions_for_distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.</p>"""
    avoid_u_turns: NotRequired[
        "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Avoid U-turns for calculation on highways and motorways.</p>"""
    heading: "capo_geo_routes.types.heading.Heading"
    """<p>GPS Heading at the position.</p>"""
    matching: NotRequired[
        "capo_geo_routes.types.route_matching_options.RouteMatchingOptions"
    ]
    """<p>Options to configure matching the provided position to the road network.</p>"""
    side_of_street: NotRequired[
        "capo_geo_routes.types.route_side_of_street_options.RouteSideOfStreetOptions"
    ]
    """<p>Options to configure matching the provided position to a side of the street.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteOriginOptions) -> dict:
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
    if "side_of_street" in value:
        import capo_geo_routes.types.route_side_of_street_options

        out["SideOfStreet"] = (
            capo_geo_routes.types.route_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteOriginOptions:
    out: RouteOriginOptions = {}  # type: ignore[typeddict-item]
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
    if data.get("SideOfStreet") is not None:
        import capo_geo_routes.types.route_side_of_street_options

        out["side_of_street"] = (
            capo_geo_routes.types.route_side_of_street_options.deserialize_json(
                data["SideOfStreet"]
            )
        )
    return out


def redact_sensitive(value: RouteOriginOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "avoid_actions_for_distance" in value:
        out["avoid_actions_for_distance"] = "*** Sensitive Data Redacted ***"
    if "avoid_u_turns" in value:
        out["avoid_u_turns"] = "*** Sensitive Data Redacted ***"
    if "heading" in value:
        out["heading"] = "*** Sensitive Data Redacted ***"
    if "matching" in value:
        import capo_geo_routes.types.route_matching_options

        out["matching"] = capo_geo_routes.types.route_matching_options.redact_sensitive(
            value["matching"]
        )
    if "side_of_street" in value:
        import capo_geo_routes.types.route_side_of_street_options

        out["side_of_street"] = (
            capo_geo_routes.types.route_side_of_street_options.redact_sensitive(
                value["side_of_street"]
            )
        )
    return out
