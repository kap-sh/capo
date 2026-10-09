"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AmazonBedrockFrontendService``."""

import uuid
import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_bedrock_runtime._auth._signers
import capo_bedrock_runtime._auth._sigv4
from capo_bedrock_runtime._auth._identity import Credentials
from capo_bedrock_runtime._auth._providers import (
    BearerTokenProvider,
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    StaticBearerTokenProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_runtime._auth._zapros_handler import AuthMiddleware
from capo_bedrock_runtime._iter import ensure_sync_iterator
from capo_bedrock_runtime._pagination import resolve_path as _resolve_path
from capo_bedrock_runtime._resources.amazon_bedrock_frontend_service.async_invoke_resource import (
    AsyncInvokeResource,
)
from capo_bedrock_runtime._resources.amazon_bedrock_frontend_service.guardrail_resource import (
    GuardrailResource,
)
from capo_bedrock_runtime._resources.amazon_bedrock_frontend_service.inference_resource import (
    InferenceResource,
)
from capo_bedrock_runtime._resources.amazon_bedrock_frontend_service.tokenizer_resource import (
    TokenizerResource,
)
from capo_bedrock_runtime._services._aws_config import aws_config
from capo_bedrock_runtime._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.additional_model_response_field_paths
    import capo_bedrock_runtime.types.apply_guardrail_request
    import capo_bedrock_runtime.types.apply_guardrail_response
    import capo_bedrock_runtime.types.async_invoke_idempotency_token
    import capo_bedrock_runtime.types.async_invoke_identifier
    import capo_bedrock_runtime.types.async_invoke_output_data_config
    import capo_bedrock_runtime.types.async_invoke_status
    import capo_bedrock_runtime.types.async_invoke_summary
    import capo_bedrock_runtime.types.body
    import capo_bedrock_runtime.types.conversational_model_id
    import capo_bedrock_runtime.types.converse_request
    import capo_bedrock_runtime.types.converse_response
    import capo_bedrock_runtime.types.converse_stream_request
    import capo_bedrock_runtime.types.converse_stream_response
    import capo_bedrock_runtime.types.count_tokens_input
    import capo_bedrock_runtime.types.count_tokens_request
    import capo_bedrock_runtime.types.count_tokens_response
    import capo_bedrock_runtime.types.foundation_model_version_identifier
    import capo_bedrock_runtime.types.get_async_invoke_request
    import capo_bedrock_runtime.types.get_async_invoke_response
    import capo_bedrock_runtime.types.guardrail_checks_config
    import capo_bedrock_runtime.types.guardrail_checks_message_list
    import capo_bedrock_runtime.types.guardrail_configuration
    import capo_bedrock_runtime.types.guardrail_content_block_list
    import capo_bedrock_runtime.types.guardrail_content_source
    import capo_bedrock_runtime.types.guardrail_identifier
    import capo_bedrock_runtime.types.guardrail_output_scope
    import capo_bedrock_runtime.types.guardrail_stream_configuration
    import capo_bedrock_runtime.types.guardrail_version
    import capo_bedrock_runtime.types.inference_configuration
    import capo_bedrock_runtime.types.invocation_arn
    import capo_bedrock_runtime.types.invoke_guardrail_checks_request
    import capo_bedrock_runtime.types.invoke_guardrail_checks_response
    import capo_bedrock_runtime.types.invoke_model_identifier
    import capo_bedrock_runtime.types.invoke_model_request
    import capo_bedrock_runtime.types.invoke_model_response
    import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input
    import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request
    import capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response
    import capo_bedrock_runtime.types.invoke_model_with_response_stream_request
    import capo_bedrock_runtime.types.invoke_model_with_response_stream_response
    import capo_bedrock_runtime.types.list_async_invokes_request
    import capo_bedrock_runtime.types.list_async_invokes_response
    import capo_bedrock_runtime.types.max_results
    import capo_bedrock_runtime.types.messages
    import capo_bedrock_runtime.types.mime_type
    import capo_bedrock_runtime.types.model_input_payload
    import capo_bedrock_runtime.types.output_config
    import capo_bedrock_runtime.types.pagination_token
    import capo_bedrock_runtime.types.performance_config_latency
    import capo_bedrock_runtime.types.performance_configuration
    import capo_bedrock_runtime.types.prompt_variable_map
    import capo_bedrock_runtime.types.request_metadata
    import capo_bedrock_runtime.types.request_metadata_json
    import capo_bedrock_runtime.types.service_tier
    import capo_bedrock_runtime.types.service_tier_type
    import capo_bedrock_runtime.types.sort_async_invocation_by
    import capo_bedrock_runtime.types.sort_order
    import capo_bedrock_runtime.types.start_async_invoke_request
    import capo_bedrock_runtime.types.start_async_invoke_response
    import capo_bedrock_runtime.types.system_content_blocks
    import capo_bedrock_runtime.types.tag_list
    import capo_bedrock_runtime.types.timestamp
    import capo_bedrock_runtime.types.tool_configuration
    import capo_bedrock_runtime.types.trace


class BedrockRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    bearer_provider: BearerTokenProvider | None
    anonymous: bool | None


class BedrockRuntimeClient:
    """A client for the ``BedrockRuntime`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        bearer: Bearer token for authentication.
        bearer_provider: Provider that resolves bearer tokens. Takes precedence over ``bearer``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        bearer: str | None = None,
        bearer_provider: BearerTokenProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if (
            resolved_credentials_provider is None
            and credentials is None
            and bearer is None
            and bearer_provider is None
        ):
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        if bearer is not None and bearer_provider is not None:
            warnings.warn(
                "Both bearer and bearer_provider given; provider takes precedence"
            )
        if bearer_provider is None and bearer is not None:
            bearer_provider = StaticBearerTokenProvider(bearer)
        self._config = BedrockRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "bearer_provider": bearer_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.async_invoke_resource = AsyncInvokeResource(self)
        self.guardrail_resource = GuardrailResource(self)
        self.inference_resource = InferenceResource(self)
        self.tokenizer_resource = TokenizerResource(self)

    def operation_options(
        self, config_overrides: Optional[BedrockRuntimeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockRuntimeClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            bearer_provider=overrides.get(
                "bearer_provider", self._config.get("bearer_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_async_invokes(
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
    ) -> "Iterator[capo_bedrock_runtime.types.async_invoke_summary.AsyncInvokeSummary]":
        _token = next_token
        while True:
            _response = self.list_async_invokes(
                config_overrides=config_overrides,
                submit_time_after=submit_time_after,
                submit_time_before=submit_time_before,
                status_equals=status_equals,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("async_invoke_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def converse(
        self,
        model_id: "capo_bedrock_runtime.types.conversational_model_id.ConversationalModelId",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        messages: Optional["capo_bedrock_runtime.types.messages.Messages"] = None,
        system: Optional[
            "capo_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
        ] = None,
        inference_config: Optional[
            "capo_bedrock_runtime.types.inference_configuration.InferenceConfiguration"
        ] = None,
        tool_config: Optional[
            "capo_bedrock_runtime.types.tool_configuration.ToolConfiguration"
        ] = None,
        guardrail_config: Optional[
            "capo_bedrock_runtime.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        additional_model_request_fields: Optional[object] = None,
        prompt_variables: Optional[
            "capo_bedrock_runtime.types.prompt_variable_map.PromptVariableMap"
        ] = None,
        additional_model_response_field_paths: Optional[
            "capo_bedrock_runtime.types.additional_model_response_field_paths.AdditionalModelResponseFieldPaths"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata.RequestMetadata"
        ] = None,
        performance_config: Optional[
            "capo_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier.ServiceTier"
        ] = None,
        output_config: Optional[
            "capo_bedrock_runtime.types.output_config.OutputConfig"
        ] = None,
    ) -> "capo_bedrock_runtime.types.converse_response.ConverseResponse":
        """<p>Sends messages to the specified Amazon Bedrock model. <code>Converse</code> provides a consistent interface that works with all models that support messages. This allows you to write code once and use it with different models. If a model has unique inference parameters, you can also pass those unique parameters to the model.</p> <p>Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response.</p> <p>You can submit a prompt by including it in the <code>messages</code> field, specifying the <code>modelId</code> of a foundation model or inference profile to run inference on it, and including any other fields that are relevant to your use case.</p> <p>You can also submit a prompt from Prompt management by specifying the ARN of the prompt version and including a map of variables to values in the <code>promptVariables</code> field. You can append more messages to the prompt by using the <code>messages</code> field. If you use a prompt from Prompt management, you can't include the following fields in the request: <code>additionalModelRequestFields</code>, <code>inferenceConfig</code>, <code>system</code>, or <code>toolConfig</code>. Instead, these fields must be defined through Prompt management. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html">Use a prompt from Prompt management</a>.</p> <p>For information about the Converse API, see <i>Use the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a guardrail, see <i>Use a guardrail with the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a tool with a model, see <i>Tool use (Function calling)</i> in the <i>Amazon Bedrock User Guide</i> </p> <p>For example code, see <i>Converse API examples</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action. </p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the base inference actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html">InvokeModel</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html">InvokeModelWithResponseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>Converse</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            model_id: <p>Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>To include a prompt that was defined in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management</a>, specify the ARN of the prompt version to use.</p> </li> </ul> <p>The Converse API doesn't support <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported models</a>.</p>
            messages: <p>The messages that you want to send to the model.</p>
            system: <p>A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.</p>
            inference_config: <p>Inference parameters to pass to the model. <code>Converse</code> and <code>ConverseStream</code> support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the <code>additionalModelRequestFields</code> request field.</p>
            tool_config: <p>Configuration information for the tools that the model can use when generating a response. </p> <p>For information about models that support tool use, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features">Supported models and model features</a>.</p>
            guardrail_config: <p>Configuration information for a guardrail that you want to use in the request. If you include <code>guardContent</code> blocks in the <code>content</code> field in the <code>messages</code> field, the guardrail operates only on those messages. If you include no <code>guardContent</code> blocks, the guardrail operates on all messages in the request body and in any included prompt resource.</p>
            additional_model_request_fields: <p>Additional inference parameters that the model supports, beyond the base set of inference parameters that <code>Converse</code> and <code>ConverseStream</code> support in the <code>inferenceConfig</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Model parameters</a>.</p>
            prompt_variables: <p>Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you don't specify a prompt resource in the <code>modelId</code> field.</p>
            additional_model_response_field_paths: <p>Additional model parameters field paths to return in the response. <code>Converse</code> and <code>ConverseStream</code> return the requested fields as a JSON Pointer object in the <code>additionalModelResponseFields</code> field. The following is example JSON for <code>additionalModelResponseFieldPaths</code>.</p> <p> <code>[ "/stop_sequence" ]</code> </p> <p>For information about the JSON Pointer syntax, see the <a href="https://datatracker.ietf.org/doc/html/rfc6901">Internet Engineering Task Force (IETF)</a> documentation.</p> <p> <code>Converse</code> and <code>ConverseStream</code> reject an empty JSON Pointer or incorrectly structured JSON Pointer with a <code>400</code> error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by <code>Converse</code>.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>
            performance_config: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier configuration used for serving the request.</p>
            output_config: <p>Output configuration for a model response.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.converse_request.ConverseRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.converse_response.ConverseResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse.converse(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.converse_request.ConverseRequest = {
            "model_id": model_id
        }
        if messages is not None:
            input_["messages"] = messages
        if system is not None:
            input_["system"] = system
        if inference_config is not None:
            input_["inference_config"] = inference_config
        if tool_config is not None:
            input_["tool_config"] = tool_config
        if guardrail_config is not None:
            input_["guardrail_config"] = guardrail_config
        if additional_model_request_fields is not None:
            input_["additional_model_request_fields"] = additional_model_request_fields
        if prompt_variables is not None:
            input_["prompt_variables"] = prompt_variables
        if additional_model_response_field_paths is not None:
            input_["additional_model_response_field_paths"] = (
                additional_model_response_field_paths
            )
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata
        if performance_config is not None:
            input_["performance_config"] = performance_config
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if output_config is not None:
            input_["output_config"] = output_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def converse_stream(
        self,
        model_id: "capo_bedrock_runtime.types.conversational_model_id.ConversationalModelId",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        messages: Optional["capo_bedrock_runtime.types.messages.Messages"] = None,
        system: Optional[
            "capo_bedrock_runtime.types.system_content_blocks.SystemContentBlocks"
        ] = None,
        inference_config: Optional[
            "capo_bedrock_runtime.types.inference_configuration.InferenceConfiguration"
        ] = None,
        tool_config: Optional[
            "capo_bedrock_runtime.types.tool_configuration.ToolConfiguration"
        ] = None,
        guardrail_config: Optional[
            "capo_bedrock_runtime.types.guardrail_stream_configuration.GuardrailStreamConfiguration"
        ] = None,
        additional_model_request_fields: Optional[object] = None,
        prompt_variables: Optional[
            "capo_bedrock_runtime.types.prompt_variable_map.PromptVariableMap"
        ] = None,
        additional_model_response_field_paths: Optional[
            "capo_bedrock_runtime.types.additional_model_response_field_paths.AdditionalModelResponseFieldPaths"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata.RequestMetadata"
        ] = None,
        performance_config: Optional[
            "capo_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier.ServiceTier"
        ] = None,
        output_config: Optional[
            "capo_bedrock_runtime.types.output_config.OutputConfig"
        ] = None,
    ) -> "Generator[capo_bedrock_runtime.types.converse_stream_response.ConverseStreamResponse]":
        """<p>Sends messages to the specified Amazon Bedrock model and returns the response in a stream. <code>ConverseStream</code> provides a consistent API that works with all Amazon Bedrock models that support messages. This allows you to write code once and use it with different models. Should a model have unique inference parameters, you can also pass those unique parameters to the model. </p> <p>To find out if a model supports streaming, call <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html">GetFoundationModel</a> and check the <code>responseStreamingSupported</code> field in the response.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>ConverseStream</code>.</p> </note> <p>Amazon Bedrock doesn't store any text, images, or documents that you provide as content. The data is only used to generate the response.</p> <p>You can submit a prompt by including it in the <code>messages</code> field, specifying the <code>modelId</code> of a foundation model or inference profile to run inference on it, and including any other fields that are relevant to your use case.</p> <p>You can also submit a prompt from Prompt management by specifying the ARN of the prompt version and including a map of variables to values in the <code>promptVariables</code> field. You can append more messages to the prompt by using the <code>messages</code> field. If you use a prompt from Prompt management, you can't include the following fields in the request: <code>additionalModelRequestFields</code>, <code>inferenceConfig</code>, <code>system</code>, or <code>toolConfig</code>. Instead, these fields must be defined through Prompt management. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-use.html">Use a prompt from Prompt management</a>.</p> <p>For information about the Converse API, see <i>Use the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a guardrail, see <i>Use a guardrail with the Converse API</i> in the <i>Amazon Bedrock User Guide</i>. To use a tool with a model, see <i>Tool use (Function calling)</i> in the <i>Amazon Bedrock User Guide</i> </p> <p>For example code, see <i>Conversation streaming example</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the base inference actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html">InvokeModel</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html">InvokeModelWithResponseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>ConverseStream</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            model_id: <p>Specifies the model or throughput with which to run inference, or the prompt resource to use in inference. The value depends on the resource that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, first purchase Provisioned Throughput for it. Then specify the ARN of the resulting provisioned model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>To include a prompt that was defined in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management</a>, specify the ARN of the prompt version to use.</p> </li> </ul> <p>The Converse API doesn't support <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported models</a>.</p>
            messages: <p>The messages that you want to send to the model.</p>
            system: <p>A prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.</p>
            inference_config: <p>Inference parameters to pass to the model. <code>Converse</code> and <code>ConverseStream</code> support a base set of inference parameters. If you need to pass additional parameters that the model supports, use the <code>additionalModelRequestFields</code> request field.</p>
            tool_config: <p>Configuration information for the tools that the model can use when generating a response.</p> <p>For information about models that support streaming tool use, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html#conversation-inference-supported-models-features">Supported models and model features</a>.</p>
            guardrail_config: <p>Configuration information for a guardrail that you want to use in the request. If you include <code>guardContent</code> blocks in the <code>content</code> field in the <code>messages</code> field, the guardrail operates only on those messages. If you include no <code>guardContent</code> blocks, the guardrail operates on all messages in the request body and in any included prompt resource.</p>
            additional_model_request_fields: <p>Additional inference parameters that the model supports, beyond the base set of inference parameters that <code>Converse</code> and <code>ConverseStream</code> support in the <code>inferenceConfig</code> field. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Model parameters</a>.</p>
            prompt_variables: <p>Contains a map of variables in a prompt from Prompt management to objects containing the values to fill in for them when running model invocation. This field is ignored if you don't specify a prompt resource in the <code>modelId</code> field.</p>
            additional_model_response_field_paths: <p>Additional model parameters field paths to return in the response. <code>Converse</code> and <code>ConverseStream</code> return the requested fields as a JSON Pointer object in the <code>additionalModelResponseFields</code> field. The following is example JSON for <code>additionalModelResponseFieldPaths</code>.</p> <p> <code>[ "/stop_sequence" ]</code> </p> <p>For information about the JSON Pointer syntax, see the <a href="https://datatracker.ietf.org/doc/html/rfc6901">Internet Engineering Task Force (IETF)</a> documentation.</p> <p> <code>Converse</code> and <code>ConverseStream</code> reject an empty JSON Pointer or incorrectly structured JSON Pointer with a <code>400</code> error code. if the JSON Pointer is valid, but the requested field is not in the model response, it is ignored by <code>Converse</code>.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>
            performance_config: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier configuration used for serving the request.</p>
            output_config: <p>Output configuration for a model response.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.converse_stream_response.ConverseStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse_stream

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.converse_stream.converse_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest = {
            "model_id": model_id
        }
        if messages is not None:
            input_["messages"] = messages
        if system is not None:
            input_["system"] = system
        if inference_config is not None:
            input_["inference_config"] = inference_config
        if tool_config is not None:
            input_["tool_config"] = tool_config
        if guardrail_config is not None:
            input_["guardrail_config"] = guardrail_config
        if additional_model_request_fields is not None:
            input_["additional_model_request_fields"] = additional_model_request_fields
        if prompt_variables is not None:
            input_["prompt_variables"] = prompt_variables
        if additional_model_response_field_paths is not None:
            input_["additional_model_response_field_paths"] = (
                additional_model_response_field_paths
            )
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata
        if performance_config is not None:
            input_["performance_config"] = performance_config
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if output_config is not None:
            input_["output_config"] = output_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def invoke_model(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        body: Optional["capo_bedrock_runtime.types.body.Body"] = None,
        content_type: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        accept: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        trace: Optional["capo_bedrock_runtime.types.trace.Trace"] = None,
        guardrail_identifier: Optional[
            "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        guardrail_version: Optional[
            "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
        ] = None,
        performance_config_latency: Optional[
            "capo_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata_json.RequestMetadataJson"
        ] = None,
    ) -> "capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse":
        """<p>Invokes the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body. You use model inference to generate text, images, and embeddings.</p> <p>For example code, see <i>Invoke model code examples</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permission for the <code>bedrock:InvokeModel</code> action.</p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html">Converse</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html">ConverseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>InvokeModel</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            body: <p>The prompt and inference parameters in the format specified in the <code>contentType</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>
            content_type: <p>The MIME type of the input data in the request. You must specify <code>application/json</code>.</p>
            accept: <p>The desired MIME type of the inference body in the response. The default value is <code>application/json</code>.</p>
            model_id: <p>The unique identifier of the model to invoke to run inference.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, specify the ARN of the custom model deployment (for on-demand inference) or the ARN of your provisioned model (for Provisioned Throughput). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            trace: <p>Specifies whether to enable or disable the Bedrock trace. If enabled, you can see the full Bedrock trace.</p>
            guardrail_identifier: <p>The unique identifier of the guardrail that you want to use. If you don't provide a value, no guardrail is applied to the invocation.</p> <p>An error will be thrown in the following situations.</p> <ul> <li> <p>You don't provide a guardrail identifier but you specify the <code>amazon-bedrock-guardrailConfig</code> field in the request body.</p> </li> <li> <p>You enable the guardrail but the <code>contentType</code> isn't <code>application/json</code>.</p> </li> <li> <p>You provide a guardrail identifier, but <code>guardrailVersion</code> isn't specified.</p> </li> </ul>
            guardrail_version: <p>The version number for the guardrail. The value can also be <code>DRAFT</code>.</p>
            performance_config_latency: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier type used for serving the request.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.invoke_model_response.InvokeModelResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model.invoke_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_request.InvokeModelRequest = {
            "model_id": model_id
        }
        if body is not None:
            input_["body"] = body
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if trace is not None:
            input_["trace"] = trace
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version
        if performance_config_latency is not None:
            input_["performance_config_latency"] = performance_config_latency
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def invoke_model_with_bidirectional_stream(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        body: "Iterator[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input._InvokeModelWithBidirectionalStreamInput] | capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_input._InvokeModelWithBidirectionalStreamInput",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
    ) -> "Generator[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse]":
        """<p>Invoke the specified Amazon Bedrock model to run inference using the bidirectional stream. The response is returned in a stream that remains open for 8 minutes. A single session can contain multiple prompts and responses from the model. The prompts to the model are provided as audio files and the model's responses are spoken back to the user and transcribed.</p> <p>It is possible for users to interrupt the model's response with a new prompt, which will halt the response speech. The model will retain contextual awareness of the conversation while pivoting to respond to the new prompt.</p>

        Args:
            model_id: <p>The model ID or ARN of the model ID to use. Currently, only <code>amazon.nova-sonic-v1:0</code> is supported.</p>
            body: <p>The prompt and inference parameters in the format specified in the <code>BidirectionalInputPayloadPart</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException: <p>An error occurred while streaming the response. Retry your request.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_bidirectional_stream

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_bidirectional_stream.invoke_model_with_bidirectional_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest = {
            "model_id": model_id,
            "body": ensure_sync_iterator(body),
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    @contextmanager
    def invoke_model_with_response_stream(
        self,
        model_id: "capo_bedrock_runtime.types.invoke_model_identifier.InvokeModelIdentifier",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
        body: Optional["capo_bedrock_runtime.types.body.Body"] = None,
        content_type: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        accept: Optional["capo_bedrock_runtime.types.mime_type.MimeType"] = None,
        trace: Optional["capo_bedrock_runtime.types.trace.Trace"] = None,
        guardrail_identifier: Optional[
            "capo_bedrock_runtime.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        guardrail_version: Optional[
            "capo_bedrock_runtime.types.guardrail_version.GuardrailVersion"
        ] = None,
        performance_config_latency: Optional[
            "capo_bedrock_runtime.types.performance_config_latency.PerformanceConfigLatency"
        ] = None,
        service_tier: Optional[
            "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
        ] = None,
        request_metadata: Optional[
            "capo_bedrock_runtime.types.request_metadata_json.RequestMetadataJson"
        ] = None,
    ) -> "Generator[capo_bedrock_runtime.types.invoke_model_with_response_stream_response.InvokeModelWithResponseStreamResponse]":
        """<p>Invoke the specified Amazon Bedrock model to run inference using the prompt and inference parameters provided in the request body. The response is returned in a stream.</p> <p>To see if a model supports streaming, call <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html">GetFoundationModel</a> and check the <code>responseStreamingSupported</code> field in the response.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeModelWithResponseStream</code>.</p> </note> <p>For example code, see <i>Invoke model with streaming code example</i> in the <i>Amazon Bedrock User Guide</i>. </p> <p>This operation requires permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action. </p> <important> <p>To deny all inference access to resources that you specify in the modelId field, you need to deny access to the <code>bedrock:InvokeModel</code> and <code>bedrock:InvokeModelWithResponseStream</code> actions. Doing this also denies access to the resource through the Converse API actions (<a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html">Converse</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html">ConverseStream</a>). For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-deny-inference">Deny access for inference on specific models</a>. </p> </important> <p>For troubleshooting some of the common errors you might encounter when using the <code>InvokeModelWithResponseStream</code> API, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html">Troubleshooting Amazon Bedrock API Error Codes</a> in the Amazon Bedrock User Guide</p>

        Args:
            body: <p>The prompt and inference parameters in the format specified in the <code>contentType</code> in the header. You must provide the body in JSON format. To see the format and content of the request and response bodies for different models, refer to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html">Inference parameters</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/api-methods-run.html">Run inference</a> in the Bedrock User Guide.</p>
            content_type: <p>The MIME type of the input data in the request. You must specify <code>application/json</code>.</p>
            accept: <p>The desired MIME type of the inference body in the response. The default value is <code>application/json</code>.</p>
            model_id: <p>The unique identifier of the model to invoke to run inference.</p> <p>The <code>modelId</code> to provide depends on the type of model or throughput that you use:</p> <ul> <li> <p>If you use a base model, specify the model ID or its ARN. For a list of model IDs for base models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">Amazon Bedrock base model IDs (on-demand throughput)</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an inference profile, specify the inference profile ID or its ARN. For a list of inference profile IDs, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference-support.html">Supported Regions and models for cross-region inference</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a provisioned model, specify the ARN of the Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html">Run inference using a Provisioned Throughput</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use a custom model, specify the ARN of the custom model deployment (for on-demand inference) or the ARN of your provisioned model (for Provisioned Throughput). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Use a custom model in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p> </li> <li> <p>If you use an <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">imported model</a>, specify the ARN of the imported model. You can get the model ARN from a successful call to <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelImportJob.html">CreateModelImportJob</a> or from the Imported models page in the Amazon Bedrock console.</p> </li> </ul>
            trace: <p>Specifies whether to enable or disable the Bedrock trace. If enabled, you can see the full Bedrock trace.</p>
            guardrail_identifier: <p>The unique identifier of the guardrail that you want to use. If you don't provide a value, no guardrail is applied to the invocation.</p> <p>An error is thrown in the following situations.</p> <ul> <li> <p>You don't provide a guardrail identifier but you specify the <code>amazon-bedrock-guardrailConfig</code> field in the request body.</p> </li> <li> <p>You enable the guardrail but the <code>contentType</code> isn't <code>application/json</code>.</p> </li> <li> <p>You provide a guardrail identifier, but <code>guardrailVersion</code> isn't specified.</p> </li> </ul>
            guardrail_version: <p>The version number for the guardrail. The value can also be <code>DRAFT</code>.</p>
            performance_config_latency: <p>Model performance settings for the request.</p>
            service_tier: <p>Specifies the processing tier type used for serving the request.</p>
            request_metadata: <p>Key-value pairs that you can use to filter invocation logs.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.model_error_exception.ModelErrorException: <p>The request failed due to an error while processing the model.</p>
            capo_bedrock_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide.</p>
            capo_bedrock_runtime.errors.model_stream_error_exception.ModelStreamErrorException: <p>An error occurred while streaming the response. Retry your request.</p>
            capo_bedrock_runtime.errors.model_timeout_exception.ModelTimeoutException: <p>The request took too long to process. Processing time exceeded the model timeout length.</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds the service quota for your account. You can view your quotas at <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html">Viewing service quotas</a>. You can resubmit your request later.</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.invoke_model_with_response_stream_request.InvokeModelWithResponseStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.invoke_model_with_response_stream_response.InvokeModelWithResponseStreamResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_response_stream

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.invoke_model_with_response_stream.invoke_model_with_response_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.invoke_model_with_response_stream_request.InvokeModelWithResponseStreamRequest = {
            "model_id": model_id
        }
        if body is not None:
            input_["body"] = body
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if trace is not None:
            input_["trace"] = trace
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version
        if performance_config_latency is not None:
            input_["performance_config_latency"] = performance_config_latency
        if service_tier is not None:
            input_["service_tier"] = service_tier
        if request_metadata is not None:
            input_["request_metadata"] = request_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def count_tokens(
        self,
        model_id: "capo_bedrock_runtime.types.foundation_model_version_identifier.FoundationModelVersionIdentifier",
        input: "capo_bedrock_runtime.types.count_tokens_input.CountTokensInput",
        *,
        config_overrides: Optional[BedrockRuntimeClientConfig] = None,
    ) -> "capo_bedrock_runtime.types.count_tokens_response.CountTokensResponse":
        """<p>Returns the token count for a given inference request. This operation helps you estimate token usage before sending requests to foundation models by returning the token count that would be used if the same input were sent to the model in an inference request.</p> <p>Token counting is model-specific because different models use different tokenization strategies. The token count returned by this operation will match the token count that would be charged if the same input were sent to the model in an <code>InvokeModel</code> or <code>Converse</code> request.</p> <p>You can use this operation to:</p> <ul> <li> <p>Estimate costs before sending inference requests.</p> </li> <li> <p>Optimize prompts to fit within token limits.</p> </li> <li> <p>Plan for token usage in your applications.</p> </li> </ul> <p>This operation accepts the same input formats as <code>InvokeModel</code> and <code>Converse</code>, allowing you to count tokens for both raw text inputs and structured conversation formats.</p> <p>The following operations are related to <code>CountTokens</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/API/API_runtime_InvokeModel.html">InvokeModel</a> - Sends inference requests to foundation models</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/API/API_runtime_Converse.html">Converse</a> - Sends conversation-based inference requests to foundation models</p> </li> </ul>

        Args:
            model_id: <p>The unique identifier or ARN of the foundation model to use for token counting. Each model processes tokens differently, so the token count is specific to the model you specify.</p>
            input: <p>The input for which to count tokens. The structure of this parameter depends on whether you're counting tokens for an <code>InvokeModel</code> or <code>Converse</code> request:</p> <ul> <li> <p>For <code>InvokeModel</code> requests, provide the request body in the <code>invokeModel</code> field</p> </li> <li> <p>For <code>Converse</code> requests, provide the messages and system content in the <code>converse</code> field</p> </li> </ul> <p>The input format must be compatible with the model specified in the <code>modelId</code> parameter.</p>

        Raises:
            capo_bedrock_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied">AccessDeniedException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure">InternalFailure</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource ARN was not found. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found">ResourceNotFound</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service isn't currently available. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-service-unavailable">ServiceUnavailable</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.throttling_exception.ThrottlingException: <p>Your request was denied due to exceeding the account quotas for <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception">ThrottlingException</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by <i>Amazon Bedrock</i>. For troubleshooting this error, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error">ValidationError</a> in the Amazon Bedrock User Guide</p>
            capo_bedrock_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_runtime.types.count_tokens_request.CountTokensRequest]",
        ) -> OperationResponse[
            "capo_bedrock_runtime.types.count_tokens_response.CountTokensResponse"
        ]:
            import capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.count_tokens

            output, http_response = (
                capo_bedrock_runtime._operations.amazon_bedrock_frontend_service.count_tokens.count_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_runtime.types.count_tokens_request.CountTokensRequest = {
            "model_id": model_id,
            "input": input,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
