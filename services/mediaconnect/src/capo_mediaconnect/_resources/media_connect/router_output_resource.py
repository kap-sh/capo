from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_mediaconnect._auth._signers
import capo_mediaconnect._auth._sigv4
from capo_mediaconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.batch_get_router_output_request
    import capo_mediaconnect.types.batch_get_router_output_response
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.create_router_output_request
    import capo_mediaconnect.types.create_router_output_response
    import capo_mediaconnect.types.delete_router_output_request
    import capo_mediaconnect.types.delete_router_output_response
    import capo_mediaconnect.types.fabric_configuration
    import capo_mediaconnect.types.get_router_output_request
    import capo_mediaconnect.types.get_router_output_response
    import capo_mediaconnect.types.list_router_outputs_request
    import capo_mediaconnect.types.list_router_outputs_response
    import capo_mediaconnect.types.listed_router_output
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.restart_router_output_request
    import capo_mediaconnect.types.restart_router_output_response
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_output_arn
    import capo_mediaconnect.types.router_output_arn_list
    import capo_mediaconnect.types.router_output_configuration
    import capo_mediaconnect.types.router_output_filter_list
    import capo_mediaconnect.types.router_output_tier
    import capo_mediaconnect.types.routing_scope
    import capo_mediaconnect.types.start_router_output_request
    import capo_mediaconnect.types.start_router_output_response
    import capo_mediaconnect.types.stop_router_output_request
    import capo_mediaconnect.types.stop_router_output_response
    import capo_mediaconnect.types.take_router_input_request
    import capo_mediaconnect.types.take_router_input_response
    import capo_mediaconnect.types.update_router_output_request
    import capo_mediaconnect.types.update_router_output_response
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class RouterOutputResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_output_configuration.RouterOutputConfiguration",
        maximum_bitrate: int,
        routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope",
        tier: "capo_mediaconnect.types.router_output_tier.RouterOutputTier",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        fabric_configuration: Optional[
            "capo_mediaconnect.types.fabric_configuration.FabricConfiguration"
        ] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse":
        """<p>Creates a new router output in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router output.</p>
            configuration: <p>The configuration settings for the router output.</p>
            maximum_bitrate: <p>The maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The tier level for the router output.</p>
            region_name: <p>The Amazon Web Services Region for the router output. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router output. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            maintenance_configuration: <p>The maintenance configuration settings for the router output, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag this router output.</p>
            fabric_configuration: <p>The fabric configuration settings for the router output.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_output_service_quota_exceeded_exception.RouterOutputServiceQuotaExceededException: <p>The request to create a new router output would exceed the service quotas (limits) set for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_router_output.create_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRouterOutput")
        )
        input_: capo_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest = {
            "name": name,
            "configuration": configuration,
            "maximum_bitrate": maximum_bitrate,
            "routing_scope": routing_scope,
            "tier": tier,
        }
        if region_name is not None:
            input_["region_name"] = region_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input_["tags"] = tags
        if fabric_configuration is not None:
            input_["fabric_configuration"] = fabric_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_output_response.GetRouterOutputResponse":
        """<p>Retrieves information about a specific router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.get_router_output_request.GetRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_output_response.GetRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_output.get_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterOutput")
        )
        input_: capo_mediaconnect.types.get_router_output_request.GetRouterOutputRequest = {
            "arn": arn
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
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_output_configuration.RouterOutputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "capo_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "capo_mediaconnect.types.router_output_tier.RouterOutputTier"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        fabric_configuration: Optional[
            "capo_mediaconnect.types.fabric_configuration.FabricConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse":
        """<p>Updates the configuration of an existing router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to update.</p>
            name: <p>The updated name for the router output.</p>
            configuration: <p>The updated configuration settings for the router output. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The updated tier level for the router output.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router output, including any changes to preferred maintenance windows and schedules.</p>
            fabric_configuration: <p>The updated fabric configuration settings for the router output. You cannot update the fabric configuration while the output has an active route. You must unroute the output before updating the fabric configuration.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_router_output.update_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRouterOutput")
        )
        input_: capo_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if routing_scope is not None:
            input_["routing_scope"] = routing_scope
        if tier is not None:
            input_["tier"] = tier
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if fabric_configuration is not None:
            input_["fabric_configuration"] = fabric_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse":
        """<p>Deletes a router output from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_router_output.delete_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRouterOutput")
        )
        input_: capo_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest = {
            "arn": arn
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
        config_overrides: Optional[MediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_mediaconnect.types.router_output_filter_list.RouterOutputFilterList"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse"
    ):
        """<p>Retrieves a list of router outputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router outputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router outputs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_outputs

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_router_outputs.list_router_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRouterOutputs")
        )
        input_: capo_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restart_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse":
        """<p>Restarts a router output. This operation can be used to recover from errors or refresh the output state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to restart.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.restart_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.restart_router_output.restart_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestartRouterOutput")
        )
        input_: capo_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> (
        "capo_mediaconnect.types.start_router_output_response.StartRouterOutputResponse"
    ):
        """<p>Starts a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to start.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.start_router_output_request.StartRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.start_router_output_response.StartRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.start_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.start_router_output.start_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartRouterOutput")
        )
        input_: capo_mediaconnect.types.start_router_output_request.StartRouterOutputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse":
        """<p>Stops a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to stop.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.stop_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.stop_router_output.stop_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopRouterOutput")
        )
        input_: capo_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def take_router_input(
        self,
        router_output_arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        router_input_arn: Optional[
            "capo_mediaconnect.types.router_input_arn.RouterInputArn"
        ] = None,
    ) -> "capo_mediaconnect.types.take_router_input_response.TakeRouterInputResponse":
        """<p>Associates a router input with a router output in AWS Elemental MediaConnect.</p>

        Args:
            router_output_arn: <p>The Amazon Resource Name (ARN) of the router output that you want to associate with a router input.</p>
            router_input_arn: <p>The Amazon Resource Name (ARN) of the router input that you want to associate with a router output.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.take_router_input_request.TakeRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.take_router_input_response.TakeRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.take_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.take_router_input.take_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("TakeRouterInput")
        )
        input_: capo_mediaconnect.types.take_router_input_request.TakeRouterInputRequest = {
            "router_output_arn": router_output_arn
        }
        if router_input_arn is not None:
            input_["router_input_arn"] = router_input_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_router_output(
        self,
        arns: "capo_mediaconnect.types.router_output_arn_list.RouterOutputArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse":
        """<p>Retrieves information about multiple router outputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router outputs you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.batch_get_router_output.batch_get_router_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetRouterOutput")
        )
        input_: capo_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRouterOutputResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_output_configuration.RouterOutputConfiguration",
        maximum_bitrate: int,
        routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope",
        tier: "capo_mediaconnect.types.router_output_tier.RouterOutputTier",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        fabric_configuration: Optional[
            "capo_mediaconnect.types.fabric_configuration.FabricConfiguration"
        ] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse":
        """<p>Creates a new router output in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router output.</p>
            configuration: <p>The configuration settings for the router output.</p>
            maximum_bitrate: <p>The maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The tier level for the router output.</p>
            region_name: <p>The Amazon Web Services Region for the router output. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router output. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            maintenance_configuration: <p>The maintenance configuration settings for the router output, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag this router output.</p>
            fabric_configuration: <p>The fabric configuration settings for the router output.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_output_service_quota_exceeded_exception.RouterOutputServiceQuotaExceededException: <p>The request to create a new router output would exceed the service quotas (limits) set for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.create_router_output_response.CreateRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.create_router_output.async_create_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRouterOutput")
        )
        input_: capo_mediaconnect.types.create_router_output_request.CreateRouterOutputRequest = {
            "name": name,
            "configuration": configuration,
            "maximum_bitrate": maximum_bitrate,
            "routing_scope": routing_scope,
            "tier": tier,
        }
        if region_name is not None:
            input_["region_name"] = region_name
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input_["tags"] = tags
        if fabric_configuration is not None:
            input_["fabric_configuration"] = fabric_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_output_response.GetRouterOutputResponse":
        """<p>Retrieves information about a specific router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.get_router_output_request.GetRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.get_router_output_response.GetRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.get_router_output.async_get_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterOutput")
        )
        input_: capo_mediaconnect.types.get_router_output_request.GetRouterOutputRequest = {
            "arn": arn
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
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_output_configuration.RouterOutputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "capo_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "capo_mediaconnect.types.router_output_tier.RouterOutputTier"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        fabric_configuration: Optional[
            "capo_mediaconnect.types.fabric_configuration.FabricConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse":
        """<p>Updates the configuration of an existing router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to update.</p>
            name: <p>The updated name for the router output.</p>
            configuration: <p>The updated configuration settings for the router output. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router output.</p>
            routing_scope: <p>Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.</p>
            tier: <p>The updated tier level for the router output.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router output, including any changes to preferred maintenance windows and schedules.</p>
            fabric_configuration: <p>The updated fabric configuration settings for the router output. You cannot update the fabric configuration while the output has an active route. You must unroute the output before updating the fabric configuration.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_router_output_response.UpdateRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_router_output.async_update_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRouterOutput")
        )
        input_: capo_mediaconnect.types.update_router_output_request.UpdateRouterOutputRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if routing_scope is not None:
            input_["routing_scope"] = routing_scope
        if tier is not None:
            input_["tier"] = tier
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if fabric_configuration is not None:
            input_["fabric_configuration"] = fabric_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse":
        """<p>Deletes a router output from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.delete_router_output_response.DeleteRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.delete_router_output.async_delete_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRouterOutput")
        )
        input_: capo_mediaconnect.types.delete_router_output_request.DeleteRouterOutputRequest = {
            "arn": arn
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
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        filters: Optional[
            "capo_mediaconnect.types.router_output_filter_list.RouterOutputFilterList"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse"
    ):
        """<p>Retrieves a list of router outputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router outputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router outputs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_router_outputs_response.ListRouterOutputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_outputs

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_router_outputs.async_list_router_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRouterOutputs")
        )
        input_: capo_mediaconnect.types.list_router_outputs_request.ListRouterOutputsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restart_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse":
        """<p>Restarts a router output. This operation can be used to recover from errors or refresh the output state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to restart.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.restart_router_output_response.RestartRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.restart_router_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.restart_router_output.async_restart_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestartRouterOutput")
        )
        input_: capo_mediaconnect.types.restart_router_output_request.RestartRouterOutputRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> (
        "capo_mediaconnect.types.start_router_output_response.StartRouterOutputResponse"
    ):
        """<p>Starts a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to start.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.start_router_output_request.StartRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.start_router_output_response.StartRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.start_router_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.start_router_output.async_start_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartRouterOutput")
        )
        input_: capo_mediaconnect.types.start_router_output_request.StartRouterOutputRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_router_output(
        self,
        arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse":
        """<p>Stops a router output in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router output that you want to stop.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.stop_router_output_response.StopRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.stop_router_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.stop_router_output.async_stop_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopRouterOutput")
        )
        input_: capo_mediaconnect.types.stop_router_output_request.StopRouterOutputRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def take_router_input(
        self,
        router_output_arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        router_input_arn: Optional[
            "capo_mediaconnect.types.router_input_arn.RouterInputArn"
        ] = None,
    ) -> "capo_mediaconnect.types.take_router_input_response.TakeRouterInputResponse":
        """<p>Associates a router input with a router output in AWS Elemental MediaConnect.</p>

        Args:
            router_output_arn: <p>The Amazon Resource Name (ARN) of the router output that you want to associate with a router input.</p>
            router_input_arn: <p>The Amazon Resource Name (ARN) of the router input that you want to associate with a router output.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.take_router_input_request.TakeRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.take_router_input_response.TakeRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.take_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.take_router_input.async_take_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("TakeRouterInput")
        )
        input_: capo_mediaconnect.types.take_router_input_request.TakeRouterInputRequest = {
            "router_output_arn": router_output_arn
        }
        if router_input_arn is not None:
            input_["router_input_arn"] = router_input_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_router_output(
        self,
        arns: "capo_mediaconnect.types.router_output_arn_list.RouterOutputArnList",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse":
        """<p>Retrieves information about multiple router outputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router outputs you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.batch_get_router_output_response.BatchGetRouterOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.batch_get_router_output.async_batch_get_router_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetRouterOutput")
        )
        input_: capo_mediaconnect.types.batch_get_router_output_request.BatchGetRouterOutputRequest = {
            "arns": arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
