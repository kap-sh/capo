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
    import capo_bedrock_agentcore_control.types.api_key_credential_provider_item
    import capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request
    import capo_bedrock_agentcore_control.types.create_api_key_credential_provider_response
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.default_api_key_type
    import capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_request
    import capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_response
    import capo_bedrock_agentcore_control.types.get_api_key_credential_provider_request
    import capo_bedrock_agentcore_control.types.get_api_key_credential_provider_response
    import capo_bedrock_agentcore_control.types.list_api_key_credential_providers_request
    import capo_bedrock_agentcore_control.types.list_api_key_credential_providers_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.secret_reference
    import capo_bedrock_agentcore_control.types.secret_source_type
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request
    import capo_bedrock_agentcore_control.types.update_api_key_credential_provider_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class ApiKeyCredentialProvider:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "capo_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse":
        """<p>Creates a new API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider. The name must be unique within your account.</p>
            api_key: <p>The API key to use for authentication. This value is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the Amazon Web Services Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>
            tags: <p>A map of tag keys and values to assign to the API key credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider.create_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request

            return capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateApiKeyCredentialProvider", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest = {
            "name": name
        }
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source
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
    ) -> "capo_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse":
        """<p>Retrieves information about an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to retrieve.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider.get_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetApiKeyCredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest = {
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
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "capo_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse":
        """<p>Updates an existing API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to update.</p>
            api_key: <p>The new API key to use for authentication. This value replaces the existing API key and is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the Amazon Web Services Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider.update_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request

            return capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateApiKeyCredentialProvider", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest = {
            "name": name
        }
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source

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
    ) -> "capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse":
        """<p>Deletes an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to delete.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider.delete_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApiKeyCredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_api_key_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse":
        """<p>Lists all API key credential providers in your account.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers.list_api_key_credential_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListApiKeyCredentialProviders")
        )
        input_: capo_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest = {}
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


class AsyncApiKeyCredentialProvider:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "capo_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse":
        """<p>Creates a new API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider. The name must be unique within your account.</p>
            api_key: <p>The API key to use for authentication. This value is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the Amazon Web Services Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>
            tags: <p>A map of tag keys and values to assign to the API key credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider.async_create_api_key_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request

            return capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateApiKeyCredentialProvider", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest = {
            "name": name
        }
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source
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
    ) -> "capo_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse":
        """<p>Retrieves information about an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to retrieve.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider.async_get_api_key_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetApiKeyCredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest = {
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
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "capo_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse":
        """<p>Updates an existing API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to update.</p>
            api_key: <p>The new API key to use for authentication. This value replaces the existing API key and is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the Amazon Web Services Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider.async_update_api_key_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request

            return capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateApiKeyCredentialProvider", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest = {
            "name": name
        }
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source

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
    ) -> "capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse":
        """<p>Deletes an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to delete.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider.async_delete_api_key_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApiKeyCredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_api_key_credential_providers(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse":
        """<p>Lists all API key credential providers in your account.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers.async_list_api_key_credential_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListApiKeyCredentialProviders")
        )
        input_: capo_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest = {}
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
