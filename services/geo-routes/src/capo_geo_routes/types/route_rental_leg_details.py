"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalLegDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_attribution_list
    import capo_geo_routes.types.route_rental_after_travel_step_list
    import capo_geo_routes.types.route_rental_agency
    import capo_geo_routes.types.route_rental_arrival
    import capo_geo_routes.types.route_rental_before_travel_step_list
    import capo_geo_routes.types.route_rental_departure
    import capo_geo_routes.types.route_rental_summary
    import capo_geo_routes.types.route_rental_transport_mode_details
    import capo_geo_routes.types.route_rental_travel_step_list
    import capo_geo_routes.types.route_web_link_list


class RouteRentalLegDetails(TypedDict, closed=True):
    after_travel_steps: "capo_geo_routes.types.route_rental_after_travel_step_list.RouteRentalAfterTravelStepList"
    """<p>Steps of a leg that must be performed after the travel portion of the leg.</p>"""
    agency: "capo_geo_routes.types.route_rental_agency.RouteRentalAgency"
    """<p>Details about the rental agency.</p>"""
    arrival: "capo_geo_routes.types.route_rental_arrival.RouteRentalArrival"
    """<p>Details corresponding to the arrival for the leg.</p>"""
    attributions: "capo_geo_routes.types.route_attribution_list.RouteAttributionList"
    """<p>List of required attributions to display.</p>"""
    before_travel_steps: "capo_geo_routes.types.route_rental_before_travel_step_list.RouteRentalBeforeTravelStepList"
    """<p>Steps of a leg that must be performed before the travel portion of the leg.</p>"""
    booking_web_links: "capo_geo_routes.types.route_web_link_list.RouteWebLinkList"
    """<p>Web links to external ticket booking services for the rental.</p>"""
    departure: "capo_geo_routes.types.route_rental_departure.RouteRentalDeparture"
    """<p>Details corresponding to the departure for the leg.</p>"""
    summary: NotRequired[
        "capo_geo_routes.types.route_rental_summary.RouteRentalSummary"
    ]
    """<p>Summary of the rental leg.</p>"""
    transport: "capo_geo_routes.types.route_rental_transport_mode_details.RouteRentalTransportModeDetails"
    """<p>Transport mode details for the rental leg.</p>"""
    travel_steps: (
        "capo_geo_routes.types.route_rental_travel_step_list.RouteRentalTravelStepList"
    )
    """<p>Steps of a leg that must be performed during the travel portion of the leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalLegDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_rental_after_travel_step_list

    out["AfterTravelSteps"] = (
        capo_geo_routes.types.route_rental_after_travel_step_list.serialize_json(
            value["after_travel_steps"]
        )
    )
    import capo_geo_routes.types.route_rental_agency

    out["Agency"] = capo_geo_routes.types.route_rental_agency.serialize_json(
        value["agency"]
    )
    import capo_geo_routes.types.route_rental_arrival

    out["Arrival"] = capo_geo_routes.types.route_rental_arrival.serialize_json(
        value["arrival"]
    )
    import capo_geo_routes.types.route_attribution_list

    out["Attributions"] = capo_geo_routes.types.route_attribution_list.serialize_json(
        value["attributions"]
    )
    import capo_geo_routes.types.route_rental_before_travel_step_list

    out["BeforeTravelSteps"] = (
        capo_geo_routes.types.route_rental_before_travel_step_list.serialize_json(
            value["before_travel_steps"]
        )
    )
    import capo_geo_routes.types.route_web_link_list

    out["BookingWebLinks"] = capo_geo_routes.types.route_web_link_list.serialize_json(
        value["booking_web_links"]
    )
    import capo_geo_routes.types.route_rental_departure

    out["Departure"] = capo_geo_routes.types.route_rental_departure.serialize_json(
        value["departure"]
    )
    if "summary" in value:
        import capo_geo_routes.types.route_rental_summary

        out["Summary"] = capo_geo_routes.types.route_rental_summary.serialize_json(
            value["summary"]
        )
    import capo_geo_routes.types.route_rental_transport_mode_details

    out["Transport"] = (
        capo_geo_routes.types.route_rental_transport_mode_details.serialize_json(
            value["transport"]
        )
    )
    import capo_geo_routes.types.route_rental_travel_step_list

    out["TravelSteps"] = (
        capo_geo_routes.types.route_rental_travel_step_list.serialize_json(
            value["travel_steps"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteRentalLegDetails:
    out: RouteRentalLegDetails = {}  # type: ignore[typeddict-item]
    if data.get("AfterTravelSteps") is not None:
        import capo_geo_routes.types.route_rental_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_rental_after_travel_step_list.deserialize_json(
                data["AfterTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.after_travel_steps required")
    if data.get("Agency") is not None:
        import capo_geo_routes.types.route_rental_agency

        out["agency"] = capo_geo_routes.types.route_rental_agency.deserialize_json(
            data["Agency"]
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.agency required")
    if data.get("Arrival") is not None:
        import capo_geo_routes.types.route_rental_arrival

        out["arrival"] = capo_geo_routes.types.route_rental_arrival.deserialize_json(
            data["Arrival"]
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.arrival required")
    if data.get("Attributions") is not None:
        import capo_geo_routes.types.route_attribution_list

        out["attributions"] = (
            capo_geo_routes.types.route_attribution_list.deserialize_json(
                data["Attributions"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.attributions required")
    if data.get("BeforeTravelSteps") is not None:
        import capo_geo_routes.types.route_rental_before_travel_step_list

        out["before_travel_steps"] = (
            capo_geo_routes.types.route_rental_before_travel_step_list.deserialize_json(
                data["BeforeTravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.before_travel_steps required")
    if data.get("BookingWebLinks") is not None:
        import capo_geo_routes.types.route_web_link_list

        out["booking_web_links"] = (
            capo_geo_routes.types.route_web_link_list.deserialize_json(
                data["BookingWebLinks"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.booking_web_links required")
    if data.get("Departure") is not None:
        import capo_geo_routes.types.route_rental_departure

        out["departure"] = (
            capo_geo_routes.types.route_rental_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.departure required")
    if data.get("Summary") is not None:
        import capo_geo_routes.types.route_rental_summary

        out["summary"] = capo_geo_routes.types.route_rental_summary.deserialize_json(
            data["Summary"]
        )
    if data.get("Transport") is not None:
        import capo_geo_routes.types.route_rental_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_rental_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.transport required")
    if data.get("TravelSteps") is not None:
        import capo_geo_routes.types.route_rental_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_rental_travel_step_list.deserialize_json(
                data["TravelSteps"]
            )
        )
    else:
        raise DeserializationError("RouteRentalLegDetails.travel_steps required")
    return out


def redact_sensitive(value: RouteRentalLegDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "after_travel_steps" in value:
        import capo_geo_routes.types.route_rental_after_travel_step_list

        out["after_travel_steps"] = (
            capo_geo_routes.types.route_rental_after_travel_step_list.redact_sensitive(
                value["after_travel_steps"]
            )
        )
    if "agency" in value:
        import capo_geo_routes.types.route_rental_agency

        out["agency"] = capo_geo_routes.types.route_rental_agency.redact_sensitive(
            value["agency"]
        )
    if "arrival" in value:
        import capo_geo_routes.types.route_rental_arrival

        out["arrival"] = capo_geo_routes.types.route_rental_arrival.redact_sensitive(
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
        import capo_geo_routes.types.route_rental_before_travel_step_list

        out["before_travel_steps"] = (
            capo_geo_routes.types.route_rental_before_travel_step_list.redact_sensitive(
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
        import capo_geo_routes.types.route_rental_departure

        out["departure"] = (
            capo_geo_routes.types.route_rental_departure.redact_sensitive(
                value["departure"]
            )
        )
    if "summary" in value:
        import capo_geo_routes.types.route_rental_summary

        out["summary"] = capo_geo_routes.types.route_rental_summary.redact_sensitive(
            value["summary"]
        )
    if "transport" in value:
        import capo_geo_routes.types.route_rental_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_rental_transport_mode_details.redact_sensitive(
                value["transport"]
            )
        )
    if "travel_steps" in value:
        import capo_geo_routes.types.route_rental_travel_step_list

        out["travel_steps"] = (
            capo_geo_routes.types.route_rental_travel_step_list.redact_sensitive(
                value["travel_steps"]
            )
        )
    return out
