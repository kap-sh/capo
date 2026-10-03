from __future__ import annotations

import uuid
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
    import capo_bedrock_runtime.types.async_invoke_idempotency_token
    import capo_bedrock_runtime.types.async_invoke_identifier
    import capo_bedrock_runtime.types.async_invoke_output_data_config
    import capo_bedrock_runtime.types.async_invoke_status
    import capo_bedrock_runtime.types.async_invoke_summary
    import capo_bedrock_runtime.types.get_async_invoke_request
    import capo_bedrock_runtime.types.get_async_invoke_response
    import capo_bedrock_runtime.types.invocation_arn
    import capo_bedrock_runtime.types.list_async_invokes_request
    import capo_bedrock_runtime.types.list_async_invokes_response
    import capo_bedrock_runtime.types.max_results
    import capo_bedrock_runtime.types.model_input_payload
    import capo_bedrock_runtime.types.pagination_token
    import capo_bedrock_runtime.types.sort_async_invocation_by
    import capo_bedrock_runtime.types.sort_order
    import capo_bedrock_runtime.types.start_async_invoke_request
    import capo_bedrock_runtime.types.start_async_invoke_response
    import capo_bedrock_runtime.types.tag_list
    import capo_bedrock_runtime.types.timestamp
    from capo_bedrock_runtime._services.async_bedrock_runtime import (
        AsyncBedrockRuntimeClient,
        AsyncBedrockRuntimeClientConfig,
    )
    from capo_bedrock_runtime._services.bedrock_runtime import (
        BedrockRuntimeClient,
        BedrockRuntimeClientConfig,
    )


