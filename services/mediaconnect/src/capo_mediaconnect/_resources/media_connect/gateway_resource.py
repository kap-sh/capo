from __future__ import annotations

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
    import capo_mediaconnect.types.__list_of_gateway_network
    import capo_mediaconnect.types.__list_of_string
    import capo_mediaconnect.types.create_gateway_request
    import capo_mediaconnect.types.create_gateway_response
    import capo_mediaconnect.types.delete_gateway_request
    import capo_mediaconnect.types.delete_gateway_response
    import capo_mediaconnect.types.describe_gateway_request
    import capo_mediaconnect.types.describe_gateway_response
    import capo_mediaconnect.types.gateway_arn
    import capo_mediaconnect.types.list_gateways_request
    import capo_mediaconnect.types.list_gateways_response
    import capo_mediaconnect.types.listed_gateway
    import capo_mediaconnect.types.max_results
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class GatewayResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        egress_cidr_blocks: Optional[
            "capo_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
        name: Optional[str] = None,
        networks: Optional[
            "capo_mediaconnect.types.__list_of_gateway_network.__listOfGatewayNetwork"
        ] = None,
    ) -> "capo_mediaconnect.types.create_gateway_response.CreateGatewayResponse":
        """<p> Creates a new gateway. The request must include at least one network (up to four).</p>

        Args:
            egress_cidr_blocks: <p> The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>
            name: <p> The name of the gateway. This name can not be modified after the gateway is created.</p>
            networks: <p> The list of networks that you want to add to the gateway.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.create_gateway420_exception.CreateGateway420Exception: <p>Exception raised by Elemental MediaConnect when creating the gateway. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_gateway_request.CreateGatewayRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_gateway

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGateway")
        )
        input_: capo_mediaconnect.types.create_gateway_request.CreateGatewayRequest = {}
        if egress_cidr_blocks is not None:
            input_["egress_cidr_blocks"] = egress_cidr_blocks
        if name is not None:
            input_["name"] = name
        if networks is not None:
            input_["networks"] = networks

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        gateway_arn: "capo_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse":
        """<p> Displays the details of a gateway. The response includes the gateway Amazon Resource Name (ARN), name, and CIDR blocks, as well as details about the networks.</p>

        Args:
            gateway_arn: <p> The ARN of the gateway that you want to describe.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_gateway

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_gateway.describe_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGateway")
        )
        input_: capo_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        gateway_arn: "capo_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse":
        """<p> Deletes a gateway. Before you can delete a gateway, you must deregister its instances and delete its bridges.</p>

        Args:
            gateway_arn: <p> The Amazon Resource Name (ARN) of the gateway that you want to delete.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_gateway

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGateway")
        )
        input_: capo_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest = {
            "gateway_arn": gateway_arn
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
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_gateways_response.ListGatewaysResponse":
        """<p> Displays a list of gateways that are associated with this account. This request returns a paginated result.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListGateways</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_gateways_request.ListGatewaysRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_gateways

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGateways")
        )
        input_: capo_mediaconnect.types.list_gateways_request.ListGatewaysRequest = {}
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


class AsyncGatewayResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        egress_cidr_blocks: Optional[
            "capo_mediaconnect.types.__list_of_string.__listOfString"
        ] = None,
        name: Optional[str] = None,
        networks: Optional[
            "capo_mediaconnect.types.__list_of_gateway_network.__listOfGatewayNetwork"
        ] = None,
    ) -> "capo_mediaconnect.types.create_gateway_response.CreateGatewayResponse":
        """<p> Creates a new gateway. The request must include at least one network (up to four).</p>

        Args:
            egress_cidr_blocks: <p> The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>
            name: <p> The name of the gateway. This name can not be modified after the gateway is created.</p>
            networks: <p> The list of networks that you want to add to the gateway.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.create_gateway420_exception.CreateGateway420Exception: <p>Exception raised by Elemental MediaConnect when creating the gateway. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.create_gateway_request.CreateGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_gateway

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.create_gateway.async_create_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGateway")
        )
        input_: capo_mediaconnect.types.create_gateway_request.CreateGatewayRequest = {}
        if egress_cidr_blocks is not None:
            input_["egress_cidr_blocks"] = egress_cidr_blocks
        if name is not None:
            input_["name"] = name
        if networks is not None:
            input_["networks"] = networks

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        gateway_arn: "capo_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse":
        """<p> Displays the details of a gateway. The response includes the gateway Amazon Resource Name (ARN), name, and CIDR blocks, as well as details about the networks.</p>

        Args:
            gateway_arn: <p> The ARN of the gateway that you want to describe.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_gateway

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.describe_gateway.async_describe_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGateway")
        )
        input_: capo_mediaconnect.types.describe_gateway_request.DescribeGatewayRequest = {
            "gateway_arn": gateway_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        gateway_arn: "capo_mediaconnect.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse":
        """<p> Deletes a gateway. Before you can delete a gateway, you must deregister its instances and delete its bridges.</p>

        Args:
            gateway_arn: <p> The Amazon Resource Name (ARN) of the gateway that you want to delete.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_gateway

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.delete_gateway.async_delete_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGateway")
        )
        input_: capo_mediaconnect.types.delete_gateway_request.DeleteGatewayRequest = {
            "gateway_arn": gateway_arn
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
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_gateways_response.ListGatewaysResponse":
        """<p> Displays a list of gateways that are associated with this account. This request returns a paginated result.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListGateways</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_gateways_request.ListGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_gateways

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_gateways.async_list_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGateways")
        )
        input_: capo_mediaconnect.types.list_gateways_request.ListGatewaysRequest = {}
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
