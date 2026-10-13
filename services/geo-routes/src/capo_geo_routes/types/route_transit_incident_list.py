"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIncidentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_incident

RouteTransitIncidentList: TypeAlias = list[
    "capo_geo_routes.types.route_transit_incident.RouteTransitIncident"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIncidentList) -> list:
    import capo_geo_routes.types.route_transit_incident

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_transit_incident.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransitIncidentList:
    import capo_geo_routes.types.route_transit_incident

    out: RouteTransitIncidentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_transit_incident.deserialize_json(item))
    return out


def redact_sensitive(value: RouteTransitIncidentList) -> list[Any]:
    import capo_geo_routes.types.route_transit_incident

    return [
        capo_geo_routes.types.route_transit_incident.redact_sensitive(item)
        for item in value
    ]
