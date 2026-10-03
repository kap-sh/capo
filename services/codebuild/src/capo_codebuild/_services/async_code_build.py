"""Generated from Smithy shape ``com.amazonaws.codebuild#CodeBuild_20161006``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_codebuild._auth._signers
import capo_codebuild._auth._sigv4
from capo_codebuild._auth._identity import Credentials
from capo_codebuild._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codebuild._auth._zapros_handler import AuthMiddleware
from capo_codebuild._pagination import resolve_path as _resolve_path
from capo_codebuild._services._aws_config import aaws_config
from capo_codebuild._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_codebuild.types.auth_type
    import capo_codebuild.types.batch_delete_builds_input
    import capo_codebuild.types.batch_delete_builds_output
    import capo_codebuild.types.batch_get_build_batches_input
    import capo_codebuild.types.batch_get_build_batches_output
    import capo_codebuild.types.batch_get_builds_input
    import capo_codebuild.types.batch_get_builds_output
    import capo_codebuild.types.batch_get_command_executions_input
    import capo_codebuild.types.batch_get_command_executions_output
    import capo_codebuild.types.batch_get_fleets_input
    import capo_codebuild.types.batch_get_fleets_output
    import capo_codebuild.types.batch_get_projects_input
    import capo_codebuild.types.batch_get_projects_output
    import capo_codebuild.types.batch_get_report_groups_input
    import capo_codebuild.types.batch_get_report_groups_output
    import capo_codebuild.types.batch_get_reports_input
    import capo_codebuild.types.batch_get_reports_output
    import capo_codebuild.types.batch_get_sandboxes_input
    import capo_codebuild.types.batch_get_sandboxes_output
    import capo_codebuild.types.boolean
    import capo_codebuild.types.build_batch_filter
    import capo_codebuild.types.build_batch_ids
    import capo_codebuild.types.build_ids
    import capo_codebuild.types.build_status_config
    import capo_codebuild.types.build_time_out
    import capo_codebuild.types.code_coverage
    import capo_codebuild.types.command_execution
    import capo_codebuild.types.command_execution_ids
    import capo_codebuild.types.command_type
    import capo_codebuild.types.compute_configuration
    import capo_codebuild.types.compute_type
    import capo_codebuild.types.create_fleet_input
    import capo_codebuild.types.create_fleet_output
    import capo_codebuild.types.create_project_input
    import capo_codebuild.types.create_project_output
    import capo_codebuild.types.create_report_group_input
    import capo_codebuild.types.create_report_group_output
    import capo_codebuild.types.create_webhook_input
    import capo_codebuild.types.create_webhook_output
    import capo_codebuild.types.delete_build_batch_input
    import capo_codebuild.types.delete_build_batch_output
    import capo_codebuild.types.delete_fleet_input
    import capo_codebuild.types.delete_fleet_output
    import capo_codebuild.types.delete_project_input
    import capo_codebuild.types.delete_project_output
    import capo_codebuild.types.delete_report_group_input
    import capo_codebuild.types.delete_report_group_output
    import capo_codebuild.types.delete_report_input
    import capo_codebuild.types.delete_report_output
    import capo_codebuild.types.delete_resource_policy_input
    import capo_codebuild.types.delete_resource_policy_output
    import capo_codebuild.types.delete_source_credentials_input
    import capo_codebuild.types.delete_source_credentials_output
    import capo_codebuild.types.delete_webhook_input
    import capo_codebuild.types.delete_webhook_output
    import capo_codebuild.types.describe_code_coverages_input
    import capo_codebuild.types.describe_code_coverages_output
    import capo_codebuild.types.describe_test_cases_input
    import capo_codebuild.types.describe_test_cases_output
    import capo_codebuild.types.environment_type
    import capo_codebuild.types.environment_variables
    import capo_codebuild.types.filter_groups
    import capo_codebuild.types.fleet_capacity
    import capo_codebuild.types.fleet_name
    import capo_codebuild.types.fleet_names
    import capo_codebuild.types.fleet_overflow_behavior
    import capo_codebuild.types.fleet_sort_by_type
    import capo_codebuild.types.get_report_group_trend_input
    import capo_codebuild.types.get_report_group_trend_output
    import capo_codebuild.types.get_resource_policy_input
    import capo_codebuild.types.get_resource_policy_output
    import capo_codebuild.types.git_clone_depth
    import capo_codebuild.types.git_submodules_config
    import capo_codebuild.types.host_kernel
    import capo_codebuild.types.image_pull_credentials_type
    import capo_codebuild.types.import_source_credentials_input
    import capo_codebuild.types.import_source_credentials_output
    import capo_codebuild.types.invalidate_project_cache_input
    import capo_codebuild.types.invalidate_project_cache_output
    import capo_codebuild.types.list_build_batches_for_project_input
    import capo_codebuild.types.list_build_batches_for_project_output
    import capo_codebuild.types.list_build_batches_input
    import capo_codebuild.types.list_build_batches_output
    import capo_codebuild.types.list_builds_for_project_input
    import capo_codebuild.types.list_builds_for_project_output
    import capo_codebuild.types.list_builds_input
    import capo_codebuild.types.list_builds_output
    import capo_codebuild.types.list_command_executions_for_sandbox_input
    import capo_codebuild.types.list_command_executions_for_sandbox_output
    import capo_codebuild.types.list_curated_environment_images_input
    import capo_codebuild.types.list_curated_environment_images_output
    import capo_codebuild.types.list_fleets_input
    import capo_codebuild.types.list_fleets_output
    import capo_codebuild.types.list_projects_input
    import capo_codebuild.types.list_projects_output
    import capo_codebuild.types.list_report_groups_input
    import capo_codebuild.types.list_report_groups_output
    import capo_codebuild.types.list_reports_for_report_group_input
    import capo_codebuild.types.list_reports_for_report_group_output
    import capo_codebuild.types.list_reports_input
    import capo_codebuild.types.list_reports_output
    import capo_codebuild.types.list_sandboxes_for_project_input
    import capo_codebuild.types.list_sandboxes_for_project_output
    import capo_codebuild.types.list_sandboxes_input
    import capo_codebuild.types.list_sandboxes_output
    import capo_codebuild.types.list_shared_projects_input
    import capo_codebuild.types.list_shared_projects_output
    import capo_codebuild.types.list_shared_report_groups_input
    import capo_codebuild.types.list_shared_report_groups_output
    import capo_codebuild.types.list_source_credentials_input
    import capo_codebuild.types.list_source_credentials_output
    import capo_codebuild.types.logs_config
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.page_size
    import capo_codebuild.types.percentage
    import capo_codebuild.types.project_artifacts
    import capo_codebuild.types.project_artifacts_list
    import capo_codebuild.types.project_build_batch_config
    import capo_codebuild.types.project_cache
    import capo_codebuild.types.project_description
    import capo_codebuild.types.project_environment
    import capo_codebuild.types.project_file_system_locations
    import capo_codebuild.types.project_fleet
    import capo_codebuild.types.project_name
    import capo_codebuild.types.project_names
    import capo_codebuild.types.project_secondary_source_versions
    import capo_codebuild.types.project_sort_by_type
    import capo_codebuild.types.project_source
    import capo_codebuild.types.project_sources
    import capo_codebuild.types.project_visibility_type
    import capo_codebuild.types.proxy_configuration
    import capo_codebuild.types.pull_request_build_policy
    import capo_codebuild.types.put_resource_policy_input
    import capo_codebuild.types.put_resource_policy_output
    import capo_codebuild.types.registry_credential
    import capo_codebuild.types.report_arns
    import capo_codebuild.types.report_code_coverage_sort_by_type
    import capo_codebuild.types.report_export_config
    import capo_codebuild.types.report_filter
    import capo_codebuild.types.report_group_arns
    import capo_codebuild.types.report_group_name
    import capo_codebuild.types.report_group_sort_by_type
    import capo_codebuild.types.report_group_trend_field_type
    import capo_codebuild.types.report_type
    import capo_codebuild.types.retry_build_batch_input
    import capo_codebuild.types.retry_build_batch_output
    import capo_codebuild.types.retry_build_batch_type
    import capo_codebuild.types.retry_build_input
    import capo_codebuild.types.retry_build_output
    import capo_codebuild.types.sandbox_ids
    import capo_codebuild.types.scaling_configuration_input
    import capo_codebuild.types.scope_configuration
    import capo_codebuild.types.sensitive_non_empty_string
    import capo_codebuild.types.sensitive_string
    import capo_codebuild.types.server_type
    import capo_codebuild.types.shared_resource_sort_by_type
    import capo_codebuild.types.sort_order_type
    import capo_codebuild.types.source_auth
    import capo_codebuild.types.source_type
    import capo_codebuild.types.start_build_batch_input
    import capo_codebuild.types.start_build_batch_output
    import capo_codebuild.types.start_build_input
    import capo_codebuild.types.start_build_output
    import capo_codebuild.types.start_command_execution_input
    import capo_codebuild.types.start_command_execution_output
    import capo_codebuild.types.start_sandbox_connection_input
    import capo_codebuild.types.start_sandbox_connection_output
    import capo_codebuild.types.start_sandbox_input
    import capo_codebuild.types.start_sandbox_output
    import capo_codebuild.types.stop_build_batch_input
    import capo_codebuild.types.stop_build_batch_output
    import capo_codebuild.types.stop_build_input
    import capo_codebuild.types.stop_build_output
    import capo_codebuild.types.stop_sandbox_input
    import capo_codebuild.types.stop_sandbox_output
    import capo_codebuild.types.string
    import capo_codebuild.types.tag_list
    import capo_codebuild.types.test_case
    import capo_codebuild.types.test_case_filter
    import capo_codebuild.types.time_out
    import capo_codebuild.types.update_fleet_input
    import capo_codebuild.types.update_fleet_output
    import capo_codebuild.types.update_project_input
    import capo_codebuild.types.update_project_output
    import capo_codebuild.types.update_project_visibility_input
    import capo_codebuild.types.update_project_visibility_output
    import capo_codebuild.types.update_report_group_input
    import capo_codebuild.types.update_report_group_output
    import capo_codebuild.types.update_webhook_input
    import capo_codebuild.types.update_webhook_output
    import capo_codebuild.types.vpc_config
    import capo_codebuild.types.webhook_build_type
    import capo_codebuild.types.wrapper_boolean
    import capo_codebuild.types.wrapper_int


class AsyncCodeBuildClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncCodeBuildClient:
    """A client for the ``CodeBuild`` service.

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
        self._config = AsyncCodeBuildClientConfig(
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
        self, config_overrides: Optional[AsyncCodeBuildClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodeBuildClientConfig = config_overrides or {}
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

    async def batch_delete_builds(
        self,
        ids: "capo_codebuild.types.build_ids.BuildIds",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.batch_delete_builds_output.BatchDeleteBuildsOutput":
        """<p>Deletes one or more builds.</p>

        Args:
            ids: <p>The IDs of the builds to delete.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_delete_builds_input.BatchDeleteBuildsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_delete_builds_output.BatchDeleteBuildsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_delete_builds

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_delete_builds.async_batch_delete_builds(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_delete_builds_input.BatchDeleteBuildsInput = {
            "ids": ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_build_batches(
        self,
        ids: "capo_codebuild.types.build_batch_ids.BuildBatchIds",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> (
        "capo_codebuild.types.batch_get_build_batches_output.BatchGetBuildBatchesOutput"
    ):
        """<p>Retrieves information about one or more batch builds.</p>

        Args:
            ids: <p>An array that contains the batch build identifiers to retrieve.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_get_build_batches_input.BatchGetBuildBatchesInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_get_build_batches_output.BatchGetBuildBatchesOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_get_build_batches

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_get_build_batches.async_batch_get_build_batches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_get_build_batches_input.BatchGetBuildBatchesInput = {
            "ids": ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_builds(
        self,
        ids: "capo_codebuild.types.build_ids.BuildIds",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.batch_get_builds_output.BatchGetBuildsOutput":
        """<p>Gets information about one or more builds.</p>

        Args:
            ids: <p>The IDs of the builds.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_get_builds_input.BatchGetBuildsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_get_builds_output.BatchGetBuildsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_get_builds

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_get_builds.async_batch_get_builds(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_get_builds_input.BatchGetBuildsInput = {
            "ids": ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_command_executions(
        self,
        sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        command_execution_ids: "capo_codebuild.types.command_execution_ids.CommandExecutionIds",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.batch_get_command_executions_output.BatchGetCommandExecutionsOutput":
        """<p>Gets information about the command executions.</p>

        Args:
            sandbox_id: <p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>
            command_execution_ids: <p>A comma separated list of <code>commandExecutionIds</code>.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_get_command_executions_input.BatchGetCommandExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_get_command_executions_output.BatchGetCommandExecutionsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_get_command_executions

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_get_command_executions.async_batch_get_command_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_get_command_executions_input.BatchGetCommandExecutionsInput = {
            "sandbox_id": sandbox_id,
            "command_execution_ids": command_execution_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_fleets(
        self,
        names: "capo_codebuild.types.fleet_names.FleetNames",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.batch_get_fleets_output.BatchGetFleetsOutput":
        """<p>Gets information about one or more compute fleets.</p>

        Args:
            names: <p>The names or ARNs of the compute fleets.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_get_fleets_input.BatchGetFleetsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_get_fleets_output.BatchGetFleetsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_get_fleets

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_get_fleets.async_batch_get_fleets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_get_fleets_input.BatchGetFleetsInput = {
            "names": names
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_projects(
        self,
        names: "capo_codebuild.types.project_names.ProjectNames",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.batch_get_projects_output.BatchGetProjectsOutput":
        """<p>Gets information about one or more build projects.</p>

        Args:
            names: <p>The names or ARNs of the build projects. To get information about a project shared with your Amazon Web Services account, its ARN must be specified. You cannot specify a shared project using its name.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_get_projects_input.BatchGetProjectsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_get_projects_output.BatchGetProjectsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_get_projects

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_get_projects.async_batch_get_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_get_projects_input.BatchGetProjectsInput = {
            "names": names
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_report_groups(
        self,
        report_group_arns: "capo_codebuild.types.report_group_arns.ReportGroupArns",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> (
        "capo_codebuild.types.batch_get_report_groups_output.BatchGetReportGroupsOutput"
    ):
        """<p> Returns an array of report groups. </p>

        Args:
            report_group_arns: <p> An array of report group ARNs that identify the report groups to return. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_get_report_groups_input.BatchGetReportGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_get_report_groups_output.BatchGetReportGroupsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_get_report_groups

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_get_report_groups.async_batch_get_report_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_get_report_groups_input.BatchGetReportGroupsInput = {
            "report_group_arns": report_group_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_reports(
        self,
        report_arns: "capo_codebuild.types.report_arns.ReportArns",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.batch_get_reports_output.BatchGetReportsOutput":
        """<p> Returns an array of reports. </p>

        Args:
            report_arns: <p> An array of ARNs that identify the <code>Report</code> objects to return. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_get_reports_input.BatchGetReportsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_get_reports_output.BatchGetReportsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_get_reports

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_get_reports.async_batch_get_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_get_reports_input.BatchGetReportsInput = {
            "report_arns": report_arns
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_sandboxes(
        self,
        ids: "capo_codebuild.types.sandbox_ids.SandboxIds",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.batch_get_sandboxes_output.BatchGetSandboxesOutput":
        """<p>Gets information about the sandbox status.</p>

        Args:
            ids: <p>A comma separated list of <code>sandboxIds</code> or <code>sandboxArns</code>.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.batch_get_sandboxes_input.BatchGetSandboxesInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.batch_get_sandboxes_output.BatchGetSandboxesOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.batch_get_sandboxes

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.batch_get_sandboxes.async_batch_get_sandboxes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.batch_get_sandboxes_input.BatchGetSandboxesInput = {
            "ids": ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_fleet(
        self,
        name: "capo_codebuild.types.fleet_name.FleetName",
        base_capacity: "capo_codebuild.types.fleet_capacity.FleetCapacity",
        environment_type: "capo_codebuild.types.environment_type.EnvironmentType",
        compute_type: "capo_codebuild.types.compute_type.ComputeType",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        compute_configuration: Optional[
            "capo_codebuild.types.compute_configuration.ComputeConfiguration"
        ] = None,
        scaling_configuration: Optional[
            "capo_codebuild.types.scaling_configuration_input.ScalingConfigurationInput"
        ] = None,
        overflow_behavior: Optional[
            "capo_codebuild.types.fleet_overflow_behavior.FleetOverflowBehavior"
        ] = None,
        vpc_config: Optional["capo_codebuild.types.vpc_config.VpcConfig"] = None,
        proxy_configuration: Optional[
            "capo_codebuild.types.proxy_configuration.ProxyConfiguration"
        ] = None,
        image_id: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        fleet_service_role: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_codebuild.types.tag_list.TagList"] = None,
    ) -> "capo_codebuild.types.create_fleet_output.CreateFleetOutput":
        """<p>Creates a compute fleet.</p>

        Args:
            name: <p>The name of the compute fleet.</p>
            base_capacity: <p>The initial number of machines allocated to the ﬂeet, which deﬁnes the number of builds that can run in parallel.</p>
            environment_type: <p>The environment type of the compute fleet.</p> <ul> <li> <p>The environment type <code>ARM_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), EU (Frankfurt), and South America (São Paulo).</p> </li> <li> <p>The environment type <code>ARM_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_GPU_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), and Asia Pacific (Sydney).</p> </li> <li> <p>The environment type <code>MAC_ARM</code> is available for Medium fleets only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), and EU (Frankfurt)</p> </li> <li> <p>The environment type <code>MAC_ARM</code> is available for Large fleets only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), and Asia Pacific (Sydney).</p> </li> <li> <p>The environment type <code>WINDOWS_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>WINDOWS_SERVER_2019_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), Asia Pacific (Tokyo), Asia Pacific (Mumbai) and EU (Ireland).</p> </li> <li> <p>The environment type <code>WINDOWS_SERVER_2022_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Tokyo), South America (São Paulo) and Asia Pacific (Mumbai).</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html">Build environment compute types</a> in the <i>CodeBuild user guide</i>.</p>
            compute_type: <p>Information about the compute resources the compute fleet uses. Available values include:</p> <ul> <li> <p> <code>ATTRIBUTE_BASED_COMPUTE</code>: Specify the amount of vCPUs, memory, disk space, and the type of machine.</p> <note> <p> If you use <code>ATTRIBUTE_BASED_COMPUTE</code>, you must define your attributes by using <code>computeConfiguration</code>. CodeBuild will select the cheapest instance that satisfies your specified attributes. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.types">Reserved capacity environment types</a> in the <i>CodeBuild User Guide</i>.</p> </note> </li> <li> <p> <code>CUSTOM_INSTANCE_TYPE</code>: Specify the instance type for your compute fleet. For a list of supported instance types, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.instance-types">Supported instance families </a> in the <i>CodeBuild User Guide</i>.</p> </li> <li> <p> <code>BUILD_GENERAL1_SMALL</code>: Use up to 4 GiB memory and 2 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_MEDIUM</code>: Use up to 8 GiB memory and 4 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_LARGE</code>: Use up to 16 GiB memory and 8 vCPUs for builds, depending on your environment type.</p> </li> <li> <p> <code>BUILD_GENERAL1_XLARGE</code>: Use up to 72 GiB memory and 36 vCPUs for builds, depending on your environment type.</p> </li> <li> <p> <code>BUILD_GENERAL1_2XLARGE</code>: Use up to 144 GiB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.</p> </li> <li> <p> <code>BUILD_LAMBDA_1GB</code>: Use up to 1 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_2GB</code>: Use up to 2 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_4GB</code>: Use up to 4 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_8GB</code>: Use up to 8 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_10GB</code>: Use up to 10 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> </ul> <p> If you use <code>BUILD_GENERAL1_SMALL</code>: </p> <ul> <li> <p> For environment type <code>LINUX_CONTAINER</code>, you can use up to 4 GiB memory and 2 vCPUs for builds. </p> </li> <li> <p> For environment type <code>LINUX_GPU_CONTAINER</code>, you can use up to 16 GiB memory, 4 vCPUs, and 1 NVIDIA A10G Tensor Core GPU for builds.</p> </li> <li> <p> For environment type <code>ARM_CONTAINER</code>, you can use up to 4 GiB memory and 2 vCPUs on ARM-based processors for builds.</p> </li> </ul> <p> If you use <code>BUILD_GENERAL1_LARGE</code>: </p> <ul> <li> <p> For environment type <code>LINUX_CONTAINER</code>, you can use up to 16 GiB memory and 8 vCPUs for builds. </p> </li> <li> <p> For environment type <code>LINUX_GPU_CONTAINER</code>, you can use up to 255 GiB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.</p> </li> <li> <p> For environment type <code>ARM_CONTAINER</code>, you can use up to 16 GiB memory and 8 vCPUs on ARM-based processors for builds.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment.types">On-demand environment types</a> in the <i>CodeBuild User Guide.</i> </p>
            compute_configuration: <p>The compute configuration of the compute fleet. This is only required if <code>computeType</code> is set to <code>ATTRIBUTE_BASED_COMPUTE</code> or <code>CUSTOM_INSTANCE_TYPE</code>.</p>
            scaling_configuration: <p>The scaling configuration of the compute fleet.</p>
            overflow_behavior: <p>The compute fleet overflow behavior.</p> <ul> <li> <p>For overflow behavior <code>QUEUE</code>, your overflow builds need to wait on the existing fleet instance to become available.</p> </li> <li> <p>For overflow behavior <code>ON_DEMAND</code>, your overflow builds run on CodeBuild on-demand.</p> <note> <p>If you choose to set your overflow behavior to on-demand while creating a VPC-connected fleet, make sure that you add the required VPC permissions to your project service role. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-create-vpc-network-interface">Example policy statement to allow CodeBuild access to Amazon Web Services services required to create a VPC network interface</a>.</p> </note> </li> </ul>
            proxy_configuration: <p>The proxy configuration of the compute fleet.</p>
            image_id: <p>The Amazon Machine Image (AMI) of the compute fleet.</p>
            fleet_service_role: <p>The service role associated with the compute fleet. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-permission-policy-fleet-service-role.html"> Allow a user to add a permission policy for a fleet service role</a> in the <i>CodeBuild User Guide</i>.</p>
            tags: <p>A list of tag key and value pairs associated with this compute fleet.</p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.</p>

        Raises:
            capo_codebuild.errors.account_limit_exceeded_exception.AccountLimitExceededException: <p>An Amazon Web Services service limit was exceeded for the calling Amazon Web Services account.</p>
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified Amazon Web Services resource cannot be created, because an Amazon Web Services resource with the same settings already exists.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.create_fleet_input.CreateFleetInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.create_fleet_output.CreateFleetOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.create_fleet

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.create_fleet.async_create_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.create_fleet_input.CreateFleetInput = {
            "name": name,
            "base_capacity": base_capacity,
            "environment_type": environment_type,
            "compute_type": compute_type,
        }
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if scaling_configuration is not None:
            input_["scaling_configuration"] = scaling_configuration
        if overflow_behavior is not None:
            input_["overflow_behavior"] = overflow_behavior
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if proxy_configuration is not None:
            input_["proxy_configuration"] = proxy_configuration
        if image_id is not None:
            input_["image_id"] = image_id
        if fleet_service_role is not None:
            input_["fleet_service_role"] = fleet_service_role
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_project(
        self,
        name: "capo_codebuild.types.project_name.ProjectName",
        source: "capo_codebuild.types.project_source.ProjectSource",
        artifacts: "capo_codebuild.types.project_artifacts.ProjectArtifacts",
        environment: "capo_codebuild.types.project_environment.ProjectEnvironment",
        service_role: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        description: Optional[
            "capo_codebuild.types.project_description.ProjectDescription"
        ] = None,
        secondary_sources: Optional[
            "capo_codebuild.types.project_sources.ProjectSources"
        ] = None,
        source_version: Optional["capo_codebuild.types.string.String"] = None,
        secondary_source_versions: Optional[
            "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
        ] = None,
        secondary_artifacts: Optional[
            "capo_codebuild.types.project_artifacts_list.ProjectArtifactsList"
        ] = None,
        cache: Optional["capo_codebuild.types.project_cache.ProjectCache"] = None,
        timeout_in_minutes: Optional[
            "capo_codebuild.types.build_time_out.BuildTimeOut"
        ] = None,
        queued_timeout_in_minutes: Optional[
            "capo_codebuild.types.time_out.TimeOut"
        ] = None,
        encryption_key: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_codebuild.types.tag_list.TagList"] = None,
        vpc_config: Optional["capo_codebuild.types.vpc_config.VpcConfig"] = None,
        badge_enabled: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        logs_config: Optional["capo_codebuild.types.logs_config.LogsConfig"] = None,
        file_system_locations: Optional[
            "capo_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
        ] = None,
        build_batch_config: Optional[
            "capo_codebuild.types.project_build_batch_config.ProjectBuildBatchConfig"
        ] = None,
        concurrent_build_limit: Optional[
            "capo_codebuild.types.wrapper_int.WrapperInt"
        ] = None,
        auto_retry_limit: Optional[
            "capo_codebuild.types.wrapper_int.WrapperInt"
        ] = None,
    ) -> "capo_codebuild.types.create_project_output.CreateProjectOutput":
        """<p>Creates a build project.</p>

        Args:
            name: <p>The name of the build project.</p>
            description: <p>A description that makes the build project easy to identify.</p>
            source: <p>Information about the build input source code for the build project.</p>
            secondary_sources: <p>An array of <code>ProjectSource</code> objects. </p>
            source_version: <p>A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of: </p> <ul> <li> <p>For CodeCommit: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For GitLab: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Amazon S3: the version ID of the object that represents the build input ZIP file to use.</p> </li> </ul> <p>If <code>sourceVersion</code> is specified at the build level, then that version takes precedence over this <code>sourceVersion</code> (at the project level). </p> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>
            secondary_source_versions: <p>An array of <code>ProjectSourceVersion</code> objects. If <code>secondarySourceVersions</code> is specified at the build level, then they take precedence over these <code>secondarySourceVersions</code> (at the project level). </p>
            artifacts: <p>Information about the build output artifacts for the build project.</p>
            secondary_artifacts: <p>An array of <code>ProjectArtifacts</code> objects. </p>
            cache: <p>Stores recently used information so that it can be quickly accessed at a later time.</p>
            environment: <p>Information about the build environment for the build project.</p>
            service_role: <p>The ARN of the IAM role that enables CodeBuild to interact with dependent Amazon Web Services services on behalf of the Amazon Web Services account.</p>
            timeout_in_minutes: <p>How long, in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before it times out any build that has not been marked as completed. The default is 60 minutes.</p>
            queued_timeout_in_minutes: <p>The number of minutes a build is allowed to be queued before it times out. </p>
            encryption_key: <p>The Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.</p> <note> <p>You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>). </p>
            tags: <p>A list of tag key and value pairs associated with this build project.</p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.</p>
            vpc_config: <p>VpcConfig enables CodeBuild to access resources in an Amazon VPC.</p> <note> <p>If you're using compute fleets during project creation, do not provide vpcConfig.</p> </note>
            badge_enabled: <p>Set this to true to generate a publicly accessible URL for your project's build badge.</p>
            logs_config: <p>Information about logs for the build project. These can be logs in CloudWatch Logs, logs uploaded to a specified S3 bucket, or both. </p>
            file_system_locations: <p> An array of <code>ProjectFileSystemLocation</code> objects for a CodeBuild build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>
            build_batch_config: <p>A <a>ProjectBuildBatchConfig</a> object that defines the batch build options for the project.</p>
            concurrent_build_limit: <p>The maximum number of concurrent builds that are allowed for this project.</p> <p>New builds are only started if the current number of builds is less than or equal to this limit. If the current build count meets this limit, new builds are throttled and are not run.</p>
            auto_retry_limit: <p>The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the <code>RetryBuild</code> API to automatically retry your build for up to 2 additional times.</p>

        Raises:
            capo_codebuild.errors.account_limit_exceeded_exception.AccountLimitExceededException: <p>An Amazon Web Services service limit was exceeded for the calling Amazon Web Services account.</p>
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified Amazon Web Services resource cannot be created, because an Amazon Web Services resource with the same settings already exists.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.create_project_input.CreateProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.create_project_output.CreateProjectOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.create_project

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.create_project.async_create_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.create_project_input.CreateProjectInput = {
            "name": name,
            "source": source,
            "artifacts": artifacts,
            "environment": environment,
            "service_role": service_role,
        }
        if description is not None:
            input_["description"] = description
        if secondary_sources is not None:
            input_["secondary_sources"] = secondary_sources
        if source_version is not None:
            input_["source_version"] = source_version
        if secondary_source_versions is not None:
            input_["secondary_source_versions"] = secondary_source_versions
        if secondary_artifacts is not None:
            input_["secondary_artifacts"] = secondary_artifacts
        if cache is not None:
            input_["cache"] = cache
        if timeout_in_minutes is not None:
            input_["timeout_in_minutes"] = timeout_in_minutes
        if queued_timeout_in_minutes is not None:
            input_["queued_timeout_in_minutes"] = queued_timeout_in_minutes
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if tags is not None:
            input_["tags"] = tags
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if badge_enabled is not None:
            input_["badge_enabled"] = badge_enabled
        if logs_config is not None:
            input_["logs_config"] = logs_config
        if file_system_locations is not None:
            input_["file_system_locations"] = file_system_locations
        if build_batch_config is not None:
            input_["build_batch_config"] = build_batch_config
        if concurrent_build_limit is not None:
            input_["concurrent_build_limit"] = concurrent_build_limit
        if auto_retry_limit is not None:
            input_["auto_retry_limit"] = auto_retry_limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_report_group(
        self,
        name: "capo_codebuild.types.report_group_name.ReportGroupName",
        type: "capo_codebuild.types.report_type.ReportType",
        export_config: "capo_codebuild.types.report_export_config.ReportExportConfig",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        tags: Optional["capo_codebuild.types.tag_list.TagList"] = None,
    ) -> "capo_codebuild.types.create_report_group_output.CreateReportGroupOutput":
        """<p> Creates a report group. A report group contains a collection of reports. </p>

        Args:
            name: <p> The name of the report group. </p>
            type: <p> The type of report group. </p>
            export_config: <p> A <code>ReportExportConfig</code> object that contains information about where the report group test results are exported. </p>
            tags: <p> A list of tag key and value pairs associated with this report group. </p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild report group tags.</p>

        Raises:
            capo_codebuild.errors.account_limit_exceeded_exception.AccountLimitExceededException: <p>An Amazon Web Services service limit was exceeded for the calling Amazon Web Services account.</p>
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified Amazon Web Services resource cannot be created, because an Amazon Web Services resource with the same settings already exists.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.create_report_group_input.CreateReportGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.create_report_group_output.CreateReportGroupOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.create_report_group

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.create_report_group.async_create_report_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.create_report_group_input.CreateReportGroupInput = {
            "name": name,
            "type": type,
            "export_config": export_config,
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

    async def create_webhook(
        self,
        project_name: "capo_codebuild.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        branch_filter: Optional["capo_codebuild.types.string.String"] = None,
        filter_groups: Optional[
            "capo_codebuild.types.filter_groups.FilterGroups"
        ] = None,
        build_type: Optional[
            "capo_codebuild.types.webhook_build_type.WebhookBuildType"
        ] = None,
        manual_creation: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        scope_configuration: Optional[
            "capo_codebuild.types.scope_configuration.ScopeConfiguration"
        ] = None,
        pull_request_build_policy: Optional[
            "capo_codebuild.types.pull_request_build_policy.PullRequestBuildPolicy"
        ] = None,
    ) -> "capo_codebuild.types.create_webhook_output.CreateWebhookOutput":
        """<p>For an existing CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, enables CodeBuild to start rebuilding the source code every time a code change is pushed to the repository.</p> <important> <p>If you enable webhooks for an CodeBuild project, and the project is used as a build step in CodePipeline, then two identical builds are created for each commit. One build is triggered through webhooks, and one through CodePipeline. Because billing is on a per-build basis, you are billed for both builds. Therefore, if you are using CodePipeline, we recommend that you disable webhooks in CodeBuild. In the CodeBuild console, clear the Webhook box. For more information, see step 5 in <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console">Change a Build Project's Settings</a>.</p> </important>

        Args:
            project_name: <p>The name of the CodeBuild project.</p>
            branch_filter: <p>A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If <code>branchFilter</code> is empty, then all branches are built.</p> <note> <p>It is recommended that you use <code>filterGroups</code> instead of <code>branchFilter</code>. </p> </note>
            filter_groups: <p>An array of arrays of <code>WebhookFilter</code> objects used to determine which webhooks are triggered. At least one <code>WebhookFilter</code> in the array must specify <code>EVENT</code> as its <code>type</code>. </p> <p>For a build to be triggered, at least one filter group in the <code>filterGroups</code> array must pass. For a filter group to pass, each of its filters must pass. </p>
            build_type: <p>Specifies the type of build this webhook will trigger.</p> <note> <p> <code>RUNNER_BUILDKITE_BUILD</code> is only available for <code>NO_SOURCE</code> source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html">Tutorial: Configure a CodeBuild-hosted Buildkite runner</a> in the <i>CodeBuild user guide</i>.</p> </note>
            manual_creation: <p>If manualCreation is true, CodeBuild doesn't create a webhook in GitHub and instead returns <code>payloadUrl</code> and <code>secret</code> values for the webhook. The <code>payloadUrl</code> and <code>secret</code> values in the output can be used to manually create a webhook within GitHub.</p> <note> <p> <code>manualCreation</code> is only available for GitHub webhooks.</p> </note>
            scope_configuration: <p>The scope configuration for global or organization webhooks.</p> <note> <p>Global or organization webhooks are only available for GitHub and Github Enterprise webhooks.</p> </note>
            pull_request_build_policy: <p>A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests. This policy helps control when automated builds are executed based on contributor permissions and approval workflows.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.o_auth_provider_exception.OAuthProviderException: <p>There was a problem with the underlying OAuth provider.</p>
            capo_codebuild.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified Amazon Web Services resource cannot be created, because an Amazon Web Services resource with the same settings already exists.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.create_webhook_input.CreateWebhookInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.create_webhook_output.CreateWebhookOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.create_webhook

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.create_webhook.async_create_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.create_webhook_input.CreateWebhookInput = {
            "project_name": project_name
        }
        if branch_filter is not None:
            input_["branch_filter"] = branch_filter
        if filter_groups is not None:
            input_["filter_groups"] = filter_groups
        if build_type is not None:
            input_["build_type"] = build_type
        if manual_creation is not None:
            input_["manual_creation"] = manual_creation
        if scope_configuration is not None:
            input_["scope_configuration"] = scope_configuration
        if pull_request_build_policy is not None:
            input_["pull_request_build_policy"] = pull_request_build_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_build_batch(
        self,
        id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.delete_build_batch_output.DeleteBuildBatchOutput":
        """<p>Deletes a batch build.</p>

        Args:
            id: <p>The identifier of the batch build to delete.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.delete_build_batch_input.DeleteBuildBatchInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.delete_build_batch_output.DeleteBuildBatchOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.delete_build_batch

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.delete_build_batch.async_delete_build_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.delete_build_batch_input.DeleteBuildBatchInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_fleet(
        self,
        arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.delete_fleet_output.DeleteFleetOutput":
        """<p>Deletes a compute fleet. When you delete a compute fleet, its builds are not deleted.</p>

        Args:
            arn: <p>The ARN of the compute fleet.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.delete_fleet_input.DeleteFleetInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.delete_fleet_output.DeleteFleetOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.delete_fleet

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.delete_fleet.async_delete_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.delete_fleet_input.DeleteFleetInput = {"arn": arn}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_project(
        self,
        name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.delete_project_output.DeleteProjectOutput":
        """<p> Deletes a build project. When you delete a project, its builds are not deleted. </p>

        Args:
            name: <p>The name of the build project.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.delete_project_input.DeleteProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.delete_project_output.DeleteProjectOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.delete_project

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.delete_project.async_delete_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.delete_project_input.DeleteProjectInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_report(
        self,
        arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.delete_report_output.DeleteReportOutput":
        """<p> Deletes a report. </p>

        Args:
            arn: <p> The ARN of the report to delete. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.delete_report_input.DeleteReportInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.delete_report_output.DeleteReportOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.delete_report

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.delete_report.async_delete_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.delete_report_input.DeleteReportInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_report_group(
        self,
        arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        delete_reports: Optional["capo_codebuild.types.boolean.Boolean"] = None,
    ) -> "capo_codebuild.types.delete_report_group_output.DeleteReportGroupOutput":
        """<p>Deletes a report group. Before you delete a report group, you must delete its reports. </p>

        Args:
            arn: <p>The ARN of the report group to delete. </p>
            delete_reports: <p>If <code>true</code>, deletes any reports that belong to a report group before deleting the report group. </p> <p>If <code>false</code>, you must delete any reports in the report group. Use <a href="https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportsForReportGroup.html">ListReportsForReportGroup</a> to get the reports in a report group. Use <a href="https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReport.html">DeleteReport</a> to delete the reports. If you call <code>DeleteReportGroup</code> for a report group that contains one or more reports, an exception is thrown. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.delete_report_group_input.DeleteReportGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.delete_report_group_output.DeleteReportGroupOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.delete_report_group

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.delete_report_group.async_delete_report_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.delete_report_group_input.DeleteReportGroupInput = {
            "arn": arn
        }
        if delete_reports is not None:
            input_["delete_reports"] = delete_reports

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> (
        "capo_codebuild.types.delete_resource_policy_output.DeleteResourcePolicyOutput"
    ):
        """<p> Deletes a resource policy that is identified by its resource ARN. </p>

        Args:
            resource_arn: <p> The ARN of the resource that is associated with the resource policy. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.delete_resource_policy_input.DeleteResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.delete_resource_policy_output.DeleteResourcePolicyOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.delete_resource_policy_input.DeleteResourcePolicyInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_source_credentials(
        self,
        arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.delete_source_credentials_output.DeleteSourceCredentialsOutput":
        """<p> Deletes a set of GitHub, GitHub Enterprise, or Bitbucket source credentials. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the token.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.delete_source_credentials_input.DeleteSourceCredentialsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.delete_source_credentials_output.DeleteSourceCredentialsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.delete_source_credentials

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.delete_source_credentials.async_delete_source_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.delete_source_credentials_input.DeleteSourceCredentialsInput = {
            "arn": arn
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
        project_name: "capo_codebuild.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.delete_webhook_output.DeleteWebhookOutput":
        """<p>For an existing CodeBuild build project that has its source code stored in a GitHub or Bitbucket repository, stops CodeBuild from rebuilding the source code every time a code change is pushed to the repository.</p>

        Args:
            project_name: <p>The name of the CodeBuild project.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.o_auth_provider_exception.OAuthProviderException: <p>There was a problem with the underlying OAuth provider.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.delete_webhook_input.DeleteWebhookInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.delete_webhook_output.DeleteWebhookOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.delete_webhook

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.delete_webhook.async_delete_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.delete_webhook_input.DeleteWebhookInput = {
            "project_name": project_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_code_coverages(
        self,
        report_arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional[
            "capo_codebuild.types.report_code_coverage_sort_by_type.ReportCodeCoverageSortByType"
        ] = None,
        min_line_coverage_percentage: Optional[
            "capo_codebuild.types.percentage.Percentage"
        ] = None,
        max_line_coverage_percentage: Optional[
            "capo_codebuild.types.percentage.Percentage"
        ] = None,
    ) -> "capo_codebuild.types.describe_code_coverages_output.DescribeCodeCoveragesOutput":
        """<p>Retrieves one or more code coverage reports.</p>

        Args:
            report_arn: <p> The ARN of the report for which test cases are returned. </p>
            next_token: <p>The <code>nextToken</code> value returned from a previous call to <code>DescribeCodeCoverages</code>. This specifies the next item to return. To return the beginning of the list, exclude this parameter.</p>
            max_results: <p>The maximum number of results to return.</p>
            sort_order: <p>Specifies if the results are sorted in ascending or descending order.</p>
            sort_by: <p>Specifies how the results are sorted. Possible values are:</p> <dl> <dt>FILE_PATH</dt> <dd> <p>The results are sorted by file path.</p> </dd> <dt>LINE_COVERAGE_PERCENTAGE</dt> <dd> <p>The results are sorted by the percentage of lines that are covered.</p> </dd> </dl>
            min_line_coverage_percentage: <p>The minimum line coverage percentage to report.</p>
            max_line_coverage_percentage: <p>The maximum line coverage percentage to report.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.describe_code_coverages_input.DescribeCodeCoveragesInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.describe_code_coverages_output.DescribeCodeCoveragesOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.describe_code_coverages

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.describe_code_coverages.async_describe_code_coverages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.describe_code_coverages_input.DescribeCodeCoveragesInput = {
            "report_arn": report_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if min_line_coverage_percentage is not None:
            input_["min_line_coverage_percentage"] = min_line_coverage_percentage
        if max_line_coverage_percentage is not None:
            input_["max_line_coverage_percentage"] = max_line_coverage_percentage

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_code_coverages(
        self,
        report_arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional[
            "capo_codebuild.types.report_code_coverage_sort_by_type.ReportCodeCoverageSortByType"
        ] = None,
        min_line_coverage_percentage: Optional[
            "capo_codebuild.types.percentage.Percentage"
        ] = None,
        max_line_coverage_percentage: Optional[
            "capo_codebuild.types.percentage.Percentage"
        ] = None,
    ) -> "AsyncIterator[capo_codebuild.types.code_coverage.CodeCoverage]":
        _token = next_token
        while True:
            _response = await self.describe_code_coverages(
                report_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                sort_order=sort_order,
                sort_by=sort_by,
                min_line_coverage_percentage=min_line_coverage_percentage,
                max_line_coverage_percentage=max_line_coverage_percentage,
            )
            _page = _resolve_path(_response, ("code_coverages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_test_cases(
        self,
        report_arn: "capo_codebuild.types.string.String",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        filter: Optional["capo_codebuild.types.test_case_filter.TestCaseFilter"] = None,
    ) -> "capo_codebuild.types.describe_test_cases_output.DescribeTestCasesOutput":
        """<p> Returns a list of details about test cases for a report. </p>

        Args:
            report_arn: <p> The ARN of the report for which test cases are returned. </p>
            next_token: <p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>
            max_results: <p> The maximum number of paginated test cases returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>TestCase</code> objects. The default value is 100. </p>
            filter: <p> A <code>TestCaseFilter</code> object used to filter the returned reports. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.describe_test_cases_input.DescribeTestCasesInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.describe_test_cases_output.DescribeTestCasesOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.describe_test_cases

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.describe_test_cases.async_describe_test_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.describe_test_cases_input.DescribeTestCasesInput = {
            "report_arn": report_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_test_cases(
        self,
        report_arn: "capo_codebuild.types.string.String",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        filter: Optional["capo_codebuild.types.test_case_filter.TestCaseFilter"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.test_case.TestCase]":
        _token = next_token
        while True:
            _response = await self.describe_test_cases(
                report_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("test_cases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_report_group_trend(
        self,
        report_group_arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        trend_field: "capo_codebuild.types.report_group_trend_field_type.ReportGroupTrendFieldType",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        num_of_reports: Optional["capo_codebuild.types.page_size.PageSize"] = None,
    ) -> "capo_codebuild.types.get_report_group_trend_output.GetReportGroupTrendOutput":
        """<p>Analyzes and accumulates test report values for the specified test reports.</p>

        Args:
            report_group_arn: <p>The ARN of the report group that contains the reports to analyze.</p>
            num_of_reports: <p>The number of reports to analyze. This operation always retrieves the most recent reports.</p> <p>If this parameter is omitted, the most recent 100 reports are analyzed.</p>
            trend_field: <p>The test report value to accumulate. This must be one of the following values:</p> <dl> <dt>Test reports:</dt> <dd> <dl> <dt>DURATION</dt> <dd> <p>Accumulate the test run times for the specified reports.</p> </dd> <dt>PASS_RATE</dt> <dd> <p>Accumulate the percentage of tests that passed for the specified test reports.</p> </dd> <dt>TOTAL</dt> <dd> <p>Accumulate the total number of tests for the specified test reports.</p> </dd> </dl> </dd> </dl> <dl> <dt>Code coverage reports:</dt> <dd> <dl> <dt>BRANCH_COVERAGE</dt> <dd> <p>Accumulate the branch coverage percentages for the specified test reports.</p> </dd> <dt>BRANCHES_COVERED</dt> <dd> <p>Accumulate the branches covered values for the specified test reports.</p> </dd> <dt>BRANCHES_MISSED</dt> <dd> <p>Accumulate the branches missed values for the specified test reports.</p> </dd> <dt>LINE_COVERAGE</dt> <dd> <p>Accumulate the line coverage percentages for the specified test reports.</p> </dd> <dt>LINES_COVERED</dt> <dd> <p>Accumulate the lines covered values for the specified test reports.</p> </dd> <dt>LINES_MISSED</dt> <dd> <p>Accumulate the lines not covered values for the specified test reports.</p> </dd> </dl> </dd> </dl>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.get_report_group_trend_input.GetReportGroupTrendInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.get_report_group_trend_output.GetReportGroupTrendOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.get_report_group_trend

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.get_report_group_trend.async_get_report_group_trend(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.get_report_group_trend_input.GetReportGroupTrendInput = {
            "report_group_arn": report_group_arn,
            "trend_field": trend_field,
        }
        if num_of_reports is not None:
            input_["num_of_reports"] = num_of_reports

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.get_resource_policy_output.GetResourcePolicyOutput":
        """<p> Gets a resource policy that is identified by its resource ARN. </p>

        Args:
            resource_arn: <p> The ARN of the resource that is associated with the resource policy. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.get_resource_policy_input.GetResourcePolicyInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_source_credentials(
        self,
        token: "capo_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        server_type: "capo_codebuild.types.server_type.ServerType",
        auth_type: "capo_codebuild.types.auth_type.AuthType",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        username: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        should_overwrite: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
    ) -> "capo_codebuild.types.import_source_credentials_output.ImportSourceCredentialsOutput":
        """<p> Imports the source repository credentials for an CodeBuild project that has its source code stored in a GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository. </p>

        Args:
            username: <p> The Bitbucket username when the <code>authType</code> is BASIC_AUTH. This parameter is not valid for other types of source providers or connections. </p>
            token: <p> For GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is either the access token or the app password. For the <code>authType</code> CODECONNECTIONS, this is the <code>connectionArn</code>. For the <code>authType</code> SECRETS_MANAGER, this is the <code>secretArn</code>.</p>
            server_type: <p> The source provider used for this project. </p>
            auth_type: <p> The type of authentication used to connect to a GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket repository. An OAUTH connection is not supported by the API and must be created using the CodeBuild console.</p>
            should_overwrite: <p> Set to <code>false</code> to prevent overwriting the repository source credentials. Set to <code>true</code> to overwrite the repository source credentials. The default value is <code>true</code>. </p>

        Raises:
            capo_codebuild.errors.account_limit_exceeded_exception.AccountLimitExceededException: <p>An Amazon Web Services service limit was exceeded for the calling Amazon Web Services account.</p>
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified Amazon Web Services resource cannot be created, because an Amazon Web Services resource with the same settings already exists.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.import_source_credentials_input.ImportSourceCredentialsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.import_source_credentials_output.ImportSourceCredentialsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.import_source_credentials

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.import_source_credentials.async_import_source_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.import_source_credentials_input.ImportSourceCredentialsInput = {
            "token": token,
            "server_type": server_type,
            "auth_type": auth_type,
        }
        if username is not None:
            input_["username"] = username
        if should_overwrite is not None:
            input_["should_overwrite"] = should_overwrite

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def invalidate_project_cache(
        self,
        project_name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.invalidate_project_cache_output.InvalidateProjectCacheOutput":
        """<p>Resets the cache for a project.</p>

        Args:
            project_name: <p>The name of the CodeBuild build project that the cache is reset for.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.invalidate_project_cache_input.InvalidateProjectCacheInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.invalidate_project_cache_output.InvalidateProjectCacheOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.invalidate_project_cache

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.invalidate_project_cache.async_invalidate_project_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.invalidate_project_cache_input.InvalidateProjectCacheInput = {
            "project_name": project_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_build_batches(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        filter: Optional[
            "capo_codebuild.types.build_batch_filter.BuildBatchFilter"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "capo_codebuild.types.list_build_batches_output.ListBuildBatchesOutput":
        """<p>Retrieves the identifiers of your build batches in the current region.</p>

        Args:
            filter: <p>A <code>BuildBatchFilter</code> object that specifies the filters for the search.</p>
            max_results: <p>The maximum number of results to return.</p>
            sort_order: <p>Specifies the sort order of the returned items. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List the batch build identifiers in ascending order by identifier.</p> </li> <li> <p> <code>DESCENDING</code>: List the batch build identifiers in descending order by identifier.</p> </li> </ul>
            next_token: <p>The <code>nextToken</code> value returned from a previous call to <code>ListBuildBatches</code>. This specifies the next item to return. To return the beginning of the list, exclude this parameter.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_build_batches_input.ListBuildBatchesInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_build_batches_output.ListBuildBatchesOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_build_batches

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_build_batches.async_list_build_batches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_build_batches_input.ListBuildBatchesInput = {}
        if filter is not None:
            input_["filter"] = filter
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_build_batches(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        filter: Optional[
            "capo_codebuild.types.build_batch_filter.BuildBatchFilter"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_build_batches(
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_build_batches_for_project(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        project_name: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        filter: Optional[
            "capo_codebuild.types.build_batch_filter.BuildBatchFilter"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "capo_codebuild.types.list_build_batches_for_project_output.ListBuildBatchesForProjectOutput":
        """<p>Retrieves the identifiers of the build batches for a specific project.</p>

        Args:
            project_name: <p>The name of the project.</p>
            filter: <p>A <code>BuildBatchFilter</code> object that specifies the filters for the search.</p>
            max_results: <p>The maximum number of results to return.</p>
            sort_order: <p>Specifies the sort order of the returned items. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List the batch build identifiers in ascending order by identifier.</p> </li> <li> <p> <code>DESCENDING</code>: List the batch build identifiers in descending order by identifier.</p> </li> </ul>
            next_token: <p>The <code>nextToken</code> value returned from a previous call to <code>ListBuildBatchesForProject</code>. This specifies the next item to return. To return the beginning of the list, exclude this parameter.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_build_batches_for_project_input.ListBuildBatchesForProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_build_batches_for_project_output.ListBuildBatchesForProjectOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_build_batches_for_project

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_build_batches_for_project.async_list_build_batches_for_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_build_batches_for_project_input.ListBuildBatchesForProjectInput = {}
        if project_name is not None:
            input_["project_name"] = project_name
        if filter is not None:
            input_["filter"] = filter
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_build_batches_for_project(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        project_name: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        filter: Optional[
            "capo_codebuild.types.build_batch_filter.BuildBatchFilter"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_build_batches_for_project(
                config_overrides=config_overrides,
                project_name=project_name,
                filter=filter,
                max_results=max_results,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_builds(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "capo_codebuild.types.list_builds_output.ListBuildsOutput":
        """<p>Gets a list of build IDs, with each build ID representing a single build.</p>

        Args:
            sort_order: <p>The order to list build IDs. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List the build IDs in ascending order by build ID.</p> </li> <li> <p> <code>DESCENDING</code>: List the build IDs in descending order by build ID.</p> </li> </ul>
            next_token: <p>During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_builds_input.ListBuildsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_builds_output.ListBuildsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_builds

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_builds.async_list_builds(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_builds_input.ListBuildsInput = {}
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_builds(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_builds(
                config_overrides=config_overrides,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_builds_for_project(
        self,
        project_name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> (
        "capo_codebuild.types.list_builds_for_project_output.ListBuildsForProjectOutput"
    ):
        """<p>Gets a list of build identifiers for the specified build project, with each build identifier representing a single build.</p>

        Args:
            project_name: <p>The name of the CodeBuild project.</p>
            sort_order: <p>The order to sort the results in. The results are sorted by build number, not the build identifier. If this is not specified, the results are sorted in descending order.</p> <p>Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List the build identifiers in ascending order, by build number.</p> </li> <li> <p> <code>DESCENDING</code>: List the build identifiers in descending order, by build number.</p> </li> </ul> <p>If the project has more than 100 builds, setting the sort order will result in an error. </p>
            next_token: <p>During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_builds_for_project_input.ListBuildsForProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_builds_for_project_output.ListBuildsForProjectOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_builds_for_project

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_builds_for_project.async_list_builds_for_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_builds_for_project_input.ListBuildsForProjectInput = {
            "project_name": project_name
        }
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_builds_for_project(
        self,
        project_name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_builds_for_project(
                project_name,
                config_overrides=config_overrides,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_command_executions_for_sandbox(
        self,
        sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional[
            "capo_codebuild.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "capo_codebuild.types.list_command_executions_for_sandbox_output.ListCommandExecutionsForSandboxOutput":
        """<p>Gets a list of command executions for a sandbox.</p>

        Args:
            sandbox_id: <p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>
            max_results: <p>The maximum number of sandbox records to be retrieved.</p>
            sort_order: <p>The order in which sandbox records should be retrieved.</p>
            next_token: <p>The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_command_executions_for_sandbox_input.ListCommandExecutionsForSandboxInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_command_executions_for_sandbox_output.ListCommandExecutionsForSandboxOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_command_executions_for_sandbox

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_command_executions_for_sandbox.async_list_command_executions_for_sandbox(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_command_executions_for_sandbox_input.ListCommandExecutionsForSandboxInput = {
            "sandbox_id": sandbox_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_command_executions_for_sandbox(
        self,
        sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional[
            "capo_codebuild.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "AsyncIterator[capo_codebuild.types.command_execution.CommandExecution]":
        _token = next_token
        while True:
            _response = await self.list_command_executions_for_sandbox(
                sandbox_id,
                config_overrides=config_overrides,
                max_results=max_results,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("command_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_curated_environment_images(
        self, *, config_overrides: Optional[AsyncCodeBuildClientConfig] = None
    ) -> "capo_codebuild.types.list_curated_environment_images_output.ListCuratedEnvironmentImagesOutput":
        """<p>Gets information about Docker images that are managed by CodeBuild.</p>

        Raises:
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_curated_environment_images_input.ListCuratedEnvironmentImagesInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_curated_environment_images_output.ListCuratedEnvironmentImagesOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_curated_environment_images

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_curated_environment_images.async_list_curated_environment_images(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_curated_environment_images_input.ListCuratedEnvironmentImagesInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_fleets(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        next_token: Optional[
            "capo_codebuild.types.sensitive_string.SensitiveString"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional[
            "capo_codebuild.types.fleet_sort_by_type.FleetSortByType"
        ] = None,
    ) -> "capo_codebuild.types.list_fleets_output.ListFleetsOutput":
        """<p>Gets a list of compute fleet names with each compute fleet name representing a single compute fleet.</p>

        Args:
            next_token: <p>During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>
            max_results: <p>The maximum number of paginated compute fleets returned per response. Use <code>nextToken</code> to iterate pages in the list of returned compute fleets.</p>
            sort_order: <p>The order in which to list compute fleets. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List in ascending order.</p> </li> <li> <p> <code>DESCENDING</code>: List in descending order.</p> </li> </ul> <p>Use <code>sortBy</code> to specify the criterion to be used to list compute fleet names.</p>
            sort_by: <p>The criterion to be used to list compute fleet names. Valid values include:</p> <ul> <li> <p> <code>CREATED_TIME</code>: List based on when each compute fleet was created.</p> </li> <li> <p> <code>LAST_MODIFIED_TIME</code>: List based on when information about each compute fleet was last changed.</p> </li> <li> <p> <code>NAME</code>: List based on each compute fleet's name.</p> </li> </ul> <p>Use <code>sortOrder</code> to specify in what order to list the compute fleet names based on the preceding criteria.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_fleets_input.ListFleetsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_fleets_output.ListFleetsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_fleets

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_fleets.async_list_fleets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_fleets_input.ListFleetsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_fleets(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        next_token: Optional[
            "capo_codebuild.types.sensitive_string.SensitiveString"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional[
            "capo_codebuild.types.fleet_sort_by_type.FleetSortByType"
        ] = None,
    ) -> "AsyncIterator[capo_codebuild.types.list_fleets_output.ListFleetsOutput]":
        _token = next_token
        while True:
            _response = await self.list_fleets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                sort_order=sort_order,
                sort_by=sort_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_projects(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_by: Optional[
            "capo_codebuild.types.project_sort_by_type.ProjectSortByType"
        ] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_codebuild.types.list_projects_output.ListProjectsOutput":
        """<p>Gets a list of build project names, with each build project name representing a single build project.</p>

        Args:
            sort_by: <p>The criterion to be used to list build project names. Valid values include:</p> <ul> <li> <p> <code>CREATED_TIME</code>: List based on when each build project was created.</p> </li> <li> <p> <code>LAST_MODIFIED_TIME</code>: List based on when information about each build project was last changed.</p> </li> <li> <p> <code>NAME</code>: List based on each build project's name.</p> </li> </ul> <p>Use <code>sortOrder</code> to specify in what order to list the build project names based on the preceding criteria.</p>
            sort_order: <p>The order in which to list build projects. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List in ascending order.</p> </li> <li> <p> <code>DESCENDING</code>: List in descending order.</p> </li> </ul> <p>Use <code>sortBy</code> to specify the criterion to be used to list build project names.</p>
            next_token: <p>During a previous call, if there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_projects_input.ListProjectsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_projects_output.ListProjectsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_projects

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_projects.async_list_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_projects_input.ListProjectsInput = {}
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

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
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_by: Optional[
            "capo_codebuild.types.project_sort_by_type.ProjectSortByType"
        ] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_projects(
                config_overrides=config_overrides,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("projects",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_report_groups(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional[
            "capo_codebuild.types.report_group_sort_by_type.ReportGroupSortByType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
    ) -> "capo_codebuild.types.list_report_groups_output.ListReportGroupsOutput":
        """<p> Gets a list ARNs for the report groups in the current Amazon Web Services account. </p>

        Args:
            sort_order: <p> Used to specify the order to sort the list of returned report groups. Valid values are <code>ASCENDING</code> and <code>DESCENDING</code>. </p>
            sort_by: <p> The criterion to be used to list build report groups. Valid values include: </p> <ul> <li> <p> <code>CREATED_TIME</code>: List based on when each report group was created.</p> </li> <li> <p> <code>LAST_MODIFIED_TIME</code>: List based on when each report group was last changed.</p> </li> <li> <p> <code>NAME</code>: List based on each report group's name.</p> </li> </ul>
            next_token: <p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>
            max_results: <p> The maximum number of paginated report groups returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>ReportGroup</code> objects. The default value is 100. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_report_groups_input.ListReportGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_report_groups_output.ListReportGroupsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_report_groups

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_report_groups.async_list_report_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_report_groups_input.ListReportGroupsInput = {}
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def iter_list_report_groups(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional[
            "capo_codebuild.types.report_group_sort_by_type.ReportGroupSortByType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_report_groups(
                config_overrides=config_overrides,
                sort_order=sort_order,
                sort_by=sort_by,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("report_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_reports(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        filter: Optional["capo_codebuild.types.report_filter.ReportFilter"] = None,
    ) -> "capo_codebuild.types.list_reports_output.ListReportsOutput":
        """<p> Returns a list of ARNs for the reports in the current Amazon Web Services account. </p>

        Args:
            sort_order: <p> Specifies the sort order for the list of returned reports. Valid values are: </p> <ul> <li> <p> <code>ASCENDING</code>: return reports in chronological order based on their creation date. </p> </li> <li> <p> <code>DESCENDING</code>: return reports in the reverse chronological order based on their creation date. </p> </li> </ul>
            next_token: <p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>
            max_results: <p> The maximum number of paginated reports returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>Report</code> objects. The default value is 100. </p>
            filter: <p> A <code>ReportFilter</code> object used to filter the returned reports. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_reports_input.ListReportsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_reports_output.ListReportsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_reports

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_reports.async_list_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_reports_input.ListReportsInput = {}
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_reports(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        filter: Optional["capo_codebuild.types.report_filter.ReportFilter"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_reports(
                config_overrides=config_overrides,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_reports_for_report_group(
        self,
        report_group_arn: "capo_codebuild.types.string.String",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        filter: Optional["capo_codebuild.types.report_filter.ReportFilter"] = None,
    ) -> "capo_codebuild.types.list_reports_for_report_group_output.ListReportsForReportGroupOutput":
        """<p> Returns a list of ARNs for the reports that belong to a <code>ReportGroup</code>. </p>

        Args:
            report_group_arn: <p> The ARN of the report group for which you want to return report ARNs. </p>
            next_token: <p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>
            sort_order: <p> Use to specify whether the results are returned in ascending or descending order. </p>
            max_results: <p> The maximum number of paginated reports in this report group returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>Report</code> objects. The default value is 100. </p>
            filter: <p> A <code>ReportFilter</code> object used to filter the returned reports. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_reports_for_report_group_input.ListReportsForReportGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_reports_for_report_group_output.ListReportsForReportGroupOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_reports_for_report_group

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_reports_for_report_group.async_list_reports_for_report_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_reports_for_report_group_input.ListReportsForReportGroupInput = {
            "report_group_arn": report_group_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_reports_for_report_group(
        self,
        report_group_arn: "capo_codebuild.types.string.String",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        filter: Optional["capo_codebuild.types.report_filter.ReportFilter"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_reports_for_report_group(
                report_group_arn,
                config_overrides=config_overrides,
                next_token=_token,
                sort_order=sort_order,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sandboxes(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "capo_codebuild.types.list_sandboxes_output.ListSandboxesOutput":
        """<p>Gets a list of sandboxes.</p>

        Args:
            max_results: <p>The maximum number of sandbox records to be retrieved.</p>
            sort_order: <p>The order in which sandbox records should be retrieved.</p>
            next_token: <p>The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_sandboxes_input.ListSandboxesInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_sandboxes_output.ListSandboxesOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_sandboxes

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_sandboxes.async_list_sandboxes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_sandboxes_input.ListSandboxesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_sandboxes(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_sandboxes(
                config_overrides=config_overrides,
                max_results=max_results,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_sandboxes_for_project(
        self,
        project_name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional[
            "capo_codebuild.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "capo_codebuild.types.list_sandboxes_for_project_output.ListSandboxesForProjectOutput":
        """<p>Gets a list of sandboxes for a given project.</p>

        Args:
            project_name: <p>The CodeBuild project name.</p>
            max_results: <p>The maximum number of sandbox records to be retrieved.</p>
            sort_order: <p>The order in which sandbox records should be retrieved.</p>
            next_token: <p>The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_sandboxes_for_project_input.ListSandboxesForProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_sandboxes_for_project_output.ListSandboxesForProjectOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_sandboxes_for_project

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_sandboxes_for_project.async_list_sandboxes_for_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_sandboxes_for_project_input.ListSandboxesForProjectInput = {
            "project_name": project_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_sandboxes_for_project(
        self,
        project_name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        next_token: Optional[
            "capo_codebuild.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_sandboxes_for_project(
                project_name,
                config_overrides=config_overrides,
                max_results=max_results,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_shared_projects(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_by: Optional[
            "capo_codebuild.types.shared_resource_sort_by_type.SharedResourceSortByType"
        ] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_codebuild.types.list_shared_projects_output.ListSharedProjectsOutput":
        """<p> Gets a list of projects that are shared with other Amazon Web Services accounts or users. </p>

        Args:
            sort_by: <p> The criterion to be used to list build projects shared with the current Amazon Web Services account or user. Valid values include: </p> <ul> <li> <p> <code>ARN</code>: List based on the ARN. </p> </li> <li> <p> <code>MODIFIED_TIME</code>: List based on when information about the shared project was last changed. </p> </li> </ul>
            sort_order: <p>The order in which to list shared build projects. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List in ascending order.</p> </li> <li> <p> <code>DESCENDING</code>: List in descending order.</p> </li> </ul>
            max_results: <p> The maximum number of paginated shared build projects returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>Project</code> objects. The default value is 100. </p>
            next_token: <p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_shared_projects_input.ListSharedProjectsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_shared_projects_output.ListSharedProjectsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_shared_projects

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_shared_projects.async_list_shared_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_shared_projects_input.ListSharedProjectsInput = {}
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_shared_projects(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_by: Optional[
            "capo_codebuild.types.shared_resource_sort_by_type.SharedResourceSortByType"
        ] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_shared_projects(
                config_overrides=config_overrides,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("projects",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_shared_report_groups(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional[
            "capo_codebuild.types.shared_resource_sort_by_type.SharedResourceSortByType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
    ) -> "capo_codebuild.types.list_shared_report_groups_output.ListSharedReportGroupsOutput":
        """<p> Gets a list of report groups that are shared with other Amazon Web Services accounts or users. </p>

        Args:
            sort_order: <p>The order in which to list shared report groups. Valid values include:</p> <ul> <li> <p> <code>ASCENDING</code>: List in ascending order.</p> </li> <li> <p> <code>DESCENDING</code>: List in descending order.</p> </li> </ul>
            sort_by: <p> The criterion to be used to list report groups shared with the current Amazon Web Services account or user. Valid values include: </p> <ul> <li> <p> <code>ARN</code>: List based on the ARN. </p> </li> <li> <p> <code>MODIFIED_TIME</code>: List based on when information about the shared report group was last changed. </p> </li> </ul>
            next_token: <p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>
            max_results: <p> The maximum number of paginated shared report groups per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>ReportGroup</code> objects. The default value is 100. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_shared_report_groups_input.ListSharedReportGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_shared_report_groups_output.ListSharedReportGroupsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_shared_report_groups

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_shared_report_groups.async_list_shared_report_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_shared_report_groups_input.ListSharedReportGroupsInput = {}
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def iter_list_shared_report_groups(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        sort_order: Optional[
            "capo_codebuild.types.sort_order_type.SortOrderType"
        ] = None,
        sort_by: Optional[
            "capo_codebuild.types.shared_resource_sort_by_type.SharedResourceSortByType"
        ] = None,
        next_token: Optional["capo_codebuild.types.string.String"] = None,
        max_results: Optional["capo_codebuild.types.page_size.PageSize"] = None,
    ) -> "AsyncIterator[capo_codebuild.types.non_empty_string.NonEmptyString]":
        _token = next_token
        while True:
            _response = await self.list_shared_report_groups(
                config_overrides=config_overrides,
                sort_order=sort_order,
                sort_by=sort_by,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("report_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_source_credentials(
        self, *, config_overrides: Optional[AsyncCodeBuildClientConfig] = None
    ) -> "capo_codebuild.types.list_source_credentials_output.ListSourceCredentialsOutput":
        """<p> Returns a list of <code>SourceCredentialsInfo</code> objects. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.list_source_credentials_input.ListSourceCredentialsInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.list_source_credentials_output.ListSourceCredentialsOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.list_source_credentials

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.list_source_credentials.async_list_source_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.list_source_credentials_input.ListSourceCredentialsInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        policy: "capo_codebuild.types.non_empty_string.NonEmptyString",
        resource_arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.put_resource_policy_output.PutResourcePolicyOutput":
        """<p> Stores a resource policy for the ARN of a <code>Project</code> or <code>ReportGroup</code> object. </p>

        Args:
            policy: <p> A JSON-formatted resource policy. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/project-sharing.html#project-sharing-share">Sharing a Project</a> and <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/report-groups-sharing.html#report-groups-sharing-share">Sharing a Report Group</a> in the <i>CodeBuild User Guide</i>. </p>
            resource_arn: <p> The ARN of the <code>Project</code> or <code>ReportGroup</code> resource you want to associate with a resource policy. </p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.put_resource_policy_input.PutResourcePolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.put_resource_policy_output.PutResourcePolicyOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.put_resource_policy_input.PutResourcePolicyInput = {
            "policy": policy,
            "resource_arn": resource_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retry_build(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        id: Optional["capo_codebuild.types.non_empty_string.NonEmptyString"] = None,
        idempotency_token: Optional["capo_codebuild.types.string.String"] = None,
    ) -> "capo_codebuild.types.retry_build_output.RetryBuildOutput":
        """<p>Restarts a build.</p>

        Args:
            id: <p>Specifies the identifier of the build to restart.</p>
            idempotency_token: <p>A unique, case sensitive identifier you provide to ensure the idempotency of the <code>RetryBuild</code> request. The token is included in the <code>RetryBuild</code> request and is valid for five minutes. If you repeat the <code>RetryBuild</code> request with the same token, but change a parameter, CodeBuild returns a parameter mismatch error.</p>

        Raises:
            capo_codebuild.errors.account_limit_exceeded_exception.AccountLimitExceededException: <p>An Amazon Web Services service limit was exceeded for the calling Amazon Web Services account.</p>
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.retry_build_input.RetryBuildInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.retry_build_output.RetryBuildOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.retry_build

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.retry_build.async_retry_build(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.retry_build_input.RetryBuildInput = {}
        if id is not None:
            input_["id"] = id
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retry_build_batch(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        id: Optional["capo_codebuild.types.non_empty_string.NonEmptyString"] = None,
        idempotency_token: Optional["capo_codebuild.types.string.String"] = None,
        retry_type: Optional[
            "capo_codebuild.types.retry_build_batch_type.RetryBuildBatchType"
        ] = None,
    ) -> "capo_codebuild.types.retry_build_batch_output.RetryBuildBatchOutput":
        """<p>Restarts a failed batch build. Only batch builds that have failed can be retried.</p>

        Args:
            id: <p>Specifies the identifier of the batch build to restart.</p>
            idempotency_token: <p>A unique, case sensitive identifier you provide to ensure the idempotency of the <code>RetryBuildBatch</code> request. The token is included in the <code>RetryBuildBatch</code> request and is valid for five minutes. If you repeat the <code>RetryBuildBatch</code> request with the same token, but change a parameter, CodeBuild returns a parameter mismatch error.</p>
            retry_type: <p>Specifies the type of retry to perform.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.retry_build_batch_input.RetryBuildBatchInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.retry_build_batch_output.RetryBuildBatchOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.retry_build_batch

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.retry_build_batch.async_retry_build_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.retry_build_batch_input.RetryBuildBatchInput = {}
        if id is not None:
            input_["id"] = id
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token
        if retry_type is not None:
            input_["retry_type"] = retry_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_build(
        self,
        project_name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        secondary_sources_override: Optional[
            "capo_codebuild.types.project_sources.ProjectSources"
        ] = None,
        secondary_sources_version_override: Optional[
            "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
        ] = None,
        source_version: Optional["capo_codebuild.types.string.String"] = None,
        artifacts_override: Optional[
            "capo_codebuild.types.project_artifacts.ProjectArtifacts"
        ] = None,
        secondary_artifacts_override: Optional[
            "capo_codebuild.types.project_artifacts_list.ProjectArtifactsList"
        ] = None,
        environment_variables_override: Optional[
            "capo_codebuild.types.environment_variables.EnvironmentVariables"
        ] = None,
        source_type_override: Optional[
            "capo_codebuild.types.source_type.SourceType"
        ] = None,
        source_location_override: Optional["capo_codebuild.types.string.String"] = None,
        source_auth_override: Optional[
            "capo_codebuild.types.source_auth.SourceAuth"
        ] = None,
        git_clone_depth_override: Optional[
            "capo_codebuild.types.git_clone_depth.GitCloneDepth"
        ] = None,
        git_submodules_config_override: Optional[
            "capo_codebuild.types.git_submodules_config.GitSubmodulesConfig"
        ] = None,
        buildspec_override: Optional["capo_codebuild.types.string.String"] = None,
        insecure_ssl_override: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        report_build_status_override: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        build_status_config_override: Optional[
            "capo_codebuild.types.build_status_config.BuildStatusConfig"
        ] = None,
        environment_type_override: Optional[
            "capo_codebuild.types.environment_type.EnvironmentType"
        ] = None,
        image_override: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        compute_type_override: Optional[
            "capo_codebuild.types.compute_type.ComputeType"
        ] = None,
        certificate_override: Optional["capo_codebuild.types.string.String"] = None,
        cache_override: Optional[
            "capo_codebuild.types.project_cache.ProjectCache"
        ] = None,
        service_role_override: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        privileged_mode_override: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        timeout_in_minutes_override: Optional[
            "capo_codebuild.types.build_time_out.BuildTimeOut"
        ] = None,
        queued_timeout_in_minutes_override: Optional[
            "capo_codebuild.types.time_out.TimeOut"
        ] = None,
        encryption_key_override: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        idempotency_token: Optional["capo_codebuild.types.string.String"] = None,
        logs_config_override: Optional[
            "capo_codebuild.types.logs_config.LogsConfig"
        ] = None,
        registry_credential_override: Optional[
            "capo_codebuild.types.registry_credential.RegistryCredential"
        ] = None,
        image_pull_credentials_type_override: Optional[
            "capo_codebuild.types.image_pull_credentials_type.ImagePullCredentialsType"
        ] = None,
        debug_session_enabled: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        fleet_override: Optional[
            "capo_codebuild.types.project_fleet.ProjectFleet"
        ] = None,
        auto_retry_limit_override: Optional[
            "capo_codebuild.types.wrapper_int.WrapperInt"
        ] = None,
        host_kernel_override: Optional[
            "capo_codebuild.types.host_kernel.HostKernel"
        ] = None,
    ) -> "capo_codebuild.types.start_build_output.StartBuildOutput":
        """<p>Starts running a build with the settings defined in the project. These setting include: how to run a build, where to get the source code, which build environment to use, which build commands to run, and where to store the build output.</p> <p>You can also start a build run by overriding some of the build settings in the project. The overrides only apply for that specific start build request. The settings in the project are unaltered.</p>

        Args:
            project_name: <p>The name of the CodeBuild build project to start running a build.</p>
            secondary_sources_override: <p> An array of <code>ProjectSource</code> objects. </p>
            secondary_sources_version_override: <p> An array of <code>ProjectSourceVersion</code> objects that specify one or more versions of the project's secondary sources to be used for this build only. </p>
            source_version: <p>The version of the build input to be built, for this build only. If not specified, the latest version is used. If specified, the contents depends on the source provider:</p> <dl> <dt>CodeCommit</dt> <dd> <p>The commit ID, branch, or Git tag to use.</p> </dd> <dt>GitHub</dt> <dd> <p>The commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </dd> <dt>GitLab</dt> <dd> <p>The commit ID, branch, or Git tag to use.</p> </dd> <dt>Bitbucket</dt> <dd> <p>The commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </dd> <dt>Amazon S3</dt> <dd> <p>The version ID of the object that represents the build input ZIP file to use.</p> </dd> </dl> <p>If <code>sourceVersion</code> is specified at the project level, then this <code>sourceVersion</code> (at the build level) takes precedence. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>
            artifacts_override: <p>Build output artifact settings that override, for this build only, the latest ones already defined in the build project.</p>
            secondary_artifacts_override: <p> An array of <code>ProjectArtifacts</code> objects. </p>
            environment_variables_override: <p>A set of environment variables that overrides, for this build only, the latest ones already defined in the build project.</p>
            source_type_override: <p>A source input type, for this build, that overrides the source input defined in the build project.</p>
            source_location_override: <p>A location that overrides, for this build, the source location for the one defined in the build project.</p>
            source_auth_override: <p>An authorization type for this build that overrides the one defined in the build project. This override applies only if the build project's source is BitBucket, GitHub, GitLab, or GitLab Self Managed.</p>
            git_clone_depth_override: <p>The user-defined depth of history, with a minimum value of 0, that overrides, for this build only, any previous depth of history defined in the build project.</p>
            git_submodules_config_override: <p> Information about the Git submodules configuration for this build of an CodeBuild build project. </p>
            buildspec_override: <p>A buildspec file declaration that overrides the latest one defined in the build project, for this build only. The buildspec defined on the project is not changed.</p> <p>If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in <code>CODEBUILD_SRC_DIR</code> environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, <code>arn:aws:s3:::my-codebuild-sample2/buildspec.yml</code>). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage">Buildspec File Name and Storage Location</a>.</p> <note> <p>Since this property allows you to change the build commands that will run in the container, you should note that an IAM principal with the ability to call this API and set this parameter can override the default settings. Moreover, we encourage that you use a trustworthy buildspec location like a file in your source repository or a Amazon S3 bucket. Alternatively, you can restrict overrides to the buildspec by using a condition key: <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/action-context-keys.html#action-context-keys-example-overridebuildspec.html">Prevent unauthorized modifications to project buildspec</a>.</p> </note>
            insecure_ssl_override: <p>Enable this flag to override the insecure SSL setting that is specified in the build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the build's source is GitHub Enterprise.</p>
            report_build_status_override: <p> Set to true to report to your source provider the status of a build's start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, or Bitbucket, an <code>invalidInputException</code> is thrown. </p> <p>To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html">Source provider access</a> in the <i>CodeBuild User Guide</i>.</p> <note> <p> The status of a build triggered by a webhook is always reported to your source provider. </p> </note>
            build_status_config_override: <p>Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is <code>GITHUB</code>, <code>GITHUB_ENTERPRISE</code>, or <code>BITBUCKET</code>.</p>
            environment_type_override: <p>A container type for this build that overrides the one specified in the build project.</p>
            image_override: <p>The name of an image for this build that overrides the one specified in the build project.</p>
            compute_type_override: <p>The name of a compute type for this build that overrides the one specified in the build project.</p>
            certificate_override: <p>The name of a certificate for this build that overrides the one specified in the build project.</p>
            cache_override: <p>A ProjectCache object specified for this build that overrides the one defined in the build project.</p>
            service_role_override: <p>The name of a service role for this build that overrides the one specified in the build project.</p>
            privileged_mode_override: <p>Enable this flag to override privileged mode in the build project.</p>
            timeout_in_minutes_override: <p>The number of build timeout minutes, from 5 to 2160 (36 hours), that overrides, for this build only, the latest setting already defined in the build project.</p>
            queued_timeout_in_minutes_override: <p> The number of minutes a build is allowed to be queued before it times out. </p>
            encryption_key_override: <p>The Key Management Service customer master key (CMK) that overrides the one specified in the build project. The CMK key encrypts the build output artifacts.</p> <note> <p> You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>).</p>
            idempotency_token: <p>A unique, case sensitive identifier you provide to ensure the idempotency of the StartBuild request. The token is included in the StartBuild request and is valid for 5 minutes. If you repeat the StartBuild request with the same token, but change a parameter, CodeBuild returns a parameter mismatch error. </p>
            logs_config_override: <p> Log settings for this build that override the log settings defined in the build project. </p>
            registry_credential_override: <p> The credentials for access to a private registry. </p>
            image_pull_credentials_type_override: <p>The type of credentials CodeBuild uses to pull images in your build. There are two valid values: </p> <dl> <dt>CODEBUILD</dt> <dd> <p>Specifies that CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust CodeBuild's service principal.</p> </dd> <dt>SERVICE_ROLE</dt> <dd> <p>Specifies that CodeBuild uses your build project's service role. </p> </dd> </dl> <p>When using a cross-account or private registry image, you must use <code>SERVICE_ROLE</code> credentials. When using an CodeBuild curated image, you must use <code>CODEBUILD</code> credentials. </p>
            debug_session_enabled: <p>Specifies if session debugging is enabled for this build. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html">Viewing a running build in Session Manager</a>.</p>
            fleet_override: <p>A ProjectFleet object specified for this build that overrides the one defined in the build project.</p>
            auto_retry_limit_override: <p>The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the <code>RetryBuild</code> API to automatically retry your build for up to 2 additional times.</p>
            host_kernel_override: <p>The host operating system kernel for this build that overrides the one specified in the build project.</p>

        Raises:
            capo_codebuild.errors.account_limit_exceeded_exception.AccountLimitExceededException: <p>An Amazon Web Services service limit was exceeded for the calling Amazon Web Services account.</p>
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.start_build_input.StartBuildInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.start_build_output.StartBuildOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.start_build

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.start_build.async_start_build(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.start_build_input.StartBuildInput = {
            "project_name": project_name
        }
        if secondary_sources_override is not None:
            input_["secondary_sources_override"] = secondary_sources_override
        if secondary_sources_version_override is not None:
            input_["secondary_sources_version_override"] = (
                secondary_sources_version_override
            )
        if source_version is not None:
            input_["source_version"] = source_version
        if artifacts_override is not None:
            input_["artifacts_override"] = artifacts_override
        if secondary_artifacts_override is not None:
            input_["secondary_artifacts_override"] = secondary_artifacts_override
        if environment_variables_override is not None:
            input_["environment_variables_override"] = environment_variables_override
        if source_type_override is not None:
            input_["source_type_override"] = source_type_override
        if source_location_override is not None:
            input_["source_location_override"] = source_location_override
        if source_auth_override is not None:
            input_["source_auth_override"] = source_auth_override
        if git_clone_depth_override is not None:
            input_["git_clone_depth_override"] = git_clone_depth_override
        if git_submodules_config_override is not None:
            input_["git_submodules_config_override"] = git_submodules_config_override
        if buildspec_override is not None:
            input_["buildspec_override"] = buildspec_override
        if insecure_ssl_override is not None:
            input_["insecure_ssl_override"] = insecure_ssl_override
        if report_build_status_override is not None:
            input_["report_build_status_override"] = report_build_status_override
        if build_status_config_override is not None:
            input_["build_status_config_override"] = build_status_config_override
        if environment_type_override is not None:
            input_["environment_type_override"] = environment_type_override
        if image_override is not None:
            input_["image_override"] = image_override
        if compute_type_override is not None:
            input_["compute_type_override"] = compute_type_override
        if certificate_override is not None:
            input_["certificate_override"] = certificate_override
        if cache_override is not None:
            input_["cache_override"] = cache_override
        if service_role_override is not None:
            input_["service_role_override"] = service_role_override
        if privileged_mode_override is not None:
            input_["privileged_mode_override"] = privileged_mode_override
        if timeout_in_minutes_override is not None:
            input_["timeout_in_minutes_override"] = timeout_in_minutes_override
        if queued_timeout_in_minutes_override is not None:
            input_["queued_timeout_in_minutes_override"] = (
                queued_timeout_in_minutes_override
            )
        if encryption_key_override is not None:
            input_["encryption_key_override"] = encryption_key_override
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token
        if logs_config_override is not None:
            input_["logs_config_override"] = logs_config_override
        if registry_credential_override is not None:
            input_["registry_credential_override"] = registry_credential_override
        if image_pull_credentials_type_override is not None:
            input_["image_pull_credentials_type_override"] = (
                image_pull_credentials_type_override
            )
        if debug_session_enabled is not None:
            input_["debug_session_enabled"] = debug_session_enabled
        if fleet_override is not None:
            input_["fleet_override"] = fleet_override
        if auto_retry_limit_override is not None:
            input_["auto_retry_limit_override"] = auto_retry_limit_override
        if host_kernel_override is not None:
            input_["host_kernel_override"] = host_kernel_override

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_build_batch(
        self,
        project_name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        secondary_sources_override: Optional[
            "capo_codebuild.types.project_sources.ProjectSources"
        ] = None,
        secondary_sources_version_override: Optional[
            "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
        ] = None,
        source_version: Optional["capo_codebuild.types.string.String"] = None,
        artifacts_override: Optional[
            "capo_codebuild.types.project_artifacts.ProjectArtifacts"
        ] = None,
        secondary_artifacts_override: Optional[
            "capo_codebuild.types.project_artifacts_list.ProjectArtifactsList"
        ] = None,
        environment_variables_override: Optional[
            "capo_codebuild.types.environment_variables.EnvironmentVariables"
        ] = None,
        source_type_override: Optional[
            "capo_codebuild.types.source_type.SourceType"
        ] = None,
        source_location_override: Optional["capo_codebuild.types.string.String"] = None,
        source_auth_override: Optional[
            "capo_codebuild.types.source_auth.SourceAuth"
        ] = None,
        git_clone_depth_override: Optional[
            "capo_codebuild.types.git_clone_depth.GitCloneDepth"
        ] = None,
        git_submodules_config_override: Optional[
            "capo_codebuild.types.git_submodules_config.GitSubmodulesConfig"
        ] = None,
        buildspec_override: Optional["capo_codebuild.types.string.String"] = None,
        insecure_ssl_override: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        report_build_batch_status_override: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        environment_type_override: Optional[
            "capo_codebuild.types.environment_type.EnvironmentType"
        ] = None,
        image_override: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        compute_type_override: Optional[
            "capo_codebuild.types.compute_type.ComputeType"
        ] = None,
        certificate_override: Optional["capo_codebuild.types.string.String"] = None,
        cache_override: Optional[
            "capo_codebuild.types.project_cache.ProjectCache"
        ] = None,
        service_role_override: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        privileged_mode_override: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        build_timeout_in_minutes_override: Optional[
            "capo_codebuild.types.build_time_out.BuildTimeOut"
        ] = None,
        queued_timeout_in_minutes_override: Optional[
            "capo_codebuild.types.time_out.TimeOut"
        ] = None,
        encryption_key_override: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        idempotency_token: Optional["capo_codebuild.types.string.String"] = None,
        logs_config_override: Optional[
            "capo_codebuild.types.logs_config.LogsConfig"
        ] = None,
        registry_credential_override: Optional[
            "capo_codebuild.types.registry_credential.RegistryCredential"
        ] = None,
        image_pull_credentials_type_override: Optional[
            "capo_codebuild.types.image_pull_credentials_type.ImagePullCredentialsType"
        ] = None,
        build_batch_config_override: Optional[
            "capo_codebuild.types.project_build_batch_config.ProjectBuildBatchConfig"
        ] = None,
        debug_session_enabled: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
    ) -> "capo_codebuild.types.start_build_batch_output.StartBuildBatchOutput":
        """<p>Starts a batch build for a project.</p>

        Args:
            project_name: <p>The name of the project.</p>
            secondary_sources_override: <p>An array of <code>ProjectSource</code> objects that override the secondary sources defined in the batch build project.</p>
            secondary_sources_version_override: <p>An array of <code>ProjectSourceVersion</code> objects that override the secondary source versions in the batch build project.</p>
            source_version: <p>The version of the batch build input to be built, for this build only. If not specified, the latest version is used. If specified, the contents depends on the source provider:</p> <dl> <dt>CodeCommit</dt> <dd> <p>The commit ID, branch, or Git tag to use.</p> </dd> <dt>GitHub</dt> <dd> <p>The commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </dd> <dt>Bitbucket</dt> <dd> <p>The commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </dd> <dt>Amazon S3</dt> <dd> <p>The version ID of the object that represents the build input ZIP file to use.</p> </dd> </dl> <p>If <code>sourceVersion</code> is specified at the project level, then this <code>sourceVersion</code> (at the build level) takes precedence. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>
            artifacts_override: <p>An array of <code>ProjectArtifacts</code> objects that contains information about the build output artifact overrides for the build project.</p>
            secondary_artifacts_override: <p>An array of <code>ProjectArtifacts</code> objects that override the secondary artifacts defined in the batch build project.</p>
            environment_variables_override: <p>An array of <code>EnvironmentVariable</code> objects that override, or add to, the environment variables defined in the batch build project.</p>
            source_type_override: <p>The source input type that overrides the source input defined in the batch build project.</p>
            source_location_override: <p>A location that overrides, for this batch build, the source location defined in the batch build project.</p>
            source_auth_override: <p>A <code>SourceAuth</code> object that overrides the one defined in the batch build project. This override applies only if the build project's source is BitBucket or GitHub.</p>
            git_clone_depth_override: <p>The user-defined depth of history, with a minimum value of 0, that overrides, for this batch build only, any previous depth of history defined in the batch build project.</p>
            git_submodules_config_override: <p>A <code>GitSubmodulesConfig</code> object that overrides the Git submodules configuration for this batch build.</p>
            buildspec_override: <p>A buildspec file declaration that overrides, for this build only, the latest one already defined in the build project.</p> <p>If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in <code>CODEBUILD_SRC_DIR</code> environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, <code>arn:aws:s3:::my-codebuild-sample2/buildspec.yml</code>). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage">Buildspec File Name and Storage Location</a>. </p>
            insecure_ssl_override: <p>Enable this flag to override the insecure SSL setting that is specified in the batch build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the build's source is GitHub Enterprise.</p>
            report_build_batch_status_override: <p>Set to <code>true</code> to report to your source provider the status of a batch build's start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, or Bitbucket, an <code>invalidInputException</code> is thrown. </p> <note> <p>The status of a build triggered by a webhook is always reported to your source provider. </p> </note>
            environment_type_override: <p>A container type for this batch build that overrides the one specified in the batch build project.</p>
            image_override: <p>The name of an image for this batch build that overrides the one specified in the batch build project.</p>
            compute_type_override: <p>The name of a compute type for this batch build that overrides the one specified in the batch build project.</p>
            certificate_override: <p>The name of a certificate for this batch build that overrides the one specified in the batch build project.</p>
            cache_override: <p>A <code>ProjectCache</code> object that specifies cache overrides.</p>
            service_role_override: <p>The name of a service role for this batch build that overrides the one specified in the batch build project.</p>
            privileged_mode_override: <p>Enable this flag to override privileged mode in the batch build project.</p>
            build_timeout_in_minutes_override: <p>Overrides the build timeout specified in the batch build project.</p>
            queued_timeout_in_minutes_override: <p>The number of minutes a batch build is allowed to be queued before it times out.</p>
            encryption_key_override: <p>The Key Management Service customer master key (CMK) that overrides the one specified in the batch build project. The CMK key encrypts the build output artifacts.</p> <note> <p>You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>).</p>
            idempotency_token: <p>A unique, case sensitive identifier you provide to ensure the idempotency of the <code>StartBuildBatch</code> request. The token is included in the <code>StartBuildBatch</code> request and is valid for five minutes. If you repeat the <code>StartBuildBatch</code> request with the same token, but change a parameter, CodeBuild returns a parameter mismatch error.</p>
            logs_config_override: <p>A <code>LogsConfig</code> object that override the log settings defined in the batch build project.</p>
            registry_credential_override: <p>A <code>RegistryCredential</code> object that overrides credentials for access to a private registry.</p>
            image_pull_credentials_type_override: <p>The type of credentials CodeBuild uses to pull images in your batch build. There are two valid values: </p> <dl> <dt>CODEBUILD</dt> <dd> <p>Specifies that CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust CodeBuild's service principal.</p> </dd> <dt>SERVICE_ROLE</dt> <dd> <p>Specifies that CodeBuild uses your build project's service role. </p> </dd> </dl> <p>When using a cross-account or private registry image, you must use <code>SERVICE_ROLE</code> credentials. When using an CodeBuild curated image, you must use <code>CODEBUILD</code> credentials. </p>
            build_batch_config_override: <p>A <code>BuildBatchConfigOverride</code> object that contains batch build configuration overrides.</p>
            debug_session_enabled: <p>Specifies if session debugging is enabled for this batch build. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html">Viewing a running build in Session Manager</a>. Batch session debugging is not supported for matrix batch builds.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.start_build_batch_input.StartBuildBatchInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.start_build_batch_output.StartBuildBatchOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.start_build_batch

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.start_build_batch.async_start_build_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.start_build_batch_input.StartBuildBatchInput = {
            "project_name": project_name
        }
        if secondary_sources_override is not None:
            input_["secondary_sources_override"] = secondary_sources_override
        if secondary_sources_version_override is not None:
            input_["secondary_sources_version_override"] = (
                secondary_sources_version_override
            )
        if source_version is not None:
            input_["source_version"] = source_version
        if artifacts_override is not None:
            input_["artifacts_override"] = artifacts_override
        if secondary_artifacts_override is not None:
            input_["secondary_artifacts_override"] = secondary_artifacts_override
        if environment_variables_override is not None:
            input_["environment_variables_override"] = environment_variables_override
        if source_type_override is not None:
            input_["source_type_override"] = source_type_override
        if source_location_override is not None:
            input_["source_location_override"] = source_location_override
        if source_auth_override is not None:
            input_["source_auth_override"] = source_auth_override
        if git_clone_depth_override is not None:
            input_["git_clone_depth_override"] = git_clone_depth_override
        if git_submodules_config_override is not None:
            input_["git_submodules_config_override"] = git_submodules_config_override
        if buildspec_override is not None:
            input_["buildspec_override"] = buildspec_override
        if insecure_ssl_override is not None:
            input_["insecure_ssl_override"] = insecure_ssl_override
        if report_build_batch_status_override is not None:
            input_["report_build_batch_status_override"] = (
                report_build_batch_status_override
            )
        if environment_type_override is not None:
            input_["environment_type_override"] = environment_type_override
        if image_override is not None:
            input_["image_override"] = image_override
        if compute_type_override is not None:
            input_["compute_type_override"] = compute_type_override
        if certificate_override is not None:
            input_["certificate_override"] = certificate_override
        if cache_override is not None:
            input_["cache_override"] = cache_override
        if service_role_override is not None:
            input_["service_role_override"] = service_role_override
        if privileged_mode_override is not None:
            input_["privileged_mode_override"] = privileged_mode_override
        if build_timeout_in_minutes_override is not None:
            input_["build_timeout_in_minutes_override"] = (
                build_timeout_in_minutes_override
            )
        if queued_timeout_in_minutes_override is not None:
            input_["queued_timeout_in_minutes_override"] = (
                queued_timeout_in_minutes_override
            )
        if encryption_key_override is not None:
            input_["encryption_key_override"] = encryption_key_override
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token
        if logs_config_override is not None:
            input_["logs_config_override"] = logs_config_override
        if registry_credential_override is not None:
            input_["registry_credential_override"] = registry_credential_override
        if image_pull_credentials_type_override is not None:
            input_["image_pull_credentials_type_override"] = (
                image_pull_credentials_type_override
            )
        if build_batch_config_override is not None:
            input_["build_batch_config_override"] = build_batch_config_override
        if debug_session_enabled is not None:
            input_["debug_session_enabled"] = debug_session_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_command_execution(
        self,
        sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        command: "capo_codebuild.types.sensitive_non_empty_string.SensitiveNonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        type: Optional["capo_codebuild.types.command_type.CommandType"] = None,
    ) -> "capo_codebuild.types.start_command_execution_output.StartCommandExecutionOutput":
        """<p>Starts a command execution.</p>

        Args:
            sandbox_id: <p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>
            command: <p>The command that needs to be executed.</p>
            type: <p>The command type.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.start_command_execution_input.StartCommandExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.start_command_execution_output.StartCommandExecutionOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.start_command_execution

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.start_command_execution.async_start_command_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.start_command_execution_input.StartCommandExecutionInput = {
            "sandbox_id": sandbox_id,
            "command": command,
        }
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_sandbox(
        self,
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        project_name: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        idempotency_token: Optional[
            "capo_codebuild.types.sensitive_string.SensitiveString"
        ] = None,
    ) -> "capo_codebuild.types.start_sandbox_output.StartSandboxOutput":
        """<p>Starts a sandbox.</p>

        Args:
            project_name: <p>The CodeBuild project name.</p>
            idempotency_token: <p>A unique client token.</p>

        Raises:
            capo_codebuild.errors.account_suspended_exception.AccountSuspendedException: <p>The CodeBuild access has been suspended for the calling Amazon Web Services account.</p>
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.start_sandbox_input.StartSandboxInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.start_sandbox_output.StartSandboxOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.start_sandbox

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.start_sandbox.async_start_sandbox(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.start_sandbox_input.StartSandboxInput = {}
        if project_name is not None:
            input_["project_name"] = project_name
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_sandbox_connection(
        self,
        sandbox_id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.start_sandbox_connection_output.StartSandboxConnectionOutput":
        """<p>Starts a sandbox connection.</p>

        Args:
            sandbox_id: <p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.start_sandbox_connection_input.StartSandboxConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.start_sandbox_connection_output.StartSandboxConnectionOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.start_sandbox_connection

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.start_sandbox_connection.async_start_sandbox_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.start_sandbox_connection_input.StartSandboxConnectionInput = {
            "sandbox_id": sandbox_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_build(
        self,
        id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.stop_build_output.StopBuildOutput":
        """<p>Attempts to stop running a build.</p>

        Args:
            id: <p>The ID of the build.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.stop_build_input.StopBuildInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.stop_build_output.StopBuildOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.stop_build

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.stop_build.async_stop_build(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.stop_build_input.StopBuildInput = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_build_batch(
        self,
        id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.stop_build_batch_output.StopBuildBatchOutput":
        """<p>Stops a running batch build.</p>

        Args:
            id: <p>The identifier of the batch build to stop.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.stop_build_batch_input.StopBuildBatchInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.stop_build_batch_output.StopBuildBatchOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.stop_build_batch

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.stop_build_batch.async_stop_build_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.stop_build_batch_input.StopBuildBatchInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_sandbox(
        self,
        id: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
    ) -> "capo_codebuild.types.stop_sandbox_output.StopSandboxOutput":
        """<p>Stops a sandbox.</p>

        Args:
            id: <p>Information about the requested sandbox ID.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.stop_sandbox_input.StopSandboxInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.stop_sandbox_output.StopSandboxOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.stop_sandbox

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.stop_sandbox.async_stop_sandbox(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.stop_sandbox_input.StopSandboxInput = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_fleet(
        self,
        arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        base_capacity: Optional[
            "capo_codebuild.types.fleet_capacity.FleetCapacity"
        ] = None,
        environment_type: Optional[
            "capo_codebuild.types.environment_type.EnvironmentType"
        ] = None,
        compute_type: Optional["capo_codebuild.types.compute_type.ComputeType"] = None,
        compute_configuration: Optional[
            "capo_codebuild.types.compute_configuration.ComputeConfiguration"
        ] = None,
        scaling_configuration: Optional[
            "capo_codebuild.types.scaling_configuration_input.ScalingConfigurationInput"
        ] = None,
        overflow_behavior: Optional[
            "capo_codebuild.types.fleet_overflow_behavior.FleetOverflowBehavior"
        ] = None,
        vpc_config: Optional["capo_codebuild.types.vpc_config.VpcConfig"] = None,
        proxy_configuration: Optional[
            "capo_codebuild.types.proxy_configuration.ProxyConfiguration"
        ] = None,
        image_id: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        fleet_service_role: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_codebuild.types.tag_list.TagList"] = None,
    ) -> "capo_codebuild.types.update_fleet_output.UpdateFleetOutput":
        """<p>Updates a compute fleet.</p>

        Args:
            arn: <p>The ARN of the compute fleet.</p>
            base_capacity: <p>The initial number of machines allocated to the compute ﬂeet, which deﬁnes the number of builds that can run in parallel.</p>
            environment_type: <p>The environment type of the compute fleet.</p> <ul> <li> <p>The environment type <code>ARM_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), EU (Frankfurt), and South America (São Paulo).</p> </li> <li> <p>The environment type <code>ARM_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_GPU_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), and Asia Pacific (Sydney).</p> </li> <li> <p>The environment type <code>MAC_ARM</code> is available for Medium fleets only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), and EU (Frankfurt)</p> </li> <li> <p>The environment type <code>MAC_ARM</code> is available for Large fleets only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), and Asia Pacific (Sydney).</p> </li> <li> <p>The environment type <code>WINDOWS_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>WINDOWS_SERVER_2019_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), Asia Pacific (Tokyo), Asia Pacific (Mumbai) and EU (Ireland).</p> </li> <li> <p>The environment type <code>WINDOWS_SERVER_2022_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Tokyo), South America (São Paulo) and Asia Pacific (Mumbai).</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html">Build environment compute types</a> in the <i>CodeBuild user guide</i>.</p>
            compute_type: <p>Information about the compute resources the compute fleet uses. Available values include:</p> <ul> <li> <p> <code>ATTRIBUTE_BASED_COMPUTE</code>: Specify the amount of vCPUs, memory, disk space, and the type of machine.</p> <note> <p> If you use <code>ATTRIBUTE_BASED_COMPUTE</code>, you must define your attributes by using <code>computeConfiguration</code>. CodeBuild will select the cheapest instance that satisfies your specified attributes. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.types">Reserved capacity environment types</a> in the <i>CodeBuild User Guide</i>.</p> </note> </li> <li> <p> <code>CUSTOM_INSTANCE_TYPE</code>: Specify the instance type for your compute fleet. For a list of supported instance types, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.instance-types">Supported instance families </a> in the <i>CodeBuild User Guide</i>.</p> </li> <li> <p> <code>BUILD_GENERAL1_SMALL</code>: Use up to 4 GiB memory and 2 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_MEDIUM</code>: Use up to 8 GiB memory and 4 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_LARGE</code>: Use up to 16 GiB memory and 8 vCPUs for builds, depending on your environment type.</p> </li> <li> <p> <code>BUILD_GENERAL1_XLARGE</code>: Use up to 72 GiB memory and 36 vCPUs for builds, depending on your environment type.</p> </li> <li> <p> <code>BUILD_GENERAL1_2XLARGE</code>: Use up to 144 GiB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.</p> </li> <li> <p> <code>BUILD_LAMBDA_1GB</code>: Use up to 1 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_2GB</code>: Use up to 2 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_4GB</code>: Use up to 4 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_8GB</code>: Use up to 8 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_10GB</code>: Use up to 10 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> </ul> <p> If you use <code>BUILD_GENERAL1_SMALL</code>: </p> <ul> <li> <p> For environment type <code>LINUX_CONTAINER</code>, you can use up to 4 GiB memory and 2 vCPUs for builds. </p> </li> <li> <p> For environment type <code>LINUX_GPU_CONTAINER</code>, you can use up to 16 GiB memory, 4 vCPUs, and 1 NVIDIA A10G Tensor Core GPU for builds.</p> </li> <li> <p> For environment type <code>ARM_CONTAINER</code>, you can use up to 4 GiB memory and 2 vCPUs on ARM-based processors for builds.</p> </li> </ul> <p> If you use <code>BUILD_GENERAL1_LARGE</code>: </p> <ul> <li> <p> For environment type <code>LINUX_CONTAINER</code>, you can use up to 16 GiB memory and 8 vCPUs for builds. </p> </li> <li> <p> For environment type <code>LINUX_GPU_CONTAINER</code>, you can use up to 255 GiB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.</p> </li> <li> <p> For environment type <code>ARM_CONTAINER</code>, you can use up to 16 GiB memory and 8 vCPUs on ARM-based processors for builds.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment.types">On-demand environment types</a> in the <i>CodeBuild User Guide.</i> </p>
            compute_configuration: <p>The compute configuration of the compute fleet. This is only required if <code>computeType</code> is set to <code>ATTRIBUTE_BASED_COMPUTE</code> or <code>CUSTOM_INSTANCE_TYPE</code>.</p>
            scaling_configuration: <p>The scaling configuration of the compute fleet.</p>
            overflow_behavior: <p>The compute fleet overflow behavior.</p> <ul> <li> <p>For overflow behavior <code>QUEUE</code>, your overflow builds need to wait on the existing fleet instance to become available.</p> </li> <li> <p>For overflow behavior <code>ON_DEMAND</code>, your overflow builds run on CodeBuild on-demand.</p> <note> <p>If you choose to set your overflow behavior to on-demand while creating a VPC-connected fleet, make sure that you add the required VPC permissions to your project service role. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-create-vpc-network-interface">Example policy statement to allow CodeBuild access to Amazon Web Services services required to create a VPC network interface</a>.</p> </note> </li> </ul>
            proxy_configuration: <p>The proxy configuration of the compute fleet.</p>
            image_id: <p>The Amazon Machine Image (AMI) of the compute fleet.</p>
            fleet_service_role: <p>The service role associated with the compute fleet. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-permission-policy-fleet-service-role.html"> Allow a user to add a permission policy for a fleet service role</a> in the <i>CodeBuild User Guide</i>.</p>
            tags: <p>A list of tag key and value pairs associated with this compute fleet.</p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.</p>

        Raises:
            capo_codebuild.errors.account_limit_exceeded_exception.AccountLimitExceededException: <p>An Amazon Web Services service limit was exceeded for the calling Amazon Web Services account.</p>
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.update_fleet_input.UpdateFleetInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.update_fleet_output.UpdateFleetOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.update_fleet

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.update_fleet.async_update_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.update_fleet_input.UpdateFleetInput = {"arn": arn}
        if base_capacity is not None:
            input_["base_capacity"] = base_capacity
        if environment_type is not None:
            input_["environment_type"] = environment_type
        if compute_type is not None:
            input_["compute_type"] = compute_type
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if scaling_configuration is not None:
            input_["scaling_configuration"] = scaling_configuration
        if overflow_behavior is not None:
            input_["overflow_behavior"] = overflow_behavior
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if proxy_configuration is not None:
            input_["proxy_configuration"] = proxy_configuration
        if image_id is not None:
            input_["image_id"] = image_id
        if fleet_service_role is not None:
            input_["fleet_service_role"] = fleet_service_role
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_project(
        self,
        name: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        description: Optional[
            "capo_codebuild.types.project_description.ProjectDescription"
        ] = None,
        source: Optional["capo_codebuild.types.project_source.ProjectSource"] = None,
        secondary_sources: Optional[
            "capo_codebuild.types.project_sources.ProjectSources"
        ] = None,
        source_version: Optional["capo_codebuild.types.string.String"] = None,
        secondary_source_versions: Optional[
            "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
        ] = None,
        artifacts: Optional[
            "capo_codebuild.types.project_artifacts.ProjectArtifacts"
        ] = None,
        secondary_artifacts: Optional[
            "capo_codebuild.types.project_artifacts_list.ProjectArtifactsList"
        ] = None,
        cache: Optional["capo_codebuild.types.project_cache.ProjectCache"] = None,
        environment: Optional[
            "capo_codebuild.types.project_environment.ProjectEnvironment"
        ] = None,
        service_role: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        timeout_in_minutes: Optional[
            "capo_codebuild.types.build_time_out.BuildTimeOut"
        ] = None,
        queued_timeout_in_minutes: Optional[
            "capo_codebuild.types.time_out.TimeOut"
        ] = None,
        encryption_key: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_codebuild.types.tag_list.TagList"] = None,
        vpc_config: Optional["capo_codebuild.types.vpc_config.VpcConfig"] = None,
        badge_enabled: Optional[
            "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
        ] = None,
        logs_config: Optional["capo_codebuild.types.logs_config.LogsConfig"] = None,
        file_system_locations: Optional[
            "capo_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
        ] = None,
        build_batch_config: Optional[
            "capo_codebuild.types.project_build_batch_config.ProjectBuildBatchConfig"
        ] = None,
        concurrent_build_limit: Optional[
            "capo_codebuild.types.wrapper_int.WrapperInt"
        ] = None,
        auto_retry_limit: Optional[
            "capo_codebuild.types.wrapper_int.WrapperInt"
        ] = None,
    ) -> "capo_codebuild.types.update_project_output.UpdateProjectOutput":
        """<p>Changes the settings of a build project.</p>

        Args:
            name: <p>The name of the build project.</p> <note> <p>You cannot change a build project's name.</p> </note>
            description: <p>A new or replacement description of the build project.</p>
            source: <p>Information to be changed about the build input source code for the build project.</p>
            secondary_sources: <p> An array of <code>ProjectSource</code> objects. </p>
            source_version: <p> A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of: </p> <ul> <li> <p>For CodeCommit: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For GitLab: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Amazon S3: the version ID of the object that represents the build input ZIP file to use.</p> </li> </ul> <p> If <code>sourceVersion</code> is specified at the build level, then that version takes precedence over this <code>sourceVersion</code> (at the project level). </p> <p> For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>
            secondary_source_versions: <p> An array of <code>ProjectSourceVersion</code> objects. If <code>secondarySourceVersions</code> is specified at the build level, then they take over these <code>secondarySourceVersions</code> (at the project level). </p>
            artifacts: <p>Information to be changed about the build output artifacts for the build project.</p>
            secondary_artifacts: <p> An array of <code>ProjectArtifact</code> objects. </p>
            cache: <p>Stores recently used information so that it can be quickly accessed at a later time.</p>
            environment: <p>Information to be changed about the build environment for the build project.</p>
            service_role: <p>The replacement ARN of the IAM role that enables CodeBuild to interact with dependent Amazon Web Services services on behalf of the Amazon Web Services account.</p>
            timeout_in_minutes: <p>The replacement value in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out any related build that did not get marked as completed.</p>
            queued_timeout_in_minutes: <p> The number of minutes a build is allowed to be queued before it times out. </p>
            encryption_key: <p>The Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.</p> <note> <p> You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>). </p>
            tags: <p>An updated list of tag key and value pairs associated with this build project.</p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.</p>
            vpc_config: <p>VpcConfig enables CodeBuild to access resources in an Amazon VPC.</p>
            badge_enabled: <p>Set this to true to generate a publicly accessible URL for your project's build badge.</p>
            logs_config: <p> Information about logs for the build project. A project can create logs in CloudWatch Logs, logs in an S3 bucket, or both. </p>
            file_system_locations: <p> An array of <code>ProjectFileSystemLocation</code> objects for a CodeBuild build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>
            concurrent_build_limit: <p>The maximum number of concurrent builds that are allowed for this project.</p> <p>New builds are only started if the current number of builds is less than or equal to this limit. If the current build count meets this limit, new builds are throttled and are not run.</p> <p>To remove this limit, set this value to -1.</p>
            auto_retry_limit: <p>The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the <code>RetryBuild</code> API to automatically retry your build for up to 2 additional times.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.update_project_input.UpdateProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.update_project_output.UpdateProjectOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.update_project

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.update_project.async_update_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.update_project_input.UpdateProjectInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if source is not None:
            input_["source"] = source
        if secondary_sources is not None:
            input_["secondary_sources"] = secondary_sources
        if source_version is not None:
            input_["source_version"] = source_version
        if secondary_source_versions is not None:
            input_["secondary_source_versions"] = secondary_source_versions
        if artifacts is not None:
            input_["artifacts"] = artifacts
        if secondary_artifacts is not None:
            input_["secondary_artifacts"] = secondary_artifacts
        if cache is not None:
            input_["cache"] = cache
        if environment is not None:
            input_["environment"] = environment
        if service_role is not None:
            input_["service_role"] = service_role
        if timeout_in_minutes is not None:
            input_["timeout_in_minutes"] = timeout_in_minutes
        if queued_timeout_in_minutes is not None:
            input_["queued_timeout_in_minutes"] = queued_timeout_in_minutes
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if tags is not None:
            input_["tags"] = tags
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if badge_enabled is not None:
            input_["badge_enabled"] = badge_enabled
        if logs_config is not None:
            input_["logs_config"] = logs_config
        if file_system_locations is not None:
            input_["file_system_locations"] = file_system_locations
        if build_batch_config is not None:
            input_["build_batch_config"] = build_batch_config
        if concurrent_build_limit is not None:
            input_["concurrent_build_limit"] = concurrent_build_limit
        if auto_retry_limit is not None:
            input_["auto_retry_limit"] = auto_retry_limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_project_visibility(
        self,
        project_arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        project_visibility: "capo_codebuild.types.project_visibility_type.ProjectVisibilityType",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        resource_access_role: Optional[
            "capo_codebuild.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_codebuild.types.update_project_visibility_output.UpdateProjectVisibilityOutput":
        """<p>Changes the public visibility for a project. The project's build results, logs, and artifacts are available to the general public. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/public-builds.html">Public build projects</a> in the <i>CodeBuild User Guide</i>.</p> <important> <p>The following should be kept in mind when making your projects public:</p> <ul> <li> <p>All of a project's build results, logs, and artifacts, including builds that were run when the project was private, are available to the general public.</p> </li> <li> <p>All build logs and artifacts are available to the public. Environment variables, source code, and other sensitive information may have been output to the build logs and artifacts. You must be careful about what information is output to the build logs. Some best practice are:</p> <ul> <li> <p>Do not store sensitive values in environment variables. We recommend that you use an Amazon EC2 Systems Manager Parameter Store or Secrets Manager to store sensitive values.</p> </li> <li> <p>Follow <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/webhooks.html#webhook-best-practices">Best practices for using webhooks</a> in the <i>CodeBuild User Guide</i> to limit which entities can trigger a build, and do not store the buildspec in the project itself, to ensure that your webhooks are as secure as possible.</p> </li> </ul> </li> <li> <p>A malicious user can use public builds to distribute malicious artifacts. We recommend that you review all pull requests to verify that the pull request is a legitimate change. We also recommend that you validate any artifacts with their checksums to make sure that the correct artifacts are being downloaded.</p> </li> </ul> </important>

        Args:
            project_arn: <p>The Amazon Resource Name (ARN) of the build project.</p>
            resource_access_role: <p>The ARN of the IAM role that enables CodeBuild to access the CloudWatch Logs and Amazon S3 artifacts for the project's builds.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.update_project_visibility_input.UpdateProjectVisibilityInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.update_project_visibility_output.UpdateProjectVisibilityOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.update_project_visibility

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.update_project_visibility.async_update_project_visibility(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.update_project_visibility_input.UpdateProjectVisibilityInput = {
            "project_arn": project_arn,
            "project_visibility": project_visibility,
        }
        if resource_access_role is not None:
            input_["resource_access_role"] = resource_access_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_report_group(
        self,
        arn: "capo_codebuild.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        export_config: Optional[
            "capo_codebuild.types.report_export_config.ReportExportConfig"
        ] = None,
        tags: Optional["capo_codebuild.types.tag_list.TagList"] = None,
    ) -> "capo_codebuild.types.update_report_group_output.UpdateReportGroupOutput":
        """<p> Updates a report group. </p>

        Args:
            arn: <p> The ARN of the report group to update. </p>
            export_config: <p> Used to specify an updated export type. Valid values are: </p> <ul> <li> <p> <code>S3</code>: The report results are exported to an S3 bucket. </p> </li> <li> <p> <code>NO_EXPORT</code>: The report results are not exported. </p> </li> </ul>
            tags: <p> An updated list of tag key and value pairs associated with this report group. </p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild report group tags.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.update_report_group_input.UpdateReportGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.update_report_group_output.UpdateReportGroupOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.update_report_group

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.update_report_group.async_update_report_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.update_report_group_input.UpdateReportGroupInput = {
            "arn": arn
        }
        if export_config is not None:
            input_["export_config"] = export_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_webhook(
        self,
        project_name: "capo_codebuild.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncCodeBuildClientConfig] = None,
        branch_filter: Optional["capo_codebuild.types.string.String"] = None,
        rotate_secret: Optional["capo_codebuild.types.boolean.Boolean"] = None,
        filter_groups: Optional[
            "capo_codebuild.types.filter_groups.FilterGroups"
        ] = None,
        build_type: Optional[
            "capo_codebuild.types.webhook_build_type.WebhookBuildType"
        ] = None,
        pull_request_build_policy: Optional[
            "capo_codebuild.types.pull_request_build_policy.PullRequestBuildPolicy"
        ] = None,
    ) -> "capo_codebuild.types.update_webhook_output.UpdateWebhookOutput":
        """<p> Updates the webhook associated with an CodeBuild build project. </p> <note> <p> If you use Bitbucket for your repository, <code>rotateSecret</code> is ignored. </p> </note>

        Args:
            project_name: <p>The name of the CodeBuild project.</p>
            branch_filter: <p>A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If <code>branchFilter</code> is empty, then all branches are built.</p> <note> <p> It is recommended that you use <code>filterGroups</code> instead of <code>branchFilter</code>. </p> </note>
            rotate_secret: <p> A boolean value that specifies whether the associated GitHub repository's secret token should be updated. If you use Bitbucket for your repository, <code>rotateSecret</code> is ignored. </p>
            filter_groups: <p> An array of arrays of <code>WebhookFilter</code> objects used to determine if a webhook event can trigger a build. A filter group must contain at least one <code>EVENT</code> <code>WebhookFilter</code>. </p>
            build_type: <p>Specifies the type of build this webhook will trigger.</p> <note> <p> <code>RUNNER_BUILDKITE_BUILD</code> is only available for <code>NO_SOURCE</code> source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html">Tutorial: Configure a CodeBuild-hosted Buildkite runner</a> in the <i>CodeBuild user guide</i>.</p> </note>
            pull_request_build_policy: <p>A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests. This policy helps control when automated builds are executed based on contributor permissions and approval workflows.</p>

        Raises:
            capo_codebuild.errors.invalid_input_exception.InvalidInputException: <p>The input value that was provided is not valid.</p>
            capo_codebuild.errors.o_auth_provider_exception.OAuthProviderException: <p>There was a problem with the underlying OAuth provider.</p>
            capo_codebuild.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified Amazon Web Services resource cannot be found.</p>
            capo_codebuild.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codebuild.types.update_webhook_input.UpdateWebhookInput]",
        ) -> AsyncOperationResponse[
            "capo_codebuild.types.update_webhook_output.UpdateWebhookOutput"
        ]:
            import capo_codebuild._operations.code_build_20161006.update_webhook

            (
                output,
                http_response,
            ) = await capo_codebuild._operations.code_build_20161006.update_webhook.async_update_webhook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codebuild.types.update_webhook_input.UpdateWebhookInput = {
            "project_name": project_name
        }
        if branch_filter is not None:
            input_["branch_filter"] = branch_filter
        if rotate_secret is not None:
            input_["rotate_secret"] = rotate_secret
        if filter_groups is not None:
            input_["filter_groups"] = filter_groups
        if build_type is not None:
            input_["build_type"] = build_type
        if pull_request_build_policy is not None:
            input_["pull_request_build_policy"] = pull_request_build_policy

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
