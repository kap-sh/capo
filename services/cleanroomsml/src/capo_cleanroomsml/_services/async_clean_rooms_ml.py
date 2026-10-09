"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AWSStarkControlService``."""

import datetime
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_cleanroomsml._auth._signers
import capo_cleanroomsml._auth._sigv4
from capo_cleanroomsml._auth._identity import Credentials
from capo_cleanroomsml._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cleanroomsml._auth._zapros_handler import AuthMiddleware
from capo_cleanroomsml._pagination import resolve_path as _resolve_path
from capo_cleanroomsml._resources.aws_stark_control_service.audience_export_job import (
    AsyncAudienceExportJob,
)
from capo_cleanroomsml._resources.aws_stark_control_service.audience_generation_job import (
    AsyncAudienceGenerationJob,
)
from capo_cleanroomsml._resources.aws_stark_control_service.audience_model import (
    AsyncAudienceModel,
)
from capo_cleanroomsml._resources.aws_stark_control_service.configured_audience_model import (
    AsyncConfiguredAudienceModel,
)
from capo_cleanroomsml._resources.aws_stark_control_service.configured_audience_model_policy import (
    AsyncConfiguredAudienceModelPolicy,
)
from capo_cleanroomsml._resources.aws_stark_control_service.configured_model_algorithm import (
    AsyncConfiguredModelAlgorithm,
)
from capo_cleanroomsml._resources.aws_stark_control_service.configured_model_algorithm_association import (
    AsyncConfiguredModelAlgorithmAssociation,
)
from capo_cleanroomsml._resources.aws_stark_control_service.ml_configuration import (
    AsyncMLConfiguration,
)
from capo_cleanroomsml._resources.aws_stark_control_service.ml_input_channel import (
    AsyncMLInputChannel,
)
from capo_cleanroomsml._resources.aws_stark_control_service.trained_model import (
    AsyncTrainedModel,
)
from capo_cleanroomsml._resources.aws_stark_control_service.trained_model_export_job import (
    AsyncTrainedModelExportJob,
)
from capo_cleanroomsml._resources.aws_stark_control_service.trained_model_inference_job import (
    AsyncTrainedModelInferenceJob,
)
from capo_cleanroomsml._resources.aws_stark_control_service.training_dataset import (
    AsyncTrainingDataset,
)
from capo_cleanroomsml._services._aws_config import aaws_config
from capo_cleanroomsml._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.audience_export_job_summary
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.audience_generation_job_data_source
    import capo_cleanroomsml.types.audience_generation_job_summary
    import capo_cleanroomsml.types.audience_model_arn
    import capo_cleanroomsml.types.audience_model_summary
    import capo_cleanroomsml.types.audience_size
    import capo_cleanroomsml.types.audience_size_config
    import capo_cleanroomsml.types.cancel_trained_model_inference_job_request
    import capo_cleanroomsml.types.cancel_trained_model_request
    import capo_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary
    import capo_cleanroomsml.types.collaboration_ml_input_channel_summary
    import capo_cleanroomsml.types.collaboration_trained_model_export_job_summary
    import capo_cleanroomsml.types.collaboration_trained_model_inference_job_summary
    import capo_cleanroomsml.types.collaboration_trained_model_summary
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.configured_audience_model_output_config
    import capo_cleanroomsml.types.configured_audience_model_summary
    import capo_cleanroomsml.types.configured_model_algorithm_arn
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import capo_cleanroomsml.types.configured_model_algorithm_association_summary
    import capo_cleanroomsml.types.configured_model_algorithm_summary
    import capo_cleanroomsml.types.container_config
    import capo_cleanroomsml.types.create_audience_model_request
    import capo_cleanroomsml.types.create_audience_model_response
    import capo_cleanroomsml.types.create_configured_audience_model_request
    import capo_cleanroomsml.types.create_configured_audience_model_response
    import capo_cleanroomsml.types.create_configured_model_algorithm_association_request
    import capo_cleanroomsml.types.create_configured_model_algorithm_association_response
    import capo_cleanroomsml.types.create_configured_model_algorithm_request
    import capo_cleanroomsml.types.create_configured_model_algorithm_response
    import capo_cleanroomsml.types.create_ml_input_channel_request
    import capo_cleanroomsml.types.create_ml_input_channel_response
    import capo_cleanroomsml.types.create_trained_model_request
    import capo_cleanroomsml.types.create_trained_model_response
    import capo_cleanroomsml.types.create_training_dataset_request
    import capo_cleanroomsml.types.create_training_dataset_response
    import capo_cleanroomsml.types.dataset_list
    import capo_cleanroomsml.types.delete_audience_generation_job_request
    import capo_cleanroomsml.types.delete_audience_model_request
    import capo_cleanroomsml.types.delete_configured_audience_model_policy_request
    import capo_cleanroomsml.types.delete_configured_audience_model_request
    import capo_cleanroomsml.types.delete_configured_model_algorithm_association_request
    import capo_cleanroomsml.types.delete_configured_model_algorithm_request
    import capo_cleanroomsml.types.delete_ml_configuration_request
    import capo_cleanroomsml.types.delete_ml_input_channel_data_request
    import capo_cleanroomsml.types.delete_trained_model_output_request
    import capo_cleanroomsml.types.delete_training_dataset_request
    import capo_cleanroomsml.types.environment
    import capo_cleanroomsml.types.get_audience_generation_job_request
    import capo_cleanroomsml.types.get_audience_generation_job_response
    import capo_cleanroomsml.types.get_audience_model_request
    import capo_cleanroomsml.types.get_audience_model_response
    import capo_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_request
    import capo_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_response
    import capo_cleanroomsml.types.get_collaboration_ml_input_channel_request
    import capo_cleanroomsml.types.get_collaboration_ml_input_channel_response
    import capo_cleanroomsml.types.get_collaboration_trained_model_request
    import capo_cleanroomsml.types.get_collaboration_trained_model_response
    import capo_cleanroomsml.types.get_configured_audience_model_policy_request
    import capo_cleanroomsml.types.get_configured_audience_model_policy_response
    import capo_cleanroomsml.types.get_configured_audience_model_request
    import capo_cleanroomsml.types.get_configured_audience_model_response
    import capo_cleanroomsml.types.get_configured_model_algorithm_association_request
    import capo_cleanroomsml.types.get_configured_model_algorithm_association_response
    import capo_cleanroomsml.types.get_configured_model_algorithm_request
    import capo_cleanroomsml.types.get_configured_model_algorithm_response
    import capo_cleanroomsml.types.get_ml_configuration_request
    import capo_cleanroomsml.types.get_ml_configuration_response
    import capo_cleanroomsml.types.get_ml_input_channel_request
    import capo_cleanroomsml.types.get_ml_input_channel_response
    import capo_cleanroomsml.types.get_trained_model_inference_job_request
    import capo_cleanroomsml.types.get_trained_model_inference_job_response
    import capo_cleanroomsml.types.get_trained_model_request
    import capo_cleanroomsml.types.get_trained_model_response
    import capo_cleanroomsml.types.get_training_dataset_request
    import capo_cleanroomsml.types.get_training_dataset_response
    import capo_cleanroomsml.types.hash
    import capo_cleanroomsml.types.hyper_parameters
    import capo_cleanroomsml.types.iam_role_arn
    import capo_cleanroomsml.types.incremental_training_data_channels
    import capo_cleanroomsml.types.inference_container_config
    import capo_cleanroomsml.types.inference_container_execution_parameters
    import capo_cleanroomsml.types.inference_environment_map
    import capo_cleanroomsml.types.inference_output_configuration
    import capo_cleanroomsml.types.inference_resource_config
    import capo_cleanroomsml.types.input_channel
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.list_audience_export_jobs_request
    import capo_cleanroomsml.types.list_audience_export_jobs_response
    import capo_cleanroomsml.types.list_audience_generation_jobs_request
    import capo_cleanroomsml.types.list_audience_generation_jobs_response
    import capo_cleanroomsml.types.list_audience_models_request
    import capo_cleanroomsml.types.list_audience_models_response
    import capo_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_request
    import capo_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_response
    import capo_cleanroomsml.types.list_collaboration_ml_input_channels_request
    import capo_cleanroomsml.types.list_collaboration_ml_input_channels_response
    import capo_cleanroomsml.types.list_collaboration_trained_model_export_jobs_request
    import capo_cleanroomsml.types.list_collaboration_trained_model_export_jobs_response
    import capo_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_request
    import capo_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_response
    import capo_cleanroomsml.types.list_collaboration_trained_models_request
    import capo_cleanroomsml.types.list_collaboration_trained_models_response
    import capo_cleanroomsml.types.list_configured_audience_models_request
    import capo_cleanroomsml.types.list_configured_audience_models_response
    import capo_cleanroomsml.types.list_configured_model_algorithm_associations_request
    import capo_cleanroomsml.types.list_configured_model_algorithm_associations_response
    import capo_cleanroomsml.types.list_configured_model_algorithms_request
    import capo_cleanroomsml.types.list_configured_model_algorithms_response
    import capo_cleanroomsml.types.list_ml_input_channels_request
    import capo_cleanroomsml.types.list_ml_input_channels_response
    import capo_cleanroomsml.types.list_tags_for_resource_request
    import capo_cleanroomsml.types.list_tags_for_resource_response
    import capo_cleanroomsml.types.list_trained_model_inference_jobs_request
    import capo_cleanroomsml.types.list_trained_model_inference_jobs_response
    import capo_cleanroomsml.types.list_trained_model_versions_request
    import capo_cleanroomsml.types.list_trained_model_versions_response
    import capo_cleanroomsml.types.list_trained_models_request
    import capo_cleanroomsml.types.list_trained_models_response
    import capo_cleanroomsml.types.list_training_datasets_request
    import capo_cleanroomsml.types.list_training_datasets_response
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.metrics_list
    import capo_cleanroomsml.types.min_matching_seed_size
    import capo_cleanroomsml.types.ml_input_channel_arn
    import capo_cleanroomsml.types.ml_input_channel_summary
    import capo_cleanroomsml.types.ml_output_configuration
    import capo_cleanroomsml.types.model_inference_data_source
    import capo_cleanroomsml.types.model_training_data_channels
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.payer_configuration
    import capo_cleanroomsml.types.policy_existence_condition
    import capo_cleanroomsml.types.privacy_configuration
    import capo_cleanroomsml.types.put_configured_audience_model_policy_request
    import capo_cleanroomsml.types.put_configured_audience_model_policy_response
    import capo_cleanroomsml.types.put_ml_configuration_request
    import capo_cleanroomsml.types.resource_config
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.resource_policy
    import capo_cleanroomsml.types.start_audience_export_job_request
    import capo_cleanroomsml.types.start_audience_generation_job_request
    import capo_cleanroomsml.types.start_audience_generation_job_response
    import capo_cleanroomsml.types.start_trained_model_export_job_request
    import capo_cleanroomsml.types.start_trained_model_inference_job_request
    import capo_cleanroomsml.types.start_trained_model_inference_job_response
    import capo_cleanroomsml.types.stopping_condition
    import capo_cleanroomsml.types.tag_keys
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.tag_on_create_policy
    import capo_cleanroomsml.types.tag_resource_request
    import capo_cleanroomsml.types.tag_resource_response
    import capo_cleanroomsml.types.taggable_arn
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_export_output_configuration
    import capo_cleanroomsml.types.trained_model_inference_job_arn
    import capo_cleanroomsml.types.trained_model_inference_job_summary
    import capo_cleanroomsml.types.trained_model_status
    import capo_cleanroomsml.types.trained_model_summary
    import capo_cleanroomsml.types.training_dataset_arn
    import capo_cleanroomsml.types.training_dataset_summary
    import capo_cleanroomsml.types.training_input_mode
    import capo_cleanroomsml.types.untag_resource_request
    import capo_cleanroomsml.types.untag_resource_response
    import capo_cleanroomsml.types.update_configured_audience_model_request
    import capo_cleanroomsml.types.update_configured_audience_model_response
    import capo_cleanroomsml.types.uuid


class AsyncCleanRoomsMLClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCleanRoomsMLClient:
    """A client for the ``CleanRoomsML`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = AsyncCleanRoomsMLClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.audience_export_job = AsyncAudienceExportJob(self)
        self.audience_generation_job = AsyncAudienceGenerationJob(self)
        self.audience_model = AsyncAudienceModel(self)
        self.configured_audience_model = AsyncConfiguredAudienceModel(self)
        self.configured_audience_model_policy = AsyncConfiguredAudienceModelPolicy(self)
        self.configured_model_algorithm = AsyncConfiguredModelAlgorithm(self)
        self.configured_model_algorithm_association = (
            AsyncConfiguredModelAlgorithmAssociation(self)
        )
        self.ml_configuration = AsyncMLConfiguration(self)
        self.ml_input_channel = AsyncMLInputChannel(self)
        self.trained_model = AsyncTrainedModel(self)
        self.trained_model_export_job = AsyncTrainedModelExportJob(self)
        self.trained_model_inference_job = AsyncTrainedModelInferenceJob(self)
        self.training_dataset = AsyncTrainingDataset(self)

    def operation_options(
        self, config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCleanRoomsMLClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_collaboration_configured_model_algorithm_associations(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_response.ListCollaborationConfiguredModelAlgorithmAssociationsResponse":
        """<p>Returns a list of the configured model algorithm associations in a collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the configured model algorithm associations that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_request.ListCollaborationConfiguredModelAlgorithmAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_response.ListCollaborationConfiguredModelAlgorithmAssociationsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_configured_model_algorithm_associations

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_configured_model_algorithm_associations.async_list_collaboration_configured_model_algorithm_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_collaboration_configured_model_algorithm_associations_request.ListCollaborationConfiguredModelAlgorithmAssociationsRequest = {
            "collaboration_identifier": collaboration_identifier
        }
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

    async def iter_list_collaboration_configured_model_algorithm_associations(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary.CollaborationConfiguredModelAlgorithmAssociationSummary]":
        _token = next_token
        while True:
            _response = (
                await self.list_collaboration_configured_model_algorithm_associations(
                    collaboration_identifier,
                    config_overrides=config_overrides,
                    next_token=_token,
                    max_results=max_results,
                )
            )
            _page = _resolve_path(
                _response, ("collaboration_configured_model_algorithm_associations",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_ml_input_channels(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_collaboration_ml_input_channels_response.ListCollaborationMLInputChannelsResponse":
        """<p>Returns a list of the ML input channels in a collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of results to return.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the ML input channels that you want to list.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_collaboration_ml_input_channels_request.ListCollaborationMLInputChannelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_collaboration_ml_input_channels_response.ListCollaborationMLInputChannelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_ml_input_channels

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_ml_input_channels.async_list_collaboration_ml_input_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_collaboration_ml_input_channels_request.ListCollaborationMLInputChannelsRequest = {
            "collaboration_identifier": collaboration_identifier
        }
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

    async def iter_list_collaboration_ml_input_channels(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.collaboration_ml_input_channel_summary.CollaborationMLInputChannelSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_ml_input_channels(
                collaboration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("collaboration_ml_input_channels_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_trained_model_export_jobs(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "capo_cleanroomsml.types.list_collaboration_trained_model_export_jobs_response.ListCollaborationTrainedModelExportJobsResponse":
        """<p>Returns a list of the export jobs for a trained model in a collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the trained model export jobs that you are interested in.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that was used to create the export jobs that you are interested in.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to filter export jobs by. When specified, only export jobs for this specific version of the trained model are returned.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_collaboration_trained_model_export_jobs_request.ListCollaborationTrainedModelExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_collaboration_trained_model_export_jobs_response.ListCollaborationTrainedModelExportJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_model_export_jobs

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_model_export_jobs.async_list_collaboration_trained_model_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_collaboration_trained_model_export_jobs_request.ListCollaborationTrainedModelExportJobsRequest = {
            "collaboration_identifier": collaboration_identifier,
            "trained_model_arn": trained_model_arn,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_collaboration_trained_model_export_jobs(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.collaboration_trained_model_export_job_summary.CollaborationTrainedModelExportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_trained_model_export_jobs(
                collaboration_identifier,
                trained_model_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                trained_model_version_identifier=trained_model_version_identifier,
            )
            _page = _resolve_path(
                _response, ("collaboration_trained_model_export_jobs",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_trained_model_inference_jobs(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        trained_model_arn: Optional[
            "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
        ] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "capo_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_response.ListCollaborationTrainedModelInferenceJobsResponse":
        """<p>Returns a list of trained model inference jobs in a specified collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the trained model inference jobs that you are interested in.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that was used to create the trained model inference jobs that you are interested in.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to filter inference jobs by. When specified, only inference jobs that used this specific version of the trained model are returned.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_request.ListCollaborationTrainedModelInferenceJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_response.ListCollaborationTrainedModelInferenceJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_model_inference_jobs

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_model_inference_jobs.async_list_collaboration_trained_model_inference_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_collaboration_trained_model_inference_jobs_request.ListCollaborationTrainedModelInferenceJobsRequest = {
            "collaboration_identifier": collaboration_identifier
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if trained_model_arn is not None:
            input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_collaboration_trained_model_inference_jobs(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        trained_model_arn: Optional[
            "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
        ] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.collaboration_trained_model_inference_job_summary.CollaborationTrainedModelInferenceJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_trained_model_inference_jobs(
                collaboration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                trained_model_arn=trained_model_arn,
                trained_model_version_identifier=trained_model_version_identifier,
            )
            _page = _resolve_path(
                _response, ("collaboration_trained_model_inference_jobs",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collaboration_trained_models(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_collaboration_trained_models_response.ListCollaborationTrainedModelsResponse":
        """<p>Returns a list of the trained models in a collaboration.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the trained models you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_collaboration_trained_models_request.ListCollaborationTrainedModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_collaboration_trained_models_response.ListCollaborationTrainedModelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_models

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_collaboration_trained_models.async_list_collaboration_trained_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_collaboration_trained_models_request.ListCollaborationTrainedModelsRequest = {
            "collaboration_identifier": collaboration_identifier
        }
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

    async def iter_list_collaboration_trained_models(
        self,
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.collaboration_trained_model_summary.CollaborationTrainedModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_collaboration_trained_models(
                collaboration_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("collaboration_trained_models",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_cleanroomsml.types.taggable_arn.TaggableArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a provided resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_cleanroomsml.types.taggable_arn.TaggableArn",
        tags: "capo_cleanroomsml.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.tag_resource_response.TagResourceResponse":
        """<p>Adds metadata tags to a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to assign tags.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_cleanroomsml.types.taggable_arn.TaggableArn",
        tag_keys: "capo_cleanroomsml.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes metadata tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p>
            tag_keys: <p>The key values of tags that you want to remove.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_audience_export_job(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        audience_size: "capo_cleanroomsml.types.audience_size.AudienceSize",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Export an audience of a specified size after you have generated an audience.</p>

        Args:
            name: <p>The name of the audience export job.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to export.</p>
            description: <p>The description of the audience export job.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job.async_start_audience_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest = {
            "name": name,
            "audience_generation_job_arn": audience_generation_job_arn,
            "audience_size": audience_size,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_audience_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        audience_generation_job_arn: Optional[
            "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
        ] = None,
    ) -> "capo_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse":
        """<p>Returns a list of the audience export jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs.async_list_audience_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if audience_generation_job_arn is not None:
            input_["audience_generation_job_arn"] = audience_generation_job_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_audience_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        audience_generation_job_arn: Optional[
            "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
        ] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.audience_export_job_summary.AudienceExportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_audience_export_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                audience_generation_job_arn=audience_generation_job_arn,
            )
            _page = _resolve_path(_response, ("audience_export_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_audience_generation_job(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        seed_audience: "capo_cleanroomsml.types.audience_generation_job_data_source.AudienceGenerationJobDataSource",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        include_seed_in_output: Optional[bool] = None,
        collaboration_id: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse":
        """<p>Information necessary to start the audience generation job.</p>

        Args:
            name: <p>The name of the audience generation job.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that is used for this audience generation job.</p>
            seed_audience: <p>The seed audience that is used to generate the audience.</p>
            include_seed_in_output: <p>Whether the seed audience is included in the audience generation output.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation job.</p>
            description: <p>The description of the audience generation job.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job.async_start_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest = {
            "name": name,
            "configured_audience_model_arn": configured_audience_model_arn,
            "seed_audience": seed_audience,
        }
        if include_seed_in_output is not None:
            input_["include_seed_in_output"] = include_seed_in_output
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_audience_generation_job(
        self,
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse":
        """<p>Returns information about an audience generation job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job.async_get_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest = {
            "audience_generation_job_arn": audience_generation_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_audience_generation_job(
        self,
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified audience generation job, and removes all data associated with the job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job.async_delete_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest = {
            "audience_generation_job_arn": audience_generation_job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_audience_generation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        configured_audience_model_arn: Optional[
            "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
        ] = None,
        collaboration_id: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
    ) -> "capo_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse":
        """<p>Returns a list of audience generation jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that was used for the audience generation jobs that you are interested in.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation jobs that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs.async_list_audience_generation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if configured_audience_model_arn is not None:
            input_["configured_audience_model_arn"] = configured_audience_model_arn
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_audience_generation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        configured_audience_model_arn: Optional[
            "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
        ] = None,
        collaboration_id: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.audience_generation_job_summary.AudienceGenerationJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_audience_generation_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                configured_audience_model_arn=configured_audience_model_arn,
                collaboration_id=collaboration_id,
            )
            _page = _resolve_path(_response, ("audience_generation_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_audience_model(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        training_dataset_arn: "capo_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        training_data_start_time: Optional[datetime.datetime] = None,
        training_data_end_time: Optional[datetime.datetime] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse":
        """<p>Defines the information necessary to create an audience model. An audience model is a machine learning model that Clean Rooms ML trains to measure similarity between users. Clean Rooms ML manages training and storing the audience model. The audience model can be used in multiple calls to the <a>StartAudienceGenerationJob</a> API.</p>

        Args:
            training_data_start_time: <p>The start date and time of the training window.</p>
            training_data_end_time: <p>The end date and time of the training window.</p>
            name: <p>The name of the audience model resource.</p>
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset for this audience model.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            description: <p>The description of the audience model.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_audience_model.async_create_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest = {
            "name": name,
            "training_dataset_arn": training_dataset_arn,
        }
        if training_data_start_time is not None:
            input_["training_data_start_time"] = training_data_start_time
        if training_data_end_time is not None:
            input_["training_data_end_time"] = training_data_end_time
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_audience_model(
        self,
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse":
        """<p>Returns information about an audience model</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_audience_model.async_get_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest = {
            "audience_model_arn": audience_model_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_audience_model(
        self,
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Specifies an audience model that you want to delete. You can't delete an audience model if there are any configured audience models that depend on the audience model.</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_model.async_delete_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest = {
            "audience_model_arn": audience_model_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_audience_models(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse":
        """<p>Returns a list of audience models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_models

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_audience_models.async_list_audience_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest = {}
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

    async def iter_list_audience_models(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.audience_model_summary.AudienceModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_audience_models(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("audience_models",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_configured_audience_model(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        output_config: "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig",
        shared_audience_metrics: "capo_cleanroomsml.types.metrics_list.MetricsList",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        min_matching_seed_size: Optional[
            "capo_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
        ] = None,
        audience_size_config: Optional[
            "capo_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        child_resource_tag_on_create_policy: Optional[
            "capo_cleanroomsml.types.tag_on_create_policy.TagOnCreatePolicy"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_configured_audience_model_response.CreateConfiguredAudienceModelResponse":
        """<p>Defines the information necessary to create a configured audience model.</p>

        Args:
            name: <p>The name of the configured audience model.</p>
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model to use for the configured audience model.</p>
            output_config: <p>Configure the Amazon S3 location and IAM Role for audiences created using this configured audience model. Each audience will have a unique location. The IAM Role must have <code>s3:PutObject</code> permission on the destination Amazon S3 location. If the destination is protected with Amazon S3 KMS-SSE, then the Role must also have the required KMS permissions.</p>
            description: <p>The description of the configured audience model.</p>
            shared_audience_metrics: <p>Whether audience metrics are shared.</p>
            min_matching_seed_size: <p>The minimum number of users from the seed audience that must match with users in the training data of the audience model. The default value is 500.</p>
            audience_size_config: <p>Configure the list of output sizes of audiences that can be created using this configured audience model. A request to <a>StartAudienceGenerationJob</a> that uses this configured audience model must have an <code>audienceSize</code> selected from this list. You can use the <code>ABSOLUTE</code> <a>AudienceSize</a> to configure out audience sizes using the count of identifiers in the output. You can use the <code>Percentage</code> <a>AudienceSize</a> to configure sizes in the range 1-100 percent.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            child_resource_tag_on_create_policy: <p>Configure how the service tags audience generation jobs created using this configured audience model. If you specify <code>NONE</code>, the tags from the <a>StartAudienceGenerationJob</a> request determine the tags of the audience generation job. If you specify <code>FROM_PARENT_RESOURCE</code>, the audience generation job inherits the tags from the configured audience model, by default. Tags in the <a>StartAudienceGenerationJob</a> will override the default.</p> <p>When the client is in a different account than the configured audience model, the tags from the client are never applied to a resource in the caller's account.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_configured_audience_model_request.CreateConfiguredAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_configured_audience_model_response.CreateConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_configured_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_configured_audience_model.async_create_configured_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.create_configured_audience_model_request.CreateConfiguredAudienceModelRequest = {
            "name": name,
            "audience_model_arn": audience_model_arn,
            "output_config": output_config,
            "shared_audience_metrics": shared_audience_metrics,
        }
        if description is not None:
            input_["description"] = description
        if min_matching_seed_size is not None:
            input_["min_matching_seed_size"] = min_matching_seed_size
        if audience_size_config is not None:
            input_["audience_size_config"] = audience_size_config
        if tags is not None:
            input_["tags"] = tags
        if child_resource_tag_on_create_policy is not None:
            input_["child_resource_tag_on_create_policy"] = (
                child_resource_tag_on_create_policy
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_audience_model(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_audience_model_response.GetConfiguredAudienceModelResponse":
        """<p>Returns information about a specified configured audience model.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_configured_audience_model_request.GetConfiguredAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_configured_audience_model_response.GetConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model.async_get_configured_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_configured_audience_model_request.GetConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configured_audience_model(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        output_config: Optional[
            "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig"
        ] = None,
        audience_model_arn: Optional[
            "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn"
        ] = None,
        shared_audience_metrics: Optional[
            "capo_cleanroomsml.types.metrics_list.MetricsList"
        ] = None,
        min_matching_seed_size: Optional[
            "capo_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
        ] = None,
        audience_size_config: Optional[
            "capo_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
        ] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanroomsml.types.update_configured_audience_model_response.UpdateConfiguredAudienceModelResponse":
        """<p>Provides the information necessary to update a configured audience model. Updates that impact audience generation jobs take effect when a new job starts, but do not impact currently running jobs.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you want to update.</p>
            output_config: <p>The new output configuration.</p>
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the new audience model that you want to use.</p>
            shared_audience_metrics: <p>The new value for whether to share audience metrics.</p>
            min_matching_seed_size: <p>The minimum number of users from the seed audience that must match with users in the training data of the audience model.</p>
            audience_size_config: <p>The new audience size configuration.</p>
            description: <p>The new description of the configured audience model.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.update_configured_audience_model_request.UpdateConfiguredAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.update_configured_audience_model_response.UpdateConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.update_configured_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.update_configured_audience_model.async_update_configured_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.update_configured_audience_model_request.UpdateConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }
        if output_config is not None:
            input_["output_config"] = output_config
        if audience_model_arn is not None:
            input_["audience_model_arn"] = audience_model_arn
        if shared_audience_metrics is not None:
            input_["shared_audience_metrics"] = shared_audience_metrics
        if min_matching_seed_size is not None:
            input_["min_matching_seed_size"] = min_matching_seed_size
        if audience_size_config is not None:
            input_["audience_size_config"] = audience_size_config
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_audience_model(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configured audience model. You can't delete a configured audience model if there are any lookalike models that use the configured audience model. If you delete a configured audience model, it will be removed from any collaborations that it is associated to.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_configured_audience_model_request.DeleteConfiguredAudienceModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model.async_delete_configured_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_configured_audience_model_request.DeleteConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configured_audience_models(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_configured_audience_models_response.ListConfiguredAudienceModelsResponse":
        """<p>Returns a list of the configured audience models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_configured_audience_models_request.ListConfiguredAudienceModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_configured_audience_models_response.ListConfiguredAudienceModelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_configured_audience_models

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_configured_audience_models.async_list_configured_audience_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_configured_audience_models_request.ListConfiguredAudienceModelsRequest = {}
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

    async def iter_list_configured_audience_models(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.configured_audience_model_summary.ConfiguredAudienceModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_configured_audience_models(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("configured_audience_models",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_configured_audience_model_policy(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        configured_audience_model_policy: "capo_cleanroomsml.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        previous_policy_hash: Optional["capo_cleanroomsml.types.hash.Hash"] = None,
        policy_existence_condition: Optional[
            "capo_cleanroomsml.types.policy_existence_condition.PolicyExistenceCondition"
        ] = None,
    ) -> "capo_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse":
        """<p>Create or update the resource policy for a configured audience model.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that the resource policy will govern.</p>
            configured_audience_model_policy: <p>The IAM resource policy.</p>
            previous_policy_hash: <p>A cryptographic hash of the contents of the policy used to prevent unexpected concurrent modification of the policy.</p>
            policy_existence_condition: <p>Use this to prevent unexpected concurrent modification of the policy.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.put_configured_audience_model_policy_response.PutConfiguredAudienceModelPolicyResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.put_configured_audience_model_policy.async_put_configured_audience_model_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.put_configured_audience_model_policy_request.PutConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn,
            "configured_audience_model_policy": configured_audience_model_policy,
        }
        if previous_policy_hash is not None:
            input_["previous_policy_hash"] = previous_policy_hash
        if policy_existence_condition is not None:
            input_["policy_existence_condition"] = policy_existence_condition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_audience_model_policy(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse":
        """<p>Returns information about a configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_configured_audience_model_policy_response.GetConfiguredAudienceModelPolicyResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model_policy.async_get_configured_audience_model_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_configured_audience_model_policy_request.GetConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_audience_model_policy(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configured audience model policy.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model policy that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model_policy.async_delete_configured_audience_model_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_configured_audience_model_policy_request.DeleteConfiguredAudienceModelPolicyRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configured_model_algorithm(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        role_arn: "capo_cleanroomsml.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        training_container_config: Optional[
            "capo_cleanroomsml.types.container_config.ContainerConfig"
        ] = None,
        inference_container_config: Optional[
            "capo_cleanroomsml.types.inference_container_config.InferenceContainerConfig"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse":
        """<p>Creates a configured model algorithm using a container image stored in an ECR repository.</p>

        Args:
            name: <p>The name of the configured model algorithm.</p>
            description: <p>The description of the configured model algorithm.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the role that is used to access the repository.</p>
            training_container_config: <p>Configuration information for the training container, including entrypoints and arguments.</p>
            inference_container_config: <p>Configuration information for the inference container that is used when you run an inference job on a configured model algorithm.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model algorithm and associated data.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm.async_create_configured_model_algorithm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest = {
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if training_container_config is not None:
            input_["training_container_config"] = training_container_config
        if inference_container_config is not None:
            input_["inference_container_config"] = inference_container_config
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_model_algorithm(
        self,
        configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse":
        """<p>Returns information about a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to return information about.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm.async_get_configured_model_algorithm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest = {
            "configured_model_algorithm_arn": configured_model_algorithm_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_model_algorithm(
        self,
        configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm.async_delete_configured_model_algorithm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest = {
            "configured_model_algorithm_arn": configured_model_algorithm_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configured_model_algorithms(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse":
        """<p>Returns a list of configured model algorithms.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms.async_list_configured_model_algorithms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest = {}
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

    async def iter_list_configured_model_algorithms(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.configured_model_algorithm_summary.ConfiguredModelAlgorithmSummary]":
        _token = next_token
        while True:
            _response = await self.list_configured_model_algorithms(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("configured_model_algorithms",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_configured_model_algorithm_association(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        name: "capo_cleanroomsml.types.name_string.NameString",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        privacy_configuration: Optional[
            "capo_cleanroomsml.types.privacy_configuration.PrivacyConfiguration"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanroomsml.types.create_configured_model_algorithm_association_response.CreateConfiguredModelAlgorithmAssociationResponse":
        """<p>Associates a configured model algorithm to a collaboration for use by any member of the collaboration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member who is associating this configured model algorithm.</p>
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to associate.</p>
            name: <p>The name of the configured model algorithm association.</p>
            description: <p>The description of the configured model algorithm association.</p>
            privacy_configuration: <p>Specifies the privacy configuration information for the configured model algorithm association. This information includes the maximum data size that can be exported.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_configured_model_algorithm_association_request.CreateConfiguredModelAlgorithmAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_configured_model_algorithm_association_response.CreateConfiguredModelAlgorithmAssociationResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm_association

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm_association.async_create_configured_model_algorithm_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.create_configured_model_algorithm_association_request.CreateConfiguredModelAlgorithmAssociationRequest = {
            "membership_identifier": membership_identifier,
            "configured_model_algorithm_arn": configured_model_algorithm_arn,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if privacy_configuration is not None:
            input_["privacy_configuration"] = privacy_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configured_model_algorithm_association(
        self,
        configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_model_algorithm_association_response.GetConfiguredModelAlgorithmAssociationResponse":
        """<p>Returns information about a configured model algorithm association.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.</p>
            membership_identifier: <p>The membership ID of the member that created the configured model algorithm association.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_configured_model_algorithm_association_request.GetConfiguredModelAlgorithmAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_configured_model_algorithm_association_response.GetConfiguredModelAlgorithmAssociationResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm_association

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm_association.async_get_configured_model_algorithm_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_configured_model_algorithm_association_request.GetConfiguredModelAlgorithmAssociationRequest = {
            "configured_model_algorithm_association_arn": configured_model_algorithm_association_arn,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configured_model_algorithm_association(
        self,
        configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a configured model algorithm association.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to delete.</p>
            membership_identifier: <p>The membership ID of the member that is deleting the configured model algorithm association.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_configured_model_algorithm_association_request.DeleteConfiguredModelAlgorithmAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm_association

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm_association.async_delete_configured_model_algorithm_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_configured_model_algorithm_association_request.DeleteConfiguredModelAlgorithmAssociationRequest = {
            "configured_model_algorithm_association_arn": configured_model_algorithm_association_arn,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configured_model_algorithm_associations(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_configured_model_algorithm_associations_response.ListConfiguredModelAlgorithmAssociationsResponse":
        """<p>Returns a list of configured model algorithm associations.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership ID of the member that created the configured model algorithm associations you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_configured_model_algorithm_associations_request.ListConfiguredModelAlgorithmAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_configured_model_algorithm_associations_response.ListConfiguredModelAlgorithmAssociationsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithm_associations

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithm_associations.async_list_configured_model_algorithm_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_configured_model_algorithm_associations_request.ListConfiguredModelAlgorithmAssociationsRequest = {
            "membership_identifier": membership_identifier
        }
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

    async def iter_list_configured_model_algorithm_associations(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.configured_model_algorithm_association_summary.ConfiguredModelAlgorithmAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_configured_model_algorithm_associations(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("configured_model_algorithm_associations",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_collaboration_configured_model_algorithm_association(
        self,
        configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_response.GetCollaborationConfiguredModelAlgorithmAssociationResponse":
        """<p>Returns information about the configured model algorithm association in a collaboration.</p>

        Args:
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.</p>
            collaboration_identifier: <p>The collaboration ID for the collaboration that contains the configured model algorithm association that you want to return information about.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_request.GetCollaborationConfiguredModelAlgorithmAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_response.GetCollaborationConfiguredModelAlgorithmAssociationResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_configured_model_algorithm_association

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_configured_model_algorithm_association.async_get_collaboration_configured_model_algorithm_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_collaboration_configured_model_algorithm_association_request.GetCollaborationConfiguredModelAlgorithmAssociationRequest = {
            "configured_model_algorithm_association_arn": configured_model_algorithm_association_arn,
            "collaboration_identifier": collaboration_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_ml_configuration(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        default_output_location: "capo_cleanroomsml.types.ml_output_configuration.MLOutputConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Assigns information about an ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is being configured.</p>
            default_output_location: <p>The default Amazon S3 location where ML output is stored for the specified member.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration.async_put_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest = {
            "membership_identifier": membership_identifier,
            "default_output_location": default_output_location,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ml_configuration(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse":
        """<p>Returns information about a specific ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that owns the ML configuration you want to return information about.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration.async_get_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest = {
            "membership_identifier": membership_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ml_configuration(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a ML modeling configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the of the member that is deleting the ML modeling configuration.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration.async_delete_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest = {
            "membership_identifier": membership_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ml_input_channel(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        configured_model_algorithm_associations: "capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList",
        input_channel: "capo_cleanroomsml.types.input_channel.InputChannel",
        name: "capo_cleanroomsml.types.name_string.NameString",
        retention_in_days: int,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        payer_configuration: Optional[
            "capo_cleanroomsml.types.payer_configuration.PayerConfiguration"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse":
        """<p>Provides the information to create an ML input channel. An ML input channel is the result of a query that can be used for ML modeling.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is creating the ML input channel.</p>
            configured_model_algorithm_associations: <p>The associated configured model algorithms that are necessary to create this ML input channel.</p>
            input_channel: <p>The input data that is used to create this ML input channel.</p>
            name: <p>The name of the ML input channel.</p>
            retention_in_days: <p>The number of days that the data in the ML input channel is retained.</p>
            description: <p>The description of the ML input channel.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            payer_configuration: <p>The payer configuration for the ML input channel. Determines which member account pays for compute and synthetic data costs.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel.async_create_ml_input_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest = {
            "membership_identifier": membership_identifier,
            "configured_model_algorithm_associations": configured_model_algorithm_associations,
            "input_channel": input_channel,
            "name": name,
            "retention_in_days": retention_in_days,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if payer_configuration is not None:
            input_["payer_configuration"] = payer_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ml_input_channel(
        self,
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse":
        """<p>Returns information about an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel that you want to get.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel.async_get_ml_input_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ml_input_channel_data(
        self,
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Provides the information necessary to delete an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to delete.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data.async_delete_ml_input_channel_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "membership_identifier": membership_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ml_input_channels(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse":
        """<p>Returns a list of ML input channels.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of ML input channels to return.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channels that you want to list.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels.async_list_ml_input_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest = {
            "membership_identifier": membership_identifier
        }
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

    async def iter_list_ml_input_channels(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.ml_input_channel_summary.MLInputChannelSummary]":
        _token = next_token
        while True:
            _response = await self.list_ml_input_channels(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("ml_input_channels_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_collaboration_ml_input_channel(
        self,
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse":
        """<p>Returns information about a specific ML input channel in a collaboration.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the ML input channel that you want to get.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel.async_get_collaboration_ml_input_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "collaboration_identifier": collaboration_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_trained_model(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        name: "capo_cleanroomsml.types.name_string.NameString",
        configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn",
        resource_config: "capo_cleanroomsml.types.resource_config.ResourceConfig",
        data_channels: "capo_cleanroomsml.types.model_training_data_channels.ModelTrainingDataChannels",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        hyperparameters: Optional[
            "capo_cleanroomsml.types.hyper_parameters.HyperParameters"
        ] = None,
        environment: Optional["capo_cleanroomsml.types.environment.Environment"] = None,
        stopping_condition: Optional[
            "capo_cleanroomsml.types.stopping_condition.StoppingCondition"
        ] = None,
        incremental_training_data_channels: Optional[
            "capo_cleanroomsml.types.incremental_training_data_channels.IncrementalTrainingDataChannels"
        ] = None,
        training_input_mode: Optional[
            "capo_cleanroomsml.types.training_input_mode.TrainingInputMode"
        ] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        ml_model_training_payer_account_id: Optional[
            "capo_cleanroomsml.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_trained_model_response.CreateTrainedModelResponse":
        """<p>Creates a trained model from an associated configured model algorithm using data from any member of the collaboration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is creating the trained model.</p>
            name: <p>The name of the trained model.</p>
            configured_model_algorithm_association_arn: <p>The associated configured model algorithm used to train this model.</p>
            hyperparameters: <p>Algorithm-specific parameters that influence the quality of the model. You set hyperparameters before you start the learning process.</p>
            environment: <p>The environment variables to set in the Docker container.</p>
            resource_config: <p>Information about the EC2 resources that are used to train this model.</p>
            stopping_condition: <p>The criteria that is used to stop model training.</p>
            incremental_training_data_channels: <p>Specifies the incremental training data channels for the trained model. </p> <p>Incremental training allows you to create a new trained model with updates without retraining from scratch. You can specify up to one incremental training data channel that references a previously trained model and its version.</p> <p>Limit: Maximum of 20 channels total (including both <code>incrementalTrainingDataChannels</code> and <code>dataChannels</code>).</p>
            data_channels: <p>Defines the data channels that are used as input for the trained model request.</p> <p>Limit: Maximum of 20 channels total (including both <code>dataChannels</code> and <code>incrementalTrainingDataChannels</code>).</p>
            training_input_mode: <p>The input mode for accessing the training data. This parameter determines how the training data is made available to the training algorithm. Valid values are:</p> <ul> <li> <p> <code>File</code> - The training data is downloaded to the training instance and made available as files.</p> </li> <li> <p> <code>FastFile</code> - The training data is streamed directly from Amazon S3 to the training algorithm, providing faster access for large datasets.</p> </li> <li> <p> <code>Pipe</code> - The training data is streamed to the training algorithm using named pipes, which can improve performance for certain algorithms.</p> </li> </ul>
            description: <p>The description of the trained model.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            ml_model_training_payer_account_id: <p>The account ID of the member that is responsible for paying for model training costs.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred. Retry your request. If the problem persists, contact AWS Support.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_trained_model_request.CreateTrainedModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_trained_model_response.CreateTrainedModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_trained_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_trained_model.async_create_trained_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.create_trained_model_request.CreateTrainedModelRequest = {
            "membership_identifier": membership_identifier,
            "name": name,
            "configured_model_algorithm_association_arn": configured_model_algorithm_association_arn,
            "resource_config": resource_config,
            "data_channels": data_channels,
        }
        if hyperparameters is not None:
            input_["hyperparameters"] = hyperparameters
        if environment is not None:
            input_["environment"] = environment
        if stopping_condition is not None:
            input_["stopping_condition"] = stopping_condition
        if incremental_training_data_channels is not None:
            input_["incremental_training_data_channels"] = (
                incremental_training_data_channels
            )
        if training_input_mode is not None:
            input_["training_input_mode"] = training_input_mode
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if ml_model_training_payer_account_id is not None:
            input_["ml_model_training_payer_account_id"] = (
                ml_model_training_payer_account_id
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_trained_model(
        self,
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        version_identifier: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
    ) -> "capo_cleanroomsml.types.get_trained_model_response.GetTrainedModelResponse":
        """<p>Returns information about a trained model.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you are interested in.</p>
            membership_identifier: <p>The membership ID of the member that created the trained model that you are interested in.</p>
            version_identifier: <p>The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_trained_model_request.GetTrainedModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_trained_model_response.GetTrainedModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_trained_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_trained_model.async_get_trained_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_trained_model_request.GetTrainedModelRequest = {
            "trained_model_arn": trained_model_arn,
            "membership_identifier": membership_identifier,
        }
        if version_identifier is not None:
            input_["version_identifier"] = version_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_trained_model_output(
        self,
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        version_identifier: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
    ) -> None:
        """<p>Deletes the model artifacts stored by the service.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model whose output you want to delete.</p>
            membership_identifier: <p>The membership ID of the member that is deleting the trained model output.</p>
            version_identifier: <p>The version identifier of the trained model to delete. If not specified, the operation will delete the base version of the trained model. When specified, only the particular version will be deleted.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_trained_model_output_request.DeleteTrainedModelOutputRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_trained_model_output

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_trained_model_output.async_delete_trained_model_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_trained_model_output_request.DeleteTrainedModelOutputRequest = {
            "trained_model_arn": trained_model_arn,
            "membership_identifier": membership_identifier,
        }
        if version_identifier is not None:
            input_["version_identifier"] = version_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_trained_models(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_cleanroomsml.types.list_trained_models_response.ListTrainedModelsResponse"
    ):
        """<p>Returns a list of trained models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership ID of the member that created the trained models you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_trained_models_request.ListTrainedModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_trained_models_response.ListTrainedModelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_trained_models

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_trained_models.async_list_trained_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_trained_models_request.ListTrainedModelsRequest = {
            "membership_identifier": membership_identifier
        }
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

    async def iter_list_trained_models(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.trained_model_summary.TrainedModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_trained_models(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("trained_models",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def cancel_trained_model(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        version_identifier: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
    ) -> None:
        """<p>Submits a request to cancel the trained model job.</p>

        Args:
            membership_identifier: <p>The membership ID of the trained model job that you want to cancel.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model job that you want to cancel.</p>
            version_identifier: <p>The version identifier of the trained model to cancel. This parameter allows you to specify which version of the trained model you want to cancel when multiple versions exist.</p> <p>If <code>versionIdentifier</code> is not specified, the base model will be cancelled.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.cancel_trained_model_request.CancelTrainedModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model.async_cancel_trained_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.cancel_trained_model_request.CancelTrainedModelRequest = {
            "membership_identifier": membership_identifier,
            "trained_model_arn": trained_model_arn,
        }
        if version_identifier is not None:
            input_["version_identifier"] = version_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collaboration_trained_model(
        self,
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        version_identifier: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
    ) -> "capo_cleanroomsml.types.get_collaboration_trained_model_response.GetCollaborationTrainedModelResponse":
        """<p>Returns information about a trained model in a collaboration.</p>

        Args:
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you want to return information about.</p>
            collaboration_identifier: <p>The collaboration ID that contains the trained model that you want to return information about.</p>
            version_identifier: <p>The version identifier of the trained model to retrieve. If not specified, the operation returns information about the latest version of the trained model.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_collaboration_trained_model_request.GetCollaborationTrainedModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_collaboration_trained_model_response.GetCollaborationTrainedModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_trained_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_trained_model.async_get_collaboration_trained_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_collaboration_trained_model_request.GetCollaborationTrainedModelRequest = {
            "trained_model_arn": trained_model_arn,
            "collaboration_identifier": collaboration_identifier,
        }
        if version_identifier is not None:
            input_["version_identifier"] = version_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_trained_model_versions(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        status: Optional[
            "capo_cleanroomsml.types.trained_model_status.TrainedModelStatus"
        ] = None,
    ) -> "capo_cleanroomsml.types.list_trained_model_versions_response.ListTrainedModelVersionsResponse":
        """<p>Returns a list of trained model versions for a specified trained model. This operation allows you to view all versions of a trained model, including information about their status and creation details. You can use this to track the evolution of your trained models and select specific versions for inference or further training.</p>

        Args:
            next_token: <p>The pagination token from a previous <code>ListTrainedModelVersions</code> request. Use this token to retrieve the next page of results.</p>
            max_results: <p>The maximum number of trained model versions to return in a single page. The default value is 10, and the maximum value is 100.</p>
            membership_identifier: <p>The membership identifier for the collaboration that contains the trained model.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model for which to list versions.</p>
            status: <p>Filter the results to only include trained model versions with the specified status. Valid values include <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>ACTIVE</code>, <code>CREATE_FAILED</code>, and others.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_trained_model_versions_request.ListTrainedModelVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_trained_model_versions_response.ListTrainedModelVersionsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_trained_model_versions

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_trained_model_versions.async_list_trained_model_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_trained_model_versions_request.ListTrainedModelVersionsRequest = {
            "membership_identifier": membership_identifier,
            "trained_model_arn": trained_model_arn,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_trained_model_versions(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        status: Optional[
            "capo_cleanroomsml.types.trained_model_status.TrainedModelStatus"
        ] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.trained_model_summary.TrainedModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_trained_model_versions(
                membership_identifier,
                trained_model_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            _page = _resolve_path(_response, ("trained_models",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_trained_model_export_job(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        output_configuration: "capo_cleanroomsml.types.trained_model_export_output_configuration.TrainedModelExportOutputConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Provides the information necessary to start a trained model export job.</p>

        Args:
            name: <p>The name of the trained model export job.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you want to export.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to export. This specifies which version of the trained model should be exported to the specified destination.</p>
            membership_identifier: <p>The membership ID of the member that is receiving the exported trained model artifacts.</p>
            output_configuration: <p>The output configuration information for the trained model export job.</p>
            description: <p>The description of the trained model export job.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job.async_start_trained_model_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest = {
            "name": name,
            "trained_model_arn": trained_model_arn,
            "membership_identifier": membership_identifier,
            "output_configuration": output_configuration,
        }
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_trained_model_inference_job(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        name: "capo_cleanroomsml.types.name_string.NameString",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        resource_config: "capo_cleanroomsml.types.inference_resource_config.InferenceResourceConfig",
        output_configuration: "capo_cleanroomsml.types.inference_output_configuration.InferenceOutputConfiguration",
        data_source: "capo_cleanroomsml.types.model_inference_data_source.ModelInferenceDataSource",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
        configured_model_algorithm_association_arn: Optional[
            "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
        ] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        container_execution_parameters: Optional[
            "capo_cleanroomsml.types.inference_container_execution_parameters.InferenceContainerExecutionParameters"
        ] = None,
        environment: Optional[
            "capo_cleanroomsml.types.inference_environment_map.InferenceEnvironmentMap"
        ] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        ml_model_inference_payer_account_id: Optional[
            "capo_cleanroomsml.types.account_id.AccountId"
        ] = None,
    ) -> "capo_cleanroomsml.types.start_trained_model_inference_job_response.StartTrainedModelInferenceJobResponse":
        """<p>Defines the information necessary to begin a trained model inference job.</p>

        Args:
            membership_identifier: <p>The membership ID of the membership that contains the trained model inference job.</p>
            name: <p>The name of the trained model inference job.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that is used for this trained model inference job.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to use for inference. This specifies which version of the trained model should be used to generate predictions on the input data.</p>
            configured_model_algorithm_association_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm association that is used for this trained model inference job.</p>
            resource_config: <p>Defines the resource configuration for the trained model inference job.</p>
            output_configuration: <p>Defines the output configuration information for the trained model inference job.</p>
            data_source: <p>Defines the data source that is used for the trained model inference job.</p>
            description: <p>The description of the trained model inference job.</p>
            container_execution_parameters: <p>The execution parameters for the container.</p>
            environment: <p>The environment variables to set in the Docker container.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the ML inference job and associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            ml_model_inference_payer_account_id: <p>The account ID of the member that is responsible for paying for model inference costs.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.start_trained_model_inference_job_request.StartTrainedModelInferenceJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.start_trained_model_inference_job_response.StartTrainedModelInferenceJobResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_trained_model_inference_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.start_trained_model_inference_job.async_start_trained_model_inference_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.start_trained_model_inference_job_request.StartTrainedModelInferenceJobRequest = {
            "membership_identifier": membership_identifier,
            "name": name,
            "trained_model_arn": trained_model_arn,
            "resource_config": resource_config,
            "output_configuration": output_configuration,
            "data_source": data_source,
        }
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )
        if configured_model_algorithm_association_arn is not None:
            input_["configured_model_algorithm_association_arn"] = (
                configured_model_algorithm_association_arn
            )
        if description is not None:
            input_["description"] = description
        if container_execution_parameters is not None:
            input_["container_execution_parameters"] = container_execution_parameters
        if environment is not None:
            input_["environment"] = environment
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if ml_model_inference_payer_account_id is not None:
            input_["ml_model_inference_payer_account_id"] = (
                ml_model_inference_payer_account_id
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_trained_model_inference_job(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        trained_model_inference_job_arn: "capo_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_trained_model_inference_job_response.GetTrainedModelInferenceJobResponse":
        """<p>Returns information about a trained model inference job.</p>

        Args:
            membership_identifier: <p>Provides the membership ID of the membership that contains the trained model inference job that you are interested in.</p>
            trained_model_inference_job_arn: <p>Provides the Amazon Resource Name (ARN) of the trained model inference job that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_trained_model_inference_job_request.GetTrainedModelInferenceJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_trained_model_inference_job_response.GetTrainedModelInferenceJobResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_trained_model_inference_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_trained_model_inference_job.async_get_trained_model_inference_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_trained_model_inference_job_request.GetTrainedModelInferenceJobRequest = {
            "membership_identifier": membership_identifier,
            "trained_model_inference_job_arn": trained_model_inference_job_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_trained_model_inference_jobs(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        trained_model_arn: Optional[
            "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
        ] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "capo_cleanroomsml.types.list_trained_model_inference_jobs_response.ListTrainedModelInferenceJobsResponse":
        """<p>Returns a list of trained model inference jobs that match the request parameters.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            membership_identifier: <p>The membership </p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of a trained model that was used to create the trained model inference jobs that you are interested in.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to filter inference jobs by. When specified, only inference jobs that used this specific version of the trained model are returned.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_trained_model_inference_jobs_request.ListTrainedModelInferenceJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_trained_model_inference_jobs_response.ListTrainedModelInferenceJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_trained_model_inference_jobs

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_trained_model_inference_jobs.async_list_trained_model_inference_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_trained_model_inference_jobs_request.ListTrainedModelInferenceJobsRequest = {
            "membership_identifier": membership_identifier
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if trained_model_arn is not None:
            input_["trained_model_arn"] = trained_model_arn
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_trained_model_inference_jobs(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        trained_model_arn: Optional[
            "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
        ] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.trained_model_inference_job_summary.TrainedModelInferenceJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_trained_model_inference_jobs(
                membership_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                trained_model_arn=trained_model_arn,
                trained_model_version_identifier=trained_model_version_identifier,
            )
            _page = _resolve_path(_response, ("trained_model_inference_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def cancel_trained_model_inference_job(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        trained_model_inference_job_arn: "capo_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Submits a request to cancel a trained model inference job.</p>

        Args:
            membership_identifier: <p>The membership ID of the trained model inference job that you want to cancel.</p>
            trained_model_inference_job_arn: <p>The Amazon Resource Name (ARN) of the trained model inference job that you want to cancel.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.cancel_trained_model_inference_job_request.CancelTrainedModelInferenceJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model_inference_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.cancel_trained_model_inference_job.async_cancel_trained_model_inference_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.cancel_trained_model_inference_job_request.CancelTrainedModelInferenceJobRequest = {
            "membership_identifier": membership_identifier,
            "trained_model_inference_job_arn": trained_model_inference_job_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_training_dataset(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        role_arn: "capo_cleanroomsml.types.iam_role_arn.IamRoleArn",
        training_data: "capo_cleanroomsml.types.dataset_list.DatasetList",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_training_dataset_response.CreateTrainingDatasetResponse":
        """<p>Defines the information necessary to create a training dataset. In Clean Rooms ML, the <code>TrainingDataset</code> is metadata that points to a Glue table, which is read only during <code>AudienceModel</code> creation.</p>

        Args:
            name: <p>The name of the training dataset. This name must be unique in your account and region.</p>
            role_arn: <p>The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the <code>dataSource</code> field of each dataset.</p> <p>Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your account, you get an <code>AccessDeniedException</code> error.</p>
            training_data: <p>An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            description: <p>The description of the training dataset.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_training_dataset_request.CreateTrainingDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_training_dataset_response.CreateTrainingDatasetResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_training_dataset

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_training_dataset.async_create_training_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.create_training_dataset_request.CreateTrainingDatasetRequest = {
            "name": name,
            "role_arn": role_arn,
            "training_data": training_data,
        }
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_training_dataset(
        self,
        training_dataset_arn: "capo_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_training_dataset_response.GetTrainingDatasetResponse":
        """<p>Returns information about a training dataset.</p>

        Args:
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_training_dataset_request.GetTrainingDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_training_dataset_response.GetTrainingDatasetResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_training_dataset

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_training_dataset.async_get_training_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.get_training_dataset_request.GetTrainingDatasetRequest = {
            "training_dataset_arn": training_dataset_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_training_dataset(
        self,
        training_dataset_arn: "capo_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Specifies a training dataset that you want to delete. You can't delete a training dataset if there are any audience models that depend on the training dataset. In Clean Rooms ML, the <code>TrainingDataset</code> is metadata that points to a Glue table, which is read only during <code>AudienceModel</code> creation. This action deletes the metadata.</p>

        Args:
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_training_dataset_request.DeleteTrainingDatasetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_training_dataset

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_training_dataset.async_delete_training_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.delete_training_dataset_request.DeleteTrainingDatasetRequest = {
            "training_dataset_arn": training_dataset_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_training_datasets(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_training_datasets_response.ListTrainingDatasetsResponse":
        """<p>Returns a list of training datasets.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_training_datasets_request.ListTrainingDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_training_datasets_response.ListTrainingDatasetsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_training_datasets

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_training_datasets.async_list_training_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cleanroomsml.types.list_training_datasets_request.ListTrainingDatasetsRequest = {}
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

    async def iter_list_training_datasets(
        self,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_cleanroomsml.types.training_dataset_summary.TrainingDatasetSummary]":
        _token = next_token
        while True:
            _response = await self.list_training_datasets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("training_datasets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
