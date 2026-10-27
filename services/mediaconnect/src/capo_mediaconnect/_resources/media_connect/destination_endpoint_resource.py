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
    import capo_mediaconnect.types.batch_get_destination_endpoint_request
    import capo_mediaconnect.types.batch_get_destination_endpoint_response
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.connect_endpoints_request
    import capo_mediaconnect.types.connect_endpoints_response
    import capo_mediaconnect.types.deregister_destination_endpoint_request
    import capo_mediaconnect.types.deregister_destination_endpoint_response
    import capo_mediaconnect.types.destination_endpoint_arn
    import capo_mediaconnect.types.destination_endpoint_arn_list
    import capo_mediaconnect.types.destination_endpoint_configuration
    import capo_mediaconnect.types.destination_endpoint_filter_list
    import capo_mediaconnect.types.disconnect_endpoints_request
    import capo_mediaconnect.types.disconnect_endpoints_response
    import capo_mediaconnect.types.get_destination_endpoint_request
    import capo_mediaconnect.types.get_destination_endpoint_response
    import capo_mediaconnect.types.list_destination_endpoints_request
    import capo_mediaconnect.types.list_destination_endpoints_response
    import capo_mediaconnect.types.listed_destination_endpoint
    import capo_mediaconnect.types.register_destination_endpoint_request
    import capo_mediaconnect.types.register_destination_endpoint_response
    import capo_mediaconnect.types.source_endpoint_arn
    import capo_mediaconnect.types.update_destination_endpoint_request
    import capo_mediaconnect.types.update_destination_endpoint_response
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class DestinationEndpointResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        configuration: "capo_mediaconnect.types.destination_endpoint_configuration.DestinationEndpointConfiguration",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        description: Optional[str] = None,
        region_name: Optional[str] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.register_destination_endpoint_response.RegisterDestinationEndpointResponse":
        """<p>Registers a new destination endpoint in MediaConnect.</p>

        Args:
            description: <p>A description to help you identify the destination endpoint.</p>
            configuration: <p>The configuration settings for the destination endpoint.</p>
            region_name: <p>The name of the Amazon Web Services Region in which to register the destination endpoint. Defaults to the current region if not specified.</p>
            tags: <p>The tags to apply to the destination endpoint. Each tag is a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.destination_endpoint_service_quota_exceeded_exception.DestinationEndpointServiceQuotaExceededException: <p>The request would cause you to exceed a service quota for destination endpoints. Delete unused destination endpoints or request a quota increase, then try your request again.</p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.register_destination_endpoint_request.RegisterDestinationEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.register_destination_endpoint_response.RegisterDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.register_destination_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.register_destination_endpoint.register_destination_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.register_destination_endpoint_request.RegisterDestinationEndpointRequest = {
            "configuration": configuration
        }
        if description is not None:
            input_["description"] = description
        if region_name is not None:
            input_["region_name"] = region_name
        if tags is not None:
            input_["tags"] = tags
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
        arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_destination_endpoint_response.GetDestinationEndpointResponse":
        """<p>Retrieves information about a destination endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to retrieve.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.get_destination_endpoint_request.GetDestinationEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_destination_endpoint_response.GetDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_destination_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_destination_endpoint.get_destination_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.get_destination_endpoint_request.GetDestinationEndpointRequest = {
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
        arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        description: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.destination_endpoint_configuration.DestinationEndpointConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_destination_endpoint_response.UpdateDestinationEndpointResponse":
        """<p>Updates the configuration of a destination endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to update.</p>
            description: <p>A description to help you identify the destination endpoint.</p>
            configuration: <p>The updated configuration settings for the destination endpoint.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.update_destination_endpoint_request.UpdateDestinationEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_destination_endpoint_response.UpdateDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_destination_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_destination_endpoint.update_destination_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.update_destination_endpoint_request.UpdateDestinationEndpointRequest = {
            "arn": arn
        }
        if description is not None:
            input_["description"] = description
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.deregister_destination_endpoint_response.DeregisterDestinationEndpointResponse":
        """<p>Deregisters a destination endpoint from MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to deregister.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.deregister_destination_endpoint_request.DeregisterDestinationEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.deregister_destination_endpoint_response.DeregisterDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.deregister_destination_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.deregister_destination_endpoint.deregister_destination_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.deregister_destination_endpoint_request.DeregisterDestinationEndpointRequest = {
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
            "capo_mediaconnect.types.destination_endpoint_filter_list.DestinationEndpointFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_destination_endpoints_response.ListDestinationEndpointsResponse":
        """<p>Retrieves a list of the destination endpoints in your account. The results are paginated. Use the NextToken value that's returned to retrieve additional results.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single request. The valid range is 1 to 100. If you don't specify a value, the service returns up to 100 results.</p>
            next_token: <p>The token that identifies the next page of results to return. Use the token that a previous request returned.</p>
            filters: <p>The filters to apply to the list of destination endpoints.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_destination_endpoints_request.ListDestinationEndpointsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_destination_endpoints_response.ListDestinationEndpointsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_destination_endpoints

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_destination_endpoints.list_destination_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDestinationEndpoints")
        )
        input_: capo_mediaconnect.types.list_destination_endpoints_request.ListDestinationEndpointsRequest = {}
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

    def connect_endpoints(
        self,
        destination_endpoint_arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        source_endpoint_arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.connect_endpoints_response.ConnectEndpointsResponse":
        """<p>Connects a source endpoint to a destination endpoint.</p>

        Args:
            destination_endpoint_arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to connect.</p>
            source_endpoint_arn: <p>The Amazon Resource Name (ARN) of the source endpoint to connect.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.connect_endpoints_request.ConnectEndpointsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.connect_endpoints_response.ConnectEndpointsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.connect_endpoints

            output, http_response = (
                capo_mediaconnect._operations.media_connect.connect_endpoints.connect_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ConnectEndpoints")
        )
        input_: capo_mediaconnect.types.connect_endpoints_request.ConnectEndpointsRequest = {
            "destination_endpoint_arn": destination_endpoint_arn,
            "source_endpoint_arn": source_endpoint_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disconnect_endpoints(
        self,
        destination_endpoint_arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        source_endpoint_arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.disconnect_endpoints_response.DisconnectEndpointsResponse":
        """<p>Disconnects a source endpoint from a destination endpoint.</p>

        Args:
            destination_endpoint_arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to disconnect.</p>
            source_endpoint_arn: <p>The Amazon Resource Name (ARN) of the source endpoint to disconnect.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.disconnect_endpoints_request.DisconnectEndpointsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.disconnect_endpoints_response.DisconnectEndpointsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.disconnect_endpoints

            output, http_response = (
                capo_mediaconnect._operations.media_connect.disconnect_endpoints.disconnect_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisconnectEndpoints")
        )
        input_: capo_mediaconnect.types.disconnect_endpoints_request.DisconnectEndpointsRequest = {
            "destination_endpoint_arn": destination_endpoint_arn,
            "source_endpoint_arn": source_endpoint_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_destination_endpoint(
        self,
        arns: "capo_mediaconnect.types.destination_endpoint_arn_list.DestinationEndpointArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_destination_endpoint_response.BatchGetDestinationEndpointResponse":
        """<p>Retrieves information about multiple destination endpoints in a single request.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of one or more destination endpoints to retrieve. You can specify from 1 to 20 ARNs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.batch_get_destination_endpoint_request.BatchGetDestinationEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.batch_get_destination_endpoint_response.BatchGetDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_destination_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.batch_get_destination_endpoint.batch_get_destination_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.batch_get_destination_endpoint_request.BatchGetDestinationEndpointRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDestinationEndpointResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        configuration: "capo_mediaconnect.types.destination_endpoint_configuration.DestinationEndpointConfiguration",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        description: Optional[str] = None,
        region_name: Optional[str] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.register_destination_endpoint_response.RegisterDestinationEndpointResponse":
        """<p>Registers a new destination endpoint in MediaConnect.</p>

        Args:
            description: <p>A description to help you identify the destination endpoint.</p>
            configuration: <p>The configuration settings for the destination endpoint.</p>
            region_name: <p>The name of the Amazon Web Services Region in which to register the destination endpoint. Defaults to the current region if not specified.</p>
            tags: <p>The tags to apply to the destination endpoint. Each tag is a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.destination_endpoint_service_quota_exceeded_exception.DestinationEndpointServiceQuotaExceededException: <p>The request would cause you to exceed a service quota for destination endpoints. Delete unused destination endpoints or request a quota increase, then try your request again.</p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.register_destination_endpoint_request.RegisterDestinationEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.register_destination_endpoint_response.RegisterDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.register_destination_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.register_destination_endpoint.async_register_destination_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.register_destination_endpoint_request.RegisterDestinationEndpointRequest = {
            "configuration": configuration
        }
        if description is not None:
            input_["description"] = description
        if region_name is not None:
            input_["region_name"] = region_name
        if tags is not None:
            input_["tags"] = tags
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
        arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_destination_endpoint_response.GetDestinationEndpointResponse":
        """<p>Retrieves information about a destination endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to retrieve.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.get_destination_endpoint_request.GetDestinationEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.get_destination_endpoint_response.GetDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_destination_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.get_destination_endpoint.async_get_destination_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.get_destination_endpoint_request.GetDestinationEndpointRequest = {
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
        arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        description: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.destination_endpoint_configuration.DestinationEndpointConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_destination_endpoint_response.UpdateDestinationEndpointResponse":
        """<p>Updates the configuration of a destination endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to update.</p>
            description: <p>A description to help you identify the destination endpoint.</p>
            configuration: <p>The updated configuration settings for the destination endpoint.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_destination_endpoint_request.UpdateDestinationEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_destination_endpoint_response.UpdateDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_destination_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_destination_endpoint.async_update_destination_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.update_destination_endpoint_request.UpdateDestinationEndpointRequest = {
            "arn": arn
        }
        if description is not None:
            input_["description"] = description
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.deregister_destination_endpoint_response.DeregisterDestinationEndpointResponse":
        """<p>Deregisters a destination endpoint from MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to deregister.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.deregister_destination_endpoint_request.DeregisterDestinationEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.deregister_destination_endpoint_response.DeregisterDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.deregister_destination_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.deregister_destination_endpoint.async_deregister_destination_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.deregister_destination_endpoint_request.DeregisterDestinationEndpointRequest = {
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
            "capo_mediaconnect.types.destination_endpoint_filter_list.DestinationEndpointFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_destination_endpoints_response.ListDestinationEndpointsResponse":
        """<p>Retrieves a list of the destination endpoints in your account. The results are paginated. Use the NextToken value that's returned to retrieve additional results.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single request. The valid range is 1 to 100. If you don't specify a value, the service returns up to 100 results.</p>
            next_token: <p>The token that identifies the next page of results to return. Use the token that a previous request returned.</p>
            filters: <p>The filters to apply to the list of destination endpoints.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_destination_endpoints_request.ListDestinationEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_destination_endpoints_response.ListDestinationEndpointsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_destination_endpoints

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_destination_endpoints.async_list_destination_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDestinationEndpoints")
        )
        input_: capo_mediaconnect.types.list_destination_endpoints_request.ListDestinationEndpointsRequest = {}
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

    async def connect_endpoints(
        self,
        destination_endpoint_arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        source_endpoint_arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.connect_endpoints_response.ConnectEndpointsResponse":
        """<p>Connects a source endpoint to a destination endpoint.</p>

        Args:
            destination_endpoint_arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to connect.</p>
            source_endpoint_arn: <p>The Amazon Resource Name (ARN) of the source endpoint to connect.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.connect_endpoints_request.ConnectEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.connect_endpoints_response.ConnectEndpointsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.connect_endpoints

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.connect_endpoints.async_connect_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ConnectEndpoints")
        )
        input_: capo_mediaconnect.types.connect_endpoints_request.ConnectEndpointsRequest = {
            "destination_endpoint_arn": destination_endpoint_arn,
            "source_endpoint_arn": source_endpoint_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disconnect_endpoints(
        self,
        destination_endpoint_arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn",
        source_endpoint_arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.disconnect_endpoints_response.DisconnectEndpointsResponse":
        """<p>Disconnects a source endpoint from a destination endpoint.</p>

        Args:
            destination_endpoint_arn: <p>The Amazon Resource Name (ARN) of the destination endpoint to disconnect.</p>
            source_endpoint_arn: <p>The Amazon Resource Name (ARN) of the source endpoint to disconnect.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.disconnect_endpoints_request.DisconnectEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.disconnect_endpoints_response.DisconnectEndpointsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.disconnect_endpoints

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.disconnect_endpoints.async_disconnect_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisconnectEndpoints")
        )
        input_: capo_mediaconnect.types.disconnect_endpoints_request.DisconnectEndpointsRequest = {
            "destination_endpoint_arn": destination_endpoint_arn,
            "source_endpoint_arn": source_endpoint_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_destination_endpoint(
        self,
        arns: "capo_mediaconnect.types.destination_endpoint_arn_list.DestinationEndpointArnList",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_destination_endpoint_response.BatchGetDestinationEndpointResponse":
        """<p>Retrieves information about multiple destination endpoints in a single request.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of one or more destination endpoints to retrieve. You can specify from 1 to 20 ARNs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.batch_get_destination_endpoint_request.BatchGetDestinationEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.batch_get_destination_endpoint_response.BatchGetDestinationEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_destination_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.batch_get_destination_endpoint.async_batch_get_destination_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetDestinationEndpoint")
        )
        input_: capo_mediaconnect.types.batch_get_destination_endpoint_request.BatchGetDestinationEndpointRequest = {
            "arns": arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
