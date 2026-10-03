"""Generated from Smithy shape ``com.amazonaws.applicationinsights#EC2WindowsBarleyService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_application_insights._auth._signers
import capo_application_insights._auth._sigv4
from capo_application_insights._auth._identity import Credentials
from capo_application_insights._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_application_insights._auth._zapros_handler import AuthMiddleware
from capo_application_insights._pagination import resolve_path as _resolve_path
from capo_application_insights._services._aws_config import aaws_config
from capo_application_insights._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.add_workload_request
    import capo_application_insights.types.add_workload_response
    import capo_application_insights.types.amazon_resource_name
    import capo_application_insights.types.attach_missing_permission
    import capo_application_insights.types.auto_config_enabled
    import capo_application_insights.types.auto_create
    import capo_application_insights.types.component_configuration
    import capo_application_insights.types.component_name
    import capo_application_insights.types.configuration_event_status
    import capo_application_insights.types.create_application_request
    import capo_application_insights.types.create_application_response
    import capo_application_insights.types.create_component_request
    import capo_application_insights.types.create_component_response
    import capo_application_insights.types.create_log_pattern_request
    import capo_application_insights.types.create_log_pattern_response
    import capo_application_insights.types.custom_component_name
    import capo_application_insights.types.cwe_monitor_enabled
    import capo_application_insights.types.delete_application_request
    import capo_application_insights.types.delete_application_response
    import capo_application_insights.types.delete_component_request
    import capo_application_insights.types.delete_component_response
    import capo_application_insights.types.delete_log_pattern_request
    import capo_application_insights.types.delete_log_pattern_response
    import capo_application_insights.types.describe_application_request
    import capo_application_insights.types.describe_application_response
    import capo_application_insights.types.describe_component_configuration_recommendation_request
    import capo_application_insights.types.describe_component_configuration_recommendation_response
    import capo_application_insights.types.describe_component_configuration_request
    import capo_application_insights.types.describe_component_configuration_response
    import capo_application_insights.types.describe_component_request
    import capo_application_insights.types.describe_component_response
    import capo_application_insights.types.describe_log_pattern_request
    import capo_application_insights.types.describe_log_pattern_response
    import capo_application_insights.types.describe_observation_request
    import capo_application_insights.types.describe_observation_response
    import capo_application_insights.types.describe_problem_observations_request
    import capo_application_insights.types.describe_problem_observations_response
    import capo_application_insights.types.describe_problem_request
    import capo_application_insights.types.describe_problem_response
    import capo_application_insights.types.describe_workload_request
    import capo_application_insights.types.describe_workload_response
    import capo_application_insights.types.end_time
    import capo_application_insights.types.grouping_type
    import capo_application_insights.types.list_applications_request
    import capo_application_insights.types.list_applications_response
    import capo_application_insights.types.list_components_request
    import capo_application_insights.types.list_components_response
    import capo_application_insights.types.list_configuration_history_request
    import capo_application_insights.types.list_configuration_history_response
    import capo_application_insights.types.list_log_pattern_sets_request
    import capo_application_insights.types.list_log_pattern_sets_response
    import capo_application_insights.types.list_log_patterns_request
    import capo_application_insights.types.list_log_patterns_response
    import capo_application_insights.types.list_problems_request
    import capo_application_insights.types.list_problems_response
    import capo_application_insights.types.list_tags_for_resource_request
    import capo_application_insights.types.list_tags_for_resource_response
    import capo_application_insights.types.list_workloads_request
    import capo_application_insights.types.list_workloads_response
    import capo_application_insights.types.log_pattern_name
    import capo_application_insights.types.log_pattern_rank
    import capo_application_insights.types.log_pattern_regex
    import capo_application_insights.types.log_pattern_set_name
    import capo_application_insights.types.max_entities
    import capo_application_insights.types.monitor
    import capo_application_insights.types.observation_id
    import capo_application_insights.types.ops_center_enabled
    import capo_application_insights.types.ops_item_sns_topic_arn
    import capo_application_insights.types.pagination_token
    import capo_application_insights.types.problem_id
    import capo_application_insights.types.recommendation_type
    import capo_application_insights.types.remove_sns_topic
    import capo_application_insights.types.remove_workload_request
    import capo_application_insights.types.remove_workload_response
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.resource_list
    import capo_application_insights.types.sns_notification_arn
    import capo_application_insights.types.start_time
    import capo_application_insights.types.tag_key_list
    import capo_application_insights.types.tag_list
    import capo_application_insights.types.tag_resource_request
    import capo_application_insights.types.tag_resource_response
    import capo_application_insights.types.tier
    import capo_application_insights.types.untag_resource_request
    import capo_application_insights.types.untag_resource_response
    import capo_application_insights.types.update_application_request
    import capo_application_insights.types.update_application_response
    import capo_application_insights.types.update_component_configuration_request
    import capo_application_insights.types.update_component_configuration_response
    import capo_application_insights.types.update_component_request
    import capo_application_insights.types.update_component_response
    import capo_application_insights.types.update_log_pattern_request
    import capo_application_insights.types.update_log_pattern_response
    import capo_application_insights.types.update_problem_request
    import capo_application_insights.types.update_problem_response
    import capo_application_insights.types.update_status
    import capo_application_insights.types.update_workload_request
    import capo_application_insights.types.update_workload_response
    import capo_application_insights.types.visibility
    import capo_application_insights.types.workload_configuration
    import capo_application_insights.types.workload_id
    import capo_application_insights.types.workload_name


class AsyncApplicationInsightsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncApplicationInsightsClient:
    """A client for the ``ApplicationInsights`` service.

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
        self._config = AsyncApplicationInsightsClientConfig(
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
        self, config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncApplicationInsightsClientConfig = config_overrides or {}
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

    async def add_workload(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        workload_configuration: "capo_application_insights.types.workload_configuration.WorkloadConfiguration",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.add_workload_response.AddWorkloadResponse":
        """<p>Adds a workload to a component. Each component can have at most five workloads.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            workload_configuration: <p>The configuration settings of the workload. The value is the escaped JSON of the configuration.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already created or in use.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.add_workload_request.AddWorkloadRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.add_workload_response.AddWorkloadResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.add_workload

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.add_workload.async_add_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.add_workload_request.AddWorkloadRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
            "workload_configuration": workload_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_application(
        self,
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        resource_group_name: Optional[
            "capo_application_insights.types.resource_group_name.ResourceGroupName"
        ] = None,
        ops_center_enabled: Optional[
            "capo_application_insights.types.ops_center_enabled.OpsCenterEnabled"
        ] = None,
        cwe_monitor_enabled: Optional[
            "capo_application_insights.types.cwe_monitor_enabled.CWEMonitorEnabled"
        ] = None,
        ops_item_sns_topic_arn: Optional[
            "capo_application_insights.types.ops_item_sns_topic_arn.OpsItemSNSTopicArn"
        ] = None,
        sns_notification_arn: Optional[
            "capo_application_insights.types.sns_notification_arn.SNSNotificationArn"
        ] = None,
        tags: Optional["capo_application_insights.types.tag_list.TagList"] = None,
        auto_config_enabled: Optional[
            "capo_application_insights.types.auto_config_enabled.AutoConfigEnabled"
        ] = None,
        auto_create: Optional[
            "capo_application_insights.types.auto_create.AutoCreate"
        ] = None,
        grouping_type: Optional[
            "capo_application_insights.types.grouping_type.GroupingType"
        ] = None,
        attach_missing_permission: Optional[
            "capo_application_insights.types.attach_missing_permission.AttachMissingPermission"
        ] = None,
    ) -> "capo_application_insights.types.create_application_response.CreateApplicationResponse":
        """<p>Adds an application that is created from a resource group.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            ops_center_enabled: <p> When set to <code>true</code>, creates opsItems for any problems detected on an application. </p>
            cwe_monitor_enabled: <p> Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as <code>instance terminated</code>, <code>failed deployment</code>, and others. </p>
            ops_item_sns_topic_arn: <p> The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem. </p>
            sns_notification_arn: <p> The SNS notification topic ARN. </p>
            tags: <p>List of tags to add to the application. tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>
            auto_config_enabled: <p> Indicates whether Application Insights automatically configures unmonitored resources in the resource group. </p>
            auto_create: <p> Configures all of the resources in the resource group by applying the recommended configurations. </p>
            grouping_type: <p>Application Insights can create applications based on a resource group or on an account. To create an account-based application using all of the resources in the account, set this parameter to <code>ACCOUNT_BASED</code>. </p>
            attach_missing_permission: <p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>

        Raises:
            capo_application_insights.errors.access_denied_exception.AccessDeniedException: <p> User does not have permissions to perform this action. </p>
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already created or in use.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.tags_already_exist_exception.TagsAlreadyExistException: <p>Tags are already registered for the specified application ARN.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.create_application

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.create_application_request.CreateApplicationRequest = {}
        if resource_group_name is not None:
            input_["resource_group_name"] = resource_group_name
        if ops_center_enabled is not None:
            input_["ops_center_enabled"] = ops_center_enabled
        if cwe_monitor_enabled is not None:
            input_["cwe_monitor_enabled"] = cwe_monitor_enabled
        if ops_item_sns_topic_arn is not None:
            input_["ops_item_sns_topic_arn"] = ops_item_sns_topic_arn
        if sns_notification_arn is not None:
            input_["sns_notification_arn"] = sns_notification_arn
        if tags is not None:
            input_["tags"] = tags
        if auto_config_enabled is not None:
            input_["auto_config_enabled"] = auto_config_enabled
        if auto_create is not None:
            input_["auto_create"] = auto_create
        if grouping_type is not None:
            input_["grouping_type"] = grouping_type
        if attach_missing_permission is not None:
            input_["attach_missing_permission"] = attach_missing_permission

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_component(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.custom_component_name.CustomComponentName",
        resource_list: "capo_application_insights.types.resource_list.ResourceList",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.create_component_response.CreateComponentResponse":
        """<p>Creates a custom component by grouping similar standalone instances to monitor.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            resource_list: <p>The list of resource ARNs that belong to the component.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already created or in use.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.create_component_request.CreateComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.create_component_response.CreateComponentResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.create_component

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.create_component.async_create_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.create_component_request.CreateComponentRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
            "resource_list": resource_list,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_log_pattern(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        pattern_set_name: "capo_application_insights.types.log_pattern_set_name.LogPatternSetName",
        pattern_name: "capo_application_insights.types.log_pattern_name.LogPatternName",
        pattern: "capo_application_insights.types.log_pattern_regex.LogPatternRegex",
        rank: "capo_application_insights.types.log_pattern_rank.LogPatternRank",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.create_log_pattern_response.CreateLogPatternResponse":
        """<p>Adds an log pattern to a <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            pattern_name: <p>The name of the log pattern.</p>
            pattern: <p>The log pattern. The pattern must be DFA compatible. Patterns that utilize forward lookahead or backreference constructions are not supported.</p>
            rank: <p>Rank of the log pattern. Must be a value between <code>1</code> and <code>1,000,000</code>. The patterns are sorted by rank, so we recommend that you set your highest priority patterns with the lowest rank. A pattern of rank <code>1</code> will be the first to get matched to a log line. A pattern of rank <code>1,000,000</code> will be last to get matched. When you configure custom log patterns from the console, a <code>Low</code> severity pattern translates to a <code>750,000</code> rank. A <code>Medium</code> severity pattern translates to a <code>500,000</code> rank. And a <code>High</code> severity pattern translates to a <code>250,000</code> rank. Rank values less than <code>1</code> or greater than <code>1,000,000</code> are reserved for Amazon Web Services provided patterns. </p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already created or in use.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.create_log_pattern_request.CreateLogPatternRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.create_log_pattern_response.CreateLogPatternResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.create_log_pattern

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.create_log_pattern.async_create_log_pattern(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.create_log_pattern_request.CreateLogPatternRequest = {
            "resource_group_name": resource_group_name,
            "pattern_set_name": pattern_set_name,
            "pattern_name": pattern_name,
            "pattern": pattern,
            "rank": rank,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_application(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.delete_application_response.DeleteApplicationResponse":
        """<p>Removes the specified application from monitoring. Does not delete the application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>

        Raises:
            capo_application_insights.errors.bad_request_exception.BadRequestException: <p>The request is not understood by the server.</p>
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.delete_application

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.delete_application_request.DeleteApplicationRequest = {
            "resource_group_name": resource_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_component(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.custom_component_name.CustomComponentName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.delete_component_response.DeleteComponentResponse":
        """<p>Ungroups a custom component. When you ungroup custom components, all applicable monitors that are set up for the component are removed and the instances revert to their standalone status.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.delete_component_request.DeleteComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.delete_component_response.DeleteComponentResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.delete_component

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.delete_component.async_delete_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.delete_component_request.DeleteComponentRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_log_pattern(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        pattern_set_name: "capo_application_insights.types.log_pattern_set_name.LogPatternSetName",
        pattern_name: "capo_application_insights.types.log_pattern_name.LogPatternName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.delete_log_pattern_response.DeleteLogPatternResponse":
        """<p>Removes the specified log pattern from a <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            pattern_name: <p>The name of the log pattern.</p>

        Raises:
            capo_application_insights.errors.bad_request_exception.BadRequestException: <p>The request is not understood by the server.</p>
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.delete_log_pattern_request.DeleteLogPatternRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.delete_log_pattern_response.DeleteLogPatternResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.delete_log_pattern

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.delete_log_pattern.async_delete_log_pattern(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.delete_log_pattern_request.DeleteLogPatternRequest = {
            "resource_group_name": resource_group_name,
            "pattern_set_name": pattern_set_name,
            "pattern_name": pattern_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_application(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.describe_application_response.DescribeApplicationResponse":
        """<p>Describes the application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_application_request.DescribeApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_application_response.DescribeApplicationResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_application

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_application.async_describe_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_application_request.DescribeApplicationRequest = {
            "resource_group_name": resource_group_name
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_component(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.describe_component_response.DescribeComponentResponse":
        """<p>Describes a component and lists the resources that are grouped together in a component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_component_request.DescribeComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_component_response.DescribeComponentResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_component

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_component.async_describe_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_component_request.DescribeComponentRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_component_configuration(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.describe_component_configuration_response.DescribeComponentConfigurationResponse":
        """<p>Describes the monitoring configuration of the component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_component_configuration_request.DescribeComponentConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_component_configuration_response.DescribeComponentConfigurationResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_component_configuration

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_component_configuration.async_describe_component_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_component_configuration_request.DescribeComponentConfigurationRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_component_configuration_recommendation(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        tier: "capo_application_insights.types.tier.Tier",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        workload_name: Optional[
            "capo_application_insights.types.workload_name.WorkloadName"
        ] = None,
        recommendation_type: Optional[
            "capo_application_insights.types.recommendation_type.RecommendationType"
        ] = None,
    ) -> "capo_application_insights.types.describe_component_configuration_recommendation_response.DescribeComponentConfigurationRecommendationResponse":
        """<p>Describes the recommended monitoring configuration of the component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            tier: <p>The tier of the application component.</p>
            workload_name: <p>The name of the workload. The name of the workload is required when the tier of the application component is <code>SAP_ASE_SINGLE_NODE</code> or <code>SAP_ASE_HIGH_AVAILABILITY</code>.</p>
            recommendation_type: <p>The recommended configuration type.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_component_configuration_recommendation_request.DescribeComponentConfigurationRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_component_configuration_recommendation_response.DescribeComponentConfigurationRecommendationResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_component_configuration_recommendation

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_component_configuration_recommendation.async_describe_component_configuration_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_component_configuration_recommendation_request.DescribeComponentConfigurationRecommendationRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
            "tier": tier,
        }
        if workload_name is not None:
            input_["workload_name"] = workload_name
        if recommendation_type is not None:
            input_["recommendation_type"] = recommendation_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_log_pattern(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        pattern_set_name: "capo_application_insights.types.log_pattern_set_name.LogPatternSetName",
        pattern_name: "capo_application_insights.types.log_pattern_name.LogPatternName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.describe_log_pattern_response.DescribeLogPatternResponse":
        """<p>Describe a specific log pattern from a <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            pattern_name: <p>The name of the log pattern.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_log_pattern_request.DescribeLogPatternRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_log_pattern_response.DescribeLogPatternResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_log_pattern

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_log_pattern.async_describe_log_pattern(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_log_pattern_request.DescribeLogPatternRequest = {
            "resource_group_name": resource_group_name,
            "pattern_set_name": pattern_set_name,
            "pattern_name": pattern_name,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_observation(
        self,
        observation_id: "capo_application_insights.types.observation_id.ObservationId",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.describe_observation_response.DescribeObservationResponse":
        """<p>Describes an anomaly or error with the application.</p>

        Args:
            observation_id: <p>The ID of the observation.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_observation_request.DescribeObservationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_observation_response.DescribeObservationResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_observation

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_observation.async_describe_observation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_observation_request.DescribeObservationRequest = {
            "observation_id": observation_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_problem(
        self,
        problem_id: "capo_application_insights.types.problem_id.ProblemId",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.describe_problem_response.DescribeProblemResponse":
        """<p>Describes an application problem.</p>

        Args:
            problem_id: <p>The ID of the problem.</p>
            account_id: <p>The Amazon Web Services account ID for the owner of the resource group affected by the problem.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_problem_request.DescribeProblemRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_problem_response.DescribeProblemResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_problem

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_problem.async_describe_problem(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_problem_request.DescribeProblemRequest = {
            "problem_id": problem_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_problem_observations(
        self,
        problem_id: "capo_application_insights.types.problem_id.ProblemId",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.describe_problem_observations_response.DescribeProblemObservationsResponse":
        """<p>Describes the anomalies or errors associated with the problem.</p>

        Args:
            problem_id: <p>The ID of the problem.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_problem_observations_request.DescribeProblemObservationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_problem_observations_response.DescribeProblemObservationsResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_problem_observations

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_problem_observations.async_describe_problem_observations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_problem_observations_request.DescribeProblemObservationsRequest = {
            "problem_id": problem_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_workload(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        workload_id: "capo_application_insights.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.describe_workload_response.DescribeWorkloadResponse":
        """<p>Describes a workload and its configuration.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            workload_id: <p>The ID of the workload.</p>
            account_id: <p>The Amazon Web Services account ID for the workload owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.describe_workload_request.DescribeWorkloadRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.describe_workload_response.DescribeWorkloadResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.describe_workload

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.describe_workload.async_describe_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.describe_workload_request.DescribeWorkloadRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
            "workload_id": workload_id,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists the IDs of the applications that you are monitoring. </p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.list_applications

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.list_applications_request.ListApplicationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "AsyncIterator[capo_application_insights.types.list_applications_response.ListApplicationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_components(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.list_components_response.ListComponentsResponse":
        """<p>Lists the auto-grouped, standalone, and custom components of the application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.list_components_request.ListComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.list_components_response.ListComponentsResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.list_components

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.list_components_request.ListComponentsRequest = {
            "resource_group_name": resource_group_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_components(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "AsyncIterator[capo_application_insights.types.list_components_response.ListComponentsResponse]":
        _token = next_token
        while True:
            _response = await self.list_components(
                resource_group_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_configuration_history(
        self,
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        resource_group_name: Optional[
            "capo_application_insights.types.resource_group_name.ResourceGroupName"
        ] = None,
        start_time: Optional[
            "capo_application_insights.types.start_time.StartTime"
        ] = None,
        end_time: Optional["capo_application_insights.types.end_time.EndTime"] = None,
        event_status: Optional[
            "capo_application_insights.types.configuration_event_status.ConfigurationEventStatus"
        ] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.list_configuration_history_response.ListConfigurationHistoryResponse":
        """<p> Lists the INFO, WARN, and ERROR events for periodic configuration updates performed by Application Insights. Examples of events represented are: </p> <ul> <li> <p>INFO: creating a new alarm or updating an alarm threshold.</p> </li> <li> <p>WARN: alarm not created due to insufficient data points used to predict thresholds.</p> </li> <li> <p>ERROR: alarm not created due to permission errors or exceeding quotas. </p> </li> </ul>

        Args:
            resource_group_name: <p>Resource group to which the application belongs. </p>
            start_time: <p>The start time of the event. </p>
            end_time: <p>The end time of the event.</p>
            event_status: <p>The status of the configuration update event. Possible values include INFO, WARN, and ERROR.</p>
            max_results: <p> The maximum number of results returned by <code>ListConfigurationHistory</code> in paginated output. When this parameter is used, <code>ListConfigurationHistory</code> returns only <code>MaxResults</code> in a single page along with a <code>NextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListConfigurationHistory</code> request with the returned <code>NextToken</code> value. If this parameter is not used, then <code>ListConfigurationHistory</code> returns all results. </p>
            next_token: <p>The <code>NextToken</code> value returned from a previous paginated <code>ListConfigurationHistory</code> request where <code>MaxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.list_configuration_history_request.ListConfigurationHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.list_configuration_history_response.ListConfigurationHistoryResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.list_configuration_history

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.list_configuration_history.async_list_configuration_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.list_configuration_history_request.ListConfigurationHistoryRequest = {}
        if resource_group_name is not None:
            input_["resource_group_name"] = resource_group_name
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if event_status is not None:
            input_["event_status"] = event_status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_configuration_history(
        self,
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        resource_group_name: Optional[
            "capo_application_insights.types.resource_group_name.ResourceGroupName"
        ] = None,
        start_time: Optional[
            "capo_application_insights.types.start_time.StartTime"
        ] = None,
        end_time: Optional["capo_application_insights.types.end_time.EndTime"] = None,
        event_status: Optional[
            "capo_application_insights.types.configuration_event_status.ConfigurationEventStatus"
        ] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "AsyncIterator[capo_application_insights.types.list_configuration_history_response.ListConfigurationHistoryResponse]":
        _token = next_token
        while True:
            _response = await self.list_configuration_history(
                config_overrides=config_overrides,
                resource_group_name=resource_group_name,
                start_time=start_time,
                end_time=end_time,
                event_status=event_status,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_log_patterns(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        pattern_set_name: Optional[
            "capo_application_insights.types.log_pattern_set_name.LogPatternSetName"
        ] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.list_log_patterns_response.ListLogPatternsResponse":
        """<p>Lists the log patterns in the specific log <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.list_log_patterns_request.ListLogPatternsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.list_log_patterns_response.ListLogPatternsResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.list_log_patterns

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.list_log_patterns.async_list_log_patterns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.list_log_patterns_request.ListLogPatternsRequest = {
            "resource_group_name": resource_group_name
        }
        if pattern_set_name is not None:
            input_["pattern_set_name"] = pattern_set_name
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_log_patterns(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        pattern_set_name: Optional[
            "capo_application_insights.types.log_pattern_set_name.LogPatternSetName"
        ] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "AsyncIterator[capo_application_insights.types.list_log_patterns_response.ListLogPatternsResponse]":
        _token = next_token
        while True:
            _response = await self.list_log_patterns(
                resource_group_name,
                config_overrides=config_overrides,
                pattern_set_name=pattern_set_name,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_log_pattern_sets(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "capo_application_insights.types.list_log_pattern_sets_response.ListLogPatternSetsResponse":
        """<p>Lists the log pattern sets in the specific application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.list_log_pattern_sets_request.ListLogPatternSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.list_log_pattern_sets_response.ListLogPatternSetsResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.list_log_pattern_sets

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.list_log_pattern_sets.async_list_log_pattern_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.list_log_pattern_sets_request.ListLogPatternSetsRequest = {
            "resource_group_name": resource_group_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_log_pattern_sets(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "AsyncIterator[capo_application_insights.types.list_log_pattern_sets_response.ListLogPatternSetsResponse]":
        _token = next_token
        while True:
            _response = await self.list_log_pattern_sets(
                resource_group_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_problems(
        self,
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
        resource_group_name: Optional[
            "capo_application_insights.types.resource_group_name.ResourceGroupName"
        ] = None,
        start_time: Optional[
            "capo_application_insights.types.start_time.StartTime"
        ] = None,
        end_time: Optional["capo_application_insights.types.end_time.EndTime"] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        component_name: Optional[
            "capo_application_insights.types.component_name.ComponentName"
        ] = None,
        visibility: Optional[
            "capo_application_insights.types.visibility.Visibility"
        ] = None,
    ) -> "capo_application_insights.types.list_problems_response.ListProblemsResponse":
        """<p>Lists the problems with your application.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID for the resource group owner.</p>
            resource_group_name: <p>The name of the resource group.</p>
            start_time: <p>The time when the problem was detected, in epoch seconds. If you don't specify a time frame for the request, problems within the past seven days are returned.</p>
            end_time: <p>The time when the problem ended, in epoch seconds. If not specified, problems within the past seven days are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            component_name: <p> The name of the component. </p>
            visibility: <p>Specifies whether or not you can view the problem. If not specified, visible and ignored problems are returned.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.list_problems_request.ListProblemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.list_problems_response.ListProblemsResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.list_problems

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.list_problems.async_list_problems(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.list_problems_request.ListProblemsRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id
        if resource_group_name is not None:
            input_["resource_group_name"] = resource_group_name
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if component_name is not None:
            input_["component_name"] = component_name
        if visibility is not None:
            input_["visibility"] = visibility

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_problems(
        self,
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
        resource_group_name: Optional[
            "capo_application_insights.types.resource_group_name.ResourceGroupName"
        ] = None,
        start_time: Optional[
            "capo_application_insights.types.start_time.StartTime"
        ] = None,
        end_time: Optional["capo_application_insights.types.end_time.EndTime"] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        component_name: Optional[
            "capo_application_insights.types.component_name.ComponentName"
        ] = None,
        visibility: Optional[
            "capo_application_insights.types.visibility.Visibility"
        ] = None,
    ) -> "AsyncIterator[capo_application_insights.types.list_problems_response.ListProblemsResponse]":
        _token = next_token
        while True:
            _response = await self.list_problems(
                config_overrides=config_overrides,
                account_id=account_id,
                resource_group_name=resource_group_name,
                start_time=start_time,
                end_time=end_time,
                max_results=max_results,
                next_token=_token,
                component_name=component_name,
                visibility=visibility,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_application_insights.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieve a list of the tags (keys and values) that are associated with a specified application. A <i>tag</i> is a label that you optionally define and associate with an application. Each tag consists of a required <i>tag key</i> and an optional associated <i>tag value</i>. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the application that you want to retrieve tag information for.</p>

        Raises:
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workloads(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> (
        "capo_application_insights.types.list_workloads_response.ListWorkloadsResponse"
    ):
        """<p>Lists the workloads that are configured on a given component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            max_results: <p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token to request the next page of results.</p>
            account_id: <p>The Amazon Web Services account ID of the owner of the workload.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.list_workloads_request.ListWorkloadsRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.list_workloads_response.ListWorkloadsResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.list_workloads

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.list_workloads.async_list_workloads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.list_workloads_request.ListWorkloadsRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_workloads(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        max_results: Optional[
            "capo_application_insights.types.max_entities.MaxEntities"
        ] = None,
        next_token: Optional[
            "capo_application_insights.types.pagination_token.PaginationToken"
        ] = None,
        account_id: Optional[
            "capo_application_insights.types.account_id.AccountId"
        ] = None,
    ) -> "AsyncIterator[capo_application_insights.types.list_workloads_response.ListWorkloadsResponse]":
        _token = next_token
        while True:
            _response = await self.list_workloads(
                resource_group_name,
                component_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def remove_workload(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        workload_id: "capo_application_insights.types.workload_id.WorkloadId",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.remove_workload_response.RemoveWorkloadResponse":
        """<p>Remove workload from a component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            workload_id: <p>The ID of the workload.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.remove_workload_request.RemoveWorkloadRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.remove_workload_response.RemoveWorkloadResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.remove_workload

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.remove_workload.async_remove_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.remove_workload_request.RemoveWorkloadRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
            "workload_id": workload_id,
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
        resource_arn: "capo_application_insights.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_application_insights.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> "capo_application_insights.types.tag_resource_response.TagResourceResponse":
        """<p>Add one or more tags (keys and values) to a specified application. A <i>tag</i> is a label that you optionally define and associate with an application. Tags can help you categorize and manage application in different ways, such as by purpose, owner, environment, or other criteria. </p> <p>Each tag consists of a required <i>tag key</i> and an associated <i>tag value</i>, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the application that you want to add one or more tags to.</p>
            tags: <p>A list of tags that to add to the application. A tag consists of a required tag key (<code>Key</code>) and an associated tag value (<code>Value</code>). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.</p>

        Raises:
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.too_many_tags_exception.TooManyTagsException: <p>The number of the provided tags is beyond the limit, or the number of total tags you are trying to attach to the specified resource exceeds the limit.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_application_insights.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_application_insights.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
    ) -> (
        "capo_application_insights.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Remove one or more tags (keys and values) from a specified application.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the application that you want to remove one or more tags from.</p>
            tag_keys: <p>The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.</p> <p>To remove more than one tag from the application, append the <code>TagKeys</code> parameter and argument for each additional tag to remove, separated by an ampersand. </p>

        Raises:
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_application(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        ops_center_enabled: Optional[
            "capo_application_insights.types.ops_center_enabled.OpsCenterEnabled"
        ] = None,
        cwe_monitor_enabled: Optional[
            "capo_application_insights.types.cwe_monitor_enabled.CWEMonitorEnabled"
        ] = None,
        ops_item_sns_topic_arn: Optional[
            "capo_application_insights.types.ops_item_sns_topic_arn.OpsItemSNSTopicArn"
        ] = None,
        sns_notification_arn: Optional[
            "capo_application_insights.types.sns_notification_arn.SNSNotificationArn"
        ] = None,
        remove_sns_topic: Optional[
            "capo_application_insights.types.remove_sns_topic.RemoveSNSTopic"
        ] = None,
        auto_config_enabled: Optional[
            "capo_application_insights.types.auto_config_enabled.AutoConfigEnabled"
        ] = None,
        attach_missing_permission: Optional[
            "capo_application_insights.types.attach_missing_permission.AttachMissingPermission"
        ] = None,
    ) -> "capo_application_insights.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates the application.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            ops_center_enabled: <p> When set to <code>true</code>, creates opsItems for any problems detected on an application. </p>
            cwe_monitor_enabled: <p> Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as <code>instance terminated</code>, <code>failed deployment</code>, and others. </p>
            ops_item_sns_topic_arn: <p> The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem.</p>
            sns_notification_arn: <p> The SNS topic ARN. Allows you to receive SNS notifications for updates and issues with an application. </p>
            remove_sns_topic: <p> Disassociates the SNS topic from the opsItem created for detected problems.</p>
            auto_config_enabled: <p> Turns auto-configuration on or off. </p>
            attach_missing_permission: <p>If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.update_application

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.update_application_request.UpdateApplicationRequest = {
            "resource_group_name": resource_group_name
        }
        if ops_center_enabled is not None:
            input_["ops_center_enabled"] = ops_center_enabled
        if cwe_monitor_enabled is not None:
            input_["cwe_monitor_enabled"] = cwe_monitor_enabled
        if ops_item_sns_topic_arn is not None:
            input_["ops_item_sns_topic_arn"] = ops_item_sns_topic_arn
        if sns_notification_arn is not None:
            input_["sns_notification_arn"] = sns_notification_arn
        if remove_sns_topic is not None:
            input_["remove_sns_topic"] = remove_sns_topic
        if auto_config_enabled is not None:
            input_["auto_config_enabled"] = auto_config_enabled
        if attach_missing_permission is not None:
            input_["attach_missing_permission"] = attach_missing_permission

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_component(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.custom_component_name.CustomComponentName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        new_component_name: Optional[
            "capo_application_insights.types.custom_component_name.CustomComponentName"
        ] = None,
        resource_list: Optional[
            "capo_application_insights.types.resource_list.ResourceList"
        ] = None,
    ) -> "capo_application_insights.types.update_component_response.UpdateComponentResponse":
        """<p>Updates the custom component name and/or the list of resources that make up the component.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            new_component_name: <p>The new name of the component.</p>
            resource_list: <p>The list of resource ARNs that belong to the component.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already created or in use.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.update_component_request.UpdateComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.update_component_response.UpdateComponentResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.update_component

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.update_component.async_update_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.update_component_request.UpdateComponentRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
        }
        if new_component_name is not None:
            input_["new_component_name"] = new_component_name
        if resource_list is not None:
            input_["resource_list"] = resource_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_component_configuration(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        monitor: Optional["capo_application_insights.types.monitor.Monitor"] = None,
        tier: Optional["capo_application_insights.types.tier.Tier"] = None,
        component_configuration: Optional[
            "capo_application_insights.types.component_configuration.ComponentConfiguration"
        ] = None,
        auto_config_enabled: Optional[
            "capo_application_insights.types.auto_config_enabled.AutoConfigEnabled"
        ] = None,
    ) -> "capo_application_insights.types.update_component_configuration_response.UpdateComponentConfigurationResponse":
        """<p>Updates the monitoring configurations for the component. The configuration input parameter is an escaped JSON of the configuration and should match the schema of what is returned by <code>DescribeComponentConfigurationRecommendation</code>. </p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p>The name of the component.</p>
            monitor: <p>Indicates whether the application component is monitored.</p>
            tier: <p>The tier of the application component.</p>
            component_configuration: <p>The configuration settings of the component. The value is the escaped JSON of the configuration. For more information about the JSON format, see <a href="https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/working-with-json.html">Working with JSON</a>. You can send a request to <code>DescribeComponentConfigurationRecommendation</code> to see the recommended configuration for a component. For the complete format of the component configuration file, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-config.html">Component Configuration</a>.</p>
            auto_config_enabled: <p> Automatically configures the component by applying the recommended configurations. </p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already created or in use.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.update_component_configuration_request.UpdateComponentConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.update_component_configuration_response.UpdateComponentConfigurationResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.update_component_configuration

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.update_component_configuration.async_update_component_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.update_component_configuration_request.UpdateComponentConfigurationRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
        }
        if monitor is not None:
            input_["monitor"] = monitor
        if tier is not None:
            input_["tier"] = tier
        if component_configuration is not None:
            input_["component_configuration"] = component_configuration
        if auto_config_enabled is not None:
            input_["auto_config_enabled"] = auto_config_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_log_pattern(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        pattern_set_name: "capo_application_insights.types.log_pattern_set_name.LogPatternSetName",
        pattern_name: "capo_application_insights.types.log_pattern_name.LogPatternName",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        pattern: Optional[
            "capo_application_insights.types.log_pattern_regex.LogPatternRegex"
        ] = None,
        rank: Optional[
            "capo_application_insights.types.log_pattern_rank.LogPatternRank"
        ] = None,
    ) -> "capo_application_insights.types.update_log_pattern_response.UpdateLogPatternResponse":
        """<p>Adds a log pattern to a <code>LogPatternSet</code>.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            pattern_set_name: <p>The name of the log pattern set.</p>
            pattern_name: <p>The name of the log pattern.</p>
            pattern: <p>The log pattern. The pattern must be DFA compatible. Patterns that utilize forward lookahead or backreference constructions are not supported.</p>
            rank: <p>Rank of the log pattern. Must be a value between <code>1</code> and <code>1,000,000</code>. The patterns are sorted by rank, so we recommend that you set your highest priority patterns with the lowest rank. A pattern of rank <code>1</code> will be the first to get matched to a log line. A pattern of rank <code>1,000,000</code> will be last to get matched. When you configure custom log patterns from the console, a <code>Low</code> severity pattern translates to a <code>750,000</code> rank. A <code>Medium</code> severity pattern translates to a <code>500,000</code> rank. And a <code>High</code> severity pattern translates to a <code>250,000</code> rank. Rank values less than <code>1</code> or greater than <code>1,000,000</code> are reserved for Amazon Web Services provided patterns. </p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is already created or in use.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.update_log_pattern_request.UpdateLogPatternRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.update_log_pattern_response.UpdateLogPatternResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.update_log_pattern

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.update_log_pattern.async_update_log_pattern(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.update_log_pattern_request.UpdateLogPatternRequest = {
            "resource_group_name": resource_group_name,
            "pattern_set_name": pattern_set_name,
            "pattern_name": pattern_name,
        }
        if pattern is not None:
            input_["pattern"] = pattern
        if rank is not None:
            input_["rank"] = rank

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_problem(
        self,
        problem_id: "capo_application_insights.types.problem_id.ProblemId",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        update_status: Optional[
            "capo_application_insights.types.update_status.UpdateStatus"
        ] = None,
        visibility: Optional[
            "capo_application_insights.types.visibility.Visibility"
        ] = None,
    ) -> (
        "capo_application_insights.types.update_problem_response.UpdateProblemResponse"
    ):
        """<p>Updates the visibility of the problem or specifies the problem as <code>RESOLVED</code>.</p>

        Args:
            problem_id: <p>The ID of the problem.</p>
            update_status: <p>The status of the problem. Arguments can be passed for only problems that show a status of <code>RECOVERING</code>.</p>
            visibility: <p>The visibility of a problem. When you pass a value of <code>IGNORED</code>, the problem is removed from the default view, and all notifications for the problem are suspended. When <code>VISIBLE</code> is passed, the <code>IGNORED</code> action is reversed.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.update_problem_request.UpdateProblemRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.update_problem_response.UpdateProblemResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.update_problem

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.update_problem.async_update_problem(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.update_problem_request.UpdateProblemRequest = {
            "problem_id": problem_id
        }
        if update_status is not None:
            input_["update_status"] = update_status
        if visibility is not None:
            input_["visibility"] = visibility

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workload(
        self,
        resource_group_name: "capo_application_insights.types.resource_group_name.ResourceGroupName",
        component_name: "capo_application_insights.types.component_name.ComponentName",
        workload_configuration: "capo_application_insights.types.workload_configuration.WorkloadConfiguration",
        *,
        config_overrides: Optional[AsyncApplicationInsightsClientConfig] = None,
        workload_id: Optional[
            "capo_application_insights.types.workload_id.WorkloadId"
        ] = None,
    ) -> "capo_application_insights.types.update_workload_response.UpdateWorkloadResponse":
        """<p>Adds a workload to a component. Each component can have at most five workloads.</p>

        Args:
            resource_group_name: <p>The name of the resource group.</p>
            component_name: <p> The name of the component. </p>
            workload_id: <p>The ID of the workload.</p>
            workload_configuration: <p>The configuration settings of the workload. The value is the escaped JSON of the configuration.</p>

        Raises:
            capo_application_insights.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_application_insights.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource does not exist in the customer account.</p>
            capo_application_insights.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_application_insights.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_insights.types.update_workload_request.UpdateWorkloadRequest]",
        ) -> AsyncOperationResponse[
            "capo_application_insights.types.update_workload_response.UpdateWorkloadResponse"
        ]:
            import capo_application_insights._operations.ec2_windows_barley_service.update_workload

            (
                output,
                http_response,
            ) = await capo_application_insights._operations.ec2_windows_barley_service.update_workload.async_update_workload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_insights.types.update_workload_request.UpdateWorkloadRequest = {
            "resource_group_name": resource_group_name,
            "component_name": component_name,
            "workload_configuration": workload_configuration,
        }
        if workload_id is not None:
            input_["workload_id"] = workload_id

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
