"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleIncidentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_incident

RouteVehicleIncidentList: TypeAlias = list[
    "capo_geo_routes.types.route_vehicle_incident.RouteVehicleIncident"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleIncidentList) -> list:
    import capo_geo_routes.types.route_vehicle_incident

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_vehicle_incident.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteVehicleIncidentList:
    import capo_geo_routes.types.route_vehicle_incident

    out: RouteVehicleIncidentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.route_vehicle_incident.deserialize_json(item))
    return out


def redact_sensitive(value: RouteVehicleIncidentList) -> list[Any]:
    import capo_geo_routes.types.route_vehicle_incident

    return [
        capo_geo_routes.types.route_vehicle_incident.redact_sensitive(item)
        for item in value
    ]
