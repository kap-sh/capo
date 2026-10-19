"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitLegDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_attribution_list
    import capo_geo_routes.types.route_pass_through_waypoint_list
    import capo_geo_routes.types.route_transit_after_travel_step_list
    import capo_geo_routes.types.route_transit_agency
    import capo_geo_routes.types.route_transit_arrival
    import capo_geo_routes.types.route_transit_before_travel_step_list
    import capo_geo_routes.types.route_transit_departure
    import capo_geo_routes.types.route_transit_incident_list
    import capo_geo_routes.types.route_transit_intermediate_stop_list
    import capo_geo_routes.types.route_transit_next_departure_list
    import capo_geo_routes.types.route_transit_notice_list
    import capo_geo_routes.types.route_transit_span_list
    import capo_geo_routes.types.route_transit_summary
    import capo_geo_routes.types.route_transit_transport_mode_details
    import capo_geo_routes.types.route_transit_travel_step_list
    import capo_geo_routes.types.route_web_link_list


class RouteTransitLegDetails(TypedDict, closed=True):
    after_travel_steps: "capo_geo_routes.types.route_transit_after_travel_step_list.RouteTransitAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    agency: NotRequired["capo_geo_routes.types.route_transit_agency.RouteTransitAgency"]
    """<p>Details about the transit agency.</p>"""
    arrival: "capo_geo_routes.types.route_transit_arrival.RouteTransitArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    attributions: "capo_geo_routes.types.route_attribution_list.RouteAttributionList"
    """<p>List of required attributions to display.</p>"""
    before_travel_steps: "capo_geo_routes.types.route_transit_before_travel_step_list.RouteTransitBeforeTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    booking_web_links: "capo_geo_routes.types.route_web_link_list.RouteWebLinkList"
    """<p>Web links to external ticket booking services for the transit.</p>"""
    departure: "capo_geo_routes.types.route_transit_departure.RouteTransitDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    incidents: (
        "capo_geo_routes.types.route_transit_incident_list.RouteTransitIncidentList"
    )
    """<p>Incidents affecting this leg of the transit route.</p>"""
    intermediate_stops: "capo_geo_routes.types.route_transit_intermediate_stop_list.RouteTransitIntermediateStopList"
    """<p>Intermediate stops between departure and destination of the transit route.</p>"""
    next_departures: "capo_geo_routes.types.route_transit_next_departure_list.RouteTransitNextDepartureList"
    """<p>List of next departures that cover the same section of the route.</p>"""
    notices: "capo_geo_routes.types.route_transit_notice_list.RouteTransitNoticeList"
    """<p>List of notices that indicate issues that occurred during route calculation.</p>"""
    pass_through_waypoints: "capo_geo_routes.types.route_pass_through_waypoint_list.RoutePassThroughWaypointList"
    """<p>Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option. Not populated when the TravelMode is <code>Transit</code> or <code>Intermodal</code>.</p>"""
    spans: "capo_geo_routes.types.route_transit_span_list.RouteTransitSpanList"
    """<p>Spans that were computed for the requested SpanAdditionalFeatures. Not populated when the TravelMode is <code>Transit</code> or <code>Intermodal</code>.</p>"""
    summary: NotRequired[
        "capo_geo_routes.types.route_transit_summary.RouteTransitSummary"
    ]
    """<p>Summary of the transit leg.</p>"""
    transport: "capo_geo_routes.types.route_transit_transport_mode_details.RouteTransitTransportModeDetails"
    """<p>Transport mode details for the transit leg.</p>"""
    travel_steps: "capo_geo_routes.types.route_transit_travel_step_list.RouteTransitTravelStepList"
    """<p>Steps of a leg that must be performed during the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitLegDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_transit_after_travel_step_list

    out["AfterTravelSteps"] = (
        capo_geo_routes.types.route_transit_after_travel_step_list.serialize_json(
            value["after_travel_steps"]
        )
    )
    if "agency" in value:
        import capo_geo_routes.types.route_transit_agency

        out["Agency"] = capo_geo_routes.types.route_transit_agency.serialize_json(
            value["agency"]
        )
    import capo_geo_routes.types.route_transit_arrival

    out["Arrival"] = capo_geo_routes.types.route_transit_arrival.serialize_json(
        value["arrival"]
    )
    import capo_geo_routes.types.route_attribution_list

    out["Attributions"] = capo_geo_routes.types.route_attribution_list.serialize_json(
        value["attributions"]
    )
    import capo_geo_routes.types.route_transit_before_travel_step_list

    out["BeforeTravelSteps"] = (
        capo_geo_routes.types.route_transit_before_travel_step_list.serialize_json(
            value["before_travel_steps"]
        )
    )
    import capo_geo_routes.types.route_web_link_list

    out["BookingWebLinks"] = capo_geo_routes.types.route_web_link_list.serialize_json(
        value["booking_web_links"]
    )
    import capo_geo_routes.types.route_transit_departure

    out["Departure"] = capo_geo_routes.types.route_transit_departure.serialize_json(
        value["departure"]
    )
    import capo_geo_routes.types.route_transit_incident_list

    out["Incidents"] = capo_geo_routes.types.route_transit_incident_list.serialize_json(
        value["incidents"]
    )
    import capo_geo_routes.types.route_transit_intermediate_stop_list

    out["IntermediateStops"] = (
        capo_geo_routes.types.route_transit_intermediate_stop_list.serialize_json(
            value["intermediate_stops"]
        )
    )
    import capo_geo_routes.types.route_transit_next_departure_list

    out["NextDepartures"] = (
        capo_geo_routes.types.route_transit_next_departure_list.serialize_json(
            value["next_departures"]
        )
    )
    import capo_geo_routes.types.route_transit_notice_list

    out["Notices"] = capo_geo_routes.types.route_transit_notice_list.serialize_json(
        value["notices"]
    )
    import capo_geo_routes.types.route_pass_through_waypoint_list

    out["PassThroughWaypoints"] = (
        capo_geo_routes.types.route_pass_through_waypoint_list.serialize_json(
            value["pass_through_waypoints"]
        )
    )
    import capo_geo_routes.types.route_transit_span_list

    out["Spans"] = capo_geo_routes.types.route_transit_span_list.serialize_json(
        value["spans"]
    )
    if "summary" in value:
        import capo_geo_routes.types.route_transit_summary

        out["Summary"] = capo_geo_routes.types.route_transit_summary.serialize_json(
            value["summary"]
        )
    import capo_geo_routes.types.route_transit_transport_mode_details

    out["Transport"] = (
        capo_geo_routes.types.route_transit_transport_mode_details.serialize_json(
            value["transport"]
        )
    )
    import capo_geo_routes.types.route_transit_travel_step_list

    out["TravelSteps"] = (
        capo_geo_routes.types.route_transit_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteTransitLegDetails:
    out: RouteTransitLegDetails = {}  # type: ignore[typeddict-item]
    if data.get("AfterTravelSteps") is not None:
        import capo_geo_routes.types.route_transit_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_transit_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        out["after_travel_steps"] = []
    if data.get("Agency") is not None:
        import capo_geo_routes.types.route_transit_agency

        out["agency"] = capo_geo_routes.types.route_transit_agency.deserialize_json(
            data["Agency"]
        )
    if data.get("Arrival") is not None:
        import capo_geo_routes.types.route_transit_arrival

        out["arrival"] = capo_geo_routes.types.route_transit_arrival.deserialize_json(
            data["Arrival"]
        )
    else:
        raise DeserializationError("RouteTransitLegDetails.arrival required")
    if data.get("Attributions") is not None:
        import capo_geo_routes.types.route_attribution_list

        out["attributions"] = (
            capo_geo_routes.types.route_attribution_list.deserialize_json(
                data["Attributions"]
            )
        )
    else:
        out["attributions"] = []
    if data.get("BeforeTravelSteps") is not None:
        import capo_geo_routes.types.route_transit_before_travel_step_list

        out["before_travel_steps"] = (
            capo_geo_routes.types.route_transit_before_travel_step_list.deserialize_json(
                data["BeforeTravelSteps"]
            )
        )
    else:
        out["before_travel_steps"] = []
    if data.get("BookingWebLinks") is not None:
        import capo_geo_routes.types.route_web_link_list

        out["booking_web_links"] = (
            capo_geo_routes.types.route_web_link_list.deserialize_json(
                data["BookingWebLinks"]
            )
        )
    else:
        out["booking_web_links"] = []
    if data.get("Departure") is not None:
        import capo_geo_routes.types.route_transit_departure

        out["departure"] = (
            capo_geo_routes.types.route_transit_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteTransitLegDetails.departure required")
    if data.get("Incidents") is not None:
        import capo_geo_routes.types.route_transit_incident_list

        out["incidents"] = (
            capo_geo_routes.types.route_transit_incident_list.deserialize_json(
                data["Incidents"]
            )
        )
    else:
        out["incidents"] = []
    if data.get("IntermediateStops") is not None:
        import capo_geo_routes.types.route_transit_intermediate_stop_list

        out["intermediate_stops"] = (
            capo_geo_routes.types.route_transit_intermediate_stop_list.deserialize_json(
                data["IntermediateStops"]
            )
        )
    else:
        out["intermediate_stops"] = []
    if data.get("NextDepartures") is not None:
        import capo_geo_routes.types.route_transit_next_departure_list

        out["next_departures"] = (
            capo_geo_routes.types.route_transit_next_departure_list.deserialize_json(
                data["NextDepartures"]
            )
        )
    else:
        out["next_departures"] = []
    if data.get("Notices") is not None:
        import capo_geo_routes.types.route_transit_notice_list

        out["notices"] = (
            capo_geo_routes.types.route_transit_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        out["notices"] = []
    if data.get("PassThroughWaypoints") is not None:
        import capo_geo_routes.types.route_pass_through_waypoint_list

        out["pass_through_waypoints"] = (
            capo_geo_routes.types.route_pass_through_waypoint_list.deserialize_json(
                data["PassThroughWaypoints"]
            )
        )
    else:
        out["pass_through_waypoints"] = []
    if data.get("Spans") is not None:
        import capo_geo_routes.types.route_transit_span_list

        out["spans"] = capo_geo_routes.types.route_transit_span_list.deserialize_json(
            data["Spans"]
        )
    else:
        out["spans"] = []
    if data.get("Summary") is not None:
        import capo_geo_routes.types.route_transit_summary

        out["summary"] = capo_geo_routes.types.route_transit_summary.deserialize_json(
            data["Summary"]
        )
    if data.get("Transport") is not None:
        import capo_geo_routes.types.route_transit_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_transit_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    else:
        raise DeserializationError("RouteTransitLegDetails.transport required")
    if data.get("TravelSteps") is not None:
        import capo_geo_routes.types.route_transit_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_transit_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        out["travel_steps"] = []
    return out


def redact_sensitive(value: RouteTransitLegDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "after_travel_steps" in value:
        import capo_geo_routes.types.route_transit_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_transit_after_travel_step_list.redact_sensitive(
                value["after_travel_steps"]
            )
        )
    if "agency" in value:
        import capo_geo_routes.types.route_transit_agency

        out["agency"] = capo_geo_routes.types.route_transit_agency.redact_sensitive(
            value["agency"]
        )
    if "arrival" in value:
        import capo_geo_routes.types.route_transit_arrival

        out["arrival"] = capo_geo_routes.types.route_transit_arrival.redact_sensitive(
            value["arrival"]
        )
    if "attributions" in value:
        import capo_geo_routes.types.route_attribution_list

        out["attributions"] = (
            capo_geo_routes.types.route_attribution_list.redact_sensitive(
                value["attributions"]
            )
        )
    if "before_travel_steps" in value:
        import capo_geo_routes.types.route_transit_before_travel_step_list

        out["before_travel_steps"] = (
            capo_geo_routes.types.route_transit_before_travel_step_list.redact_sensitive(
                value["before_travel_steps"]
            )
        )
    if "booking_web_links" in value:
        import capo_geo_routes.types.route_web_link_list

        out["booking_web_links"] = (
            capo_geo_routes.types.route_web_link_list.redact_sensitive(
                value["booking_web_links"]
            )
        )
    if "departure" in value:
        import capo_geo_routes.types.route_transit_departure

        out["departure"] = (
            capo_geo_routes.types.route_transit_departure.redact_sensitive(
                value["departure"]
            )
        )
    if "incidents" in value:
        import capo_geo_routes.types.route_transit_incident_list

        out["incidents"] = (
            capo_geo_routes.types.route_transit_incident_list.redact_sensitive(
                value["incidents"]
            )
        )
    if "intermediate_stops" in value:
        import capo_geo_routes.types.route_transit_intermediate_stop_list

        out["intermediate_stops"] = (
            capo_geo_routes.types.route_transit_intermediate_stop_list.redact_sensitive(
                value["intermediate_stops"]
            )
        )
    if "next_departures" in value:
        import capo_geo_routes.types.route_transit_next_departure_list

        out["next_departures"] = (
            capo_geo_routes.types.route_transit_next_departure_list.redact_sensitive(
                value["next_departures"]
            )
        )
    if "pass_through_waypoints" in value:
        import capo_geo_routes.types.route_pass_through_waypoint_list

        out["pass_through_waypoints"] = (
            capo_geo_routes.types.route_pass_through_waypoint_list.redact_sensitive(
                value["pass_through_waypoints"]
            )
        )
    if "spans" in value:
        import capo_geo_routes.types.route_transit_span_list

        out["spans"] = capo_geo_routes.types.route_transit_span_list.redact_sensitive(
            value["spans"]
        )
    if "summary" in value:
        import capo_geo_routes.types.route_transit_summary

        out["summary"] = capo_geo_routes.types.route_transit_summary.redact_sensitive(
            value["summary"]
        )
    if "transport" in value:
        import capo_geo_routes.types.route_transit_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_transit_transport_mode_details.redact_sensitive(
                value["transport"]
            )
        )
    if "travel_steps" in value:
        import capo_geo_routes.types.route_transit_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_transit_travel_step_list.redact_sensitive(
                value["travel_steps"]
            )
        )
    return out
