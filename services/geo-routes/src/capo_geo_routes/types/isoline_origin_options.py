"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineOriginOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.heading
    import capo_geo_routes.types.isoline_matching_options
    import capo_geo_routes.types.isoline_side_of_street_options


class IsolineOriginOptions(TypedDict, closed=True):
    avoid_actions_for_distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The distance in meters from the origin point within which certain routing actions (such as U-turns or left turns across traffic) are restricted. This helps generate more practical routes by avoiding potentially dangerous maneuvers near the starting point.</p>"""
    heading: "capo_geo_routes.types.heading.Heading"
    """<p>Initial direction of travel in degrees (0-360, where 0 is north). This affects which road segments are considered accessible from the starting point and is particularly useful when the origin is on a divided road or at a complex intersection.</p>"""
    matching: NotRequired[
        "capo_geo_routes.types.isoline_matching_options.IsolineMatchingOptions"
    ]
    """<p>Controls how the origin point is matched to the road network, including search radius and matching strategy.</p>"""
    side_of_street: NotRequired[
        "capo_geo_routes.types.isoline_side_of_street_options.IsolineSideOfStreetOptions"
    ]
    """<p>Controls which side of the street is considered accessible from the origin point, particularly important for divided roads where building entrances or parking access may only be available from one direction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineOriginOptions) -> dict:
    out: dict = {}
    out["AvoidActionsForDistance"] = value.get("avoid_actions_for_distance", 0)
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
        import capo_geo_routes.types.isoline_matching_options

        out["Matching"] = capo_geo_routes.types.isoline_matching_options.serialize_json(
            value["matching"]
        )
    if "side_of_street" in value:
        import capo_geo_routes.types.isoline_side_of_street_options

        out["SideOfStreet"] = (
            capo_geo_routes.types.isoline_side_of_street_options.serialize_json(
                value["side_of_street"]
            )
        )
    return out


def deserialize_json(data: dict) -> IsolineOriginOptions:
    out: IsolineOriginOptions = {}  # type: ignore[typeddict-item]
    if data.get("AvoidActionsForDistance") is not None:
        out["avoid_actions_for_distance"] = data["AvoidActionsForDistance"]
    else:
        out["avoid_actions_for_distance"] = 0
    if data.get("Heading") is not None:
        out["heading"] = float(data["Heading"])
    else:
        out["heading"] = 0
    if data.get("Matching") is not None:
        import capo_geo_routes.types.isoline_matching_options

        out["matching"] = (
            capo_geo_routes.types.isoline_matching_options.deserialize_json(
                data["Matching"]
            )
        )
    if data.get("SideOfStreet") is not None:
        import capo_geo_routes.types.isoline_side_of_street_options

        out["side_of_street"] = (
            capo_geo_routes.types.isoline_side_of_street_options.deserialize_json(
                data["SideOfStreet"]
            )
        )
    return out


def redact_sensitive(value: IsolineOriginOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "avoid_actions_for_distance" in value:
        out["avoid_actions_for_distance"] = "*** Sensitive Data Redacted ***"
    if "heading" in value:
        out["heading"] = "*** Sensitive Data Redacted ***"
    if "matching" in value:
        import capo_geo_routes.types.isoline_matching_options

        out["matching"] = (
            capo_geo_routes.types.isoline_matching_options.redact_sensitive(
                value["matching"]
            )
        )
    if "side_of_street" in value:
        import capo_geo_routes.types.isoline_side_of_street_options

        out["side_of_street"] = (
            capo_geo_routes.types.isoline_side_of_street_options.redact_sensitive(
                value["side_of_street"]
            )
        )
    return out
