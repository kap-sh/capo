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
    import capo_bedrock_agentcore_control.types.create_payment_credential_provider_request
    import capo_bedrock_agentcore_control.types.create_payment_credential_provider_response
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.delete_payment_credential_provider_request
    import capo_bedrock_agentcore_control.types.delete_payment_credential_provider_response
    import capo_bedrock_agentcore_control.types.get_payment_credential_provider_request
    import capo_bedrock_agentcore_control.types.get_payment_credential_provider_response
    import capo_bedrock_agentcore_control.types.list_payment_credential_providers_request
    import capo_bedrock_agentcore_control.types.list_payment_credential_providers_response
    import capo_bedrock_agentcore_control.types.payment_credential_provider_item
    import capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type
    import capo_bedrock_agentcore_control.types.payment_provider_configuration_input
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_payment_credential_provider_request
    import capo_bedrock_agentcore_control.types.update_payment_credential_provider_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class PaymentCredentialProvider:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType",
        provider_configuration_input: "capo_bedrock_agentcore_control.types.payment_provider_configuration_input.PaymentProviderConfigurationInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_payment_credential_provider_response.CreatePaymentCredentialProviderResponse":
        """<p>Creates a new payment credential provider for storing authentication credentials used by payment connectors to communicate with external payment providers.</p>

        Args:
            name: <p>Unique name for the payment credential provider.</p>
            credential_provider_vendor: <p>The vendor type for the payment credential provider (e.g., CoinbaseCDP, StripePrivy).</p>
            provider_configuration_input: <p>Configuration specific to the vendor, including API credentials.</p>
            tags: <p>Optional tags for resource organization.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.CreatePaymentCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_payment_credential_provider_response.CreatePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_credential_provider.create_payment_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.CreatePaymentCredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_payment_credential_provider_request

            return capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePaymentCredentialProvider", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.CreatePaymentCredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "provider_configuration_input": provider_configuration_input,
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
    ) -> "capo_bedrock_agentcore_control.types.get_payment_credential_provider_response.GetPaymentCredentialProviderResponse":
        """<p>Retrieves information about a specific payment credential provider.</p>

        Args:
            name: <p>The name of the payment credential provider to retrieve.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_payment_credential_provider_request.GetPaymentCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_payment_credential_provider_response.GetPaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_credential_provider.get_payment_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPaymentCredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.get_payment_credential_provider_request.GetPaymentCredentialProviderRequest = {
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
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType",
        provider_configuration_input: "capo_bedrock_agentcore_control.types.payment_provider_configuration_input.PaymentProviderConfigurationInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_payment_credential_provider_response.UpdatePaymentCredentialProviderResponse":
        """<p>Updates an existing payment credential provider with new authentication credentials.</p>

        Args:
            name: <p>The name of the payment credential provider to update.</p>
            credential_provider_vendor: <p>The vendor type for the payment credential provider (e.g., CoinbaseCDP, StripePrivy).</p>
            provider_configuration_input: <p>Configuration specific to the vendor, including API credentials.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.UpdatePaymentCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_payment_credential_provider_response.UpdatePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_credential_provider.update_payment_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.UpdatePaymentCredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_payment_credential_provider_request

            return capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePaymentCredentialProvider", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.UpdatePaymentCredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "provider_configuration_input": provider_configuration_input,
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
    ) -> "capo_bedrock_agentcore_control.types.delete_payment_credential_provider_response.DeletePaymentCredentialProviderResponse":
        """<p>Deletes a payment credential provider and its associated stored credentials.</p>

        Args:
            name: <p>The name of the payment credential provider to delete.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_payment_credential_provider_request.DeletePaymentCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_payment_credential_provider_response.DeletePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_credential_provider.delete_payment_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePaymentCredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.delete_payment_credential_provider_request.DeletePaymentCredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_payment_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_payment_credential_providers_response.ListPaymentCredentialProvidersResponse":
        """<p>Lists all payment credential providers in the account.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_payment_credential_providers_request.ListPaymentCredentialProvidersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_payment_credential_providers_response.ListPaymentCredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_credential_providers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_credential_providers.list_payment_credential_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPaymentCredentialProviders")
        )
        input_: capo_bedrock_agentcore_control.types.list_payment_credential_providers_request.ListPaymentCredentialProvidersRequest = {}
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


class AsyncPaymentCredentialProvider:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType",
        provider_configuration_input: "capo_bedrock_agentcore_control.types.payment_provider_configuration_input.PaymentProviderConfigurationInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_payment_credential_provider_response.CreatePaymentCredentialProviderResponse":
        """<p>Creates a new payment credential provider for storing authentication credentials used by payment connectors to communicate with external payment providers.</p>

        Args:
            name: <p>Unique name for the payment credential provider.</p>
            credential_provider_vendor: <p>The vendor type for the payment credential provider (e.g., CoinbaseCDP, StripePrivy).</p>
            provider_configuration_input: <p>Configuration specific to the vendor, including API credentials.</p>
            tags: <p>Optional tags for resource organization.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.CreatePaymentCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_payment_credential_provider_response.CreatePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_credential_provider.async_create_payment_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.CreatePaymentCredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.create_payment_credential_provider_request

            return capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePaymentCredentialProvider", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.CreatePaymentCredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "provider_configuration_input": provider_configuration_input,
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
    ) -> "capo_bedrock_agentcore_control.types.get_payment_credential_provider_response.GetPaymentCredentialProviderResponse":
        """<p>Retrieves information about a specific payment credential provider.</p>

        Args:
            name: <p>The name of the payment credential provider to retrieve.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_payment_credential_provider_request.GetPaymentCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_payment_credential_provider_response.GetPaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_credential_provider.async_get_payment_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPaymentCredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.get_payment_credential_provider_request.GetPaymentCredentialProviderRequest = {
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
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType",
        provider_configuration_input: "capo_bedrock_agentcore_control.types.payment_provider_configuration_input.PaymentProviderConfigurationInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_payment_credential_provider_response.UpdatePaymentCredentialProviderResponse":
        """<p>Updates an existing payment credential provider with new authentication credentials.</p>

        Args:
            name: <p>The name of the payment credential provider to update.</p>
            credential_provider_vendor: <p>The vendor type for the payment credential provider (e.g., CoinbaseCDP, StripePrivy).</p>
            provider_configuration_input: <p>Configuration specific to the vendor, including API credentials.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.UpdatePaymentCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_payment_credential_provider_response.UpdatePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_credential_provider.async_update_payment_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.UpdatePaymentCredentialProviderRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore_control.types.update_payment_credential_provider_request

            return capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePaymentCredentialProvider", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.UpdatePaymentCredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "provider_configuration_input": provider_configuration_input,
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
    ) -> "capo_bedrock_agentcore_control.types.delete_payment_credential_provider_response.DeletePaymentCredentialProviderResponse":
        """<p>Deletes a payment credential provider and its associated stored credentials.</p>

        Args:
            name: <p>The name of the payment credential provider to delete.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_payment_credential_provider_request.DeletePaymentCredentialProviderRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_payment_credential_provider_response.DeletePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_credential_provider

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_credential_provider.async_delete_payment_credential_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePaymentCredentialProvider")
        )
        input_: capo_bedrock_agentcore_control.types.delete_payment_credential_provider_request.DeletePaymentCredentialProviderRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_payment_credential_providers(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_payment_credential_providers_response.ListPaymentCredentialProvidersResponse":
        """<p>Lists all payment credential providers in the account.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_payment_credential_providers_request.ListPaymentCredentialProvidersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_payment_credential_providers_response.ListPaymentCredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_credential_providers

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_credential_providers.async_list_payment_credential_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPaymentCredentialProviders")
        )
        input_: capo_bedrock_agentcore_control.types.list_payment_credential_providers_request.ListPaymentCredentialProvidersRequest = {}
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
