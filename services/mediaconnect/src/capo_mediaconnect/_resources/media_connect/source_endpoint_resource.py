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
    import capo_mediaconnect.types.batch_get_source_endpoint_request
    import capo_mediaconnect.types.batch_get_source_endpoint_response
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.deregister_source_endpoint_request
    import capo_mediaconnect.types.deregister_source_endpoint_response
    import capo_mediaconnect.types.get_source_endpoint_request
    import capo_mediaconnect.types.get_source_endpoint_response
    import capo_mediaconnect.types.list_source_endpoints_request
    import capo_mediaconnect.types.list_source_endpoints_response
    import capo_mediaconnect.types.listed_source_endpoint
    import capo_mediaconnect.types.register_source_endpoint_request
    import capo_mediaconnect.types.register_source_endpoint_response
    import capo_mediaconnect.types.source_endpoint_arn
    import capo_mediaconnect.types.source_endpoint_arn_list
    import capo_mediaconnect.types.source_endpoint_configuration
    import capo_mediaconnect.types.source_endpoint_filter_list
    import capo_mediaconnect.types.update_source_endpoint_request
    import capo_mediaconnect.types.update_source_endpoint_response
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class SourceEndpointResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        configuration: "capo_mediaconnect.types.source_endpoint_configuration.SourceEndpointConfiguration",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.register_source_endpoint_response.RegisterSourceEndpointResponse":
        """<p>Registers a new source endpoint in MediaConnect.</p>

        Args:
            region_name: <p>The name of the Amazon Web Services Region in which to register the source endpoint. Defaults to the current region if not specified.</p>
            description: <p>A description to help you identify the source endpoint.</p>
            configuration: <p>The configuration settings for the source endpoint.</p>
            tags: <p>The tags to apply to the source endpoint. Each tag is a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.source_endpoint_service_quota_exceeded_exception.SourceEndpointServiceQuotaExceededException: <p>The request would cause you to exceed a service quota for source endpoints. Delete unused source endpoints or request a quota increase, then try your request again.</p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.register_source_endpoint_request.RegisterSourceEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.register_source_endpoint_response.RegisterSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.register_source_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.register_source_endpoint.register_source_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterSourceEndpoint")
        )
        input_: capo_mediaconnect.types.register_source_endpoint_request.RegisterSourceEndpointRequest = {
            "configuration": configuration
        }
        if region_name is not None:
            input_["region_name"] = region_name
        if description is not None:
            input_["description"] = description
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
        arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> (
        "capo_mediaconnect.types.get_source_endpoint_response.GetSourceEndpointResponse"
    ):
        """<p>Retrieves information about a source endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the source endpoint to retrieve.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.get_source_endpoint_request.GetSourceEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_source_endpoint_response.GetSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_source_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_source_endpoint.get_source_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSourceEndpoint")
        )
        input_: capo_mediaconnect.types.get_source_endpoint_request.GetSourceEndpointRequest = {
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
        arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        description: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.source_endpoint_configuration.SourceEndpointConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_source_endpoint_response.UpdateSourceEndpointResponse":
        """<p>Updates the configuration of a source endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the source endpoint to update.</p>
            description: <p>A description to help you identify the source endpoint.</p>
            configuration: <p>The updated configuration settings for the source endpoint.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.update_source_endpoint_request.UpdateSourceEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_source_endpoint_response.UpdateSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_source_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_source_endpoint.update_source_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateSourceEndpoint")
        )
        input_: capo_mediaconnect.types.update_source_endpoint_request.UpdateSourceEndpointRequest = {
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
        arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.deregister_source_endpoint_response.DeregisterSourceEndpointResponse":
        """<p>Deregisters a source endpoint from MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the source endpoint to deregister.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.deregister_source_endpoint_request.DeregisterSourceEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.deregister_source_endpoint_response.DeregisterSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.deregister_source_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.deregister_source_endpoint.deregister_source_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterSourceEndpoint")
        )
        input_: capo_mediaconnect.types.deregister_source_endpoint_request.DeregisterSourceEndpointRequest = {
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
            "capo_mediaconnect.types.source_endpoint_filter_list.SourceEndpointFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_source_endpoints_response.ListSourceEndpointsResponse":
        """<p>Retrieves a list of the source endpoints in your account. The results are paginated. Use the NextToken value that's returned to retrieve additional results.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single request. The valid range is 1 to 100. If you don't specify a value, the service returns up to 100 results.</p>
            next_token: <p>The token that identifies the next page of results to return. Use the token that a previous request returned.</p>
            filters: <p>The filters to apply to the list of source endpoints.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_source_endpoints_request.ListSourceEndpointsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_source_endpoints_response.ListSourceEndpointsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_source_endpoints

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_source_endpoints.list_source_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSourceEndpoints")
        )
        input_: capo_mediaconnect.types.list_source_endpoints_request.ListSourceEndpointsRequest = {}
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

    def batch_get_source_endpoint(
        self,
        arns: "capo_mediaconnect.types.source_endpoint_arn_list.SourceEndpointArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_source_endpoint_response.BatchGetSourceEndpointResponse":
        """<p>Retrieves information about multiple source endpoints in a single request.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of one or more source endpoints to retrieve. You can specify from 1 to 20 ARNs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.batch_get_source_endpoint_request.BatchGetSourceEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.batch_get_source_endpoint_response.BatchGetSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_source_endpoint

            output, http_response = (
                capo_mediaconnect._operations.media_connect.batch_get_source_endpoint.batch_get_source_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetSourceEndpoint")
        )
        input_: capo_mediaconnect.types.batch_get_source_endpoint_request.BatchGetSourceEndpointRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSourceEndpointResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        configuration: "capo_mediaconnect.types.source_endpoint_configuration.SourceEndpointConfiguration",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.register_source_endpoint_response.RegisterSourceEndpointResponse":
        """<p>Registers a new source endpoint in MediaConnect.</p>

        Args:
            region_name: <p>The name of the Amazon Web Services Region in which to register the source endpoint. Defaults to the current region if not specified.</p>
            description: <p>A description to help you identify the source endpoint.</p>
            configuration: <p>The configuration settings for the source endpoint.</p>
            tags: <p>The tags to apply to the source endpoint. Each tag is a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.source_endpoint_service_quota_exceeded_exception.SourceEndpointServiceQuotaExceededException: <p>The request would cause you to exceed a service quota for source endpoints. Delete unused source endpoints or request a quota increase, then try your request again.</p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.register_source_endpoint_request.RegisterSourceEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.register_source_endpoint_response.RegisterSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.register_source_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.register_source_endpoint.async_register_source_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterSourceEndpoint")
        )
        input_: capo_mediaconnect.types.register_source_endpoint_request.RegisterSourceEndpointRequest = {
            "configuration": configuration
        }
        if region_name is not None:
            input_["region_name"] = region_name
        if description is not None:
            input_["description"] = description
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
        arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> (
        "capo_mediaconnect.types.get_source_endpoint_response.GetSourceEndpointResponse"
    ):
        """<p>Retrieves information about a source endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the source endpoint to retrieve.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.get_source_endpoint_request.GetSourceEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.get_source_endpoint_response.GetSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_source_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.get_source_endpoint.async_get_source_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSourceEndpoint")
        )
        input_: capo_mediaconnect.types.get_source_endpoint_request.GetSourceEndpointRequest = {
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
        arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        description: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.source_endpoint_configuration.SourceEndpointConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_source_endpoint_response.UpdateSourceEndpointResponse":
        """<p>Updates the configuration of a source endpoint.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the source endpoint to update.</p>
            description: <p>A description to help you identify the source endpoint.</p>
            configuration: <p>The updated configuration settings for the source endpoint.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_source_endpoint_request.UpdateSourceEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_source_endpoint_response.UpdateSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_source_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_source_endpoint.async_update_source_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateSourceEndpoint")
        )
        input_: capo_mediaconnect.types.update_source_endpoint_request.UpdateSourceEndpointRequest = {
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
        arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.deregister_source_endpoint_response.DeregisterSourceEndpointResponse":
        """<p>Deregisters a source endpoint from MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the source endpoint to deregister.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.deregister_source_endpoint_request.DeregisterSourceEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.deregister_source_endpoint_response.DeregisterSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.deregister_source_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.deregister_source_endpoint.async_deregister_source_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterSourceEndpoint")
        )
        input_: capo_mediaconnect.types.deregister_source_endpoint_request.DeregisterSourceEndpointRequest = {
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
            "capo_mediaconnect.types.source_endpoint_filter_list.SourceEndpointFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_source_endpoints_response.ListSourceEndpointsResponse":
        """<p>Retrieves a list of the source endpoints in your account. The results are paginated. Use the NextToken value that's returned to retrieve additional results.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single request. The valid range is 1 to 100. If you don't specify a value, the service returns up to 100 results.</p>
            next_token: <p>The token that identifies the next page of results to return. Use the token that a previous request returned.</p>
            filters: <p>The filters to apply to the list of source endpoints.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_source_endpoints_request.ListSourceEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_source_endpoints_response.ListSourceEndpointsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_source_endpoints

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_source_endpoints.async_list_source_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSourceEndpoints")
        )
        input_: capo_mediaconnect.types.list_source_endpoints_request.ListSourceEndpointsRequest = {}
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

    async def batch_get_source_endpoint(
        self,
        arns: "capo_mediaconnect.types.source_endpoint_arn_list.SourceEndpointArnList",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_source_endpoint_response.BatchGetSourceEndpointResponse":
        """<p>Retrieves information about multiple source endpoints in a single request.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of one or more source endpoints to retrieve. You can specify from 1 to 20 ARNs.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.batch_get_source_endpoint_request.BatchGetSourceEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.batch_get_source_endpoint_response.BatchGetSourceEndpointResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_source_endpoint

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.batch_get_source_endpoint.async_batch_get_source_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetSourceEndpoint")
        )
        input_: capo_mediaconnect.types.batch_get_source_endpoint_request.BatchGetSourceEndpointRequest = {
            "arns": arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
