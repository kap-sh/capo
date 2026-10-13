"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIntermediateStop``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_transit_departure
    import capo_geo_routes.types.route_transit_intermediate_stop_attribute_list
    import capo_geo_routes.types.route_transit_transport_mode_details


class RouteTransitIntermediateStop(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_geo_routes.types.route_transit_intermediate_stop_attribute_list.RouteTransitIntermediateStopAttributeList"
    ]
    """<p>Attributes of the intermediate stop.</p>"""
    departure: "capo_geo_routes.types.route_transit_departure.RouteTransitDeparture"
    """<p>Departure details for the intermediate stop.</p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the stop.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this stop.</p>"""
    transport: NotRequired[
        "capo_geo_routes.types.route_transit_transport_mode_details.RouteTransitTransportModeDetails"
    ]
    """<p>Transport mode details at the intermediate stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIntermediateStop) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_geo_routes.types.route_transit_intermediate_stop_attribute_list

        out["Attributes"] = (
            capo_geo_routes.types.route_transit_intermediate_stop_attribute_list.serialize_json(
                value["attributes"]
            )
        )
    import capo_geo_routes.types.route_transit_departure

    out["Departure"] = capo_geo_routes.types.route_transit_departure.serialize_json(
        value["departure"]
    )
    out["Duration"] = value["duration"]
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "transport" in value:
        import capo_geo_routes.types.route_transit_transport_mode_details

        out["Transport"] = (
            capo_geo_routes.types.route_transit_transport_mode_details.serialize_json(
                value["transport"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTransitIntermediateStop:
    out: RouteTransitIntermediateStop = {}  # type: ignore[typeddict-item]
    if data.get("Attributes") is not None:
        import capo_geo_routes.types.route_transit_intermediate_stop_attribute_list

        out["attributes"] = (
            capo_geo_routes.types.route_transit_intermediate_stop_attribute_list.deserialize_json(
                data["Attributes"]
            )
        )
    if data.get("Departure") is not None:
        import capo_geo_routes.types.route_transit_departure

        out["departure"] = (
            capo_geo_routes.types.route_transit_departure.deserialize_json(
                data["Departure"]
            )
        )
    else:
        raise DeserializationError("RouteTransitIntermediateStop.departure required")
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTransitIntermediateStop.duration required")
    if data.get("GeometryOffset") is not None:
        out["geometry_offset"] = data["GeometryOffset"]
    if data.get("Transport") is not None:
        import capo_geo_routes.types.route_transit_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_transit_transport_mode_details.deserialize_json(
                data["Transport"]
            )
        )
    return out


def redact_sensitive(value: RouteTransitIntermediateStop) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attributes" in value:
        import capo_geo_routes.types.route_transit_intermediate_stop_attribute_list

        out["attributes"] = (
            capo_geo_routes.types.route_transit_intermediate_stop_attribute_list.redact_sensitive(
                value["attributes"]
            )
        )
    if "departure" in value:
        import capo_geo_routes.types.route_transit_departure

        out["departure"] = (
            capo_geo_routes.types.route_transit_departure.redact_sensitive(
                value["departure"]
            )
        )
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "transport" in value:
        import capo_geo_routes.types.route_transit_transport_mode_details

        out["transport"] = (
            capo_geo_routes.types.route_transit_transport_mode_details.redact_sensitive(
                value["transport"]
            )
        )
    return out
