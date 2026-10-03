"""Generated from Smithy shape ``com.amazonaws.georoutes#CalculateRouteMatrixRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.api_key
    import capo_geo_routes.types.route_matrix_allow_options
    import capo_geo_routes.types.route_matrix_avoidance_options
    import capo_geo_routes.types.route_matrix_boundary
    import capo_geo_routes.types.route_matrix_destination_list
    import capo_geo_routes.types.route_matrix_exclusion_options
    import capo_geo_routes.types.route_matrix_origin_list
    import capo_geo_routes.types.route_matrix_traffic_options
    import capo_geo_routes.types.route_matrix_travel_mode
    import capo_geo_routes.types.route_matrix_travel_mode_options
    import capo_geo_routes.types.routing_objective
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.timestamp_with_timezone_offset


class CalculateRouteMatrixRequest(TypedDict, closed=True):
    allow: NotRequired[
        "capo_geo_routes.types.route_matrix_allow_options.RouteMatrixAllowOptions"
    ]
    """<p>Features that are allowed while calculating a route.</p>"""
    avoid: NotRequired[
        "capo_geo_routes.types.route_matrix_avoidance_options.RouteMatrixAvoidanceOptions"
    ]
    """<p> Features that are avoided while calculating a route. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, it violates the avoidance and the returned response produces a notice for the violation. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>TollRoads</code>, <code>Ferries</code>, and <code>ControlledAccessHighways</code>. </p>"""
    depart_now: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Uses the current time as the time of departure.</p>"""
    departure_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Time of departure from the origin.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    destinations: (
        "capo_geo_routes.types.route_matrix_destination_list.RouteMatrixDestinationList"
    )
    """<p>List of destinations for the route in World Geodetic System (WGS 84) format: [longitude, latitude].</p> <note> <p>Route calculations are billed for each origin and destination pair. If you use a large matrix of origins and destinations, your costs will increase accordingly. For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html">Routes pricing</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>The maximum number of destinations depends on the routing boundary configuration:</p> <ul> <li> <p>With <code>RoutingBoundary.Geometry</code> set: maximum 500 destinations</p> </li> <li> <p>With <code>RoutingBoundary.Unbounded</code> set to <code>true</code>: maximum 100 destinations</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers in <code>ap-southeast-1</code> and <code>ap-southeast-5</code>: maximum 350 destinations</p> </li> </ul> <p>The total matrix size (origins × destinations) must not exceed:</p> <ul> <li> <p>With <code>RoutingBoundary.Geometry</code>: 160,000</p> </li> <li> <p>With <code>RoutingBoundary.Unbounded</code>: 100</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers in <code>ap-southeast-1</code> and <code>ap-southeast-5</code>: 122,500</p> </li> </ul>"""
    exclude: NotRequired[
        "capo_geo_routes.types.route_matrix_exclusion_options.RouteMatrixExclusionOptions"
    ]
    """<p> Features to be strictly excluded while calculating the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    key: NotRequired["capo_geo_routes.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>"""
    optimize_routing_for: NotRequired[
        "capo_geo_routes.types.routing_objective.RoutingObjective"
    ]
    """<p>Controls the trade-off between finding the shortest travel time (<code>FastestRoute</code>) and the shortest distance (<code>ShortestRoute</code>) when calculating reachable areas.</p> <p>Default value: <code>FastestRoute</code> </p>"""
    origins: "capo_geo_routes.types.route_matrix_origin_list.RouteMatrixOriginList"
    """<p>List of origins for the route in World Geodetic System (WGS 84) format: [longitude, latitude].</p> <note> <p>Route calculations are billed for each origin and destination pair. Using a large amount of Origins in a request can lead you to incur unexpected charges. For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html">Routes pricing</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>The maximum number of origins depends on the routing boundary configuration:</p> <ul> <li> <p>With <code>RoutingBoundary.Geometry</code> set: maximum 500 origins</p> </li> <li> <p>With <code>RoutingBoundary.Unbounded</code> set to <code>true</code>: maximum 15 origins</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers in <code>ap-southeast-1</code> and <code>ap-southeast-5</code>: maximum 350 origins</p> </li> </ul> <p>The total matrix size (origins × destinations) must not exceed:</p> <ul> <li> <p>With <code>RoutingBoundary.Geometry</code>: 160,000</p> </li> <li> <p>With <code>RoutingBoundary.Unbounded</code>: 100</p> </li> <li> <p>For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers in <code>ap-southeast-1</code> and <code>ap-southeast-5</code>: 122,500</p> </li> </ul>"""
    routing_boundary: NotRequired[
        "capo_geo_routes.types.route_matrix_boundary.RouteMatrixBoundary"
    ]
    """<p> Boundary within which the matrix is to be calculated. All data, origins and destinations outside the boundary are considered invalid. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Unbounded</code> set to <code>true</code>. </p> <p>Default value: <code>Unbounded set to true</code> </p> <note> <p>When <code>AutoCircle</code> is set in the request, the response routing boundary will return <code>Circle</code> derived from the <code>AutoCircle</code> settings.</p> </note>"""
    traffic: NotRequired[
        "capo_geo_routes.types.route_matrix_traffic_options.RouteMatrixTrafficOptions"
    ]
    """<p> Traffic related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    travel_mode: NotRequired[
        "capo_geo_routes.types.route_matrix_travel_mode.RouteMatrixTravelMode"
    ]
    """<p> Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Car</code>, <code>Pedestrian</code>, and <code>Scooter</code>. </p> <p>Default value: <code>Car</code> </p>"""
    travel_mode_options: NotRequired[
        "capo_geo_routes.types.route_matrix_travel_mode_options.RouteMatrixTravelModeOptions"
    ]
    """<p> Travel mode related options for the provided travel mode. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteMatrixRequest) -> dict:
    out: dict = {}
    if "allow" in value:
        import capo_geo_routes.types.route_matrix_allow_options

        out["Allow"] = capo_geo_routes.types.route_matrix_allow_options.serialize_json(
            value["allow"]
        )
    if "avoid" in value:
        import capo_geo_routes.types.route_matrix_avoidance_options

        out["Avoid"] = (
            capo_geo_routes.types.route_matrix_avoidance_options.serialize_json(
                value["avoid"]
            )
        )
    if "depart_now" in value:
        out["DepartNow"] = value["depart_now"]
    if "departure_time" in value:
        out["DepartureTime"] = value["departure_time"]
    import capo_geo_routes.types.route_matrix_destination_list

    out["Destinations"] = (
        capo_geo_routes.types.route_matrix_destination_list.serialize_json(
            value["destinations"]
        )
    )
    if "exclude" in value:
        import capo_geo_routes.types.route_matrix_exclusion_options

        out["Exclude"] = (
            capo_geo_routes.types.route_matrix_exclusion_options.serialize_json(
                value["exclude"]
            )
        )
    if "optimize_routing_for" in value:
        import capo_geo_routes.types.routing_objective

        out["OptimizeRoutingFor"] = (
            capo_geo_routes.types.routing_objective.serialize_json(
                value["optimize_routing_for"]
            )
        )
    import capo_geo_routes.types.route_matrix_origin_list

    out["Origins"] = capo_geo_routes.types.route_matrix_origin_list.serialize_json(
        value["origins"]
    )
    if "routing_boundary" in value:
        import capo_geo_routes.types.route_matrix_boundary

        out["RoutingBoundary"] = (
            capo_geo_routes.types.route_matrix_boundary.serialize_json(
                value["routing_boundary"]
            )
        )
    if "traffic" in value:
        import capo_geo_routes.types.route_matrix_traffic_options

        out["Traffic"] = (
            capo_geo_routes.types.route_matrix_traffic_options.serialize_json(
                value["traffic"]
            )
        )
    if "travel_mode" in value:
        import capo_geo_routes.types.route_matrix_travel_mode

        out["TravelMode"] = (
            capo_geo_routes.types.route_matrix_travel_mode.serialize_json(
                value["travel_mode"]
            )
        )
    if "travel_mode_options" in value:
        import capo_geo_routes.types.route_matrix_travel_mode_options

        out["TravelModeOptions"] = (
            capo_geo_routes.types.route_matrix_travel_mode_options.serialize_json(
                value["travel_mode_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> CalculateRouteMatrixRequest:
    out: CalculateRouteMatrixRequest = {}  # type: ignore[typeddict-item]
    if data.get("Allow") is not None:
        import capo_geo_routes.types.route_matrix_allow_options

        out["allow"] = (
            capo_geo_routes.types.route_matrix_allow_options.deserialize_json(
                data["Allow"]
            )
        )
    if data.get("Avoid") is not None:
        import capo_geo_routes.types.route_matrix_avoidance_options

        out["avoid"] = (
            capo_geo_routes.types.route_matrix_avoidance_options.deserialize_json(
                data["Avoid"]
            )
        )
    if data.get("DepartNow") is not None:
        out["depart_now"] = data["DepartNow"]
    if data.get("DepartureTime") is not None:
        out["departure_time"] = data["DepartureTime"]
    if data.get("Destinations") is not None:
        import capo_geo_routes.types.route_matrix_destination_list

        out["destinations"] = (
            capo_geo_routes.types.route_matrix_destination_list.deserialize_json(
                data["Destinations"]
            )
        )
    else:
        raise DeserializationError("CalculateRouteMatrixRequest.destinations required")
    if data.get("Exclude") is not None:
        import capo_geo_routes.types.route_matrix_exclusion_options

        out["exclude"] = (
            capo_geo_routes.types.route_matrix_exclusion_options.deserialize_json(
                data["Exclude"]
            )
        )
    if data.get("OptimizeRoutingFor") is not None:
        import capo_geo_routes.types.routing_objective

        out["optimize_routing_for"] = (
            capo_geo_routes.types.routing_objective.deserialize_json(
                data["OptimizeRoutingFor"]
            )
        )
    if data.get("Origins") is not None:
        import capo_geo_routes.types.route_matrix_origin_list

        out["origins"] = (
            capo_geo_routes.types.route_matrix_origin_list.deserialize_json(
                data["Origins"]
            )
        )
    else:
        raise DeserializationError("CalculateRouteMatrixRequest.origins required")
    if data.get("RoutingBoundary") is not None:
        import capo_geo_routes.types.route_matrix_boundary

        out["routing_boundary"] = (
            capo_geo_routes.types.route_matrix_boundary.deserialize_json(
                data["RoutingBoundary"]
            )
        )
    if data.get("Traffic") is not None:
        import capo_geo_routes.types.route_matrix_traffic_options

        out["traffic"] = (
            capo_geo_routes.types.route_matrix_traffic_options.deserialize_json(
                data["Traffic"]
            )
        )
    if data.get("TravelMode") is not None:
        import capo_geo_routes.types.route_matrix_travel_mode

        out["travel_mode"] = (
            capo_geo_routes.types.route_matrix_travel_mode.deserialize_json(
                data["TravelMode"]
            )
        )
    if data.get("TravelModeOptions") is not None:
        import capo_geo_routes.types.route_matrix_travel_mode_options

        out["travel_mode_options"] = (
            capo_geo_routes.types.route_matrix_travel_mode_options.deserialize_json(
                data["TravelModeOptions"]
            )
        )
    return out
