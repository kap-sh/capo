"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitTransportModeDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.hex_color
    import capo_geo_routes.types.route_accessibility_availability_details
    import capo_geo_routes.types.route_transit_mode
    import capo_geo_routes.types.sensitive_string


class RouteTransitTransportModeDetails(TypedDict, closed=True):
    accessibility: NotRequired[
        "capo_geo_routes.types.route_accessibility_availability_details.RouteAccessibilityAvailabilityDetails"
    ]
    """<p>Wheelchair accessibility information for the transit vehicle.</p>"""
    color: NotRequired["capo_geo_routes.types.hex_color.HexColor"]
    """<p>Color of the transport polyline and background for the transport name.</p>"""
    headsign: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Transit route headsign.</p>"""
    long_route_name: NotRequired[
        "capo_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>Long name of the transit route.</p>"""
    mode: "capo_geo_routes.types.route_transit_mode.RouteTransitMode"
    """<p>Mode of the transit transport.</p>"""
    route_name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Transit route name.</p>"""
    short_route_name: NotRequired[
        "capo_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>Short name of the transit route.</p>"""
    text_color: NotRequired["capo_geo_routes.types.hex_color.HexColor"]
    """<p>Color of the transport name text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitTransportModeDetails) -> dict:
    out: dict = {}
    if "accessibility" in value:
        import capo_geo_routes.types.route_accessibility_availability_details

        out["Accessibility"] = (
            capo_geo_routes.types.route_accessibility_availability_details.serialize_json(
                value["accessibility"]
            )
        )
    if "color" in value:
        out["Color"] = value["color"]
    if "headsign" in value:
        out["Headsign"] = value["headsign"]
    if "long_route_name" in value:
        out["LongRouteName"] = value["long_route_name"]
    import capo_geo_routes.types.route_transit_mode

    out["Mode"] = capo_geo_routes.types.route_transit_mode.serialize_json(value["mode"])
    if "route_name" in value:
        out["RouteName"] = value["route_name"]
    if "short_route_name" in value:
        out["ShortRouteName"] = value["short_route_name"]
    if "text_color" in value:
        out["TextColor"] = value["text_color"]
    return out


def deserialize_json(data: dict) -> RouteTransitTransportModeDetails:
    out: RouteTransitTransportModeDetails = {}  # type: ignore[typeddict-item]
    if data.get("Accessibility") is not None:
        import capo_geo_routes.types.route_accessibility_availability_details

        out["accessibility"] = (
            capo_geo_routes.types.route_accessibility_availability_details.deserialize_json(
                data["Accessibility"]
            )
        )
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    if data.get("Headsign") is not None:
        out["headsign"] = data["Headsign"]
    if data.get("LongRouteName") is not None:
        out["long_route_name"] = data["LongRouteName"]
    if data.get("Mode") is not None:
        import capo_geo_routes.types.route_transit_mode

        out["mode"] = capo_geo_routes.types.route_transit_mode.deserialize_json(
            data["Mode"]
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_geo_routes.types.route_transit_mode.RouteTransitMode", ""
        )
    if data.get("RouteName") is not None:
        out["route_name"] = data["RouteName"]
    if data.get("ShortRouteName") is not None:
        out["short_route_name"] = data["ShortRouteName"]
    if data.get("TextColor") is not None:
        out["text_color"] = data["TextColor"]
    return out


def redact_sensitive(value: RouteTransitTransportModeDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "color" in value:
        out["color"] = "*** Sensitive Data Redacted ***"
    if "headsign" in value:
        out["headsign"] = "*** Sensitive Data Redacted ***"
    if "long_route_name" in value:
        out["long_route_name"] = "*** Sensitive Data Redacted ***"
    if "mode" in value:
        out["mode"] = "*** Sensitive Data Redacted ***"
    if "route_name" in value:
        out["route_name"] = "*** Sensitive Data Redacted ***"
    if "short_route_name" in value:
        out["short_route_name"] = "*** Sensitive Data Redacted ***"
    if "text_color" in value:
        out["text_color"] = "*** Sensitive Data Redacted ***"
    return out
