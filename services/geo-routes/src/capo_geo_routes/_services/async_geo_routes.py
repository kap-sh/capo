"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutesService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_geo_routes._auth._signers
import capo_geo_routes._auth._sigv4
from capo_geo_routes._auth._identity import Credentials
from capo_geo_routes._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_geo_routes._auth._zapros_handler import AuthMiddleware
from capo_geo_routes._resources.routes_service.provider_resource import (
    AsyncProviderResource,
)
from capo_geo_routes._services._aws_config import aaws_config
from capo_geo_routes._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_geo_routes.types.api_key
    import capo_geo_routes.types.calculate_isolines_request
    import capo_geo_routes.types.calculate_isolines_response
    import capo_geo_routes.types.calculate_route_matrix_request
    import capo_geo_routes.types.calculate_route_matrix_response
    import capo_geo_routes.types.calculate_routes_request
    import capo_geo_routes.types.calculate_routes_response
    import capo_geo_routes.types.distance_meters
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
    import capo_geo_routes.types.language_tag_list
    import capo_geo_routes.types.measurement_system
    import capo_geo_routes.types.optimize_waypoints_request
    import capo_geo_routes.types.optimize_waypoints_response
    import capo_geo_routes.types.position
    import capo_geo_routes.types.road_snap_trace_point_list
    import capo_geo_routes.types.road_snap_travel_mode
    import capo_geo_routes.types.road_snap_travel_mode_options
    import capo_geo_routes.types.route_allow_options
    import capo_geo_routes.types.route_avoidance_options
    import capo_geo_routes.types.route_destination_options
    import capo_geo_routes.types.route_driver_options
    import capo_geo_routes.types.route_exclusion_options
    import capo_geo_routes.types.route_leg_additional_feature_list
    import capo_geo_routes.types.route_matrix_allow_options
    import capo_geo_routes.types.route_matrix_avoidance_options
    import capo_geo_routes.types.route_matrix_boundary
    import capo_geo_routes.types.route_matrix_destination_list
    import capo_geo_routes.types.route_matrix_exclusion_options
    import capo_geo_routes.types.route_matrix_origin_list
    import capo_geo_routes.types.route_matrix_traffic_options
    import capo_geo_routes.types.route_matrix_travel_mode
    import capo_geo_routes.types.route_matrix_travel_mode_options
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
    import capo_geo_routes.types.snap_to_roads_request
    import capo_geo_routes.types.snap_to_roads_response
    import capo_geo_routes.types.timestamp_with_timezone_offset
    import capo_geo_routes.types.waypoint_optimization_avoidance_options
    import capo_geo_routes.types.waypoint_optimization_clustering_options
    import capo_geo_routes.types.waypoint_optimization_destination_options
    import capo_geo_routes.types.waypoint_optimization_driver_options
    import capo_geo_routes.types.waypoint_optimization_exclusion_options
    import capo_geo_routes.types.waypoint_optimization_origin_options
    import capo_geo_routes.types.waypoint_optimization_sequencing_objective
    import capo_geo_routes.types.waypoint_optimization_traffic_options
    import capo_geo_routes.types.waypoint_optimization_travel_mode
    import capo_geo_routes.types.waypoint_optimization_travel_mode_options
    import capo_geo_routes.types.waypoint_optimization_waypoint_list


class AsyncGeoRoutesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncGeoRoutesClient:
    """A client for the ``GeoRoutes`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncGeoRoutesClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.provider_resource = AsyncProviderResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncGeoRoutesClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGeoRoutesClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def calculate_isolines(
        self,
        thresholds: "capo_geo_routes.types.isoline_thresholds.IsolineThresholds",
        *,
        config_overrides: Optional[AsyncGeoRoutesClientConfig] = None,
        allow: Optional[
            "capo_geo_routes.types.isoline_allow_options.IsolineAllowOptions"
        ] = None,
        arrival_time: Optional[
            "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
        ] = None,
        avoid: Optional[
            "capo_geo_routes.types.isoline_avoidance_options.IsolineAvoidanceOptions"
        ] = None,
        depart_now: Optional[
            "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        departure_time: Optional[
            "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
        ] = None,
        destination: Optional["capo_geo_routes.types.position.Position"] = None,
        destination_options: Optional[
            "capo_geo_routes.types.isoline_destination_options.IsolineDestinationOptions"
        ] = None,
        isoline_geometry_format: Optional[
            "capo_geo_routes.types.geometry_format.GeometryFormat"
        ] = None,
        isoline_granularity: Optional[
            "capo_geo_routes.types.isoline_granularity_options.IsolineGranularityOptions"
        ] = None,
        key: Optional["capo_geo_routes.types.api_key.ApiKey"] = None,
        optimize_isoline_for: Optional[
            "capo_geo_routes.types.isoline_optimization_objective.IsolineOptimizationObjective"
        ] = None,
        optimize_routing_for: Optional[
            "capo_geo_routes.types.routing_objective.RoutingObjective"
        ] = None,
        origin: Optional["capo_geo_routes.types.position.Position"] = None,
        origin_options: Optional[
            "capo_geo_routes.types.isoline_origin_options.IsolineOriginOptions"
        ] = None,
        traffic: Optional[
            "capo_geo_routes.types.isoline_traffic_options.IsolineTrafficOptions"
        ] = None,
        travel_mode: Optional[
            "capo_geo_routes.types.isoline_travel_mode.IsolineTravelMode"
        ] = None,
        travel_mode_options: Optional[
            "capo_geo_routes.types.isoline_travel_mode_options.IsolineTravelModeOptions"
        ] = None,
    ) -> "capo_geo_routes.types.calculate_isolines_response.CalculateIsolinesResponse":
        r"""<p>Calculates areas that can be reached within specified time or distance thresholds from a given point. For example, you can use this operation to determine the area within a 30-minute drive of a store location, find neighborhoods within walking distance of a school, or identify delivery zones based on drive time.</p> <p>Isolines (also known as isochrones for time-based calculations) are useful for various applications including:</p> <ul> <li> <p>Service area visualization - Show customers the area you can serve within promised delivery times</p> </li> <li> <p>Site selection - Analyze potential business locations based on population within travel distance</p> </li> <li> <p>Site selection - Determine areas that can be reached within specified response times</p> </li> </ul> <note> <p>Route preferences such as avoiding toll roads or ferries are treated as preferences rather than absolute restrictions. If a viable route cannot be calculated while honoring all preferences, some may be ignored.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/calculate-isolines.html\">Calculate isolines</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            allow: <p>Enables special road types or features that should be considered for routing even if they might be restricted by default for the selected travel mode. These include high-occupancy vehicle and toll lanes.</p>
            arrival_time: <p>Determine areas from which <code>Destination</code> can be reached by this time, taking into account predicted traffic conditions and working backward to account for congestion patterns. This attribute cannot be used together with <code>DepartureTime</code> or <code>DepartNow</code>. Specified as an ISO-8601 timestamp with timezone offset.</p> <p>Time format: <code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>
            avoid: <p>Specifies road types, features, or areas to avoid (if possible) when calculating reachable areas. These are treated as preferences rather than strict constraints—if a route cannot be calculated without using an avoided feature, that avoidance preference may be ignored.</p>
            depart_now: <p>When true, uses the current time as the departure time and takes current traffic conditions into account. This attribute cannot be used together with <code>DepartureTime</code> or <code>ArrivalTime</code>.</p>
            departure_time: <p>Determine areas that can be reached when departing at this time, taking into account predicted traffic conditions. This attribute cannot be used together with <code>ArrivalTime</code> or <code>DepartNow</code>. Specified as an ISO-8601 timestamp with timezone offset.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>
            destination: <p>An optional destination point, specified as <code>[longitude, latitude]</code> coordinates. When provided, the service calculates areas from which this destination can be reached within the specified thresholds. This reverses the usual isoline calculation to show areas that could reach your location, rather than areas you could reach from your location. Either <code>Origin</code> or <code>Destination</code> must be provided.</p>
            destination_options: <p>Options that control how the destination point is matched to the road network and how routes can approach it. These options help improve travel time accuracy by accounting for real-world access to the destination.</p>
            isoline_geometry_format: <p>The format of the returned IsolineGeometry. </p> <p>Default value:<code>FlexiblePolyline</code> </p>
            isoline_granularity: <p>Controls the detail level of the generated isolines. Higher granularity produces smoother shapes but requires more processing time and results in larger responses.</p>
            key: <p>An Amazon Location Service API Key with access to this action. If omitted, the request must be signed using Signature Version 4.</p>
            optimize_isoline_for: <p>Controls the trade-off between calculation speed and isoline precision. Choose <code> FastCalculation</code> for quicker results with less detail, <code>AccurateCalculation</code> for more precise results, or <code>BalancedCalculation</code> for a middle ground.</p> <p>Default value: <code>BalancedCalculation</code> </p>
            optimize_routing_for: <p>Determines whether routes prioritize shortest travel time (<code>FastestRoute</code>) or shortest physical distance (<code>ShortestRoute</code>) when calculating reachable areas.</p> <p>Default value: <code>FastestRoute</code> </p>
            origin: <p>The starting point for isoline calculations, specified as <code>[longitude, latitude]</code> coordinates. For example, this could be a store location, service center, or any point from which you want to calculate reachable areas. Either <code>Origin</code> or <code>Destination</code> must be provided.</p>
            origin_options: <p>Options that control how the origin point is matched to the road network and how routes can depart from it. These options help improve travel time accuracy by accounting for real-world access from the origin.</p>
            thresholds: <p>The distance or time thresholds used to determine reachable areas. You can specify up to five thresholds (which all must be the same type) to calculate multiple isolines in a single request. For example, to determine the areas that are reachable within 10 and 20 minutes of the origin, specify time thresholds of 600 and 1200 seconds.</p> <p>You incur a calculation charge for each threshold. Using a large number of thresholds in a request can lead to unexpected charges. For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html\">Routes pricing</a> in the <i>Amazon Location Service Developer Guide</i>.</p>
            traffic: <p>Configures how real-time and historical traffic data affects isoline calculations. Traffic patterns can significantly impact reachable areas, especially during peak hours.</p>
            travel_mode: <p>The mode of transportation to use for calculations. This affects which road types or features can be used, estimated speed, and the traffic levels that are applied.</p> <ul> <li> <p> <code>Car</code>—Standard passenger vehicle routing using roads accessible to cars</p> </li> <li> <p> <code>Pedestrian</code>—Walking routes using pedestrian paths, sidewalks, and crossings</p> </li> <li> <p> <code>Scooter</code>—Light two-wheeled vehicle routing using roads and paths accessible to scooters</p> </li> <li> <p> <code>Truck</code>—Commercial truck routing considering vehicle dimensions, weight restrictions, and hazardous material regulations</p> </li> </ul> <note> <p>The mode <code>Scooter</code> also applies to motorcycles; set this to <code>Scooter</code> when calculating isolines for motorcycles.</p> </note> <p>Default value: <code>Car</code> </p>
            travel_mode_options: <p>Additional attributes that refine how reachable areas are calculated based on specific vehicle characteristics. These options help produce more accurate results by accounting for real-world constraints and capabilities.</p> <p>For example:</p> <ul> <li> <p>For trucks (<code>Truck</code>), specify dimensions, weight limits, and hazardous cargo restrictions to ensure isolines only include roads that can physically and legally accommodate the vehicle</p> </li> <li> <p>For cars (<code>Car</code>), set maximum speed capabilities or indicate high-occupancy vehicle eligibility to better estimate reachable areas</p> </li> <li> <p>For scooters (<code>Scooter</code>), specify engine type and speed limitations to more accurately model their travel capabilities</p> </li> </ul> <p>Without these options, calculations use default assumptions that may not match your specific use case.</p>

        Raises:
            capo_geo_routes.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_routes.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_routes.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_routes.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_routes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_geo_routes.types.calculate_isolines_request.CalculateIsolinesRequest]",
        ) -> AsyncOperationResponse[
            "capo_geo_routes.types.calculate_isolines_response.CalculateIsolinesResponse"
        ]:
            import capo_geo_routes._operations.routes_service.calculate_isolines

            (
                output,
                http_response,
            ) = await capo_geo_routes._operations.routes_service.calculate_isolines.async_calculate_isolines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_routes.types.calculate_isolines_request.CalculateIsolinesRequest = {
            "thresholds": thresholds
        }
        if allow is not None:
            input_["allow"] = allow
        if arrival_time is not None:
            input_["arrival_time"] = arrival_time
        if avoid is not None:
            input_["avoid"] = avoid
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if destination is not None:
            input_["destination"] = destination
        if destination_options is not None:
            input_["destination_options"] = destination_options
        if isoline_geometry_format is not None:
            input_["isoline_geometry_format"] = isoline_geometry_format
        if isoline_granularity is not None:
            input_["isoline_granularity"] = isoline_granularity
        if key is not None:
            input_["key"] = key
        if optimize_isoline_for is not None:
            input_["optimize_isoline_for"] = optimize_isoline_for
        if optimize_routing_for is not None:
            input_["optimize_routing_for"] = optimize_routing_for
        if origin is not None:
            input_["origin"] = origin
        if origin_options is not None:
            input_["origin_options"] = origin_options
        if traffic is not None:
            input_["traffic"] = traffic
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if travel_mode_options is not None:
            input_["travel_mode_options"] = travel_mode_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def calculate_route_matrix(
        self,
        destinations: "capo_geo_routes.types.route_matrix_destination_list.RouteMatrixDestinationList",
        origins: "capo_geo_routes.types.route_matrix_origin_list.RouteMatrixOriginList",
        *,
        config_overrides: Optional[AsyncGeoRoutesClientConfig] = None,
        allow: Optional[
            "capo_geo_routes.types.route_matrix_allow_options.RouteMatrixAllowOptions"
        ] = None,
        avoid: Optional[
            "capo_geo_routes.types.route_matrix_avoidance_options.RouteMatrixAvoidanceOptions"
        ] = None,
        depart_now: Optional[
            "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        departure_time: Optional[
            "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
        ] = None,
        exclude: Optional[
            "capo_geo_routes.types.route_matrix_exclusion_options.RouteMatrixExclusionOptions"
        ] = None,
        key: Optional["capo_geo_routes.types.api_key.ApiKey"] = None,
        optimize_routing_for: Optional[
            "capo_geo_routes.types.routing_objective.RoutingObjective"
        ] = None,
        routing_boundary: Optional[
            "capo_geo_routes.types.route_matrix_boundary.RouteMatrixBoundary"
        ] = None,
        traffic: Optional[
            "capo_geo_routes.types.route_matrix_traffic_options.RouteMatrixTrafficOptions"
        ] = None,
        travel_mode: Optional[
            "capo_geo_routes.types.route_matrix_travel_mode.RouteMatrixTravelMode"
        ] = None,
        travel_mode_options: Optional[
            "capo_geo_routes.types.route_matrix_travel_mode_options.RouteMatrixTravelModeOptions"
        ] = None,
    ) -> "capo_geo_routes.types.calculate_route_matrix_response.CalculateRouteMatrixResponse":
        r"""<p> Use <code>CalculateRouteMatrix</code> to compute results for all pairs of Origins to Destinations. Each row corresponds to one entry in Origins. Each entry in the row corresponds to the route from that entry in Origins to an entry in Destinations positions.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html\">Calculate route matrix</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            allow: <p>Features that are allowed while calculating a route.</p>
            avoid: <p> Features that are avoided while calculating a route. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, it violates the avoidance and the returned response produces a notice for the violation. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>TollRoads</code>, <code>Ferries</code>, and <code>ControlledAccessHighways</code>. </p>
            depart_now: <p>Uses the current time as the time of departure.</p>
            departure_time: <p>Time of departure from the origin.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>
            destinations: <p>List of destinations for the route in World Geodetic System (WGS 84) format: [longitude, latitude].</p> <note> <p>Route calculations are billed for each origin and destination pair. If you use a large matrix of origins and destinations, your costs will increase accordingly. For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html\">Routes pricing</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>The maximum number of destinations depends on the routing boundary configuration:</p> <ul> <li> <p>With <code>RoutingBoundary.Geometry</code> set: maximum 500 destinations</p> </li> <li> <p>With <code>RoutingBoundary.Unbounded</code> set to <code>true</code>: maximum 100 destinations</p> </li> <li> <p>For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers in <code>ap-southeast-1</code> and <code>ap-southeast-5</code>: maximum 350 destinations</p> </li> </ul> <p>The total matrix size (origins × destinations) must not exceed:</p> <ul> <li> <p>With <code>RoutingBoundary.Geometry</code>: 160,000</p> </li> <li> <p>With <code>RoutingBoundary.Unbounded</code>: 100</p> </li> <li> <p>For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers in <code>ap-southeast-1</code> and <code>ap-southeast-5</code>: 122,500</p> </li> </ul>
            exclude: <p> Features to be strictly excluded while calculating the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>
            optimize_routing_for: <p>Controls the trade-off between finding the shortest travel time (<code>FastestRoute</code>) and the shortest distance (<code>ShortestRoute</code>) when calculating reachable areas.</p> <p>Default value: <code>FastestRoute</code> </p>
            origins: <p>List of origins for the route in World Geodetic System (WGS 84) format: [longitude, latitude].</p> <note> <p>Route calculations are billed for each origin and destination pair. Using a large amount of Origins in a request can lead you to incur unexpected charges. For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html\">Routes pricing</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>The maximum number of origins depends on the routing boundary configuration:</p> <ul> <li> <p>With <code>RoutingBoundary.Geometry</code> set: maximum 500 origins</p> </li> <li> <p>With <code>RoutingBoundary.Unbounded</code> set to <code>true</code>: maximum 15 origins</p> </li> <li> <p>For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers in <code>ap-southeast-1</code> and <code>ap-southeast-5</code>: maximum 350 origins</p> </li> </ul> <p>The total matrix size (origins × destinations) must not exceed:</p> <ul> <li> <p>With <code>RoutingBoundary.Geometry</code>: 160,000</p> </li> <li> <p>With <code>RoutingBoundary.Unbounded</code>: 100</p> </li> <li> <p>For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers in <code>ap-southeast-1</code> and <code>ap-southeast-5</code>: 122,500</p> </li> </ul>
            routing_boundary: <p> Boundary within which the matrix is to be calculated. All data, origins and destinations outside the boundary are considered invalid. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Unbounded</code> set to <code>true</code>. </p> <p>Default value: <code>Unbounded set to true</code> </p> <note> <p>When <code>AutoCircle</code> is set in the request, the response routing boundary will return <code>Circle</code> derived from the <code>AutoCircle</code> settings.</p> </note>
            traffic: <p> Traffic related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            travel_mode: <p> Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Car</code>, <code>Pedestrian</code>, and <code>Scooter</code>. </p> <p>Default value: <code>Car</code> </p>
            travel_mode_options: <p> Travel mode related options for the provided travel mode. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>

        Raises:
            capo_geo_routes.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_routes.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_routes.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_routes.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_routes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_geo_routes.types.calculate_route_matrix_request.CalculateRouteMatrixRequest]",
        ) -> AsyncOperationResponse[
            "capo_geo_routes.types.calculate_route_matrix_response.CalculateRouteMatrixResponse"
        ]:
            import capo_geo_routes._operations.routes_service.calculate_route_matrix

            (
                output,
                http_response,
            ) = await capo_geo_routes._operations.routes_service.calculate_route_matrix.async_calculate_route_matrix(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_routes.types.calculate_route_matrix_request.CalculateRouteMatrixRequest = {
            "destinations": destinations,
            "origins": origins,
        }
        if allow is not None:
            input_["allow"] = allow
        if avoid is not None:
            input_["avoid"] = avoid
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if exclude is not None:
            input_["exclude"] = exclude
        if key is not None:
            input_["key"] = key
        if optimize_routing_for is not None:
            input_["optimize_routing_for"] = optimize_routing_for
        if routing_boundary is not None:
            input_["routing_boundary"] = routing_boundary
        if traffic is not None:
            input_["traffic"] = traffic
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if travel_mode_options is not None:
            input_["travel_mode_options"] = travel_mode_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def calculate_routes(
        self,
        destination: "capo_geo_routes.types.position.Position",
        origin: "capo_geo_routes.types.position.Position",
        *,
        config_overrides: Optional[AsyncGeoRoutesClientConfig] = None,
        allow: Optional[
            "capo_geo_routes.types.route_allow_options.RouteAllowOptions"
        ] = None,
        arrival_time: Optional[
            "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
        ] = None,
        avoid: Optional[
            "capo_geo_routes.types.route_avoidance_options.RouteAvoidanceOptions"
        ] = None,
        depart_now: Optional[
            "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        departure_time: Optional[
            "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
        ] = None,
        destination_options: Optional[
            "capo_geo_routes.types.route_destination_options.RouteDestinationOptions"
        ] = None,
        driver: Optional[
            "capo_geo_routes.types.route_driver_options.RouteDriverOptions"
        ] = None,
        exclude: Optional[
            "capo_geo_routes.types.route_exclusion_options.RouteExclusionOptions"
        ] = None,
        instructions_measurement_system: Optional[
            "capo_geo_routes.types.measurement_system.MeasurementSystem"
        ] = None,
        key: Optional["capo_geo_routes.types.api_key.ApiKey"] = None,
        languages: Optional[
            "capo_geo_routes.types.language_tag_list.LanguageTagList"
        ] = None,
        leg_additional_features: Optional[
            "capo_geo_routes.types.route_leg_additional_feature_list.RouteLegAdditionalFeatureList"
        ] = None,
        leg_geometry_format: Optional[
            "capo_geo_routes.types.geometry_format.GeometryFormat"
        ] = None,
        max_alternatives: Optional[int] = None,
        optimize_routing_for: Optional[
            "capo_geo_routes.types.routing_objective.RoutingObjective"
        ] = None,
        origin_options: Optional[
            "capo_geo_routes.types.route_origin_options.RouteOriginOptions"
        ] = None,
        span_additional_features: Optional[
            "capo_geo_routes.types.route_span_additional_feature_list.RouteSpanAdditionalFeatureList"
        ] = None,
        tolls: Optional[
            "capo_geo_routes.types.route_toll_options.RouteTollOptions"
        ] = None,
        traffic: Optional[
            "capo_geo_routes.types.route_traffic_options.RouteTrafficOptions"
        ] = None,
        travel_mode: Optional[
            "capo_geo_routes.types.route_travel_mode.RouteTravelMode"
        ] = None,
        travel_mode_options: Optional[
            "capo_geo_routes.types.route_travel_mode_options.RouteTravelModeOptions"
        ] = None,
        travel_step_type: Optional[
            "capo_geo_routes.types.route_travel_step_type.RouteTravelStepType"
        ] = None,
        waypoints: Optional[
            "capo_geo_routes.types.route_waypoint_list.RouteWaypointList"
        ] = None,
    ) -> "capo_geo_routes.types.calculate_routes_response.CalculateRoutesResponse":
        r"""<p> <code>CalculateRoutes</code> computes routes given the following required parameters: <code>Origin</code> and <code>Destination</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes.html\">Calculate routes</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            allow: <p> Features that are allowed while calculating a route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            arrival_time: <p> Time of arrival at the destination. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>
            avoid: <p> Features that are avoided while calculating a route. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, it violates the avoidance and the returned response produces a notice for the violation. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>ControlledAccessHighways</code>, <code>Ferries</code>, and <code>TollRoads</code> </p>
            depart_now: <p>Uses the current time as the time of departure.</p>
            departure_time: <p>Time of departure from the origin.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>
            destination: <p>The final position for the route. In the World Geodetic System (WGS 84) format: <code>[longitude, latitude]</code>.</p>
            destination_options: <p> Destination related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            driver: <p> Driver related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            exclude: <p> Features to be strictly excluded while calculating the route. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            instructions_measurement_system: <p>Measurement system to be used for instructions within steps in the response.</p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>
            languages: <p> List of languages for instructions within steps in the response. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <note> <p>Instructions in the requested language are returned only if they are available.</p> </note>
            leg_additional_features: <p> A list of optional additional parameters such as timezone that can be requested for each result. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>PassThroughWaypoints</code>, <code>Summary</code>, and <code>TravelStepInstructions</code> </p> <ul> <li> <p> <code>Elevation</code>: Retrieves the elevation information for each location.</p> </li> <li> <p> <code>Incidents</code>: Provides information on traffic incidents along the route.</p> </li> <li> <p> <code>PassThroughWaypoints</code>: Indicates waypoints that are passed through without stopping.</p> </li> <li> <p> <code>Summary</code>: Returns a summary of the route, including distance and duration.</p> </li> <li> <p> <code>Tolls</code>: Supplies toll cost information along the route.</p> </li> <li> <p> <code>TravelStepInstructions</code>: Provides step-by-step instructions for travel along the route.</p> </li> <li> <p> <code>TruckRoadTypes</code>: Returns information about road types suitable for trucks.</p> </li> <li> <p> <code>TypicalDuration</code>: Gives typical travel duration based on historical data.</p> </li> <li> <p> <code>Zones</code>: Specifies the time zone information for each waypoint.</p> </li> </ul>
            leg_geometry_format: <p>Specifies the format of the geometry returned for each leg of the route. You can choose between two different geometry encoding formats.</p> <p> <code>FlexiblePolyline</code>: A compact and precise encoding format for the leg geometry. For more information on the format, see the GitHub repository for <a href=\"https://github.com/aws-geospatial/polyline\">https://github.com/aws-geospatial/polyline</a>.</p> <p> <code>Simple</code>: A less compact encoding, which is easier to decode but may be less precise and result in larger payloads.</p>
            max_alternatives: <p>Maximum number of alternative routes to be provided in the response, if available. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only up to 3 alternative routes. </p>
            optimize_routing_for: <p>Controls the trade-off between achieving the shortest travel time (<code>FastestRoute</code>) and achieving the shortest physical distance ((<code>ShortestRoute</code>) when calculating each route in the matrix.</p> <p>Default value: <code>FastestRoute</code> </p>
            origin: <p>The start position for the route in World Geodetic System (WGS 84) format: [longitude, latitude].</p>
            origin_options: <p> Specifies how the origin point should be matched to the road network and any routing constraints that apply when the traveler is departing the origin. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            span_additional_features: <p> A list of optional features such as <code>SpeedLimit</code> that can be requested for a Span. A span is a section of a Leg for which the requested features have the same values. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            tolls: <p> Toll related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            traffic: <p> Traffic related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            travel_mode: <p> Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Car</code>, <code>Pedestrian</code>, and <code>Scooter</code> values. </p> <p>Default value: <code>Car</code> </p>
            travel_mode_options: <p> Travel mode related options for the provided travel mode. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only <code>Car</code> and <code>Pedestrian</code> travel mode options. </p>
            travel_step_type: <p>Type of step returned by the response. <code>Default</code> provides basic steps intended for web based applications. <code>TurnByTurn</code> provides detailed instructions with more granularity intended for a turn based navigation system. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions <code>Default</code> does not return any steps. </p>
            waypoints: <p> List of waypoints between the Origin and Destination. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions max length is <code>100</code>. </p> <p>Max length: <code>23</code> </p>

        Raises:
            capo_geo_routes.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_routes.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_routes.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_routes.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_routes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_geo_routes.types.calculate_routes_request.CalculateRoutesRequest]",
        ) -> AsyncOperationResponse[
            "capo_geo_routes.types.calculate_routes_response.CalculateRoutesResponse"
        ]:
            import capo_geo_routes._operations.routes_service.calculate_routes

            (
                output,
                http_response,
            ) = await capo_geo_routes._operations.routes_service.calculate_routes.async_calculate_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_routes.types.calculate_routes_request.CalculateRoutesRequest = {
            "destination": destination,
            "origin": origin,
        }
        if allow is not None:
            input_["allow"] = allow
        if arrival_time is not None:
            input_["arrival_time"] = arrival_time
        if avoid is not None:
            input_["avoid"] = avoid
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if destination_options is not None:
            input_["destination_options"] = destination_options
        if driver is not None:
            input_["driver"] = driver
        if exclude is not None:
            input_["exclude"] = exclude
        if instructions_measurement_system is not None:
            input_["instructions_measurement_system"] = instructions_measurement_system
        if key is not None:
            input_["key"] = key
        if languages is not None:
            input_["languages"] = languages
        if leg_additional_features is not None:
            input_["leg_additional_features"] = leg_additional_features
        if leg_geometry_format is not None:
            input_["leg_geometry_format"] = leg_geometry_format
        if max_alternatives is not None:
            input_["max_alternatives"] = max_alternatives
        if optimize_routing_for is not None:
            input_["optimize_routing_for"] = optimize_routing_for
        if origin_options is not None:
            input_["origin_options"] = origin_options
        if span_additional_features is not None:
            input_["span_additional_features"] = span_additional_features
        if tolls is not None:
            input_["tolls"] = tolls
        if traffic is not None:
            input_["traffic"] = traffic
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if travel_mode_options is not None:
            input_["travel_mode_options"] = travel_mode_options
        if travel_step_type is not None:
            input_["travel_step_type"] = travel_step_type
        if waypoints is not None:
            input_["waypoints"] = waypoints

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def optimize_waypoints(
        self,
        origin: "capo_geo_routes.types.position.Position",
        *,
        config_overrides: Optional[AsyncGeoRoutesClientConfig] = None,
        avoid: Optional[
            "capo_geo_routes.types.waypoint_optimization_avoidance_options.WaypointOptimizationAvoidanceOptions"
        ] = None,
        clustering: Optional[
            "capo_geo_routes.types.waypoint_optimization_clustering_options.WaypointOptimizationClusteringOptions"
        ] = None,
        departure_time: Optional[
            "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
        ] = None,
        destination: Optional["capo_geo_routes.types.position.Position"] = None,
        destination_options: Optional[
            "capo_geo_routes.types.waypoint_optimization_destination_options.WaypointOptimizationDestinationOptions"
        ] = None,
        driver: Optional[
            "capo_geo_routes.types.waypoint_optimization_driver_options.WaypointOptimizationDriverOptions"
        ] = None,
        exclude: Optional[
            "capo_geo_routes.types.waypoint_optimization_exclusion_options.WaypointOptimizationExclusionOptions"
        ] = None,
        key: Optional["capo_geo_routes.types.api_key.ApiKey"] = None,
        optimize_sequencing_for: Optional[
            "capo_geo_routes.types.waypoint_optimization_sequencing_objective.WaypointOptimizationSequencingObjective"
        ] = None,
        origin_options: Optional[
            "capo_geo_routes.types.waypoint_optimization_origin_options.WaypointOptimizationOriginOptions"
        ] = None,
        traffic: Optional[
            "capo_geo_routes.types.waypoint_optimization_traffic_options.WaypointOptimizationTrafficOptions"
        ] = None,
        travel_mode: Optional[
            "capo_geo_routes.types.waypoint_optimization_travel_mode.WaypointOptimizationTravelMode"
        ] = None,
        travel_mode_options: Optional[
            "capo_geo_routes.types.waypoint_optimization_travel_mode_options.WaypointOptimizationTravelModeOptions"
        ] = None,
        waypoints: Optional[
            "capo_geo_routes.types.waypoint_optimization_waypoint_list.WaypointOptimizationWaypointList"
        ] = None,
    ) -> "capo_geo_routes.types.optimize_waypoints_response.OptimizeWaypointsResponse":
        r"""<p> <code>OptimizeWaypoints</code> calculates the optimal order to travel between a set of waypoints to minimize either the travel time or the distance travelled during the journey, based on road network restrictions and the traffic pattern data.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/actions-optimize-waypoints.html\">Optimize waypoints</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            avoid: <p>Features that are avoided. Avoidance is on a best-case basis. If an avoidance can't be satisfied for a particular case, this setting is ignored.</p>
            clustering: <p>Clustering allows you to specify how nearby waypoints can be clustered to improve the optimized sequence.</p>
            departure_time: <p>Departure time from the waypoint.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>
            destination: <p>The final position for the route in the World Geodetic System (WGS 84) format: <code>[longitude, latitude]</code>.</p>
            destination_options: <p>Destination related options.</p>
            driver: <p>Driver related options.</p>
            exclude: <p>Features to be strictly excluded while calculating the route.</p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>
            optimize_sequencing_for: <p>Specifies the optimization criteria for the calculated sequence.</p> <p>Default value: <code>FastestRoute</code>.</p>
            origin: <p>The start position for the route in World Geodetic System (WGS 84) format: [longitude, latitude].</p>
            origin_options: <p>Origin related options.</p>
            traffic: <p>Traffic-related options.</p>
            travel_mode: <p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>Default value: <code>Car</code> </p>
            travel_mode_options: <p>Travel mode related options for the provided travel mode.</p>
            waypoints: <p>List of waypoints between the <code>Origin</code> and <code>Destination</code>, in World Geodetic System (WGS 84) format: [longitude, latitude].</p> <p>The maximum number of waypoints allowed per request:</p> <ul> <li> <p>Maximum 50 waypoints per request</p> </li> <li> <p>Maximum 20 waypoints when using constraints (<code>AccessHours</code>, <code>AppointmentTime</code>, <code>ServiceDuration</code>, <code>Heading</code>, <code>SideOfStreet</code>, <code>Before</code>)</p> </li> </ul>

        Raises:
            capo_geo_routes.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_routes.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_routes.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_routes.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_routes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_geo_routes.types.optimize_waypoints_request.OptimizeWaypointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_geo_routes.types.optimize_waypoints_response.OptimizeWaypointsResponse"
        ]:
            import capo_geo_routes._operations.routes_service.optimize_waypoints

            (
                output,
                http_response,
            ) = await capo_geo_routes._operations.routes_service.optimize_waypoints.async_optimize_waypoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_routes.types.optimize_waypoints_request.OptimizeWaypointsRequest = {
            "origin": origin
        }
        if avoid is not None:
            input_["avoid"] = avoid
        if clustering is not None:
            input_["clustering"] = clustering
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if destination is not None:
            input_["destination"] = destination
        if destination_options is not None:
            input_["destination_options"] = destination_options
        if driver is not None:
            input_["driver"] = driver
        if exclude is not None:
            input_["exclude"] = exclude
        if key is not None:
            input_["key"] = key
        if optimize_sequencing_for is not None:
            input_["optimize_sequencing_for"] = optimize_sequencing_for
        if origin_options is not None:
            input_["origin_options"] = origin_options
        if traffic is not None:
            input_["traffic"] = traffic
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if travel_mode_options is not None:
            input_["travel_mode_options"] = travel_mode_options
        if waypoints is not None:
            input_["waypoints"] = waypoints

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def snap_to_roads(
        self,
        trace_points: "capo_geo_routes.types.road_snap_trace_point_list.RoadSnapTracePointList",
        *,
        config_overrides: Optional[AsyncGeoRoutesClientConfig] = None,
        key: Optional["capo_geo_routes.types.api_key.ApiKey"] = None,
        snapped_geometry_format: Optional[
            "capo_geo_routes.types.geometry_format.GeometryFormat"
        ] = None,
        snap_radius: Optional[
            "capo_geo_routes.types.distance_meters.DistanceMeters"
        ] = None,
        travel_mode: Optional[
            "capo_geo_routes.types.road_snap_travel_mode.RoadSnapTravelMode"
        ] = None,
        travel_mode_options: Optional[
            "capo_geo_routes.types.road_snap_travel_mode_options.RoadSnapTravelModeOptions"
        ] = None,
    ) -> "capo_geo_routes.types.snap_to_roads_response.SnapToRoadsResponse":
        r"""<p> <code>SnapToRoads</code> matches GPS trace to roads most likely traveled on.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/snap-to-roads.html\">Snap to Roads</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>
            snapped_geometry_format: <p>Chooses what the returned SnappedGeometry format should be.</p> <p>Default value: <code>FlexiblePolyline</code> </p>
            snap_radius: <p>The radius around the provided tracepoint that is considered for snapping.</p> <p> <b>Unit</b>: <code>meters</code> </p> <p>Default value: <code>300</code> </p>
            trace_points: <p>List of trace points to be snapped onto the road network.</p>
            travel_mode: <p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>Default value: <code>Car</code> </p>
            travel_mode_options: <p>Travel mode related options for the provided travel mode.</p>

        Raises:
            capo_geo_routes.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_routes.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_routes.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_routes.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_routes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_geo_routes.types.snap_to_roads_request.SnapToRoadsRequest]",
        ) -> AsyncOperationResponse[
            "capo_geo_routes.types.snap_to_roads_response.SnapToRoadsResponse"
        ]:
            import capo_geo_routes._operations.routes_service.snap_to_roads

            (
                output,
                http_response,
            ) = await capo_geo_routes._operations.routes_service.snap_to_roads.async_snap_to_roads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_routes.types.snap_to_roads_request.SnapToRoadsRequest = {
            "trace_points": trace_points
        }
        if key is not None:
            input_["key"] = key
        if snapped_geometry_format is not None:
            input_["snapped_geometry_format"] = snapped_geometry_format
        if snap_radius is not None:
            input_["snap_radius"] = snap_radius
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if travel_mode_options is not None:
            input_["travel_mode_options"] = travel_mode_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
