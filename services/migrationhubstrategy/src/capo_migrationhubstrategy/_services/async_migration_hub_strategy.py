"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AWSMigrationHubStrategyRecommendation``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_migrationhubstrategy._auth._signers
import capo_migrationhubstrategy._auth._sigv4
from capo_migrationhubstrategy._auth._identity import Credentials
from capo_migrationhubstrategy._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_migrationhubstrategy._auth._zapros_handler import AuthMiddleware
from capo_migrationhubstrategy._pagination import resolve_path as _resolve_path
from capo_migrationhubstrategy._services._aws_config import aaws_config
from capo_migrationhubstrategy._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.analyzable_server_summary
    import capo_migrationhubstrategy.types.app_type
    import capo_migrationhubstrategy.types.application_component_criteria
    import capo_migrationhubstrategy.types.application_component_detail
    import capo_migrationhubstrategy.types.application_component_id
    import capo_migrationhubstrategy.types.application_mode
    import capo_migrationhubstrategy.types.application_preferences
    import capo_migrationhubstrategy.types.assessment_data_source_type
    import capo_migrationhubstrategy.types.assessment_targets
    import capo_migrationhubstrategy.types.associated_application
    import capo_migrationhubstrategy.types.async_task_id
    import capo_migrationhubstrategy.types.boolean
    import capo_migrationhubstrategy.types.collector
    import capo_migrationhubstrategy.types.data_source_type
    import capo_migrationhubstrategy.types.database_preferences
    import capo_migrationhubstrategy.types.get_application_component_details_request
    import capo_migrationhubstrategy.types.get_application_component_details_response
    import capo_migrationhubstrategy.types.get_application_component_strategies_request
    import capo_migrationhubstrategy.types.get_application_component_strategies_response
    import capo_migrationhubstrategy.types.get_assessment_request
    import capo_migrationhubstrategy.types.get_assessment_response
    import capo_migrationhubstrategy.types.get_import_file_task_request
    import capo_migrationhubstrategy.types.get_import_file_task_response
    import capo_migrationhubstrategy.types.get_latest_assessment_id_request
    import capo_migrationhubstrategy.types.get_latest_assessment_id_response
    import capo_migrationhubstrategy.types.get_portfolio_preferences_request
    import capo_migrationhubstrategy.types.get_portfolio_preferences_response
    import capo_migrationhubstrategy.types.get_portfolio_summary_request
    import capo_migrationhubstrategy.types.get_portfolio_summary_response
    import capo_migrationhubstrategy.types.get_recommendation_report_details_request
    import capo_migrationhubstrategy.types.get_recommendation_report_details_response
    import capo_migrationhubstrategy.types.get_server_details_request
    import capo_migrationhubstrategy.types.get_server_details_response
    import capo_migrationhubstrategy.types.get_server_strategies_request
    import capo_migrationhubstrategy.types.get_server_strategies_response
    import capo_migrationhubstrategy.types.group_ids
    import capo_migrationhubstrategy.types.import_file_task_information
    import capo_migrationhubstrategy.types.import_s3_bucket
    import capo_migrationhubstrategy.types.inclusion_status
    import capo_migrationhubstrategy.types.integer
    import capo_migrationhubstrategy.types.list_analyzable_servers_request
    import capo_migrationhubstrategy.types.list_analyzable_servers_response
    import capo_migrationhubstrategy.types.list_application_components_request
    import capo_migrationhubstrategy.types.list_application_components_response
    import capo_migrationhubstrategy.types.list_collectors_request
    import capo_migrationhubstrategy.types.list_collectors_response
    import capo_migrationhubstrategy.types.list_import_file_task_request
    import capo_migrationhubstrategy.types.list_import_file_task_response
    import capo_migrationhubstrategy.types.list_servers_request
    import capo_migrationhubstrategy.types.list_servers_response
    import capo_migrationhubstrategy.types.max_result
    import capo_migrationhubstrategy.types.next_token
    import capo_migrationhubstrategy.types.output_format
    import capo_migrationhubstrategy.types.prioritize_business_goals
    import capo_migrationhubstrategy.types.put_portfolio_preferences_request
    import capo_migrationhubstrategy.types.put_portfolio_preferences_response
    import capo_migrationhubstrategy.types.recommendation_task_id
    import capo_migrationhubstrategy.types.secrets_manager_key
    import capo_migrationhubstrategy.types.server_criteria
    import capo_migrationhubstrategy.types.server_detail
    import capo_migrationhubstrategy.types.server_id
    import capo_migrationhubstrategy.types.sort_order
    import capo_migrationhubstrategy.types.source_code_list
    import capo_migrationhubstrategy.types.start_assessment_request
    import capo_migrationhubstrategy.types.start_assessment_response
    import capo_migrationhubstrategy.types.start_import_file_task_request
    import capo_migrationhubstrategy.types.start_import_file_task_response
    import capo_migrationhubstrategy.types.start_recommendation_report_generation_request
    import capo_migrationhubstrategy.types.start_recommendation_report_generation_response
    import capo_migrationhubstrategy.types.stop_assessment_request
    import capo_migrationhubstrategy.types.stop_assessment_response
    import capo_migrationhubstrategy.types.strategy_option
    import capo_migrationhubstrategy.types.string
    import capo_migrationhubstrategy.types.update_application_component_config_request
    import capo_migrationhubstrategy.types.update_application_component_config_response
    import capo_migrationhubstrategy.types.update_server_config_request
    import capo_migrationhubstrategy.types.update_server_config_response


class AsyncMigrationHubStrategyClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMigrationHubStrategyClient:
    """A client for the ``MigrationHubStrategy`` service.

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
        self._config = AsyncMigrationHubStrategyClientConfig(
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
        self, config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMigrationHubStrategyClientConfig = config_overrides or {}
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

    async def get_application_component_details(
        self,
        application_component_id: "capo_migrationhubstrategy.types.application_component_id.ApplicationComponentId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.get_application_component_details_response.GetApplicationComponentDetailsResponse":
        """<p> Retrieves details about an application component. </p>

        Args:
            application_component_id: <p> The ID of the application component. The ID is unique within an AWS account.</p>

        Raises:
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_application_component_details_request.GetApplicationComponentDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_application_component_details_response.GetApplicationComponentDetailsResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_application_component_details

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_application_component_details.async_get_application_component_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_application_component_details_request.GetApplicationComponentDetailsRequest = {
            "application_component_id": application_component_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_application_component_strategies(
        self,
        application_component_id: "capo_migrationhubstrategy.types.application_component_id.ApplicationComponentId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.get_application_component_strategies_response.GetApplicationComponentStrategiesResponse":
        """<p> Retrieves a list of all the recommended strategies and tools for an application component running on a server. </p>

        Args:
            application_component_id: <p> The ID of the application component. The ID is unique within an AWS account.</p>

        Raises:
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_application_component_strategies_request.GetApplicationComponentStrategiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_application_component_strategies_response.GetApplicationComponentStrategiesResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_application_component_strategies

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_application_component_strategies.async_get_application_component_strategies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_application_component_strategies_request.GetApplicationComponentStrategiesRequest = {
            "application_component_id": application_component_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_assessment(
        self,
        id: "capo_migrationhubstrategy.types.async_task_id.AsyncTaskId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> (
        "capo_migrationhubstrategy.types.get_assessment_response.GetAssessmentResponse"
    ):
        """<p> Retrieves the status of an on-going assessment. </p>

        Args:
            id: <p> The <code>assessmentid</code> returned by <a>StartAssessment</a>.</p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_assessment_request.GetAssessmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_assessment_response.GetAssessmentResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_assessment

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_assessment.async_get_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_assessment_request.GetAssessmentRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_import_file_task(
        self,
        id: "capo_migrationhubstrategy.types.string.String",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.get_import_file_task_response.GetImportFileTaskResponse":
        """<p> Retrieves the details about a specific import task. </p>

        Args:
            id: <p> The ID of the import file task. This ID is returned in the response of <a>StartImportFileTask</a>. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_import_file_task_request.GetImportFileTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_import_file_task_response.GetImportFileTaskResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_import_file_task

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_import_file_task.async_get_import_file_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_import_file_task_request.GetImportFileTaskRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_latest_assessment_id(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.get_latest_assessment_id_response.GetLatestAssessmentIdResponse":
        """<p>Retrieve the latest ID of a specific assessment task.</p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_latest_assessment_id_request.GetLatestAssessmentIdRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_latest_assessment_id_response.GetLatestAssessmentIdResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_latest_assessment_id

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_latest_assessment_id.async_get_latest_assessment_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_latest_assessment_id_request.GetLatestAssessmentIdRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_portfolio_preferences(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.get_portfolio_preferences_response.GetPortfolioPreferencesResponse":
        """<p> Retrieves your migration and modernization preferences. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_portfolio_preferences_request.GetPortfolioPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_portfolio_preferences_response.GetPortfolioPreferencesResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_portfolio_preferences

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_portfolio_preferences.async_get_portfolio_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_portfolio_preferences_request.GetPortfolioPreferencesRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_portfolio_summary(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.get_portfolio_summary_response.GetPortfolioSummaryResponse":
        """<p> Retrieves overall summary including the number of servers to rehost and the overall number of anti-patterns. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_portfolio_summary_request.GetPortfolioSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_portfolio_summary_response.GetPortfolioSummaryResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_portfolio_summary

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_portfolio_summary.async_get_portfolio_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_portfolio_summary_request.GetPortfolioSummaryRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_recommendation_report_details(
        self,
        id: "capo_migrationhubstrategy.types.recommendation_task_id.RecommendationTaskId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.get_recommendation_report_details_response.GetRecommendationReportDetailsResponse":
        """<p> Retrieves detailed information about the specified recommendation report. </p>

        Args:
            id: <p> The recommendation report generation task <code>id</code> returned by <a>StartRecommendationReportGeneration</a>. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_recommendation_report_details_request.GetRecommendationReportDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_recommendation_report_details_response.GetRecommendationReportDetailsResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_recommendation_report_details

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_recommendation_report_details.async_get_recommendation_report_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_recommendation_report_details_request.GetRecommendationReportDetailsRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_server_details(
        self,
        server_id: "capo_migrationhubstrategy.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.get_server_details_response.GetServerDetailsResponse":
        """<p> Retrieves detailed information about a specified server. </p>

        Args:
            server_id: <p> The ID of the server. </p>
            next_token: <p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>
            max_results: <p> The maximum number of items to include in the response. The maximum value is 100. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_server_details_request.GetServerDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_server_details_response.GetServerDetailsResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_server_details

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_server_details.async_get_server_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_server_details_request.GetServerDetailsRequest = {
            "server_id": server_id
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

    async def iter_get_server_details(
        self,
        server_id: "capo_migrationhubstrategy.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhubstrategy.types.associated_application.AssociatedApplication]":
        _token = next_token
        while True:
            _response = await self.get_server_details(
                server_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("associated_applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_server_strategies(
        self,
        server_id: "capo_migrationhubstrategy.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.get_server_strategies_response.GetServerStrategiesResponse":
        """<p> Retrieves recommended strategies and tools for the specified server. </p>

        Args:
            server_id: <p> The ID of the server. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.get_server_strategies_request.GetServerStrategiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.get_server_strategies_response.GetServerStrategiesResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_server_strategies

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.get_server_strategies.async_get_server_strategies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.get_server_strategies_request.GetServerStrategiesRequest = {
            "server_id": server_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_analyzable_servers(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        sort: Optional["capo_migrationhubstrategy.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.list_analyzable_servers_response.ListAnalyzableServersResponse":
        """Retrieves a list of all the servers fetched from customer vCenter using Strategy Recommendation Collector.

        Args:
            sort: Specifies whether to sort by ascending (ASC) or descending (DESC) order.
            next_token: The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set maxResults to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.
            max_results: The maximum number of items to include in the response. The maximum value is 100.

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListAnalyzableServers

            >>> await client.list_analyzable_servers(max_results=100, sort='ASC')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.list_analyzable_servers_request.ListAnalyzableServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.list_analyzable_servers_response.ListAnalyzableServersResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_analyzable_servers

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_analyzable_servers.async_list_analyzable_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.list_analyzable_servers_request.ListAnalyzableServersRequest = {}
        if sort is not None:
            input_["sort"] = sort
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

    async def iter_list_analyzable_servers(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        sort: Optional["capo_migrationhubstrategy.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhubstrategy.types.analyzable_server_summary.AnalyzableServerSummary]":
        _token = next_token
        while True:
            _response = await self.list_analyzable_servers(
                config_overrides=config_overrides,
                sort=sort,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("analyzable_servers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_application_components(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        application_component_criteria: Optional[
            "capo_migrationhubstrategy.types.application_component_criteria.ApplicationComponentCriteria"
        ] = None,
        filter_value: Optional["capo_migrationhubstrategy.types.string.String"] = None,
        sort: Optional["capo_migrationhubstrategy.types.sort_order.SortOrder"] = None,
        group_id_filter: Optional[
            "capo_migrationhubstrategy.types.group_ids.GroupIds"
        ] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.list_application_components_response.ListApplicationComponentsResponse":
        """<p> Retrieves a list of all the application components (processes). </p>

        Args:
            application_component_criteria: <p> Criteria for filtering the list of application components. </p>
            filter_value: <p> Specify the value based on the application component criteria type. For example, if <code>applicationComponentCriteria</code> is set to <code>SERVER_ID</code> and <code>filterValue</code> is set to <code>server1</code>, then <a>ListApplicationComponents</a> returns all the application components running on server1. </p>
            sort: <p> Specifies whether to sort by ascending (<code>ASC</code>) or descending (<code>DESC</code>) order. </p>
            group_id_filter: <p> The group ID specified in to filter on. </p>
            next_token: <p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>
            max_results: <p> The maximum number of items to include in the response. The maximum value is 100. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.service_linked_role_lock_client_exception.ServiceLinkedRoleLockClientException: <p> Exception to indicate that the service-linked role (SLR) is locked. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.list_application_components_request.ListApplicationComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.list_application_components_response.ListApplicationComponentsResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_application_components

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_application_components.async_list_application_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.list_application_components_request.ListApplicationComponentsRequest = {}
        if application_component_criteria is not None:
            input_["application_component_criteria"] = application_component_criteria
        if filter_value is not None:
            input_["filter_value"] = filter_value
        if sort is not None:
            input_["sort"] = sort
        if group_id_filter is not None:
            input_["group_id_filter"] = group_id_filter
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

    async def iter_list_application_components(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        application_component_criteria: Optional[
            "capo_migrationhubstrategy.types.application_component_criteria.ApplicationComponentCriteria"
        ] = None,
        filter_value: Optional["capo_migrationhubstrategy.types.string.String"] = None,
        sort: Optional["capo_migrationhubstrategy.types.sort_order.SortOrder"] = None,
        group_id_filter: Optional[
            "capo_migrationhubstrategy.types.group_ids.GroupIds"
        ] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhubstrategy.types.application_component_detail.ApplicationComponentDetail]":
        _token = next_token
        while True:
            _response = await self.list_application_components(
                config_overrides=config_overrides,
                application_component_criteria=application_component_criteria,
                filter_value=filter_value,
                sort=sort,
                group_id_filter=group_id_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_component_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_collectors(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.list_collectors_response.ListCollectorsResponse":
        """<p> Retrieves a list of all the installed collectors. </p>

        Args:
            next_token: <p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>
            max_results: <p> The maximum number of items to include in the response. The maximum value is 100. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.list_collectors_request.ListCollectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.list_collectors_response.ListCollectorsResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_collectors

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_collectors.async_list_collectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.list_collectors_request.ListCollectorsRequest = {}
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

    async def iter_list_collectors(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhubstrategy.types.collector.Collector]":
        _token = next_token
        while True:
            _response = await self.list_collectors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("collectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_import_file_task(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        next_token: Optional["capo_migrationhubstrategy.types.string.String"] = None,
        max_results: Optional["capo_migrationhubstrategy.types.integer.Integer"] = None,
    ) -> "capo_migrationhubstrategy.types.list_import_file_task_response.ListImportFileTaskResponse":
        """<p> Retrieves a list of all the imports performed. </p>

        Args:
            next_token: <p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>
            max_results: <p> The total number of items to return. The maximum value is 100. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.list_import_file_task_request.ListImportFileTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.list_import_file_task_response.ListImportFileTaskResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_import_file_task

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_import_file_task.async_list_import_file_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.list_import_file_task_request.ListImportFileTaskRequest = {}
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

    async def iter_list_import_file_task(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        next_token: Optional["capo_migrationhubstrategy.types.string.String"] = None,
        max_results: Optional["capo_migrationhubstrategy.types.integer.Integer"] = None,
    ) -> "AsyncIterator[capo_migrationhubstrategy.types.import_file_task_information.ImportFileTaskInformation]":
        _token = next_token
        while True:
            _response = await self.list_import_file_task(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("task_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_servers(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        server_criteria: Optional[
            "capo_migrationhubstrategy.types.server_criteria.ServerCriteria"
        ] = None,
        filter_value: Optional["capo_migrationhubstrategy.types.string.String"] = None,
        sort: Optional["capo_migrationhubstrategy.types.sort_order.SortOrder"] = None,
        group_id_filter: Optional[
            "capo_migrationhubstrategy.types.group_ids.GroupIds"
        ] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.list_servers_response.ListServersResponse":
        """<p> Returns a list of all the servers. </p>

        Args:
            server_criteria: <p> Criteria for filtering servers. </p>
            filter_value: <p> Specifies the filter value, which is based on the type of server criteria. For example, if <code>serverCriteria</code> is <code>OS_NAME</code>, and the <code>filterValue</code> is equal to <code>WindowsServer</code>, then <code>ListServers</code> returns all of the servers matching the OS name <code>WindowsServer</code>. </p>
            sort: <p> Specifies whether to sort by ascending (<code>ASC</code>) or descending (<code>DESC</code>) order. </p>
            group_id_filter: <p> Specifies the group ID to filter on. </p>
            next_token: <p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>
            max_results: <p> The maximum number of items to include in the response. The maximum value is 100. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.list_servers_request.ListServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.list_servers_response.ListServersResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_servers

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.list_servers.async_list_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.list_servers_request.ListServersRequest = {}
        if server_criteria is not None:
            input_["server_criteria"] = server_criteria
        if filter_value is not None:
            input_["filter_value"] = filter_value
        if sort is not None:
            input_["sort"] = sort
        if group_id_filter is not None:
            input_["group_id_filter"] = group_id_filter
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

    async def iter_list_servers(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        server_criteria: Optional[
            "capo_migrationhubstrategy.types.server_criteria.ServerCriteria"
        ] = None,
        filter_value: Optional["capo_migrationhubstrategy.types.string.String"] = None,
        sort: Optional["capo_migrationhubstrategy.types.sort_order.SortOrder"] = None,
        group_id_filter: Optional[
            "capo_migrationhubstrategy.types.group_ids.GroupIds"
        ] = None,
        next_token: Optional[
            "capo_migrationhubstrategy.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migrationhubstrategy.types.max_result.MaxResult"
        ] = None,
    ) -> "AsyncIterator[capo_migrationhubstrategy.types.server_detail.ServerDetail]":
        _token = next_token
        while True:
            _response = await self.list_servers(
                config_overrides=config_overrides,
                server_criteria=server_criteria,
                filter_value=filter_value,
                sort=sort,
                group_id_filter=group_id_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("server_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_portfolio_preferences(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        prioritize_business_goals: Optional[
            "capo_migrationhubstrategy.types.prioritize_business_goals.PrioritizeBusinessGoals"
        ] = None,
        application_preferences: Optional[
            "capo_migrationhubstrategy.types.application_preferences.ApplicationPreferences"
        ] = None,
        database_preferences: Optional[
            "capo_migrationhubstrategy.types.database_preferences.DatabasePreferences"
        ] = None,
        application_mode: Optional[
            "capo_migrationhubstrategy.types.application_mode.ApplicationMode"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.put_portfolio_preferences_response.PutPortfolioPreferencesResponse":
        """<p> Saves the specified migration and modernization preferences. </p>

        Args:
            prioritize_business_goals: <p> The rank of the business goals based on priority. </p>
            application_preferences: <p> The transformation preferences for non-database applications. </p>
            database_preferences: <p> The transformation preferences for database applications. </p>
            application_mode: <p>The classification for application component types.</p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.conflict_exception.ConflictException: <p> Exception to indicate that there is an ongoing task when a new task is created. Return when once the existing tasks are complete. </p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.put_portfolio_preferences_request.PutPortfolioPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.put_portfolio_preferences_response.PutPortfolioPreferencesResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.put_portfolio_preferences

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.put_portfolio_preferences.async_put_portfolio_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.put_portfolio_preferences_request.PutPortfolioPreferencesRequest = {}
        if prioritize_business_goals is not None:
            input_["prioritize_business_goals"] = prioritize_business_goals
        if application_preferences is not None:
            input_["application_preferences"] = application_preferences
        if database_preferences is not None:
            input_["database_preferences"] = database_preferences
        if application_mode is not None:
            input_["application_mode"] = application_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_assessment(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        s3bucket_for_analysis_data: Optional[
            "capo_migrationhubstrategy.types.string.String"
        ] = None,
        s3bucket_for_report_data: Optional[
            "capo_migrationhubstrategy.types.string.String"
        ] = None,
        assessment_targets: Optional[
            "capo_migrationhubstrategy.types.assessment_targets.AssessmentTargets"
        ] = None,
        assessment_data_source_type: Optional[
            "capo_migrationhubstrategy.types.assessment_data_source_type.AssessmentDataSourceType"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.start_assessment_response.StartAssessmentResponse":
        """<p> Starts the assessment of an on-premises environment. </p>

        Args:
            s3bucket_for_analysis_data: <p> The S3 bucket used by the collectors to send analysis data to the service. The bucket name must begin with <code>migrationhub-strategy-</code>. </p>
            s3bucket_for_report_data: <p> The S3 bucket where all the reports generated by the service are stored. The bucket name must begin with <code>migrationhub-strategy-</code>. </p>
            assessment_targets: <p>List of criteria for assessment.</p>
            assessment_data_source_type: The data source type of an assessment to be started.

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The AWS account has reached its quota of imports. Contact AWS Support to increase the quota for this account. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.start_assessment_request.StartAssessmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.start_assessment_response.StartAssessmentResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.start_assessment

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.start_assessment.async_start_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.start_assessment_request.StartAssessmentRequest = {}
        if s3bucket_for_analysis_data is not None:
            input_["s3bucket_for_analysis_data"] = s3bucket_for_analysis_data
        if s3bucket_for_report_data is not None:
            input_["s3bucket_for_report_data"] = s3bucket_for_report_data
        if assessment_targets is not None:
            input_["assessment_targets"] = assessment_targets
        if assessment_data_source_type is not None:
            input_["assessment_data_source_type"] = assessment_data_source_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import_file_task(
        self,
        name: "capo_migrationhubstrategy.types.string.String",
        s3_bucket: "capo_migrationhubstrategy.types.import_s3_bucket.importS3Bucket",
        s3key: "capo_migrationhubstrategy.types.string.String",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        data_source_type: Optional[
            "capo_migrationhubstrategy.types.data_source_type.DataSourceType"
        ] = None,
        group_id: Optional["capo_migrationhubstrategy.types.group_ids.GroupIds"] = None,
        s3bucket_for_report_data: Optional[
            "capo_migrationhubstrategy.types.string.String"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.start_import_file_task_response.StartImportFileTaskResponse":
        """<p> Starts a file import. </p>

        Args:
            name: <p> A descriptive name for the request. </p>
            s3_bucket: <p> The S3 bucket where the import file is located. The bucket name is required to begin with <code>migrationhub-strategy-</code>.</p>
            s3key: <p> The Amazon S3 key name of the import file. </p>
            data_source_type: <p>Specifies the source that the servers are coming from. By default, Strategy Recommendations assumes that the servers specified in the import file are available in AWS Application Discovery Service. </p>
            group_id: <p>Groups the resources in the import file together with a unique name. This ID can be as filter in <code>ListApplicationComponents</code> and <code>ListServers</code>. </p>
            s3bucket_for_report_data: <p> The S3 bucket where Strategy Recommendations uploads import results. The bucket name is required to begin with migrationhub-strategy-. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The AWS account has reached its quota of imports. Contact AWS Support to increase the quota for this account. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.start_import_file_task_request.StartImportFileTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.start_import_file_task_response.StartImportFileTaskResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.start_import_file_task

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.start_import_file_task.async_start_import_file_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.start_import_file_task_request.StartImportFileTaskRequest = {
            "name": name,
            "s3_bucket": s3_bucket,
            "s3key": s3key,
        }
        if data_source_type is not None:
            input_["data_source_type"] = data_source_type
        if group_id is not None:
            input_["group_id"] = group_id
        if s3bucket_for_report_data is not None:
            input_["s3bucket_for_report_data"] = s3bucket_for_report_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_recommendation_report_generation(
        self,
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        output_format: Optional[
            "capo_migrationhubstrategy.types.output_format.OutputFormat"
        ] = None,
        group_id_filter: Optional[
            "capo_migrationhubstrategy.types.group_ids.GroupIds"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.start_recommendation_report_generation_response.StartRecommendationReportGenerationResponse":
        """<p> Starts generating a recommendation report. </p>

        Args:
            output_format: <p> The output format for the recommendation report file. The default format is Microsoft Excel. </p>
            group_id_filter: <p> Groups the resources in the recommendation report with a unique name. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.conflict_exception.ConflictException: <p> Exception to indicate that there is an ongoing task when a new task is created. Return when once the existing tasks are complete. </p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.start_recommendation_report_generation_request.StartRecommendationReportGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.start_recommendation_report_generation_response.StartRecommendationReportGenerationResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.start_recommendation_report_generation

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.start_recommendation_report_generation.async_start_recommendation_report_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.start_recommendation_report_generation_request.StartRecommendationReportGenerationRequest = {}
        if output_format is not None:
            input_["output_format"] = output_format
        if group_id_filter is not None:
            input_["group_id_filter"] = group_id_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_assessment(
        self,
        assessment_id: "capo_migrationhubstrategy.types.async_task_id.AsyncTaskId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
    ) -> "capo_migrationhubstrategy.types.stop_assessment_response.StopAssessmentResponse":
        """<p> Stops the assessment of an on-premises environment. </p>

        Args:
            assessment_id: <p> The <code>assessmentId</code> returned by <a>StartAssessment</a>. </p>

        Raises:
            capo_migrationhubstrategy.errors.access_denied_exception.AccessDeniedException: <p> The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.</p>
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.stop_assessment_request.StopAssessmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.stop_assessment_response.StopAssessmentResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.stop_assessment

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.stop_assessment.async_stop_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.stop_assessment_request.StopAssessmentRequest = {
            "assessment_id": assessment_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application_component_config(
        self,
        application_component_id: "capo_migrationhubstrategy.types.application_component_id.ApplicationComponentId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        inclusion_status: Optional[
            "capo_migrationhubstrategy.types.inclusion_status.InclusionStatus"
        ] = None,
        strategy_option: Optional[
            "capo_migrationhubstrategy.types.strategy_option.StrategyOption"
        ] = None,
        source_code_list: Optional[
            "capo_migrationhubstrategy.types.source_code_list.SourceCodeList"
        ] = None,
        secrets_manager_key: Optional[
            "capo_migrationhubstrategy.types.secrets_manager_key.SecretsManagerKey"
        ] = None,
        configure_only: Optional[
            "capo_migrationhubstrategy.types.boolean.Boolean"
        ] = None,
        app_type: Optional["capo_migrationhubstrategy.types.app_type.AppType"] = None,
    ) -> "capo_migrationhubstrategy.types.update_application_component_config_response.UpdateApplicationComponentConfigResponse":
        """<p> Updates the configuration of an application component. </p>

        Args:
            application_component_id: <p> The ID of the application component. The ID is unique within an AWS account. </p>
            inclusion_status: <p> Indicates whether the application component has been included for server recommendation or not. </p>
            strategy_option: <p> The preferred strategy options for the application component. Use values from the <a>GetApplicationComponentStrategies</a> response. </p>
            source_code_list: <p> The list of source code configurations to update for the application component. </p>
            secrets_manager_key: <p> Database credentials. </p>
            configure_only: <p>Update the configuration request of an application component. If it is set to true, the source code and/or database credentials are updated. If it is set to false, the source code and/or database credentials are updated and an analysis is initiated.</p>
            app_type: <p>The type of known component.</p>

        Raises:
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.update_application_component_config_request.UpdateApplicationComponentConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.update_application_component_config_response.UpdateApplicationComponentConfigResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.update_application_component_config

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.update_application_component_config.async_update_application_component_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.update_application_component_config_request.UpdateApplicationComponentConfigRequest = {
            "application_component_id": application_component_id
        }
        if inclusion_status is not None:
            input_["inclusion_status"] = inclusion_status
        if strategy_option is not None:
            input_["strategy_option"] = strategy_option
        if source_code_list is not None:
            input_["source_code_list"] = source_code_list
        if secrets_manager_key is not None:
            input_["secrets_manager_key"] = secrets_manager_key
        if configure_only is not None:
            input_["configure_only"] = configure_only
        if app_type is not None:
            input_["app_type"] = app_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_server_config(
        self,
        server_id: "capo_migrationhubstrategy.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncMigrationHubStrategyClientConfig] = None,
        strategy_option: Optional[
            "capo_migrationhubstrategy.types.strategy_option.StrategyOption"
        ] = None,
    ) -> "capo_migrationhubstrategy.types.update_server_config_response.UpdateServerConfigResponse":
        """<p> Updates the configuration of the specified server. </p>

        Args:
            server_id: <p> The ID of the server. </p>
            strategy_option: <p> The preferred strategy options for the application component. See the response from <a>GetServerStrategies</a>.</p>

        Raises:
            capo_migrationhubstrategy.errors.internal_server_exception.InternalServerException: <p> The server experienced an internal error. Try again. </p>
            capo_migrationhubstrategy.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ID in the request is not found. </p>
            capo_migrationhubstrategy.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_migrationhubstrategy.errors.validation_exception.ValidationException: <p> The request body isn't valid. </p>
            capo_migrationhubstrategy.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_migrationhubstrategy.types.update_server_config_request.UpdateServerConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_migrationhubstrategy.types.update_server_config_response.UpdateServerConfigResponse"
        ]:
            import capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.update_server_config

            (
                output,
                http_response,
            ) = await capo_migrationhubstrategy._operations.aws_migration_hub_strategy_recommendation.update_server_config.async_update_server_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migrationhubstrategy.types.update_server_config_request.UpdateServerConfigRequest = {
            "server_id": server_id
        }
        if strategy_option is not None:
            input_["strategy_option"] = strategy_option

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
