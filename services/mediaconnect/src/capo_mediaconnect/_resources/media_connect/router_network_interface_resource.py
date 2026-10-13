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
    import capo_mediaconnect.types.batch_get_router_network_interface_request
    import capo_mediaconnect.types.batch_get_router_network_interface_response
    import capo_mediaconnect.types.client_token
    import capo_mediaconnect.types.create_router_network_interface_request
    import capo_mediaconnect.types.create_router_network_interface_response
    import capo_mediaconnect.types.delete_router_network_interface_request
    import capo_mediaconnect.types.delete_router_network_interface_response
    import capo_mediaconnect.types.get_router_network_interface_request
    import capo_mediaconnect.types.get_router_network_interface_response
    import capo_mediaconnect.types.list_router_network_interfaces_request
    import capo_mediaconnect.types.list_router_network_interfaces_response
    import capo_mediaconnect.types.listed_router_network_interface
    import capo_mediaconnect.types.router_network_interface_arn
    import capo_mediaconnect.types.router_network_interface_arn_list
    import capo_mediaconnect.types.router_network_interface_configuration
    import capo_mediaconnect.types.router_network_interface_filter_list
    import capo_mediaconnect.types.update_router_network_interface_request
    import capo_mediaconnect.types.update_router_network_interface_response
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class RouterNetworkInterfaceResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse":
        """<p>Creates a new router network interface in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router network interface.</p>
            configuration: <p>The configuration settings for the router network interface.</p>
            region_name: <p>The Amazon Web Services Region for the router network interface. Defaults to the current region if not specified.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router network interface.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_network_interface_service_quota_exceeded_exception.RouterNetworkInterfaceServiceQuotaExceededException: <p>The request to create a new router network interface would exceed the service quotas (limits) set for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_router_network_interface.create_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest = {
            "name": name,
            "configuration": configuration,
        }
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
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about a specific router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to retrieve information about.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.get_router_network_interface.get_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest = {
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
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse":
        """<p>Updates the configuration of an existing router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to update.</p>
            name: <p>The updated name for the router network interface.</p>
            configuration: <p>The updated configuration settings for the router network interface. Changing the type of the configuration is not supported.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_router_network_interface.update_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
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
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse":
        """<p>Deletes a router network interface from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to delete.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_router_network_interface.delete_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest = {
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
            "capo_mediaconnect.types.router_network_interface_filter_list.RouterNetworkInterfaceFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse":
        """<p>Retrieves a list of router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router network interfaces to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router network interfaces.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_network_interfaces

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_router_network_interfaces.list_router_network_interfaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRouterNetworkInterfaces")
        )
        input_: capo_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest = {}
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

    def batch_get_router_network_interface(
        self,
        arns: "capo_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about multiple router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router network interfaces you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_network_interface

            output, http_response = (
                capo_mediaconnect._operations.media_connect.batch_get_router_network_interface.batch_get_router_network_interface(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest = {
            "arns": arns
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRouterNetworkInterfaceResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        configuration: "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        region_name: Optional[str] = None,
        tags: Optional["capo_mediaconnect.types.__map_of_string.__mapOfString"] = None,
        client_token: Optional[
            "capo_mediaconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse":
        """<p>Creates a new router network interface in AWS Elemental MediaConnect.</p>

        Args:
            name: <p>The name of the router network interface.</p>
            configuration: <p>The configuration settings for the router network interface.</p>
            region_name: <p>The Amazon Web Services Region for the router network interface. Defaults to the current region if not specified.</p>
            tags: <p>Key-value pairs that can be used to tag and organize this router network interface.</p>
            client_token: <p>A unique identifier for the request to ensure idempotency.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.router_network_interface_service_quota_exceeded_exception.RouterNetworkInterfaceServiceQuotaExceededException: <p>The request to create a new router network interface would exceed the service quotas (limits) set for the account. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.create_router_network_interface_response.CreateRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_router_network_interface

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.create_router_network_interface.async_create_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.create_router_network_interface_request.CreateRouterNetworkInterfaceRequest = {
            "name": name,
            "configuration": configuration,
        }
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
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about a specific router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to retrieve information about.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.get_router_network_interface_response.GetRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.get_router_network_interface

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.get_router_network_interface.async_get_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.get_router_network_interface_request.GetRouterNetworkInterfaceRequest = {
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
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        name: Optional[str] = None,
        configuration: Optional[
            "capo_mediaconnect.types.router_network_interface_configuration.RouterNetworkInterfaceConfiguration"
        ] = None,
    ) -> "capo_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse":
        """<p>Updates the configuration of an existing router network interface in AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to update.</p>
            name: <p>The updated name for the router network interface.</p>
            configuration: <p>The updated configuration settings for the router network interface. Changing the type of the configuration is not supported.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_router_network_interface_response.UpdateRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_router_network_interface

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_router_network_interface.async_update_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.update_router_network_interface_request.UpdateRouterNetworkInterfaceRequest = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
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
        arn: "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse":
        """<p>Deletes a router network interface from AWS Elemental MediaConnect.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the router network interface that you want to delete.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.delete_router_network_interface_response.DeleteRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_router_network_interface

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.delete_router_network_interface.async_delete_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.delete_router_network_interface_request.DeleteRouterNetworkInterfaceRequest = {
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
            "capo_mediaconnect.types.router_network_interface_filter_list.RouterNetworkInterfaceFilterList"
        ] = None,
    ) -> "capo_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse":
        """<p>Retrieves a list of router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            max_results: <p>The maximum number of router network interfaces to return in the response.</p>
            next_token: <p>A token used to retrieve the next page of results.</p>
            filters: <p>The filters to apply when retrieving the list of router network interfaces.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_router_network_interfaces_response.ListRouterNetworkInterfacesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_router_network_interfaces

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_router_network_interfaces.async_list_router_network_interfaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRouterNetworkInterfaces")
        )
        input_: capo_mediaconnect.types.list_router_network_interfaces_request.ListRouterNetworkInterfacesRequest = {}
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

    async def batch_get_router_network_interface(
        self,
        arns: "capo_mediaconnect.types.router_network_interface_arn_list.RouterNetworkInterfaceArnList",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse":
        """<p>Retrieves information about multiple router network interfaces in AWS Elemental MediaConnect.</p>

        Args:
            arns: <p>The Amazon Resource Names (ARNs) of the router network interfaces you want to retrieve information about.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.batch_get_router_network_interface_response.BatchGetRouterNetworkInterfaceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.batch_get_router_network_interface

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.batch_get_router_network_interface.async_batch_get_router_network_interface(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchGetRouterNetworkInterface")
        )
        input_: capo_mediaconnect.types.batch_get_router_network_interface_request.BatchGetRouterNetworkInterfaceRequest = {
            "arns": arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
