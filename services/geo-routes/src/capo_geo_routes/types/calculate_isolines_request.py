"""Generated from Smithy shape ``com.amazonaws.georoutes#CalculateIsolinesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.api_key
    import capo_geo_routes.types.geometry_format
    import capo_geo_routes.types.isoline_allow_options
    import capo_geo_routes.types.isoline_avoidance_options
    import capo_geo_routes.types.isoline_destination_options
    import capo_geo_routes.types.isoline_granularity_options
    import capo_geo_routes.types.isoline_optimization_objective
    import capo_geo_routes.types.isoline_origin_options
    import capo_geo_routes.types.isoline_thresholds
    import capo_geo_routes.types.isoline_traffic_options
    import capo_geo_routes.types.isoline_travel_mode
    import capo_geo_routes.types.isoline_travel_mode_options
    import capo_geo_routes.types.position
    import capo_geo_routes.types.routing_objective
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.timestamp_with_timezone_offset


class CalculateIsolinesRequest(TypedDict, closed=True):
    allow: NotRequired[
        "capo_geo_routes.types.isoline_allow_options.IsolineAllowOptions"
    ]
    """<p>Enables special road types or features that should be considered for routing even if they might be restricted by default for the selected travel mode. These include high-occupancy vehicle and toll lanes.</p>"""
    arrival_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Determine areas from which <code>Destination</code> can be reached by this time, taking into account predicted traffic conditions and working backward to account for congestion patterns. This attribute cannot be used together with <code>DepartureTime</code> or <code>DepartNow</code>. Specified as an ISO-8601 timestamp with timezone offset.</p> <p>Time format: <code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    avoid: NotRequired[
        "capo_geo_routes.types.isoline_avoidance_options.IsolineAvoidanceOptions"
    ]
    """<p>Specifies road types, features, or areas to avoid (if possible) when calculating reachable areas. These are treated as preferences rather than strict constraints—if a route cannot be calculated without using an avoided feature, that avoidance preference may be ignored.</p>"""
    depart_now: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>When true, uses the current time as the departure time and takes current traffic conditions into account. This attribute cannot be used together with <code>DepartureTime</code> or <code>ArrivalTime</code>.</p>"""
    departure_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Determine areas that can be reached when departing at this time, taking into account predicted traffic conditions. This attribute cannot be used together with <code>ArrivalTime</code> or <code>DepartNow</code>. Specified as an ISO-8601 timestamp with timezone offset.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    destination: NotRequired["capo_geo_routes.types.position.Position"]
    """<p>An optional destination point, specified as <code>[longitude, latitude]</code> coordinates. When provided, the service calculates areas from which this destination can be reached within the specified thresholds. This reverses the usual isoline calculation to show areas that could reach your location, rather than areas you could reach from your location. Either <code>Origin</code> or <code>Destination</code> must be provided.</p>"""
    destination_options: NotRequired[
        "capo_geo_routes.types.isoline_destination_options.IsolineDestinationOptions"
    ]
    """<p>Options that control how the destination point is matched to the road network and how routes can approach it. These options help improve travel time accuracy by accounting for real-world access to the destination.</p>"""
    isoline_geometry_format: NotRequired[
        "capo_geo_routes.types.geometry_format.GeometryFormat"
    ]
    """<p>The format of the returned IsolineGeometry. </p> <p>Default value:<code>FlexiblePolyline</code> </p>"""
    isoline_granularity: NotRequired[
        "capo_geo_routes.types.isoline_granularity_options.IsolineGranularityOptions"
    ]
    """<p>Controls the detail level of the generated isolines. Higher granularity produces smoother shapes but requires more processing time and results in larger responses.</p>"""
    key: NotRequired["capo_geo_routes.types.api_key.ApiKey"]
    """<p>An Amazon Location Service API Key with access to this action. If omitted, the request must be signed using Signature Version 4.</p>"""
    optimize_isoline_for: NotRequired[
        "capo_geo_routes.types.isoline_optimization_objective.IsolineOptimizationObjective"
    ]
    """<p>Controls the trade-off between calculation speed and isoline precision. Choose <code> FastCalculation</code> for quicker results with less detail, <code>AccurateCalculation</code> for more precise results, or <code>BalancedCalculation</code> for a middle ground.</p> <p>Default value: <code>BalancedCalculation</code> </p>"""
    optimize_routing_for: NotRequired[
        "capo_geo_routes.types.routing_objective.RoutingObjective"
    ]
    """<p>Determines whether routes prioritize shortest travel time (<code>FastestRoute</code>) or shortest physical distance (<code>ShortestRoute</code>) when calculating reachable areas.</p> <p>Default value: <code>FastestRoute</code> </p>"""
    origin: NotRequired["capo_geo_routes.types.position.Position"]
    """<p>The starting point for isoline calculations, specified as <code>[longitude, latitude]</code> coordinates. For example, this could be a store location, service center, or any point from which you want to calculate reachable areas. Either <code>Origin</code> or <code>Destination</code> must be provided.</p>"""
    origin_options: NotRequired[
        "capo_geo_routes.types.isoline_origin_options.IsolineOriginOptions"
    ]
    """<p>Options that control how the origin point is matched to the road network and how routes can depart from it. These options help improve travel time accuracy by accounting for real-world access from the origin.</p>"""
    thresholds: "capo_geo_routes.types.isoline_thresholds.IsolineThresholds"
    """<p>The distance or time thresholds used to determine reachable areas. You can specify up to five thresholds (which all must be the same type) to calculate multiple isolines in a single request. For example, to determine the areas that are reachable within 10 and 20 minutes of the origin, specify time thresholds of 600 and 1200 seconds.</p> <p>You incur a calculation charge for each threshold. Using a large number of thresholds in a request can lead to unexpected charges. For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html">Routes pricing</a> in the <i>Amazon Location Service Developer Guide</i>.</p>"""
    traffic: NotRequired[
        "capo_geo_routes.types.isoline_traffic_options.IsolineTrafficOptions"
    ]
    """<p>Configures how real-time and historical traffic data affects isoline calculations. Traffic patterns can significantly impact reachable areas, especially during peak hours.</p>"""
    travel_mode: NotRequired[
        "capo_geo_routes.types.isoline_travel_mode.IsolineTravelMode"
    ]
    """<p>The mode of transportation to use for calculations. This affects which road types or features can be used, estimated speed, and the traffic levels that are applied.</p> <ul> <li> <p> <code>Car</code>—Standard passenger vehicle routing using roads accessible to cars</p> </li> <li> <p> <code>Pedestrian</code>—Walking routes using pedestrian paths, sidewalks, and crossings</p> </li> <li> <p> <code>Scooter</code>—Light two-wheeled vehicle routing using roads and paths accessible to scooters</p> </li> <li> <p> <code>Truck</code>—Commercial truck routing considering vehicle dimensions, weight restrictions, and hazardous material regulations</p> </li> </ul> <note> <p>The mode <code>Scooter</code> also applies to motorcycles; set this to <code>Scooter</code> when calculating isolines for motorcycles.</p> </note> <p>Default value: <code>Car</code> </p>"""
    travel_mode_options: NotRequired[
        "capo_geo_routes.types.isoline_travel_mode_options.IsolineTravelModeOptions"
    ]
    """<p>Additional attributes that refine how reachable areas are calculated based on specific vehicle characteristics. These options help produce more accurate results by accounting for real-world constraints and capabilities.</p> <p>For example:</p> <ul> <li> <p>For trucks (<code>Truck</code>), specify dimensions, weight limits, and hazardous cargo restrictions to ensure isolines only include roads that can physically and legally accommodate the vehicle</p> </li> <li> <p>For cars (<code>Car</code>), set maximum speed capabilities or indicate high-occupancy vehicle eligibility to better estimate reachable areas</p> </li> <li> <p>For scooters (<code>Scooter</code>), specify engine type and speed limitations to more accurately model their travel capabilities</p> </li> </ul> <p>Without these options, calculations use default assumptions that may not match your specific use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateIsolinesRequest) -> dict:
    out: dict = {}
    if "allow" in value:
        import capo_geo_routes.types.isoline_allow_options

        out["Allow"] = capo_geo_routes.types.isoline_allow_options.serialize_json(
            value["allow"]
        )
    if "arrival_time" in value:
        out["ArrivalTime"] = value["arrival_time"]
    if "avoid" in value:
        import capo_geo_routes.types.isoline_avoidance_options

        out["Avoid"] = capo_geo_routes.types.isoline_avoidance_options.serialize_json(
            value["avoid"]
        )
    if "depart_now" in value:
        out["DepartNow"] = value["depart_now"]
    if "departure_time" in value:
        out["DepartureTime"] = value["departure_time"]
    if "destination" in value:
        import capo_geo_routes.types.position

        out["Destination"] = capo_geo_routes.types.position.serialize_json(
            value["destination"]
        )
    if "destination_options" in value:
        import capo_geo_routes.types.isoline_destination_options

        out["DestinationOptions"] = (
            capo_geo_routes.types.isoline_destination_options.serialize_json(
                value["destination_options"]
            )
        )
    if "isoline_geometry_format" in value:
        import capo_geo_routes.types.geometry_format

        out["IsolineGeometryFormat"] = (
            capo_geo_routes.types.geometry_format.serialize_json(
                value["isoline_geometry_format"]
            )
        )
    if "isoline_granularity" in value:
        import capo_geo_routes.types.isoline_granularity_options

        out["IsolineGranularity"] = (
            capo_geo_routes.types.isoline_granularity_options.serialize_json(
                value["isoline_granularity"]
            )
        )
    if "optimize_isoline_for" in value:
        import capo_geo_routes.types.isoline_optimization_objective

        out["OptimizeIsolineFor"] = (
            capo_geo_routes.types.isoline_optimization_objective.serialize_json(
                value["optimize_isoline_for"]
            )
        )
    if "optimize_routing_for" in value:
        import capo_geo_routes.types.routing_objective

        out["OptimizeRoutingFor"] = (
            capo_geo_routes.types.routing_objective.serialize_json(
                value["optimize_routing_for"]
            )
        )
    if "origin" in value:
        import capo_geo_routes.types.position

        out["Origin"] = capo_geo_routes.types.position.serialize_json(value["origin"])
    if "origin_options" in value:
        import capo_geo_routes.types.isoline_origin_options

        out["OriginOptions"] = (
            capo_geo_routes.types.isoline_origin_options.serialize_json(
                value["origin_options"]
            )
        )
    import capo_geo_routes.types.isoline_thresholds

    out["Thresholds"] = capo_geo_routes.types.isoline_thresholds.serialize_json(
        value["thresholds"]
    )
    if "traffic" in value:
        import capo_geo_routes.types.isoline_traffic_options

        out["Traffic"] = capo_geo_routes.types.isoline_traffic_options.serialize_json(
            value["traffic"]
        )
    if "travel_mode" in value:
        import capo_geo_routes.types.isoline_travel_mode

        out["TravelMode"] = capo_geo_routes.types.isoline_travel_mode.serialize_json(
            value["travel_mode"]
        )
    if "travel_mode_options" in value:
        import capo_geo_routes.types.isoline_travel_mode_options

        out["TravelModeOptions"] = (
            capo_geo_routes.types.isoline_travel_mode_options.serialize_json(
                value["travel_mode_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> CalculateIsolinesRequest:
    out: CalculateIsolinesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Allow") is not None:
        import capo_geo_routes.types.isoline_allow_options

        out["allow"] = capo_geo_routes.types.isoline_allow_options.deserialize_json(
            data["Allow"]
        )
    if data.get("ArrivalTime") is not None:
        out["arrival_time"] = data["ArrivalTime"]
    if data.get("Avoid") is not None:
        import capo_geo_routes.types.isoline_avoidance_options

        out["avoid"] = capo_geo_routes.types.isoline_avoidance_options.deserialize_json(
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
    if data.get("DestinationOptions") is not None:
        import capo_geo_routes.types.isoline_destination_options

        out["destination_options"] = (
            capo_geo_routes.types.isoline_destination_options.deserialize_json(
                data["DestinationOptions"]
            )
        )
    if data.get("IsolineGeometryFormat") is not None:
        import capo_geo_routes.types.geometry_format

        out["isoline_geometry_format"] = (
            capo_geo_routes.types.geometry_format.deserialize_json(
                data["IsolineGeometryFormat"]
            )
        )
    if data.get("IsolineGranularity") is not None:
        import capo_geo_routes.types.isoline_granularity_options

        out["isoline_granularity"] = (
            capo_geo_routes.types.isoline_granularity_options.deserialize_json(
                data["IsolineGranularity"]
            )
        )
    if data.get("OptimizeIsolineFor") is not None:
        import capo_geo_routes.types.isoline_optimization_objective

        out["optimize_isoline_for"] = (
            capo_geo_routes.types.isoline_optimization_objective.deserialize_json(
                data["OptimizeIsolineFor"]
            )
        )
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
    if data.get("OriginOptions") is not None:
        import capo_geo_routes.types.isoline_origin_options

        out["origin_options"] = (
            capo_geo_routes.types.isoline_origin_options.deserialize_json(
                data["OriginOptions"]
            )
        )
    if data.get("Thresholds") is not None:
        import capo_geo_routes.types.isoline_thresholds

        out["thresholds"] = capo_geo_routes.types.isoline_thresholds.deserialize_json(
            data["Thresholds"]
        )
    else:
        raise DeserializationError("CalculateIsolinesRequest.thresholds required")
    if data.get("Traffic") is not None:
        import capo_geo_routes.types.isoline_traffic_options

        out["traffic"] = capo_geo_routes.types.isoline_traffic_options.deserialize_json(
            data["Traffic"]
        )
    if data.get("TravelMode") is not None:
        import capo_geo_routes.types.isoline_travel_mode

        out["travel_mode"] = capo_geo_routes.types.isoline_travel_mode.deserialize_json(
            data["TravelMode"]
        )
    if data.get("TravelModeOptions") is not None:
        import capo_geo_routes.types.isoline_travel_mode_options

        out["travel_mode_options"] = (
            capo_geo_routes.types.isoline_travel_mode_options.deserialize_json(
                data["TravelModeOptions"]
            )
        )
    return out
