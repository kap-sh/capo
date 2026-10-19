"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryLegDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_ferry_after_travel_step_list
    import capo_geo_routes.types.route_ferry_arrival
    import capo_geo_routes.types.route_ferry_before_travel_step_list
    import capo_geo_routes.types.route_ferry_departure
    import capo_geo_routes.types.route_ferry_notice_list
    import capo_geo_routes.types.route_ferry_span_list
    import capo_geo_routes.types.route_ferry_summary
    import capo_geo_routes.types.route_ferry_travel_step_list
    import capo_geo_routes.types.route_pass_through_waypoint_list
    import capo_geo_routes.types.sensitive_string


class RouteFerryLegDetails(TypedDict, closed=True):
    after_travel_steps: "capo_geo_routes.types.route_ferry_after_travel_step_list.RouteFerryAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    arrival: "capo_geo_routes.types.route_ferry_arrival.RouteFerryArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    before_travel_steps: "capo_geo_routes.types.route_ferry_before_travel_step_list.RouteFerryBeforeTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    departure: "capo_geo_routes.types.route_ferry_departure.RouteFerryDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    notices: "capo_geo_routes.types.route_ferry_notice_list.RouteFerryNoticeList"
    """<p>Notices are additional information returned that indicate issues that occurred during route calculation.</p>"""
    pass_through_waypoints: "capo_geo_routes.types.route_pass_through_waypoint_list.RoutePassThroughWaypointList"
    """<p>Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.</p>"""
    route_name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Route name of the ferry line.</p>"""
    spans: "capo_geo_routes.types.route_ferry_span_list.RouteFerrySpanList"
    """<p>Spans that were computed for the requested SpanAdditionalFeatures.</p>"""
    summary: NotRequired["capo_geo_routes.types.route_ferry_summary.RouteFerrySummary"]
    """<p>Summarized details of the leg.</p>"""
    travel_steps: (
        "capo_geo_routes.types.route_ferry_travel_step_list.RouteFerryTravelStepList"
    )
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryLegDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_ferry_after_travel_step_list

    out["AfterTravelSteps"] = (
        capo_geo_routes.types.route_ferry_after_travel_step_list.serialize_json(
            value["after_travel_steps"]
        )
    )
    import capo_geo_routes.types.route_ferry_arrival

    out["Arrival"] = capo_geo_routes.types.route_ferry_arrival.serialize_json(
        value["arrival"]
    )
    import capo_geo_routes.types.route_ferry_before_travel_step_list

    out["BeforeTravelSteps"] = (
        capo_geo_routes.types.route_ferry_before_travel_step_list.serialize_json(
            value["before_travel_steps"]
        )
    )
    import capo_geo_routes.types.route_ferry_departure

    out["Departure"] = capo_geo_routes.types.route_ferry_departure.serialize_json(
        value["departure"]
    )
    import capo_geo_routes.types.route_ferry_notice_list

    out["Notices"] = capo_geo_routes.types.route_ferry_notice_list.serialize_json(
        value["notices"]
    )
    import capo_geo_routes.types.route_pass_through_waypoint_list

    out["PassThroughWaypoints"] = (
        capo_geo_routes.types.route_pass_through_waypoint_list.serialize_json(
            value["pass_through_waypoints"]
        )
    )
    if "route_name" in value:
        out["RouteName"] = value["route_name"]
    import capo_geo_routes.types.route_ferry_span_list

    out["Spans"] = capo_geo_routes.types.route_ferry_span_list.serialize_json(
        value["spans"]
    )
    if "summary" in value:
        import capo_geo_routes.types.route_ferry_summary

        out["Summary"] = capo_geo_routes.types.route_ferry_summary.serialize_json(
            value["summary"]
        )
    import capo_geo_routes.types.route_ferry_travel_step_list

    out["TravelSteps"] = (
        capo_geo_routes.types.route_ferry_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteFerryLegDetails:
    out: RouteFerryLegDetails = {}  # type: ignore[typeddict-item]
    if data.get("AfterTravelSteps") is not None:
        import capo_geo_routes.types.route_ferry_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_ferry_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        out["after_travel_steps"] = []
    if data.get("Arrival") is not None:
        import capo_geo_routes.types.route_ferry_arrival

        out["arrival"] = capo_geo_routes.types.route_ferry_arrival.deserialize_json(
            data["Arrival"]
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.arrival required")
    if data.get("BeforeTravelSteps") is not None:
        import capo_geo_routes.types.route_ferry_before_travel_step_list

        out["before_travel_steps"] = (
            capo_geo_routes.types.route_ferry_before_travel_step_list.deserialize_json(
                data["BeforeTravelSteps"]
            )
        )
    else:
        out["before_travel_steps"] = []
    if data.get("Departure") is not None:
        import capo_geo_routes.types.route_ferry_departure

        out["departure"] = capo_geo_routes.types.route_ferry_departure.deserialize_json(
            data["Departure"]
        )
    else:
        raise DeserializationError("RouteFerryLegDetails.departure required")
    if data.get("Notices") is not None:
        import capo_geo_routes.types.route_ferry_notice_list

        out["notices"] = capo_geo_routes.types.route_ferry_notice_list.deserialize_json(
            data["Notices"]
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
    if data.get("RouteName") is not None:
        out["route_name"] = data["RouteName"]
    if data.get("Spans") is not None:
        import capo_geo_routes.types.route_ferry_span_list

        out["spans"] = capo_geo_routes.types.route_ferry_span_list.deserialize_json(
            data["Spans"]
        )
    else:
        out["spans"] = []
    if data.get("Summary") is not None:
        import capo_geo_routes.types.route_ferry_summary

        out["summary"] = capo_geo_routes.types.route_ferry_summary.deserialize_json(
            data["Summary"]
        )
    if data.get("TravelSteps") is not None:
        import capo_geo_routes.types.route_ferry_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_ferry_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        out["travel_steps"] = []
    return out


def redact_sensitive(value: RouteFerryLegDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "after_travel_steps" in value:
        import capo_geo_routes.types.route_ferry_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_ferry_after_travel_step_list.redact_sensitive(
                value["after_travel_steps"]
            )
        )
    if "arrival" in value:
        import capo_geo_routes.types.route_ferry_arrival

        out["arrival"] = capo_geo_routes.types.route_ferry_arrival.redact_sensitive(
            value["arrival"]
        )
    if "before_travel_steps" in value:
        import capo_geo_routes.types.route_ferry_before_travel_step_list

        out["before_travel_steps"] = (
            capo_geo_routes.types.route_ferry_before_travel_step_list.redact_sensitive(
                value["before_travel_steps"]
            )
        )
    if "departure" in value:
        import capo_geo_routes.types.route_ferry_departure

        out["departure"] = capo_geo_routes.types.route_ferry_departure.redact_sensitive(
            value["departure"]
        )
    if "pass_through_waypoints" in value:
        import capo_geo_routes.types.route_pass_through_waypoint_list

        out["pass_through_waypoints"] = (
            capo_geo_routes.types.route_pass_through_waypoint_list.redact_sensitive(
                value["pass_through_waypoints"]
            )
        )
    if "route_name" in value:
        out["route_name"] = "*** Sensitive Data Redacted ***"
    if "spans" in value:
        import capo_geo_routes.types.route_ferry_span_list

        out["spans"] = capo_geo_routes.types.route_ferry_span_list.redact_sensitive(
            value["spans"]
        )
    if "summary" in value:
        import capo_geo_routes.types.route_ferry_summary

        out["summary"] = capo_geo_routes.types.route_ferry_summary.redact_sensitive(
            value["summary"]
        )
    if "travel_steps" in value:
        import capo_geo_routes.types.route_ferry_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_ferry_travel_step_list.redact_sensitive(
                value["travel_steps"]
            )
        )
    return out
