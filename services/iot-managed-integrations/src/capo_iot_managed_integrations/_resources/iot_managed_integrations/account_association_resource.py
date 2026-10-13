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
    import capo_iot_managed_integrations.types.account_association_description
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.account_association_item
    import capo_iot_managed_integrations.types.account_association_name
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.create_account_association_request
    import capo_iot_managed_integrations.types.create_account_association_response
    import capo_iot_managed_integrations.types.delete_account_association_request
    import capo_iot_managed_integrations.types.general_authorization_name
    import capo_iot_managed_integrations.types.get_account_association_request
    import capo_iot_managed_integrations.types.get_account_association_response
    import capo_iot_managed_integrations.types.list_account_associations_request
    import capo_iot_managed_integrations.types.list_account_associations_response
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.start_account_association_refresh_request
    import capo_iot_managed_integrations.types.start_account_association_refresh_response
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.update_account_association_request
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class AccountAssociationResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        connector_destination_id: "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        general_authorization: Optional[
            "capo_iot_managed_integrations.types.general_authorization_name.GeneralAuthorizationName"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse":
        """<p>Creates a new account association via the destination id.</p>

        Args:
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            connector_destination_id: <p>The identifier of the connector destination.</p>
            name: <p>The name of the destination for the new account association.</p>
            description: <p>A description of the account association request.</p>
            tags: <p>A set of key/value pairs that are used to manage the account association.</p>
            general_authorization: <p>The General Authorization reference by authorization material name.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_account_association

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_account_association.create_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_account_association_request

            return capo_iot_managed_integrations.types.create_account_association_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_account_association_response

            return capo_iot_managed_integrations.types.create_account_association_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAccountAssociation",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest = {
            "connector_destination_id": connector_destination_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if general_authorization is not None:
            input_["general_authorization"] = general_authorization

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse":
        """<p>Get an account association for an Amazon Web Services account linked to a customer-managed destination.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to retrieve.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_account_association

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_account_association.get_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_account_association_response

            return capo_iot_managed_integrations.types.get_account_association_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAccountAssociation", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest = {
            "account_association_id": account_association_id
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
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
    ) -> None:
        """<p>Updates the properties of an existing account association.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to update.</p>
            name: <p>The new name to assign to the account association.</p>
            description: <p>The new description to assign to the account association.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_account_association

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.update_account_association.update_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAccountAssociation")
        )
        input_: capo_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest = {
            "account_association_id": account_association_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Remove a third-party account association for an end user.</p> <note> <p>You must first call the <code>DeregisterAccountAssociation</code> to remove the connection between the managed thing and the third-party account before calling the <code>DeleteAccountAssociation</code> API.</p> </note>

        Args:
            account_association_id: <p>The unique identifier of the account association to be deleted.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association.delete_account_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAccountAssociation")
        )
        input_: capo_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest = {
            "account_association_id": account_association_id
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
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        connector_destination_id: Optional[
            "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse":
        """<p>Lists all account associations, with optional filtering by connector destination ID.</p>

        Args:
            connector_destination_id: <p>The identifier of the connector destination to filter account associations by.</p>
            max_results: <p>The maximum number of account associations to return in a single response.</p>
            next_token: <p>A token used for pagination of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations.list_account_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAccountAssociations")
        )
        input_: capo_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest = {}
        if connector_destination_id is not None:
            input_["connector_destination_id"] = connector_destination_id
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

    def start_account_association_refresh(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse":
        """<p>Initiates a refresh of an existing account association to update its authorization and connection status.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to refresh.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh.start_account_association_refresh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.start_account_association_refresh_response

            return capo_iot_managed_integrations.types.start_account_association_refresh_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartAccountAssociationRefresh", redact_output=_redact_output
            ),
        )
        input_: capo_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest = {
            "account_association_id": account_association_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAccountAssociationResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        connector_destination_id: "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        general_authorization: Optional[
            "capo_iot_managed_integrations.types.general_authorization_name.GeneralAuthorizationName"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse":
        """<p>Creates a new account association via the destination id.</p>

        Args:
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            connector_destination_id: <p>The identifier of the connector destination.</p>
            name: <p>The name of the destination for the new account association.</p>
            description: <p>A description of the account association request.</p>
            tags: <p>A set of key/value pairs that are used to manage the account association.</p>
            general_authorization: <p>The General Authorization reference by authorization material name.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_account_association.async_create_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_account_association_request

            return capo_iot_managed_integrations.types.create_account_association_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_account_association_response

            return capo_iot_managed_integrations.types.create_account_association_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAccountAssociation",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest = {
            "connector_destination_id": connector_destination_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if general_authorization is not None:
            input_["general_authorization"] = general_authorization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse":
        """<p>Get an account association for an Amazon Web Services account linked to a customer-managed destination.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to retrieve.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_account_association.async_get_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_account_association_response

            return capo_iot_managed_integrations.types.get_account_association_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAccountAssociation", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest = {
            "account_association_id": account_association_id
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
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
    ) -> None:
        """<p>Updates the properties of an existing account association.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to update.</p>
            name: <p>The new name to assign to the account association.</p>
            description: <p>The new description to assign to the account association.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_account_association.async_update_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAccountAssociation")
        )
        input_: capo_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest = {
            "account_association_id": account_association_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Remove a third-party account association for an end user.</p> <note> <p>You must first call the <code>DeregisterAccountAssociation</code> to remove the connection between the managed thing and the third-party account before calling the <code>DeleteAccountAssociation</code> API.</p> </note>

        Args:
            account_association_id: <p>The unique identifier of the account association to be deleted.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association.async_delete_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAccountAssociation")
        )
        input_: capo_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest = {
            "account_association_id": account_association_id
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
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        connector_destination_id: Optional[
            "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse":
        """<p>Lists all account associations, with optional filtering by connector destination ID.</p>

        Args:
            connector_destination_id: <p>The identifier of the connector destination to filter account associations by.</p>
            max_results: <p>The maximum number of account associations to return in a single response.</p>
            next_token: <p>A token used for pagination of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations.async_list_account_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAccountAssociations")
        )
        input_: capo_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest = {}
        if connector_destination_id is not None:
            input_["connector_destination_id"] = connector_destination_id
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

    async def start_account_association_refresh(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse":
        """<p>Initiates a refresh of an existing account association to update its authorization and connection status.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to refresh.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh.async_start_account_association_refresh(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.start_account_association_refresh_response

            return capo_iot_managed_integrations.types.start_account_association_refresh_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartAccountAssociationRefresh", redact_output=_redact_output
            ),
        )
        input_: capo_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest = {
            "account_association_id": account_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
