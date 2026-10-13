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
    import capo_mediaconnect.types.bridge_placement
    import capo_mediaconnect.types.deregister_gateway_instance_request
    import capo_mediaconnect.types.deregister_gateway_instance_response
    import capo_mediaconnect.types.describe_gateway_instance_request
    import capo_mediaconnect.types.describe_gateway_instance_response
    import capo_mediaconnect.types.gateway_instance_arn
    import capo_mediaconnect.types.list_gateway_instances_request
    import capo_mediaconnect.types.list_gateway_instances_response
    import capo_mediaconnect.types.listed_gateway_instance
    import capo_mediaconnect.types.max_results
    import capo_mediaconnect.types.update_gateway_instance_request
    import capo_mediaconnect.types.update_gateway_instance_response
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class GatewayInstanceResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def read(
        self,
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse":
        """<p> Displays the details of an instance. </p>

        Args:
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway instance that you want to describe.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_gateway_instance

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_gateway_instance.describe_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGatewayInstance")
        )
        input_: capo_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
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
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        bridge_placement: Optional[
            "capo_mediaconnect.types.bridge_placement.BridgePlacement"
        ] = None,
    ) -> "capo_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse":
        """<p>Updates an existing gateway instance. </p>

        Args:
            bridge_placement: <p>The state of the instance. <code>ACTIVE</code> or <code>INACTIVE</code>. </p>
            gateway_instance_arn: <p>The Amazon Resource Name (ARN) of the gateway instance that you want to update. </p>

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
            req: "OperationRequest[capo_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_gateway_instance

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_gateway_instance.update_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGatewayInstance")
        )
        input_: capo_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
        }
        if bridge_placement is not None:
            input_["bridge_placement"] = bridge_placement

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse":
        """<p> Deregisters an instance. Before you deregister an instance, all bridges running on the instance must be stopped. If you want to deregister an instance without stopping the bridges, you must use the --force option.</p>

        Args:
            force: <p> Force the deregistration of an instance. Force will deregister an instance, even if there are bridges running on it.</p>
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway that contains the instance that you want to deregister.</p>

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
            req: "OperationRequest[capo_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.deregister_gateway_instance

            output, http_response = (
                capo_mediaconnect._operations.media_connect.deregister_gateway_instance.deregister_gateway_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterGatewayInstance")
        )
        input_: capo_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
        }
        if force is not None:
            input_["force"] = force

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
        filter_arn: Optional[str] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse":
        """<p> Displays a list of instances associated with the Amazon Web Services account. This request returns a paginated result. You can use the filterArn property to display only the instances associated with the selected Gateway Amazon Resource Name (ARN).</p>

        Args:
            filter_arn: <p> Filter the list results to display only the instances associated with the selected Gateway ARN.</p>
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a ListInstances request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListInstances</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListInstances</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_gateway_instances

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_gateway_instances.list_gateway_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGatewayInstances")
        )
        input_: capo_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest = {}
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
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


class AsyncGatewayInstanceResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def read(
        self,
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse":
        """<p> Displays the details of an instance. </p>

        Args:
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway instance that you want to describe.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.describe_gateway_instance_response.DescribeGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_gateway_instance

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.describe_gateway_instance.async_describe_gateway_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeGatewayInstance")
        )
        input_: capo_mediaconnect.types.describe_gateway_instance_request.DescribeGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
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
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        bridge_placement: Optional[
            "capo_mediaconnect.types.bridge_placement.BridgePlacement"
        ] = None,
    ) -> "capo_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse":
        """<p>Updates an existing gateway instance. </p>

        Args:
            bridge_placement: <p>The state of the instance. <code>ACTIVE</code> or <code>INACTIVE</code>. </p>
            gateway_instance_arn: <p>The Amazon Resource Name (ARN) of the gateway instance that you want to update. </p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_gateway_instance_response.UpdateGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_gateway_instance

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_gateway_instance.async_update_gateway_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGatewayInstance")
        )
        input_: capo_mediaconnect.types.update_gateway_instance_request.UpdateGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
        }
        if bridge_placement is not None:
            input_["bridge_placement"] = bridge_placement

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        gateway_instance_arn: "capo_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse":
        """<p> Deregisters an instance. Before you deregister an instance, all bridges running on the instance must be stopped. If you want to deregister an instance without stopping the bridges, you must use the --force option.</p>

        Args:
            force: <p> Force the deregistration of an instance. Force will deregister an instance, even if there are bridges running on it.</p>
            gateway_instance_arn: <p> The Amazon Resource Name (ARN) of the gateway that contains the instance that you want to deregister.</p>

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
            req: "AsyncOperationRequest[capo_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.deregister_gateway_instance_response.DeregisterGatewayInstanceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.deregister_gateway_instance

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.deregister_gateway_instance.async_deregister_gateway_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterGatewayInstance")
        )
        input_: capo_mediaconnect.types.deregister_gateway_instance_request.DeregisterGatewayInstanceRequest = {
            "gateway_instance_arn": gateway_instance_arn
        }
        if force is not None:
            input_["force"] = force

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
        filter_arn: Optional[str] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse":
        """<p> Displays a list of instances associated with the Amazon Web Services account. This request returns a paginated result. You can use the filterArn property to display only the instances associated with the selected Gateway Amazon Resource Name (ARN).</p>

        Args:
            filter_arn: <p> Filter the list results to display only the instances associated with the selected Gateway ARN.</p>
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a ListInstances request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListInstances</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListInstances</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_gateway_instances_response.ListGatewayInstancesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_gateway_instances

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_gateway_instances.async_list_gateway_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGatewayInstances")
        )
        input_: capo_mediaconnect.types.list_gateway_instances_request.ListGatewayInstancesRequest = {}
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
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
