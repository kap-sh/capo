"""Generated from Smithy shape ``com.amazonaws.sagemakerinferencerouterruntime#SageMakerInferenceRouterRuntime``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sagemaker_inference_router_runtime._auth._signers
import capo_sagemaker_inference_router_runtime._auth._sigv4
from capo_sagemaker_inference_router_runtime._auth._identity import Credentials
from capo_sagemaker_inference_router_runtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemaker_inference_router_runtime._auth._zapros_handler import AuthMiddleware
from capo_sagemaker_inference_router_runtime._services._aws_config import aaws_config
from capo_sagemaker_inference_router_runtime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    RateLimiter,
    RetryQuota,
    aexecute_pipeline,
    alog_operation,
    arate_limit,
    aretry,
)

if TYPE_CHECKING:
    import capo_sagemaker_inference_router_runtime.types.custom_attributes_header
    import capo_sagemaker_inference_router_runtime.types.inference_router_body_blob
    import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input
    import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output
    import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_input
    import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_output


class AsyncSageMakerInferenceRouterRuntimeClientConfig(
    TypedDict, total=False, closed=True
):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSageMakerInferenceRouterRuntimeClient:
    """A client for the ``SageMakerInferenceRouterRuntime`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        retry_mode: Literal["standard", "adaptive"] | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = AsyncClient(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = RetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = RateLimiter()
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(raw_handler)
            )
        self._config = AsyncSageMakerInferenceRouterRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[
            AsyncSageMakerInferenceRouterRuntimeClientConfig
        ] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSageMakerInferenceRouterRuntimeClientConfig = (
            config_overrides or {}
        )
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(alog_operation(operation_logging))
        interceptors_.append(aretry())
        interceptors_.append(arate_limit())
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def invoke_inference_router(
        self,
        inference_router_name: str,
        routing_target_name: str,
        body: "capo_sagemaker_inference_router_runtime.types.inference_router_body_blob.InferenceRouterBodyBlob",
        *,
        config_overrides: Optional[
            AsyncSageMakerInferenceRouterRuntimeClientConfig
        ] = None,
        content_type: Optional[str] = None,
        accept: Optional[str] = None,
        inference_id: Optional[str] = None,
        prefix_aware_id: Optional[str] = None,
        custom_attributes: Optional[
            "capo_sagemaker_inference_router_runtime.types.custom_attributes_header.CustomAttributesHeader"
        ] = None,
    ) -> "capo_sagemaker_inference_router_runtime.types.invoke_inference_router_output.InvokeInferenceRouterOutput":
        """<p>Sends a real-time inference request to an inference router. In the request, you name the routing target, and the router sends the request to one of the routing target's destinations. The response includes the destination that served the request and the reason that the router chose it.</p> <p>The following limits apply:</p> <ul> <li> <p>The maximum request payload is 6 MB. A request with a larger body fails with HTTP status code 413.</p> </li> <li> <p>Your model has up to 60 seconds for each attempt, the same limit as <code>InvokeEndpoint</code>. If your account has a higher model execution timeout for <code>InvokeEndpoint</code>, it doesn't apply through an inference router. For models that take longer, use <code>InvokeInferenceRouterAsync</code>.</p> </li> </ul> <p>If a destination returns an error that the router can retry, such as a throttling error, before your model produces a response, the router retries the request once on another destination. A request that times out on a destination isn't retried. Because a request can make two attempts, set your client read timeout to at least 170 seconds.</p> <p>The caller needs permission to invoke the inference router and every destination of the routing target. For information about permissions, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router.html">Route requests across Regions with inference routers</a>.</p>

        Args:
            inference_router_name: <p>The name of the inference router to invoke.</p>
            routing_target_name: <p>The name of the routing target in the inference router. The routing target lists the destinations that can serve the request.</p>
            content_type: <p>The MIME type of the input data in the request body. The router passes it to the destination.</p>
            accept: <p>The MIME type that you want for the inference response. The router passes it to the destination.</p>
            inference_id: <p>An identifier for the inference request. The router passes it to the destination.</p>
            prefix_aware_id: <p>An optional, stable identifier that serves as a routing hint for prefix-aware routing. The router passes it to the destination that serves the request. Within that destination, requests with the same prefix and the same identifier go to the same instance. If requests from different applications might have the same prompt prefix, set a different identifier for each application to differentiate their routing decisions.</p> <p>Applies only to destination endpoints configured with a <code>RoutingStrategy</code> of <code>PREFIX_AWARE</code>.</p>
            custom_attributes: <p>Provides additional information about the inference request. The value is an opaque string that the router passes, unchanged, to the model container of the destination that serves the request. The value can contain up to 1,024 visible US-ASCII characters.</p>
            body: <p>The input data for the inference, in the format that your model expects. The body can't be empty.</p>

        Raises:
            capo_sagemaker_inference_router_runtime.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this action. Check that the caller is allowed to invoke the inference router and every destination of the routing target.</p>
            capo_sagemaker_inference_router_runtime.errors.internal_dependency_exception.InternalDependencyException: <p>The request failed because of an error in an internal dependency. Retry the request with exponential backoff.</p>
            capo_sagemaker_inference_router_runtime.errors.internal_failure.InternalFailure: <p>An internal error occurred. Retry the request with exponential backoff. The Amazon Web Services SDKs and the Amazon Web Services CLI do this by default.</p>
            capo_sagemaker_inference_router_runtime.errors.model_error.ModelError: <p>The model in the destination that served the request returned an error. Check <code>OriginalStatusCode</code>, <code>OriginalMessage</code>, and the destination's logs in Amazon CloudWatch.</p>
            capo_sagemaker_inference_router_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p>The destination isn't ready to serve the model, for example because an inference component has no copies. Retry the request later.</p>
            capo_sagemaker_inference_router_runtime.errors.request_timeout_exception.RequestTimeoutException: <p>The inference router didn't receive the complete request within 300 seconds of accepting it, for example because of a very slow upload. Retry the request.</p>
            capo_sagemaker_inference_router_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. For example, no destination of the routing target could serve the request, or a destination didn't respond. Retry the request with exponential backoff. The Amazon Web Services SDKs and the Amazon Web Services CLI do this by default.</p>
            capo_sagemaker_inference_router_runtime.errors.throttling_exception.ThrottlingException: <p>The request was denied because you exceeded the request rate for the inference router, or because a destination throttled the request. Retry the request with exponential backoff.</p>
            capo_sagemaker_inference_router_runtime.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the inference router name, the routing target name, and the request parameters, and then try again.</p>
            capo_sagemaker_inference_router_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke an inference router
            The following example sends a JSON request to the my-target routing target of the my-router inference router. The response shows that a destination in the router's Region served the request.

            >>> await client.invoke_inference_router(inference_router_name='my-router', routing_target_name='my-target', content_type='application/json', body='{"instances": [[1.0, 2.0, 5.0]]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_inference_router_runtime.types.invoke_inference_router_input.InvokeInferenceRouterInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_inference_router_runtime.types.invoke_inference_router_output.InvokeInferenceRouterOutput"
        ]:
            import capo_sagemaker_inference_router_runtime._operations.sage_maker_inference_router_runtime.invoke_inference_router

            (
                output,
                http_response,
            ) = await capo_sagemaker_inference_router_runtime._operations.sage_maker_inference_router_runtime.invoke_inference_router.async_invoke_inference_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemaker_inference_router_runtime.types.invoke_inference_router_input.InvokeInferenceRouterInput",
        ) -> dict[str, Any]:
            import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_input

            return capo_sagemaker_inference_router_runtime.types.invoke_inference_router_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemaker_inference_router_runtime.types.invoke_inference_router_output.InvokeInferenceRouterOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_output

            return capo_sagemaker_inference_router_runtime.types.invoke_inference_router_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "InvokeInferenceRouter",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemaker_inference_router_runtime.types.invoke_inference_router_input.InvokeInferenceRouterInput = {
            "inference_router_name": inference_router_name,
            "routing_target_name": routing_target_name,
            "body": body,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if inference_id is not None:
            input_["inference_id"] = inference_id
        if prefix_aware_id is not None:
            input_["prefix_aware_id"] = prefix_aware_id
        if custom_attributes is not None:
            input_["custom_attributes"] = custom_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def invoke_inference_router_async(
        self,
        inference_router_name: str,
        routing_target_name: str,
        input_location: str,
        *,
        config_overrides: Optional[
            AsyncSageMakerInferenceRouterRuntimeClientConfig
        ] = None,
        content_type: Optional[str] = None,
        accept: Optional[str] = None,
        custom_attributes: Optional[
            "capo_sagemaker_inference_router_runtime.types.custom_attributes_header.CustomAttributesHeader"
        ] = None,
        inference_id: Optional[str] = None,
        s3_output_path_extension: Optional[str] = None,
        filename: Optional[str] = None,
        request_ttl_seconds: Optional[int] = None,
        invocation_timeout_seconds: Optional[int] = None,
    ) -> "capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.InvokeInferenceRouterAsyncOutput":
        """<p>Submits an asynchronous inference request to an inference router. Before you call this operation, upload the input data to Amazon S3 in the router's Amazon Web Services Region. The router returns as soon as it accepts the request, and sends the request to one of the destinations of the routing target. The destination reads the input from Amazon S3, and the inference response is written to the Amazon S3 output path that the routing target specifies.</p> <p>If a destination doesn't start the request within the routing target's <code>MaxTimeInBacklogSeconds</code>, the router moves the request to another destination. After your model starts processing the request, the request doesn't move. If no destination can take the request before <code>RequestTTLSeconds</code> runs out, or every destination has been tried, the router writes a failure object to the <code>FailureLocation</code> and publishes a notification to the routing target's error topic, if one is configured.</p> <p>For information about the permissions that the caller and each destination need, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html">Send asynchronous requests through an inference router</a>.</p>

        Args:
            inference_router_name: <p>The name of the inference router to invoke.</p>
            routing_target_name: <p>The name of the routing target in the inference router. The routing target must be configured for asynchronous inference.</p>
            content_type: <p>The MIME type of the input data in Amazon S3. The router passes it to the destination.</p>
            accept: <p>The MIME type that you want for the inference response. The router passes it to the destination.</p>
            custom_attributes: <p>Provides additional information about the inference request. The value is an opaque string that the router passes, unchanged, to the model container of the destination that serves the request. The value can contain up to 1,024 visible US-ASCII characters.</p>
            inference_id: <p>An identifier for the inference request. If you don't provide one, SageMaker AI generates one and returns it in the response.</p>
            input_location: <p>The Amazon S3 URI of the object that contains the input data for the inference. The bucket must be in the inference router's Amazon Web Services Region and owned by the router's account. The destination endpoint's execution role reads the object, and the destination's asynchronous inference limits apply to it.</p>
            s3_output_path_extension: <p>The path extension that is appended to the routing target's Amazon S3 output path where the inference response is stored.</p>
            filename: <p>The file name of the inference response stored in Amazon S3. If you don't provide one, SageMaker AI generates one.</p>
            request_ttl_seconds: <p>The time to live of the request, in seconds, measured from when the router accepts it. If no destination starts the request in this time, the request fails. The default is 21,600 seconds (6 hours).</p>
            invocation_timeout_seconds: <p>The maximum time, in seconds, that a destination can spend processing the request before the request is marked as expired. The default is 900 seconds (15 minutes).</p>

        Raises:
            capo_sagemaker_inference_router_runtime.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this action. Check that the caller is allowed to invoke the inference router and every destination of the routing target.</p>
            capo_sagemaker_inference_router_runtime.errors.internal_failure.InternalFailure: <p>An internal error occurred. Retry the request with exponential backoff. The Amazon Web Services SDKs and the Amazon Web Services CLI do this by default.</p>
            capo_sagemaker_inference_router_runtime.errors.request_timeout_exception.RequestTimeoutException: <p>The inference router didn't receive the complete request within 300 seconds of accepting it, for example because of a very slow upload. Retry the request.</p>
            capo_sagemaker_inference_router_runtime.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. For example, no destination of the routing target could serve the request, or a destination didn't respond. Retry the request with exponential backoff. The Amazon Web Services SDKs and the Amazon Web Services CLI do this by default.</p>
            capo_sagemaker_inference_router_runtime.errors.throttling_exception.ThrottlingException: <p>The request was denied because you exceeded the request rate for the inference router, or because a destination throttled the request. Retry the request with exponential backoff.</p>
            capo_sagemaker_inference_router_runtime.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the inference router name, the routing target name, and the request parameters, and then try again.</p>
            capo_sagemaker_inference_router_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input.InvokeInferenceRouterAsyncInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_output.InvokeInferenceRouterAsyncOutput"
        ]:
            import capo_sagemaker_inference_router_runtime._operations.sage_maker_inference_router_runtime.invoke_inference_router_async

            (
                output,
                http_response,
            ) = await capo_sagemaker_inference_router_runtime._operations.sage_maker_inference_router_runtime.invoke_inference_router_async.async_invoke_inference_router_async(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input.InvokeInferenceRouterAsyncInput",
        ) -> dict[str, Any]:
            import capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input

            return capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("InvokeInferenceRouterAsync", redact_input=_redact_input),
        )
        input_: capo_sagemaker_inference_router_runtime.types.invoke_inference_router_async_input.InvokeInferenceRouterAsyncInput = {
            "inference_router_name": inference_router_name,
            "routing_target_name": routing_target_name,
            "input_location": input_location,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if custom_attributes is not None:
            input_["custom_attributes"] = custom_attributes
        if inference_id is not None:
            input_["inference_id"] = inference_id
        if s3_output_path_extension is not None:
            input_["s3_output_path_extension"] = s3_output_path_extension
        if filename is not None:
            input_["filename"] = filename
        if request_ttl_seconds is not None:
            input_["request_ttl_seconds"] = request_ttl_seconds
        if invocation_timeout_seconds is not None:
            input_["invocation_timeout_seconds"] = invocation_timeout_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
