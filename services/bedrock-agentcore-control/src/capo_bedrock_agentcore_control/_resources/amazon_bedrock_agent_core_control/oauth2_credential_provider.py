from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request
    import capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.credential_provider_vendor_type
    import capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request
    import capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response
    import capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_request
    import capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response
    import capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_request
    import capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_response
    import capo_bedrock_agentcore_control.types.oauth2_credential_provider_item
    import capo_bedrock_agentcore_control.types.oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request
    import capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class Oauth2CredentialProvider:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "capo_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse":
        """<p>Creates a new OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider. The name must be unique within your account.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.</p>
            oauth2_provider_config_input: <p>The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.</p>
            tags: <p>A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Exception thrown when a resource limit is exceeded.</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider.create_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request

            return capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response

            return capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateOauth2CredentialProvider",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "oauth2_provider_config_input": oauth2_provider_config_input,
        }
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
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse":
        """<p>Retrieves information about an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider.get_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response

            return capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetOauth2CredentialProvider", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest = {
            "name": name
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
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "capo_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse":
        """<p>Updates an existing OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to update.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider.</p>
            oauth2_provider_config_input: <p>The configuration input for the OAuth2 provider.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider.update_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request

            return capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response

            return capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateOauth2CredentialProvider",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "oauth2_provider_config_input": oauth2_provider_config_input,
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
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse":
        """<p>Deletes an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider.delete_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteOauth2CredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_oauth2_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse":
        """<p>Lists all OAuth2 credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers.list_oauth2_credential_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListOauth2CredentialProviders")
        )
        input_: capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest = {}
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


class AsyncOauth2CredentialProvider:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "capo_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse":
        """<p>Creates a new OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider. The name must be unique within your account.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.</p>
            oauth2_provider_config_input: <p>The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.</p>
            tags: <p>A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Exception thrown when a resource limit is exceeded.</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider.async_create_oauth2_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request

            return capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response

            return capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateOauth2CredentialProvider",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "oauth2_provider_config_input": oauth2_provider_config_input,
        }
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
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse":
        """<p>Retrieves information about an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider.async_get_oauth2_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response

            return capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetOauth2CredentialProvider", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest = {
            "name": name
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
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "capo_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse":
        """<p>Updates an existing OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to update.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider.</p>
            oauth2_provider_config_input: <p>The configuration input for the OAuth2 provider.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider.async_update_oauth2_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request

            return capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response

            return capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateOauth2CredentialProvider",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "oauth2_provider_config_input": oauth2_provider_config_input,
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
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse":
        """<p>Deletes an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider.async_delete_oauth2_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteOauth2CredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_oauth2_credential_providers(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse":
        """<p>Lists all OAuth2 credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers.async_list_oauth2_credential_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListOauth2CredentialProviders")
        )
        input_: capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest = {}
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
