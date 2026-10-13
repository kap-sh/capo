from __future__ import annotations

from typing import TYPE_CHECKING, Optional

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
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.deregister_account_association_request
    import capo_iot_managed_integrations.types.device_discovery_id
    import capo_iot_managed_integrations.types.list_managed_thing_account_associations_request
    import capo_iot_managed_integrations.types.list_managed_thing_account_associations_response
    import capo_iot_managed_integrations.types.managed_thing_association
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.register_account_association_request
    import capo_iot_managed_integrations.types.register_account_association_response
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class ManagedThingAssociationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def deregister_account_association(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deregister an account association from a managed thing.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to be deregistered from the account association.</p>
            account_association_id: <p>The unique identifier of the account association to be deregistered.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.deregister_account_association_request.DeregisterAccountAssociationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.deregister_account_association

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.deregister_account_association.deregister_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterAccountAssociation")
        )
        input_: capo_iot_managed_integrations.types.deregister_account_association_request.DeregisterAccountAssociationRequest = {
            "managed_thing_id": managed_thing_id,
            "account_association_id": account_association_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_managed_thing_account_associations(
        self,
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        managed_thing_id: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        account_association_id: Optional[
            "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_thing_account_associations_response.ListManagedThingAccountAssociationsResponse":
        """<p>Lists all account associations for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to list account associations for.</p>
            account_association_id: <p>The identifier of the account association to filter results by. When specified, only associations with this account association ID will be returned.</p>
            max_results: <p>The maximum number of account associations to return in a single response.</p>
            next_token: <p>A token used for pagination of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_managed_thing_account_associations_request.ListManagedThingAccountAssociationsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_managed_thing_account_associations_response.ListManagedThingAccountAssociationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_account_associations

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_account_associations.list_managed_thing_account_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListManagedThingAccountAssociations")
        )
        input_: capo_iot_managed_integrations.types.list_managed_thing_account_associations_request.ListManagedThingAccountAssociationsRequest = {}
        if managed_thing_id is not None:
            input_["managed_thing_id"] = managed_thing_id
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id
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

    def register_account_association(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        device_discovery_id: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.register_account_association_response.RegisterAccountAssociationResponse":
        """<p>Registers an account association with a managed thing, establishing a connection between a device and a third-party account.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to register with the account association.</p>
            account_association_id: <p>The identifier of the account association to register with the managed thing.</p>
            device_discovery_id: <p>The identifier of the device discovery job associated with this registration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.register_account_association_request.RegisterAccountAssociationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.register_account_association_response.RegisterAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.register_account_association

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.register_account_association.register_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterAccountAssociation")
        )
        input_: capo_iot_managed_integrations.types.register_account_association_request.RegisterAccountAssociationRequest = {
            "managed_thing_id": managed_thing_id,
            "account_association_id": account_association_id,
            "device_discovery_id": device_discovery_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncManagedThingAssociationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def deregister_account_association(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deregister an account association from a managed thing.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to be deregistered from the account association.</p>
            account_association_id: <p>The unique identifier of the account association to be deregistered.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.deregister_account_association_request.DeregisterAccountAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.deregister_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.deregister_account_association.async_deregister_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterAccountAssociation")
        )
        input_: capo_iot_managed_integrations.types.deregister_account_association_request.DeregisterAccountAssociationRequest = {
            "managed_thing_id": managed_thing_id,
            "account_association_id": account_association_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_thing_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        managed_thing_id: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        account_association_id: Optional[
            "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_thing_account_associations_response.ListManagedThingAccountAssociationsResponse":
        """<p>Lists all account associations for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to list account associations for.</p>
            account_association_id: <p>The identifier of the account association to filter results by. When specified, only associations with this account association ID will be returned.</p>
            max_results: <p>The maximum number of account associations to return in a single response.</p>
            next_token: <p>A token used for pagination of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_managed_thing_account_associations_request.ListManagedThingAccountAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_managed_thing_account_associations_response.ListManagedThingAccountAssociationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_account_associations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_account_associations.async_list_managed_thing_account_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListManagedThingAccountAssociations")
        )
        input_: capo_iot_managed_integrations.types.list_managed_thing_account_associations_request.ListManagedThingAccountAssociationsRequest = {}
        if managed_thing_id is not None:
            input_["managed_thing_id"] = managed_thing_id
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id
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

    async def register_account_association(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        device_discovery_id: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.register_account_association_response.RegisterAccountAssociationResponse":
        """<p>Registers an account association with a managed thing, establishing a connection between a device and a third-party account.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to register with the account association.</p>
            account_association_id: <p>The identifier of the account association to register with the managed thing.</p>
            device_discovery_id: <p>The identifier of the device discovery job associated with this registration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.register_account_association_request.RegisterAccountAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.register_account_association_response.RegisterAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.register_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.register_account_association.async_register_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterAccountAssociation")
        )
        input_: capo_iot_managed_integrations.types.register_account_association_request.RegisterAccountAssociationRequest = {
            "managed_thing_id": managed_thing_id,
            "account_association_id": account_association_id,
            "device_discovery_id": device_discovery_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