class AsyncInvokeResource:
    def __init__(self, service: BedrockRuntimeClient) -> None:
        self._service = service

    def get_async_invoke(
        self,
        invocation_arn: "capo_bedrock_runtime.types.invocation_arn.InvocationArn",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
    ) -> "capo_bedrock_runtime.types.get_async_invoke_response.GetAsyncInvokeResponse":
        """<p>Retrieve information about an asynchronous invocation.</p>

        Args:
            invocation_arn: <p>The invocation's ARN.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.get_async_invoke_request.GetAsyncInvokeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.get_async_invoke_response.GetAsyncInvokeResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.get_async_invoke

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.get_async_invoke.get_async_invoke(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.get_async_invoke_request.GetAsyncInvokeRequest = {
            "invocation_arn": invocation_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_async_invokes(
        self,
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        submit_time_after: Optional[
            "capo_bedrock_runtime.types.timestamp.Timestamp"
        ] = None,
        submit_time_before: Optional[
            "capo_bedrock_runtime.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "capo_bedrock_runtime.types.async_invoke_status.AsyncInvokeStatus"
        ] = None,
        max_results: Optional[
            "capo_bedrock_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_runtime.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_bedrock_runtime.types.sort_async_invocation_by.SortAsyncInvocationBy"
        ] = None,
        sort_order: Optional["capo_bedrock_runtime.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock_runtime.types.list_async_invokes_response.ListAsyncInvokesResponse":
        """<p>Lists asynchronous invocations.</p>

        Args:
            submit_time_after: <p>Include invocations submitted after this time.</p>
            submit_time_before: <p>Include invocations submitted before this time.</p>
            status_equals: <p>Filter invocations by status.</p>
            max_results: <p>The maximum number of invocations to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            sort_by: <p>How to sort the response.</p>
            sort_order: <p>The sorting order for the response.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.list_async_invokes_request.ListAsyncInvokesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.list_async_invokes_response.ListAsyncInvokesResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.list_async_invokes

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.list_async_invokes.list_async_invokes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.list_async_invokes_request.ListAsyncInvokesRequest = {}
        if submit_time_after is not None:
            input_["submit_time_after"] = submit_time_after
        if submit_time_before is not None:
            input_["submit_time_before"] = submit_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_async_invoke(
        self,
        model_id: "capo_bedrock_runtime.types.async_invoke_identifier.AsyncInvokeIdentifier",
        model_input: "capo_bedrock_runtime.types.model_input_payload.ModelInputPayload",
        output_data_config: "capo_bedrock_runtime.types.async_invoke_output_data_config.AsyncInvokeOutputDataConfig",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock_runtime.types.async_invoke_idempotency_token.AsyncInvokeIdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock_runtime.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_runtime.types.start_async_invoke_response.StartAsyncInvokeResponse":
        """<p>Starts an asynchronous invocation.</p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html">Converse</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html">ConverseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important>

        Args:
            client_request_token: <p>Specify idempotency token to ensure that requests are not duplicated.</p>
            model_id: <p>The model to invoke.</p>
            model_input: <p>Input to send to the model.</p>
            output_data_config: <p>Where to store the output.</p>
            tags: <p>Tags to apply to the invocation.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.start_async_invoke_request.StartAsyncInvokeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.start_async_invoke_response.StartAsyncInvokeResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.start_async_invoke

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.start_async_invoke.start_async_invoke(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.start_async_invoke_request.StartAsyncInvokeRequest = {
            "model_id": model_id,
            "model_input": model_input,
            "output_data_config": output_data_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAsyncInvokeResource:
    def __init__(self, service: AsyncBedrockRuntimeClient) -> None:
        self._service = service

    async def get_async_invoke(
        self,
        invocation_arn: "capo_bedrock_runtime.types.invocation_arn.InvocationArn",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
    ) -> "capo_bedrock_runtime.types.get_async_invoke_response.GetAsyncInvokeResponse":
        """<p>Retrieve information about an asynchronous invocation.</p>

        Args:
            invocation_arn: <p>The invocation's ARN.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.get_async_invoke_request.GetAsyncInvokeRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.get_async_invoke_response.GetAsyncInvokeResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.get_async_invoke

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.get_async_invoke.async_get_async_invoke(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.get_async_invoke_request.GetAsyncInvokeRequest = {
            "invocation_arn": invocation_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_async_invokes(
        self,
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        submit_time_after: Optional[
            "capo_bedrock_runtime.types.timestamp.Timestamp"
        ] = None,
        submit_time_before: Optional[
            "capo_bedrock_runtime.types.timestamp.Timestamp"
        ] = None,
        status_equals: Optional[
            "capo_bedrock_runtime.types.async_invoke_status.AsyncInvokeStatus"
        ] = None,
        max_results: Optional[
            "capo_bedrock_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_runtime.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_bedrock_runtime.types.sort_async_invocation_by.SortAsyncInvocationBy"
        ] = None,
        sort_order: Optional["capo_bedrock_runtime.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock_runtime.types.list_async_invokes_response.ListAsyncInvokesResponse":
        """<p>Lists asynchronous invocations.</p>

        Args:
            submit_time_after: <p>Include invocations submitted after this time.</p>
            submit_time_before: <p>Include invocations submitted before this time.</p>
            status_equals: <p>Filter invocations by status.</p>
            max_results: <p>The maximum number of invocations to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            sort_by: <p>How to sort the response.</p>
            sort_order: <p>The sorting order for the response.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.list_async_invokes_request.ListAsyncInvokesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.list_async_invokes_response.ListAsyncInvokesResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.list_async_invokes

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.list_async_invokes.async_list_async_invokes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.list_async_invokes_request.ListAsyncInvokesRequest = {}
        if submit_time_after is not None:
            input_["submit_time_after"] = submit_time_after
        if submit_time_before is not None:
            input_["submit_time_before"] = submit_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_async_invoke(
        self,
        model_id: "capo_bedrock_runtime.types.async_invoke_identifier.AsyncInvokeIdentifier",
        model_input: "capo_bedrock_runtime.types.model_input_payload.ModelInputPayload",
        output_data_config: "capo_bedrock_runtime.types.async_invoke_output_data_config.AsyncInvokeOutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockRuntimeClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock_runtime.types.async_invoke_idempotency_token.AsyncInvokeIdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock_runtime.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock_runtime.types.start_async_invoke_response.StartAsyncInvokeResponse":
        """<p>Starts an asynchronous invocation.</p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html">Converse</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html">ConverseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important>

        Args:
            client_request_token: <p>Specify idempotency token to ensure that requests are not duplicated.</p>
            model_id: <p>The model to invoke.</p>
            model_input: <p>Input to send to the model.</p>
            output_data_config: <p>Where to store the output.</p>
            tags: <p>Tags to apply to the invocation.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_runtime.types.start_async_invoke_request.StartAsyncInvokeRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_runtime.types.start_async_invoke_response.StartAsyncInvokeResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.start_async_invoke

            (
                output,
                http_response,
            ) = await capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.start_async_invoke.async_start_async_invoke(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.start_async_invoke_request.StartAsyncInvokeRequest = {
            "model_id": model_id,
            "model_input": model_input,
            "output_data_config": output_data_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
