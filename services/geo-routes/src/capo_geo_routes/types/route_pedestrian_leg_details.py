"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianLegDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_pass_through_waypoint_list
    import capo_geo_routes.types.route_pedestrian_after_travel_step_list
    import capo_geo_routes.types.route_pedestrian_arrival
    import capo_geo_routes.types.route_pedestrian_departure
    import capo_geo_routes.types.route_pedestrian_notice_list
    import capo_geo_routes.types.route_pedestrian_span_list
    import capo_geo_routes.types.route_pedestrian_summary
    import capo_geo_routes.types.route_pedestrian_travel_step_list


class RoutePedestrianLegDetails(TypedDict, closed=True):
    after_travel_steps: "capo_geo_routes.types.route_pedestrian_after_travel_step_list.RoutePedestrianAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    arrival: "capo_geo_routes.types.route_pedestrian_arrival.RoutePedestrianArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    departure: (
        "capo_geo_routes.types.route_pedestrian_departure.RoutePedestrianDeparture"
    )
    """<p>Details corresponding to the departure for the leg.</p>"""
    notices: (
        "capo_geo_routes.types.route_pedestrian_notice_list.RoutePedestrianNoticeList"
    )
    """<p> Notices are additional information returned that indicate issues that occurred during route calculation. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    pass_through_waypoints: "capo_geo_routes.types.route_pass_through_waypoint_list.RoutePassThroughWaypointList"
    """<p>Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.</p>"""
    spans: "capo_geo_routes.types.route_pedestrian_span_list.RoutePedestrianSpanList"
    """<p> Spans that were computed for the requested SpanAdditionalFeatures. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    summary: NotRequired[
        "capo_geo_routes.types.route_pedestrian_summary.RoutePedestrianSummary"
    ]
    """<p>Summarized details of the leg.</p>"""
    travel_steps: "capo_geo_routes.types.route_pedestrian_travel_step_list.RoutePedestrianTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianLegDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_pedestrian_after_travel_step_list

    out["AfterTravelSteps"] = (
        capo_geo_routes.types.route_pedestrian_after_travel_step_list.serialize_json(
            value.get("after_travel_steps", [])
        )
    )
    import capo_geo_routes.types.route_pedestrian_arrival

    out["Arrival"] = capo_geo_routes.types.route_pedestrian_arrival.serialize_json(
        value["arrival"]
    )
    import capo_geo_routes.types.route_pedestrian_departure

    out["Departure"] = capo_geo_routes.types.route_pedestrian_departure.serialize_json(
        value["departure"]
    )
    import capo_geo_routes.types.route_pedestrian_notice_list

    out["Notices"] = capo_geo_routes.types.route_pedestrian_notice_list.serialize_json(
        value["notices"]
    )
    import capo_geo_routes.types.route_pass_through_waypoint_list

    out["PassThroughWaypoints"] = (
        capo_geo_routes.types.route_pass_through_waypoint_list.serialize_json(
            value["pass_through_waypoints"]
        )
    )
    import capo_geo_routes.types.route_pedestrian_span_list

    out["Spans"] = capo_geo_routes.types.route_pedestrian_span_list.serialize_json(
        value["spans"]
    )
    if "summary" in value:
        import capo_geo_routes.types.route_pedestrian_summary

        out["Summary"] = capo_geo_routes.types.route_pedestrian_summary.serialize_json(
            value["summary"]
        )
    import capo_geo_routes.types.route_pedestrian_travel_step_list

    out["TravelSteps"] = (
        capo_geo_routes.types.route_pedestrian_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RoutePedestrianLegDetails:
    out: RoutePedestrianLegDetails = {}  # type: ignore[typeddict-item]
    if data.get("AfterTravelSteps") is not None:
        import capo_geo_routes.types.route_pedestrian_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_pedestrian_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        out["after_travel_steps"] = []
    if data.get("Arrival") is not None:
        import capo_geo_routes.types.route_pedestrian_arrival

        out["arrival"] = (
            capo_geo_routes.types.route_pedestrian_arrival.deserialize_json(
                data["Arrival"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.arrival required")
    if data.get("Departure") is not None:
        import capo_geo_routes.types.route_pedestrian_departure

        out["departure"] = (
            capo_geo_routes.types.route_pedestrian_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.departure required")
    if data.get("Notices") is not None:
        import capo_geo_routes.types.route_pedestrian_notice_list

        out["notices"] = (
            capo_geo_routes.types.route_pedestrian_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.notices required")
    if data.get("PassThroughWaypoints") is not None:
        import capo_geo_routes.types.route_pass_through_waypoint_list

        out["pass_through_waypoints"] = (
            capo_geo_routes.types.route_pass_through_waypoint_list.deserialize_json(
                data["PassThroughWaypoints"]
            )
        )
    else:
        raise DeserializationError(
            "RoutePedestrianLegDetails.pass_through_waypoints required"
        )
    if data.get("Spans") is not None:
        import capo_geo_routes.types.route_pedestrian_span_list

        out["spans"] = (
            capo_geo_routes.types.route_pedestrian_span_list.deserialize_json(
                data["Spans"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.spans required")
    if data.get("Summary") is not None:
        import capo_geo_routes.types.route_pedestrian_summary

        out["summary"] = (
            capo_geo_routes.types.route_pedestrian_summary.deserialize_json(
                data["Summary"]
            )
        )
    if data.get("TravelSteps") is not None:
        import capo_geo_routes.types.route_pedestrian_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_pedestrian_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RoutePedestrianLegDetails.travel_steps required")
    return out
