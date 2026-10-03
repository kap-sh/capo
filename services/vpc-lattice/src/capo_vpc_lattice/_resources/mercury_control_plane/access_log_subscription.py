from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_vpc_lattice._auth._signers
import capo_vpc_lattice._auth._sigv4
from capo_vpc_lattice._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_destination_arn
    import capo_vpc_lattice.types.access_log_subscription_identifier
    import capo_vpc_lattice.types.access_log_subscription_summary
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.create_access_log_subscription_request
    import capo_vpc_lattice.types.create_access_log_subscription_response
    import capo_vpc_lattice.types.delete_access_log_subscription_request
    import capo_vpc_lattice.types.delete_access_log_subscription_response
    import capo_vpc_lattice.types.get_access_log_subscription_request
    import capo_vpc_lattice.types.get_access_log_subscription_response
    import capo_vpc_lattice.types.list_access_log_subscriptions_request
    import capo_vpc_lattice.types.list_access_log_subscriptions_response
    import capo_vpc_lattice.types.max_results
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.resource_identifier
    import capo_vpc_lattice.types.service_network_log_type
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.update_access_log_subscription_request
    import capo_vpc_lattice.types.update_access_log_subscription_response
    from capo_vpc_lattice._services.async_vpc_lattice import (
        AsyncVPCLatticeClient,
        AsyncVPCLatticeClientConfig,
    )
    from capo_vpc_lattice._services.vpc_lattice import (
        VPCLatticeClient,
        VPCLatticeClientConfig,
    )


class AccessLogSubscription:
    def __init__(self, service: VPCLatticeClient) -> None:
        self._service = service

    def create(
        self,
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        destination_arn: "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        service_network_log_type: Optional[
            "capo_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse":
        """<p>Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner can only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html">Access logs</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.</p>
            service_network_log_type: <p>The type of log that monitors your Amazon VPC Lattice service networks.</p>
            tags: <p>The tags for the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription.create_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest = {
            "resource_identifier": resource_identifier,
            "destination_arn": destination_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if service_network_log_type is not None:
            input_["service_network_log_type"] = service_network_log_type
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
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse":
        """<p>Retrieves information about the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription.get_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier
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
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        destination_arn: "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse":
        """<p>Updates the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the access log destination.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription.update_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier,
            "destination_arn": destination_arn,
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
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse":
        """<p>Deletes the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription.delete_access_log_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier
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
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[VPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse":
        """<p>Lists the access log subscriptions for the specified service network or service.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions

            output, http_response = (
                capo_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions.list_access_log_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest = {
            "resource_identifier": resource_identifier
        }
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


class AsyncAccessLogSubscription:
    def __init__(self, service: AsyncVPCLatticeClient) -> None:
        self._service = service

    async def create(
        self,
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        destination_arn: "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        client_token: Optional[
            "capo_vpc_lattice.types.client_token.ClientToken"
        ] = None,
        service_network_log_type: Optional[
            "capo_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
        ] = None,
        tags: Optional["capo_vpc_lattice.types.tag_map.TagMap"] = None,
    ) -> "capo_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse":
        """<p>Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner can only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see <a href="https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html">Access logs</a> in the <i>Amazon VPC Lattice User Guide</i>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.</p>
            service_network_log_type: <p>The type of log that monitors your Amazon VPC Lattice service networks.</p>
            tags: <p>The tags for the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.create_access_log_subscription_response.CreateAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.create_access_log_subscription.async_create_access_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.create_access_log_subscription_request.CreateAccessLogSubscriptionRequest = {
            "resource_identifier": resource_identifier,
            "destination_arn": destination_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if service_network_log_type is not None:
            input_["service_network_log_type"] = service_network_log_type
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
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse":
        """<p>Retrieves information about the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.get_access_log_subscription_response.GetAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.get_access_log_subscription.async_get_access_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.get_access_log_subscription_request.GetAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier
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
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        destination_arn: "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse":
        """<p>Updates the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>
            destination_arn: <p>The Amazon Resource Name (ARN) of the access log destination.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. Updating or deleting a resource can cause an inconsistent state.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.update_access_log_subscription_response.UpdateAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.update_access_log_subscription.async_update_access_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.update_access_log_subscription_request.UpdateAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier,
            "destination_arn": destination_arn,
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
        access_log_subscription_identifier: "capo_vpc_lattice.types.access_log_subscription_identifier.AccessLogSubscriptionIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
    ) -> "capo_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse":
        """<p>Deletes the specified access log subscription.</p>

        Args:
            access_log_subscription_identifier: <p>The ID or ARN of the access log subscription.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.delete_access_log_subscription_response.DeleteAccessLogSubscriptionResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.delete_access_log_subscription.async_delete_access_log_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.delete_access_log_subscription_request.DeleteAccessLogSubscriptionRequest = {
            "access_log_subscription_identifier": access_log_subscription_identifier
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
        resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncVPCLatticeClientConfig] = None,
        max_results: Optional["capo_vpc_lattice.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_vpc_lattice.types.next_token.NextToken"] = None,
    ) -> "capo_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse":
        """<p>Lists the access log subscriptions for the specified service network or service.</p>

        Args:
            resource_identifier: <p>The ID or ARN of the service network or service.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A pagination token for the next page of results.</p>

        Raises:
            capo_vpc_lattice.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action.</p>
            capo_vpc_lattice.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_vpc_lattice.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_vpc_lattice.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_vpc_lattice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_vpc_lattice.types.list_access_log_subscriptions_response.ListAccessLogSubscriptionsResponse"
        ]:
            import capo_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions

            (
                output,
                http_response,
            ) = await capo_vpc_lattice._operations.mercury_control_plane.list_access_log_subscriptions.async_list_access_log_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_vpc_lattice.types.list_access_log_subscriptions_request.ListAccessLogSubscriptionsRequest = {
            "resource_identifier": resource_identifier
        }
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
