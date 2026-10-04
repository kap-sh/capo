from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_securityagent._auth._signers
import capo_securityagent._auth._sigv4
from capo_securityagent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_securityagent.types.create_integration_input
    import capo_securityagent.types.create_integration_output
    import capo_securityagent.types.delete_integration_input
    import capo_securityagent.types.delete_integration_output
    import capo_securityagent.types.get_integration_input
    import capo_securityagent.types.get_integration_output
    import capo_securityagent.types.integration_filter
    import capo_securityagent.types.integration_id
    import capo_securityagent.types.integration_summary
    import capo_securityagent.types.kms_key_id
    import capo_securityagent.types.list_integrations_input
    import capo_securityagent.types.list_integrations_output
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token
    import capo_securityagent.types.private_connection_name
    import capo_securityagent.types.provider
    import capo_securityagent.types.provider_input
    import capo_securityagent.types.tag_map
    import capo_securityagent.types.update_integration_input
    import capo_securityagent.types.update_integration_output
    import capo_securityagent.types.webhook_action
    from capo_securityagent._services.async_security_agent import (
        AsyncSecurityAgentClient,
        AsyncSecurityAgentClientConfig,
    )
    from capo_securityagent._services.security_agent import (
        SecurityAgentClient,
        SecurityAgentClientConfig,
    )


