"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleLegDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_pass_through_waypoint_list
    import capo_geo_routes.types.route_toll_list
    import capo_geo_routes.types.route_toll_system_list
    import capo_geo_routes.types.route_vehicle_after_travel_step_list
    import capo_geo_routes.types.route_vehicle_arrival
    import capo_geo_routes.types.route_vehicle_departure
    import capo_geo_routes.types.route_vehicle_incident_list
    import capo_geo_routes.types.route_vehicle_notice_list
    import capo_geo_routes.types.route_vehicle_span_list
    import capo_geo_routes.types.route_vehicle_summary
    import capo_geo_routes.types.route_vehicle_travel_step_list
    import capo_geo_routes.types.route_zone_list
    import capo_geo_routes.types.truck_road_type_list


class RouteVehicleLegDetails(TypedDict, closed=True):
    after_travel_steps: "capo_geo_routes.types.route_vehicle_after_travel_step_list.RouteVehicleAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    arrival: "capo_geo_routes.types.route_vehicle_arrival.RouteVehicleArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    departure: "capo_geo_routes.types.route_vehicle_departure.RouteVehicleDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    incidents: (
        "capo_geo_routes.types.route_vehicle_incident_list.RouteVehicleIncidentList"
    )
    """<p> Incidents corresponding to this leg of the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    notices: "capo_geo_routes.types.route_vehicle_notice_list.RouteVehicleNoticeList"
    """<p> Notices are additional information returned that indicate issues that occurred during route calculation. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    pass_through_waypoints: "capo_geo_routes.types.route_pass_through_waypoint_list.RoutePassThroughWaypointList"
    """<p>Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.</p>"""
    spans: "capo_geo_routes.types.route_vehicle_span_list.RouteVehicleSpanList"
    """<p> Spans that were computed for the requested SpanAdditionalFeatures. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    summary: NotRequired[
        "capo_geo_routes.types.route_vehicle_summary.RouteVehicleSummary"
    ]
    """<p>Summarized details of the leg.</p>"""
    tolls: "capo_geo_routes.types.route_toll_list.RouteTollList"
    """<p> Toll related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    toll_systems: "capo_geo_routes.types.route_toll_system_list.RouteTollSystemList"
    """<p> Toll systems are authorities that collect payments for the toll. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    travel_steps: "capo_geo_routes.types.route_vehicle_travel_step_list.RouteVehicleTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    truck_road_types: "capo_geo_routes.types.truck_road_type_list.TruckRoadTypeList"
    """<p> Truck road type identifiers. <code>BK1</code> through <code>BK4</code> apply only to Sweden. <code>A2,A4,B2,B4,C,D,ET2,ET4</code> apply only to Mexico. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <note> <p>There are currently no other supported values as of 26th April 2024.</p> </note>"""
    zones: "capo_geo_routes.types.route_zone_list.RouteZoneList"
    """<p> Zones corresponding to this leg of the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleLegDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_vehicle_after_travel_step_list

    out["AfterTravelSteps"] = (
        capo_geo_routes.types.route_vehicle_after_travel_step_list.serialize_json(
            value.get("after_travel_steps", [])
        )
    )
    import capo_geo_routes.types.route_vehicle_arrival

    out["Arrival"] = capo_geo_routes.types.route_vehicle_arrival.serialize_json(
        value["arrival"]
    )
    import capo_geo_routes.types.route_vehicle_departure

    out["Departure"] = capo_geo_routes.types.route_vehicle_departure.serialize_json(
        value["departure"]
    )
    import capo_geo_routes.types.route_vehicle_incident_list

    out["Incidents"] = capo_geo_routes.types.route_vehicle_incident_list.serialize_json(
        value["incidents"]
    )
    import capo_geo_routes.types.route_vehicle_notice_list

    out["Notices"] = capo_geo_routes.types.route_vehicle_notice_list.serialize_json(
        value["notices"]
    )
    import capo_geo_routes.types.route_pass_through_waypoint_list

    out["PassThroughWaypoints"] = (
        capo_geo_routes.types.route_pass_through_waypoint_list.serialize_json(
            value["pass_through_waypoints"]
        )
    )
    import capo_geo_routes.types.route_vehicle_span_list

    out["Spans"] = capo_geo_routes.types.route_vehicle_span_list.serialize_json(
        value["spans"]
    )
    if "summary" in value:
        import capo_geo_routes.types.route_vehicle_summary

        out["Summary"] = capo_geo_routes.types.route_vehicle_summary.serialize_json(
            value["summary"]
        )
    import capo_geo_routes.types.route_toll_list

    out["Tolls"] = capo_geo_routes.types.route_toll_list.serialize_json(value["tolls"])
    import capo_geo_routes.types.route_toll_system_list

    out["TollSystems"] = capo_geo_routes.types.route_toll_system_list.serialize_json(
        value["toll_systems"]
    )
    import capo_geo_routes.types.route_vehicle_travel_step_list

    out["TravelSteps"] = (
        capo_geo_routes.types.route_vehicle_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    import capo_geo_routes.types.truck_road_type_list

    out["TruckRoadTypes"] = capo_geo_routes.types.truck_road_type_list.serialize_json(
        value["truck_road_types"]
    )
    import capo_geo_routes.types.route_zone_list

    out["Zones"] = capo_geo_routes.types.route_zone_list.serialize_json(value["zones"])
    return out


def deserialize_json(data: dict) -> RouteVehicleLegDetails:
    out: RouteVehicleLegDetails = {}  # type: ignore[typeddict-item]
    if data.get("AfterTravelSteps") is not None:
        import capo_geo_routes.types.route_vehicle_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_vehicle_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        out["after_travel_steps"] = []
    if data.get("Arrival") is not None:
        import capo_geo_routes.types.route_vehicle_arrival

        out["arrival"] = capo_geo_routes.types.route_vehicle_arrival.deserialize_json(
            data["Arrival"]
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.arrival required")
    if data.get("Departure") is not None:
        import capo_geo_routes.types.route_vehicle_departure

        out["departure"] = (
            capo_geo_routes.types.route_vehicle_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.departure required")
    if data.get("Incidents") is not None:
        import capo_geo_routes.types.route_vehicle_incident_list

        out["incidents"] = (
            capo_geo_routes.types.route_vehicle_incident_list.deserialize_json(
                data["Incidents"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.incidents required")
    if data.get("Notices") is not None:
        import capo_geo_routes.types.route_vehicle_notice_list

        out["notices"] = (
            capo_geo_routes.types.route_vehicle_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.notices required")
    if data.get("PassThroughWaypoints") is not None:
        import capo_geo_routes.types.route_pass_through_waypoint_list

        out["pass_through_waypoints"] = (
            capo_geo_routes.types.route_pass_through_waypoint_list.deserialize_json(
                data["PassThroughWaypoints"]
            )
        )
    else:
        raise DeserializationError(
            "RouteVehicleLegDetails.pass_through_waypoints required"
        )
    if data.get("Spans") is not None:
        import capo_geo_routes.types.route_vehicle_span_list

        out["spans"] = capo_geo_routes.types.route_vehicle_span_list.deserialize_json(
            data["Spans"]
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.spans required")
    if data.get("Summary") is not None:
        import capo_geo_routes.types.route_vehicle_summary

        out["summary"] = capo_geo_routes.types.route_vehicle_summary.deserialize_json(
            data["Summary"]
        )
    if data.get("Tolls") is not None:
        import capo_geo_routes.types.route_toll_list

        out["tolls"] = capo_geo_routes.types.route_toll_list.deserialize_json(
            data["Tolls"]
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.tolls required")
    if data.get("TollSystems") is not None:
        import capo_geo_routes.types.route_toll_system_list

        out["toll_systems"] = (
            capo_geo_routes.types.route_toll_system_list.deserialize_json(
                data["TollSystems"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.toll_systems required")
    if data.get("TravelSteps") is not None:
        import capo_geo_routes.types.route_vehicle_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_vehicle_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.travel_steps required")
    if data.get("TruckRoadTypes") is not None:
        import capo_geo_routes.types.truck_road_type_list

        out["truck_road_types"] = (
            capo_geo_routes.types.truck_road_type_list.deserialize_json(
                data["TruckRoadTypes"]
            )
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.truck_road_types required")
    if data.get("Zones") is not None:
        import capo_geo_routes.types.route_zone_list

        out["zones"] = capo_geo_routes.types.route_zone_list.deserialize_json(
            data["Zones"]
        )
    else:
        raise DeserializationError("RouteVehicleLegDetails.zones required")
    return out
