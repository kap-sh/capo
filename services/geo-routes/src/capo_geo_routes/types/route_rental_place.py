"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalPlace``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.position23
    import capo_geo_routes.types.route_access_point_details
    import capo_geo_routes.types.route_rental_place_type
    import capo_geo_routes.types.route_station_details
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.sensitive_string


class RouteRentalPlace(TypedDict, closed=True):
    access_point_details: NotRequired[
        "capo_geo_routes.types.route_access_point_details.RouteAccessPointDetails"
    ]
    """<p>Details of the access point.</p>"""
    name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The name of the place.</p>"""
    original_position: NotRequired["capo_geo_routes.types.position23.Position23"]
    """<p>Position provided in the request.</p>"""
    position: "capo_geo_routes.types.position23.Position23"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    station_details: NotRequired[
        "capo_geo_routes.types.route_station_details.RouteStationDetails"
    ]
    """<p>Details about the station.</p>"""
    type: NotRequired[
        "capo_geo_routes.types.route_rental_place_type.RouteRentalPlaceType"
    ]
    """<p>The type of the place.</p>"""
    waypoint_index: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Index of the waypoint in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalPlace) -> dict:
    out: dict = {}
    if "access_point_details" in value:
        import capo_geo_routes.types.route_access_point_details

        out["AccessPointDetails"] = (
            capo_geo_routes.types.route_access_point_details.serialize_json(
                value["access_point_details"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "original_position" in value:
        import capo_geo_routes.types.position23

        out["OriginalPosition"] = capo_geo_routes.types.position23.serialize_json(
            value["original_position"]
        )
    import capo_geo_routes.types.position23

    out["Position"] = capo_geo_routes.types.position23.serialize_json(value["position"])
    if "station_details" in value:
        import capo_geo_routes.types.route_station_details

        out["StationDetails"] = (
            capo_geo_routes.types.route_station_details.serialize_json(
                value["station_details"]
            )
        )
    if "type" in value:
        import capo_geo_routes.types.route_rental_place_type

        out["Type"] = capo_geo_routes.types.route_rental_place_type.serialize_json(
            value["type"]
        )
    if "waypoint_index" in value:
        out["WaypointIndex"] = value["waypoint_index"]
    return out


def deserialize_json(data: dict) -> RouteRentalPlace:
    out: RouteRentalPlace = {}  # type: ignore[typeddict-item]
    if data.get("AccessPointDetails") is not None:
        import capo_geo_routes.types.route_access_point_details

        out["access_point_details"] = (
            capo_geo_routes.types.route_access_point_details.deserialize_json(
                data["AccessPointDetails"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("OriginalPosition") is not None:
        import capo_geo_routes.types.position23

        out["original_position"] = capo_geo_routes.types.position23.deserialize_json(
            data["OriginalPosition"]
        )
    if data.get("Position") is not None:
        import capo_geo_routes.types.position23

        out["position"] = capo_geo_routes.types.position23.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteRentalPlace.position required")
    if data.get("StationDetails") is not None:
        import capo_geo_routes.types.route_station_details

        out["station_details"] = (
            capo_geo_routes.types.route_station_details.deserialize_json(
                data["StationDetails"]
            )
        )
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_rental_place_type

        out["type"] = capo_geo_routes.types.route_rental_place_type.deserialize_json(
            data["Type"]
        )
    if data.get("WaypointIndex") is not None:
        out["waypoint_index"] = data["WaypointIndex"]
    return out


def redact_sensitive(value: RouteRentalPlace) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "original_position" in value:
        out["original_position"] = "*** Sensitive Data Redacted ***"
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    if "station_details" in value:
        import capo_geo_routes.types.route_station_details

        out["station_details"] = (
            capo_geo_routes.types.route_station_details.redact_sensitive(
                value["station_details"]
            )
        )
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    if "waypoint_index" in value:
        out["waypoint_index"] = "*** Sensitive Data Redacted ***"
    return out
