"""Generated from Smithy shape ``com.amazonaws.codepipeline#CodePipeline_20150709``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_codepipeline._auth._signers
import capo_codepipeline._auth._sigv4
from capo_codepipeline._auth._identity import Credentials
from capo_codepipeline._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codepipeline._auth._zapros_handler import AuthMiddleware
from capo_codepipeline._pagination import resolve_path as _resolve_path
from capo_codepipeline._services._aws_config import aaws_config
from capo_codepipeline._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_codepipeline.types.acknowledge_job_input
    import capo_codepipeline.types.acknowledge_job_output
    import capo_codepipeline.types.acknowledge_third_party_job_input
    import capo_codepipeline.types.acknowledge_third_party_job_output
    import capo_codepipeline.types.action_category
    import capo_codepipeline.types.action_configuration_property_list
    import capo_codepipeline.types.action_execution_detail
    import capo_codepipeline.types.action_execution_filter
    import capo_codepipeline.types.action_execution_id
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.action_owner
    import capo_codepipeline.types.action_provider
    import capo_codepipeline.types.action_revision
    import capo_codepipeline.types.action_type
    import capo_codepipeline.types.action_type_declaration
    import capo_codepipeline.types.action_type_id
    import capo_codepipeline.types.action_type_owner
    import capo_codepipeline.types.action_type_settings
    import capo_codepipeline.types.approval_result
    import capo_codepipeline.types.approval_token
    import capo_codepipeline.types.artifact_details
    import capo_codepipeline.types.aws_region_name
    import capo_codepipeline.types.boolean
    import capo_codepipeline.types.client_request_token
    import capo_codepipeline.types.client_token
    import capo_codepipeline.types.condition_type
    import capo_codepipeline.types.continuation_token
    import capo_codepipeline.types.create_custom_action_type_input
    import capo_codepipeline.types.create_custom_action_type_output
    import capo_codepipeline.types.create_pipeline_input
    import capo_codepipeline.types.create_pipeline_output
    import capo_codepipeline.types.current_revision
    import capo_codepipeline.types.delete_custom_action_type_input
    import capo_codepipeline.types.delete_pipeline_input
    import capo_codepipeline.types.delete_webhook_input
    import capo_codepipeline.types.delete_webhook_output
    import capo_codepipeline.types.deploy_action_execution_target
    import capo_codepipeline.types.deregister_webhook_with_third_party_input
    import capo_codepipeline.types.deregister_webhook_with_third_party_output
    import capo_codepipeline.types.disable_stage_transition_input
    import capo_codepipeline.types.disabled_reason
    import capo_codepipeline.types.enable_stage_transition_input
    import capo_codepipeline.types.execution_details
    import capo_codepipeline.types.failure_details
    import capo_codepipeline.types.get_action_type_input
    import capo_codepipeline.types.get_action_type_output
    import capo_codepipeline.types.get_job_details_input
    import capo_codepipeline.types.get_job_details_output
    import capo_codepipeline.types.get_pipeline_execution_input
    import capo_codepipeline.types.get_pipeline_execution_output
    import capo_codepipeline.types.get_pipeline_input
    import capo_codepipeline.types.get_pipeline_output
    import capo_codepipeline.types.get_pipeline_state_input
    import capo_codepipeline.types.get_pipeline_state_output
    import capo_codepipeline.types.get_third_party_job_details_input
    import capo_codepipeline.types.get_third_party_job_details_output
    import capo_codepipeline.types.job_id
    import capo_codepipeline.types.list_action_executions_input
    import capo_codepipeline.types.list_action_executions_output
    import capo_codepipeline.types.list_action_types_input
    import capo_codepipeline.types.list_action_types_output
    import capo_codepipeline.types.list_deploy_action_execution_targets_input
    import capo_codepipeline.types.list_deploy_action_execution_targets_output
    import capo_codepipeline.types.list_pipeline_executions_input
    import capo_codepipeline.types.list_pipeline_executions_output
    import capo_codepipeline.types.list_pipelines_input
    import capo_codepipeline.types.list_pipelines_output
    import capo_codepipeline.types.list_rule_executions_input
    import capo_codepipeline.types.list_rule_executions_output
    import capo_codepipeline.types.list_rule_types_input
    import capo_codepipeline.types.list_rule_types_output
    import capo_codepipeline.types.list_tags_for_resource_input
    import capo_codepipeline.types.list_tags_for_resource_output
    import capo_codepipeline.types.list_webhook_item
    import capo_codepipeline.types.list_webhooks_input
    import capo_codepipeline.types.list_webhooks_output
    import capo_codepipeline.types.max_batch_size
    import capo_codepipeline.types.max_pipelines
    import capo_codepipeline.types.max_results
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.nonce
    import capo_codepipeline.types.output_variables_map
    import capo_codepipeline.types.override_stage_condition_input
    import capo_codepipeline.types.pipeline_declaration
    import capo_codepipeline.types.pipeline_execution_filter
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_execution_summary
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.pipeline_summary
    import capo_codepipeline.types.pipeline_variable_list
    import capo_codepipeline.types.pipeline_version
    import capo_codepipeline.types.poll_for_jobs_input
    import capo_codepipeline.types.poll_for_jobs_output
    import capo_codepipeline.types.poll_for_third_party_jobs_input
    import capo_codepipeline.types.poll_for_third_party_jobs_output
    import capo_codepipeline.types.put_action_revision_input
    import capo_codepipeline.types.put_action_revision_output
    import capo_codepipeline.types.put_approval_result_input
    import capo_codepipeline.types.put_approval_result_output
    import capo_codepipeline.types.put_job_failure_result_input
    import capo_codepipeline.types.put_job_success_result_input
    import capo_codepipeline.types.put_third_party_job_failure_result_input
    import capo_codepipeline.types.put_third_party_job_success_result_input
    import capo_codepipeline.types.put_webhook_input
    import capo_codepipeline.types.put_webhook_output
    import capo_codepipeline.types.query_param_map
    import capo_codepipeline.types.register_webhook_with_third_party_input
    import capo_codepipeline.types.register_webhook_with_third_party_output
    import capo_codepipeline.types.resource_arn
    import capo_codepipeline.types.retry_stage_execution_input
    import capo_codepipeline.types.retry_stage_execution_output
    import capo_codepipeline.types.rollback_stage_input
    import capo_codepipeline.types.rollback_stage_output
    import capo_codepipeline.types.rule_execution_detail
    import capo_codepipeline.types.rule_execution_filter
    import capo_codepipeline.types.rule_owner
    import capo_codepipeline.types.source_revision_override_list
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.stage_retry_mode
    import capo_codepipeline.types.stage_transition_type
    import capo_codepipeline.types.start_pipeline_execution_input
    import capo_codepipeline.types.start_pipeline_execution_output
    import capo_codepipeline.types.stop_pipeline_execution_input
    import capo_codepipeline.types.stop_pipeline_execution_output
    import capo_codepipeline.types.stop_pipeline_execution_reason
    import capo_codepipeline.types.tag
    import capo_codepipeline.types.tag_key_list
    import capo_codepipeline.types.tag_list
    import capo_codepipeline.types.tag_resource_input
    import capo_codepipeline.types.tag_resource_output
    import capo_codepipeline.types.target_filter_list
    import capo_codepipeline.types.third_party_job_id
    import capo_codepipeline.types.untag_resource_input
    import capo_codepipeline.types.untag_resource_output
    import capo_codepipeline.types.update_action_type_input
    import capo_codepipeline.types.update_pipeline_input
    import capo_codepipeline.types.update_pipeline_output
    import capo_codepipeline.types.version
    import capo_codepipeline.types.webhook_definition
    import capo_codepipeline.types.webhook_name


class AsyncCodePipelineClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncCodePipelineClient:
    """A client for the ``CodePipeline`` service.

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
        self._config = AsyncCodePipelineClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncCodePipelineClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodePipelineClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def acknowledge_job(
        self,
        job_id: "capo_codepipeline.types.job_id.JobId",
        nonce: "capo_codepipeline.types.nonce.Nonce",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.acknowledge_job_output.AcknowledgeJobOutput":
        """<p>Returns information about a specified job and whether that job has been received by the job worker. Used for custom actions only.</p>

        Args:
            job_id: <p>The unique system-generated ID of the job for which you want to confirm receipt.</p>
            nonce: <p>A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response of the <a>PollForJobs</a> request that returned this job.</p>

        Raises:
            capo_codepipeline.errors.invalid_nonce_exception.InvalidNonceException: <p>The nonce was specified in an invalid format.</p>
            capo_codepipeline.errors.job_not_found_exception.JobNotFoundException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.acknowledge_job_input.AcknowledgeJobInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.acknowledge_job_output.AcknowledgeJobOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.acknowledge_job

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.acknowledge_job.async_acknowledge_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.acknowledge_job_input.AcknowledgeJobInput = {
            "job_id": job_id,
            "nonce": nonce,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def acknowledge_third_party_job(
        self,
        job_id: "capo_codepipeline.types.third_party_job_id.ThirdPartyJobId",
        nonce: "capo_codepipeline.types.nonce.Nonce",
        client_token: "capo_codepipeline.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.acknowledge_third_party_job_output.AcknowledgeThirdPartyJobOutput":
        """<p>Confirms a job worker has received the specified job. Used for partner actions only.</p>

        Args:
            job_id: <p>The unique system-generated ID of the job.</p>
            nonce: <p>A system-generated random number that CodePipeline uses to ensure that the job is being worked on by only one job worker. Get this number from the response to a <a>GetThirdPartyJobDetails</a> request.</p>
            client_token: <p>The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.</p>

        Raises:
            capo_codepipeline.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The client token was specified in an invalid format</p>
            capo_codepipeline.errors.invalid_nonce_exception.InvalidNonceException: <p>The nonce was specified in an invalid format.</p>
            capo_codepipeline.errors.job_not_found_exception.JobNotFoundException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.acknowledge_third_party_job_input.AcknowledgeThirdPartyJobInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.acknowledge_third_party_job_output.AcknowledgeThirdPartyJobOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.acknowledge_third_party_job

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.acknowledge_third_party_job.async_acknowledge_third_party_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.acknowledge_third_party_job_input.AcknowledgeThirdPartyJobInput = {
            "job_id": job_id,
            "nonce": nonce,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_action_type(
        self,
        category: "capo_codepipeline.types.action_category.ActionCategory",
        provider: "capo_codepipeline.types.action_provider.ActionProvider",
        version: "capo_codepipeline.types.version.Version",
        input_artifact_details: "capo_codepipeline.types.artifact_details.ArtifactDetails",
        output_artifact_details: "capo_codepipeline.types.artifact_details.ArtifactDetails",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        settings: Optional[
            "capo_codepipeline.types.action_type_settings.ActionTypeSettings"
        ] = None,
        configuration_properties: Optional[
            "capo_codepipeline.types.action_configuration_property_list.ActionConfigurationPropertyList"
        ] = None,
        tags: Optional["capo_codepipeline.types.tag_list.TagList"] = None,
    ) -> "capo_codepipeline.types.create_custom_action_type_output.CreateCustomActionTypeOutput":
        """<p>Creates a new custom action that can be used in all pipelines associated with the Amazon Web Services account. Only used for custom actions.</p>

        Args:
            category: <p>The category of the custom action, such as a build action or a test action.</p>
            provider: <p>The provider of the service used in the custom action, such as CodeDeploy.</p>
            version: <p>The version identifier of the custom action.</p>
            settings: <p>URLs that provide users information about this custom action.</p>
            configuration_properties: <p>The configuration properties for the custom action.</p> <note> <p>You can refer to a name in the configuration properties of the custom action within the URL templates by following the format of {Config:name}, as long as the configuration property is both required and not secret. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-create-custom-action.html">Create a Custom Action for a Pipeline</a>.</p> </note>
            input_artifact_details: <p>The details of the input artifact for the action, such as its commit ID.</p>
            output_artifact_details: <p>The details of the output artifact of the action, such as its commit ID.</p>
            tags: <p>The tags for the custom action.</p>

        Raises:
            capo_codepipeline.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Unable to modify the tag due to a simultaneous update request.</p>
            capo_codepipeline.errors.invalid_tags_exception.InvalidTagsException: <p>The specified resource tags are invalid.</p>
            capo_codepipeline.errors.limit_exceeded_exception.LimitExceededException: <p>The number of pipelines associated with the Amazon Web Services account has exceeded the limit allowed for the account.</p>
            capo_codepipeline.errors.too_many_tags_exception.TooManyTagsException: <p>The tags limit for a resource has been exceeded.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.create_custom_action_type_input.CreateCustomActionTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.create_custom_action_type_output.CreateCustomActionTypeOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.create_custom_action_type

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.create_custom_action_type.async_create_custom_action_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.create_custom_action_type_input.CreateCustomActionTypeInput = {
            "category": category,
            "provider": provider,
            "version": version,
            "input_artifact_details": input_artifact_details,
            "output_artifact_details": output_artifact_details,
        }
        if settings is not None:
            input_["settings"] = settings
        if configuration_properties is not None:
            input_["configuration_properties"] = configuration_properties
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_pipeline(
        self,
        pipeline: "capo_codepipeline.types.pipeline_declaration.PipelineDeclaration",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        tags: Optional["capo_codepipeline.types.tag_list.TagList"] = None,
    ) -> "capo_codepipeline.types.create_pipeline_output.CreatePipelineOutput":
        """<p>Creates a pipeline.</p> <note> <p>In the pipeline structure, you must include either <code>artifactStore</code> or <code>artifactStores</code> in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use <code>artifactStores</code>.</p> </note>

        Args:
            pipeline: <p>Represents the structure of actions and stages to be performed in the pipeline. </p>
            tags: <p>The tags for the pipeline.</p>

        Raises:
            capo_codepipeline.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Unable to modify the tag due to a simultaneous update request.</p>
            capo_codepipeline.errors.invalid_action_declaration_exception.InvalidActionDeclarationException: <p>The action declaration was specified in an invalid format.</p>
            capo_codepipeline.errors.invalid_blocker_declaration_exception.InvalidBlockerDeclarationException: <p>Reserved for future use.</p>
            capo_codepipeline.errors.invalid_stage_declaration_exception.InvalidStageDeclarationException: <p>The stage declaration was specified in an invalid format.</p>
            capo_codepipeline.errors.invalid_structure_exception.InvalidStructureException: <p>The structure was specified in an invalid format.</p>
            capo_codepipeline.errors.invalid_tags_exception.InvalidTagsException: <p>The specified resource tags are invalid.</p>
            capo_codepipeline.errors.limit_exceeded_exception.LimitExceededException: <p>The number of pipelines associated with the Amazon Web Services account has exceeded the limit allowed for the account.</p>
            capo_codepipeline.errors.pipeline_name_in_use_exception.PipelineNameInUseException: <p>The specified pipeline name is already in use.</p>
            capo_codepipeline.errors.too_many_tags_exception.TooManyTagsException: <p>The tags limit for a resource has been exceeded.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.create_pipeline_input.CreatePipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.create_pipeline_output.CreatePipelineOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.create_pipeline

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.create_pipeline.async_create_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.create_pipeline_input.CreatePipelineInput = {
            "pipeline": pipeline
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

    async def delete_custom_action_type(
        self,
        category: "capo_codepipeline.types.action_category.ActionCategory",
        provider: "capo_codepipeline.types.action_provider.ActionProvider",
        version: "capo_codepipeline.types.version.Version",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> None:
        """<p>Marks a custom action as deleted. <code>PollForJobs</code> for the custom action fails after the action is marked for deletion. Used for custom actions only.</p> <important> <p>To re-create a custom action after it has been deleted you must use a string in the version field that has never been used before. This string can be an incremented version number, for example. To restore a deleted custom action, use a JSON file that is identical to the deleted action, including the original string in the version field.</p> </important>

        Args:
            category: <p>The category of the custom action that you want to delete, such as source or deploy.</p>
            provider: <p>The provider of the service used in the custom action, such as CodeDeploy.</p>
            version: <p>The version of the custom action to delete.</p>

        Raises:
            capo_codepipeline.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Unable to modify the tag due to a simultaneous update request.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.delete_custom_action_type_input.DeleteCustomActionTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.delete_custom_action_type

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.delete_custom_action_type.async_delete_custom_action_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.delete_custom_action_type_input.DeleteCustomActionTypeInput = {
            "category": category,
            "provider": provider,
            "version": version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_pipeline(
        self,
        name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified pipeline.</p>

        Args:
            name: <p>The name of the pipeline to be deleted.</p>

        Raises:
            capo_codepipeline.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Unable to modify the tag due to a simultaneous update request.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.delete_pipeline_input.DeletePipelineInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.delete_pipeline

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.delete_pipeline.async_delete_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.delete_pipeline_input.DeletePipelineInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_webhook(
        self,
        name: "capo_codepipeline.types.webhook_name.WebhookName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.delete_webhook_output.DeleteWebhookOutput":
        """<p>Deletes a previously created webhook by name. Deleting the webhook stops CodePipeline from starting a pipeline every time an external event occurs. The API returns successfully when trying to delete a webhook that is already deleted. If a deleted webhook is re-created by calling PutWebhook with the same name, it will have a different URL.</p>

        Args:
            name: <p>The name of the webhook you want to delete.</p>

        Raises:
            capo_codepipeline.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Unable to modify the tag due to a simultaneous update request.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.delete_webhook_input.DeleteWebhookInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.delete_webhook_output.DeleteWebhookOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.delete_webhook

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.delete_webhook.async_delete_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.delete_webhook_input.DeleteWebhookInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_webhook_with_third_party(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        webhook_name: Optional[
            "capo_codepipeline.types.webhook_name.WebhookName"
        ] = None,
    ) -> "capo_codepipeline.types.deregister_webhook_with_third_party_output.DeregisterWebhookWithThirdPartyOutput":
        """<p>Removes the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.</p>

        Args:
            webhook_name: <p>The name of the webhook you want to deregister.</p>

        Raises:
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.webhook_not_found_exception.WebhookNotFoundException: <p>The specified webhook was entered in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.deregister_webhook_with_third_party_input.DeregisterWebhookWithThirdPartyInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.deregister_webhook_with_third_party_output.DeregisterWebhookWithThirdPartyOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.deregister_webhook_with_third_party

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.deregister_webhook_with_third_party.async_deregister_webhook_with_third_party(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.deregister_webhook_with_third_party_input.DeregisterWebhookWithThirdPartyInput = {}
        if webhook_name is not None:
            input_["webhook_name"] = webhook_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_stage_transition(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        stage_name: "capo_codepipeline.types.stage_name.StageName",
        transition_type: "capo_codepipeline.types.stage_transition_type.StageTransitionType",
        reason: "capo_codepipeline.types.disabled_reason.DisabledReason",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> None:
        """<p>Prevents artifacts in a pipeline from transitioning to the next stage in the pipeline.</p>

        Args:
            pipeline_name: <p>The name of the pipeline in which you want to disable the flow of artifacts from one stage to another.</p>
            stage_name: <p>The name of the stage where you want to disable the inbound or outbound transition of artifacts.</p>
            transition_type: <p>Specifies whether artifacts are prevented from transitioning into the stage and being processed by the actions in that stage (inbound), or prevented from transitioning from the stage after they have been processed by the actions in that stage (outbound).</p>
            reason: <p>The reason given to the user that a stage is disabled, such as waiting for manual approval or manual tests. This message is displayed in the pipeline console UI.</p>

        Raises:
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.stage_not_found_exception.StageNotFoundException: <p>The stage was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.disable_stage_transition_input.DisableStageTransitionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.disable_stage_transition

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.disable_stage_transition.async_disable_stage_transition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.disable_stage_transition_input.DisableStageTransitionInput = {
            "pipeline_name": pipeline_name,
            "stage_name": stage_name,
            "transition_type": transition_type,
            "reason": reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_stage_transition(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        stage_name: "capo_codepipeline.types.stage_name.StageName",
        transition_type: "capo_codepipeline.types.stage_transition_type.StageTransitionType",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> None:
        """<p>Enables artifacts in a pipeline to transition to a stage in a pipeline.</p>

        Args:
            pipeline_name: <p>The name of the pipeline in which you want to enable the flow of artifacts from one stage to another.</p>
            stage_name: <p>The name of the stage where you want to enable the transition of artifacts, either into the stage (inbound) or from that stage to the next stage (outbound).</p>
            transition_type: <p>Specifies whether artifacts are allowed to enter the stage and be processed by the actions in that stage (inbound) or whether already processed artifacts are allowed to transition to the next stage (outbound).</p>

        Raises:
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.stage_not_found_exception.StageNotFoundException: <p>The stage was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.enable_stage_transition_input.EnableStageTransitionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.enable_stage_transition

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.enable_stage_transition.async_enable_stage_transition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.enable_stage_transition_input.EnableStageTransitionInput = {
            "pipeline_name": pipeline_name,
            "stage_name": stage_name,
            "transition_type": transition_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_action_type(
        self,
        category: "capo_codepipeline.types.action_category.ActionCategory",
        owner: "capo_codepipeline.types.action_type_owner.ActionTypeOwner",
        provider: "capo_codepipeline.types.action_provider.ActionProvider",
        version: "capo_codepipeline.types.version.Version",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.get_action_type_output.GetActionTypeOutput":
        """<p>Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.</p>

        Args:
            category: <p>Defines what kind of action can be taken in the stage. The following are the valid values:</p> <ul> <li> <p> <code>Source</code> </p> </li> <li> <p> <code>Build</code> </p> </li> <li> <p> <code>Test</code> </p> </li> <li> <p> <code>Deploy</code> </p> </li> <li> <p> <code>Approval</code> </p> </li> <li> <p> <code>Invoke</code> </p> </li> <li> <p> <code>Compute</code> </p> </li> </ul>
            owner: <p>The creator of an action type that was created with any supported integration model. There are two valid values: <code>AWS</code> and <code>ThirdParty</code>.</p>
            provider: <p>The provider of the action type being called. The provider name is specified when the action type is created.</p>
            version: <p>A string that describes the action type version.</p>

        Raises:
            capo_codepipeline.errors.action_type_not_found_exception.ActionTypeNotFoundException: <p>The specified action type cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.get_action_type_input.GetActionTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.get_action_type_output.GetActionTypeOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.get_action_type

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.get_action_type.async_get_action_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.get_action_type_input.GetActionTypeInput = {
            "category": category,
            "owner": owner,
            "provider": provider,
            "version": version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_job_details(
        self,
        job_id: "capo_codepipeline.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.get_job_details_output.GetJobDetailsOutput":
        """<p>Returns information about a job. Used for custom actions only.</p> <important> <p>When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.</p> </important>

        Args:
            job_id: <p>The unique system-generated ID for the job.</p>

        Raises:
            capo_codepipeline.errors.job_not_found_exception.JobNotFoundException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.get_job_details_input.GetJobDetailsInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.get_job_details_output.GetJobDetailsOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.get_job_details

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.get_job_details.async_get_job_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.get_job_details_input.GetJobDetailsInput = {
            "job_id": job_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_pipeline(
        self,
        name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        version: Optional[
            "capo_codepipeline.types.pipeline_version.PipelineVersion"
        ] = None,
    ) -> "capo_codepipeline.types.get_pipeline_output.GetPipelineOutput":
        """<p>Returns the metadata, structure, stages, and actions of a pipeline. Can be used to return the entire structure of a pipeline in JSON format, which can then be modified and used to update the pipeline structure with <a>UpdatePipeline</a>.</p>

        Args:
            name: <p>The name of the pipeline for which you want to get information. Pipeline names must be unique in an Amazon Web Services account.</p>
            version: <p>The version number of the pipeline. If you do not specify a version, defaults to the current version.</p>

        Raises:
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.pipeline_version_not_found_exception.PipelineVersionNotFoundException: <p>The pipeline version was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.get_pipeline_input.GetPipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.get_pipeline_output.GetPipelineOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.get_pipeline

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.get_pipeline.async_get_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.get_pipeline_input.GetPipelineInput = {
            "name": name
        }
        if version is not None:
            input_["version"] = version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_pipeline_execution(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        pipeline_execution_id: "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.get_pipeline_execution_output.GetPipelineExecutionOutput":
        """<p>Returns information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.</p>

        Args:
            pipeline_name: <p>The name of the pipeline about which you want to get execution details.</p>
            pipeline_execution_id: <p>The ID of the pipeline execution about which you want to get execution details.</p>

        Raises:
            capo_codepipeline.errors.pipeline_execution_not_found_exception.PipelineExecutionNotFoundException: <p>The pipeline execution was specified in an invalid format or cannot be found, or an execution ID does not belong to the specified pipeline. </p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.get_pipeline_execution_input.GetPipelineExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.get_pipeline_execution_output.GetPipelineExecutionOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.get_pipeline_execution

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.get_pipeline_execution.async_get_pipeline_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.get_pipeline_execution_input.GetPipelineExecutionInput = {
            "pipeline_name": pipeline_name,
            "pipeline_execution_id": pipeline_execution_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_pipeline_state(
        self,
        name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.get_pipeline_state_output.GetPipelineStateOutput":
        """<p>Returns information about the state of a pipeline, including the stages and actions.</p> <note> <p>Values returned in the <code>revisionId</code> and <code>revisionUrl</code> fields indicate the source revision information, such as the commit ID, for the current state.</p> </note>

        Args:
            name: <p>The name of the pipeline about which you want to get information.</p>

        Raises:
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.get_pipeline_state_input.GetPipelineStateInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.get_pipeline_state_output.GetPipelineStateOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.get_pipeline_state

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.get_pipeline_state.async_get_pipeline_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.get_pipeline_state_input.GetPipelineStateInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_third_party_job_details(
        self,
        job_id: "capo_codepipeline.types.third_party_job_id.ThirdPartyJobId",
        client_token: "capo_codepipeline.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.get_third_party_job_details_output.GetThirdPartyJobDetailsOutput":
        """<p>Requests the details of a job for a third party action. Used for partner actions only.</p> <important> <p>When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.</p> </important>

        Args:
            job_id: <p>The unique system-generated ID used for identifying the job.</p>
            client_token: <p>The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.</p>

        Raises:
            capo_codepipeline.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The client token was specified in an invalid format</p>
            capo_codepipeline.errors.invalid_job_exception.InvalidJobException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.job_not_found_exception.JobNotFoundException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.get_third_party_job_details_input.GetThirdPartyJobDetailsInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.get_third_party_job_details_output.GetThirdPartyJobDetailsOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.get_third_party_job_details

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.get_third_party_job_details.async_get_third_party_job_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.get_third_party_job_details_input.GetThirdPartyJobDetailsInput = {
            "job_id": job_id,
            "client_token": client_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_action_executions(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        filter: Optional[
            "capo_codepipeline.types.action_execution_filter.ActionExecutionFilter"
        ] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
    ) -> "capo_codepipeline.types.list_action_executions_output.ListActionExecutionsOutput":
        """<p>Lists the action executions that have occurred in a pipeline.</p>

        Args:
            pipeline_name: <p> The name of the pipeline for which you want to list action execution history.</p>
            filter: <p>Input information used to filter action execution history.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Action execution history is retained for up to 12 months, based on action execution start times. Default value is 100. </p>
            next_token: <p>The token that was returned from the previous <code>ListActionExecutions</code> call, which can be used to return the next set of action executions in the list.</p>

        Raises:
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.pipeline_execution_not_found_exception.PipelineExecutionNotFoundException: <p>The pipeline execution was specified in an invalid format or cannot be found, or an execution ID does not belong to the specified pipeline. </p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_action_executions_input.ListActionExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_action_executions_output.ListActionExecutionsOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_action_executions

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_action_executions.async_list_action_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_action_executions_input.ListActionExecutionsInput = {
            "pipeline_name": pipeline_name
        }
        if filter is not None:
            input_["filter"] = filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_action_executions(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        filter: Optional[
            "capo_codepipeline.types.action_execution_filter.ActionExecutionFilter"
        ] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_codepipeline.types.action_execution_detail.ActionExecutionDetail]":
        _token = next_token
        while True:
            _response = await self.list_action_executions(
                pipeline_name,
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("action_execution_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_action_types(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        action_owner_filter: Optional[
            "capo_codepipeline.types.action_owner.ActionOwner"
        ] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
        region_filter: Optional[
            "capo_codepipeline.types.aws_region_name.AWSRegionName"
        ] = None,
    ) -> "capo_codepipeline.types.list_action_types_output.ListActionTypesOutput":
        """<p>Gets a summary of all CodePipeline action types associated with your account.</p>

        Args:
            action_owner_filter: <p>Filters the list of action types to those created by a specified entity.</p>
            next_token: <p>An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.</p>
            region_filter: <p>The Region to filter on for the list of action types.</p>

        Raises:
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_action_types_input.ListActionTypesInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_action_types_output.ListActionTypesOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_action_types

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_action_types.async_list_action_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_action_types_input.ListActionTypesInput = {}
        if action_owner_filter is not None:
            input_["action_owner_filter"] = action_owner_filter
        if next_token is not None:
            input_["next_token"] = next_token
        if region_filter is not None:
            input_["region_filter"] = region_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_action_types(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        action_owner_filter: Optional[
            "capo_codepipeline.types.action_owner.ActionOwner"
        ] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
        region_filter: Optional[
            "capo_codepipeline.types.aws_region_name.AWSRegionName"
        ] = None,
    ) -> "AsyncIterator[capo_codepipeline.types.action_type.ActionType]":
        _token = next_token
        while True:
            _response = await self.list_action_types(
                config_overrides=config_overrides,
                action_owner_filter=action_owner_filter,
                next_token=_token,
                region_filter=region_filter,
            )
            _page = _resolve_path(_response, ("action_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_deploy_action_execution_targets(
        self,
        action_execution_id: "capo_codepipeline.types.action_execution_id.ActionExecutionId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        pipeline_name: Optional[
            "capo_codepipeline.types.pipeline_name.PipelineName"
        ] = None,
        filters: Optional[
            "capo_codepipeline.types.target_filter_list.TargetFilterList"
        ] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
    ) -> "capo_codepipeline.types.list_deploy_action_execution_targets_output.ListDeployActionExecutionTargetsOutput":
        """<p>Lists the targets for the deploy action.</p>

        Args:
            pipeline_name: <p>The name of the pipeline with the deploy action.</p>
            action_execution_id: <p>The execution ID for the deploy action.</p>
            filters: <p>Filters the targets for a specified deploy action.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>
            next_token: <p>An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.</p>

        Raises:
            capo_codepipeline.errors.action_execution_not_found_exception.ActionExecutionNotFoundException: <p>The action execution was not found.</p>
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_deploy_action_execution_targets_input.ListDeployActionExecutionTargetsInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_deploy_action_execution_targets_output.ListDeployActionExecutionTargetsOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_deploy_action_execution_targets

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_deploy_action_execution_targets.async_list_deploy_action_execution_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_deploy_action_execution_targets_input.ListDeployActionExecutionTargetsInput = {
            "action_execution_id": action_execution_id
        }
        if pipeline_name is not None:
            input_["pipeline_name"] = pipeline_name
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_deploy_action_execution_targets(
        self,
        action_execution_id: "capo_codepipeline.types.action_execution_id.ActionExecutionId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        pipeline_name: Optional[
            "capo_codepipeline.types.pipeline_name.PipelineName"
        ] = None,
        filters: Optional[
            "capo_codepipeline.types.target_filter_list.TargetFilterList"
        ] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_codepipeline.types.deploy_action_execution_target.DeployActionExecutionTarget]":
        _token = next_token
        while True:
            _response = await self.list_deploy_action_execution_targets(
                action_execution_id,
                config_overrides=config_overrides,
                pipeline_name=pipeline_name,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pipeline_executions(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_codepipeline.types.pipeline_execution_filter.PipelineExecutionFilter"
        ] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
    ) -> "capo_codepipeline.types.list_pipeline_executions_output.ListPipelineExecutionsOutput":
        """<p>Gets a summary of the most recent executions for a pipeline.</p> <note> <p>When applying the filter for pipeline executions that have succeeded in the stage, the operation returns all executions in the current pipeline version beginning on February 1, 2024.</p> </note>

        Args:
            pipeline_name: <p>The name of the pipeline for which you want to get execution summary information.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.</p>
            filter: <p>The pipeline execution to filter on.</p>
            next_token: <p>The token that was returned from the previous <code>ListPipelineExecutions</code> call, which can be used to return the next set of pipeline executions in the list.</p>

        Raises:
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_pipeline_executions_input.ListPipelineExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_pipeline_executions_output.ListPipelineExecutionsOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_pipeline_executions

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_pipeline_executions.async_list_pipeline_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_pipeline_executions_input.ListPipelineExecutionsInput = {
            "pipeline_name": pipeline_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_pipeline_executions(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_codepipeline.types.pipeline_execution_filter.PipelineExecutionFilter"
        ] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_codepipeline.types.pipeline_execution_summary.PipelineExecutionSummary]":
        _token = next_token
        while True:
            _response = await self.list_pipeline_executions(
                pipeline_name,
                config_overrides=config_overrides,
                max_results=max_results,
                filter=filter,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pipeline_execution_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_codepipeline.types.max_pipelines.MaxPipelines"
        ] = None,
    ) -> "capo_codepipeline.types.list_pipelines_output.ListPipelinesOutput":
        """<p>Gets a summary of all of the pipelines associated with your account.</p>

        Args:
            next_token: <p>An identifier that was returned from the previous list pipelines call. It can be used to return the next set of pipelines in the list.</p>
            max_results: <p>The maximum number of pipelines to return in a single call. To retrieve the remaining pipelines, make another call with the returned nextToken value. The minimum value you can specify is 1. The maximum accepted value is 1000.</p>

        Raises:
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_pipelines_input.ListPipelinesInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_pipelines_output.ListPipelinesOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_pipelines

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_pipelines.async_list_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_pipelines_input.ListPipelinesInput = {}
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

    async def iter_list_pipelines(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_codepipeline.types.max_pipelines.MaxPipelines"
        ] = None,
    ) -> "AsyncIterator[capo_codepipeline.types.pipeline_summary.PipelineSummary]":
        _token = next_token
        while True:
            _response = await self.list_pipelines(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("pipelines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_rule_executions(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        filter: Optional[
            "capo_codepipeline.types.rule_execution_filter.RuleExecutionFilter"
        ] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
    ) -> "capo_codepipeline.types.list_rule_executions_output.ListRuleExecutionsOutput":
        """<p>Lists the rule executions that have occurred in a pipeline configured for conditions with rules.</p>

        Args:
            pipeline_name: <p>The name of the pipeline for which you want to get execution summary information.</p>
            filter: <p>Input information used to filter rule execution history.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.</p>
            next_token: <p>The token that was returned from the previous <code>ListRuleExecutions</code> call, which can be used to return the next set of rule executions in the list.</p>

        Raises:
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.pipeline_execution_not_found_exception.PipelineExecutionNotFoundException: <p>The pipeline execution was specified in an invalid format or cannot be found, or an execution ID does not belong to the specified pipeline. </p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_rule_executions_input.ListRuleExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_rule_executions_output.ListRuleExecutionsOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_rule_executions

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_rule_executions.async_list_rule_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_rule_executions_input.ListRuleExecutionsInput = {
            "pipeline_name": pipeline_name
        }
        if filter is not None:
            input_["filter"] = filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_rule_executions(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        filter: Optional[
            "capo_codepipeline.types.rule_execution_filter.RuleExecutionFilter"
        ] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_codepipeline.types.rule_execution_detail.RuleExecutionDetail]":
        _token = next_token
        while True:
            _response = await self.list_rule_executions(
                pipeline_name,
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rule_execution_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_rule_types(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        rule_owner_filter: Optional[
            "capo_codepipeline.types.rule_owner.RuleOwner"
        ] = None,
        region_filter: Optional[
            "capo_codepipeline.types.aws_region_name.AWSRegionName"
        ] = None,
    ) -> "capo_codepipeline.types.list_rule_types_output.ListRuleTypesOutput":
        """<p>Lists the rules for the condition. For more information about conditions, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html">Stage conditions</a> and <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html">How do stage conditions work?</a>.For more information about rules, see the <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html">CodePipeline rule reference</a>.</p>

        Args:
            rule_owner_filter: <p>The rule owner to filter on.</p>
            region_filter: <p>The rule Region to filter on.</p>

        Raises:
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_rule_types_input.ListRuleTypesInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_rule_types_output.ListRuleTypesOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_rule_types

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_rule_types.async_list_rule_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_rule_types_input.ListRuleTypesInput = {}
        if rule_owner_filter is not None:
            input_["rule_owner_filter"] = rule_owner_filter
        if region_filter is not None:
            input_["region_filter"] = region_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_codepipeline.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
    ) -> "capo_codepipeline.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Gets the set of key-value pairs (metadata) that are used to manage the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to get tags for.</p>
            next_token: <p>The token that was returned from the previous API call, which would be used to return the next page of the list. The ListTagsforResource call lists all available tags in one call and does not use pagination.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_codepipeline.errors.invalid_arn_exception.InvalidArnException: <p>The specified resource ARN is invalid.</p>
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was specified in an invalid format.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
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

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_codepipeline.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_codepipeline.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_webhooks(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
    ) -> "capo_codepipeline.types.list_webhooks_output.ListWebhooksOutput":
        """<p>Gets a listing of all the webhooks in this Amazon Web Services Region for this account. The output lists all webhooks and includes the webhook URL and ARN and the configuration for each webhook.</p> <note> <p>If a secret token was provided, it will be redacted in the response.</p> </note>

        Args:
            next_token: <p>The token that was returned from the previous ListWebhooks call, which can be used to return the next set of webhooks in the list.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>

        Raises:
            capo_codepipeline.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The next token was specified in an invalid format. Make sure that the next token you provide is the token returned by a previous call.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.list_webhooks_input.ListWebhooksInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.list_webhooks_output.ListWebhooksOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.list_webhooks

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.list_webhooks.async_list_webhooks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.list_webhooks_input.ListWebhooksInput = {}
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

    async def iter_list_webhooks(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        next_token: Optional["capo_codepipeline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_codepipeline.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_codepipeline.types.list_webhook_item.ListWebhookItem]":
        _token = next_token
        while True:
            _response = await self.list_webhooks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("webhooks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def override_stage_condition(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        stage_name: "capo_codepipeline.types.stage_name.StageName",
        pipeline_execution_id: "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId",
        condition_type: "capo_codepipeline.types.condition_type.ConditionType",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> None:
        """<p>Used to override a stage condition. For more information about conditions, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html">Stage conditions</a> and <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html">How do stage conditions work?</a>.</p>

        Args:
            pipeline_name: <p>The name of the pipeline with the stage that will override the condition.</p>
            stage_name: <p>The name of the stage for the override.</p>
            pipeline_execution_id: <p>The ID of the pipeline execution for the override.</p>
            condition_type: <p>The type of condition to override for the stage, such as entry conditions, failure conditions, or success conditions.</p>

        Raises:
            capo_codepipeline.errors.concurrent_pipeline_executions_limit_exceeded_exception.ConcurrentPipelineExecutionsLimitExceededException: <p>The pipeline has reached the limit for concurrent pipeline executions.</p>
            capo_codepipeline.errors.condition_not_overridable_exception.ConditionNotOverridableException: <p>Unable to override because the condition does not allow overrides.</p>
            capo_codepipeline.errors.conflict_exception.ConflictException: <p>Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.</p>
            capo_codepipeline.errors.not_latest_pipeline_execution_exception.NotLatestPipelineExecutionException: <p>The stage has failed in a later run of the pipeline and the <code>pipelineExecutionId</code> associated with the request is out of date.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.stage_not_found_exception.StageNotFoundException: <p>The stage was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.override_stage_condition_input.OverrideStageConditionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.override_stage_condition

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.override_stage_condition.async_override_stage_condition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.override_stage_condition_input.OverrideStageConditionInput = {
            "pipeline_name": pipeline_name,
            "stage_name": stage_name,
            "pipeline_execution_id": pipeline_execution_id,
            "condition_type": condition_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def poll_for_jobs(
        self,
        action_type_id: "capo_codepipeline.types.action_type_id.ActionTypeId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        max_batch_size: Optional[
            "capo_codepipeline.types.max_batch_size.MaxBatchSize"
        ] = None,
        query_param: Optional[
            "capo_codepipeline.types.query_param_map.QueryParamMap"
        ] = None,
    ) -> "capo_codepipeline.types.poll_for_jobs_output.PollForJobsOutput":
        """<p>Returns information about any jobs for CodePipeline to act on. <code>PollForJobs</code> is valid only for action types with "Custom" in the owner field. If the action type contains <code>AWS</code> or <code>ThirdParty</code> in the owner field, the <code>PollForJobs</code> action returns an error.</p> <important> <p>When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts. This API also returns any secret values defined for the action.</p> </important>

        Args:
            action_type_id: <p>Represents information about an action type.</p>
            max_batch_size: <p>The maximum number of jobs to return in a poll for jobs call.</p>
            query_param: <p>A map of property names and values. For an action type with no queryable properties, this value must be null or an empty map. For an action type with a queryable property, you must supply that property as a key in the map. Only jobs whose action configuration matches the mapped value are returned.</p>

        Raises:
            capo_codepipeline.errors.action_type_not_found_exception.ActionTypeNotFoundException: <p>The specified action type cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.poll_for_jobs_input.PollForJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.poll_for_jobs_output.PollForJobsOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.poll_for_jobs

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.poll_for_jobs.async_poll_for_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.poll_for_jobs_input.PollForJobsInput = {
            "action_type_id": action_type_id
        }
        if max_batch_size is not None:
            input_["max_batch_size"] = max_batch_size
        if query_param is not None:
            input_["query_param"] = query_param

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def poll_for_third_party_jobs(
        self,
        action_type_id: "capo_codepipeline.types.action_type_id.ActionTypeId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        max_batch_size: Optional[
            "capo_codepipeline.types.max_batch_size.MaxBatchSize"
        ] = None,
    ) -> "capo_codepipeline.types.poll_for_third_party_jobs_output.PollForThirdPartyJobsOutput":
        """<p>Determines whether there are any third party jobs for a job worker to act on. Used for partner actions only.</p> <important> <p>When this API is called, CodePipeline returns temporary credentials for the S3 bucket used to store artifacts for the pipeline, if the action requires access to that S3 bucket for input or output artifacts.</p> </important>

        Args:
            action_type_id: <p>Represents information about an action type.</p>
            max_batch_size: <p>The maximum number of jobs to return in a poll for jobs call.</p>

        Raises:
            capo_codepipeline.errors.action_type_not_found_exception.ActionTypeNotFoundException: <p>The specified action type cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.poll_for_third_party_jobs_input.PollForThirdPartyJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.poll_for_third_party_jobs_output.PollForThirdPartyJobsOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.poll_for_third_party_jobs

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.poll_for_third_party_jobs.async_poll_for_third_party_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.poll_for_third_party_jobs_input.PollForThirdPartyJobsInput = {
            "action_type_id": action_type_id
        }
        if max_batch_size is not None:
            input_["max_batch_size"] = max_batch_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_action_revision(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        stage_name: "capo_codepipeline.types.stage_name.StageName",
        action_name: "capo_codepipeline.types.action_name.ActionName",
        action_revision: "capo_codepipeline.types.action_revision.ActionRevision",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.put_action_revision_output.PutActionRevisionOutput":
        """<p>Provides information to CodePipeline about new revisions to a source.</p>

        Args:
            pipeline_name: <p>The name of the pipeline that starts processing the revision to the source.</p>
            stage_name: <p>The name of the stage that contains the action that acts on the revision.</p>
            action_name: <p>The name of the action that processes the revision.</p>
            action_revision: <p>Represents information about the version (or revision) of an action.</p>

        Raises:
            capo_codepipeline.errors.action_not_found_exception.ActionNotFoundException: <p>The specified action cannot be found.</p>
            capo_codepipeline.errors.concurrent_pipeline_executions_limit_exceeded_exception.ConcurrentPipelineExecutionsLimitExceededException: <p>The pipeline has reached the limit for concurrent pipeline executions.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.stage_not_found_exception.StageNotFoundException: <p>The stage was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.put_action_revision_input.PutActionRevisionInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.put_action_revision_output.PutActionRevisionOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.put_action_revision

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.put_action_revision.async_put_action_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.put_action_revision_input.PutActionRevisionInput = {
            "pipeline_name": pipeline_name,
            "stage_name": stage_name,
            "action_name": action_name,
            "action_revision": action_revision,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_approval_result(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        stage_name: "capo_codepipeline.types.stage_name.StageName",
        action_name: "capo_codepipeline.types.action_name.ActionName",
        result: "capo_codepipeline.types.approval_result.ApprovalResult",
        token: "capo_codepipeline.types.approval_token.ApprovalToken",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.put_approval_result_output.PutApprovalResultOutput":
        """<p>Provides the response to a manual approval request to CodePipeline. Valid responses include Approved and Rejected.</p>

        Args:
            pipeline_name: <p>The name of the pipeline that contains the action. </p>
            stage_name: <p>The name of the stage that contains the action.</p>
            action_name: <p>The name of the action for which approval is requested.</p>
            result: <p>Represents information about the result of the approval request.</p>
            token: <p>The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the <a>GetPipelineState</a> action. It is used to validate that the approval request corresponding to this token is still valid.</p> <important> <p>For a pipeline where the execution mode is set to PARALLEL, the token required to approve/reject an approval request as detailed above is not available. Instead, use the <code>externalExecutionId</code> in the response output from the <a>ListActionExecutions</a> action as the token in the approval request.</p> </important>

        Raises:
            capo_codepipeline.errors.action_not_found_exception.ActionNotFoundException: <p>The specified action cannot be found.</p>
            capo_codepipeline.errors.approval_already_completed_exception.ApprovalAlreadyCompletedException: <p>The approval action has already been approved or rejected.</p>
            capo_codepipeline.errors.invalid_approval_token_exception.InvalidApprovalTokenException: <p>The approval request already received a response or has expired.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.stage_not_found_exception.StageNotFoundException: <p>The stage was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.put_approval_result_input.PutApprovalResultInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.put_approval_result_output.PutApprovalResultOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.put_approval_result

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.put_approval_result.async_put_approval_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.put_approval_result_input.PutApprovalResultInput = {
            "pipeline_name": pipeline_name,
            "stage_name": stage_name,
            "action_name": action_name,
            "result": result,
            "token": token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_job_failure_result(
        self,
        job_id: "capo_codepipeline.types.job_id.JobId",
        failure_details: "capo_codepipeline.types.failure_details.FailureDetails",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> None:
        """<p>Represents the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.</p>

        Args:
            job_id: <p>The unique system-generated ID of the job that failed. This is the same ID returned from <code>PollForJobs</code>.</p>
            failure_details: <p>The details about the failure of a job.</p>

        Raises:
            capo_codepipeline.errors.invalid_job_state_exception.InvalidJobStateException: <p>The job state was specified in an invalid format.</p>
            capo_codepipeline.errors.job_not_found_exception.JobNotFoundException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.put_job_failure_result_input.PutJobFailureResultInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.put_job_failure_result

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.put_job_failure_result.async_put_job_failure_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.put_job_failure_result_input.PutJobFailureResultInput = {
            "job_id": job_id,
            "failure_details": failure_details,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_job_success_result(
        self,
        job_id: "capo_codepipeline.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        current_revision: Optional[
            "capo_codepipeline.types.current_revision.CurrentRevision"
        ] = None,
        continuation_token: Optional[
            "capo_codepipeline.types.continuation_token.ContinuationToken"
        ] = None,
        execution_details: Optional[
            "capo_codepipeline.types.execution_details.ExecutionDetails"
        ] = None,
        output_variables: Optional[
            "capo_codepipeline.types.output_variables_map.OutputVariablesMap"
        ] = None,
    ) -> None:
        """<p>Represents the success of a job as returned to the pipeline by a job worker. Used for custom actions only.</p>

        Args:
            job_id: <p>The unique system-generated ID of the job that succeeded. This is the same ID returned from <code>PollForJobs</code>.</p>
            current_revision: <p>The ID of the current revision of the artifact successfully worked on by the job.</p>
            continuation_token: <p>A token generated by a job worker, such as a CodeDeploy deployment ID, that a successful job provides to identify a custom action in progress. Future jobs use this token to identify the running instance of the action. It can be reused to return more information about the progress of the custom action. When the action is complete, no continuation token should be supplied.</p>
            execution_details: <p>The execution details of the successful job, such as the actions taken by the job worker.</p>
            output_variables: <p>Key-value pairs produced as output by a job worker that can be made available to a downstream action configuration. <code>outputVariables</code> can be included only when there is no continuation token on the request.</p>

        Raises:
            capo_codepipeline.errors.invalid_job_state_exception.InvalidJobStateException: <p>The job state was specified in an invalid format.</p>
            capo_codepipeline.errors.job_not_found_exception.JobNotFoundException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.output_variables_size_exceeded_exception.OutputVariablesSizeExceededException: <p>Exceeded the total size limit for all variables in the pipeline.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.put_job_success_result_input.PutJobSuccessResultInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.put_job_success_result

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.put_job_success_result.async_put_job_success_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.put_job_success_result_input.PutJobSuccessResultInput = {
            "job_id": job_id
        }
        if current_revision is not None:
            input_["current_revision"] = current_revision
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if execution_details is not None:
            input_["execution_details"] = execution_details
        if output_variables is not None:
            input_["output_variables"] = output_variables

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_third_party_job_failure_result(
        self,
        job_id: "capo_codepipeline.types.third_party_job_id.ThirdPartyJobId",
        client_token: "capo_codepipeline.types.client_token.ClientToken",
        failure_details: "capo_codepipeline.types.failure_details.FailureDetails",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> None:
        """<p>Represents the failure of a third party job as returned to the pipeline by a job worker. Used for partner actions only.</p>

        Args:
            job_id: <p>The ID of the job that failed. This is the same ID returned from <code>PollForThirdPartyJobs</code>.</p>
            client_token: <p>The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.</p>
            failure_details: <p>Represents information about failure details.</p>

        Raises:
            capo_codepipeline.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The client token was specified in an invalid format</p>
            capo_codepipeline.errors.invalid_job_state_exception.InvalidJobStateException: <p>The job state was specified in an invalid format.</p>
            capo_codepipeline.errors.job_not_found_exception.JobNotFoundException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.put_third_party_job_failure_result_input.PutThirdPartyJobFailureResultInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.put_third_party_job_failure_result

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.put_third_party_job_failure_result.async_put_third_party_job_failure_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.put_third_party_job_failure_result_input.PutThirdPartyJobFailureResultInput = {
            "job_id": job_id,
            "client_token": client_token,
            "failure_details": failure_details,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_third_party_job_success_result(
        self,
        job_id: "capo_codepipeline.types.third_party_job_id.ThirdPartyJobId",
        client_token: "capo_codepipeline.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        current_revision: Optional[
            "capo_codepipeline.types.current_revision.CurrentRevision"
        ] = None,
        continuation_token: Optional[
            "capo_codepipeline.types.continuation_token.ContinuationToken"
        ] = None,
        execution_details: Optional[
            "capo_codepipeline.types.execution_details.ExecutionDetails"
        ] = None,
    ) -> None:
        """<p>Represents the success of a third party job as returned to the pipeline by a job worker. Used for partner actions only.</p>

        Args:
            job_id: <p>The ID of the job that successfully completed. This is the same ID returned from <code>PollForThirdPartyJobs</code>.</p>
            client_token: <p>The clientToken portion of the clientId and clientToken pair used to verify that the calling entity is allowed access to the job and its details.</p>
            current_revision: <p>Represents information about a current revision.</p>
            continuation_token: <p>A token generated by a job worker, such as a CodeDeploy deployment ID, that a successful job provides to identify a partner action in progress. Future jobs use this token to identify the running instance of the action. It can be reused to return more information about the progress of the partner action. When the action is complete, no continuation token should be supplied.</p>
            execution_details: <p>The details of the actions taken and results produced on an artifact as it passes through stages in the pipeline. </p>

        Raises:
            capo_codepipeline.errors.invalid_client_token_exception.InvalidClientTokenException: <p>The client token was specified in an invalid format</p>
            capo_codepipeline.errors.invalid_job_state_exception.InvalidJobStateException: <p>The job state was specified in an invalid format.</p>
            capo_codepipeline.errors.job_not_found_exception.JobNotFoundException: <p>The job was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.put_third_party_job_success_result_input.PutThirdPartyJobSuccessResultInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.put_third_party_job_success_result

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.put_third_party_job_success_result.async_put_third_party_job_success_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.put_third_party_job_success_result_input.PutThirdPartyJobSuccessResultInput = {
            "job_id": job_id,
            "client_token": client_token,
        }
        if current_revision is not None:
            input_["current_revision"] = current_revision
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if execution_details is not None:
            input_["execution_details"] = execution_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_webhook(
        self,
        webhook: "capo_codepipeline.types.webhook_definition.WebhookDefinition",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        tags: Optional["capo_codepipeline.types.tag_list.TagList"] = None,
    ) -> "capo_codepipeline.types.put_webhook_output.PutWebhookOutput":
        """<p>Defines a webhook and returns a unique webhook URL generated by CodePipeline. This URL can be supplied to third party source hosting providers to call every time there's a code change. When CodePipeline receives a POST request on this URL, the pipeline defined in the webhook is started as long as the POST request satisfied the authentication and filtering requirements supplied when defining the webhook. RegisterWebhookWithThirdParty and DeregisterWebhookWithThirdParty APIs can be used to automatically configure supported third parties to call the generated webhook URL.</p> <important> <p>When creating CodePipeline webhooks, do not use your own credentials or reuse the same secret token across multiple webhooks. For optimal security, generate a unique secret token for each webhook you create. The secret token is an arbitrary string that you provide, which GitHub uses to compute and sign the webhook payloads sent to CodePipeline, for protecting the integrity and authenticity of the webhook payloads. Using your own credentials or reusing the same token across multiple webhooks can lead to security vulnerabilities.</p> </important> <note> <p>If a secret token was provided, it will be redacted in the response.</p> </note>

        Args:
            webhook: <p>The detail provided in an input file to create the webhook, such as the webhook name, the pipeline name, and the action name. Give the webhook a unique name that helps you identify it. You might name the webhook after the pipeline and action it targets so that you can easily recognize what it's used for later.</p>
            tags: <p>The tags for the webhook.</p>

        Raises:
            capo_codepipeline.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Unable to modify the tag due to a simultaneous update request.</p>
            capo_codepipeline.errors.invalid_tags_exception.InvalidTagsException: <p>The specified resource tags are invalid.</p>
            capo_codepipeline.errors.invalid_webhook_authentication_parameters_exception.InvalidWebhookAuthenticationParametersException: <p>The specified authentication type is in an invalid format.</p>
            capo_codepipeline.errors.invalid_webhook_filter_pattern_exception.InvalidWebhookFilterPatternException: <p>The specified event filter rule is in an invalid format.</p>
            capo_codepipeline.errors.limit_exceeded_exception.LimitExceededException: <p>The number of pipelines associated with the Amazon Web Services account has exceeded the limit allowed for the account.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.too_many_tags_exception.TooManyTagsException: <p>The tags limit for a resource has been exceeded.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.put_webhook_input.PutWebhookInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.put_webhook_output.PutWebhookOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.put_webhook

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.put_webhook.async_put_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.put_webhook_input.PutWebhookInput = {
            "webhook": webhook
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

    async def register_webhook_with_third_party(
        self,
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        webhook_name: Optional[
            "capo_codepipeline.types.webhook_name.WebhookName"
        ] = None,
    ) -> "capo_codepipeline.types.register_webhook_with_third_party_output.RegisterWebhookWithThirdPartyOutput":
        """<p>Configures a connection between the webhook that was created and the external tool with events to be detected.</p>

        Args:
            webhook_name: <p>The name of an existing webhook created with PutWebhook to register with a supported third party. </p>

        Raises:
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.webhook_not_found_exception.WebhookNotFoundException: <p>The specified webhook was entered in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.register_webhook_with_third_party_input.RegisterWebhookWithThirdPartyInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.register_webhook_with_third_party_output.RegisterWebhookWithThirdPartyOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.register_webhook_with_third_party

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.register_webhook_with_third_party.async_register_webhook_with_third_party(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.register_webhook_with_third_party_input.RegisterWebhookWithThirdPartyInput = {}
        if webhook_name is not None:
            input_["webhook_name"] = webhook_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retry_stage_execution(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        stage_name: "capo_codepipeline.types.stage_name.StageName",
        pipeline_execution_id: "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId",
        retry_mode: "capo_codepipeline.types.stage_retry_mode.StageRetryMode",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> (
        "capo_codepipeline.types.retry_stage_execution_output.RetryStageExecutionOutput"
    ):
        """<p>You can retry a stage that has failed without having to run a pipeline again from the beginning. You do this by either retrying the failed actions in a stage or by retrying all actions in the stage starting from the first action in the stage. When you retry the failed actions in a stage, all actions that are still in progress continue working, and failed actions are triggered again. When you retry a failed stage from the first action in the stage, the stage cannot have any actions in progress. Before a stage can be retried, it must either have all actions failed or some actions failed and some succeeded.</p>

        Args:
            pipeline_name: <p>The name of the pipeline that contains the failed stage.</p>
            stage_name: <p>The name of the failed stage to be retried.</p>
            pipeline_execution_id: <p>The ID of the pipeline execution in the failed stage to be retried. Use the <a>GetPipelineState</a> action to retrieve the current pipelineExecutionId of the failed stage</p>
            retry_mode: <p>The scope of the retry attempt.</p>

        Raises:
            capo_codepipeline.errors.concurrent_pipeline_executions_limit_exceeded_exception.ConcurrentPipelineExecutionsLimitExceededException: <p>The pipeline has reached the limit for concurrent pipeline executions.</p>
            capo_codepipeline.errors.conflict_exception.ConflictException: <p>Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.</p>
            capo_codepipeline.errors.not_latest_pipeline_execution_exception.NotLatestPipelineExecutionException: <p>The stage has failed in a later run of the pipeline and the <code>pipelineExecutionId</code> associated with the request is out of date.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.stage_not_found_exception.StageNotFoundException: <p>The stage was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.stage_not_retryable_exception.StageNotRetryableException: <p>Unable to retry. The pipeline structure or stage state might have changed while actions awaited retry, or the stage contains no failed actions.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.retry_stage_execution_input.RetryStageExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.retry_stage_execution_output.RetryStageExecutionOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.retry_stage_execution

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.retry_stage_execution.async_retry_stage_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.retry_stage_execution_input.RetryStageExecutionInput = {
            "pipeline_name": pipeline_name,
            "stage_name": stage_name,
            "pipeline_execution_id": pipeline_execution_id,
            "retry_mode": retry_mode,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rollback_stage(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        stage_name: "capo_codepipeline.types.stage_name.StageName",
        target_pipeline_execution_id: "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.rollback_stage_output.RollbackStageOutput":
        """<p>Rolls back a stage execution.</p>

        Args:
            pipeline_name: <p>The name of the pipeline for which the stage will be rolled back. </p>
            stage_name: <p>The name of the stage in the pipeline to be rolled back. </p>
            target_pipeline_execution_id: <p>The pipeline execution ID for the stage to be rolled back to. </p>

        Raises:
            capo_codepipeline.errors.conflict_exception.ConflictException: <p>Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.</p>
            capo_codepipeline.errors.pipeline_execution_not_found_exception.PipelineExecutionNotFoundException: <p>The pipeline execution was specified in an invalid format or cannot be found, or an execution ID does not belong to the specified pipeline. </p>
            capo_codepipeline.errors.pipeline_execution_outdated_exception.PipelineExecutionOutdatedException: <p>The specified pipeline execution is outdated and cannot be used as a target pipeline execution for rollback.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.stage_not_found_exception.StageNotFoundException: <p>The stage was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.unable_to_rollback_stage_exception.UnableToRollbackStageException: <p>Unable to roll back the stage. The cause might be if the pipeline version has changed since the target pipeline execution was deployed, the stage is currently running, or an incorrect target pipeline execution ID was provided.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.rollback_stage_input.RollbackStageInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.rollback_stage_output.RollbackStageOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.rollback_stage

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.rollback_stage.async_rollback_stage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.rollback_stage_input.RollbackStageInput = {
            "pipeline_name": pipeline_name,
            "stage_name": stage_name,
            "target_pipeline_execution_id": target_pipeline_execution_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_pipeline_execution(
        self,
        name: "capo_codepipeline.types.pipeline_name.PipelineName",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        variables: Optional[
            "capo_codepipeline.types.pipeline_variable_list.PipelineVariableList"
        ] = None,
        client_request_token: Optional[
            "capo_codepipeline.types.client_request_token.ClientRequestToken"
        ] = None,
        source_revisions: Optional[
            "capo_codepipeline.types.source_revision_override_list.SourceRevisionOverrideList"
        ] = None,
    ) -> "capo_codepipeline.types.start_pipeline_execution_output.StartPipelineExecutionOutput":
        r"""<p>Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.</p>

        Args:
            name: <p>The name of the pipeline to start.</p>
            variables: <p>A list that overrides pipeline variables for a pipeline execution that's being started. Variable names must match <code>[A-Za-z0-9@\-_]+</code>, and the values can be anything except an empty string.</p>
            client_request_token: <p>The system-generated unique ID used to identify a unique execution request.</p>
            source_revisions: <p>A list that allows you to specify, or override, the source revision for a pipeline execution that's being started. A source revision is the version with all the changes to your application code, or source artifact, for the pipeline execution.</p>

        Raises:
            capo_codepipeline.errors.concurrent_pipeline_executions_limit_exceeded_exception.ConcurrentPipelineExecutionsLimitExceededException: <p>The pipeline has reached the limit for concurrent pipeline executions.</p>
            capo_codepipeline.errors.conflict_exception.ConflictException: <p>Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.start_pipeline_execution_input.StartPipelineExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.start_pipeline_execution_output.StartPipelineExecutionOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.start_pipeline_execution

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.start_pipeline_execution.async_start_pipeline_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.start_pipeline_execution_input.StartPipelineExecutionInput = {
            "name": name
        }
        if variables is not None:
            input_["variables"] = variables
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if source_revisions is not None:
            input_["source_revisions"] = source_revisions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_pipeline_execution(
        self,
        pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName",
        pipeline_execution_id: "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
        abandon: Optional["capo_codepipeline.types.boolean.Boolean"] = None,
        reason: Optional[
            "capo_codepipeline.types.stop_pipeline_execution_reason.StopPipelineExecutionReason"
        ] = None,
    ) -> "capo_codepipeline.types.stop_pipeline_execution_output.StopPipelineExecutionOutput":
        """<p>Stops the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. While completing or abandoning in-progress actions, the pipeline execution is in a <code>Stopping</code> state. After all in-progress actions are completed or abandoned, the pipeline execution is in a <code>Stopped</code> state.</p>

        Args:
            pipeline_name: <p>The name of the pipeline to stop.</p>
            pipeline_execution_id: <p>The ID of the pipeline execution to be stopped in the current stage. Use the <code>GetPipelineState</code> action to retrieve the current pipelineExecutionId.</p>
            abandon: <p>Use this option to stop the pipeline execution by abandoning, rather than finishing, in-progress actions.</p> <note> <p>This option can lead to failed or out-of-sequence tasks.</p> </note>
            reason: <p>Use this option to enter comments, such as the reason the pipeline was stopped.</p>

        Raises:
            capo_codepipeline.errors.conflict_exception.ConflictException: <p>Your request cannot be handled because the pipeline is busy handling ongoing activities. Try again later.</p>
            capo_codepipeline.errors.duplicated_stop_request_exception.DuplicatedStopRequestException: <p>The pipeline execution is already in a <code>Stopping</code> state. If you already chose to stop and wait, you cannot make that request again. You can choose to stop and abandon now, but be aware that this option can lead to failed tasks or out of sequence tasks. If you already chose to stop and abandon, you cannot make that request again.</p>
            capo_codepipeline.errors.pipeline_execution_not_stoppable_exception.PipelineExecutionNotStoppableException: <p>Unable to stop the pipeline execution. The execution might already be in a <code>Stopped</code> state, or it might no longer be in progress.</p>
            capo_codepipeline.errors.pipeline_not_found_exception.PipelineNotFoundException: <p>The pipeline was specified in an invalid format or cannot be found.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.stop_pipeline_execution_input.StopPipelineExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.stop_pipeline_execution_output.StopPipelineExecutionOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.stop_pipeline_execution

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.stop_pipeline_execution.async_stop_pipeline_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.stop_pipeline_execution_input.StopPipelineExecutionInput = {
            "pipeline_name": pipeline_name,
            "pipeline_execution_id": pipeline_execution_id,
        }
        if abandon is not None:
            input_["abandon"] = abandon
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_codepipeline.types.resource_arn.ResourceArn",
        tags: "capo_codepipeline.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.tag_resource_output.TagResourceOutput":
        """<p>Adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource you want to add tags to.</p>
            tags: <p>The tags you want to modify or add to the resource.</p>

        Raises:
            capo_codepipeline.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Unable to modify the tag due to a simultaneous update request.</p>
            capo_codepipeline.errors.invalid_arn_exception.InvalidArnException: <p>The specified resource ARN is invalid.</p>
            capo_codepipeline.errors.invalid_tags_exception.InvalidTagsException: <p>The specified resource tags are invalid.</p>
            capo_codepipeline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was specified in an invalid format.</p>
            capo_codepipeline.errors.too_many_tags_exception.TooManyTagsException: <p>The tags limit for a resource has been exceeded.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.tag_resource

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_codepipeline.types.resource_arn.ResourceArn",
        tag_keys: "capo_codepipeline.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from an Amazon Web Services resource.</p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The list of keys for the tags to be removed from the resource.</p>

        Raises:
            capo_codepipeline.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Unable to modify the tag due to a simultaneous update request.</p>
            capo_codepipeline.errors.invalid_arn_exception.InvalidArnException: <p>The specified resource ARN is invalid.</p>
            capo_codepipeline.errors.invalid_tags_exception.InvalidTagsException: <p>The specified resource tags are invalid.</p>
            capo_codepipeline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was specified in an invalid format.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.untag_resource

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.untag_resource_input.UntagResourceInput = {
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

    async def update_action_type(
        self,
        action_type: "capo_codepipeline.types.action_type_declaration.ActionTypeDeclaration",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> None:
        """<p>Updates an action type that was created with any supported integration model, where the action type is to be used by customers of the action type provider. Use a JSON file with the action definition and <code>UpdateActionType</code> to provide the full structure.</p>

        Args:
            action_type: <p>The action type definition for the action type to be updated.</p>

        Raises:
            capo_codepipeline.errors.action_type_not_found_exception.ActionTypeNotFoundException: <p>The specified action type cannot be found.</p>
            capo_codepipeline.errors.request_failed_exception.RequestFailedException: <p>The request failed because of an unknown error, exception, or failure.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.update_action_type_input.UpdateActionTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_codepipeline._operations.code_pipeline_20150709.update_action_type

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.update_action_type.async_update_action_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.update_action_type_input.UpdateActionTypeInput = {
            "action_type": action_type
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_pipeline(
        self,
        pipeline: "capo_codepipeline.types.pipeline_declaration.PipelineDeclaration",
        *,
        config_overrides: Optional[AsyncCodePipelineClientConfig] = None,
    ) -> "capo_codepipeline.types.update_pipeline_output.UpdatePipelineOutput":
        """<p>Updates a specified pipeline with edits or changes to its structure. Use a JSON file with the pipeline structure and <code>UpdatePipeline</code> to provide the full structure of the pipeline. Updating the pipeline increases the version number of the pipeline by 1.</p>

        Args:
            pipeline: <p>The name of the pipeline to be updated.</p>

        Raises:
            capo_codepipeline.errors.invalid_action_declaration_exception.InvalidActionDeclarationException: <p>The action declaration was specified in an invalid format.</p>
            capo_codepipeline.errors.invalid_blocker_declaration_exception.InvalidBlockerDeclarationException: <p>Reserved for future use.</p>
            capo_codepipeline.errors.invalid_stage_declaration_exception.InvalidStageDeclarationException: <p>The stage declaration was specified in an invalid format.</p>
            capo_codepipeline.errors.invalid_structure_exception.InvalidStructureException: <p>The structure was specified in an invalid format.</p>
            capo_codepipeline.errors.limit_exceeded_exception.LimitExceededException: <p>The number of pipelines associated with the Amazon Web Services account has exceeded the limit allowed for the account.</p>
            capo_codepipeline.errors.validation_exception.ValidationException: <p>The validation was specified in an invalid format.</p>
            capo_codepipeline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codepipeline.types.update_pipeline_input.UpdatePipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_codepipeline.types.update_pipeline_output.UpdatePipelineOutput"
        ]:
            import capo_codepipeline._operations.code_pipeline_20150709.update_pipeline

            (
                output,
                http_response,
            ) = await capo_codepipeline._operations.code_pipeline_20150709.update_pipeline.async_update_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codepipeline.types.update_pipeline_input.UpdatePipelineInput = {
            "pipeline": pipeline
        }

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
