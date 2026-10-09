"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#AmazonSageMakerRuntimeHttp2``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sagemaker_runtime_http2._auth._signers
import capo_sagemaker_runtime_http2._auth._sigv4
from capo_sagemaker_runtime_http2._auth._identity import Credentials
from capo_sagemaker_runtime_http2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemaker_runtime_http2._auth._zapros_handler import AuthMiddleware
from capo_sagemaker_runtime_http2._iter import (
    ensure_async_iterator,
)
from capo_sagemaker_runtime_http2._services._aws_config import aaws_config
from capo_sagemaker_runtime_http2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input
    import capo_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output
    import capo_sagemaker_runtime_http2.types.request_stream_event


class AsyncSageMakerRuntimeHTTP2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSageMakerRuntimeHTTP2Client:
    """A client for the ``SageMakerRuntimeHTTP2`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
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
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncSageMakerRuntimeHTTP2ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSageMakerRuntimeHTTP2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSageMakerRuntimeHTTP2ClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
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

    @asynccontextmanager
    async def invoke_endpoint_with_bidirectional_stream(
        self,
        endpoint_name: str,
        body: "AsyncIterator[capo_sagemaker_runtime_http2.types.request_stream_event._RequestStreamEvent] | capo_sagemaker_runtime_http2.types.request_stream_event._RequestStreamEvent",
        *,
        config_overrides: Optional[AsyncSageMakerRuntimeHTTP2ClientConfig] = None,
        target_variant: Optional[str] = None,
        model_invocation_path: Optional[str] = None,
        model_query_string: Optional[str] = None,
    ) -> "AsyncGenerator[capo_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput]":
        """<p>Invokes a model endpoint with bidirectional streaming capabilities. This operation establishes a persistent connection that allows you to send multiple requests and receive streaming responses from the model in real-time.</p> <p>Bidirectional streaming is useful for interactive applications such as chatbots, real-time translation, or any scenario where you need to maintain a conversation-like interaction with the model. The connection remains open, allowing you to send additional input and receive responses without establishing a new connection for each request.</p> <p>For an overview of Amazon SageMaker AI, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html">How It Works</a>.</p> <p>Amazon SageMaker AI strips all POST headers except those supported by the API. Amazon SageMaker AI might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax. </p> <p>Calls to <code>InvokeEndpointWithBidirectionalStream</code> are authenticated by using Amazon Web Services Signature Version 4. For information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon S3 API Reference</i>.</p> <p>The bidirectional stream maintains the connection until either the client closes it or the model indicates completion. Each request and response in the stream is sent as an event with optional headers for data type and completion state.</p> <note> <p>Endpoints are scoped to an individual account, and are not public. The URL does not contain the account ID, but Amazon SageMaker AI determines the account ID from the authentication token that is supplied by the caller.</p> </note>

        Args:
            endpoint_name: <p>The name of the endpoint to invoke.</p>
            body: <p>The request payload stream.</p>
            target_variant: <p>Target variant for the request.</p>
            model_invocation_path: <p>Model invocation path.</p>
            model_query_string: <p>Model query string.</p>

        Raises:
            capo_sagemaker_runtime_http2.errors.input_validation_error.InputValidationError: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_sagemaker_runtime_http2.errors.internal_server_error.InternalServerError: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_sagemaker_runtime_http2.errors.internal_stream_failure.InternalStreamFailure: <p>Internal stream failure that occurs during streaming.</p>
            capo_sagemaker_runtime_http2.errors.model_error.ModelError: <p>An error occurred while processing the model.</p>
            capo_sagemaker_runtime_http2.errors.model_stream_error.ModelStreamError: <p>Model stream error that occurs during streaming.</p>
            capo_sagemaker_runtime_http2.errors.service_unavailable_error.ServiceUnavailableError: <p>The request has failed due to a temporary failure of the server.</p>
            capo_sagemaker_runtime_http2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input.InvokeEndpointWithBidirectionalStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput"
        ]:
            import capo_sagemaker_runtime_http2._operations.amazon_sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream

            (
                output,
                http_response,
            ) = await capo_sagemaker_runtime_http2._operations.amazon_sage_maker_runtime_http2.invoke_endpoint_with_bidirectional_stream.async_invoke_endpoint_with_bidirectional_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input.InvokeEndpointWithBidirectionalStreamInput = {
            "endpoint_name": endpoint_name,
            "body": ensure_async_iterator(body),
        }
        if target_variant is not None:
            input_["target_variant"] = target_variant
        if model_invocation_path is not None:
            input_["model_invocation_path"] = model_invocation_path
        if model_query_string is not None:
            input_["model_query_string"] = model_query_string

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
