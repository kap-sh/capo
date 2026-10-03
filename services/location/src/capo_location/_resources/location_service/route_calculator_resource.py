from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_location._auth._signers
import capo_location._auth._sigv4
from capo_location._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.calculate_route_car_mode_options
    import capo_location.types.calculate_route_matrix_request
    import capo_location.types.calculate_route_matrix_response
    import capo_location.types.calculate_route_request
    import capo_location.types.calculate_route_response
    import capo_location.types.calculate_route_truck_mode_options
    import capo_location.types.create_route_calculator_request
    import capo_location.types.create_route_calculator_response
    import capo_location.types.delete_route_calculator_request
    import capo_location.types.delete_route_calculator_response
    import capo_location.types.describe_route_calculator_request
    import capo_location.types.describe_route_calculator_response
    import capo_location.types.distance_unit
    import capo_location.types.list_route_calculators_request
    import capo_location.types.list_route_calculators_response
    import capo_location.types.list_route_calculators_response_entry
    import capo_location.types.optimization_mode
    import capo_location.types.position
    import capo_location.types.position_list
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.sensitive_boolean
    import capo_location.types.tag_map
    import capo_location.types.timestamp
    import capo_location.types.token
    import capo_location.types.travel_mode
    import capo_location.types.update_route_calculator_request
    import capo_location.types.update_route_calculator_response
    import capo_location.types.waypoint_position_list
    from capo_location._services.async_location import (
        AsyncLocationClient,
        AsyncLocationClientConfig,
    )
    from capo_location._services.location import LocationClient, LocationClientConfig


