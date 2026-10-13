"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalTransitOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_intermodal_enabled_legs_list
    import capo_geo_routes.types.route_transit_mode_list


class RouteIntermodalTransitOptions(TypedDict, closed=True):
    allowed_modes: NotRequired[
        "capo_geo_routes.types.route_transit_mode_list.RouteTransitModeList"
    ]
    """<p>Allowed transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with <code>ExcludedModes</code>.</p>"""
    enabled_for: NotRequired[
        "capo_geo_routes.types.route_intermodal_enabled_legs_list.RouteIntermodalEnabledLegsList"
    ]
    """<p>Specifies the portion of the route for which this leg type is enabled. By default, the leg type is enabled for all legs. Valid values:</p> <ul> <li> <p> <code>FirstLeg</code> - Enable this leg type for the first non-pedestrian leg of the route.</p> </li> <li> <p> <code>LastLeg</code> - Enable this leg type for the last non-pedestrian leg of the route.</p> </li> <li> <p> <code>EntireRoute</code> - Enable this leg type for the entire route.</p> </li> <li> <p> <code>None</code> - Disable this leg type entirely.</p> </li> </ul>"""
    excluded_modes: NotRequired[
        "capo_geo_routes.types.route_transit_mode_list.RouteTransitModeList"
    ]
    """<p>Excluded transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with <code>AllowedModes</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteIntermodalTransitOptions) -> dict:
    out: dict = {}
    if "allowed_modes" in value:
        import capo_geo_routes.types.route_transit_mode_list

        out["AllowedModes"] = (
            capo_geo_routes.types.route_transit_mode_list.serialize_json(
                value["allowed_modes"]
            )
        )
    if "enabled_for" in value:
        import capo_geo_routes.types.route_intermodal_enabled_legs_list

        out["EnabledFor"] = (
            capo_geo_routes.types.route_intermodal_enabled_legs_list.serialize_json(
                value["enabled_for"]
            )
        )
    if "excluded_modes" in value:
        import capo_geo_routes.types.route_transit_mode_list

        out["ExcludedModes"] = (
            capo_geo_routes.types.route_transit_mode_list.serialize_json(
                value["excluded_modes"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteIntermodalTransitOptions:
    out: RouteIntermodalTransitOptions = {}  # type: ignore[typeddict-item]
    if data.get("AllowedModes") is not None:
        import capo_geo_routes.types.route_transit_mode_list

        out["allowed_modes"] = (
            capo_geo_routes.types.route_transit_mode_list.deserialize_json(
                data["AllowedModes"]
            )
        )
    if data.get("EnabledFor") is not None:
        import capo_geo_routes.types.route_intermodal_enabled_legs_list

        out["enabled_for"] = (
            capo_geo_routes.types.route_intermodal_enabled_legs_list.deserialize_json(
                data["EnabledFor"]
            )
        )
    if data.get("ExcludedModes") is not None:
        import capo_geo_routes.types.route_transit_mode_list

        out["excluded_modes"] = (
            capo_geo_routes.types.route_transit_mode_list.deserialize_json(
                data["ExcludedModes"]
            )
        )
    return out


def redact_sensitive(value: RouteIntermodalTransitOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "allowed_modes" in value:
        import capo_geo_routes.types.route_transit_mode_list

        out["allowed_modes"] = (
            capo_geo_routes.types.route_transit_mode_list.redact_sensitive(
                value["allowed_modes"]
            )
        )
    if "enabled_for" in value:
        import capo_geo_routes.types.route_intermodal_enabled_legs_list

        out["enabled_for"] = (
            capo_geo_routes.types.route_intermodal_enabled_legs_list.redact_sensitive(
                value["enabled_for"]
            )
        )
    if "excluded_modes" in value:
        import capo_geo_routes.types.route_transit_mode_list

        out["excluded_modes"] = (
            capo_geo_routes.types.route_transit_mode_list.redact_sensitive(
                value["excluded_modes"]
            )
        )
    return out
