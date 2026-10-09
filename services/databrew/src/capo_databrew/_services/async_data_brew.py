"""Generated from Smithy shape ``com.amazonaws.databrew#AWSGlueDataBrew``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_databrew._auth._signers
import capo_databrew._auth._sigv4
from capo_databrew._auth._identity import Credentials
from capo_databrew._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_databrew._auth._zapros_handler import AuthMiddleware
from capo_databrew._pagination import resolve_path as _resolve_path
from capo_databrew._services._aws_config import aaws_config
from capo_databrew._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.assume_control
    import capo_databrew.types.batch_delete_recipe_version_request
    import capo_databrew.types.batch_delete_recipe_version_response
    import capo_databrew.types.client_session_id
    import capo_databrew.types.create_dataset_request
    import capo_databrew.types.create_dataset_response
    import capo_databrew.types.create_profile_job_request
    import capo_databrew.types.create_profile_job_response
    import capo_databrew.types.create_project_request
    import capo_databrew.types.create_project_response
    import capo_databrew.types.create_recipe_job_request
    import capo_databrew.types.create_recipe_job_response
    import capo_databrew.types.create_recipe_request
    import capo_databrew.types.create_recipe_response
    import capo_databrew.types.create_ruleset_request
    import capo_databrew.types.create_ruleset_response
    import capo_databrew.types.create_schedule_request
    import capo_databrew.types.create_schedule_response
    import capo_databrew.types.cron_expression
    import capo_databrew.types.data_catalog_output_list
    import capo_databrew.types.database_output_list
    import capo_databrew.types.dataset
    import capo_databrew.types.dataset_name
    import capo_databrew.types.delete_dataset_request
    import capo_databrew.types.delete_dataset_response
    import capo_databrew.types.delete_job_request
    import capo_databrew.types.delete_job_response
    import capo_databrew.types.delete_project_request
    import capo_databrew.types.delete_project_response
    import capo_databrew.types.delete_recipe_version_request
    import capo_databrew.types.delete_recipe_version_response
    import capo_databrew.types.delete_ruleset_request
    import capo_databrew.types.delete_ruleset_response
    import capo_databrew.types.delete_schedule_request
    import capo_databrew.types.delete_schedule_response
    import capo_databrew.types.describe_dataset_request
    import capo_databrew.types.describe_dataset_response
    import capo_databrew.types.describe_job_request
    import capo_databrew.types.describe_job_response
    import capo_databrew.types.describe_job_run_request
    import capo_databrew.types.describe_job_run_response
    import capo_databrew.types.describe_project_request
    import capo_databrew.types.describe_project_response
    import capo_databrew.types.describe_recipe_request
    import capo_databrew.types.describe_recipe_response
    import capo_databrew.types.describe_ruleset_request
    import capo_databrew.types.describe_ruleset_response
    import capo_databrew.types.describe_schedule_request
    import capo_databrew.types.describe_schedule_response
    import capo_databrew.types.encryption_key_arn
    import capo_databrew.types.encryption_mode
    import capo_databrew.types.format_options
    import capo_databrew.types.input
    import capo_databrew.types.input_format
    import capo_databrew.types.job
    import capo_databrew.types.job_name
    import capo_databrew.types.job_name_list
    import capo_databrew.types.job_run
    import capo_databrew.types.job_run_id
    import capo_databrew.types.job_sample
    import capo_databrew.types.list_datasets_request
    import capo_databrew.types.list_datasets_response
    import capo_databrew.types.list_job_runs_request
    import capo_databrew.types.list_job_runs_response
    import capo_databrew.types.list_jobs_request
    import capo_databrew.types.list_jobs_response
    import capo_databrew.types.list_projects_request
    import capo_databrew.types.list_projects_response
    import capo_databrew.types.list_recipe_versions_request
    import capo_databrew.types.list_recipe_versions_response
    import capo_databrew.types.list_recipes_request
    import capo_databrew.types.list_recipes_response
    import capo_databrew.types.list_rulesets_request
    import capo_databrew.types.list_rulesets_response
    import capo_databrew.types.list_schedules_request
    import capo_databrew.types.list_schedules_response
    import capo_databrew.types.list_tags_for_resource_request
    import capo_databrew.types.list_tags_for_resource_response
    import capo_databrew.types.log_subscription
    import capo_databrew.types.max_capacity
    import capo_databrew.types.max_results100
    import capo_databrew.types.max_retries
    import capo_databrew.types.next_token
    import capo_databrew.types.output_list
    import capo_databrew.types.path_options
    import capo_databrew.types.preview
    import capo_databrew.types.profile_configuration
    import capo_databrew.types.project
    import capo_databrew.types.project_name
    import capo_databrew.types.publish_recipe_request
    import capo_databrew.types.publish_recipe_response
    import capo_databrew.types.recipe
    import capo_databrew.types.recipe_description
    import capo_databrew.types.recipe_name
    import capo_databrew.types.recipe_reference
    import capo_databrew.types.recipe_step
    import capo_databrew.types.recipe_step_list
    import capo_databrew.types.recipe_version
    import capo_databrew.types.recipe_version_list
    import capo_databrew.types.rule_list
    import capo_databrew.types.ruleset_description
    import capo_databrew.types.ruleset_item
    import capo_databrew.types.ruleset_name
    import capo_databrew.types.s3_location
    import capo_databrew.types.sample
    import capo_databrew.types.schedule
    import capo_databrew.types.schedule_name
    import capo_databrew.types.send_project_session_action_request
    import capo_databrew.types.send_project_session_action_response
    import capo_databrew.types.start_job_run_request
    import capo_databrew.types.start_job_run_response
    import capo_databrew.types.start_project_session_request
    import capo_databrew.types.start_project_session_response
    import capo_databrew.types.step_index
    import capo_databrew.types.stop_job_run_request
    import capo_databrew.types.stop_job_run_response
    import capo_databrew.types.tag_key_list
    import capo_databrew.types.tag_map
    import capo_databrew.types.tag_resource_request
    import capo_databrew.types.tag_resource_response
    import capo_databrew.types.timeout
    import capo_databrew.types.untag_resource_request
    import capo_databrew.types.untag_resource_response
    import capo_databrew.types.update_dataset_request
    import capo_databrew.types.update_dataset_response
    import capo_databrew.types.update_profile_job_request
    import capo_databrew.types.update_profile_job_response
    import capo_databrew.types.update_project_request
    import capo_databrew.types.update_project_response
    import capo_databrew.types.update_recipe_job_request
    import capo_databrew.types.update_recipe_job_response
    import capo_databrew.types.update_recipe_request
    import capo_databrew.types.update_recipe_response
    import capo_databrew.types.update_ruleset_request
    import capo_databrew.types.update_ruleset_response
    import capo_databrew.types.update_schedule_request
    import capo_databrew.types.update_schedule_response
    import capo_databrew.types.validation_configuration_list
    import capo_databrew.types.view_frame


class AsyncDataBrewClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncDataBrewClient:
    """A client for the ``DataBrew`` service.

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
        self._config = AsyncDataBrewClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncDataBrewClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDataBrewClientConfig = config_overrides or {}
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

    async def batch_delete_recipe_version(
        self,
        name: "capo_databrew.types.recipe_name.RecipeName",
        recipe_versions: "capo_databrew.types.recipe_version_list.RecipeVersionList",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.batch_delete_recipe_version_response.BatchDeleteRecipeVersionResponse":
        """<p>Deletes one or more versions of a recipe at a time.</p> <p>The entire request will be rejected if:</p> <ul> <li> <p>The recipe does not exist.</p> </li> <li> <p>There is an invalid version identifier in the list of versions.</p> </li> <li> <p>The version list is empty.</p> </li> <li> <p>The version list size exceeds 50.</p> </li> <li> <p>The version list contains duplicate entries.</p> </li> </ul> <p>The request will complete successfully, but with partial failures, if:</p> <ul> <li> <p>A version does not exist.</p> </li> <li> <p>A version is being used by a job.</p> </li> <li> <p>You specify <code>LATEST_WORKING</code>, but it's being used by a project.</p> </li> <li> <p>The version fails to be deleted.</p> </li> </ul> <p>The <code>LATEST_WORKING</code> version will only be deleted if the recipe has no other versions. If you try to delete <code>LATEST_WORKING</code> while other versions exist (or if they can't be deleted), then <code>LATEST_WORKING</code> will be listed as partial failure in the response.</p>

        Args:
            name: <p>The name of the recipe whose versions are to be deleted.</p>
            recipe_versions: <p>An array of version identifiers, for the recipe versions to be deleted. You can specify numeric versions (<code>X.Y</code>) or <code>LATEST_WORKING</code>. <code>LATEST_PUBLISHED</code> is not supported.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.batch_delete_recipe_version_request.BatchDeleteRecipeVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.batch_delete_recipe_version_response.BatchDeleteRecipeVersionResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.batch_delete_recipe_version

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.batch_delete_recipe_version.async_batch_delete_recipe_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.batch_delete_recipe_version_request.BatchDeleteRecipeVersionRequest = {
            "name": name,
            "recipe_versions": recipe_versions,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_dataset(
        self,
        name: "capo_databrew.types.dataset_name.DatasetName",
        input: "capo_databrew.types.input.Input",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        format: Optional["capo_databrew.types.input_format.InputFormat"] = None,
        format_options: Optional[
            "capo_databrew.types.format_options.FormatOptions"
        ] = None,
        path_options: Optional["capo_databrew.types.path_options.PathOptions"] = None,
        tags: Optional["capo_databrew.types.tag_map.TagMap"] = None,
    ) -> "capo_databrew.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates a new DataBrew dataset.</p>

        Args:
            name: <p>The name of the dataset to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>
            format: <p>The file format of a dataset that is created from an Amazon S3 file or folder.</p>
            path_options: <p>A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.</p>
            tags: <p>Metadata tags to apply to this dataset.</p>

        Raises:
            capo_databrew.errors.access_denied_exception.AccessDeniedException: <p>Access to the specified resource was denied.</p>
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.create_dataset

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.create_dataset_request.CreateDatasetRequest = {
            "name": name,
            "input": input,
        }
        if format is not None:
            input_["format"] = format
        if format_options is not None:
            input_["format_options"] = format_options
        if path_options is not None:
            input_["path_options"] = path_options
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_profile_job(
        self,
        dataset_name: "capo_databrew.types.dataset_name.DatasetName",
        name: "capo_databrew.types.job_name.JobName",
        output_location: "capo_databrew.types.s3_location.S3Location",
        role_arn: "capo_databrew.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        encryption_key_arn: Optional[
            "capo_databrew.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        encryption_mode: Optional[
            "capo_databrew.types.encryption_mode.EncryptionMode"
        ] = None,
        log_subscription: Optional[
            "capo_databrew.types.log_subscription.LogSubscription"
        ] = None,
        max_capacity: Optional["capo_databrew.types.max_capacity.MaxCapacity"] = None,
        max_retries: Optional["capo_databrew.types.max_retries.MaxRetries"] = None,
        configuration: Optional[
            "capo_databrew.types.profile_configuration.ProfileConfiguration"
        ] = None,
        validation_configurations: Optional[
            "capo_databrew.types.validation_configuration_list.ValidationConfigurationList"
        ] = None,
        tags: Optional["capo_databrew.types.tag_map.TagMap"] = None,
        timeout: Optional["capo_databrew.types.timeout.Timeout"] = None,
        job_sample: Optional["capo_databrew.types.job_sample.JobSample"] = None,
    ) -> "capo_databrew.types.create_profile_job_response.CreateProfileJobResponse":
        """<p>Creates a new job to analyze a dataset and create its data profile.</p>

        Args:
            dataset_name: <p>The name of the dataset that this job is to act upon.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.</p>
            encryption_mode: <p>The encryption mode for the job, which can be one of the following:</p> <ul> <li> <p> <code>SSE-KMS</code> - <code>SSE-KMS</code> - Server-side encryption with KMS-managed keys.</p> </li> <li> <p> <code>SSE-S3</code> - Server-side encryption with keys managed by Amazon S3.</p> </li> </ul>
            name: <p>The name of the job to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>
            log_subscription: <p>Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.</p>
            max_capacity: <p>The maximum number of nodes that DataBrew can use when the job processes data.</p>
            max_retries: <p>The maximum number of times to retry the job after a job run fails.</p>
            configuration: <p>Configuration for profile jobs. Used to select columns, do evaluations, and override default parameters of evaluations. When configuration is null, the profile job will run with default settings.</p>
            validation_configurations: <p>List of validation configurations that are applied to the profile job.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.</p>
            tags: <p>Metadata tags to apply to this job.</p>
            timeout: <p>The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of <code>TIMEOUT</code>.</p>
            job_sample: <p>Sample configuration for profile jobs only. Determines the number of rows on which the profile job will be executed. If a JobSample value is not provided, the default value will be used. The default value is CUSTOM_ROWS for the mode parameter and 20000 for the size parameter.</p>

        Raises:
            capo_databrew.errors.access_denied_exception.AccessDeniedException: <p>Access to the specified resource was denied.</p>
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.create_profile_job_request.CreateProfileJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.create_profile_job_response.CreateProfileJobResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.create_profile_job

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.create_profile_job.async_create_profile_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.create_profile_job_request.CreateProfileJobRequest = {
            "dataset_name": dataset_name,
            "name": name,
            "output_location": output_location,
            "role_arn": role_arn,
        }
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if encryption_mode is not None:
            input_["encryption_mode"] = encryption_mode
        if log_subscription is not None:
            input_["log_subscription"] = log_subscription
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if max_retries is not None:
            input_["max_retries"] = max_retries
        if configuration is not None:
            input_["configuration"] = configuration
        if validation_configurations is not None:
            input_["validation_configurations"] = validation_configurations
        if tags is not None:
            input_["tags"] = tags
        if timeout is not None:
            input_["timeout"] = timeout
        if job_sample is not None:
            input_["job_sample"] = job_sample

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_project(
        self,
        dataset_name: "capo_databrew.types.dataset_name.DatasetName",
        name: "capo_databrew.types.project_name.ProjectName",
        recipe_name: "capo_databrew.types.recipe_name.RecipeName",
        role_arn: "capo_databrew.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        sample: Optional["capo_databrew.types.sample.Sample"] = None,
        tags: Optional["capo_databrew.types.tag_map.TagMap"] = None,
    ) -> "capo_databrew.types.create_project_response.CreateProjectResponse":
        """<p>Creates a new DataBrew project.</p>

        Args:
            dataset_name: <p>The name of an existing dataset to associate this project with.</p>
            name: <p>A unique name for the new project. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>
            recipe_name: <p>The name of an existing recipe to associate with the project.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed for this request.</p>
            tags: <p>Metadata tags to apply to this project.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.internal_server_exception.InternalServerException: <p>An internal service failure occurred.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.create_project_request.CreateProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.create_project_response.CreateProjectResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.create_project

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.create_project.async_create_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.create_project_request.CreateProjectRequest = {
            "dataset_name": dataset_name,
            "name": name,
            "recipe_name": recipe_name,
            "role_arn": role_arn,
        }
        if sample is not None:
            input_["sample"] = sample
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_recipe(
        self,
        name: "capo_databrew.types.recipe_name.RecipeName",
        steps: "capo_databrew.types.recipe_step_list.RecipeStepList",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        description: Optional[
            "capo_databrew.types.recipe_description.RecipeDescription"
        ] = None,
        tags: Optional["capo_databrew.types.tag_map.TagMap"] = None,
    ) -> "capo_databrew.types.create_recipe_response.CreateRecipeResponse":
        """<p>Creates a new DataBrew recipe.</p>

        Args:
            description: <p>A description for the recipe.</p>
            name: <p>A unique name for the recipe. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>
            steps: <p>An array containing the steps to be performed by the recipe. Each recipe step consists of one recipe action and (optionally) an array of condition expressions.</p>
            tags: <p>Metadata tags to apply to this recipe.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.create_recipe_request.CreateRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.create_recipe_response.CreateRecipeResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.create_recipe

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.create_recipe.async_create_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.create_recipe_request.CreateRecipeRequest = {
            "name": name,
            "steps": steps,
        }
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

    async def create_recipe_job(
        self,
        name: "capo_databrew.types.job_name.JobName",
        role_arn: "capo_databrew.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        dataset_name: Optional["capo_databrew.types.dataset_name.DatasetName"] = None,
        encryption_key_arn: Optional[
            "capo_databrew.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        encryption_mode: Optional[
            "capo_databrew.types.encryption_mode.EncryptionMode"
        ] = None,
        log_subscription: Optional[
            "capo_databrew.types.log_subscription.LogSubscription"
        ] = None,
        max_capacity: Optional["capo_databrew.types.max_capacity.MaxCapacity"] = None,
        max_retries: Optional["capo_databrew.types.max_retries.MaxRetries"] = None,
        outputs: Optional["capo_databrew.types.output_list.OutputList"] = None,
        data_catalog_outputs: Optional[
            "capo_databrew.types.data_catalog_output_list.DataCatalogOutputList"
        ] = None,
        database_outputs: Optional[
            "capo_databrew.types.database_output_list.DatabaseOutputList"
        ] = None,
        project_name: Optional["capo_databrew.types.project_name.ProjectName"] = None,
        recipe_reference: Optional[
            "capo_databrew.types.recipe_reference.RecipeReference"
        ] = None,
        tags: Optional["capo_databrew.types.tag_map.TagMap"] = None,
        timeout: Optional["capo_databrew.types.timeout.Timeout"] = None,
    ) -> "capo_databrew.types.create_recipe_job_response.CreateRecipeJobResponse":
        """<p>Creates a new job to transform input data, using steps defined in an existing Glue DataBrew recipe</p>

        Args:
            dataset_name: <p>The name of the dataset that this job processes.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.</p>
            encryption_mode: <p>The encryption mode for the job, which can be one of the following:</p> <ul> <li> <p> <code>SSE-KMS</code> - Server-side encryption with keys managed by KMS.</p> </li> <li> <p> <code>SSE-S3</code> - Server-side encryption with keys managed by Amazon S3.</p> </li> </ul>
            name: <p>A unique name for the job. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>
            log_subscription: <p>Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.</p>
            max_capacity: <p>The maximum number of nodes that DataBrew can consume when the job processes data.</p>
            max_retries: <p>The maximum number of times to retry the job after a job run fails.</p>
            outputs: <p>One or more artifacts that represent the output from running the job.</p>
            data_catalog_outputs: <p>One or more artifacts that represent the Glue Data Catalog output from running the job.</p>
            database_outputs: <p>Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write to. </p>
            project_name: <p>Either the name of an existing project, or a combination of a recipe and a dataset to associate with the recipe.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.</p>
            tags: <p>Metadata tags to apply to this job.</p>
            timeout: <p>The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of <code>TIMEOUT</code>.</p>

        Raises:
            capo_databrew.errors.access_denied_exception.AccessDeniedException: <p>Access to the specified resource was denied.</p>
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.create_recipe_job_request.CreateRecipeJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.create_recipe_job_response.CreateRecipeJobResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.create_recipe_job

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.create_recipe_job.async_create_recipe_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.create_recipe_job_request.CreateRecipeJobRequest = {
            "name": name,
            "role_arn": role_arn,
        }
        if dataset_name is not None:
            input_["dataset_name"] = dataset_name
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if encryption_mode is not None:
            input_["encryption_mode"] = encryption_mode
        if log_subscription is not None:
            input_["log_subscription"] = log_subscription
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if max_retries is not None:
            input_["max_retries"] = max_retries
        if outputs is not None:
            input_["outputs"] = outputs
        if data_catalog_outputs is not None:
            input_["data_catalog_outputs"] = data_catalog_outputs
        if database_outputs is not None:
            input_["database_outputs"] = database_outputs
        if project_name is not None:
            input_["project_name"] = project_name
        if recipe_reference is not None:
            input_["recipe_reference"] = recipe_reference
        if tags is not None:
            input_["tags"] = tags
        if timeout is not None:
            input_["timeout"] = timeout

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ruleset(
        self,
        name: "capo_databrew.types.ruleset_name.RulesetName",
        target_arn: "capo_databrew.types.arn.Arn",
        rules: "capo_databrew.types.rule_list.RuleList",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        description: Optional[
            "capo_databrew.types.ruleset_description.RulesetDescription"
        ] = None,
        tags: Optional["capo_databrew.types.tag_map.TagMap"] = None,
    ) -> "capo_databrew.types.create_ruleset_response.CreateRulesetResponse":
        """<p>Creates a new ruleset that can be used in a profile job to validate the data quality of a dataset.</p>

        Args:
            name: <p>The name of the ruleset to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>
            description: <p>The description of the ruleset.</p>
            target_arn: <p>The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.</p>
            rules: <p>A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.</p>
            tags: <p>Metadata tags to apply to the ruleset.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.create_ruleset_request.CreateRulesetRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.create_ruleset_response.CreateRulesetResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.create_ruleset

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.create_ruleset.async_create_ruleset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.create_ruleset_request.CreateRulesetRequest = {
            "name": name,
            "target_arn": target_arn,
            "rules": rules,
        }
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

    async def create_schedule(
        self,
        cron_expression: "capo_databrew.types.cron_expression.CronExpression",
        name: "capo_databrew.types.schedule_name.ScheduleName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        job_names: Optional["capo_databrew.types.job_name_list.JobNameList"] = None,
        tags: Optional["capo_databrew.types.tag_map.TagMap"] = None,
    ) -> "capo_databrew.types.create_schedule_response.CreateScheduleResponse":
        """<p>Creates a new schedule for one or more DataBrew jobs. Jobs can be run at a specific date and time, or at regular intervals.</p>

        Args:
            job_names: <p>The name or names of one or more jobs to be run.</p>
            cron_expression: <p>The date or dates and time or times when the jobs are to be run. For more information, see <a href="https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html">Cron expressions</a> in the <i>Glue DataBrew Developer Guide</i>.</p>
            tags: <p>Metadata tags to apply to this schedule.</p>
            name: <p>A unique name for the schedule. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.create_schedule_request.CreateScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.create_schedule_response.CreateScheduleResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.create_schedule

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.create_schedule.async_create_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.create_schedule_request.CreateScheduleRequest = {
            "cron_expression": cron_expression,
            "name": name,
        }
        if job_names is not None:
            input_["job_names"] = job_names
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_dataset(
        self,
        name: "capo_databrew.types.dataset_name.DatasetName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.delete_dataset_response.DeleteDatasetResponse":
        """<p>Deletes a dataset from DataBrew.</p>

        Args:
            name: <p>The name of the dataset to be deleted.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.delete_dataset_response.DeleteDatasetResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.delete_dataset

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.delete_dataset_request.DeleteDatasetRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_job(
        self,
        name: "capo_databrew.types.job_name.JobName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes the specified DataBrew job.</p>

        Args:
            name: <p>The name of the job to be deleted.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.delete_job_request.DeleteJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.delete_job_response.DeleteJobResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.delete_job

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.delete_job.async_delete_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.delete_job_request.DeleteJobRequest = {"name": name}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_project(
        self,
        name: "capo_databrew.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.delete_project_response.DeleteProjectResponse":
        """<p>Deletes an existing DataBrew project.</p>

        Args:
            name: <p>The name of the project to be deleted.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.delete_project_request.DeleteProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.delete_project_response.DeleteProjectResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.delete_project

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.delete_project.async_delete_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.delete_project_request.DeleteProjectRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_recipe_version(
        self,
        name: "capo_databrew.types.recipe_name.RecipeName",
        recipe_version: "capo_databrew.types.recipe_version.RecipeVersion",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> (
        "capo_databrew.types.delete_recipe_version_response.DeleteRecipeVersionResponse"
    ):
        """<p>Deletes a single version of a DataBrew recipe.</p>

        Args:
            name: <p>The name of the recipe.</p>
            recipe_version: <p>The version of the recipe to be deleted. You can specify a numeric versions (<code>X.Y</code>) or <code>LATEST_WORKING</code>. <code>LATEST_PUBLISHED</code> is not supported.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.delete_recipe_version_request.DeleteRecipeVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.delete_recipe_version_response.DeleteRecipeVersionResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.delete_recipe_version

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.delete_recipe_version.async_delete_recipe_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.delete_recipe_version_request.DeleteRecipeVersionRequest = {
            "name": name,
            "recipe_version": recipe_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ruleset(
        self,
        name: "capo_databrew.types.ruleset_name.RulesetName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.delete_ruleset_response.DeleteRulesetResponse":
        """<p>Deletes a ruleset.</p>

        Args:
            name: <p>The name of the ruleset to be deleted.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.delete_ruleset_request.DeleteRulesetRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.delete_ruleset_response.DeleteRulesetResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.delete_ruleset

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.delete_ruleset.async_delete_ruleset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.delete_ruleset_request.DeleteRulesetRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_schedule(
        self,
        name: "capo_databrew.types.schedule_name.ScheduleName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.delete_schedule_response.DeleteScheduleResponse":
        """<p>Deletes the specified DataBrew schedule.</p>

        Args:
            name: <p>The name of the schedule to be deleted.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.delete_schedule_request.DeleteScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.delete_schedule_response.DeleteScheduleResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.delete_schedule

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.delete_schedule.async_delete_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.delete_schedule_request.DeleteScheduleRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset(
        self,
        name: "capo_databrew.types.dataset_name.DatasetName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.describe_dataset_response.DescribeDatasetResponse":
        """<p>Returns the definition of a specific DataBrew dataset.</p>

        Args:
            name: <p>The name of the dataset to be described.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.describe_dataset

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.describe_dataset.async_describe_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.describe_dataset_request.DescribeDatasetRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_job(
        self,
        name: "capo_databrew.types.job_name.JobName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.describe_job_response.DescribeJobResponse":
        """<p>Returns the definition of a specific DataBrew job.</p>

        Args:
            name: <p>The name of the job to be described.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.describe_job_request.DescribeJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.describe_job_response.DescribeJobResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.describe_job

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.describe_job.async_describe_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.describe_job_request.DescribeJobRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_job_run(
        self,
        name: "capo_databrew.types.job_name.JobName",
        run_id: "capo_databrew.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.describe_job_run_response.DescribeJobRunResponse":
        """<p>Represents one run of a DataBrew job.</p>

        Args:
            name: <p>The name of the job being processed during this run.</p>
            run_id: <p>The unique identifier of the job run.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.describe_job_run_request.DescribeJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.describe_job_run_response.DescribeJobRunResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.describe_job_run

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.describe_job_run.async_describe_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.describe_job_run_request.DescribeJobRunRequest = {
            "name": name,
            "run_id": run_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_project(
        self,
        name: "capo_databrew.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.describe_project_response.DescribeProjectResponse":
        """<p>Returns the definition of a specific DataBrew project.</p>

        Args:
            name: <p>The name of the project to be described.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.describe_project_request.DescribeProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.describe_project_response.DescribeProjectResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.describe_project

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.describe_project.async_describe_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.describe_project_request.DescribeProjectRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_recipe(
        self,
        name: "capo_databrew.types.recipe_name.RecipeName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        recipe_version: Optional[
            "capo_databrew.types.recipe_version.RecipeVersion"
        ] = None,
    ) -> "capo_databrew.types.describe_recipe_response.DescribeRecipeResponse":
        """<p>Returns the definition of a specific DataBrew recipe corresponding to a particular version.</p>

        Args:
            name: <p>The name of the recipe to be described.</p>
            recipe_version: <p>The recipe version identifier. If this parameter isn't specified, then the latest published version is returned.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.describe_recipe_request.DescribeRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.describe_recipe_response.DescribeRecipeResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.describe_recipe

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.describe_recipe.async_describe_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.describe_recipe_request.DescribeRecipeRequest = {
            "name": name
        }
        if recipe_version is not None:
            input_["recipe_version"] = recipe_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_ruleset(
        self,
        name: "capo_databrew.types.ruleset_name.RulesetName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.describe_ruleset_response.DescribeRulesetResponse":
        """<p>Retrieves detailed information about the ruleset.</p>

        Args:
            name: <p>The name of the ruleset to be described.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.describe_ruleset_request.DescribeRulesetRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.describe_ruleset_response.DescribeRulesetResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.describe_ruleset

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.describe_ruleset.async_describe_ruleset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.describe_ruleset_request.DescribeRulesetRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_schedule(
        self,
        name: "capo_databrew.types.schedule_name.ScheduleName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.describe_schedule_response.DescribeScheduleResponse":
        """<p>Returns the definition of a specific DataBrew schedule.</p>

        Args:
            name: <p>The name of the schedule to be described.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.describe_schedule_request.DescribeScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.describe_schedule_response.DescribeScheduleResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.describe_schedule

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.describe_schedule.async_describe_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.describe_schedule_request.DescribeScheduleRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "capo_databrew.types.list_datasets_response.ListDatasetsResponse":
        """<p>Lists all of the DataBrew datasets.</p>

        Args:
            max_results: <p>The maximum number of results to return in this request. </p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>

        Raises:
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_datasets

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_datasets_request.ListDatasetsRequest = {}
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

    async def iter_list_datasets(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_databrew.types.dataset.Dataset]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("datasets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_job_runs(
        self,
        name: "capo_databrew.types.job_name.JobName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "capo_databrew.types.list_job_runs_response.ListJobRunsResponse":
        """<p>Lists all of the previous runs of a particular DataBrew job.</p>

        Args:
            name: <p>The name of the job.</p>
            max_results: <p>The maximum number of results to return in this request. </p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_job_runs_request.ListJobRunsRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_job_runs_response.ListJobRunsResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_job_runs

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_job_runs.async_list_job_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_job_runs_request.ListJobRunsRequest = {
            "name": name
        }
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

    async def iter_list_job_runs(
        self,
        name: "capo_databrew.types.job_name.JobName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_databrew.types.job_run.JobRun]":
        _token = next_token
        while True:
            _response = await self.list_job_runs(
                name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_jobs(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        dataset_name: Optional["capo_databrew.types.dataset_name.DatasetName"] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
        project_name: Optional["capo_databrew.types.project_name.ProjectName"] = None,
    ) -> "capo_databrew.types.list_jobs_response.ListJobsResponse":
        """<p>Lists all of the DataBrew jobs that are defined.</p>

        Args:
            dataset_name: <p>The name of a dataset. Using this parameter indicates to return only those jobs that act on the specified dataset.</p>
            max_results: <p>The maximum number of results to return in this request. </p>
            next_token: <p>A token generated by DataBrew that specifies where to continue pagination if a previous request was truncated. To get the next set of pages, pass in the NextToken value from the response object of the previous page call. </p>
            project_name: <p>The name of a project. Using this parameter indicates to return only those jobs that are associated with the specified project.</p>

        Raises:
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_jobs_request.ListJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_jobs_response.ListJobsResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_jobs

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_jobs.async_list_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_jobs_request.ListJobsRequest = {}
        if dataset_name is not None:
            input_["dataset_name"] = dataset_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if project_name is not None:
            input_["project_name"] = project_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_jobs(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        dataset_name: Optional["capo_databrew.types.dataset_name.DatasetName"] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
        project_name: Optional["capo_databrew.types.project_name.ProjectName"] = None,
    ) -> "AsyncIterator[capo_databrew.types.job.Job]":
        _token = next_token
        while True:
            _response = await self.list_jobs(
                config_overrides=config_overrides,
                dataset_name=dataset_name,
                max_results=max_results,
                next_token=_token,
                project_name=project_name,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_projects(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
    ) -> "capo_databrew.types.list_projects_response.ListProjectsResponse":
        """<p>Lists all of the DataBrew projects that are defined.</p>

        Args:
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return in this request. </p>

        Raises:
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_projects_request.ListProjectsRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_projects_response.ListProjectsResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_projects

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_projects.async_list_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_projects_request.ListProjectsRequest = {}
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

    async def iter_list_projects(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
    ) -> "AsyncIterator[capo_databrew.types.project.Project]":
        _token = next_token
        while True:
            _response = await self.list_projects(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("projects",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recipes(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
        recipe_version: Optional[
            "capo_databrew.types.recipe_version.RecipeVersion"
        ] = None,
    ) -> "capo_databrew.types.list_recipes_response.ListRecipesResponse":
        """<p>Lists all of the DataBrew recipes that are defined.</p>

        Args:
            max_results: <p>The maximum number of results to return in this request. </p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            recipe_version: <p>Return only those recipes with a version identifier of <code>LATEST_WORKING</code> or <code>LATEST_PUBLISHED</code>. If <code>RecipeVersion</code> is omitted, <code>ListRecipes</code> returns all of the <code>LATEST_PUBLISHED</code> recipe versions.</p> <p>Valid values: <code>LATEST_WORKING</code> | <code>LATEST_PUBLISHED</code> </p>

        Raises:
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_recipes_request.ListRecipesRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_recipes_response.ListRecipesResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_recipes

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_recipes.async_list_recipes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_recipes_request.ListRecipesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if recipe_version is not None:
            input_["recipe_version"] = recipe_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recipes(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
        recipe_version: Optional[
            "capo_databrew.types.recipe_version.RecipeVersion"
        ] = None,
    ) -> "AsyncIterator[capo_databrew.types.recipe.Recipe]":
        _token = next_token
        while True:
            _response = await self.list_recipes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                recipe_version=recipe_version,
            )
            _page = _resolve_path(_response, ("recipes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recipe_versions(
        self,
        name: "capo_databrew.types.recipe_name.RecipeName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "capo_databrew.types.list_recipe_versions_response.ListRecipeVersionsResponse":
        """<p>Lists the versions of a particular DataBrew recipe, except for <code>LATEST_WORKING</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in this request. </p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>
            name: <p>The name of the recipe for which to return version information.</p>

        Raises:
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_recipe_versions_request.ListRecipeVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_recipe_versions_response.ListRecipeVersionsResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_recipe_versions

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_recipe_versions.async_list_recipe_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_recipe_versions_request.ListRecipeVersionsRequest = {
            "name": name
        }
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

    async def iter_list_recipe_versions(
        self,
        name: "capo_databrew.types.recipe_name.RecipeName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_databrew.types.recipe.Recipe]":
        _token = next_token
        while True:
            _response = await self.list_recipe_versions(
                name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recipes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_rulesets(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        target_arn: Optional["capo_databrew.types.arn.Arn"] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "capo_databrew.types.list_rulesets_response.ListRulesetsResponse":
        """<p>List all rulesets available in the current account or rulesets associated with a specific resource (dataset).</p>

        Args:
            target_arn: <p>The Amazon Resource Name (ARN) of a resource (dataset). Using this parameter indicates to return only those rulesets that are associated with the specified resource.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p>A token generated by DataBrew that specifies where to continue pagination if a previous request was truncated. To get the next set of pages, pass in the NextToken value from the response object of the previous page call.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_rulesets_request.ListRulesetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_rulesets_response.ListRulesetsResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_rulesets

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_rulesets.async_list_rulesets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_rulesets_request.ListRulesetsRequest = {}
        if target_arn is not None:
            input_["target_arn"] = target_arn
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

    async def iter_list_rulesets(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        target_arn: Optional["capo_databrew.types.arn.Arn"] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_databrew.types.ruleset_item.RulesetItem]":
        _token = next_token
        while True:
            _response = await self.list_rulesets(
                config_overrides=config_overrides,
                target_arn=target_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rulesets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_schedules(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        job_name: Optional["capo_databrew.types.job_name.JobName"] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "capo_databrew.types.list_schedules_response.ListSchedulesResponse":
        """<p>Lists the DataBrew schedules that are defined.</p>

        Args:
            job_name: <p>The name of the job that these schedules apply to.</p>
            max_results: <p>The maximum number of results to return in this request. </p>
            next_token: <p>The token returned by a previous call to retrieve the next set of results.</p>

        Raises:
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_schedules_request.ListSchedulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_schedules_response.ListSchedulesResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_schedules

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_schedules.async_list_schedules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_schedules_request.ListSchedulesRequest = {}
        if job_name is not None:
            input_["job_name"] = job_name
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

    async def iter_list_schedules(
        self,
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        job_name: Optional["capo_databrew.types.job_name.JobName"] = None,
        max_results: Optional[
            "capo_databrew.types.max_results100.MaxResults100"
        ] = None,
        next_token: Optional["capo_databrew.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_databrew.types.schedule.Schedule]":
        _token = next_token
        while True:
            _response = await self.list_schedules(
                config_overrides=config_overrides,
                job_name=job_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schedules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_databrew.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all the tags for a DataBrew resource. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the DataBrew resource. </p>

        Raises:
            capo_databrew.errors.internal_server_exception.InternalServerException: <p>An internal service failure occurred.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def publish_recipe(
        self,
        name: "capo_databrew.types.recipe_name.RecipeName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        description: Optional[
            "capo_databrew.types.recipe_description.RecipeDescription"
        ] = None,
    ) -> "capo_databrew.types.publish_recipe_response.PublishRecipeResponse":
        """<p>Publishes a new version of a DataBrew recipe.</p>

        Args:
            description: <p>A description of the recipe to be published, for this version of the recipe.</p>
            name: <p>The name of the recipe to be published.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.publish_recipe_request.PublishRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.publish_recipe_response.PublishRecipeResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.publish_recipe

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.publish_recipe.async_publish_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.publish_recipe_request.PublishRecipeRequest = {
            "name": name
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

    async def send_project_session_action(
        self,
        name: "capo_databrew.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        preview: Optional["capo_databrew.types.preview.Preview"] = None,
        recipe_step: Optional["capo_databrew.types.recipe_step.RecipeStep"] = None,
        step_index: Optional["capo_databrew.types.step_index.StepIndex"] = None,
        client_session_id: Optional[
            "capo_databrew.types.client_session_id.ClientSessionId"
        ] = None,
        view_frame: Optional["capo_databrew.types.view_frame.ViewFrame"] = None,
    ) -> "capo_databrew.types.send_project_session_action_response.SendProjectSessionActionResponse":
        """<p>Performs a recipe step within an interactive DataBrew session that's currently open.</p>

        Args:
            preview: <p>If true, the result of the recipe step will be returned, but not applied.</p>
            name: <p>The name of the project to apply the action to.</p>
            step_index: <p>The index from which to preview a step. This index is used to preview the result of steps that have already been applied, so that the resulting view frame is from earlier in the view frame stack.</p>
            client_session_id: <p>A unique identifier for an interactive session that's currently open and ready for work. The action will be performed on this session.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.send_project_session_action_request.SendProjectSessionActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.send_project_session_action_response.SendProjectSessionActionResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.send_project_session_action

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.send_project_session_action.async_send_project_session_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.send_project_session_action_request.SendProjectSessionActionRequest = {
            "name": name
        }
        if preview is not None:
            input_["preview"] = preview
        if recipe_step is not None:
            input_["recipe_step"] = recipe_step
        if step_index is not None:
            input_["step_index"] = step_index
        if client_session_id is not None:
            input_["client_session_id"] = client_session_id
        if view_frame is not None:
            input_["view_frame"] = view_frame

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_job_run(
        self,
        name: "capo_databrew.types.job_name.JobName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.start_job_run_response.StartJobRunResponse":
        """<p>Runs a DataBrew job.</p>

        Args:
            name: <p>The name of the job to be run.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.start_job_run_request.StartJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.start_job_run_response.StartJobRunResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.start_job_run

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.start_job_run.async_start_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.start_job_run_request.StartJobRunRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_project_session(
        self,
        name: "capo_databrew.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        assume_control: Optional[
            "capo_databrew.types.assume_control.AssumeControl"
        ] = None,
    ) -> (
        "capo_databrew.types.start_project_session_response.StartProjectSessionResponse"
    ):
        """<p>Creates an interactive session, enabling you to manipulate data in a DataBrew project.</p>

        Args:
            name: <p>The name of the project to act upon.</p>
            assume_control: <p>A value that, if true, enables you to take control of a session, even if a different client is currently accessing the project.</p>

        Raises:
            capo_databrew.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.start_project_session_request.StartProjectSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.start_project_session_response.StartProjectSessionResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.start_project_session

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.start_project_session.async_start_project_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.start_project_session_request.StartProjectSessionRequest = {
            "name": name
        }
        if assume_control is not None:
            input_["assume_control"] = assume_control

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_job_run(
        self,
        name: "capo_databrew.types.job_name.JobName",
        run_id: "capo_databrew.types.job_run_id.JobRunId",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.stop_job_run_response.StopJobRunResponse":
        """<p>Stops a particular run of a job.</p>

        Args:
            name: <p>The name of the job to be stopped.</p>
            run_id: <p>The ID of the job run to be stopped.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.stop_job_run_request.StopJobRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.stop_job_run_response.StopJobRunResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.stop_job_run

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.stop_job_run.async_stop_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.stop_job_run_request.StopJobRunRequest = {
            "name": name,
            "run_id": run_id,
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
        resource_arn: "capo_databrew.types.arn.Arn",
        tags: "capo_databrew.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.tag_resource_response.TagResourceResponse":
        """<p>Adds metadata tags to a DataBrew resource, such as a dataset, project, recipe, job, or schedule.</p>

        Args:
            resource_arn: <p>The DataBrew resource to which tags should be added. The value for this parameter is an Amazon Resource Name (ARN). For DataBrew, you can tag a dataset, a job, a project, or a recipe.</p>
            tags: <p>One or more tags to be assigned to the resource.</p>

        Raises:
            capo_databrew.errors.internal_server_exception.InternalServerException: <p>An internal service failure occurred.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.tag_resource

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_databrew.types.arn.Arn",
        tag_keys: "capo_databrew.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
    ) -> "capo_databrew.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes metadata tags from a DataBrew resource.</p>

        Args:
            resource_arn: <p>A DataBrew resource from which you want to remove a tag or tags. The value for this parameter is an Amazon Resource Name (ARN). </p>
            tag_keys: <p>The tag keys (names) of one or more tags to be removed.</p>

        Raises:
            capo_databrew.errors.internal_server_exception.InternalServerException: <p>An internal service failure occurred.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.untag_resource

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_dataset(
        self,
        name: "capo_databrew.types.dataset_name.DatasetName",
        input: "capo_databrew.types.input.Input",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        format: Optional["capo_databrew.types.input_format.InputFormat"] = None,
        format_options: Optional[
            "capo_databrew.types.format_options.FormatOptions"
        ] = None,
        path_options: Optional["capo_databrew.types.path_options.PathOptions"] = None,
    ) -> "capo_databrew.types.update_dataset_response.UpdateDatasetResponse":
        """<p>Modifies the definition of an existing DataBrew dataset.</p>

        Args:
            name: <p>The name of the dataset to be updated.</p>
            format: <p>The file format of a dataset that is created from an Amazon S3 file or folder.</p>
            path_options: <p>A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.</p>

        Raises:
            capo_databrew.errors.access_denied_exception.AccessDeniedException: <p>Access to the specified resource was denied.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.update_dataset_request.UpdateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.update_dataset_response.UpdateDatasetResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.update_dataset

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.update_dataset.async_update_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.update_dataset_request.UpdateDatasetRequest = {
            "name": name,
            "input": input,
        }
        if format is not None:
            input_["format"] = format
        if format_options is not None:
            input_["format_options"] = format_options
        if path_options is not None:
            input_["path_options"] = path_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_profile_job(
        self,
        name: "capo_databrew.types.job_name.JobName",
        output_location: "capo_databrew.types.s3_location.S3Location",
        role_arn: "capo_databrew.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        configuration: Optional[
            "capo_databrew.types.profile_configuration.ProfileConfiguration"
        ] = None,
        encryption_key_arn: Optional[
            "capo_databrew.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        encryption_mode: Optional[
            "capo_databrew.types.encryption_mode.EncryptionMode"
        ] = None,
        log_subscription: Optional[
            "capo_databrew.types.log_subscription.LogSubscription"
        ] = None,
        max_capacity: Optional["capo_databrew.types.max_capacity.MaxCapacity"] = None,
        max_retries: Optional["capo_databrew.types.max_retries.MaxRetries"] = None,
        validation_configurations: Optional[
            "capo_databrew.types.validation_configuration_list.ValidationConfigurationList"
        ] = None,
        timeout: Optional["capo_databrew.types.timeout.Timeout"] = None,
        job_sample: Optional["capo_databrew.types.job_sample.JobSample"] = None,
    ) -> "capo_databrew.types.update_profile_job_response.UpdateProfileJobResponse":
        """<p>Modifies the definition of an existing profile job.</p>

        Args:
            configuration: <p>Configuration for profile jobs. Used to select columns, do evaluations, and override default parameters of evaluations. When configuration is null, the profile job will run with default settings.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.</p>
            encryption_mode: <p>The encryption mode for the job, which can be one of the following:</p> <ul> <li> <p> <code>SSE-KMS</code> - Server-side encryption with keys managed by KMS.</p> </li> <li> <p> <code>SSE-S3</code> - Server-side encryption with keys managed by Amazon S3.</p> </li> </ul>
            name: <p>The name of the job to be updated.</p>
            log_subscription: <p>Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.</p>
            max_capacity: <p>The maximum number of compute nodes that DataBrew can use when the job processes data.</p>
            max_retries: <p>The maximum number of times to retry the job after a job run fails.</p>
            validation_configurations: <p>List of validation configurations that are applied to the profile job.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.</p>
            timeout: <p>The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of <code>TIMEOUT</code>.</p>
            job_sample: <p>Sample configuration for Profile Jobs only. Determines the number of rows on which the Profile job will be executed. If a JobSample value is not provided for profile jobs, the default value will be used. The default value is CUSTOM_ROWS for the mode parameter and 20000 for the size parameter.</p>

        Raises:
            capo_databrew.errors.access_denied_exception.AccessDeniedException: <p>Access to the specified resource was denied.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.update_profile_job_request.UpdateProfileJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.update_profile_job_response.UpdateProfileJobResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.update_profile_job

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.update_profile_job.async_update_profile_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.update_profile_job_request.UpdateProfileJobRequest = {
            "name": name,
            "output_location": output_location,
            "role_arn": role_arn,
        }
        if configuration is not None:
            input_["configuration"] = configuration
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if encryption_mode is not None:
            input_["encryption_mode"] = encryption_mode
        if log_subscription is not None:
            input_["log_subscription"] = log_subscription
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if max_retries is not None:
            input_["max_retries"] = max_retries
        if validation_configurations is not None:
            input_["validation_configurations"] = validation_configurations
        if timeout is not None:
            input_["timeout"] = timeout
        if job_sample is not None:
            input_["job_sample"] = job_sample

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_project(
        self,
        role_arn: "capo_databrew.types.arn.Arn",
        name: "capo_databrew.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        sample: Optional["capo_databrew.types.sample.Sample"] = None,
    ) -> "capo_databrew.types.update_project_response.UpdateProjectResponse":
        """<p>Modifies the definition of an existing DataBrew project.</p>

        Args:
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to be assumed for this request.</p>
            name: <p>The name of the project to be updated.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.update_project_request.UpdateProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.update_project_response.UpdateProjectResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.update_project

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.update_project.async_update_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.update_project_request.UpdateProjectRequest = {
            "role_arn": role_arn,
            "name": name,
        }
        if sample is not None:
            input_["sample"] = sample

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_recipe(
        self,
        name: "capo_databrew.types.recipe_name.RecipeName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        description: Optional[
            "capo_databrew.types.recipe_description.RecipeDescription"
        ] = None,
        steps: Optional["capo_databrew.types.recipe_step_list.RecipeStepList"] = None,
    ) -> "capo_databrew.types.update_recipe_response.UpdateRecipeResponse":
        """<p>Modifies the definition of the <code>LATEST_WORKING</code> version of a DataBrew recipe.</p>

        Args:
            description: <p>A description of the recipe.</p>
            name: <p>The name of the recipe to be updated.</p>
            steps: <p>One or more steps to be performed by the recipe. Each step consists of an action, and the conditions under which the action should succeed.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.update_recipe_request.UpdateRecipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.update_recipe_response.UpdateRecipeResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.update_recipe

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.update_recipe.async_update_recipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.update_recipe_request.UpdateRecipeRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if steps is not None:
            input_["steps"] = steps

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_recipe_job(
        self,
        name: "capo_databrew.types.job_name.JobName",
        role_arn: "capo_databrew.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        encryption_key_arn: Optional[
            "capo_databrew.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        encryption_mode: Optional[
            "capo_databrew.types.encryption_mode.EncryptionMode"
        ] = None,
        log_subscription: Optional[
            "capo_databrew.types.log_subscription.LogSubscription"
        ] = None,
        max_capacity: Optional["capo_databrew.types.max_capacity.MaxCapacity"] = None,
        max_retries: Optional["capo_databrew.types.max_retries.MaxRetries"] = None,
        outputs: Optional["capo_databrew.types.output_list.OutputList"] = None,
        data_catalog_outputs: Optional[
            "capo_databrew.types.data_catalog_output_list.DataCatalogOutputList"
        ] = None,
        database_outputs: Optional[
            "capo_databrew.types.database_output_list.DatabaseOutputList"
        ] = None,
        timeout: Optional["capo_databrew.types.timeout.Timeout"] = None,
    ) -> "capo_databrew.types.update_recipe_job_response.UpdateRecipeJobResponse":
        """<p>Modifies the definition of an existing DataBrew recipe job.</p>

        Args:
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of an encryption key that is used to protect the job.</p>
            encryption_mode: <p>The encryption mode for the job, which can be one of the following:</p> <ul> <li> <p> <code>SSE-KMS</code> - Server-side encryption with keys managed by KMS.</p> </li> <li> <p> <code>SSE-S3</code> - Server-side encryption with keys managed by Amazon S3.</p> </li> </ul>
            name: <p>The name of the job to update.</p>
            log_subscription: <p>Enables or disables Amazon CloudWatch logging for the job. If logging is enabled, CloudWatch writes one log stream for each job run.</p>
            max_capacity: <p>The maximum number of nodes that DataBrew can consume when the job processes data.</p>
            max_retries: <p>The maximum number of times to retry the job after a job run fails.</p>
            outputs: <p>One or more artifacts that represent the output from running the job. </p>
            data_catalog_outputs: <p>One or more artifacts that represent the Glue Data Catalog output from running the job.</p>
            database_outputs: <p>Represents a list of JDBC database output objects which defines the output destination for a DataBrew recipe job to write into.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role to be assumed when DataBrew runs the job.</p>
            timeout: <p>The job's timeout in minutes. A job that attempts to run longer than this timeout period ends with a status of <code>TIMEOUT</code>.</p>

        Raises:
            capo_databrew.errors.access_denied_exception.AccessDeniedException: <p>Access to the specified resource was denied.</p>
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.update_recipe_job_request.UpdateRecipeJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.update_recipe_job_response.UpdateRecipeJobResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.update_recipe_job

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.update_recipe_job.async_update_recipe_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.update_recipe_job_request.UpdateRecipeJobRequest = {
            "name": name,
            "role_arn": role_arn,
        }
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if encryption_mode is not None:
            input_["encryption_mode"] = encryption_mode
        if log_subscription is not None:
            input_["log_subscription"] = log_subscription
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if max_retries is not None:
            input_["max_retries"] = max_retries
        if outputs is not None:
            input_["outputs"] = outputs
        if data_catalog_outputs is not None:
            input_["data_catalog_outputs"] = data_catalog_outputs
        if database_outputs is not None:
            input_["database_outputs"] = database_outputs
        if timeout is not None:
            input_["timeout"] = timeout

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ruleset(
        self,
        name: "capo_databrew.types.ruleset_name.RulesetName",
        rules: "capo_databrew.types.rule_list.RuleList",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        description: Optional[
            "capo_databrew.types.ruleset_description.RulesetDescription"
        ] = None,
    ) -> "capo_databrew.types.update_ruleset_response.UpdateRulesetResponse":
        """<p>Updates specified ruleset.</p>

        Args:
            name: <p>The name of the ruleset to be updated.</p>
            description: <p>The description of the ruleset.</p>
            rules: <p>A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.update_ruleset_request.UpdateRulesetRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.update_ruleset_response.UpdateRulesetResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.update_ruleset

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.update_ruleset.async_update_ruleset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.update_ruleset_request.UpdateRulesetRequest = {
            "name": name,
            "rules": rules,
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

    async def update_schedule(
        self,
        cron_expression: "capo_databrew.types.cron_expression.CronExpression",
        name: "capo_databrew.types.schedule_name.ScheduleName",
        *,
        config_overrides: Optional[AsyncDataBrewClientConfig] = None,
        job_names: Optional["capo_databrew.types.job_name_list.JobNameList"] = None,
    ) -> "capo_databrew.types.update_schedule_response.UpdateScheduleResponse":
        """<p>Modifies the definition of an existing DataBrew schedule.</p>

        Args:
            job_names: <p>The name or names of one or more jobs to be run for this schedule.</p>
            cron_expression: <p>The date or dates and time or times when the jobs are to be run. For more information, see <a href="https://docs.aws.amazon.com/databrew/latest/dg/jobs.cron.html">Cron expressions</a> in the <i>Glue DataBrew Developer Guide</i>.</p>
            name: <p>The name of the schedule to update.</p>

        Raises:
            capo_databrew.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_databrew.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota is exceeded.</p>
            capo_databrew.errors.validation_exception.ValidationException: <p>The input parameters for this request failed validation.</p>
            capo_databrew.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_databrew.types.update_schedule_request.UpdateScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_databrew.types.update_schedule_response.UpdateScheduleResponse"
        ]:
            import capo_databrew._operations.aws_glue_data_brew.update_schedule

            (
                output,
                http_response,
            ) = await capo_databrew._operations.aws_glue_data_brew.update_schedule.async_update_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_databrew.types.update_schedule_request.UpdateScheduleRequest = {
            "cron_expression": cron_expression,
            "name": name,
        }
        if job_names is not None:
            input_["job_names"] = job_names

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
