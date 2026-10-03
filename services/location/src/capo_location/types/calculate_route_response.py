"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.calculate_route_summary
    import capo_location.types.leg_list


class CalculateRouteResponse(TypedDict, closed=True):
    legs: "capo_location.types.leg_list.LegList"
    """<p>Contains details about each path between a pair of positions included along a route such as: <code>StartPosition</code>, <code>EndPosition</code>, <code>Distance</code>, <code>DurationSeconds</code>, <code>Geometry</code>, and <code>Steps</code>. The number of legs returned corresponds to one fewer than the total number of positions in the request. </p> <p>For example, a route with a departure position and destination position returns one leg with the positions <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">snapped to a nearby road</a>:</p> <ul> <li> <p>The <code>StartPosition</code> is the departure position.</p> </li> <li> <p>The <code>EndPosition</code> is the destination position.</p> </li> </ul> <p>A route with a waypoint between the departure and destination position returns two legs with the positions snapped to a nearby road:</p> <ul> <li> <p>Leg 1: The <code>StartPosition</code> is the departure position . The <code>EndPosition</code> is the waypoint positon.</p> </li> <li> <p>Leg 2: The <code>StartPosition</code> is the waypoint position. The <code>EndPosition</code> is the destination position.</p> </li> </ul>"""
    summary: "capo_location.types.calculate_route_summary.CalculateRouteSummary"
    """<p>Contains information about the whole route, such as: <code>RouteBBox</code>, <code>DataSource</code>, <code>Distance</code>, <code>DistanceUnit</code>, and <code>DurationSeconds</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteResponse) -> dict:
    out: dict = {}
    import capo_location.types.leg_list

    out["Legs"] = capo_location.types.leg_list.serialize_json(value["legs"])
    import capo_location.types.calculate_route_summary

    out["Summary"] = capo_location.types.calculate_route_summary.serialize_json(
        value["summary"]
    )
    return out


def deserialize_json(data: dict) -> CalculateRouteResponse:
    out: CalculateRouteResponse = {}  # type: ignore[typeddict-item]
    if data.get("Legs") is not None:
        import capo_location.types.leg_list

        out["legs"] = capo_location.types.leg_list.deserialize_json(data["Legs"])
    else:
        raise DeserializationError("CalculateRouteResponse.legs required")
    if data.get("Summary") is not None:
        import capo_location.types.calculate_route_summary

        out["summary"] = capo_location.types.calculate_route_summary.deserialize_json(
            data["Summary"]
        )
    else:
        raise DeserializationError("CalculateRouteResponse.summary required")
    return out
