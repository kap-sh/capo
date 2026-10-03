"""Generated from Smithy shape ``com.amazonaws.georoutes#CalculateRoutesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.api_key
    import capo_geo_routes.types.geometry_format
    import capo_geo_routes.types.language_tag_list
    import capo_geo_routes.types.measurement_system
    import capo_geo_routes.types.position
    import capo_geo_routes.types.route_allow_options
    import capo_geo_routes.types.route_avoidance_options
    import capo_geo_routes.types.route_destination_options
    import capo_geo_routes.types.route_driver_options
    import capo_geo_routes.types.route_exclusion_options
    import capo_geo_routes.types.route_leg_additional_feature_list
    import capo_geo_routes.types.route_origin_options
    import capo_geo_routes.types.route_span_additional_feature_list
    import capo_geo_routes.types.route_toll_options
    import capo_geo_routes.types.route_traffic_options
    import capo_geo_routes.types.route_travel_mode
    import capo_geo_routes.types.route_travel_mode_options
    import capo_geo_routes.types.route_travel_step_type
    import capo_geo_routes.types.route_waypoint_list
    import capo_geo_routes.types.routing_objective
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.timestamp_with_timezone_offset


class CalculateRoutesRequest(TypedDict, closed=True):
    allow: NotRequired["capo_geo_routes.types.route_allow_options.RouteAllowOptions"]
    """<p> Features that are allowed while calculating a route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    arrival_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p> Time of arrival at the destination. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    avoid: NotRequired[
        "capo_geo_routes.types.route_avoidance_options.RouteAvoidanceOptions"
    ]
    """<p> Features that are avoided while calculating a route. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, it violates the avoidance and the returned response produces a notice for the violation. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>ControlledAccessHighways</code>, <code>Ferries</code>, and <code>TollRoads</code> </p>"""
    depart_now: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Uses the current time as the time of departure.</p>"""
    departure_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Time of departure from the origin.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    destination: "capo_geo_routes.types.position.Position"
    """<p>The final position for the route. In the World Geodetic System (WGS 84) format: <code>[longitude, latitude]</code>.</p>"""
    destination_options: NotRequired[
        "capo_geo_routes.types.route_destination_options.RouteDestinationOptions"
    ]
    """<p> Destination related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    driver: NotRequired["capo_geo_routes.types.route_driver_options.RouteDriverOptions"]
    """<p> Driver related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    exclude: NotRequired[
        "capo_geo_routes.types.route_exclusion_options.RouteExclusionOptions"
    ]
    """<p> Features to be strictly excluded while calculating the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    instructions_measurement_system: NotRequired[
        "capo_geo_routes.types.measurement_system.MeasurementSystem"
    ]
    """<p>Measurement system to be used for instructions within steps in the response.</p>"""
    key: NotRequired["capo_geo_routes.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>"""
    languages: NotRequired["capo_geo_routes.types.language_tag_list.LanguageTagList"]
    """<p> List of languages for instructions within steps in the response. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <note> <p>Instructions in the requested language are returned only if they are available.</p> </note>"""
    leg_additional_features: NotRequired[
        "capo_geo_routes.types.route_leg_additional_feature_list.RouteLegAdditionalFeatureList"
    ]
    """<p> A list of optional additional parameters such as timezone that can be requested for each result. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>PassThroughWaypoints</code>, <code>Summary</code>, and <code>TravelStepInstructions</code> </p> <ul> <li> <p> <code>Elevation</code>: Retrieves the elevation information for each location.</p> </li> <li> <p> <code>Incidents</code>: Provides information on traffic incidents along the route.</p> </li> <li> <p> <code>PassThroughWaypoints</code>: Indicates waypoints that are passed through without stopping.</p> </li> <li> <p> <code>Summary</code>: Returns a summary of the route, including distance and duration.</p> </li> <li> <p> <code>Tolls</code>: Supplies toll cost information along the route.</p> </li> <li> <p> <code>TravelStepInstructions</code>: Provides step-by-step instructions for travel along the route.</p> </li> <li> <p> <code>TruckRoadTypes</code>: Returns information about road types suitable for trucks.</p> </li> <li> <p> <code>TypicalDuration</code>: Gives typical travel duration based on historical data.</p> </li> <li> <p> <code>Zones</code>: Specifies the time zone information for each waypoint.</p> </li> </ul>"""
    leg_geometry_format: NotRequired[
        "capo_geo_routes.types.geometry_format.GeometryFormat"
    ]
    """<p>Specifies the format of the geometry returned for each leg of the route. You can choose between two different geometry encoding formats.</p> <p> <code>FlexiblePolyline</code>: A compact and precise encoding format for the leg geometry. For more information on the format, see the GitHub repository for <a href="https://github.com/aws-geospatial/polyline">https://github.com/aws-geospatial/polyline</a>.</p> <p> <code>Simple</code>: A less compact encoding, which is easier to decode but may be less precise and result in larger payloads.</p>"""
    max_alternatives: NotRequired["int"]
    """<p>Maximum number of alternative routes to be provided in the response, if available. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only up to 3 alternative routes. </p>"""
    optimize_routing_for: NotRequired[
        "capo_geo_routes.types.routing_objective.RoutingObjective"
    ]
    """<p>Controls the trade-off between achieving the shortest travel time (<code>FastestRoute</code>) and achieving the shortest physical distance ((<code>ShortestRoute</code>) when calculating each route in the matrix.</p> <p>Default value: <code>FastestRoute</code> </p>"""
    origin: "capo_geo_routes.types.position.Position"
    """<p>The start position for the route in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    origin_options: NotRequired[
        "capo_geo_routes.types.route_origin_options.RouteOriginOptions"
    ]
    """<p> Specifies how the origin point should be matched to the road network and any routing constraints that apply when the traveler is departing the origin. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    span_additional_features: NotRequired[
        "capo_geo_routes.types.route_span_additional_feature_list.RouteSpanAdditionalFeatureList"
    ]
    """<p> A list of optional features such as <code>SpeedLimit</code> that can be requested for a Span. A span is a section of a Leg for which the requested features have the same values. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    tolls: NotRequired["capo_geo_routes.types.route_toll_options.RouteTollOptions"]
    """<p> Toll related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    traffic: NotRequired[
        "capo_geo_routes.types.route_traffic_options.RouteTrafficOptions"
    ]
    """<p> Traffic related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    travel_mode: NotRequired["capo_geo_routes.types.route_travel_mode.RouteTravelMode"]
    """<p> Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Car</code>, <code>Pedestrian</code>, and <code>Scooter</code> values. </p> <p>Default value: <code>Car</code> </p>"""
    travel_mode_options: NotRequired[
        "capo_geo_routes.types.route_travel_mode_options.RouteTravelModeOptions"
    ]
    """<p> Travel mode related options for the provided travel mode. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Car</code> and <code>Pedestrian</code> travel mode options. </p>"""
    travel_step_type: NotRequired[
        "capo_geo_routes.types.route_travel_step_type.RouteTravelStepType"
    ]
    """<p>Type of step returned by the response. <code>Default</code> provides basic steps intended for web based applications. <code>TurnByTurn</code> provides detailed instructions with more granularity intended for a turn based navigation system. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions <code>Default</code> does not return any steps. </p>"""
    waypoints: NotRequired[
        "capo_geo_routes.types.route_waypoint_list.RouteWaypointList"
    ]
    """<p> List of waypoints between the Origin and Destination. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions max length is <code>100</code>. </p> <p>Max length: <code>23</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRoutesRequest) -> dict:
    out: dict = {}
    if "allow" in value:
        import capo_geo_routes.types.route_allow_options

        out["Allow"] = capo_geo_routes.types.route_allow_options.serialize_json(
            value["allow"]
        )
    if "arrival_time" in value:
        out["ArrivalTime"] = value["arrival_time"]
    if "avoid" in value:
        import capo_geo_routes.types.route_avoidance_options

        out["Avoid"] = capo_geo_routes.types.route_avoidance_options.serialize_json(
            value["avoid"]
        )
    if "depart_now" in value:
        out["DepartNow"] = value["depart_now"]
    if "departure_time" in value:
        out["DepartureTime"] = value["departure_time"]
    import capo_geo_routes.types.position

    out["Destination"] = capo_geo_routes.types.position.serialize_json(
        value["destination"]
    )
    if "destination_options" in value:
        import capo_geo_routes.types.route_destination_options

        out["DestinationOptions"] = (
            capo_geo_routes.types.route_destination_options.serialize_json(
                value["destination_options"]
            )
        )
    if "driver" in value:
        import capo_geo_routes.types.route_driver_options

        out["Driver"] = capo_geo_routes.types.route_driver_options.serialize_json(
            value["driver"]
        )
    if "exclude" in value:
        import capo_geo_routes.types.route_exclusion_options

        out["Exclude"] = capo_geo_routes.types.route_exclusion_options.serialize_json(
            value["exclude"]
        )
    if "instructions_measurement_system" in value:
        import capo_geo_routes.types.measurement_system

        out["InstructionsMeasurementSystem"] = (
            capo_geo_routes.types.measurement_system.serialize_json(
                value["instructions_measurement_system"]
            )
        )
    if "languages" in value:
        import capo_geo_routes.types.language_tag_list

        out["Languages"] = capo_geo_routes.types.language_tag_list.serialize_json(
            value["languages"]
        )
    if "leg_additional_features" in value:
        import capo_geo_routes.types.route_leg_additional_feature_list

        out["LegAdditionalFeatures"] = (
            capo_geo_routes.types.route_leg_additional_feature_list.serialize_json(
                value["leg_additional_features"]
            )
        )
    if "leg_geometry_format" in value:
        import capo_geo_routes.types.geometry_format

        out["LegGeometryFormat"] = capo_geo_routes.types.geometry_format.serialize_json(
            value["leg_geometry_format"]
        )
    if "max_alternatives" in value:
        out["MaxAlternatives"] = value["max_alternatives"]
    if "optimize_routing_for" in value:
        import capo_geo_routes.types.routing_objective

        out["OptimizeRoutingFor"] = (
            capo_geo_routes.types.routing_objective.serialize_json(
                value["optimize_routing_for"]
            )
        )
    import capo_geo_routes.types.position

    out["Origin"] = capo_geo_routes.types.position.serialize_json(value["origin"])
    if "origin_options" in value:
        import capo_geo_routes.types.route_origin_options

        out["OriginOptions"] = (
            capo_geo_routes.types.route_origin_options.serialize_json(
                value["origin_options"]
            )
        )
    if "span_additional_features" in value:
        import capo_geo_routes.types.route_span_additional_feature_list

        out["SpanAdditionalFeatures"] = (
            capo_geo_routes.types.route_span_additional_feature_list.serialize_json(
                value["span_additional_features"]
            )
        )
    if "tolls" in value:
        import capo_geo_routes.types.route_toll_options

        out["Tolls"] = capo_geo_routes.types.route_toll_options.serialize_json(
            value["tolls"]
        )
    if "traffic" in value:
        import capo_geo_routes.types.route_traffic_options

        out["Traffic"] = capo_geo_routes.types.route_traffic_options.serialize_json(
            value["traffic"]
        )
    if "travel_mode" in value:
        import capo_geo_routes.types.route_travel_mode

        out["TravelMode"] = capo_geo_routes.types.route_travel_mode.serialize_json(
            value["travel_mode"]
        )
    if "travel_mode_options" in value:
        import capo_geo_routes.types.route_travel_mode_options

        out["TravelModeOptions"] = (
            capo_geo_routes.types.route_travel_mode_options.serialize_json(
                value["travel_mode_options"]
            )
        )
    if "travel_step_type" in value:
        import capo_geo_routes.types.route_travel_step_type

        out["TravelStepType"] = (
            capo_geo_routes.types.route_travel_step_type.serialize_json(
                value["travel_step_type"]
            )
        )
    if "waypoints" in value:
        import capo_geo_routes.types.route_waypoint_list

        out["Waypoints"] = capo_geo_routes.types.route_waypoint_list.serialize_json(
            value["waypoints"]
        )
    return out


