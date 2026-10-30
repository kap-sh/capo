"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#LegoRouterService``."""

import warnings
from collections.abc import Generator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_sagemakertrainingsessionruntime._auth._signers
import capo_sagemakertrainingsessionruntime._auth._sigv4
from capo_sagemakertrainingsessionruntime._auth._identity import Credentials
from capo_sagemakertrainingsessionruntime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemakertrainingsessionruntime._auth._zapros_handler import AuthMiddleware
from capo_sagemakertrainingsessionruntime._services._aws_config import aws_config
from capo_sagemakertrainingsessionruntime._services._pipeline import (
    Interceptor,
    OperationLogging,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    ThreadSafeRetryQuota,
    execute_pipeline,
    log_operation,
    retry,
)

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.client_token
    import capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_input
    import capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_output
    import capo_sagemakertrainingsessionruntime.types.execute_training_operation_input
    import capo_sagemakertrainingsessionruntime.types.execute_training_operation_output
    import capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_input
    import capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_output
    import capo_sagemakertrainingsessionruntime.types.get_training_operation_result_input
    import capo_sagemakertrainingsessionruntime.types.get_training_operation_result_output
    import capo_sagemakertrainingsessionruntime.types.inference_body
    import capo_sagemakertrainingsessionruntime.types.operation_config
    import capo_sagemakertrainingsessionruntime.types.operation_id
    import capo_sagemakertrainingsessionruntime.types.sample_operation_config
    import capo_sagemakertrainingsessionruntime.types.sample_training_session_input
    import capo_sagemakertrainingsessionruntime.types.sample_training_session_output
    import capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_input
    import capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_output
    import capo_sagemakertrainingsessionruntime.types.sequence_number
    import capo_sagemakertrainingsessionruntime.types.training_session_name


class SageMakerTrainingSessionRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SageMakerTrainingSessionRuntimeClient:
    """A client for the ``SageMakerTrainingSessionRuntime`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = Client(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = ThreadSafeRetryQuota()
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
                Client(raw_handler)
            )
        self._config = SageMakerTrainingSessionRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[SageMakerTrainingSessionRuntimeClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SageMakerTrainingSessionRuntimeClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(log_operation(operation_logging))
        interceptors_.append(retry())
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
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

    def execute_sampling_operation(
        self,
        training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName",
        operation_config: "capo_sagemakertrainingsessionruntime.types.sample_operation_config.SampleOperationConfig",
        *,
        config_overrides: Optional[SageMakerTrainingSessionRuntimeClientConfig] = None,
    ) -> "capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_output.ExecuteSamplingOperationOutput":
        """<p>Submits an asynchronous sampling operation to generate text or compute log-probabilities from the model associated with the specified training session. The session must be in <code>Running</code> or <code>Blocked</code> state. Use <code>GetSamplingOperationResult</code> to poll for the result.</p>

        Args:
            training_session_name: <p>The name of the training session to sample from.</p>
            operation_config: <p>The configuration for the sample operation. Specify either a sample configuration to generate text or a computeLogprobs configuration to compute token log-probabilities.</p>

        Raises:
            capo_sagemakertrainingsessionruntime.errors.conflict_exception.ConflictException: <p>The training session is in a state that cannot accept new operations. The session must be in <code>Running</code> or <code>Blocked</code> state to accept requests.</p>
            capo_sagemakertrainingsessionruntime.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Retry the request using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified training session or operation does not exist, or the operation does not belong to the specified training session.</p>
            capo_sagemakertrainingsessionruntime.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry the request after a brief wait using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.validation_exception.ValidationException: <p>The request is not valid. Check the request syntax and parameters. Examples include invalid sequence numbers, malformed client tokens, missing required fields, or invalid operation configuration.</p>
            capo_sagemakertrainingsessionruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Generate samples from a prompt
            Generates completions for a tokenized prompt using the session's current weights. Generation behavior is controlled by `samplingParams`, and the operation is dispatched asynchronously.

            >>> client.execute_sampling_operation(training_session_name='my-training-session', operation_config={'sample': {'prompt': {'chunks': [{'tokens': [791, 6864, 315, 9822, 374], 'type': 'encoded_text'}]}, 'numSamples': 4, 'samplingParams': {'maxTokens': 1024, 'temperature': 0.7, 'topP': 0.9}}})
        """

        def _handler(
            req: "OperationRequest[capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_input.ExecuteSamplingOperationInput]",
        ) -> OperationResponse[
            "capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_output.ExecuteSamplingOperationOutput"
        ]:
            import capo_sagemakertrainingsessionruntime._operations.lego_router_service.execute_sampling_operation

            output, http_response = (
                capo_sagemakertrainingsessionruntime._operations.lego_router_service.execute_sampling_operation.execute_sampling_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_input.ExecuteSamplingOperationInput",
        ) -> dict[str, Any]:
            import capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_input

            return capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("ExecuteSamplingOperation", redact_input=_redact_input),
        )
        input_: capo_sagemakertrainingsessionruntime.types.execute_sampling_operation_input.ExecuteSamplingOperationInput = {
            "training_session_name": training_session_name,
            "operation_config": operation_config,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_training_operation(
        self,
        training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName",
        sequence_number: "capo_sagemakertrainingsessionruntime.types.sequence_number.SequenceNumber",
        operation_config: "capo_sagemakertrainingsessionruntime.types.operation_config.OperationConfig",
        *,
        config_overrides: Optional[SageMakerTrainingSessionRuntimeClientConfig] = None,
        client_token: Optional[
            "capo_sagemakertrainingsessionruntime.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_sagemakertrainingsessionruntime.types.execute_training_operation_output.ExecuteTrainingOperationOutput":
        """<p>Submits an asynchronous training operation to the specified training session. The service executes operations in sequence number order. The session must be in <code>Running</code> or <code>Blocked</code> state. Use <code>GetTrainingOperationResult</code> to poll for the result. Supported operation types: <code>forward</code>, <code>forwardBackward</code>, <code>optimizerStep</code>, <code>saveWeights</code>, <code>saveState</code>, and <code>loadState</code>.</p>

        Args:
            training_session_name: <p>The name of the training session to submit the operation to.</p>
            sequence_number: <p>The monotonically increasing sequence number that determines execution order. The training session processes operations strictly in sequence number order. If a gap exists, the session blocks until the missing operation arrives or times out. Must be at least 1.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service ignores the request but does not return an error.</p>
            operation_config: <p>The configuration that specifies the type and parameters of the training operation. Exactly one member of the union must be set.</p>

        Raises:
            capo_sagemakertrainingsessionruntime.errors.conflict_exception.ConflictException: <p>The training session is in a state that cannot accept new operations. The session must be in <code>Running</code> or <code>Blocked</code> state to accept requests.</p>
            capo_sagemakertrainingsessionruntime.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Retry the request using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified training session or operation does not exist, or the operation does not belong to the specified training session.</p>
            capo_sagemakertrainingsessionruntime.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry the request after a brief wait using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.validation_exception.ValidationException: <p>The request is not valid. Check the request syntax and parameters. Examples include invalid sequence numbers, malformed client tokens, missing required fields, or invalid operation configuration.</p>
            capo_sagemakertrainingsessionruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Run a forward and backward pass
            Computes gradients for a batch of tokenized prompts and accumulates them into the session. Operations are applied in `sequenceNumber` order, so each call must supply the next number in the sequence.

            >>> client.execute_training_operation(training_session_name='my-training-session', sequence_number=1, operation_config={'forwardBackward': {'lossFnName': 'cross_entropy', 'datumList': [{'modelInput': {'chunks': [{'tokens': [791, 6864, 315, 9822, 374, 12366], 'type': 'encoded_text'}]}}]}})
        """

        def _handler(
            req: "OperationRequest[capo_sagemakertrainingsessionruntime.types.execute_training_operation_input.ExecuteTrainingOperationInput]",
        ) -> OperationResponse[
            "capo_sagemakertrainingsessionruntime.types.execute_training_operation_output.ExecuteTrainingOperationOutput"
        ]:
            import capo_sagemakertrainingsessionruntime._operations.lego_router_service.execute_training_operation

            output, http_response = (
                capo_sagemakertrainingsessionruntime._operations.lego_router_service.execute_training_operation.execute_training_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemakertrainingsessionruntime.types.execute_training_operation_input.ExecuteTrainingOperationInput",
        ) -> dict[str, Any]:
            import capo_sagemakertrainingsessionruntime.types.execute_training_operation_input

            return capo_sagemakertrainingsessionruntime.types.execute_training_operation_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("ExecuteTrainingOperation", redact_input=_redact_input),
        )
        input_: capo_sagemakertrainingsessionruntime.types.execute_training_operation_input.ExecuteTrainingOperationInput = {
            "training_session_name": training_session_name,
            "sequence_number": sequence_number,
            "operation_config": operation_config,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sampling_operation_result(
        self,
        training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName",
        operation_id: "capo_sagemakertrainingsessionruntime.types.operation_id.OperationId",
        *,
        config_overrides: Optional[SageMakerTrainingSessionRuntimeClientConfig] = None,
    ) -> "capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_output.GetSamplingOperationResultOutput":
        """<p>Retrieves the current status and result of a previously submitted sampling operation. Poll this operation until the status reaches a terminal state (Completed or Failed).</p>

        Args:
            training_session_name: <p>The name of the training session that owns the sample operation.</p>
            operation_id: <p>The unique identifier of the sample operation to retrieve, returned by <code>ExecuteSamplingOperation</code>.</p>

        Raises:
            capo_sagemakertrainingsessionruntime.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Retry the request using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified training session or operation does not exist, or the operation does not belong to the specified training session.</p>
            capo_sagemakertrainingsessionruntime.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry the request after a brief wait using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.validation_exception.ValidationException: <p>The request is not valid. Check the request syntax and parameters. Examples include invalid sequence numbers, malformed client tokens, missing required fields, or invalid operation configuration.</p>
            capo_sagemakertrainingsessionruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the result of a sampling operation
            Retrieves the status and generated sequences for a sampling operation submitted with ExecuteSamplingOperation.

            >>> client.get_sampling_operation_result(training_session_name='my-training-session', operation_id='a1b2c3d4-5678-90ab-cdef-1234567890ab')
        """

        def _handler(
            req: "OperationRequest[capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_input.GetSamplingOperationResultInput]",
        ) -> OperationResponse[
            "capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_output.GetSamplingOperationResultOutput"
        ]:
            import capo_sagemakertrainingsessionruntime._operations.lego_router_service.get_sampling_operation_result

            output, http_response = (
                capo_sagemakertrainingsessionruntime._operations.lego_router_service.get_sampling_operation_result.get_sampling_operation_result(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_output.GetSamplingOperationResultOutput",
        ) -> dict[str, Any]:
            import capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_output

            return capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "GetSamplingOperationResult", redact_output=_redact_output
            ),
        )
        input_: capo_sagemakertrainingsessionruntime.types.get_sampling_operation_result_input.GetSamplingOperationResultInput = {
            "training_session_name": training_session_name,
            "operation_id": operation_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_training_operation_result(
        self,
        training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName",
        operation_id: "capo_sagemakertrainingsessionruntime.types.operation_id.OperationId",
        *,
        config_overrides: Optional[SageMakerTrainingSessionRuntimeClientConfig] = None,
    ) -> "capo_sagemakertrainingsessionruntime.types.get_training_operation_result_output.GetTrainingOperationResultOutput":
        """<p>Retrieves the current status and result of a previously submitted training operation. Poll this operation until the status reaches a terminal state (Completed, Failed, or Skipped).</p>

        Args:
            training_session_name: <p>The name of the training session that owns the operation.</p>
            operation_id: <p>The unique identifier of the operation to retrieve, returned by <code>ExecuteTrainingOperation</code>.</p>

        Raises:
            capo_sagemakertrainingsessionruntime.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Retry the request using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified training session or operation does not exist, or the operation does not belong to the specified training session.</p>
            capo_sagemakertrainingsessionruntime.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry the request after a brief wait using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.validation_exception.ValidationException: <p>The request is not valid. Check the request syntax and parameters. Examples include invalid sequence numbers, malformed client tokens, missing required fields, or invalid operation configuration.</p>
            capo_sagemakertrainingsessionruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get the result of a training operation
            Retrieves the status and result of a training operation submitted with ExecuteTrainingOperation.

            >>> client.get_training_operation_result(training_session_name='my-training-session', operation_id='a1b2c3d4-5678-90ab-cdef-1234567890ab')
        """

        def _handler(
            req: "OperationRequest[capo_sagemakertrainingsessionruntime.types.get_training_operation_result_input.GetTrainingOperationResultInput]",
        ) -> OperationResponse[
            "capo_sagemakertrainingsessionruntime.types.get_training_operation_result_output.GetTrainingOperationResultOutput"
        ]:
            import capo_sagemakertrainingsessionruntime._operations.lego_router_service.get_training_operation_result

            output, http_response = (
                capo_sagemakertrainingsessionruntime._operations.lego_router_service.get_training_operation_result.get_training_operation_result(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetTrainingOperationResult")
        )
        input_: capo_sagemakertrainingsessionruntime.types.get_training_operation_result_input.GetTrainingOperationResultInput = {
            "training_session_name": training_session_name,
            "operation_id": operation_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def sample_training_session(
        self,
        training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName",
        *,
        config_overrides: Optional[SageMakerTrainingSessionRuntimeClientConfig] = None,
        content_type: Optional[str] = None,
        accept: Optional[str] = None,
        model_package_arn: Optional[str] = None,
        body: Optional[
            "capo_sagemakertrainingsessionruntime.types.inference_body.InferenceBody"
        ] = None,
    ) -> "capo_sagemakertrainingsessionruntime.types.sample_training_session_output.SampleTrainingSessionOutput":
        """<p>Sends an inference request to the model associated with the specified training session and returns the response synchronously. The service passes the request and response bodies to and from the model without modification.</p>

        Args:
            training_session_name: <p>The name of the training session whose model to invoke.</p>
            content_type: <p>The MIME type of the input data in the request body.</p>
            accept: <p>The desired MIME type of the inference body in the response.</p>
            model_package_arn: <p>The ARN of the model package whose checkpoint to invoke.</p>
            body: <p>The raw inference request body.</p>

        Raises:
            capo_sagemakertrainingsessionruntime.errors.conflict_exception.ConflictException: <p>The training session is in a state that cannot accept new operations. The session must be in <code>Running</code> or <code>Blocked</code> state to accept requests.</p>
            capo_sagemakertrainingsessionruntime.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Retry the request using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified training session or operation does not exist, or the operation does not belong to the specified training session.</p>
            capo_sagemakertrainingsessionruntime.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry the request after a brief wait using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.validation_exception.ValidationException: <p>The request is not valid. Check the request syntax and parameters. Examples include invalid sequence numbers, malformed client tokens, missing required fields, or invalid operation configuration.</p>
            capo_sagemakertrainingsessionruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample from a training session
            Sends a chat completion request to the session's current weights and receives the complete response in a single payload.

            >>> client.sample_training_session(training_session_name='my-training-session', content_type='application/json', accept='application/json', body='eyJtZXNzYWdlcyI6W3sicm9sZSI6InVzZXIiLCJjb250ZW50IjoiV2hhdCBpcyB0aGUgY2FwaXRhbCBvZiBGcmFuY2U/In1dLCJtYXhfdG9rZW5zIjoxMjh9')
        """

        def _handler(
            req: "OperationRequest[capo_sagemakertrainingsessionruntime.types.sample_training_session_input.SampleTrainingSessionInput]",
        ) -> OperationResponse[
            "capo_sagemakertrainingsessionruntime.types.sample_training_session_output.SampleTrainingSessionOutput"
        ]:
            import capo_sagemakertrainingsessionruntime._operations.lego_router_service.sample_training_session

            output, http_response = (
                capo_sagemakertrainingsessionruntime._operations.lego_router_service.sample_training_session.sample_training_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemakertrainingsessionruntime.types.sample_training_session_input.SampleTrainingSessionInput",
        ) -> dict[str, Any]:
            import capo_sagemakertrainingsessionruntime.types.sample_training_session_input

            return capo_sagemakertrainingsessionruntime.types.sample_training_session_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemakertrainingsessionruntime.types.sample_training_session_output.SampleTrainingSessionOutput",
        ) -> dict[str, Any]:
            import capo_sagemakertrainingsessionruntime.types.sample_training_session_output

            return capo_sagemakertrainingsessionruntime.types.sample_training_session_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "SampleTrainingSession",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemakertrainingsessionruntime.types.sample_training_session_input.SampleTrainingSessionInput = {
            "training_session_name": training_session_name
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if model_package_arn is not None:
            input_["model_package_arn"] = model_package_arn
        if body is not None:
            input_["body"] = body

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def sample_training_session_with_response_stream(
        self,
        training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName",
        *,
        config_overrides: Optional[SageMakerTrainingSessionRuntimeClientConfig] = None,
        content_type: Optional[str] = None,
        accept: Optional[str] = None,
        model_package_arn: Optional[str] = None,
        body: Optional[
            "capo_sagemakertrainingsessionruntime.types.inference_body.InferenceBody"
        ] = None,
    ) -> "Generator[capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_output.SampleTrainingSessionWithResponseStreamOutput]":
        """<p>Streams inference responses from the model associated with the specified training session. Use this operation for real-time token-by-token generation. The service passes the request body to the model without modification.</p>

        Args:
            training_session_name: <p>The name of the training session whose model to invoke.</p>
            content_type: <p>The MIME type of the input data in the request body.</p>
            accept: <p>The desired MIME type of the inference body in the response.</p>
            model_package_arn: <p>The ARN of the model package whose checkpoint to invoke.</p>
            body: <p>The raw inference request body.</p>

        Raises:
            capo_sagemakertrainingsessionruntime.errors.conflict_exception.ConflictException: <p>The training session is in a state that cannot accept new operations. The session must be in <code>Running</code> or <code>Blocked</code> state to accept requests.</p>
            capo_sagemakertrainingsessionruntime.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred. Retry the request using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified training session or operation does not exist, or the operation does not belong to the specified training session.</p>
            capo_sagemakertrainingsessionruntime.errors.throttling_exception.ThrottlingException: <p>The request was throttled. Retry the request after a brief wait using exponential backoff.</p>
            capo_sagemakertrainingsessionruntime.errors.validation_exception.ValidationException: <p>The request is not valid. Check the request syntax and parameters. Examples include invalid sequence numbers, malformed client tokens, missing required fields, or invalid operation configuration.</p>
            capo_sagemakertrainingsessionruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Stream samples from a training session
            Sends a chat completion request to the session's current weights and receives the response as a stream of payload chunks.

            >>> client.sample_training_session_with_response_stream(training_session_name='my-training-session', content_type='application/json', accept='application/json', body='eyJtZXNzYWdlcyI6W3sicm9sZSI6InVzZXIiLCJjb250ZW50IjoiV2hhdCBpcyB0aGUgY2FwaXRhbCBvZiBGcmFuY2U/In1dLCJtYXhfdG9rZW5zIjoxMjgsInN0cmVhbSI6dHJ1ZX0=')
        """

        def _handler(
            req: "OperationRequest[capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_input.SampleTrainingSessionWithResponseStreamInput]",
        ) -> OperationResponse[
            "capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_output.SampleTrainingSessionWithResponseStreamOutput"
        ]:
            import capo_sagemakertrainingsessionruntime._operations.lego_router_service.sample_training_session_with_response_stream

            output, http_response = (
                capo_sagemakertrainingsessionruntime._operations.lego_router_service.sample_training_session_with_response_stream.sample_training_session_with_response_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_input.SampleTrainingSessionWithResponseStreamInput",
        ) -> dict[str, Any]:
            import capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_input

            return capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_output.SampleTrainingSessionWithResponseStreamOutput",
        ) -> dict[str, Any]:
            import capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_output

            return capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "SampleTrainingSessionWithResponseStream",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemakertrainingsessionruntime.types.sample_training_session_with_response_stream_input.SampleTrainingSessionWithResponseStreamInput = {
            "training_session_name": training_session_name
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if model_package_arn is not None:
            input_["model_package_arn"] = model_package_arn
        if body is not None:
            input_["body"] = body

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
