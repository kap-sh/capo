"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_accessibility_attribute_list
    import capo_geo_routes.types.route_transit_mode_list
    import capo_geo_routes.types.route_transit_pedestrian_options


class RouteTransitOptions(TypedDict, closed=True):
    accessibility_attributes: NotRequired[
        "capo_geo_routes.types.route_accessibility_attribute_list.RouteAccessibilityAttributeList"
    ]
    """<p>Accessibility attributes to consider when calculating the route.</p>"""
    allowed_modes: NotRequired[
        "capo_geo_routes.types.route_transit_mode_list.RouteTransitModeList"
    ]
    """<p>Allowed transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with <code>ExcludedModes</code>.</p>"""
    excluded_modes: NotRequired[
        "capo_geo_routes.types.route_transit_mode_list.RouteTransitModeList"
    ]
    """<p>Excluded transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with <code>AllowedModes</code>.</p>"""
    max_transfers: NotRequired["int"]
    """<p>Maximum number of transfers allowed when calculating the route.</p>"""
    pedestrian: NotRequired[
        "capo_geo_routes.types.route_transit_pedestrian_options.RouteTransitPedestrianOptions"
    ]
    """<p>Options for the pedestrian leg of the transit route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitOptions) -> dict:
    out: dict = {}
    if "accessibility_attributes" in value:
        import capo_geo_routes.types.route_accessibility_attribute_list

        out["AccessibilityAttributes"] = (
            capo_geo_routes.types.route_accessibility_attribute_list.serialize_json(
                value["accessibility_attributes"]
            )
        )
    if "allowed_modes" in value:
        import capo_geo_routes.types.route_transit_mode_list

        out["AllowedModes"] = (
            capo_geo_routes.types.route_transit_mode_list.serialize_json(
                value["allowed_modes"]
            )
        )
    if "excluded_modes" in value:
        import capo_geo_routes.types.route_transit_mode_list

        out["ExcludedModes"] = (
            capo_geo_routes.types.route_transit_mode_list.serialize_json(
                value["excluded_modes"]
            )
        )
    if "max_transfers" in value:
        out["MaxTransfers"] = value["max_transfers"]
    if "pedestrian" in value:
        import capo_geo_routes.types.route_transit_pedestrian_options

        out["Pedestrian"] = (
            capo_geo_routes.types.route_transit_pedestrian_options.serialize_json(
                value["pedestrian"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTransitOptions:
    out: RouteTransitOptions = {}  # type: ignore[typeddict-item]
    if data.get("AccessibilityAttributes") is not None:
        import capo_geo_routes.types.route_accessibility_attribute_list

        out["accessibility_attributes"] = (
            capo_geo_routes.types.route_accessibility_attribute_list.deserialize_json(
                data["AccessibilityAttributes"]
            )
        )
    if data.get("AllowedModes") is not None:
        import capo_geo_routes.types.route_transit_mode_list

        out["allowed_modes"] = (
            capo_geo_routes.types.route_transit_mode_list.deserialize_json(
                data["AllowedModes"]
            )
        )
    if data.get("ExcludedModes") is not None:
        import capo_geo_routes.types.route_transit_mode_list

        out["excluded_modes"] = (
            capo_geo_routes.types.route_transit_mode_list.deserialize_json(
                data["ExcludedModes"]
            )
        )
    if data.get("MaxTransfers") is not None:
        out["max_transfers"] = data["MaxTransfers"]
    if data.get("Pedestrian") is not None:
        import capo_geo_routes.types.route_transit_pedestrian_options

        out["pedestrian"] = (
            capo_geo_routes.types.route_transit_pedestrian_options.deserialize_json(
                data["Pedestrian"]
            )
        )
    return out


def redact_sensitive(value: RouteTransitOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "accessibility_attributes" in value:
        import capo_geo_routes.types.route_accessibility_attribute_list

        out["accessibility_attributes"] = (
            capo_geo_routes.types.route_accessibility_attribute_list.redact_sensitive(
                value["accessibility_attributes"]
            )
        )
    if "allowed_modes" in value:
        import capo_geo_routes.types.route_transit_mode_list

        out["allowed_modes"] = (
            capo_geo_routes.types.route_transit_mode_list.redact_sensitive(
                value["allowed_modes"]
            )
        )
    if "excluded_modes" in value:
        import capo_geo_routes.types.route_transit_mode_list

        out["excluded_modes"] = (
            capo_geo_routes.types.route_transit_mode_list.redact_sensitive(
                value["excluded_modes"]
            )
        )
    if "pedestrian" in value:
        import capo_geo_routes.types.route_transit_pedestrian_options

        out["pedestrian"] = (
            capo_geo_routes.types.route_transit_pedestrian_options.redact_sensitive(
                value["pedestrian"]
            )
        )
    return out
