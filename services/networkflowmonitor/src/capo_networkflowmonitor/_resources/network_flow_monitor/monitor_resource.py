from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Optional

import capo_networkflowmonitor._auth._signers
import capo_networkflowmonitor._auth._sigv4
from capo_networkflowmonitor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.arn
    import capo_networkflowmonitor.types.create_monitor_input
    import capo_networkflowmonitor.types.create_monitor_output
    import capo_networkflowmonitor.types.delete_monitor_input
    import capo_networkflowmonitor.types.delete_monitor_output
    import capo_networkflowmonitor.types.destination_category
    import capo_networkflowmonitor.types.get_monitor_input
    import capo_networkflowmonitor.types.get_monitor_output
    import capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_input
    import capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_output
    import capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_input
    import capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_output
    import capo_networkflowmonitor.types.limit
    import capo_networkflowmonitor.types.list_monitors_input
    import capo_networkflowmonitor.types.list_monitors_output
    import capo_networkflowmonitor.types.max_results
    import capo_networkflowmonitor.types.monitor_local_resources
    import capo_networkflowmonitor.types.monitor_metric
    import capo_networkflowmonitor.types.monitor_remote_resources
    import capo_networkflowmonitor.types.monitor_status
    import capo_networkflowmonitor.types.monitor_summary
    import capo_networkflowmonitor.types.monitor_top_contributors_row
    import capo_networkflowmonitor.types.resource_name
    import capo_networkflowmonitor.types.start_query_monitor_top_contributors_input
    import capo_networkflowmonitor.types.start_query_monitor_top_contributors_output
    import capo_networkflowmonitor.types.stop_query_monitor_top_contributors_input
    import capo_networkflowmonitor.types.stop_query_monitor_top_contributors_output
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.update_monitor_input
    import capo_networkflowmonitor.types.update_monitor_output
    import capo_networkflowmonitor.types.uuid_string
    from capo_networkflowmonitor._services.async_network_flow_monitor import (
        AsyncNetworkFlowMonitorClient,
        AsyncNetworkFlowMonitorClientConfig,
    )
    from capo_networkflowmonitor._services.network_flow_monitor import (
        NetworkFlowMonitorClient,
        NetworkFlowMonitorClientConfig,
    )


class MonitorResource:
    def __init__(self, service: NetworkFlowMonitorClient) -> None:
        self._service = service

    def put(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        local_resources: "capo_networkflowmonitor.types.monitor_local_resources.MonitorLocalResources",
        scope_arn: "capo_networkflowmonitor.types.arn.Arn",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.create_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.create_monitor.create_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_monitor.get_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_monitor_input.GetMonitorInput = {
            "monitor_name": monitor_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.update_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.update_monitor.update_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.delete_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.delete_monitor.delete_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.delete_monitor_input.DeleteMonitorInput = {
            "monitor_name": monitor_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.list_monitors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.list_monitors.list_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.list_monitors_input.ListMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if monitor_status is not None:
            input_["monitor_status"] = monitor_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_results_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_input.GetQueryResultsMonitorTopContributorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_output.GetQueryResultsMonitorTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_monitor_top_contributors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_monitor_top_contributors.get_query_results_monitor_top_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_results_monitor_top_contributors_input.GetQueryResultsMonitorTopContributorsInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_status_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_input.GetQueryStatusMonitorTopContributorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_output.GetQueryStatusMonitorTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_monitor_top_contributors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_monitor_top_contributors.get_query_status_monitor_top_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_status_monitor_top_contributors_input.GetQueryStatusMonitorTopContributorsInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_query_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        metric_name: "capo_networkflowmonitor.types.monitor_metric.MonitorMetric",
        destination_category: "capo_networkflowmonitor.types.destination_category.DestinationCategory",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.start_query_monitor_top_contributors_input.StartQueryMonitorTopContributorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.start_query_monitor_top_contributors_output.StartQueryMonitorTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.start_query_monitor_top_contributors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.start_query_monitor_top_contributors.start_query_monitor_top_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.start_query_monitor_top_contributors_input.StartQueryMonitorTopContributorsInput = {
            "monitor_name": monitor_name,
            "start_time": start_time,
            "end_time": end_time,
            "metric_name": metric_name,
            "destination_category": destination_category,
        }
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_query_monitor_top_contributors(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.stop_query_monitor_top_contributors_input.StopQueryMonitorTopContributorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.stop_query_monitor_top_contributors_output.StopQueryMonitorTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.stop_query_monitor_top_contributors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.stop_query_monitor_top_contributors.stop_query_monitor_top_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.stop_query_monitor_top_contributors_input.StopQueryMonitorTopContributorsInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMonitorResource:
    def __init__(self, service: AsyncNetworkFlowMonitorClient) -> None:
        self._service = service

    async def put(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def update(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
