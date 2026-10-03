"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteMatrixRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.calculate_route_car_mode_options
    import capo_location.types.calculate_route_truck_mode_options
    import capo_location.types.distance_unit
    import capo_location.types.position_list
    import capo_location.types.resource_name
    import capo_location.types.sensitive_boolean
    import capo_location.types.timestamp
    import capo_location.types.travel_mode


class CalculateRouteMatrixRequest(TypedDict, closed=True):
    calculator_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the route calculator resource that you want to use to calculate the route matrix. </p>"""
    departure_positions: "capo_location.types.position_list.PositionList"
    """<p>The list of departure (origin) positions for the route matrix. An array of points, each of which is itself a 2-value array defined in <a href="https://earth-info.nga.mil/GandG/wgs84/index.html">WGS 84</a> format: <code>[longitude, latitude]</code>. For example, <code>[-123.115, 49.285]</code>.</p> <important> <p>Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits"> Position restrictions</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </important> <note> <p>For route calculators that use Esri as the data provider, if you specify a departure that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html"> moves the position to the nearest road</a>. The snapped value is available in the result in <code>SnappedDeparturePositions</code>.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>"""
    destination_positions: "capo_location.types.position_list.PositionList"
    """<p>The list of destination positions for the route matrix. An array of points, each of which is itself a 2-value array defined in <a href="https://earth-info.nga.mil/GandG/wgs84/index.html">WGS 84</a> format: <code>[longitude, latitude]</code>. For example, <code>[-122.339, 47.615]</code> </p> <important> <p>Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits"> Position restrictions</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </important> <note> <p>For route calculators that use Esri as the data provider, if you specify a destination that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html"> moves the position to the nearest road</a>. The snapped value is available in the result in <code>SnappedDestinationPositions</code>.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>"""
    travel_mode: NotRequired["capo_location.types.travel_mode.TravelMode"]
    """<p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>The <code>TravelMode</code> you specify also determines how you specify route preferences: </p> <ul> <li> <p>If traveling by <code>Car</code> use the <code>CarModeOptions</code> parameter.</p> </li> <li> <p>If traveling by <code>Truck</code> use the <code>TruckModeOptions</code> parameter.</p> </li> </ul> <note> <p> <code>Bicycle</code> or <code>Motorcycle</code> are only valid when using <code>Grab</code> as a data provider, and only within Southeast Asia.</p> <p> <code>Truck</code> is not available for Grab.</p> <p>For more information about using Grab as a data provider, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>Default Value: <code>Car</code> </p>"""
    departure_time: NotRequired["capo_location.types.timestamp.Timestamp"]
    """<p>Specifies the desired time of departure. Uses the given time to calculate the route matrix. You can't set both <code>DepartureTime</code> and <code>DepartNow</code>. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.</p> <note> <p>Setting a departure time in the past returns a <code>400 ValidationException</code> error.</p> </note> <ul> <li> <p>In <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>"""
    depart_now: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Sets the time of departure as the current time. Uses the current time to calculate the route matrix. You can't set both <code>DepartureTime</code> and <code>DepartNow</code>. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    distance_unit: NotRequired["capo_location.types.distance_unit.DistanceUnit"]
    """<p>Set the unit system to specify the distance.</p> <p>Default Value: <code>Kilometers</code> </p>"""
    car_mode_options: NotRequired[
        "capo_location.types.calculate_route_car_mode_options.CalculateRouteCarModeOptions"
    ]
    """<p>Specifies route preferences when traveling by <code>Car</code>, such as avoiding routes that use ferries or tolls.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Car</code>.</p>"""
    truck_mode_options: NotRequired[
        "capo_location.types.calculate_route_truck_mode_options.CalculateRouteTruckModeOptions"
    ]
    """<p>Specifies route preferences when traveling by <code>Truck</code>, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Truck</code>.</p>"""
    key: NotRequired["capo_location.types.api_key.ApiKey"]
    """<p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteMatrixRequest) -> dict:
    out: dict = {}
    import capo_location.types.position_list

    out["DeparturePositions"] = capo_location.types.position_list.serialize_json(
        value["departure_positions"]
    )
    import capo_location.types.position_list

    out["DestinationPositions"] = capo_location.types.position_list.serialize_json(
        value["destination_positions"]
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
    return out


def deserialize_json(data: dict) -> CalculateRouteMatrixRequest:
    out: CalculateRouteMatrixRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeparturePositions") is not None:
        import capo_location.types.position_list

        out["departure_positions"] = capo_location.types.position_list.deserialize_json(
            data["DeparturePositions"]
        )
    else:
        raise DeserializationError(
            "CalculateRouteMatrixRequest.departure_positions required"
        )
    if data.get("DestinationPositions") is not None:
        import capo_location.types.position_list

        out["destination_positions"] = (
            capo_location.types.position_list.deserialize_json(
                data["DestinationPositions"]
            )
        )
    else:
        raise DeserializationError(
            "CalculateRouteMatrixRequest.destination_positions required"
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
    return out
