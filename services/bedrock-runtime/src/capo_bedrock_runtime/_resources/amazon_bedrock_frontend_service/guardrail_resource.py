from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock_runtime._auth._signers
import capo_bedrock_runtime._auth._sigv4
from capo_bedrock_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.apply_guardrail_request
    import capo_bedrock_runtime.types.apply_guardrail_response
    import capo_bedrock_runtime.types.guardrail_checks_config
    import capo_bedrock_runtime.types.guardrail_checks_message_list
    import capo_bedrock_runtime.types.guardrail_content_block_list
    import capo_bedrock_runtime.types.guardrail_content_source
    import capo_bedrock_runtime.types.guardrail_identifier
    import capo_bedrock_runtime.types.guardrail_output_scope
    import capo_bedrock_runtime.types.guardrail_version
    import capo_bedrock_runtime.types.invoke_guardrail_checks_request
    import capo_bedrock_runtime.types.invoke_guardrail_checks_response
    from capo_bedrock_runtime._services.async_bedrock_runtime import (
        AsyncBedrockRuntimeClient,
        AsyncBedrockRuntimeClientConfig,
    )
    from capo_bedrock_runtime._services.bedrock_runtime import (
        BedrockRuntimeClient,
        BedrockRuntimeClientConfig,
    )


class GuardrailResource:
    def __init__(self, service: BedrockRuntimeClient) -> None:
        self._service = service

    def apply_guardrail(
        self,
        guardrail_identifier: "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier",
        guardrail_version: "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion",
        source: "capo_bedrock_runtime.types.guardrail_content_source.GuardrailContentSource",
        content: "capo_bedrock_runtime.types.guardrail_content_block_list.GuardrailContentBlockList",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        output_scope: Optional[
            "capo_bedrock_runtime.types.guardrail_output_scope.GuardrailOutputScope"
        ] = None,
    ) -> "capo_bedrock_runtime.types.apply_guardrail_response.ApplyGuardrailResponse":
        """<p>The action to apply a guardrail.</p> <p>For troubleshooting some of the common errors you might encounter when using the <code>ApplyGuardrail</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            guardrail_identifier: <p>The guardrail identifier used in the request to apply the guardrail.</p>
            guardrail_version: <p>The guardrail version used in the request to apply the guardrail.</p>
            source: <p>The source of data used in the request to apply the guardrail.</p>
            content: <p>The content details used in the request to apply the guardrail.</p>
            output_scope: <p>Specifies the scope of the output that you get in the response. Set to <code>FULL</code> to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.</p> <p>Note that the full output scope doesn't apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.apply_guardrail_request.ApplyGuardrailRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.apply_guardrail_response.ApplyGuardrailResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.apply_guardrail

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.apply_guardrail.apply_guardrail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.apply_guardrail_request.ApplyGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier,
            "guardrail_version": guardrail_version,
            "source": source,
            "content": content,
        }
        if output_scope is not None:
            input_["output_scope"] = output_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def invoke_guardrail_checks(
        self,
        messages: "capo_bedrock_runtime.types.guardrail_checks_message_list.GuardrailChecksMessageList",
        checks: "capo_bedrock_runtime.types.guardrail_checks_config.GuardrailChecksConfig",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
    ) -> "capo_bedrock_runtime.types.invoke_guardrail_checks_response.InvokeGuardrailChecksResponse":
        """<p>Evaluates messages against inline guardrail checks. You specify the check configurations directly in the request, and Amazon Bedrock returns per-check results with severity or confidence scores.</p>

        Args:
            messages: <p>The messages to evaluate against the specified guardrail checks. Each message includes a role and one or more content blocks.</p>
            checks: <p>The inline check configurations that specify which guardrail checks to run against the messages.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.invoke_guardrail_checks_request.InvokeGuardrailChecksRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.invoke_guardrail_checks_response.InvokeGuardrailChecksResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_guardrail_checks

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_guardrail_checks.invoke_guardrail_checks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_guardrail_checks_request.InvokeGuardrailChecksRequest = {
            "messages": messages,
            "checks": checks,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGuardrailResource:
    def __init__(self, service: AsyncBedrockRuntimeClient) -> None:
        self._service = service

    async def apply_guardrail(
        self,
        guardrail_identifier: "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier",
        guardrail_version: "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion",
        source: "capo_bedrock_runtime.types.guardrail_content_source.GuardrailContentSource",
        content: "capo_bedrock_runtime.types.guardrail_content_block_list.GuardrailContentBlockList",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        output_scope: Optional[
            "capo_bedrock_runtime.types.guardrail_output_scope.GuardrailOutputScope"
        ] = None,
    ) -> "capo_bedrock_runtime.types.apply_guardrail_response.ApplyGuardrailResponse":
        """<p>The action to apply a guardrail.</p> <p>For troubleshooting some of the common errors you might encounter when using the <code>ApplyGuardrail</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            guardrail_identifier: <p>The guardrail identifier used in the request to apply the guardrail.</p>
            guardrail_version: <p>The guardrail version used in the request to apply the guardrail.</p>
            source: <p>The source of data used in the request to apply the guardrail.</p>
            content: <p>The content details used in the request to apply the guardrail.</p>
            output_scope: <p>Specifies the scope of the output that you get in the response. Set to <code>FULL</code> to return the entire output, including any detected and non-detected entries in the response for enhanced debugging.</p> <p>Note that the full output scope doesn't apply to word filters or regex in sensitive information filters. It does apply to all other filtering policies, including sensitive information with filters that can detect personally identifiable information (PII).</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.apply_guardrail_request.ApplyGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.apply_guardrail_response.ApplyGuardrailResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.apply_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.apply_guardrail.async_apply_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.apply_guardrail_request.ApplyGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier,
            "guardrail_version": guardrail_version,
            "source": source,
            "content": content,
        }
        if output_scope is not None:
            input_["output_scope"] = output_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def invoke_guardrail_checks(
        self,
        messages: "capo_bedrock_runtime.types.guardrail_checks_message_list.GuardrailChecksMessageList",
        checks: "capo_bedrock_runtime.types.guardrail_checks_config.GuardrailChecksConfig",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
    ) -> "capo_bedrock_runtime.types.invoke_guardrail_checks_response.InvokeGuardrailChecksResponse":
        """<p>Evaluates messages against inline guardrail checks. You specify the check configurations directly in the request, and Amazon Bedrock returns per-check results with severity or confidence scores.</p>

        Args:
            messages: <p>The messages to evaluate against the specified guardrail checks. Each message includes a role and one or more content blocks.</p>
            checks: <p>The inline check configurations that specify which guardrail checks to run against the messages.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.invoke_guardrail_checks_request.InvokeGuardrailChecksRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.invoke_guardrail_checks_response.InvokeGuardrailChecksResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_guardrail_checks

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_guardrail_checks.async_invoke_guardrail_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_guardrail_checks_request.InvokeGuardrailChecksRequest = {
            "messages": messages,
            "checks": checks,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
