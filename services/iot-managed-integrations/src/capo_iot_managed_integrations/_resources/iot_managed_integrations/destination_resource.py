from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.create_destination_request
    import capo_iot_managed_integrations.types.create_destination_response
    import capo_iot_managed_integrations.types.delete_destination_request
    import capo_iot_managed_integrations.types.delivery_destination_arn
    import capo_iot_managed_integrations.types.delivery_destination_role_arn
    import capo_iot_managed_integrations.types.delivery_destination_type
    import capo_iot_managed_integrations.types.destination_description
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.destination_summary
    import capo_iot_managed_integrations.types.get_destination_request
    import capo_iot_managed_integrations.types.get_destination_response
    import capo_iot_managed_integrations.types.list_destinations_request
    import capo_iot_managed_integrations.types.list_destinations_response
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.update_destination_request
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class DestinationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create_destination(
        self,
        delivery_destination_arn: "capo_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn",
        delivery_destination_type: "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType",
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        role_arn: "capo_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse":
        """<p> Create a notification destination such as Kinesis Data Streams that receive events and notifications from Managed integrations. Managed integrations uses the destination to determine where to deliver notifications.</p>

        Args:
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            name: <p>The name of the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            description: <p>The description of the customer-managed destination.</p>
            tags: <p>A set of key/value pairs that are used to manage the destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_destination

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_destination.create_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_destination_request

            return capo_iot_managed_integrations.types.create_destination_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDestination", redact_input=_redact_input),
        )
        input_: capo_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest = {
            "delivery_destination_arn": delivery_destination_arn,
            "delivery_destination_type": delivery_destination_type,
            "name": name,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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

    def delete_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification destination specified by name. </p>

        Args:
            name: <p>The id of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_destination

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_destination.delete_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDestination")
        )
        input_: capo_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_destination_response.GetDestinationResponse":
        """<p>Gets a destination by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_destination_request.GetDestinationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_destination_response.GetDestinationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_destination

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_destination.get_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_destination_response.GetDestinationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_destination_response

            return capo_iot_managed_integrations.types.get_destination_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDestination", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_destination_request.GetDestinationRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_destinations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse":
        """<p> List all notification destinations.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_destinations

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_destinations.list_destinations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDestinations")
        )
        input_: capo_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        delivery_destination_arn: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn"
        ] = None,
        delivery_destination_type: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType"
        ] = None,
        role_arn: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
    ) -> None:
        """<p> Update a destination specified by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            description: <p>The description of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_destination

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.update_destination.update_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDestination")
        )
        input_: capo_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest = {
            "name": name
        }
        if delivery_destination_arn is not None:
            input_["delivery_destination_arn"] = delivery_destination_arn
        if delivery_destination_type is not None:
            input_["delivery_destination_type"] = delivery_destination_type
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDestinationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create_destination(
        self,
        delivery_destination_arn: "capo_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn",
        delivery_destination_type: "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType",
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        role_arn: "capo_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse":
        """<p> Create a notification destination such as Kinesis Data Streams that receive events and notifications from Managed integrations. Managed integrations uses the destination to determine where to deliver notifications.</p>

        Args:
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            name: <p>The name of the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            description: <p>The description of the customer-managed destination.</p>
            tags: <p>A set of key/value pairs that are used to manage the destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_destination.async_create_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_destination_request

            return capo_iot_managed_integrations.types.create_destination_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateDestination", redact_input=_redact_input),
        )
        input_: capo_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest = {
            "delivery_destination_arn": delivery_destination_arn,
            "delivery_destination_type": delivery_destination_type,
            "name": name,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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

    async def delete_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification destination specified by name. </p>

        Args:
            name: <p>The id of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_destination.async_delete_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDestination")
        )
        input_: capo_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_destination_response.GetDestinationResponse":
        """<p>Gets a destination by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_destination_request.GetDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_destination_response.GetDestinationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_destination.async_get_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_destination_response.GetDestinationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_destination_response

            return capo_iot_managed_integrations.types.get_destination_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDestination", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_destination_request.GetDestinationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_destinations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse":
        """<p> List all notification destinations.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_destinations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_destinations.async_list_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDestinations")
        )
        input_: capo_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        delivery_destination_arn: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn"
        ] = None,
        delivery_destination_type: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType"
        ] = None,
        role_arn: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
    ) -> None:
        """<p> Update a destination specified by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            description: <p>The description of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_destination.async_update_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateDestination")
        )
        input_: capo_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest = {
            "name": name
        }
        if delivery_destination_arn is not None:
            input_["delivery_destination_arn"] = delivery_destination_arn
        if delivery_destination_type is not None:
            input_["delivery_destination_type"] = delivery_destination_type
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
