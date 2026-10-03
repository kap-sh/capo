"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.calculate_route_car_mode_options
    import capo_location.types.calculate_route_truck_mode_options
    import capo_location.types.distance_unit
    import capo_location.types.optimization_mode
    import capo_location.types.position
    import capo_location.types.resource_name
    import capo_location.types.sensitive_boolean
    import capo_location.types.timestamp
    import capo_location.types.travel_mode
    import capo_location.types.waypoint_position_list


class CalculateRouteRequest(TypedDict, closed=True):
    calculator_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the route calculator resource that you want to use to calculate the route. </p>"""
    departure_position: "capo_location.types.position.Position"
    """<p>The start position for the route. Defined in <a href="https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84">World Geodetic System (WGS 84)</a> format: <code>[longitude, latitude]</code>.</p> <ul> <li> <p>For example, <code>[-123.115, 49.285]</code> </p> </li> </ul> <note> <p>If you specify a departure that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a <code>400 RoutesValidationException</code> error.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>"""
    destination_position: "capo_location.types.position.Position"
    """<p>The finish position for the route. Defined in <a href="https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84">World Geodetic System (WGS 84)</a> format: <code>[longitude, latitude]</code>.</p> <ul> <li> <p> For example, <code>[-122.339, 47.615]</code> </p> </li> </ul> <note> <p>If you specify a destination that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. </p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>"""
    waypoint_positions: NotRequired[
        "capo_location.types.waypoint_position_list.WaypointPositionList"
    ]
    """<p>Specifies an ordered list of up to 23 intermediate positions to include along a route between the departure position and destination position. </p> <ul> <li> <p>For example, from the <code>DeparturePosition</code> <code>[-123.115, 49.285]</code>, the route follows the order that the waypoint positions are given <code>[[-122.757, 49.0021],[-122.349, 47.620]]</code> </p> </li> </ul> <note> <p>If you specify a waypoint position that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. </p> <p>Specifying more than 23 waypoints returns a <code>400 ValidationException</code> error.</p> <p>If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a <code>400 RoutesValidationException</code> error.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>"""
    travel_mode: NotRequired["capo_location.types.travel_mode.TravelMode"]
    """<p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. You can choose <code>Car</code>, <code>Truck</code>, <code>Walking</code>, <code>Bicycle</code> or <code>Motorcycle</code> as options for the <code>TravelMode</code>.</p> <note> <p> <code>Bicycle</code> and <code>Motorcycle</code> are only valid when using Grab as a data provider, and only within Southeast Asia.</p> <p> <code>Truck</code> is not available for Grab.</p> <p>For more details on the using Grab for routing, including areas of coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>The <code>TravelMode</code> you specify also determines how you specify route preferences: </p> <ul> <li> <p>If traveling by <code>Car</code> use the <code>CarModeOptions</code> parameter.</p> </li> <li> <p>If traveling by <code>Truck</code> use the <code>TruckModeOptions</code> parameter.</p> </li> </ul> <p>Default Value: <code>Car</code> </p>"""
    departure_time: NotRequired["capo_location.types.timestamp.Timestamp"]
    """<p>Specifies the desired time of departure. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <ul> <li> <p>In <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>"""
    depart_now: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Sets the time of departure as the current time. Uses the current time to calculate a route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    distance_unit: NotRequired["capo_location.types.distance_unit.DistanceUnit"]
    """<p>Set the unit system to specify the distance.</p> <p>Default Value: <code>Kilometers</code> </p>"""
    include_leg_geometry: NotRequired[
        "capo_location.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>Set to include the geometry details in the result for each path between a pair of positions.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    car_mode_options: NotRequired[
        "capo_location.types.calculate_route_car_mode_options.CalculateRouteCarModeOptions"
    ]
    """<p>Specifies route preferences when traveling by <code>Car</code>, such as avoiding routes that use ferries or tolls.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Car</code>.</p>"""
    truck_mode_options: NotRequired[
        "capo_location.types.calculate_route_truck_mode_options.CalculateRouteTruckModeOptions"
    ]
    """<p>Specifies route preferences when traveling by <code>Truck</code>, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Truck</code>.</p>"""
    arrival_time: NotRequired["capo_location.types.timestamp.Timestamp"]
    """<p>Specifies the desired time of arrival. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <note> <p>ArrivalTime is not supported Esri.</p> </note>"""
    optimize_for: NotRequired["capo_location.types.optimization_mode.OptimizationMode"]
    """<p>Specifies the distance to optimize for when calculating a route.</p>"""
    key: NotRequired["capo_location.types.api_key.ApiKey"]
    """<p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteRequest) -> dict:
    out: dict = {}
    import capo_location.types.position

    out["DeparturePosition"] = capo_location.types.position.serialize_json(
        value["departure_position"]
    )
    import capo_location.types.position

    out["DestinationPosition"] = capo_location.types.position.serialize_json(
        value["destination_position"]
    )
    if "waypoint_positions" in value:
        import capo_location.types.waypoint_position_list

        out["WaypointPositions"] = (
            capo_location.types.waypoint_position_list.serialize_json(
                value["waypoint_positions"]
            )
        )
    if "travel_mode" in value:
        out["TravelMode"] = value["travel_mode"]
    if "departure_time" in value:
        import capo_location.types.timestamp

        out["DepartureTime"] = capo_location.types.timestamp.serialize_json(
            value["departure_time"]
        )
    if "depart_now" in value:
        out["DepartNow"] = value["depart_now"]
    if "distance_unit" in value:
        out["DistanceUnit"] = value["distance_unit"]
    if "include_leg_geometry" in value:
        out["IncludeLegGeometry"] = value["include_leg_geometry"]
    if "car_mode_options" in value:
        import capo_location.types.calculate_route_car_mode_options

        out["CarModeOptions"] = (
            capo_location.types.calculate_route_car_mode_options.serialize_json(
                value["car_mode_options"]
            )
        )
    if "truck_mode_options" in value:
        import capo_location.types.calculate_route_truck_mode_options

        out["TruckModeOptions"] = (
            capo_location.types.calculate_route_truck_mode_options.serialize_json(
                value["truck_mode_options"]
            )
        )
    if "arrival_time" in value:
        import capo_location.types.timestamp

        out["ArrivalTime"] = capo_location.types.timestamp.serialize_json(
            value["arrival_time"]
        )
    if "optimize_for" in value:
        out["OptimizeFor"] = value["optimize_for"]
    return out