class IntegrationResource:
    def __init__(self, service: SecurityAgentClient) -> None:
        self._service = service

    def create(
        self,
        provider: "capo_securityagent.types.provider.Provider",
        input: "capo_securityagent.types.provider_input.ProviderInput",
        integration_display_name: str,
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        kms_key_id: Optional["capo_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
        private_connection_name: Optional[
            "capo_securityagent.types.private_connection_name.PrivateConnectionName"
        ] = None,
    ) -> "capo_securityagent.types.create_integration_output.CreateIntegrationOutput":
        """<p>Creates a new integration with a third-party provider, such as GitHub, for code review and remediation.</p>

        Args:
            provider: <p>The integration provider.</p>
            input: <p>The provider-specific input required to create the integration.</p>
            integration_display_name: <p>The display name for the integration.</p>
            kms_key_id: <p>The identifier of the AWS KMS key to use for encrypting data associated with the integration.</p>
            tags: <p>The tags to associate with the integration.</p>
            private_connection_name: <p>The name of an active private connection used to reach a self-hosted provider instance over private networking. Specify this when the instance is not publicly reachable.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.create_integration_input.CreateIntegrationInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_integration

            output, http_response = (
                capo_securityagent._operations.security_agent.create_integration.create_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.create_integration_input.CreateIntegrationInput = {
            "provider": provider,
            "input": input,
            "integration_display_name": integration_display_name,
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if private_connection_name is not None:
            input_["private_connection_name"] = private_connection_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_integration_output.GetIntegrationOutput":
        """<p>Retrieves information about an integration.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to retrieve.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.get_integration_input.GetIntegrationInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.get_integration_output.GetIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.get_integration

            output, http_response = (
                capo_securityagent._operations.security_agent.get_integration.get_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.get_integration_input.GetIntegrationInput = {
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
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        webhook_action: "capo_securityagent.types.webhook_action.WebhookAction",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.update_integration_output.UpdateIntegrationOutput":
        """<p>Creates an integration's webhook, or rotates the HMAC signing secret of an existing one. The secret is returned only once, in this response, and cannot be retrieved again.</p>

        Args:
            integration_id: <p>The ID of the integration whose webhook you want to create or rotate.</p>
            webhook_action: <p>The action to perform on the integration's webhook.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.update_integration_input.UpdateIntegrationInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.update_integration_output.UpdateIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_integration

            output, http_response = (
                capo_securityagent._operations.security_agent.update_integration.update_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.update_integration_input.UpdateIntegrationInput = {
            "integration_id": integration_id,
            "webhook_action": webhook_action,
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
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_integration_output.DeleteIntegrationOutput":
        """<p>Deletes an integration with a third-party provider.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.delete_integration_output.DeleteIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_integration

            output, http_response = (
                capo_securityagent._operations.security_agent.delete_integration.delete_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_integration_input.DeleteIntegrationInput = {
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
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        filter: Optional[
            "capo_securityagent.types.integration_filter.IntegrationFilter"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_integrations_output.ListIntegrationsOutput":
        """<p>Lists the integrations in your account, optionally filtered by provider or provider type.</p>

        Args:
            filter: <p>A filter to apply to the list of integrations.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.list_integrations_input.ListIntegrationsInput]",
        ) -> OperationResponse[
            "capo_securityagent.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_integrations

            output, http_response = (
                capo_securityagent._operations.security_agent.list_integrations.list_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.list_integrations_input.ListIntegrationsInput = {}
        if filter is not None:
            input_["filter"] = filter
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


class AsyncIntegrationResource:
    def __init__(self, service: AsyncSecurityAgentClient) -> None:
        self._service = service

    async def create(
        self,
        provider: "capo_securityagent.types.provider.Provider",
        input: "capo_securityagent.types.provider_input.ProviderInput",
        integration_display_name: str,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        kms_key_id: Optional["capo_securityagent.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
        private_connection_name: Optional[
            "capo_securityagent.types.private_connection_name.PrivateConnectionName"
        ] = None,
    ) -> "capo_securityagent.types.create_integration_output.CreateIntegrationOutput":
        """<p>Creates a new integration with a third-party provider, such as GitHub, for code review and remediation.</p>

        Args:
            provider: <p>The integration provider.</p>
            input: <p>The provider-specific input required to create the integration.</p>
            integration_display_name: <p>The display name for the integration.</p>
            kms_key_id: <p>The identifier of the AWS KMS key to use for encrypting data associated with the integration.</p>
            tags: <p>The tags to associate with the integration.</p>
            private_connection_name: <p>The name of an active private connection used to reach a self-hosted provider instance over private networking. Specify this when the instance is not publicly reachable.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_integration_input.CreateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_integration_output.CreateIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.create_integration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_integration.async_create_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.create_integration_input.CreateIntegrationInput = {
            "provider": provider,
            "input": input,
            "integration_display_name": integration_display_name,
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if private_connection_name is not None:
            input_["private_connection_name"] = private_connection_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_integration_output.GetIntegrationOutput":
        """<p>Retrieves information about an integration.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to retrieve.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.get_integration_input.GetIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.get_integration_output.GetIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.get_integration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.get_integration.async_get_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.get_integration_input.GetIntegrationInput = {
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
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        webhook_action: "capo_securityagent.types.webhook_action.WebhookAction",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.update_integration_output.UpdateIntegrationOutput":
        """<p>Creates an integration's webhook, or rotates the HMAC signing secret of an existing one. The secret is returned only once, in this response, and cannot be retrieved again.</p>

        Args:
            integration_id: <p>The ID of the integration whose webhook you want to create or rotate.</p>
            webhook_action: <p>The action to perform on the integration's webhook.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_integration_input.UpdateIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_integration_output.UpdateIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.update_integration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_integration.async_update_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.update_integration_input.UpdateIntegrationInput = {
            "integration_id": integration_id,
            "webhook_action": webhook_action,
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
        integration_id: "capo_securityagent.types.integration_id.IntegrationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.delete_integration_output.DeleteIntegrationOutput":
        """<p>Deletes an integration with a third-party provider.</p>

        Args:
            integration_id: <p>The unique identifier of the integration to delete.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_integration_input.DeleteIntegrationInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.delete_integration_output.DeleteIntegrationOutput"
        ]:
            import capo_securityagent._operations.security_agent.delete_integration

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_integration.async_delete_integration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.delete_integration_input.DeleteIntegrationInput = {
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
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        filter: Optional[
            "capo_securityagent.types.integration_filter.IntegrationFilter"
        ] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_integrations_output.ListIntegrationsOutput":
        """<p>Lists the integrations in your account, optionally filtered by provider or provider type.</p>

        Args:
            filter: <p>A filter to apply to the list of integrations.</p>
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_securityagent.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of your request.</p>
            capo_securityagent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists in the specified agent space or account.</p>
            capo_securityagent.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_securityagent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_integrations_input.ListIntegrationsInput]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_integrations_output.ListIntegrationsOutput"
        ]:
            import capo_securityagent._operations.security_agent.list_integrations

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_integrations.async_list_integrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securityagent.types.list_integrations_input.ListIntegrationsInput = {}
        if filter is not None:
            input_["filter"] = filter
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
