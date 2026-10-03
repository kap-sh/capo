"""Generated from Smithy shape ``com.amazonaws.resourcegroups#Ardi``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_resource_groups._auth._signers
import capo_resource_groups._auth._sigv4
from capo_resource_groups._auth._identity import Credentials
from capo_resource_groups._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_resource_groups._auth._zapros_handler import AuthMiddleware
from capo_resource_groups._pagination import resolve_path as _resolve_path
from capo_resource_groups._services._aws_config import aaws_config
from capo_resource_groups._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_resource_groups.types.cancel_tag_sync_task_input
    import capo_resource_groups.types.create_group_input
    import capo_resource_groups.types.create_group_name
    import capo_resource_groups.types.create_group_output
    import capo_resource_groups.types.criticality
    import capo_resource_groups.types.delete_group_input
    import capo_resource_groups.types.delete_group_output
    import capo_resource_groups.types.description
    import capo_resource_groups.types.display_name
    import capo_resource_groups.types.get_account_settings_output
    import capo_resource_groups.types.get_group_configuration_input
    import capo_resource_groups.types.get_group_configuration_output
    import capo_resource_groups.types.get_group_input
    import capo_resource_groups.types.get_group_output
    import capo_resource_groups.types.get_group_query_input
    import capo_resource_groups.types.get_group_query_output
    import capo_resource_groups.types.get_tag_sync_task_input
    import capo_resource_groups.types.get_tag_sync_task_output
    import capo_resource_groups.types.get_tags_input
    import capo_resource_groups.types.get_tags_output
    import capo_resource_groups.types.group_arn_v2
    import capo_resource_groups.types.group_configuration_list
    import capo_resource_groups.types.group_filter_list
    import capo_resource_groups.types.group_identifier
    import capo_resource_groups.types.group_lifecycle_events_desired_status
    import capo_resource_groups.types.group_name
    import capo_resource_groups.types.group_resources_input
    import capo_resource_groups.types.group_resources_output
    import capo_resource_groups.types.group_string
    import capo_resource_groups.types.group_string_v2
    import capo_resource_groups.types.grouping_statuses_item
    import capo_resource_groups.types.list_group_resources_input
    import capo_resource_groups.types.list_group_resources_output
    import capo_resource_groups.types.list_grouping_statuses_filter_list
    import capo_resource_groups.types.list_grouping_statuses_input
    import capo_resource_groups.types.list_grouping_statuses_output
    import capo_resource_groups.types.list_groups_input
    import capo_resource_groups.types.list_groups_output
    import capo_resource_groups.types.list_tag_sync_tasks_filter_list
    import capo_resource_groups.types.list_tag_sync_tasks_input
    import capo_resource_groups.types.list_tag_sync_tasks_output
    import capo_resource_groups.types.max_results
    import capo_resource_groups.types.next_token
    import capo_resource_groups.types.owner
    import capo_resource_groups.types.put_group_configuration_input
    import capo_resource_groups.types.put_group_configuration_output
    import capo_resource_groups.types.resource_arn_list
    import capo_resource_groups.types.resource_filter_list
    import capo_resource_groups.types.resource_identifier
    import capo_resource_groups.types.resource_query
    import capo_resource_groups.types.role_arn
    import capo_resource_groups.types.search_resources_input
    import capo_resource_groups.types.search_resources_output
    import capo_resource_groups.types.start_tag_sync_task_input
    import capo_resource_groups.types.start_tag_sync_task_output
    import capo_resource_groups.types.tag_input
    import capo_resource_groups.types.tag_key
    import capo_resource_groups.types.tag_key_list
    import capo_resource_groups.types.tag_output
    import capo_resource_groups.types.tag_sync_task_arn
    import capo_resource_groups.types.tag_sync_task_item
    import capo_resource_groups.types.tag_value
    import capo_resource_groups.types.tags
    import capo_resource_groups.types.ungroup_resources_input
    import capo_resource_groups.types.ungroup_resources_output
    import capo_resource_groups.types.untag_input
    import capo_resource_groups.types.untag_output
    import capo_resource_groups.types.update_account_settings_input
    import capo_resource_groups.types.update_account_settings_output
    import capo_resource_groups.types.update_group_input
    import capo_resource_groups.types.update_group_output
    import capo_resource_groups.types.update_group_query_input
    import capo_resource_groups.types.update_group_query_output


class AsyncResourceGroupsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncResourceGroupsClient:
    """A client for the ``ResourceGroups`` service.

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
        self._config = AsyncResourceGroupsClientConfig(
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
        self, config_overrides: Optional[AsyncResourceGroupsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncResourceGroupsClientConfig = config_overrides or {}
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

    async def cancel_tag_sync_task(
        self,
        task_arn: "capo_resource_groups.types.tag_sync_task_arn.TagSyncTaskArn",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
    ) -> None:
        """<p>Cancels the specified tag-sync task. </p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:CancelTagSyncTask</code> on the application group</p> </li> <li> <p> <code>resource-groups:DeleteGroup</code> </p> </li> </ul>

        Args:
            task_arn: <p>The Amazon resource name (ARN) of the tag-sync task. </p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.cancel_tag_sync_task_input.CancelTagSyncTaskInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_resource_groups._operations.ardi.cancel_tag_sync_task

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.cancel_tag_sync_task.async_cancel_tag_sync_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.cancel_tag_sync_task_input.CancelTagSyncTaskInput = {
            "task_arn": task_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_group(
        self,
        name: "capo_resource_groups.types.create_group_name.CreateGroupName",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        description: Optional[
            "capo_resource_groups.types.description.Description"
        ] = None,
        resource_query: Optional[
            "capo_resource_groups.types.resource_query.ResourceQuery"
        ] = None,
        tags: Optional["capo_resource_groups.types.tags.Tags"] = None,
        configuration: Optional[
            "capo_resource_groups.types.group_configuration_list.GroupConfigurationList"
        ] = None,
        criticality: Optional[
            "capo_resource_groups.types.criticality.Criticality"
        ] = None,
        owner: Optional["capo_resource_groups.types.owner.Owner"] = None,
        display_name: Optional[
            "capo_resource_groups.types.display_name.DisplayName"
        ] = None,
    ) -> "capo_resource_groups.types.create_group_output.CreateGroupOutput":
        """<p>Creates a resource group with the specified name and description. You can optionally include either a resource query or a service configuration. For more information about constructing a resource query, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/getting_started-query.html">Build queries and groups in Resource Groups</a> in the <i>Resource Groups User Guide</i>. For more information about service-linked groups and service configurations, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html">Service configurations for Resource Groups</a>.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:CreateGroup</code> </p> </li> </ul>

        Args:
            name: <p>The name of the group, which is the identifier of the group in other operations. You can't change the name of a resource group after you create it. A resource group name can consist of letters, numbers, hyphens, periods, and underscores. The name cannot start with <code>AWS</code>, <code>aws</code>, or any other possible capitalization; these are reserved. A resource group name must be unique within each Amazon Web Services Region in your Amazon Web Services account.</p>
            description: <p>The description of the resource group. Descriptions can consist of letters, numbers, hyphens, underscores, periods, and spaces.</p>
            resource_query: <p>The resource query that determines which Amazon Web Services resources are members of this group. For more information about resource queries, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag">Create a tag-based group in Resource Groups</a>. </p> <note> <p>A resource group can contain either a <code>ResourceQuery</code> or a <code>Configuration</code>, but not both.</p> </note>
            tags: <p>The tags to add to the group. A tag is key-value pair string.</p>
            configuration: <p>A configuration associates the resource group with an Amazon Web Services service and specifies how the service can interact with the resources in the group. A configuration is an array of <a>GroupConfigurationItem</a> elements. For details about the syntax of service configurations, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html">Service configurations for Resource Groups</a>.</p> <note> <p>A resource group can contain either a <code>Configuration</code> or a <code>ResourceQuery</code>, but not both.</p> </note>
            criticality: <p>The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.</p>
            owner: <p>A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization. </p>
            display_name: <p>The name of the application group, which you can change at any time. </p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.create_group_input.CreateGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.create_group_output.CreateGroupOutput"
        ]:
            import capo_resource_groups._operations.ardi.create_group

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.create_group.async_create_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.create_group_input.CreateGroupInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if resource_query is not None:
            input_["resource_query"] = resource_query
        if tags is not None:
            input_["tags"] = tags
        if configuration is not None:
            input_["configuration"] = configuration
        if criticality is not None:
            input_["criticality"] = criticality
        if owner is not None:
            input_["owner"] = owner
        if display_name is not None:
            input_["display_name"] = display_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_group(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group_name: Optional["capo_resource_groups.types.group_name.GroupName"] = None,
        group: Optional[
            "capo_resource_groups.types.group_string_v2.GroupStringV2"
        ] = None,
    ) -> "capo_resource_groups.types.delete_group_output.DeleteGroupOutput":
        """<p>Deletes the specified resource group. Deleting a resource group does not delete any resources that are members of the group; it only deletes the group structure.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:DeleteGroup</code> </p> </li> </ul>

        Args:
            group_name: <p>Deprecated - don't use this parameter. Use <code>Group</code> instead.</p>
            group: <p>The name or the Amazon resource name (ARN) of the resource group to delete.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.delete_group_input.DeleteGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.delete_group_output.DeleteGroupOutput"
        ]:
            import capo_resource_groups._operations.ardi.delete_group

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.delete_group.async_delete_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.delete_group_input.DeleteGroupInput = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if group is not None:
            input_["group"] = group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account_settings(
        self, *, config_overrides: Optional[AsyncResourceGroupsClientConfig] = None
    ) -> "capo_resource_groups.types.get_account_settings_output.GetAccountSettingsOutput":
        """<p>Retrieves the current status of optional features in Resource Groups.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.get_account_settings_output.GetAccountSettingsOutput"
        ]:
            import capo_resource_groups._operations.ardi.get_account_settings

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.get_account_settings.async_get_account_settings(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group_name: Optional["capo_resource_groups.types.group_name.GroupName"] = None,
        group: Optional[
            "capo_resource_groups.types.group_string_v2.GroupStringV2"
        ] = None,
    ) -> "capo_resource_groups.types.get_group_output.GetGroupOutput":
        """<p>Returns information about a specified resource group.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:GetGroup</code> </p> </li> </ul>

        Args:
            group_name: <p>Deprecated - don't use this parameter. Use <code>Group</code> instead.</p>
            group: <p>The name or the Amazon resource name (ARN) of the resource group to retrieve.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.get_group_input.GetGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.get_group_output.GetGroupOutput"
        ]:
            import capo_resource_groups._operations.ardi.get_group

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.get_group.async_get_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.get_group_input.GetGroupInput = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if group is not None:
            input_["group"] = group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group_configuration(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group: Optional["capo_resource_groups.types.group_string.GroupString"] = None,
    ) -> "capo_resource_groups.types.get_group_configuration_output.GetGroupConfigurationOutput":
        """<p>Retrieves the service configuration associated with the specified resource group. For details about the service configuration syntax, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html">Service configurations for Resource Groups</a>.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:GetGroupConfiguration</code> </p> </li> </ul>

        Args:
            group: <p>The name or the Amazon resource name (ARN) of the resource group for which you want to retrive the service configuration.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.get_group_configuration_input.GetGroupConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.get_group_configuration_output.GetGroupConfigurationOutput"
        ]:
            import capo_resource_groups._operations.ardi.get_group_configuration

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.get_group_configuration.async_get_group_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.get_group_configuration_input.GetGroupConfigurationInput = {}
        if group is not None:
            input_["group"] = group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group_query(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group_name: Optional["capo_resource_groups.types.group_name.GroupName"] = None,
        group: Optional["capo_resource_groups.types.group_string.GroupString"] = None,
    ) -> "capo_resource_groups.types.get_group_query_output.GetGroupQueryOutput":
        """<p>Retrieves the resource query associated with the specified resource group. For more information about resource queries, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag">Create a tag-based group in Resource Groups</a>.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:GetGroupQuery</code> </p> </li> </ul>

        Args:
            group_name: <p>Don't use this parameter. Use <code>Group</code> instead.</p>
            group: <p>The name or the Amazon resource name (ARN) of the resource group to query.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.get_group_query_input.GetGroupQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.get_group_query_output.GetGroupQueryOutput"
        ]:
            import capo_resource_groups._operations.ardi.get_group_query

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.get_group_query.async_get_group_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.get_group_query_input.GetGroupQueryInput = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if group is not None:
            input_["group"] = group

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_tags(
        self,
        arn: "capo_resource_groups.types.group_arn_v2.GroupArnV2",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
    ) -> "capo_resource_groups.types.get_tags_output.GetTagsOutput":
        """<p>Returns a list of tags that are associated with a resource group, specified by an Amazon resource name (ARN).</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:GetTags</code> </p> </li> </ul>

        Args:
            arn: <p>The Amazon resource name (ARN) of the resource group whose tags you want to retrieve.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.get_tags_input.GetTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.get_tags_output.GetTagsOutput"
        ]:
            import capo_resource_groups._operations.ardi.get_tags

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.get_tags.async_get_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.get_tags_input.GetTagsInput = {"arn": arn}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_tag_sync_task(
        self,
        task_arn: "capo_resource_groups.types.tag_sync_task_arn.TagSyncTaskArn",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
    ) -> "capo_resource_groups.types.get_tag_sync_task_output.GetTagSyncTaskOutput":
        """<p>Returns information about a specified tag-sync task. </p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:GetTagSyncTask</code> on the application group</p> </li> </ul>

        Args:
            task_arn: <p>The Amazon resource name (ARN) of the tag-sync task. </p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.get_tag_sync_task_input.GetTagSyncTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.get_tag_sync_task_output.GetTagSyncTaskOutput"
        ]:
            import capo_resource_groups._operations.ardi.get_tag_sync_task

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.get_tag_sync_task.async_get_tag_sync_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.get_tag_sync_task_input.GetTagSyncTaskInput = {
            "task_arn": task_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def group_resources(
        self,
        group: "capo_resource_groups.types.group_string_v2.GroupStringV2",
        resource_arns: "capo_resource_groups.types.resource_arn_list.ResourceArnList",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
    ) -> "capo_resource_groups.types.group_resources_output.GroupResourcesOutput":
        """<p>Adds the specified resources to the specified group.</p> <important> <p>You can only use this operation with the following groups:</p> <ul> <li> <p> <code>AWS::EC2::HostManagement</code> </p> </li> <li> <p> <code>AWS::EC2::CapacityReservationPool</code> </p> </li> <li> <p> <code>AWS::ResourceGroups::ApplicationGroup</code> </p> </li> </ul> <p>Other resource group types and resource types are not currently supported by this operation.</p> </important> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:GroupResources</code> </p> </li> </ul>

        Args:
            group: <p>The name or the Amazon resource name (ARN) of the resource group to add resources to.</p>
            resource_arns: <p>The list of Amazon resource names (ARNs) of the resources to be added to the group. </p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.group_resources_input.GroupResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.group_resources_output.GroupResourcesOutput"
        ]:
            import capo_resource_groups._operations.ardi.group_resources

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.group_resources.async_group_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.group_resources_input.GroupResourcesInput = {
            "group": group,
            "resource_arns": resource_arns,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_grouping_statuses(
        self,
        group: "capo_resource_groups.types.group_string_v2.GroupStringV2",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_resource_groups.types.list_grouping_statuses_filter_list.ListGroupingStatusesFilterList"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "capo_resource_groups.types.list_grouping_statuses_output.ListGroupingStatusesOutput":
        """<p>Returns the status of the last grouping or ungrouping action for each resource in the specified application group. </p>

        Args:
            group: <p>The application group identifier, expressed as an Amazon resource name (ARN) or the application group name. </p>
            max_results: <p>The maximum number of resources and their statuses returned in the response. </p>
            filters: <p>The filter name and value pair that is used to return more specific results from a list of resources. </p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from. </p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.list_grouping_statuses_input.ListGroupingStatusesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.list_grouping_statuses_output.ListGroupingStatusesOutput"
        ]:
            import capo_resource_groups._operations.ardi.list_grouping_statuses

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.list_grouping_statuses.async_list_grouping_statuses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.list_grouping_statuses_input.ListGroupingStatusesInput = {
            "group": group
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_grouping_statuses(
        self,
        group: "capo_resource_groups.types.group_string_v2.GroupStringV2",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_resource_groups.types.list_grouping_statuses_filter_list.ListGroupingStatusesFilterList"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_resource_groups.types.grouping_statuses_item.GroupingStatusesItem]":
        _token = next_token
        while True:
            _response = await self.list_grouping_statuses(
                group,
                config_overrides=config_overrides,
                max_results=max_results,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("grouping_statuses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_group_resources(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group_name: Optional["capo_resource_groups.types.group_name.GroupName"] = None,
        group: Optional[
            "capo_resource_groups.types.group_string_v2.GroupStringV2"
        ] = None,
        filters: Optional[
            "capo_resource_groups.types.resource_filter_list.ResourceFilterList"
        ] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "capo_resource_groups.types.list_group_resources_output.ListGroupResourcesOutput":
        """<p>Returns a list of Amazon resource names (ARNs) of the resources that are members of a specified resource group.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:ListGroupResources</code> </p> </li> <li> <p> <code>cloudformation:DescribeStacks</code> </p> </li> <li> <p> <code>cloudformation:ListStackResources</code> </p> </li> <li> <p> <code>tag:GetResources</code> </p> </li> </ul>

        Args:
            group_name: <important> <p> <i> <b>Deprecated - don't use this parameter. Use the <code>Group</code> request field instead.</b> </i> </p> </important>
            group: <p>The name or the Amazon resource name (ARN) of the resource group. </p>
            filters: <p>Filters, formatted as <a>ResourceFilter</a> objects, that you want to apply to a <code>ListGroupResources</code> operation. Filters the results to include only those of the specified resource types.</p> <ul> <li> <p> <code>resource-type</code> - Filter resources by their type. Specify up to five resource types in the format <code>AWS::ServiceCode::ResourceType</code>. For example, <code>AWS::EC2::Instance</code>, or <code>AWS::S3::Bucket</code>. </p> </li> </ul> <p>When you specify a <code>resource-type</code> filter for <code>ListGroupResources</code>, Resource Groups validates your filter resource types against the types that are defined in the query associated with the group. For example, if a group contains only S3 buckets because its query specifies only that resource type, but your <code>resource-type</code> filter includes EC2 instances, AWS Resource Groups does not filter for EC2 instances. In this case, a <code>ListGroupResources</code> request returns a <code>BadRequestException</code> error with a message similar to the following:</p> <p> <code>The resource types specified as filters in the request are not valid.</code> </p> <p>The error includes a list of resource types that failed the validation because they are not part of the query associated with the group. This validation doesn't occur when the group query specifies <code>AWS::AllSupported</code>, because a group based on such a query can contain any of the allowed resource types for the query type (tag-based or Amazon CloudFront stack-based queries).</p>
            max_results: <p>The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.list_group_resources_input.ListGroupResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.list_group_resources_output.ListGroupResourcesOutput"
        ]:
            import capo_resource_groups._operations.ardi.list_group_resources

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.list_group_resources.async_list_group_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.list_group_resources_input.ListGroupResourcesInput = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if group is not None:
            input_["group"] = group
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

    async def iter_list_group_resources(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group_name: Optional["capo_resource_groups.types.group_name.GroupName"] = None,
        group: Optional[
            "capo_resource_groups.types.group_string_v2.GroupStringV2"
        ] = None,
        filters: Optional[
            "capo_resource_groups.types.resource_filter_list.ResourceFilterList"
        ] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_resource_groups.types.resource_identifier.ResourceIdentifier]":
        _token = next_token
        while True:
            _response = await self.list_group_resources(
                config_overrides=config_overrides,
                group_name=group_name,
                group=group,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_identifiers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_groups(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        filters: Optional[
            "capo_resource_groups.types.group_filter_list.GroupFilterList"
        ] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "capo_resource_groups.types.list_groups_output.ListGroupsOutput":
        """<p>Returns a list of existing Resource Groups in your account.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:ListGroups</code> </p> </li> </ul>

        Args:
            filters: <p>Filters, formatted as <a>GroupFilter</a> objects, that you want to apply to a <code>ListGroups</code> operation.</p> <ul> <li> <p> <code>resource-type</code> - Filter the results to include only those resource groups that have the specified resource type in their <code>ResourceTypeFilter</code>. For example, <code>AWS::EC2::Instance</code> would return any resource group with a <code>ResourceTypeFilter</code> that includes <code>AWS::EC2::Instance</code>.</p> </li> <li> <p> <code>configuration-type</code> - Filter the results to include only those groups that have the specified configuration types attached. The current supported values are:</p> <ul> <li> <p> <code>AWS::ResourceGroups::ApplicationGroup</code> </p> </li> <li> <p> <code>AWS::AppRegistry::Application</code> </p> </li> <li> <p> <code>AWS::AppRegistry::ApplicationResourceGroup</code> </p> </li> <li> <p> <code>AWS::CloudFormation::Stack</code> </p> </li> <li> <p> <code>AWS::EC2::CapacityReservationPool</code> </p> </li> <li> <p> <code>AWS::EC2::HostManagement</code> </p> </li> <li> <p> <code>AWS::NetworkFirewall::RuleGroup</code> </p> </li> </ul> </li> </ul>
            max_results: <p>The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.list_groups_input.ListGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.list_groups_output.ListGroupsOutput"
        ]:
            import capo_resource_groups._operations.ardi.list_groups

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.list_groups.async_list_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.list_groups_input.ListGroupsInput = {}
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

    async def iter_list_groups(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        filters: Optional[
            "capo_resource_groups.types.group_filter_list.GroupFilterList"
        ] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_resource_groups.types.group_identifier.GroupIdentifier]":
        _token = next_token
        while True:
            _response = await self.list_groups(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("group_identifiers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tag_sync_tasks(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        filters: Optional[
            "capo_resource_groups.types.list_tag_sync_tasks_filter_list.ListTagSyncTasksFilterList"
        ] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "capo_resource_groups.types.list_tag_sync_tasks_output.ListTagSyncTasksOutput":
        """<p>Returns a list of tag-sync tasks. </p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:ListTagSyncTasks</code> with the group passed in the filters as the resource or * if using no filters </p> </li> </ul>

        Args:
            filters: <p>The Amazon resource name (ARN) or name of the application group for which you want to return a list of tag-sync tasks. </p>
            max_results: <p>The maximum number of results to be included in the response. </p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from. </p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.list_tag_sync_tasks_input.ListTagSyncTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.list_tag_sync_tasks_output.ListTagSyncTasksOutput"
        ]:
            import capo_resource_groups._operations.ardi.list_tag_sync_tasks

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.list_tag_sync_tasks.async_list_tag_sync_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.list_tag_sync_tasks_input.ListTagSyncTasksInput = {}
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

    async def iter_list_tag_sync_tasks(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        filters: Optional[
            "capo_resource_groups.types.list_tag_sync_tasks_filter_list.ListTagSyncTasksFilterList"
        ] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_resource_groups.types.tag_sync_task_item.TagSyncTaskItem]":
        _token = next_token
        while True:
            _response = await self.list_tag_sync_tasks(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tag_sync_tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_group_configuration(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group: Optional["capo_resource_groups.types.group_string.GroupString"] = None,
        configuration: Optional[
            "capo_resource_groups.types.group_configuration_list.GroupConfigurationList"
        ] = None,
    ) -> "capo_resource_groups.types.put_group_configuration_output.PutGroupConfigurationOutput":
        """<p>Attaches a service configuration to the specified group. This occurs asynchronously, and can take time to complete. You can use <a>GetGroupConfiguration</a> to check the status of the update.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:PutGroupConfiguration</code> </p> </li> </ul>

        Args:
            group: <p>The name or Amazon resource name (ARN) of the resource group with the configuration that you want to update.</p>
            configuration: <p>The new configuration to associate with the specified group. A configuration associates the resource group with an Amazon Web Services service and specifies how the service can interact with the resources in the group. A configuration is an array of <a>GroupConfigurationItem</a> elements.</p> <p>For information about the syntax of a service configuration, see <a href="https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html">Service configurations for Resource Groups</a>.</p> <note> <p>A resource group can contain either a <code>Configuration</code> or a <code>ResourceQuery</code>, but not both.</p> </note>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.put_group_configuration_input.PutGroupConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.put_group_configuration_output.PutGroupConfigurationOutput"
        ]:
            import capo_resource_groups._operations.ardi.put_group_configuration

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.put_group_configuration.async_put_group_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.put_group_configuration_input.PutGroupConfigurationInput = {}
        if group is not None:
            input_["group"] = group
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_resources(
        self,
        resource_query: "capo_resource_groups.types.resource_query.ResourceQuery",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "capo_resource_groups.types.search_resources_output.SearchResourcesOutput":
        """<p>Returns a list of Amazon Web Services resource identifiers that matches the specified query. The query uses the same format as a resource query in a <a>CreateGroup</a> or <a>UpdateGroupQuery</a> operation.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:SearchResources</code> </p> </li> <li> <p> <code>cloudformation:DescribeStacks</code> </p> </li> <li> <p> <code>cloudformation:ListStackResources</code> </p> </li> <li> <p> <code>tag:GetResources</code> </p> </li> </ul>

        Args:
            resource_query: <p>The search query, using the same formats that are supported for resource group definition. For more information, see <a>CreateGroup</a>.</p>
            max_results: <p>The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>
            next_token: <p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.search_resources_input.SearchResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.search_resources_output.SearchResourcesOutput"
        ]:
            import capo_resource_groups._operations.ardi.search_resources

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.search_resources.async_search_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.search_resources_input.SearchResourcesInput = {
            "resource_query": resource_query
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

    async def iter_search_resources(
        self,
        resource_query: "capo_resource_groups.types.resource_query.ResourceQuery",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        max_results: Optional[
            "capo_resource_groups.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resource_groups.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_resource_groups.types.resource_identifier.ResourceIdentifier]":
        _token = next_token
        while True:
            _response = await self.search_resources(
                resource_query,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_identifiers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_tag_sync_task(
        self,
        group: "capo_resource_groups.types.group_string_v2.GroupStringV2",
        role_arn: "capo_resource_groups.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        tag_key: Optional["capo_resource_groups.types.tag_key.TagKey"] = None,
        tag_value: Optional["capo_resource_groups.types.tag_value.TagValue"] = None,
        resource_query: Optional[
            "capo_resource_groups.types.resource_query.ResourceQuery"
        ] = None,
    ) -> "capo_resource_groups.types.start_tag_sync_task_output.StartTagSyncTaskOutput":
        r"""<p>Creates a new tag-sync task to onboard and sync resources tagged with a specific tag key-value pair to an application. To start a tag-sync task, you need a <a href="https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#tag-sync-role">resource tagging role</a>. The resource tagging role grants permissions to tag and untag applications resources and must include a trust policy that allows Resource Groups to assume the role and perform resource tagging tasks on your behalf. </p> <p>For instructions on creating a tag-sync task, see <a href="https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#create-tag-sync">Create a tag-sync using the Resource Groups API</a> in the <i>Amazon Web Services Service Catalog AppRegistry Administrator Guide</i>. </p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:StartTagSyncTask</code> on the application group</p> </li> <li> <p> <code>resource-groups:CreateGroup</code> </p> </li> <li> <p> <code>iam:PassRole</code> on the role provided in the request </p> </li> </ul>

        Args:
            group: <p>The Amazon resource name (ARN) or name of the application group for which you want to create a tag-sync task. </p>
            tag_key: <p>The tag key. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application. </p> <p>When using the <code>TagKey</code> parameter, you must also specify the <code>TagValue</code> parameter. If you specify a tag key-value pair, you can't use the <code>ResourceQuery</code> parameter. </p>
            tag_value: <p>The tag value. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application. </p> <p>When using the <code>TagValue</code> parameter, you must also specify the <code>TagKey</code> parameter. If you specify a tag key-value pair, you can't use the <code>ResourceQuery</code> parameter. </p>
            resource_query: <p>The query you can use to create the tag-sync task. With this method, all resources matching the query are added to the specified application group. A <code>ResourceQuery</code> specifies both a query <code>Type</code> and a <code>Query</code> string as JSON string objects. For more information on defining a resource query for a tag-sync task, see the tag-based query type in <a href="https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#getting_started-query_types"> Types of resource group queries</a> in <i>Resource Groups User Guide</i>. </p> <p>When using the <code>ResourceQuery</code> parameter, you cannot use the <code>TagKey</code> and <code>TagValue</code> parameters. </p> <p>When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (\). For example, a complete <code>ResourceQuery</code> parameter must be formatted like the following CLI parameter example:</p> <p> <code>--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'</code> </p> <p>In the preceding example, all of the double quote characters in the value part of the <code>Query</code> element must be escaped because the value itself is surrounded by double quotes. For more information, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html">Quoting strings</a> in the <i>Command Line Interface User Guide</i>.</p> <p>For the complete list of resource types that you can use in the array value for <code>ResourceTypeFilters</code>, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html">Resources you can use with Resource Groups and Tag Editor</a> in the <i>Resource Groups User Guide</i>. For example:</p> <p> <code>"ResourceTypeFilters":["AWS::S3::Bucket", "AWS::EC2::Instance"]</code> </p>
            role_arn: <p>The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.unauthorized_exception.UnauthorizedException: <p>The request was rejected because it doesn't have valid credentials for the target resource.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.start_tag_sync_task_input.StartTagSyncTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.start_tag_sync_task_output.StartTagSyncTaskOutput"
        ]:
            import capo_resource_groups._operations.ardi.start_tag_sync_task

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.start_tag_sync_task.async_start_tag_sync_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.start_tag_sync_task_input.StartTagSyncTaskInput = {
            "group": group,
            "role_arn": role_arn,
        }
        if tag_key is not None:
            input_["tag_key"] = tag_key
        if tag_value is not None:
            input_["tag_value"] = tag_value
        if resource_query is not None:
            input_["resource_query"] = resource_query

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag(
        self,
        arn: "capo_resource_groups.types.group_arn_v2.GroupArnV2",
        tags: "capo_resource_groups.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
    ) -> "capo_resource_groups.types.tag_output.TagOutput":
        """<p>Adds tags to a resource group with the specified Amazon resource name (ARN). Existing tags on a resource group are not changed if they are not specified in the request parameters.</p> <important> <p>Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.</p> </important> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:Tag</code> </p> </li> </ul>

        Args:
            arn: <p>The Amazon resource name (ARN) of the resource group to which to add tags.</p>
            tags: <p>The tags to add to the specified resource group. A tag is a string-to-string map of key-value pairs.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.tag_input.TagInput]",
        ) -> AsyncOperationResponse["capo_resource_groups.types.tag_output.TagOutput"]:
            import capo_resource_groups._operations.ardi.tag

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.tag.async_tag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.tag_input.TagInput = {
            "arn": arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def ungroup_resources(
        self,
        group: "capo_resource_groups.types.group_string_v2.GroupStringV2",
        resource_arns: "capo_resource_groups.types.resource_arn_list.ResourceArnList",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
    ) -> "capo_resource_groups.types.ungroup_resources_output.UngroupResourcesOutput":
        """<p>Removes the specified resources from the specified group. This operation works only with static groups that you populated using the <a>GroupResources</a> operation. It doesn't work with any resource groups that are automatically populated by tag-based or CloudFormation stack-based queries.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:UngroupResources</code> </p> </li> </ul>

        Args:
            group: <p>The name or the Amazon resource name (ARN) of the resource group from which to remove the resources.</p>
            resource_arns: <p>The Amazon resource names (ARNs) of the resources to be removed from the group.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.ungroup_resources_input.UngroupResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.ungroup_resources_output.UngroupResourcesOutput"
        ]:
            import capo_resource_groups._operations.ardi.ungroup_resources

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.ungroup_resources.async_ungroup_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.ungroup_resources_input.UngroupResourcesInput = {
            "group": group,
            "resource_arns": resource_arns,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag(
        self,
        arn: "capo_resource_groups.types.group_arn_v2.GroupArnV2",
        keys: "capo_resource_groups.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
    ) -> "capo_resource_groups.types.untag_output.UntagOutput":
        """<p>Deletes tags from a specified resource group.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:Untag</code> </p> </li> </ul>

        Args:
            arn: <p>The Amazon resource name (ARN) of the resource group from which to remove tags. The command removed both the specified keys and any values associated with those keys.</p>
            keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.untag_input.UntagInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.untag_output.UntagOutput"
        ]:
            import capo_resource_groups._operations.ardi.untag

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.untag.async_untag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.untag_input.UntagInput = {
            "arn": arn,
            "keys": keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_account_settings(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group_lifecycle_events_desired_status: Optional[
            "capo_resource_groups.types.group_lifecycle_events_desired_status.GroupLifecycleEventsDesiredStatus"
        ] = None,
    ) -> "capo_resource_groups.types.update_account_settings_output.UpdateAccountSettingsOutput":
        """<p>Turns on or turns off optional features in Resource Groups.</p> <p>The preceding example shows that the request to turn on group lifecycle events is <code>IN_PROGRESS</code>. You can call the <a>GetAccountSettings</a> operation to check for completion by looking for <code>GroupLifecycleEventsStatus</code> to change to <code>ACTIVE</code>.</p>

        Args:
            group_lifecycle_events_desired_status: <p>Specifies whether you want to turn <a href="https://docs.aws.amazon.com/ARG/latest/userguide/monitor-groups.html">group lifecycle events</a> on or off.</p> <p>You can't turn on group lifecycle events if your resource groups quota is greater than 2,000. </p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.update_account_settings_input.UpdateAccountSettingsInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.update_account_settings_output.UpdateAccountSettingsOutput"
        ]:
            import capo_resource_groups._operations.ardi.update_account_settings

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.update_account_settings.async_update_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.update_account_settings_input.UpdateAccountSettingsInput = {}
        if group_lifecycle_events_desired_status is not None:
            input_["group_lifecycle_events_desired_status"] = (
                group_lifecycle_events_desired_status
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_group(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group_name: Optional["capo_resource_groups.types.group_name.GroupName"] = None,
        group: Optional[
            "capo_resource_groups.types.group_string_v2.GroupStringV2"
        ] = None,
        description: Optional[
            "capo_resource_groups.types.description.Description"
        ] = None,
        criticality: Optional[
            "capo_resource_groups.types.criticality.Criticality"
        ] = None,
        owner: Optional["capo_resource_groups.types.owner.Owner"] = None,
        display_name: Optional[
            "capo_resource_groups.types.display_name.DisplayName"
        ] = None,
    ) -> "capo_resource_groups.types.update_group_output.UpdateGroupOutput":
        """<p>Updates the description for an existing group. You cannot update the name of a resource group.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:UpdateGroup</code> </p> </li> </ul>

        Args:
            group_name: <p>Don't use this parameter. Use <code>Group</code> instead.</p>
            group: <p>The name or the ARN of the resource group to update.</p>
            description: <p>The new description that you want to update the resource group with. Descriptions can contain letters, numbers, hyphens, underscores, periods, and spaces.</p>
            criticality: <p>The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.</p>
            owner: <p>A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization. </p>
            display_name: <p>The name of the application group, which you can change at any time. </p>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.update_group_input.UpdateGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.update_group_output.UpdateGroupOutput"
        ]:
            import capo_resource_groups._operations.ardi.update_group

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.update_group.async_update_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.update_group_input.UpdateGroupInput = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if group is not None:
            input_["group"] = group
        if description is not None:
            input_["description"] = description
        if criticality is not None:
            input_["criticality"] = criticality
        if owner is not None:
            input_["owner"] = owner
        if display_name is not None:
            input_["display_name"] = display_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_group_query(
        self,
        resource_query: "capo_resource_groups.types.resource_query.ResourceQuery",
        *,
        config_overrides: Optional[AsyncResourceGroupsClientConfig] = None,
        group_name: Optional["capo_resource_groups.types.group_name.GroupName"] = None,
        group: Optional["capo_resource_groups.types.group_string.GroupString"] = None,
    ) -> "capo_resource_groups.types.update_group_query_output.UpdateGroupQueryOutput":
        """<p>Updates the resource query of a group. For more information about resource queries, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag">Create a tag-based group in Resource Groups</a>.</p> <p> <b>Minimum permissions</b> </p> <p>To run this command, you must have the following permissions:</p> <ul> <li> <p> <code>resource-groups:UpdateGroupQuery</code> </p> </li> </ul>

        Args:
            group_name: <p>Don't use this parameter. Use <code>Group</code> instead.</p>
            group: <p>The name or the Amazon resource name (ARN) of the resource group to query.</p>
            resource_query: <p>The resource query to determine which Amazon Web Services resources are members of this resource group.</p> <note> <p>A resource group can contain either a <code>Configuration</code> or a <code>ResourceQuery</code>, but not both.</p> </note>

        Raises:
            capo_resource_groups.errors.bad_request_exception.BadRequestException: <p>The request includes one or more parameters that violate validation rules.</p>
            capo_resource_groups.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request. Check permissions.</p>
            capo_resource_groups.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred while processing the request. Try again later.</p>
            capo_resource_groups.errors.method_not_allowed_exception.MethodNotAllowedException: <p>The request uses an HTTP method that isn't allowed for the specified resource.</p>
            capo_resource_groups.errors.not_found_exception.NotFoundException: <p>One or more of the specified resources don't exist.</p>
            capo_resource_groups.errors.too_many_requests_exception.TooManyRequestsException: <p>You've exceeded throttling limits by making too many requests in a period of time.</p>
            capo_resource_groups.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups.types.update_group_query_input.UpdateGroupQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups.types.update_group_query_output.UpdateGroupQueryOutput"
        ]:
            import capo_resource_groups._operations.ardi.update_group_query

            (
                output,
                http_response,
            ) = await capo_resource_groups._operations.ardi.update_group_query.async_update_group_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups.types.update_group_query_input.UpdateGroupQueryInput = {
            "resource_query": resource_query
        }
        if group_name is not None:
            input_["group_name"] = group_name
        if group is not None:
            input_["group"] = group

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