def deserialize_json(data: dict) -> CalculateRoutesRequest:
    out: CalculateRoutesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Allow") is not None:
        import capo_geo_routes.types.route_allow_options

        out["allow"] = capo_geo_routes.types.route_allow_options.deserialize_json(
            data["Allow"]
        )
    if data.get("ArrivalTime") is not None:
        out["arrival_time"] = data["ArrivalTime"]
    if data.get("Avoid") is not None:
        import capo_geo_routes.types.route_avoidance_options

        out["avoid"] = capo_geo_routes.types.route_avoidance_options.deserialize_json(
            data["Avoid"]
        )
    if data.get("DepartNow") is not None:
        out["depart_now"] = data["DepartNow"]
    if data.get("DepartureTime") is not None:
        out["departure_time"] = data["DepartureTime"]
    if data.get("Destination") is not None:
        import capo_geo_routes.types.position

        out["destination"] = capo_geo_routes.types.position.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError("CalculateRoutesRequest.destination required")
    if data.get("DestinationOptions") is not None:
        import capo_geo_routes.types.route_destination_options

        out["destination_options"] = (
            capo_geo_routes.types.route_destination_options.deserialize_json(
                data["DestinationOptions"]
            )
        )
    if data.get("Driver") is not None:
        import capo_geo_routes.types.route_driver_options

        out["driver"] = capo_geo_routes.types.route_driver_options.deserialize_json(
            data["Driver"]
        )
    if data.get("Exclude") is not None:
        import capo_geo_routes.types.route_exclusion_options

        out["exclude"] = capo_geo_routes.types.route_exclusion_options.deserialize_json(
            data["Exclude"]
        )
    if data.get("InstructionsMeasurementSystem") is not None:
        import capo_geo_routes.types.measurement_system

        out["instructions_measurement_system"] = (
            capo_geo_routes.types.measurement_system.deserialize_json(
                data["InstructionsMeasurementSystem"]
            )
        )
    if data.get("Languages") is not None:
        import capo_geo_routes.types.language_tag_list

        out["languages"] = capo_geo_routes.types.language_tag_list.deserialize_json(
            data["Languages"]
        )
    if data.get("LegAdditionalFeatures") is not None:
        import capo_geo_routes.types.route_leg_additional_feature_list

        out["leg_additional_features"] = (
            capo_geo_routes.types.route_leg_additional_feature_list.deserialize_json(
                data["LegAdditionalFeatures"]
            )
        )
    if data.get("LegGeometryFormat") is not None:
        import capo_geo_routes.types.geometry_format

        out["leg_geometry_format"] = (
            capo_geo_routes.types.geometry_format.deserialize_json(
                data["LegGeometryFormat"]
            )
        )
    if data.get("MaxAlternatives") is not None:
        out["max_alternatives"] = data["MaxAlternatives"]
    if data.get("OptimizeRoutingFor") is not None:
        import capo_geo_routes.types.routing_objective

        out["optimize_routing_for"] = (
            capo_geo_routes.types.routing_objective.deserialize_json(
                data["OptimizeRoutingFor"]
            )
        )
    if data.get("Origin") is not None:
        import capo_geo_routes.types.position

        out["origin"] = capo_geo_routes.types.position.deserialize_json(data["Origin"])
    else:
        raise DeserializationError("CalculateRoutesRequest.origin required")
    if data.get("OriginOptions") is not None:
        import capo_geo_routes.types.route_origin_options

        out["origin_options"] = (
            capo_geo_routes.types.route_origin_options.deserialize_json(
                data["OriginOptions"]
            )
        )
    if data.get("SpanAdditionalFeatures") is not None:
        import capo_geo_routes.types.route_span_additional_feature_list

        out["span_additional_features"] = (
            capo_geo_routes.types.route_span_additional_feature_list.deserialize_json(
                data["SpanAdditionalFeatures"]
            )
        )
    if data.get("Tolls") is not None:
        import capo_geo_routes.types.route_toll_options

        out["tolls"] = capo_geo_routes.types.route_toll_options.deserialize_json(
            data["Tolls"]
        )
    if data.get("Traffic") is not None:
        import capo_geo_routes.types.route_traffic_options

        out["traffic"] = capo_geo_routes.types.route_traffic_options.deserialize_json(
            data["Traffic"]
        )
    if data.get("TravelMode") is not None:
        import capo_geo_routes.types.route_travel_mode

        out["travel_mode"] = capo_geo_routes.types.route_travel_mode.deserialize_json(
            data["TravelMode"]
        )
    if data.get("TravelModeOptions") is not None:
        import capo_geo_routes.types.route_travel_mode_options

        out["travel_mode_options"] = (
            capo_geo_routes.types.route_travel_mode_options.deserialize_json(
                data["TravelModeOptions"]
            )
        )
    if data.get("TravelStepType") is not None:
        import capo_geo_routes.types.route_travel_step_type

        out["travel_step_type"] = (
            capo_geo_routes.types.route_travel_step_type.deserialize_json(
                data["TravelStepType"]
            )
        )
    if data.get("Waypoints") is not None:
        import capo_geo_routes.types.route_waypoint_list

        out["waypoints"] = capo_geo_routes.types.route_waypoint_list.deserialize_json(
            data["Waypoints"]
        )
    return out
