from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_continuum._auth._signers
import capo_continuum._auth._sigv4
from capo_continuum._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_continuum.types.create_integration_input
    import capo_continuum.types.create_integration_output
    import capo_continuum.types.delete_integration_input
    import capo_continuum.types.get_integration_input
    import capo_continuum.types.get_integration_output
    import capo_continuum.types.integration_client_token
    import capo_continuum.types.integration_id
    import capo_continuum.types.integration_name
    import capo_continuum.types.integration_summary
    import capo_continuum.types.list_integrations_input
    import capo_continuum.types.list_integrations_output
    import capo_continuum.types.max_results
    import capo_continuum.types.next_token
    import capo_continuum.types.provider_configuration
    import capo_continuum.types.update_integration_input
    import capo_continuum.types.update_integration_output
    import capo_continuum.types.update_provider_configuration
    from capo_continuum._services.async_continuum import (
        AsyncContinuumClient,
        AsyncContinuumClientConfig,
    )
    from capo_continuum._services.continuum import (
        ContinuumClient,
        ContinuumClientConfig,
    )


class Integration:
    def __init__(self, service: ContinuumClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_continuum.types.integration_name.IntegrationName",
        provider_configuration: "capo_continuum.types.provider_configuration.ProviderConfiguration",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        client_token: Optional[
            "capo_continuum.types.integration_client_token.IntegrationClientToken"
        ] = None,
    ) -> "capo_continuum.types.create_integration_output.CreateIntegrationOutput":
        """Creates a new integration with an external source provider. Repeating an identical request with the same clientToken returns the original integrationId, integrationArn, and createdAt. Token records are retained for eight hours after success or terminal failure, including after the integration is deleted; replaying a deleted integration's token does not recreate it. An identical request with a retained terminal failure returns the recorded error. Reusing a token with different parameters returns ValidationException. A fresh token starts a new create attempt; if the name is already owned by another integration, ConflictException includes that integration's identifier. An attempt still in progress may return ThrottlingException with retryAfterSeconds set to 1; retry with the same token and identical parameters. GitHub authorization codes are single use. Retry an unresolved attempt with its original token and unchanged parameters first. If the service reports a terminal failure, an expired attempt, or a successful token exchange whose integration could not be saved, restart GitHub authorization with a fresh token and authorization code. The service does not checkpoint provider results for recovery by another request.

        Args:
            client_token: An optional token identifying one create attempt within the caller's account, Region, and operation. SDKs generate a token when omitted. If a request reaches the service without a token, the service generates one for that request. Each request without a token starts a new attempt. To replay an attempt, supply the same token and identical input. Authorized users and roles in the same account can retry an attempt this way. Token records are retained for eight hours after success or terminal failure, including after deletion of a successfully created integration. Different input with the same token returns ValidationException.
            name: The name for the integration.
            provider_configuration: The provider-specific configuration required to create the integration. Only one member may be specified.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.create_integration_input.CreateIntegrationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_integration

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.create_integration.create_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.create_integration_input.CreateIntegrationInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.create_integration_input

            return capo_continuum.types.create_integration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateIntegration", redact_input=_redact_input),
        )
        input_: capo_continuum.types.create_integration_input.CreateIntegrationInput = {
            "name": name,
            "provider_configuration": provider_configuration,
        }
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
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_integration_output.GetIntegrationOutput":
        """Retrieves information about an integration.

        Args:
            integration_id: The unique identifier of the integration to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_integration_input.GetIntegrationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_integration_output.GetIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_integration

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_integration.get_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIntegration")
        )
        input_: capo_continuum.types.get_integration_input.GetIntegrationInput = {
            "integration_id": integration_id
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
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        provider_configuration: "capo_continuum.types.update_provider_configuration.UpdateProviderConfiguration",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.update_integration_output.UpdateIntegrationOutput":
        """Rotates the credentials used by an Amazon S3 integration. Only S3 integrations can be updated; GitHub integrations cannot be modified. The integration's name, provider type, and bucket remain fixed. The caller must have iam:PassRole permission for the supplied role, including when only the external ID changes. Continuum verifies that the role can be assumed with the requested external ID and can access the existing bucket before saving both credentials atomically. Omitting externalId preserves its current value. Repeating both current credentials leaves updatedAt unchanged, but still requires authorization and access validation.

        Args:
            integration_id: The unique identifier of the S3 integration to update.
            provider_configuration: The provider-specific changes to apply. The member must match the integration's provider type, and only S3 integrations can be updated.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.update_integration_input.UpdateIntegrationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.update_integration_output.UpdateIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_integration

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.update_integration.update_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.update_integration_input.UpdateIntegrationInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.update_integration_input

            return capo_continuum.types.update_integration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateIntegration", redact_input=_redact_input),
        )
        input_: capo_continuum.types.update_integration_input.UpdateIntegrationInput = {
            "integration_id": integration_id,
            "provider_configuration": provider_configuration,
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
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> None:
        """Deletes an integration and releases its name and account quota. Its retained CreateIntegration token receipt can still replay the original result without recreating the integration. Shared provider registrations are retained: deleting one integration does not remove provider access used by another integration. A fresh GitHub CreateIntegration attempt requires a fresh OAuth authorization code and a new clientToken.

        Args:
            integration_id: The unique identifier of the integration to delete.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> OperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_integration

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.delete_integration.delete_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIntegration")
        )
        input_: capo_continuum.types.delete_integration_input.DeleteIntegrationInput = {
            "integration_id": integration_id
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
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_integrations_output.ListIntegrationsOutput":
        """Lists the integrations in your account in descending integrationId order.

        Args:
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_integrations_input.ListIntegrationsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_integrations

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_integrations.list_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIntegrations")
        )
        input_: capo_continuum.types.list_integrations_input.ListIntegrationsInput = {}
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


class AsyncIntegration:
    def __init__(self, service: AsyncContinuumClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_continuum.types.integration_name.IntegrationName",
        provider_configuration: "capo_continuum.types.provider_configuration.ProviderConfiguration",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        client_token: Optional[
            "capo_continuum.types.integration_client_token.IntegrationClientToken"
        ] = None,
    ) -> "capo_continuum.types.create_integration_output.CreateIntegrationOutput":
        """Creates a new integration with an external source provider. Repeating an identical request with the same clientToken returns the original integrationId, integrationArn, and createdAt. Token records are retained for eight hours after success or terminal failure, including after the integration is deleted; replaying a deleted integration's token does not recreate it. An identical request with a retained terminal failure returns the recorded error. Reusing a token with different parameters returns ValidationException. A fresh token starts a new create attempt; if the name is already owned by another integration, ConflictException includes that integration's identifier. An attempt still in progress may return ThrottlingException with retryAfterSeconds set to 1; retry with the same token and identical parameters. GitHub authorization codes are single use. Retry an unresolved attempt with its original token and unchanged parameters first. If the service reports a terminal failure, an expired attempt, or a successful token exchange whose integration could not be saved, restart GitHub authorization with a fresh token and authorization code. The service does not checkpoint provider results for recovery by another request.

        Args:
            client_token: An optional token identifying one create attempt within the caller's account, Region, and operation. SDKs generate a token when omitted. If a request reaches the service without a token, the service generates one for that request. Each request without a token starts a new attempt. To replay an attempt, supply the same token and identical input. Authorized users and roles in the same account can retry an attempt this way. Token records are retained for eight hours after success or terminal failure, including after deletion of a successfully created integration. Different input with the same token returns ValidationException.
            name: The name for the integration.
            provider_configuration: The provider-specific configuration required to create the integration. Only one member may be specified.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.create_integration_input.CreateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_integration

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.create_integration.async_create_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.create_integration_input.CreateIntegrationInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.create_integration_input

            return capo_continuum.types.create_integration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateIntegration", redact_input=_redact_input),
        )
        input_: capo_continuum.types.create_integration_input.CreateIntegrationInput = {
            "name": name,
            "provider_configuration": provider_configuration,
        }
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
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_integration_output.GetIntegrationOutput":
        """Retrieves information about an integration.

        Args:
            integration_id: The unique identifier of the integration to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.get_integration_input.GetIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.get_integration_output.GetIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_integration

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.get_integration.async_get_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIntegration")
        )
        input_: capo_continuum.types.get_integration_input.GetIntegrationInput = {
            "integration_id": integration_id
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
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        provider_configuration: "capo_continuum.types.update_provider_configuration.UpdateProviderConfiguration",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
    ) -> "capo_continuum.types.update_integration_output.UpdateIntegrationOutput":
        """Rotates the credentials used by an Amazon S3 integration. Only S3 integrations can be updated; GitHub integrations cannot be modified. The integration's name, provider type, and bucket remain fixed. The caller must have iam:PassRole permission for the supplied role, including when only the external ID changes. Continuum verifies that the role can be assumed with the requested external ID and can access the existing bucket before saving both credentials atomically. Omitting externalId preserves its current value. Repeating both current credentials leaves updatedAt unchanged, but still requires authorization and access validation.

        Args:
            integration_id: The unique identifier of the S3 integration to update.
            provider_configuration: The provider-specific changes to apply. The member must match the integration's provider type, and only S3 integrations can be updated.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.update_integration_input.UpdateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.update_integration_output.UpdateIntegrationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_integration

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.update_integration.async_update_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.update_integration_input.UpdateIntegrationInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.update_integration_input

            return capo_continuum.types.update_integration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateIntegration", redact_input=_redact_input),
        )
        input_: capo_continuum.types.update_integration_input.UpdateIntegrationInput = {
            "integration_id": integration_id,
            "provider_configuration": provider_configuration,
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
        integration_id: "capo_continuum.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
    ) -> None:
        """Deletes an integration and releases its name and account quota. Its retained CreateIntegration token receipt can still replay the original result without recreating the integration. Shared provider registrations are retained: deleting one integration does not remove provider access used by another integration. A fresh GitHub CreateIntegration attempt requires a fresh OAuth authorization code and a new clientToken.

        Args:
            integration_id: The unique identifier of the integration to delete.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_integration

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.delete_integration.async_delete_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIntegration")
        )
        input_: capo_continuum.types.delete_integration_input.DeleteIntegrationInput = {
            "integration_id": integration_id
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
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_integrations_output.ListIntegrationsOutput":
        """Lists the integrations in your account in descending integrationId order.

        Args:
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.list_integrations_input.ListIntegrationsInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_integrations

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.list_integrations.async_list_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIntegrations")
        )
        input_: capo_continuum.types.list_integrations_input.ListIntegrationsInput = {}
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
