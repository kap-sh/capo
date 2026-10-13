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
    import capo_mediaconnect.types.batch_get_router_input_request
    import capo_mediaconnect.types.batch_get_router_input_response
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.create_router_input_request
    import capo_mediaconnect.types.create_router_input_response
    import capo_mediaconnect.types.delete_router_input_request
    import capo_mediaconnect.types.delete_router_input_response
    import capo_mediaconnect.types.get_router_input_request
    import capo_mediaconnect.types.get_router_input_response
    import capo_mediaconnect.types.get_router_input_source_metadata_request
    import capo_mediaconnect.types.get_router_input_source_metadata_response
    import capo_mediaconnect.types.get_router_input_thumbnail_request
    import capo_mediaconnect.types.get_router_input_thumbnail_response
    import capo_mediaconnect.types.list_router_inputs_request
    import capo_mediaconnect.types.list_router_inputs_response
    import capo_mediaconnect.types.listed_router_input
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.restart_router_input_request
    import capo_mediaconnect.types.restart_router_input_response
    import capo_mediaconnect.types.router_content_quality_analysis_configuration
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_arn_list
    import capo_mediaconnect.types.router_input_configuration
    import capo_mediaconnect.types.router_input_filter_list
    import capo_mediaconnect.types.router_input_tier
    import capo_mediaconnect.types.router_input_transit_encryption
    import capo_mediaconnect.types.routing_scope
    import capo_mediaconnect.types.start_router_input_request
    import capo_mediaconnect.types.start_router_input_response
    import capo_mediaconnect.types.stop_router_input_request
    import capo_mediaconnect.types.stop_router_input_response
    import capo_mediaconnect.types.update_router_input_request
    import capo_mediaconnect.types.update_router_input_response
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class RouterInputResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration",
        maximum_bitrate: int,
        routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope",
        tier: "capo_mediaconnect.types.router_input_tier.RouterInputTier",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        transit_encryption: Optional[
            "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
        content_quality_analysis_configuration: Optional[
            "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.create_router_input_response.CreateRouterInputResponse"
    ):
        """<p>Creates a new router input in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router input.</p>
            configuration: <p>The configuration settings for the router input, which can include the protocol, network interface, and other details.</p>
            maximum_bitrate: <p>The maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - connects only to outputs in same Region. GLOBAL - connects to outputs in any Region.</p>
            tier: <p>The tier level for the router input.</p>
            region_name: <p>The Amazon Web Services Region for the router input. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router input. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            transit_encryption: <p>The transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The maintenance configuration settings for the router input, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router input.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>
            content_quality_analysis_configuration: <p>The content quality analysis configuration for the router input.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_input_service_quota_exceeded_exception.RouterInputServiceQuotaExceededException: <p>The request to create a new router input would exceed the service quotas for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_router_input_request.CreateRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_router_input_response.CreateRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_router_input.create_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRouterInput")
        )
        input_: capo_mediaconnect.types.create_router_input_request.CreateRouterInputRequest = {
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
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if content_quality_analysis_configuration is not None:
            input_["content_quality_analysis_configuration"] = (
                content_quality_analysis_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_response.GetRouterInputResponse":
        """<p>Retrieves information about a specific router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve information about.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.get_router_input_request.GetRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_input_response.GetRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_input.get_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterInput")
        )
        input_: capo_mediaconnect.types.get_router_input_request.GetRouterInputRequest = {
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
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "capo_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "capo_mediaconnect.types.router_input_tier.RouterInputTier"
        ] = None,
        transit_encryption: Optional[
            "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        content_quality_analysis_configuration: Optional[
            "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse"
    ):
        """<p>Updates the configuration of an existing router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to update.</p>
            name: <p>The updated name for the router input.</p>
            configuration: <p>The updated configuration settings for the router input. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - can be assigned only to outputs in the same Region. GLOBAL - can be assigned to outputs in any Region.</p>
            tier: <p>The updated tier level for the router input.</p>
            transit_encryption: <p>The updated transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router input, including any changes to preferred maintenance windows and schedules.</p>
            content_quality_analysis_configuration: <p>The content quality analysis configuration for the router input.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_router_input.update_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRouterInput")
        )
        input_: capo_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest = {
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
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if content_quality_analysis_configuration is not None:
            input_["content_quality_analysis_configuration"] = (
                content_quality_analysis_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> (
        "capo_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse"
    ):
        """<p>Deletes a router input from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to delete.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_router_input.delete_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRouterInput")
        )
        input_: capo_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest = {
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
            "capo_mediaconnect.types.router_input_filter_list.RouterInputFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse":
        """<p>Retrieves a list of router inputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router inputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router inputs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_inputs

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_router_inputs.list_router_inputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRouterInputs")
        )
        input_: capo_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest = {}
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

    def get_router_input_source_metadata(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse":
        """<p>Retrieves detailed metadata information about a specific router input source, including stream details and connection state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve metadata for.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input_source_metadata

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_input_source_metadata.get_router_input_source_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterInputSourceMetadata")
        )
        input_: capo_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_router_input_thumbnail(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse":
        """<p>Retrieves the thumbnail for a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to see a thumbnail of.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input_thumbnail

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_input_thumbnail.get_router_input_thumbnail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterInputThumbnail")
        )
        input_: capo_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restart_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse":
        """<p>Restarts a router input. This operation can be used to recover from errors or refresh the input state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to restart.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.restart_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.restart_router_input.restart_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestartRouterInput")
        )
        input_: capo_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.start_router_input_response.StartRouterInputResponse":
        """<p>Starts a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to start.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.start_router_input_request.StartRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.start_router_input_response.StartRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.start_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.start_router_input.start_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartRouterInput")
        )
        input_: capo_mediaconnect.types.start_router_input_request.StartRouterInputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.stop_router_input_response.StopRouterInputResponse":
        """<p>Stops a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to stop.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.stop_router_input_request.StopRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.stop_router_input_response.StopRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.stop_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.stop_router_input.stop_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopRouterInput")
        )
        input_: capo_mediaconnect.types.stop_router_input_request.StopRouterInputRequest = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_router_input(
        self,
        arns: "capo_mediaconnect.types.router_input_arn_list.RouterInputArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse":
        """<p>Retrieves information about multiple router inputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router inputs you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_input

            output, http_response = (
                capo_mediaconnect._operations.media_connect.batch_get_router_input.batch_get_router_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetRouterInput")
        )
        input_: capo_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRouterInputResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration",
        maximum_bitrate: int,
        routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope",
        tier: "capo_mediaconnect.types.router_input_tier.RouterInputTier",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        availability_zone: Optional[str] = None,
        transit_encryption: Optional[
            "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
        content_quality_analysis_configuration: Optional[
            "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.create_router_input_response.CreateRouterInputResponse"
    ):
        """<p>Creates a new router input in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router input.</p>
            configuration: <p>The configuration settings for the router input, which can include the protocol, network interface, and other details.</p>
            maximum_bitrate: <p>The maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - connects only to outputs in same Region. GLOBAL - connects to outputs in any Region.</p>
            tier: <p>The tier level for the router input.</p>
            region_name: <p>The Amazon Web Services Region for the router input. Defaults to the current region if not specified.</p>
            availability_zone: <p>The Availability Zone where you want to create the router input. This must be a valid Availability Zone for the region specified by <code>regionName</code>, or the current region if no <code>regionName</code> is provided. </p>
            transit_encryption: <p>The transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The maintenance configuration settings for the router input, including preferred maintenance windows and schedules.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router input.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>
            content_quality_analysis_configuration: <p>The content quality analysis configuration for the router input.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_input_service_quota_exceeded_exception.RouterInputServiceQuotaExceededException: <p>The request to create a new router input would exceed the service quotas for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.create_router_input_request.CreateRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.create_router_input_response.CreateRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.create_router_input.async_create_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRouterInput")
        )
        input_: capo_mediaconnect.types.create_router_input_request.CreateRouterInputRequest = {
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
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if content_quality_analysis_configuration is not None:
            input_["content_quality_analysis_configuration"] = (
                content_quality_analysis_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_response.GetRouterInputResponse":
        """<p>Retrieves information about a specific router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve information about.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.get_router_input_request.GetRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.get_router_input_response.GetRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.get_router_input.async_get_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterInput")
        )
        input_: capo_mediaconnect.types.get_router_input_request.GetRouterInputRequest = {
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
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
        ] = None,
        maximum_bitrate: Optional[int] = None,
        routing_scope: Optional[
            "capo_mediaconnect.types.routing_scope.RoutingScope"
        ] = None,
        tier: Optional[
            "capo_mediaconnect.types.router_input_tier.RouterInputTier"
        ] = None,
        transit_encryption: Optional[
            "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
        ] = None,
        maintenance_configuration: Optional[
            "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
        ] = None,
        content_quality_analysis_configuration: Optional[
            "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse"
    ):
        """<p>Updates the configuration of an existing router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to update.</p>
            name: <p>The updated name for the router input.</p>
            configuration: <p>The updated configuration settings for the router input. Changing the type of the configuration is not supported.</p>
            maximum_bitrate: <p>The updated maximum bitrate for the router input.</p>
            routing_scope: <p>Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - can be assigned only to outputs in the same Region. GLOBAL - can be assigned to outputs in any Region.</p>
            tier: <p>The updated tier level for the router input.</p>
            transit_encryption: <p>The updated transit encryption settings for the router input.</p>
            maintenance_configuration: <p>The updated maintenance configuration settings for the router input, including any changes to preferred maintenance windows and schedules.</p>
            content_quality_analysis_configuration: <p>The content quality analysis configuration for the router input.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_router_input_response.UpdateRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_router_input.async_update_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRouterInput")
        )
        input_: capo_mediaconnect.types.update_router_input_request.UpdateRouterInputRequest = {
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
        if transit_encryption is not None:
            input_["transit_encryption"] = transit_encryption
        if maintenance_configuration is not None:
            input_["maintenance_configuration"] = maintenance_configuration
        if content_quality_analysis_configuration is not None:
            input_["content_quality_analysis_configuration"] = (
                content_quality_analysis_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> (
        "capo_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse"
    ):
        """<p>Deletes a router input from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to delete.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.delete_router_input_response.DeleteRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.delete_router_input.async_delete_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRouterInput")
        )
        input_: capo_mediaconnect.types.delete_router_input_request.DeleteRouterInputRequest = {
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
            "capo_mediaconnect.types.router_input_filter_list.RouterInputFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse":
        """<p>Retrieves a list of router inputs in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router inputs to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router inputs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_router_inputs_response.ListRouterInputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_inputs

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_router_inputs.async_list_router_inputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRouterInputs")
        )
        input_: capo_mediaconnect.types.list_router_inputs_request.ListRouterInputsRequest = {}
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

    async def get_router_input_source_metadata(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse":
        """<p>Retrieves detailed metadata information about a specific router input source, including stream details and connection state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input to retrieve metadata for.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.get_router_input_source_metadata_response.GetRouterInputSourceMetadataResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input_source_metadata

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.get_router_input_source_metadata.async_get_router_input_source_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterInputSourceMetadata")
        )
        input_: capo_mediaconnect.types.get_router_input_source_metadata_request.GetRouterInputSourceMetadataRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_router_input_thumbnail(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse":
        """<p>Retrieves the thumbnail for a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to see a thumbnail of.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.get_router_input_thumbnail_response.GetRouterInputThumbnailResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_input_thumbnail

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.get_router_input_thumbnail.async_get_router_input_thumbnail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterInputThumbnail")
        )
        input_: capo_mediaconnect.types.get_router_input_thumbnail_request.GetRouterInputThumbnailRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restart_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse":
        """<p>Restarts a router input. This operation can be used to recover from errors or refresh the input state.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to restart.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.restart_router_input_response.RestartRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.restart_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.restart_router_input.async_restart_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestartRouterInput")
        )
        input_: capo_mediaconnect.types.restart_router_input_request.RestartRouterInputRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.start_router_input_response.StartRouterInputResponse":
        """<p>Starts a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to start.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.start_router_input_request.StartRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.start_router_input_response.StartRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.start_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.start_router_input.async_start_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartRouterInput")
        )
        input_: capo_mediaconnect.types.start_router_input_request.StartRouterInputRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_router_input(
        self,
        arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.stop_router_input_response.StopRouterInputResponse":
        """<p>Stops a router input in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router input that you want to stop.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.stop_router_input_request.StopRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.stop_router_input_response.StopRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.stop_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.stop_router_input.async_stop_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopRouterInput")
        )
        input_: capo_mediaconnect.types.stop_router_input_request.StopRouterInputRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_router_input(
        self,
        arns: "capo_mediaconnect.types.router_input_arn_list.RouterInputArnList",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse":
        """<p>Retrieves information about multiple router inputs in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router inputs you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.batch_get_router_input_response.BatchGetRouterInputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_input

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.batch_get_router_input.async_batch_get_router_input(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetRouterInput")
        )
        input_: capo_mediaconnect.types.batch_get_router_input_request.BatchGetRouterInputRequest = {
            "arns": arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
