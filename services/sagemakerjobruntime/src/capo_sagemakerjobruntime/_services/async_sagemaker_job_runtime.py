"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#AgenticRFTRuntimeService``."""

import uuid
import warnings
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sagemakerjobruntime._auth._signers
import capo_sagemakerjobruntime._auth._sigv4
from capo_sagemakerjobruntime._auth._identity import Credentials
from capo_sagemakerjobruntime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemakerjobruntime._auth._zapros_handler import AuthMiddleware
from capo_sagemakerjobruntime._services._aws_config import aaws_config
from capo_sagemakerjobruntime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_sagemakerjobruntime.types.complete_rollout_request
    import capo_sagemakerjobruntime.types.complete_rollout_response
    import capo_sagemakerjobruntime.types.completion_status
    import capo_sagemakerjobruntime.types.double_list
    import capo_sagemakerjobruntime.types.inference_request_body
    import capo_sagemakerjobruntime.types.job_arn
    import capo_sagemakerjobruntime.types.sample_request
    import capo_sagemakerjobruntime.types.sample_response
    import capo_sagemakerjobruntime.types.sample_with_response_stream_request
    import capo_sagemakerjobruntime.types.sample_with_response_stream_response
    import capo_sagemakerjobruntime.types.trajectory_id
    import capo_sagemakerjobruntime.types.update_reward_request
    import capo_sagemakerjobruntime.types.update_reward_response


class AsyncSagemakerJobRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSagemakerJobRuntimeClient:
    """A client for the ``SagemakerJobRuntime`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
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
        self._config = AsyncSagemakerJobRuntimeClientConfig(
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
        self, config_overrides: Optional[AsyncSagemakerJobRuntimeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSagemakerJobRuntimeClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def complete_rollout(
        self,
        job_arn: "capo_sagemakerjobruntime.types.job_arn.JobArn",
        trajectory_id: "capo_sagemakerjobruntime.types.trajectory_id.TrajectoryId",
        *,
        config_overrides: Optional[AsyncSagemakerJobRuntimeClientConfig] = None,
        status: Optional[
            "capo_sagemakerjobruntime.types.completion_status.CompletionStatus"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_sagemakerjobruntime.types.complete_rollout_response.CompleteRolloutResponse":
        """Marks a rollout as complete, indicating that no further turns will be appended to the trajectory. After calling this operation, the trajectory is sealed and eligible for reward submission via the UpdateReward operation.

        Args:
            job_arn: The job ARN.
            trajectory_id: The trajectory ID to mark as complete.
            status: The target status for the trajectory. Defaults to READY if not specified. Set to FAILED if the rollout encountered an error and the trajectory should not be used for processing.
            client_token: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        Raises:
            capo_sagemakerjobruntime.errors.access_denied_exception.AccessDeniedException: You do not have permission to perform this operation.
            capo_sagemakerjobruntime.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_sagemakerjobruntime.errors.internal_service_error.InternalServiceError: An internal service error occurred. Retry the request.
            capo_sagemakerjobruntime.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_sagemakerjobruntime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You have exceeded a service quota.
            capo_sagemakerjobruntime.errors.throttling_exception.ThrottlingException: The request was throttled. Retry the request after a brief wait.
            capo_sagemakerjobruntime.errors.validation_exception.ValidationException: The request is not valid. Check the request syntax and parameters
            capo_sagemakerjobruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke CompleteRollout
            Marks a rollout as complete so the trajectory is sealed and eligible for reward submission.

            >>> await client.complete_rollout(job_arn='arn:aws:sagemaker:us-east-1:123456789012:job/AgentRFT/my-training-job', trajectory_id='trajectory-001', status='ready')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemakerjobruntime.types.complete_rollout_request.CompleteRolloutRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemakerjobruntime.types.complete_rollout_response.CompleteRolloutResponse"
        ]:
            import capo_sagemakerjobruntime._operations.agentic_rft_runtime_service.complete_rollout

            (
                output,
                http_response,
            ) = await capo_sagemakerjobruntime._operations.agentic_rft_runtime_service.complete_rollout.async_complete_rollout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemakerjobruntime.types.complete_rollout_request.CompleteRolloutRequest = {
            "job_arn": job_arn,
            "trajectory_id": trajectory_id,
        }
        if status is not None:
            input_["status"] = status
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def sample(
        self,
        job_arn: "capo_sagemakerjobruntime.types.job_arn.JobArn",
        trajectory_id: "capo_sagemakerjobruntime.types.trajectory_id.TrajectoryId",
        body: "capo_sagemakerjobruntime.types.inference_request_body.InferenceRequestBody",
        *,
        config_overrides: Optional[AsyncSagemakerJobRuntimeClientConfig] = None,
    ) -> "capo_sagemakerjobruntime.types.sample_response.SampleResponse":
        """Sends an inference request to the model during a job execution. The request and response bodies are forwarded to and from the model without modification. Each turn (prompt and response) is captured for later use.

        Args:
            job_arn: The job ARN that identifies which model session to route the inference request to.
            trajectory_id: The trajectory ID for grouping turns into a single rollout. Each turn (prompt and response) is captured for later use.
            body: The raw inference request body in OpenAI-compatible JSON format.

        Raises:
            capo_sagemakerjobruntime.errors.access_denied_exception.AccessDeniedException: You do not have permission to perform this operation.
            capo_sagemakerjobruntime.errors.internal_service_error.InternalServiceError: An internal service error occurred. Retry the request.
            capo_sagemakerjobruntime.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_sagemakerjobruntime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You have exceeded a service quota.
            capo_sagemakerjobruntime.errors.throttling_exception.ThrottlingException: The request was throttled. Retry the request after a brief wait.
            capo_sagemakerjobruntime.errors.validation_exception.ValidationException: The request is not valid. Check the request syntax and parameters
            capo_sagemakerjobruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke Sample
            Sends an inference request to the model and receives the response.

            >>> await client.sample(job_arn='arn:aws:sagemaker:us-east-1:123456789012:job/AgentRFT/my-training-job', trajectory_id='trajectory-001', body='eyJtb2RlbCI6Im15LW1vZGVsIiwibWVzc2FnZXMiOlt7InJvbGUiOiJ1c2VyIiwiY29udGVudCI6IkhlbGxvIn1dfQ==')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemakerjobruntime.types.sample_request.SampleRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemakerjobruntime.types.sample_response.SampleResponse"
        ]:
            import capo_sagemakerjobruntime._operations.agentic_rft_runtime_service.sample

            (
                output,
                http_response,
            ) = await capo_sagemakerjobruntime._operations.agentic_rft_runtime_service.sample.async_sample(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemakerjobruntime.types.sample_request.SampleRequest = {
            "job_arn": job_arn,
            "trajectory_id": trajectory_id,
            "body": body,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def sample_with_response_stream(
        self,
        job_arn: "capo_sagemakerjobruntime.types.job_arn.JobArn",
        trajectory_id: "capo_sagemakerjobruntime.types.trajectory_id.TrajectoryId",
        body: "capo_sagemakerjobruntime.types.inference_request_body.InferenceRequestBody",
        *,
        config_overrides: Optional[AsyncSagemakerJobRuntimeClientConfig] = None,
    ) -> "AsyncGenerator[capo_sagemakerjobruntime.types.sample_with_response_stream_response.SampleWithResponseStreamResponse]":
        """Sends a streaming inference request to the model during a job execution. Returns the response as a stream of payload chunks. Each turn is captured for later use.

        Args:
            job_arn: The job ARN that identifies which model session to route the inference request to.
            trajectory_id: The trajectory ID for grouping turns into a single rollout. Each turn is captured for later use.
            body: The raw inference request body in OpenAI-compatible JSON format.

        Raises:
            capo_sagemakerjobruntime.errors.access_denied_exception.AccessDeniedException: You do not have permission to perform this operation.
            capo_sagemakerjobruntime.errors.internal_service_error.InternalServiceError: An internal service error occurred. Retry the request.
            capo_sagemakerjobruntime.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_sagemakerjobruntime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You have exceeded a service quota.
            capo_sagemakerjobruntime.errors.throttling_exception.ThrottlingException: The request was throttled. Retry the request after a brief wait.
            capo_sagemakerjobruntime.errors.validation_exception.ValidationException: The request is not valid. Check the request syntax and parameters
            capo_sagemakerjobruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke SampleWithResponseStream
            Sends a streaming inference request and receives the response as a stream of payload chunks.

            >>> await client.sample_with_response_stream(job_arn='arn:aws:sagemaker:us-east-1:123456789012:job/AgentRFT/my-training-job', trajectory_id='trajectory-001', body='eyJtb2RlbCI6Im15LW1vZGVsIiwibWVzc2FnZXMiOlt7InJvbGUiOiJ1c2VyIiwiY29udGVudCI6IkhlbGxvIn1dfQ==')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemakerjobruntime.types.sample_with_response_stream_request.SampleWithResponseStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemakerjobruntime.types.sample_with_response_stream_response.SampleWithResponseStreamResponse"
        ]:
            import capo_sagemakerjobruntime._operations.agentic_rft_runtime_service.sample_with_response_stream

            (
                output,
                http_response,
            ) = await capo_sagemakerjobruntime._operations.agentic_rft_runtime_service.sample_with_response_stream.async_sample_with_response_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemakerjobruntime.types.sample_with_response_stream_request.SampleWithResponseStreamRequest = {
            "job_arn": job_arn,
            "trajectory_id": trajectory_id,
            "body": body,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def update_reward(
        self,
        job_arn: "capo_sagemakerjobruntime.types.job_arn.JobArn",
        trajectory_id: "capo_sagemakerjobruntime.types.trajectory_id.TrajectoryId",
        rewards: "capo_sagemakerjobruntime.types.double_list.DoubleList",
        *,
        config_overrides: Optional[AsyncSagemakerJobRuntimeClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_sagemakerjobruntime.types.update_reward_response.UpdateRewardResponse":
        """Updates the reward values for a trajectory and transitions it to reward-received status, signaling that it is eligible for processing. Call this operation after CompleteRollout to provide the computed reward scores.

        Args:
            job_arn: The job ARN.
            trajectory_id: The trajectory ID to update with reward values.
            rewards: The list of reward values to assign to this trajectory. Provide one reward value per turn in the trajectory.
            client_token: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        Raises:
            capo_sagemakerjobruntime.errors.access_denied_exception.AccessDeniedException: You do not have permission to perform this operation.
            capo_sagemakerjobruntime.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_sagemakerjobruntime.errors.internal_service_error.InternalServiceError: An internal service error occurred. Retry the request.
            capo_sagemakerjobruntime.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found.
            capo_sagemakerjobruntime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: You have exceeded a service quota.
            capo_sagemakerjobruntime.errors.throttling_exception.ThrottlingException: The request was throttled. Retry the request after a brief wait.
            capo_sagemakerjobruntime.errors.validation_exception.ValidationException: The request is not valid. Check the request syntax and parameters
            capo_sagemakerjobruntime.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke UpdateReward
            Updates the reward values for a completed trajectory.

            >>> await client.update_reward(job_arn='arn:aws:sagemaker:us-east-1:123456789012:job/AgentRFT/my-training-job', trajectory_id='trajectory-001', rewards=[0.85, 0.92, 0.78])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemakerjobruntime.types.update_reward_request.UpdateRewardRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemakerjobruntime.types.update_reward_response.UpdateRewardResponse"
        ]:
            import capo_sagemakerjobruntime._operations.agentic_rft_runtime_service.update_reward

            (
                output,
                http_response,
            ) = await capo_sagemakerjobruntime._operations.agentic_rft_runtime_service.update_reward.async_update_reward(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemakerjobruntime.types.update_reward_request.UpdateRewardRequest = {
            "job_arn": job_arn,
            "trajectory_id": trajectory_id,
            "rewards": rewards,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

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