def deserialize_json(data: dict) -> CalculateRouteRequest:
    out: CalculateRouteRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeparturePosition") is not None:
        import capo_location.types.position

        out["departure_position"] = capo_location.types.position.deserialize_json(
            data["DeparturePosition"]
        )
    else:
        raise DeserializationError("CalculateRouteRequest.departure_position required")
    if data.get("DestinationPosition") is not None:
        import capo_location.types.position

        out["destination_position"] = capo_location.types.position.deserialize_json(
            data["DestinationPosition"]
        )
    else:
        raise DeserializationError(
            "CalculateRouteRequest.destination_position required"
        )
    if data.get("WaypointPositions") is not None:
        import capo_location.types.waypoint_position_list

        out["waypoint_positions"] = (
            capo_location.types.waypoint_position_list.deserialize_json(
                data["WaypointPositions"]
            )
        )
    if data.get("TravelMode") is not None:
        out["travel_mode"] = data["TravelMode"]
    if data.get("DepartureTime") is not None:
        import capo_location.types.timestamp

        out["departure_time"] = capo_location.types.timestamp.deserialize_json(
            data["DepartureTime"]
        )
    if data.get("DepartNow") is not None:
        out["depart_now"] = data["DepartNow"]
    if data.get("DistanceUnit") is not None:
        out["distance_unit"] = data["DistanceUnit"]
    if data.get("IncludeLegGeometry") is not None:
        out["include_leg_geometry"] = data["IncludeLegGeometry"]
    if data.get("CarModeOptions") is not None:
        import capo_location.types.calculate_route_car_mode_options

        out["car_mode_options"] = (
            capo_location.types.calculate_route_car_mode_options.deserialize_json(
                data["CarModeOptions"]
            )
        )
    if data.get("TruckModeOptions") is not None:
        import capo_location.types.calculate_route_truck_mode_options

        out["truck_mode_options"] = (
            capo_location.types.calculate_route_truck_mode_options.deserialize_json(
                data["TruckModeOptions"]
            )
        )
    if data.get("ArrivalTime") is not None:
        import capo_location.types.timestamp

        out["arrival_time"] = capo_location.types.timestamp.deserialize_json(
            data["ArrivalTime"]
        )
    if data.get("OptimizeFor") is not None:
        out["optimize_for"] = data["OptimizeFor"]
    return out