class RouteCalculatorResource:
    def __init__(self, service: LocationClient) -> None:
        self._service = service

    def put(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        data_source: str,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_route_calculator_response.CreateRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>CreateRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Creates a route calculator resource in your Amazon Web Services account.</p> <p>You can send requests to a route calculator resource to estimate travel time, distance, and get directions. A route calculator sources traffic and road network data from your chosen data provider.</p> <note> <p>If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the <a href="http://aws.amazon.com/service-terms">Amazon Web Services service terms</a> for more details.</p> </note>

        Args:
            calculator_name: <p>The name of the route calculator resource. </p> <p>Requirements:</p> <ul> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9) , hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique Route calculator resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleRouteCalculator</code>.</p> </li> </ul>
            data_source: <p>Specifies the data provider of traffic and road network data.</p> <note> <p>This field is case-sensitive. Enter the valid values as shown. For example, entering <code>HERE</code> returns an error.</p> </note> <p>Valid values include:</p> <ul> <li> <p> <code>Esri</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/esri.html">Esri</a>'s coverage in your region of interest, see <a href="https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm">Esri details on street networks and traffic coverage</a>.</p> <p>Route calculators that use Esri as a data source only calculate routes that are shorter than 400 km.</p> </li> <li> <p> <code>Grab</code> – Grab provides routing functionality for Southeast Asia. For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a>' coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area">GrabMaps countries and areas covered</a>.</p> </li> <li> <p> <code>Here</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/HERE.html">HERE Technologies</a>' coverage in your region of interest, see <a href="https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html">HERE car routing coverage</a> and <a href="https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html">HERE truck routing coverage</a>.</p> </li> </ul> <p>For additional information , see <a href="https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html">Data providers</a> on the <i>Amazon Location Service Developer Guide</i>.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>The optional description for the route calculator resource.</p>
            tags: <p>Applies one or more tags to the route calculator resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.</p> <ul> <li> <p>For example: { <code>"tag1" : "value1"</code>, <code>"tag2" : "value2"</code>}</p> </li> </ul> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_route_calculator_request.CreateRouteCalculatorRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_route_calculator_response.CreateRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.create_route_calculator

            output, http_response = (
                capo_location._operations.location_service.create_route_calculator.create_route_calculator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.create_route_calculator_request.CreateRouteCalculatorRequest = {
            "calculator_name": calculator_name,
            "data_source": data_source,
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_route_calculator_response.DescribeRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DescribeRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the route calculator resource details.</p>

        Args:
            calculator_name: <p>The name of the route calculator resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_route_calculator_request.DescribeRouteCalculatorRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_route_calculator_response.DescribeRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.describe_route_calculator

            output, http_response = (
                capo_location._operations.location_service.describe_route_calculator.describe_route_calculator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.describe_route_calculator_request.DescribeRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_location.types.update_route_calculator_response.UpdateRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>UpdateRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Updates the specified properties for a given route calculator resource.</p>

        Args:
            calculator_name: <p>The name of the route calculator resource to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>Updates the description for the route calculator resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_route_calculator_request.UpdateRouteCalculatorRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_route_calculator_response.UpdateRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.update_route_calculator

            output, http_response = (
                capo_location._operations.location_service.update_route_calculator.update_route_calculator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.update_route_calculator_request.UpdateRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.delete_route_calculator_response.DeleteRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DeleteRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Deletes a route calculator resource from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently.</p> </note>

        Args:
            calculator_name: <p>The name of the route calculator resource to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_route_calculator_request.DeleteRouteCalculatorRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_route_calculator_response.DeleteRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.delete_route_calculator

            output, http_response = (
                capo_location._operations.location_service.delete_route_calculator.delete_route_calculator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.delete_route_calculator_request.DeleteRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_route_calculators_response.ListRouteCalculatorsResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>ListRouteCalculators</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Lists route calculator resources in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional maximum number of results returned in a single call.</p> <p>Default Value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default Value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_route_calculators_request.ListRouteCalculatorsRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_route_calculators_response.ListRouteCalculatorsResponse"
        ]:
            import capo_location._operations.location_service.list_route_calculators

            output, http_response = (
                capo_location._operations.location_service.list_route_calculators.list_route_calculators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_route_calculators_request.ListRouteCalculatorsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def calculate_route(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        departure_position: "capo_location.types.position.Position",
        destination_position: "capo_location.types.position.Position",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        waypoint_positions: Optional[
            "capo_location.types.waypoint_position_list.WaypointPositionList"
        ] = None,
        travel_mode: Optional["capo_location.types.travel_mode.TravelMode"] = None,
        departure_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        depart_now: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
        include_leg_geometry: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        car_mode_options: Optional[
            "capo_location.types.calculate_route_car_mode_options.CalculateRouteCarModeOptions"
        ] = None,
        truck_mode_options: Optional[
            "capo_location.types.calculate_route_truck_mode_options.CalculateRouteTruckModeOptions"
        ] = None,
        arrival_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        optimize_for: Optional[
            "capo_location.types.optimization_mode.OptimizationMode"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.calculate_route_response.CalculateRouteResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_CalculateRoutes.html"> <code>CalculateRoutes</code> </a> or <a href="/location/latest/APIReference/API_CalculateIsolines.html"> <code>CalculateIsolines</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>CalculateRoute</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>CalculateRoutes</code> operation gives better results for point-to-point routing, while the version 2 <code>CalculateIsolines</code> operation adds support for calculating service areas and travel time envelopes.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route.html">Calculates a route</a> given the following required parameters: <code>DeparturePosition</code> and <code>DestinationPosition</code>. Requires that you first <a href="https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html">create a route calculator resource</a>.</p> <p>By default, a request that doesn't specify a departure time uses the best time of day to travel with the best traffic conditions when calculating the route.</p> <p>Additional options include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html">Specifying a departure time</a> using either <code>DepartureTime</code> or <code>DepartNow</code>. This calculates a route based on predictive traffic data at the given time. </p> <note> <p>You can't specify both <code>DepartureTime</code> and <code>DepartNow</code> in a single request. Specifying both parameters returns a validation error.</p> </note> </li> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html">Specifying a travel mode</a> using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in <code>CarModeOptions</code> if traveling by <code>Car</code>, or <code>TruckModeOptions</code> if traveling by <code>Truck</code>.</p> <note> <p>If you specify <code>walking</code> for the travel mode and your data provider is Esri, the start and destination must be within 40km.</p> </note> </li> </ul>

        Args:
            calculator_name: <p>The name of the route calculator resource that you want to use to calculate the route. </p>
            departure_position: <p>The start position for the route. Defined in <a href="https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84">World Geodetic System (WGS 84)</a> format: <code>[longitude, latitude]</code>.</p> <ul> <li> <p>For example, <code>[-123.115, 49.285]</code> </p> </li> </ul> <note> <p>If you specify a departure that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a <code>400 RoutesValidationException</code> error.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            destination_position: <p>The finish position for the route. Defined in <a href="https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84">World Geodetic System (WGS 84)</a> format: <code>[longitude, latitude]</code>.</p> <ul> <li> <p> For example, <code>[-122.339, 47.615]</code> </p> </li> </ul> <note> <p>If you specify a destination that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. </p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            waypoint_positions: <p>Specifies an ordered list of up to 23 intermediate positions to include along a route between the departure position and destination position. </p> <ul> <li> <p>For example, from the <code>DeparturePosition</code> <code>[-123.115, 49.285]</code>, the route follows the order that the waypoint positions are given <code>[[-122.757, 49.0021],[-122.349, 47.620]]</code> </p> </li> </ul> <note> <p>If you specify a waypoint position that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. </p> <p>Specifying more than 23 waypoints returns a <code>400 ValidationException</code> error.</p> <p>If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a <code>400 RoutesValidationException</code> error.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            travel_mode: <p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. You can choose <code>Car</code>, <code>Truck</code>, <code>Walking</code>, <code>Bicycle</code> or <code>Motorcycle</code> as options for the <code>TravelMode</code>.</p> <note> <p> <code>Bicycle</code> and <code>Motorcycle</code> are only valid when using Grab as a data provider, and only within Southeast Asia.</p> <p> <code>Truck</code> is not available for Grab.</p> <p>For more details on the using Grab for routing, including areas of coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>The <code>TravelMode</code> you specify also determines how you specify route preferences: </p> <ul> <li> <p>If traveling by <code>Car</code> use the <code>CarModeOptions</code> parameter.</p> </li> <li> <p>If traveling by <code>Truck</code> use the <code>TruckModeOptions</code> parameter.</p> </li> </ul> <p>Default Value: <code>Car</code> </p>
            departure_time: <p>Specifies the desired time of departure. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <ul> <li> <p>In <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>
            depart_now: <p>Sets the time of departure as the current time. Uses the current time to calculate a route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            distance_unit: <p>Set the unit system to specify the distance.</p> <p>Default Value: <code>Kilometers</code> </p>
            include_leg_geometry: <p>Set to include the geometry details in the result for each path between a pair of positions.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            car_mode_options: <p>Specifies route preferences when traveling by <code>Car</code>, such as avoiding routes that use ferries or tolls.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Car</code>.</p>
            truck_mode_options: <p>Specifies route preferences when traveling by <code>Truck</code>, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Truck</code>.</p>
            arrival_time: <p>Specifies the desired time of arrival. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <note> <p>ArrivalTime is not supported Esri.</p> </note>
            optimize_for: <p>Specifies the distance to optimize for when calculating a route.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.calculate_route_request.CalculateRouteRequest]",
        ) -> OperationResponse[
            "capo_location.types.calculate_route_response.CalculateRouteResponse"
        ]:
            import capo_location._operations.location_service.calculate_route

            output, http_response = (
                capo_location._operations.location_service.calculate_route.calculate_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.calculate_route_request.CalculateRouteRequest = {
            "calculator_name": calculator_name,
            "departure_position": departure_position,
            "destination_position": destination_position,
        }
        if waypoint_positions is not None:
            input_["waypoint_positions"] = waypoint_positions
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit
        if include_leg_geometry is not None:
            input_["include_leg_geometry"] = include_leg_geometry
        if car_mode_options is not None:
            input_["car_mode_options"] = car_mode_options
        if truck_mode_options is not None:
            input_["truck_mode_options"] = truck_mode_options
        if arrival_time is not None:
            input_["arrival_time"] = arrival_time
        if optimize_for is not None:
            input_["optimize_for"] = optimize_for
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def calculate_route_matrix(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        departure_positions: "capo_location.types.position_list.PositionList",
        destination_positions: "capo_location.types.position_list.PositionList",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        travel_mode: Optional["capo_location.types.travel_mode.TravelMode"] = None,
        departure_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        depart_now: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
        car_mode_options: Optional[
            "capo_location.types.calculate_route_car_mode_options.CalculateRouteCarModeOptions"
        ] = None,
        truck_mode_options: Optional[
            "capo_location.types.calculate_route_truck_mode_options.CalculateRouteTruckModeOptions"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.calculate_route_matrix_response.CalculateRouteMatrixResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the <a href="/location/latest/APIReference/API_CalculateRouteMatrix.html">V2 <code>CalculateRouteMatrix</code> </a> unless you require Grab data.</p> <ul> <li> <p>This version of <code>CalculateRouteMatrix</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>CalculateRouteMatrix</code> operation gives better results for matrix routing calculations.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html"> Calculates a route matrix</a> given the following required parameters: <code>DeparturePositions</code> and <code>DestinationPositions</code>. <code>CalculateRouteMatrix</code> calculates routes and returns the travel time and travel distance from each departure position to each destination position in the request. For example, given departure positions A and B, and destination positions X and Y, <code>CalculateRouteMatrix</code> will return time and distance for routes from A to X, A to Y, B to X, and B to Y (in that order). The number of results returned (and routes calculated) will be the number of <code>DeparturePositions</code> times the number of <code>DestinationPositions</code>.</p> <note> <p>Your account is charged for each route calculated, not the number of requests.</p> </note> <p>Requires that you first <a href="https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html">create a route calculator resource</a>.</p> <p>By default, a request that doesn't specify a departure time uses the best time of day to travel with the best traffic conditions when calculating routes.</p> <p>Additional options include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html"> Specifying a departure time</a> using either <code>DepartureTime</code> or <code>DepartNow</code>. This calculates routes based on predictive traffic data at the given time. </p> <note> <p>You can't specify both <code>DepartureTime</code> and <code>DepartNow</code> in a single request. Specifying both parameters returns a validation error.</p> </note> </li> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html">Specifying a travel mode</a> using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in <code>CarModeOptions</code> if traveling by <code>Car</code>, or <code>TruckModeOptions</code> if traveling by <code>Truck</code>.</p> </li> </ul>

        Args:
            calculator_name: <p>The name of the route calculator resource that you want to use to calculate the route matrix. </p>
            departure_positions: <p>The list of departure (origin) positions for the route matrix. An array of points, each of which is itself a 2-value array defined in <a href="https://earth-info.nga.mil/GandG/wgs84/index.html">WGS 84</a> format: <code>[longitude, latitude]</code>. For example, <code>[-123.115, 49.285]</code>.</p> <important> <p>Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits"> Position restrictions</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </important> <note> <p>For route calculators that use Esri as the data provider, if you specify a departure that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html"> moves the position to the nearest road</a>. The snapped value is available in the result in <code>SnappedDeparturePositions</code>.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            destination_positions: <p>The list of destination positions for the route matrix. An array of points, each of which is itself a 2-value array defined in <a href="https://earth-info.nga.mil/GandG/wgs84/index.html">WGS 84</a> format: <code>[longitude, latitude]</code>. For example, <code>[-122.339, 47.615]</code> </p> <important> <p>Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits"> Position restrictions</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </important> <note> <p>For route calculators that use Esri as the data provider, if you specify a destination that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html"> moves the position to the nearest road</a>. The snapped value is available in the result in <code>SnappedDestinationPositions</code>.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            travel_mode: <p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>The <code>TravelMode</code> you specify also determines how you specify route preferences: </p> <ul> <li> <p>If traveling by <code>Car</code> use the <code>CarModeOptions</code> parameter.</p> </li> <li> <p>If traveling by <code>Truck</code> use the <code>TruckModeOptions</code> parameter.</p> </li> </ul> <note> <p> <code>Bicycle</code> or <code>Motorcycle</code> are only valid when using <code>Grab</code> as a data provider, and only within Southeast Asia.</p> <p> <code>Truck</code> is not available for Grab.</p> <p>For more information about using Grab as a data provider, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>Default Value: <code>Car</code> </p>
            departure_time: <p>Specifies the desired time of departure. Uses the given time to calculate the route matrix. You can't set both <code>DepartureTime</code> and <code>DepartNow</code>. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.</p> <note> <p>Setting a departure time in the past returns a <code>400 ValidationException</code> error.</p> </note> <ul> <li> <p>In <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>
            depart_now: <p>Sets the time of departure as the current time. Uses the current time to calculate the route matrix. You can't set both <code>DepartureTime</code> and <code>DepartNow</code>. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            distance_unit: <p>Set the unit system to specify the distance.</p> <p>Default Value: <code>Kilometers</code> </p>
            car_mode_options: <p>Specifies route preferences when traveling by <code>Car</code>, such as avoiding routes that use ferries or tolls.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Car</code>.</p>
            truck_mode_options: <p>Specifies route preferences when traveling by <code>Truck</code>, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Truck</code>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.calculate_route_matrix_request.CalculateRouteMatrixRequest]",
        ) -> OperationResponse[
            "capo_location.types.calculate_route_matrix_response.CalculateRouteMatrixResponse"
        ]:
            import capo_location._operations.location_service.calculate_route_matrix

            output, http_response = (
                capo_location._operations.location_service.calculate_route_matrix.calculate_route_matrix(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.calculate_route_matrix_request.CalculateRouteMatrixRequest = {
            "calculator_name": calculator_name,
            "departure_positions": departure_positions,
            "destination_positions": destination_positions,
        }
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit
        if car_mode_options is not None:
            input_["car_mode_options"] = car_mode_options
        if truck_mode_options is not None:
            input_["truck_mode_options"] = truck_mode_options
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRouteCalculatorResource:
    def __init__(self, service: AsyncLocationClient) -> None:
        self._service = service

    async def put(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        data_source: str,
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_route_calculator_response.CreateRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>CreateRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Creates a route calculator resource in your Amazon Web Services account.</p> <p>You can send requests to a route calculator resource to estimate travel time, distance, and get directions. A route calculator sources traffic and road network data from your chosen data provider.</p> <note> <p>If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the <a href="http://aws.amazon.com/service-terms">Amazon Web Services service terms</a> for more details.</p> </note>

        Args:
            calculator_name: <p>The name of the route calculator resource. </p> <p>Requirements:</p> <ul> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9) , hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique Route calculator resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleRouteCalculator</code>.</p> </li> </ul>
            data_source: <p>Specifies the data provider of traffic and road network data.</p> <note> <p>This field is case-sensitive. Enter the valid values as shown. For example, entering <code>HERE</code> returns an error.</p> </note> <p>Valid values include:</p> <ul> <li> <p> <code>Esri</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/esri.html">Esri</a>'s coverage in your region of interest, see <a href="https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm">Esri details on street networks and traffic coverage</a>.</p> <p>Route calculators that use Esri as a data source only calculate routes that are shorter than 400 km.</p> </li> <li> <p> <code>Grab</code> – Grab provides routing functionality for Southeast Asia. For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a>' coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area">GrabMaps countries and areas covered</a>.</p> </li> <li> <p> <code>Here</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/HERE.html">HERE Technologies</a>' coverage in your region of interest, see <a href="https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html">HERE car routing coverage</a> and <a href="https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html">HERE truck routing coverage</a>.</p> </li> </ul> <p>For additional information , see <a href="https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html">Data providers</a> on the <i>Amazon Location Service Developer Guide</i>.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>The optional description for the route calculator resource.</p>
            tags: <p>Applies one or more tags to the route calculator resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.</p> <ul> <li> <p>For example: { <code>"tag1" : "value1"</code>, <code>"tag2" : "value2"</code>}</p> </li> </ul> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.create_route_calculator_request.CreateRouteCalculatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.create_route_calculator_response.CreateRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.create_route_calculator

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.create_route_calculator.async_create_route_calculator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.create_route_calculator_request.CreateRouteCalculatorRequest = {
            "calculator_name": calculator_name,
            "data_source": data_source,
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "capo_location.types.describe_route_calculator_response.DescribeRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DescribeRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the route calculator resource details.</p>

        Args:
            calculator_name: <p>The name of the route calculator resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.describe_route_calculator_request.DescribeRouteCalculatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.describe_route_calculator_response.DescribeRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.describe_route_calculator

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.describe_route_calculator.async_describe_route_calculator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.describe_route_calculator_request.DescribeRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_location.types.update_route_calculator_response.UpdateRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>UpdateRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Updates the specified properties for a given route calculator resource.</p>

        Args:
            calculator_name: <p>The name of the route calculator resource to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>Updates the description for the route calculator resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.update_route_calculator_request.UpdateRouteCalculatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.update_route_calculator_response.UpdateRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.update_route_calculator

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.update_route_calculator.async_update_route_calculator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.update_route_calculator_request.UpdateRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "capo_location.types.delete_route_calculator_response.DeleteRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DeleteRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Deletes a route calculator resource from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently.</p> </note>

        Args:
            calculator_name: <p>The name of the route calculator resource to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.delete_route_calculator_request.DeleteRouteCalculatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.delete_route_calculator_response.DeleteRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.delete_route_calculator

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.delete_route_calculator.async_delete_route_calculator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.delete_route_calculator_request.DeleteRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_route_calculators_response.ListRouteCalculatorsResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>ListRouteCalculators</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Lists route calculator resources in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional maximum number of results returned in a single call.</p> <p>Default Value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default Value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.list_route_calculators_request.ListRouteCalculatorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.list_route_calculators_response.ListRouteCalculatorsResponse"
        ]:
            import capo_location._operations.location_service.list_route_calculators

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.list_route_calculators.async_list_route_calculators(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_route_calculators_request.ListRouteCalculatorsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def calculate_route(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        departure_position: "capo_location.types.position.Position",
        destination_position: "capo_location.types.position.Position",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        waypoint_positions: Optional[
            "capo_location.types.waypoint_position_list.WaypointPositionList"
        ] = None,
        travel_mode: Optional["capo_location.types.travel_mode.TravelMode"] = None,
        departure_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        depart_now: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
        include_leg_geometry: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        car_mode_options: Optional[
            "capo_location.types.calculate_route_car_mode_options.CalculateRouteCarModeOptions"
        ] = None,
        truck_mode_options: Optional[
            "capo_location.types.calculate_route_truck_mode_options.CalculateRouteTruckModeOptions"
        ] = None,
        arrival_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        optimize_for: Optional[
            "capo_location.types.optimization_mode.OptimizationMode"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.calculate_route_response.CalculateRouteResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_CalculateRoutes.html"> <code>CalculateRoutes</code> </a> or <a href="/location/latest/APIReference/API_CalculateIsolines.html"> <code>CalculateIsolines</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>CalculateRoute</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>CalculateRoutes</code> operation gives better results for point-to-point routing, while the version 2 <code>CalculateIsolines</code> operation adds support for calculating service areas and travel time envelopes.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route.html">Calculates a route</a> given the following required parameters: <code>DeparturePosition</code> and <code>DestinationPosition</code>. Requires that you first <a href="https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html">create a route calculator resource</a>.</p> <p>By default, a request that doesn't specify a departure time uses the best time of day to travel with the best traffic conditions when calculating the route.</p> <p>Additional options include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html">Specifying a departure time</a> using either <code>DepartureTime</code> or <code>DepartNow</code>. This calculates a route based on predictive traffic data at the given time. </p> <note> <p>You can't specify both <code>DepartureTime</code> and <code>DepartNow</code> in a single request. Specifying both parameters returns a validation error.</p> </note> </li> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html">Specifying a travel mode</a> using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in <code>CarModeOptions</code> if traveling by <code>Car</code>, or <code>TruckModeOptions</code> if traveling by <code>Truck</code>.</p> <note> <p>If you specify <code>walking</code> for the travel mode and your data provider is Esri, the start and destination must be within 40km.</p> </note> </li> </ul>

        Args:
            calculator_name: <p>The name of the route calculator resource that you want to use to calculate the route. </p>
            departure_position: <p>The start position for the route. Defined in <a href="https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84">World Geodetic System (WGS 84)</a> format: <code>[longitude, latitude]</code>.</p> <ul> <li> <p>For example, <code>[-123.115, 49.285]</code> </p> </li> </ul> <note> <p>If you specify a departure that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a <code>400 RoutesValidationException</code> error.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            destination_position: <p>The finish position for the route. Defined in <a href="https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84">World Geodetic System (WGS 84)</a> format: <code>[longitude, latitude]</code>.</p> <ul> <li> <p> For example, <code>[-122.339, 47.615]</code> </p> </li> </ul> <note> <p>If you specify a destination that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. </p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            waypoint_positions: <p>Specifies an ordered list of up to 23 intermediate positions to include along a route between the departure position and destination position. </p> <ul> <li> <p>For example, from the <code>DeparturePosition</code> <code>[-123.115, 49.285]</code>, the route follows the order that the waypoint positions are given <code>[[-122.757, 49.0021],[-122.349, 47.620]]</code> </p> </li> </ul> <note> <p>If you specify a waypoint position that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. </p> <p>Specifying more than 23 waypoints returns a <code>400 ValidationException</code> error.</p> <p>If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a <code>400 RoutesValidationException</code> error.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            travel_mode: <p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. You can choose <code>Car</code>, <code>Truck</code>, <code>Walking</code>, <code>Bicycle</code> or <code>Motorcycle</code> as options for the <code>TravelMode</code>.</p> <note> <p> <code>Bicycle</code> and <code>Motorcycle</code> are only valid when using Grab as a data provider, and only within Southeast Asia.</p> <p> <code>Truck</code> is not available for Grab.</p> <p>For more details on the using Grab for routing, including areas of coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>The <code>TravelMode</code> you specify also determines how you specify route preferences: </p> <ul> <li> <p>If traveling by <code>Car</code> use the <code>CarModeOptions</code> parameter.</p> </li> <li> <p>If traveling by <code>Truck</code> use the <code>TruckModeOptions</code> parameter.</p> </li> </ul> <p>Default Value: <code>Car</code> </p>
            departure_time: <p>Specifies the desired time of departure. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <ul> <li> <p>In <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>
            depart_now: <p>Sets the time of departure as the current time. Uses the current time to calculate a route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            distance_unit: <p>Set the unit system to specify the distance.</p> <p>Default Value: <code>Kilometers</code> </p>
            include_leg_geometry: <p>Set to include the geometry details in the result for each path between a pair of positions.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            car_mode_options: <p>Specifies route preferences when traveling by <code>Car</code>, such as avoiding routes that use ferries or tolls.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Car</code>.</p>
            truck_mode_options: <p>Specifies route preferences when traveling by <code>Truck</code>, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Truck</code>.</p>
            arrival_time: <p>Specifies the desired time of arrival. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <note> <p>ArrivalTime is not supported Esri.</p> </note>
            optimize_for: <p>Specifies the distance to optimize for when calculating a route.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.calculate_route_request.CalculateRouteRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.calculate_route_response.CalculateRouteResponse"
        ]:
            import capo_location._operations.location_service.calculate_route

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.calculate_route.async_calculate_route(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.calculate_route_request.CalculateRouteRequest = {
            "calculator_name": calculator_name,
            "departure_position": departure_position,
            "destination_position": destination_position,
        }
        if waypoint_positions is not None:
            input_["waypoint_positions"] = waypoint_positions
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit
        if include_leg_geometry is not None:
            input_["include_leg_geometry"] = include_leg_geometry
        if car_mode_options is not None:
            input_["car_mode_options"] = car_mode_options
        if truck_mode_options is not None:
            input_["truck_mode_options"] = truck_mode_options
        if arrival_time is not None:
            input_["arrival_time"] = arrival_time
        if optimize_for is not None:
            input_["optimize_for"] = optimize_for
        if key is not None:
            input_["key"] = key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def calculate_route_matrix(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        departure_positions: "capo_location.types.position_list.PositionList",
        destination_positions: "capo_location.types.position_list.PositionList",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        travel_mode: Optional["capo_location.types.travel_mode.TravelMode"] = None,
        departure_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        depart_now: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
        car_mode_options: Optional[
            "capo_location.types.calculate_route_car_mode_options.CalculateRouteCarModeOptions"
        ] = None,
        truck_mode_options: Optional[
            "capo_location.types.calculate_route_truck_mode_options.CalculateRouteTruckModeOptions"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.calculate_route_matrix_response.CalculateRouteMatrixResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the <a href="/location/latest/APIReference/API_CalculateRouteMatrix.html">V2 <code>CalculateRouteMatrix</code> </a> unless you require Grab data.</p> <ul> <li> <p>This version of <code>CalculateRouteMatrix</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>CalculateRouteMatrix</code> operation gives better results for matrix routing calculations.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html"> Calculates a route matrix</a> given the following required parameters: <code>DeparturePositions</code> and <code>DestinationPositions</code>. <code>CalculateRouteMatrix</code> calculates routes and returns the travel time and travel distance from each departure position to each destination position in the request. For example, given departure positions A and B, and destination positions X and Y, <code>CalculateRouteMatrix</code> will return time and distance for routes from A to X, A to Y, B to X, and B to Y (in that order). The number of results returned (and routes calculated) will be the number of <code>DeparturePositions</code> times the number of <code>DestinationPositions</code>.</p> <note> <p>Your account is charged for each route calculated, not the number of requests.</p> </note> <p>Requires that you first <a href="https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html">create a route calculator resource</a>.</p> <p>By default, a request that doesn't specify a departure time uses the best time of day to travel with the best traffic conditions when calculating routes.</p> <p>Additional options include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html"> Specifying a departure time</a> using either <code>DepartureTime</code> or <code>DepartNow</code>. This calculates routes based on predictive traffic data at the given time. </p> <note> <p>You can't specify both <code>DepartureTime</code> and <code>DepartNow</code> in a single request. Specifying both parameters returns a validation error.</p> </note> </li> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html">Specifying a travel mode</a> using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in <code>CarModeOptions</code> if traveling by <code>Car</code>, or <code>TruckModeOptions</code> if traveling by <code>Truck</code>.</p> </li> </ul>

        Args:
            calculator_name: <p>The name of the route calculator resource that you want to use to calculate the route matrix. </p>
            departure_positions: <p>The list of departure (origin) positions for the route matrix. An array of points, each of which is itself a 2-value array defined in <a href="https://earth-info.nga.mil/GandG/wgs84/index.html">WGS 84</a> format: <code>[longitude, latitude]</code>. For example, <code>[-123.115, 49.285]</code>.</p> <important> <p>Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits"> Position restrictions</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </important> <note> <p>For route calculators that use Esri as the data provider, if you specify a departure that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html"> moves the position to the nearest road</a>. The snapped value is available in the result in <code>SnappedDeparturePositions</code>.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            destination_positions: <p>The list of destination positions for the route matrix. An array of points, each of which is itself a 2-value array defined in <a href="https://earth-info.nga.mil/GandG/wgs84/index.html">WGS 84</a> format: <code>[longitude, latitude]</code>. For example, <code>[-122.339, 47.615]</code> </p> <important> <p>Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits"> Position restrictions</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </important> <note> <p>For route calculators that use Esri as the data provider, if you specify a destination that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html"> moves the position to the nearest road</a>. The snapped value is available in the result in <code>SnappedDestinationPositions</code>.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            travel_mode: <p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>The <code>TravelMode</code> you specify also determines how you specify route preferences: </p> <ul> <li> <p>If traveling by <code>Car</code> use the <code>CarModeOptions</code> parameter.</p> </li> <li> <p>If traveling by <code>Truck</code> use the <code>TruckModeOptions</code> parameter.</p> </li> </ul> <note> <p> <code>Bicycle</code> or <code>Motorcycle</code> are only valid when using <code>Grab</code> as a data provider, and only within Southeast Asia.</p> <p> <code>Truck</code> is not available for Grab.</p> <p>For more information about using Grab as a data provider, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>Default Value: <code>Car</code> </p>
            departure_time: <p>Specifies the desired time of departure. Uses the given time to calculate the route matrix. You can't set both <code>DepartureTime</code> and <code>DepartNow</code>. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.</p> <note> <p>Setting a departure time in the past returns a <code>400 ValidationException</code> error.</p> </note> <ul> <li> <p>In <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>
            depart_now: <p>Sets the time of departure as the current time. Uses the current time to calculate the route matrix. You can't set both <code>DepartureTime</code> and <code>DepartNow</code>. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            distance_unit: <p>Set the unit system to specify the distance.</p> <p>Default Value: <code>Kilometers</code> </p>
            car_mode_options: <p>Specifies route preferences when traveling by <code>Car</code>, such as avoiding routes that use ferries or tolls.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Car</code>.</p>
            truck_mode_options: <p>Specifies route preferences when traveling by <code>Truck</code>, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Truck</code>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.calculate_route_matrix_request.CalculateRouteMatrixRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.calculate_route_matrix_response.CalculateRouteMatrixResponse"
        ]:
            import capo_location._operations.location_service.calculate_route_matrix

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.calculate_route_matrix.async_calculate_route_matrix(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.calculate_route_matrix_request.CalculateRouteMatrixRequest = {
            "calculator_name": calculator_name,
            "departure_positions": departure_positions,
            "destination_positions": destination_positions,
        }
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit
        if car_mode_options is not None:
            input_["car_mode_options"] = car_mode_options
        if truck_mode_options is not None:
            input_["truck_mode_options"] = truck_mode_options
        if key is not None:
            input_["key"] = key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
