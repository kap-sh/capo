"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#NetworkFlowMonitor``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_networkflowmonitor._auth._signers
import capo_networkflowmonitor._auth._sigv4
from capo_networkflowmonitor._auth._identity import Credentials
from capo_networkflowmonitor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_networkflowmonitor._auth._zapros_handler import AuthMiddleware
from capo_networkflowmonitor._pagination import resolve_path as _resolve_path
from capo_networkflowmonitor._resources.network_flow_monitor.monitor_resource import (
    AsyncMonitorResource,
)
from capo_networkflowmonitor._resources.network_flow_monitor.scope_resource import (
    AsyncScopeResource,
)
from capo_networkflowmonitor._services._aws_config import aaws_config
from capo_networkflowmonitor._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.arn
    import capo_networkflowmonitor.types.create_monitor_input
    import capo_networkflowmonitor.types.create_monitor_output
    import capo_networkflowmonitor.types.create_scope_input
    import capo_networkflowmonitor.types.create_scope_output
    import capo_networkflowmonitor.types.delete_monitor_input
    import capo_networkflowmonitor.types.delete_monitor_output
    import capo_networkflowmonitor.types.delete_scope_input
    import capo_networkflowmonitor.types.delete_scope_output
    import capo_networkflowmonitor.types.destination_category
    import capo_networkflowmonitor.types.get_monitor_input
    import capo_networkflowmonitor.types.get_monitor_output
    import capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_input
    import capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_output
    import capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_input
    import capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_output
    import capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_input
    import capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_output
    import capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_input
    import capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_output
    import capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_input
    import capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_output
    import capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_input
    import capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_output
    import capo_networkflowmonitor.types.get_scope_input
    import capo_networkflowmonitor.types.get_scope_output
    import capo_networkflowmonitor.types.limit
    import capo_networkflowmonitor.types.list_monitors_input
    import capo_networkflowmonitor.types.list_monitors_output
    import capo_networkflowmonitor.types.list_scopes_input
    import capo_networkflowmonitor.types.list_scopes_output
    import capo_networkflowmonitor.types.list_tags_for_resource_input
    import capo_networkflowmonitor.types.list_tags_for_resource_output
    import capo_networkflowmonitor.types.max_results
    import capo_networkflowmonitor.types.monitor_local_resources
    import capo_networkflowmonitor.types.monitor_metric
    import capo_networkflowmonitor.types.monitor_remote_resources
    import capo_networkflowmonitor.types.monitor_status
    import capo_networkflowmonitor.types.monitor_summary
    import capo_networkflowmonitor.types.monitor_top_contributors_row
    import capo_networkflowmonitor.types.resource_name
    import capo_networkflowmonitor.types.scope_id
    import capo_networkflowmonitor.types.scope_summary
    import capo_networkflowmonitor.types.start_query_monitor_top_contributors_input
    import capo_networkflowmonitor.types.start_query_monitor_top_contributors_output
    import capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_input
    import capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_output
    import capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_input
    import capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_output
    import capo_networkflowmonitor.types.stop_query_monitor_top_contributors_input
    import capo_networkflowmonitor.types.stop_query_monitor_top_contributors_output
    import capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_input
    import capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_output
    import capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_input
    import capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_output
    import capo_networkflowmonitor.types.tag_key_list
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.tag_resource_input
    import capo_networkflowmonitor.types.tag_resource_output
    import capo_networkflowmonitor.types.target_resource_list
    import capo_networkflowmonitor.types.untag_resource_input
    import capo_networkflowmonitor.types.untag_resource_output
    import capo_networkflowmonitor.types.update_monitor_input
    import capo_networkflowmonitor.types.update_monitor_output
    import capo_networkflowmonitor.types.update_scope_input
    import capo_networkflowmonitor.types.update_scope_output
    import capo_networkflowmonitor.types.uuid_string
    import capo_networkflowmonitor.types.workload_insights_metric
    import capo_networkflowmonitor.types.workload_insights_top_contributors_data_point
    import capo_networkflowmonitor.types.workload_insights_top_contributors_row


class AsyncNetworkFlowMonitorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncNetworkFlowMonitorClient:
    """A client for the ``NetworkFlowMonitor`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
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
        self._config = AsyncNetworkFlowMonitorClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.monitor_resource = AsyncMonitorResource(self)
        self.scope_resource = AsyncScopeResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncNetworkFlowMonitorClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_networkflowmonitor.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns all the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_networkflowmonitor.types.arn.Arn",
        tags: "capo_networkflowmonitor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.tag_resource_output.TagResourceOutput":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags for a resource.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.tag_resource

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_networkflowmonitor.types.arn.Arn",
        tag_keys: "capo_networkflowmonitor.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>Keys that you specified when you tagged a resource.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.untag_resource

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.untag_resource_input.UntagResourceInput = {
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

    async def create_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        local_resources: "capo_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources",
        scope_arn: "capo_networkflowmonitor.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        remote_resources: Optional[
            "capo_networkflowmonitor.types.monitor_remote_resources.MonitorRemoteResources"
        ] = None,
        client_token: Optional[
            "capo_networkflowmonitor.types.uuid_string.UuidString"
        ] = None,
        tags: Optional["capo_networkflowmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkflowmonitor.types.create_monitor_output.CreateMonitorOutput":
        """<p>Create a monitor for specific network flows between local and remote resources, so that you can monitor network performance for one or several of your workloads. For each monitor, Network Flow Monitor publishes detailed end-to-end performance metrics and a network health indicator (NHI) that informs you whether there were Amazon Web Services network issues for one or more of the network flows tracked by a monitor, during a time period that you choose. </p>

        Args:
            monitor_name: <p>The name of the monitor. </p>
            local_resources: <p>The local resources to monitor. A local resource in a workload is the location of the host, or hosts, where the Network Flow Monitor agent is installed. For example, if a workload consists of an interaction between a web service and a backend database (for example, Amazon Dynamo DB), the subnet with the EC2 instance that hosts the web service, which also runs the agent, is the local resource.</p> <p>Be aware that all local resources must belong to the current Region.</p>
            remote_resources: <p>The remote resources to monitor. A remote resource is the other endpoint in the bi-directional flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource.</p> <p>When you specify remote resources, be aware that specific combinations of resources are allowed and others are not, including the following constraints:</p> <ul> <li> <p>All remote resources that you specify must all belong to a single Region.</p> </li> <li> <p>If you specify Amazon Web Services services as remote resources, any other remote resources that you specify must be in the current Region.</p> </li> <li> <p>When you specify a remote resource for another Region, you can only specify the <code>Region</code> resource type. You cannot specify a subnet, VPC, or Availability Zone in another Region.</p> </li> <li> <p>If you leave the <code>RemoteResources</code> parameter empty, the monitor will include all network flows that terminate in the current Region.</p> </li> </ul>
            scope_arn: <p>The Amazon Resource Name (ARN) of the scope for the monitor.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>
            tags: <p>The tags for a monitor. You can add a maximum of 200 tags.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.create_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.create_monitor.async_create_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.create_monitor_input.CreateMonitorInput = {
            "monitor_name": monitor_name,
            "local_resources": local_resources,
            "scope_arn": scope_arn,
        }
        if remote_resources is not None:
            input_["remote_resources"] = remote_resources
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.get_monitor_output.GetMonitorOutput":
        """<p>Gets information about a monitor in Network Flow Monitor based on a monitor name. The information returned includes the Amazon Resource Name (ARN), create time, modified time, resources included in the monitor, and status information.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_monitor.async_get_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_monitor_input.GetMonitorInput = {
            "monitor_name": monitor_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        local_resources_to_add: Optional[
            "capo_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources"
        ] = None,
        local_resources_to_remove: Optional[
            "capo_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources"
        ] = None,
        remote_resources_to_add: Optional[
            "capo_networkflowmonitor.types.monitor_remote_resources.MonitorRemoteResources"
        ] = None,
        remote_resources_to_remove: Optional[
            "capo_networkflowmonitor.types.monitor_remote_resources.MonitorRemoteResources"
        ] = None,
        client_token: Optional[
            "capo_networkflowmonitor.types.uuid_string.UuidString"
        ] = None,
    ) -> "capo_networkflowmonitor.types.update_monitor_output.UpdateMonitorOutput":
        """<p>Update a monitor to add or remove local or remote resources.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            local_resources_to_add: <p>Additional local resources to specify network flows for a monitor, as an array of resources with identifiers and types. A local resource in a workload is the location of hosts where the Network Flow Monitor agent is installed. </p>
            local_resources_to_remove: <p>The local resources to remove, as an array of resources with identifiers and types.</p>
            remote_resources_to_add: <p>The remote resources to add, as an array of resources with identifiers and types.</p> <p>A remote resource is the other endpoint in the flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource. </p>
            remote_resources_to_remove: <p>The remote resources to remove, as an array of resources with identifiers and types.</p> <p>A remote resource is the other endpoint specified for the network flow of a workload, with a local resource. For example, Amazon Dynamo DB can be a remote resource. </p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.update_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.update_monitor.async_update_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.update_monitor_input.UpdateMonitorInput = {
            "monitor_name": monitor_name
        }
        if local_resources_to_add is not None:
            input_["local_resources_to_add"] = local_resources_to_add
        if local_resources_to_remove is not None:
            input_["local_resources_to_remove"] = local_resources_to_remove
        if remote_resources_to_add is not None:
            input_["remote_resources_to_add"] = remote_resources_to_add
        if remote_resources_to_remove is not None:
            input_["remote_resources_to_remove"] = remote_resources_to_remove
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

    async def delete_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.delete_monitor_output.DeleteMonitorOutput":
        """<p>Deletes a monitor in Network Flow Monitor.</p>

        Args:
            monitor_name: <p>The name of the monitor to delete.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.delete_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.delete_monitor.async_delete_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.delete_monitor_input.DeleteMonitorInput = {
            "monitor_name": monitor_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_monitors(
        self,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_networkflowmonitor.types.max_results.MaxResults"
        ] = None,
        monitor_status: Optional[
            "capo_networkflowmonitor.types.monitor_status.MonitorStatus"
        ] = None,
    ) -> "capo_networkflowmonitor.types.list_monitors_output.ListMonitorsOutput":
        """<p>List all monitors in an account. Optionally, you can list only monitors that have a specific status, by using the <code>STATUS</code> parameter.</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>
            monitor_status: <p>The status of a monitor. The status can be one of the following</p> <ul> <li> <p> <code>PENDING</code>: The monitor is in the process of being created.</p> </li> <li> <p> <code>ACTIVE</code>: The monitor is active.</p> </li> <li> <p> <code>INACTIVE</code>: The monitor is inactive.</p> </li> <li> <p> <code>ERROR</code>: Monitor creation failed due to an error.</p> </li> <li> <p> <code>DELETING</code>: The monitor is in the process of being deleted.</p> </li> </ul>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.list_monitors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.list_monitors.async_list_monitors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.list_monitors_input.ListMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if monitor_status is not None:
            input_["monitor_status"] = monitor_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_monitors(
        self,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_networkflowmonitor.types.max_results.MaxResults"
        ] = None,
        monitor_status: Optional[
            "capo_networkflowmonitor.types.monitor_status.MonitorStatus"
        ] = None,
    ) -> "AsyncIterator[capo_networkflowmonitor.types.monitor_summary.MonitorSummary]":
        _token = next_token
        while True:
            _response = await self.list_monitors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                monitor_status=monitor_status,
            )
            _page = _resolve_path(_response, ("monitors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_query_results_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_output.GetQueryResultsMonitorTopContributorsOutput":
        """<p>Return the data for a query with the Network Flow Monitor query interface. You specify the query that you want to return results for by providing a query ID and a monitor name. This query returns the top contributors for a specific monitor.</p> <p>Create a query ID for this call by calling the corresponding API call to start the query, <code>StartQueryMonitorTopContributors</code>. Use the scope ID that was returned for your account by <code>CreateScope</code>.</p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_input.GetQueryResultsMonitorTopContributorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_output.GetQueryResultsMonitorTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_monitor_top_contributors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_monitor_top_contributors.async_get_query_results_monitor_top_contributors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_input.GetQueryResultsMonitorTopContributorsInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
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

    async def iter_get_query_results_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_networkflowmonitor.types.monitor_top_contributors_row.MonitorTopContributorsRow]":
        _token = next_token
        while True:
            _response = await self.get_query_results_monitor_top_contributors(
                monitor_name,
                query_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("top_contributors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_query_status_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_output.GetQueryStatusMonitorTopContributorsOutput":
        """<p>Returns the current status of a query for the Network Flow Monitor query interface, for a specified query ID and monitor. This call returns the query status for the top contributors for a monitor.</p> <p>When you create a query, use this call to check the status of the query to make sure that it has has <code>SUCCEEDED</code> before you review the results. Use the same query ID that you used for the corresponding API call to start (create) the query, <code>StartQueryMonitorTopContributors</code>.</p> <p>When you run a query, use this call to check the status of the query to make sure that the query has <code>SUCCEEDED</code> before you review the results.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_input.GetQueryStatusMonitorTopContributorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_output.GetQueryStatusMonitorTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_monitor_top_contributors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_monitor_top_contributors.async_get_query_status_monitor_top_contributors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_input.GetQueryStatusMonitorTopContributorsInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_query_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        metric_name: "capo_networkflowmonitor.types.monitor_metric.MonitorMetric",
        destination_category: "capo_networkflowmonitor.types.destination_category.DestinationCategory",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        limit: Optional["capo_networkflowmonitor.types.limit.Limit"] = None,
    ) -> "capo_networkflowmonitor.types.start_query_monitor_top_contributors_output.StartQueryMonitorTopContributorsOutput":
        """<p>Create a query that you can use with the Network Flow Monitor query interface to return the top contributors for a monitor. Specify the monitor that you want to create the query for. </p> <p>The call returns a query ID that you can use with <a href="https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsMonitorTopContributors.html"> GetQueryResultsMonitorTopContributors</a> to run the query and return the top contributors for a specific monitor.</p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable APIs for the top contributors that you want to be returned.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            start_time: <p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>
            end_time: <p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>
            metric_name: <p>The metric that you want to query top contributors for. That is, you can specify a metric with this call and return the top contributor network flows, for that type of metric, for a monitor and (optionally) within a specific category, such as network flows between Availability Zones.</p>
            destination_category: <p>The category that you want to query top contributors for, for a specific monitor. Destination categories can be one of the following: </p> <ul> <li> <p> <code>INTRA_AZ</code>: Top contributor network flows within a single Availability Zone</p> </li> <li> <p> <code>INTER_AZ</code>: Top contributor network flows between Availability Zones</p> </li> <li> <p> <code>INTER_REGION</code>: Top contributor network flows between Regions (to the edge of another Region)</p> </li> <li> <p> <code>INTER_VPC</code>: Top contributor network flows between VPCs</p> </li> <li> <p> <code>AMAZON_S3</code>: Top contributor network flows to or from Amazon S3</p> </li> <li> <p> <code>AMAZON_DYNAMODB</code>: Top contributor network flows to or from Amazon Dynamo DB</p> </li> <li> <p> <code>UNCLASSIFIED</code>: Top contributor network flows that do not have a bucket classification</p> </li> </ul>
            limit: <p>The maximum number of top contributors to return.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.start_query_monitor_top_contributors_input.StartQueryMonitorTopContributorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.start_query_monitor_top_contributors_output.StartQueryMonitorTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.start_query_monitor_top_contributors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.start_query_monitor_top_contributors.async_start_query_monitor_top_contributors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.start_query_monitor_top_contributors_input.StartQueryMonitorTopContributorsInput = {
            "monitor_name": monitor_name,
            "start_time": start_time,
            "end_time": end_time,
            "metric_name": metric_name,
            "destination_category": destination_category,
        }
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_query_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.stop_query_monitor_top_contributors_output.StopQueryMonitorTopContributorsOutput":
        """<p>Stop a top contributors query for a monitor. Specify the query that you want to stop by providing a query ID and a monitor name. </p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.stop_query_monitor_top_contributors_input.StopQueryMonitorTopContributorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.stop_query_monitor_top_contributors_output.StopQueryMonitorTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.stop_query_monitor_top_contributors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.stop_query_monitor_top_contributors.async_stop_query_monitor_top_contributors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.stop_query_monitor_top_contributors_input.StopQueryMonitorTopContributorsInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_scope(
        self,
        targets: "capo_networkflowmonitor.types.target_resource_list.TargetResourceList",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        client_token: Optional[
            "capo_networkflowmonitor.types.uuid_string.UuidString"
        ] = None,
        tags: Optional["capo_networkflowmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkflowmonitor.types.create_scope_output.CreateScopeOutput":
        """<p>In Network Flow Monitor, you specify a scope for the service to generate metrics for. By using the scope, Network Flow Monitor can generate a topology of all the resources to measure performance metrics for. When you create a scope, you enable permissions for Network Flow Monitor.</p> <p>A scope is a Region-account pair or multiple Region-account pairs. Network Flow Monitor uses your scope to determine all the resources (the topology) where Network Flow Monitor will gather network flow performance metrics for you. To provide performance metrics, Network Flow Monitor uses the data that is sent by the Network Flow Monitor agents you install on the resources.</p> <p>To define the Region-account pairs for your scope, the Network Flow Monitor API uses the following constucts, which allow for future flexibility in defining scopes:</p> <ul> <li> <p> <i>Targets</i>, which are arrays of targetResources.</p> </li> <li> <p> <i>Target resources</i>, which are Region-targetIdentifier pairs.</p> </li> <li> <p> <i>Target identifiers</i>, made up of a targetID (currently always an account ID) and a targetType (currently always an account). </p> </li> </ul>

        Args:
            targets: <p>The targets to define the scope to be monitored. A target is an array of targetResources, which are currently Region-account pairs, defined by targetResource constructs.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>
            tags: <p>The tags for a scope. You can add a maximum of 200 tags.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.create_scope_input.CreateScopeInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.create_scope_output.CreateScopeOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.create_scope

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.create_scope.async_create_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.create_scope_input.CreateScopeInput = {
            "targets": targets
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_scope(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.get_scope_output.GetScopeOutput":
        """<p>Gets information about a scope, including the name, status, tags, and target details. The scope in Network Flow Monitor is an account.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account. A scope ID is returned from a <code>CreateScope</code> API call.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_scope_input.GetScopeInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_scope_output.GetScopeOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_scope

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_scope.async_get_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_scope_input.GetScopeInput = {
            "scope_id": scope_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_scope(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        resources_to_add: Optional[
            "capo_networkflowmonitor.types.target_resource_list.TargetResourceList"
        ] = None,
        resources_to_delete: Optional[
            "capo_networkflowmonitor.types.target_resource_list.TargetResourceList"
        ] = None,
    ) -> "capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput":
        """<p>Update a scope to add or remove resources that you want to be available for Network Flow Monitor to generate metrics for, when you have active agents on those resources sending metrics reports to the Network Flow Monitor backend.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>
            resources_to_add: <p>A list of resources to add to a scope.</p>
            resources_to_delete: <p>A list of resources to delete from a scope.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.update_scope_input.UpdateScopeInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.update_scope

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.update_scope.async_update_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.update_scope_input.UpdateScopeInput = {
            "scope_id": scope_id
        }
        if resources_to_add is not None:
            input_["resources_to_add"] = resources_to_add
        if resources_to_delete is not None:
            input_["resources_to_delete"] = resources_to_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_scope(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.delete_scope_output.DeleteScopeOutput":
        """<p>Deletes a scope that has been defined.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.delete_scope_input.DeleteScopeInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.delete_scope_output.DeleteScopeOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.delete_scope

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.delete_scope.async_delete_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.delete_scope_input.DeleteScopeInput = {
            "scope_id": scope_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_scopes(
        self,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_networkflowmonitor.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_networkflowmonitor.types.list_scopes_output.ListScopesOutput":
        """<p>List all the scopes for an account.</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.list_scopes_input.ListScopesInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.list_scopes_output.ListScopesOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.list_scopes

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.list_scopes.async_list_scopes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.list_scopes_input.ListScopesInput = {}
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

    async def iter_list_scopes(
        self,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_networkflowmonitor.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_networkflowmonitor.types.scope_summary.ScopeSummary]":
        _token = next_token
        while True:
            _response = await self.list_scopes(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("scopes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_query_results_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_output.GetQueryResultsWorkloadInsightsTopContributorsOutput":
        """<p>Return the data for a query with the Network Flow Monitor query interface. You specify the query that you want to return results for by providing a query ID and a monitor name.</p> <p>This query returns the top contributors for a scope for workload insights. Workload insights provide a high level view of network flow performance data collected by agents. To return the data for the top contributors, see <code>GetQueryResultsWorkloadInsightsTopContributorsData</code>.</p> <p>Create a query ID for this call by calling the corresponding API call to start the query, <code>StartQueryWorkloadInsightsTopContributors</code>. Use the scope ID that was returned for your account by <code>CreateScope</code>.</p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_input.GetQueryResultsWorkloadInsightsTopContributorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_output.GetQueryResultsWorkloadInsightsTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_workload_insights_top_contributors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_workload_insights_top_contributors.async_get_query_results_workload_insights_top_contributors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_input.GetQueryResultsWorkloadInsightsTopContributorsInput = {
            "scope_id": scope_id,
            "query_id": query_id,
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

    async def iter_get_query_results_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_networkflowmonitor.types.workload_insights_top_contributors_row.WorkloadInsightsTopContributorsRow]":
        _token = next_token
        while True:
            _response = await self.get_query_results_workload_insights_top_contributors(
                scope_id,
                query_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("top_contributors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_query_results_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_output.GetQueryResultsWorkloadInsightsTopContributorsDataOutput":
        """<p>Return the data for a query with the Network Flow Monitor query interface. Specify the query that you want to return results for by providing a query ID and a scope ID.</p> <p>This query returns the data for top contributors for workload insights for a specific scope. Workload insights provide a high level view of network flow performance data collected by agents for a scope. To return just the top contributors, see <code>GetQueryResultsWorkloadInsightsTopContributors</code>.</p> <p>Create a query ID for this call by calling the corresponding API call to start the query, <code>StartQueryWorkloadInsightsTopContributorsData</code>. Use the scope ID that was returned for your account by <code>CreateScope</code>.</p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p> <p>The top contributor network flows overall are for a specific metric type, for example, the number of retransmissions.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_input.GetQueryResultsWorkloadInsightsTopContributorsDataInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_output.GetQueryResultsWorkloadInsightsTopContributorsDataOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_workload_insights_top_contributors_data

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_workload_insights_top_contributors_data.async_get_query_results_workload_insights_top_contributors_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_input.GetQueryResultsWorkloadInsightsTopContributorsDataInput = {
            "scope_id": scope_id,
            "query_id": query_id,
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

    async def iter_get_query_results_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_networkflowmonitor.types.workload_insights_top_contributors_data_point.WorkloadInsightsTopContributorsDataPoint]":
        _token = next_token
        while True:
            _response = (
                await self.get_query_results_workload_insights_top_contributors_data(
                    scope_id,
                    query_id,
                    config_overrides=config_overrides,
                    next_token=_token,
                    max_results=max_results,
                )
            )
            _page = _resolve_path(_response, ("datapoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_query_status_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_output.GetQueryStatusWorkloadInsightsTopContributorsOutput":
        """<p>Return the data for a query with the Network Flow Monitor query interface. Specify the query that you want to return results for by providing a query ID and a monitor name. This query returns the top contributors for workload insights.</p> <p>When you start a query, use this call to check the status of the query to make sure that it has has <code>SUCCEEDED</code> before you review the results. Use the same query ID that you used for the corresponding API call to start the query, <code>StartQueryWorkloadInsightsTopContributors</code>.</p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_input.GetQueryStatusWorkloadInsightsTopContributorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_output.GetQueryStatusWorkloadInsightsTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_workload_insights_top_contributors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_workload_insights_top_contributors.async_get_query_status_workload_insights_top_contributors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_input.GetQueryStatusWorkloadInsightsTopContributorsInput = {
            "scope_id": scope_id,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_query_status_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_output.GetQueryStatusWorkloadInsightsTopContributorsDataOutput":
        """<p>Returns the current status of a query for the Network Flow Monitor query interface, for a specified query ID and monitor. This call returns the query status for the top contributors data for workload insights.</p> <p>When you start a query, use this call to check the status of the query to make sure that it has has <code>SUCCEEDED</code> before you review the results. Use the same query ID that you used for the corresponding API call to start the query, <code>StartQueryWorkloadInsightsTopContributorsData</code>.</p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p> <p>The top contributor network flows overall are for a specific metric type, for example, the number of retransmissions.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account. A scope ID is returned from a <code>CreateScope</code> API call.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_input.GetQueryStatusWorkloadInsightsTopContributorsDataInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_output.GetQueryStatusWorkloadInsightsTopContributorsDataOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_workload_insights_top_contributors_data

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_workload_insights_top_contributors_data.async_get_query_status_workload_insights_top_contributors_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_input.GetQueryStatusWorkloadInsightsTopContributorsDataInput = {
            "scope_id": scope_id,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_query_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        metric_name: "capo_networkflowmonitor.types.workload_insights_metric.WorkloadInsightsMetric",
        destination_category: "capo_networkflowmonitor.types.destination_category.DestinationCategory",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        limit: Optional["capo_networkflowmonitor.types.limit.Limit"] = None,
    ) -> "capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_output.StartQueryWorkloadInsightsTopContributorsOutput":
        """<p>Create a query with the Network Flow Monitor query interface that you can run to return workload insights top contributors. Specify the scope that you want to create a query for.</p> <p>The call returns a query ID that you can use with <a href="https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributors.html"> GetQueryResultsWorkloadInsightsTopContributors</a> to run the query and return the top contributors for the workload insights for a scope.</p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable APIs for the top contributors that you want to be returned.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account. A scope ID is returned from a <code>CreateScope</code> API call.</p>
            start_time: <p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>
            end_time: <p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>
            metric_name: <p>The metric that you want to query top contributors for. That is, you can specify this metric to return the top contributor network flows, for this type of metric, for a monitor and (optionally) within a specific category, such as network flows between Availability Zones.</p>
            destination_category: <p>The destination category for a top contributors row. Destination categories can be one of the following: </p> <ul> <li> <p> <code>INTRA_AZ</code>: Top contributor network flows within a single Availability Zone</p> </li> <li> <p> <code>INTER_AZ</code>: Top contributor network flows between Availability Zones</p> </li> <li> <p> <code>INTER_REGION</code>: Top contributor network flows between Regions (to the edge of another Region)</p> </li> <li> <p> <code>INTER_VPC</code>: Top contributor network flows between VPCs</p> </li> <li> <p> <code>AWS_SERVICES</code>: Top contributor network flows to or from Amazon Web Services services</p> </li> <li> <p> <code>UNCLASSIFIED</code>: Top contributor network flows that do not have a bucket classification</p> </li> </ul>
            limit: <p>The maximum number of top contributors to return.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_input.StartQueryWorkloadInsightsTopContributorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_output.StartQueryWorkloadInsightsTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.start_query_workload_insights_top_contributors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.start_query_workload_insights_top_contributors.async_start_query_workload_insights_top_contributors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_input.StartQueryWorkloadInsightsTopContributorsInput = {
            "scope_id": scope_id,
            "start_time": start_time,
            "end_time": end_time,
            "metric_name": metric_name,
            "destination_category": destination_category,
        }
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_query_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        metric_name: "capo_networkflowmonitor.types.workload_insights_metric.WorkloadInsightsMetric",
        destination_category: "capo_networkflowmonitor.types.destination_category.DestinationCategory",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_output.StartQueryWorkloadInsightsTopContributorsDataOutput":
        """<p>Create a query with the Network Flow Monitor query interface that you can run to return data for workload insights top contributors. Specify the scope that you want to create a query for.</p> <p>The call returns a query ID that you can use with <a href="https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsWorkloadInsightsTopContributorsData.html"> GetQueryResultsWorkloadInsightsTopContributorsData</a> to run the query and return the data for the top contributors for the workload insights for a scope.</p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>
            start_time: <p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>
            end_time: <p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>
            metric_name: <p>The metric that you want to query top contributors for. That is, you can specify this metric to return the top contributor network flows, for this type of metric, for a monitor and (optionally) within a specific category, such as network flows between Availability Zones.</p>
            destination_category: <p>The destination category for a top contributors. Destination categories can be one of the following: </p> <ul> <li> <p> <code>INTRA_AZ</code>: Top contributor network flows within a single Availability Zone</p> </li> <li> <p> <code>INTER_AZ</code>: Top contributor network flows between Availability Zones</p> </li> <li> <p> <code>INTER_REGION</code>: Top contributor network flows between Regions (to the edge of another Region)</p> </li> <li> <p> <code>INTER_VPC</code>: Top contributor network flows between VPCs</p> </li> <li> <p> <code>AWS_SERVICES</code>: Top contributor network flows to or from Amazon Web Services services</p> </li> <li> <p> <code>UNCLASSIFIED</code>: Top contributor network flows that do not have a bucket classification</p> </li> </ul>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_input.StartQueryWorkloadInsightsTopContributorsDataInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_output.StartQueryWorkloadInsightsTopContributorsDataOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.start_query_workload_insights_top_contributors_data

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.start_query_workload_insights_top_contributors_data.async_start_query_workload_insights_top_contributors_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_input.StartQueryWorkloadInsightsTopContributorsDataInput = {
            "scope_id": scope_id,
            "start_time": start_time,
            "end_time": end_time,
            "metric_name": metric_name,
            "destination_category": destination_category,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_query_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_output.StopQueryWorkloadInsightsTopContributorsOutput":
        """<p>Stop a top contributors query for workload insights. Specify the query that you want to stop by providing a query ID and a scope ID. </p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_input.StopQueryWorkloadInsightsTopContributorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_output.StopQueryWorkloadInsightsTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.stop_query_workload_insights_top_contributors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.stop_query_workload_insights_top_contributors.async_stop_query_workload_insights_top_contributors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_input.StopQueryWorkloadInsightsTopContributorsInput = {
            "scope_id": scope_id,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_query_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_output.StopQueryWorkloadInsightsTopContributorsDataOutput":
        """<p>Stop a top contributors data query for workload insights. Specify the query that you want to stop by providing a query ID and a scope ID. </p> <p>Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.</p>

        Args:
            scope_id: <p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeded a service quota.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_input.StopQueryWorkloadInsightsTopContributorsDataInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_output.StopQueryWorkloadInsightsTopContributorsDataOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.stop_query_workload_insights_top_contributors_data

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.stop_query_workload_insights_top_contributors_data.async_stop_query_workload_insights_top_contributors_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_input.StopQueryWorkloadInsightsTopContributorsDataInput = {
            "scope_id": scope_id,
            "query_id": query_id,
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
