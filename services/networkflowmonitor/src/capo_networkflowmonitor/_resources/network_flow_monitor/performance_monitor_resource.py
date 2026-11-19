from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Optional

import capo_networkflowmonitor._auth._signers
import capo_networkflowmonitor._auth._sigv4
from capo_networkflowmonitor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.arn
    import capo_networkflowmonitor.types.create_performance_monitor_input
    import capo_networkflowmonitor.types.create_performance_monitor_output
    import capo_networkflowmonitor.types.delete_performance_monitor_input
    import capo_networkflowmonitor.types.delete_performance_monitor_output
    import capo_networkflowmonitor.types.filter_parameters
    import capo_networkflowmonitor.types.get_performance_monitor_input
    import capo_networkflowmonitor.types.get_performance_monitor_output
    import capo_networkflowmonitor.types.get_query_results_performance_monitor_input
    import capo_networkflowmonitor.types.get_query_results_performance_monitor_output
    import capo_networkflowmonitor.types.get_query_status_performance_monitor_input
    import capo_networkflowmonitor.types.get_query_status_performance_monitor_output
    import capo_networkflowmonitor.types.list_performance_monitors_input
    import capo_networkflowmonitor.types.list_performance_monitors_output
    import capo_networkflowmonitor.types.max_results
    import capo_networkflowmonitor.types.monitor_status
    import capo_networkflowmonitor.types.performance_monitor_query_type
    import capo_networkflowmonitor.types.performance_monitor_summary
    import capo_networkflowmonitor.types.performance_monitor_targets
    import capo_networkflowmonitor.types.performance_monitor_type
    import capo_networkflowmonitor.types.query_limit
    import capo_networkflowmonitor.types.query_max_results
    import capo_networkflowmonitor.types.query_row
    import capo_networkflowmonitor.types.resource_name
    import capo_networkflowmonitor.types.start_query_performance_monitor_input
    import capo_networkflowmonitor.types.start_query_performance_monitor_output
    import capo_networkflowmonitor.types.stop_query_performance_monitor_input
    import capo_networkflowmonitor.types.stop_query_performance_monitor_output
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.update_performance_monitor_input
    import capo_networkflowmonitor.types.update_performance_monitor_output
    import capo_networkflowmonitor.types.uuid_string
    from capo_networkflowmonitor._services.async_network_flow_monitor import (
        AsyncNetworkFlowMonitorClient,
        AsyncNetworkFlowMonitorClientConfig,
    )
    from capo_networkflowmonitor._services.network_flow_monitor import (
        NetworkFlowMonitorClient,
        NetworkFlowMonitorClientConfig,
    )


class PerformanceMonitorResource:
    def __init__(self, service: NetworkFlowMonitorClient) -> None:
        self._service = service

    def put(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        targets: "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
        scope_arn: Optional["capo_networkflowmonitor.types.arn.Arn"] = None,
        client_token: Optional[
            "capo_networkflowmonitor.types.uuid_string.UuidString"
        ] = None,
        tags: Optional["capo_networkflowmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkflowmonitor.types.create_performance_monitor_output.CreatePerformanceMonitorOutput":
        """<p>Create a performance monitor to monitor the traffic of the Amazon Virtual Private Clouds (VPCs) that you specify as targets, to determine whether the Amazon Web Services network is causing issues for your workloads. With a performance monitor, you can identify network degradation across paths between Availability Zones and across Amazon Web Services Regions.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            scope_arn: <p>The Amazon Resource Name (ARN) of the scope for the performance monitor.</p>
            targets: <p>The resources to monitor. Each target identifies a resource, currently a VPC, for which you can track network performance. For a VPC, specify the VPC ARN.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. If the token matches a previous request, the service ignores the request without returning an error. Don't reuse the same client token for other API requests.</p>
            tags: <p>The tags for a performance monitor. You can add a maximum of 200 tags.</p>

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
            req: "OperationRequest[capo_networkflowmonitor.types.create_performance_monitor_input.CreatePerformanceMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.create_performance_monitor_output.CreatePerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.create_performance_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.create_performance_monitor.create_performance_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreatePerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.create_performance_monitor_input.CreatePerformanceMonitorInput = {
            "monitor_name": monitor_name,
            "targets": targets,
        }
        if scope_arn is not None:
            input_["scope_arn"] = scope_arn
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
    ) -> "capo_networkflowmonitor.types.get_performance_monitor_output.GetPerformanceMonitorOutput":
        """<p>Returns information about a performance monitor, including the resources that it monitors, its status, and the tags for the monitor.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_performance_monitor_input.GetPerformanceMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_performance_monitor_output.GetPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_performance_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_performance_monitor.get_performance_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.get_performance_monitor_input.GetPerformanceMonitorInput = {
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
        targets_to_add: Optional[
            "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
        ] = None,
        targets_to_remove: Optional[
            "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
        ] = None,
        client_token: Optional[
            "capo_networkflowmonitor.types.uuid_string.UuidString"
        ] = None,
    ) -> "capo_networkflowmonitor.types.update_performance_monitor_output.UpdatePerformanceMonitorOutput":
        """<p>Update a performance monitor, to add or remove the resources that the monitor tracks network performance for.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            targets_to_add: <p>The resources to add to the performance monitor.</p>
            targets_to_remove: <p>The resources to remove from the performance monitor.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. If the token matches a previous request, the service ignores the request without returning an error. Don't reuse the same client token for other API requests.</p>

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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.update_performance_monitor_input.UpdatePerformanceMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.update_performance_monitor_output.UpdatePerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.update_performance_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.update_performance_monitor.update_performance_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdatePerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.update_performance_monitor_input.UpdatePerformanceMonitorInput = {
            "monitor_name": monitor_name
        }
        if targets_to_add is not None:
            input_["targets_to_add"] = targets_to_add
        if targets_to_remove is not None:
            input_["targets_to_remove"] = targets_to_remove
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
    ) -> "capo_networkflowmonitor.types.delete_performance_monitor_output.DeletePerformanceMonitorOutput":
        """<p>Delete a performance monitor. Network Flow Monitor stops tracking network performance for the resources that the monitor included.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>

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
            req: "OperationRequest[capo_networkflowmonitor.types.delete_performance_monitor_input.DeletePerformanceMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.delete_performance_monitor_output.DeletePerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.delete_performance_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.delete_performance_monitor.delete_performance_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.delete_performance_monitor_input.DeletePerformanceMonitorInput = {
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
        monitor_type: Optional[
            "capo_networkflowmonitor.types.performance_monitor_type.PerformanceMonitorType"
        ] = None,
    ) -> "capo_networkflowmonitor.types.list_performance_monitors_output.ListPerformanceMonitorsOutput":
        """<p>Returns a list of the performance monitors in an account. You can optionally return only the monitors that have a specific status or type.</p> <p>Results are paginated. Use the <code>nextToken</code> parameter to return additional results.</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of performance monitors that you want to return with this call. If you don't specify a value, the default is 25.</p>
            monitor_status: <p>The status of the performance monitors that you want to return. If you don't specify a status, Network Flow Monitor returns performance monitors with any status.</p>
            monitor_type: <p>The type of the performance monitors that you want to return. If you don't specify a type, Network Flow Monitor returns performance monitors of any type.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.list_performance_monitors_input.ListPerformanceMonitorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.list_performance_monitors_output.ListPerformanceMonitorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.list_performance_monitors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.list_performance_monitors.list_performance_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPerformanceMonitors")
        )
        input_: capo_networkflowmonitor.types.list_performance_monitors_input.ListPerformanceMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if monitor_status is not None:
            input_["monitor_status"] = monitor_status
        if monitor_type is not None:
            input_["monitor_type"] = monitor_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_results_performance_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_networkflowmonitor.types.query_max_results.QueryMaxResults"
        ] = None,
    ) -> "capo_networkflowmonitor.types.get_query_results_performance_monitor_output.GetQueryResultsPerformanceMonitorOutput":
        """<p>Returns the results of a query for the Network Flow Monitor query interface, for a specified query ID and performance monitor. This call returns the top paths for a performance monitor.</p> <p>Create a query with <a href="https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryPerformanceMonitor.html"> StartQueryPerformanceMonitor</a>, and then use the query ID with this call to return the results.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>
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
            req: "OperationRequest[capo_networkflowmonitor.types.get_query_results_performance_monitor_input.GetQueryResultsPerformanceMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_query_results_performance_monitor_output.GetQueryResultsPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_performance_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_performance_monitor.get_query_results_performance_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQueryResultsPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.get_query_results_performance_monitor_input.GetQueryResultsPerformanceMonitorInput = {
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

    def get_query_status_performance_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.get_query_status_performance_monitor_output.GetQueryStatusPerformanceMonitorOutput":
        """<p>Returns the current status of a query for the Network Flow Monitor query interface, for a specified query ID and performance monitor. This call returns the query status for the top paths for a performance monitor.</p> <p>When you run a query, use this call to check the status of the query to make sure that the query has <code>SUCCEEDED</code> before you review the results. Use the same query ID that you used for the corresponding API call to start (create) the query, <code>StartQueryPerformanceMonitor</code>.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>

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
            req: "OperationRequest[capo_networkflowmonitor.types.get_query_status_performance_monitor_input.GetQueryStatusPerformanceMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_query_status_performance_monitor_output.GetQueryStatusPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_performance_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_performance_monitor.get_query_status_performance_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQueryStatusPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.get_query_status_performance_monitor_input.GetQueryStatusPerformanceMonitorInput = {
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

    def start_query_performance_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        query_type: "capo_networkflowmonitor.types.performance_monitor_query_type.PerformanceMonitorQueryType",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
        filter_parameters: Optional[
            "capo_networkflowmonitor.types.filter_parameters.FilterParameters"
        ] = None,
        limit: Optional["capo_networkflowmonitor.types.query_limit.QueryLimit"] = None,
    ) -> "capo_networkflowmonitor.types.start_query_performance_monitor_output.StartQueryPerformanceMonitorOutput":
        """<p>Create a query that you can use with the Network Flow Monitor query interface to return the top paths for a performance monitor. Specify the performance monitor that you want to create the query for.</p> <p>The call returns a query ID that you can use with <a href="https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsPerformanceMonitor.html"> GetQueryResultsPerformanceMonitor</a> to return the results of the query.</p> <p>Top paths in Network Flow Monitor are the network paths used by the traffic for the resources that a performance monitor tracks, ranked by impact score and then by traffic volume. Each path includes the traffic and round-trip time for the path, together with a breakdown of the subnet pairs that the path includes.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            start_time: <p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>
            end_time: <p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>
            query_type: <p>The type of query that you want to create. Specify <code>TOP_PATHS</code> to return the top paths for the performance monitor.</p>
            filter_parameters: <p>The filters for the query, to return a subset of the top paths. For a <code>TOP_PATHS</code> query, you can filter on the following fields:</p> <ul> <li> <p> <code>local_az_id</code>: The Availability Zone ID of the local end of a path</p> </li> <li> <p> <code>remote_az_id</code>: The Availability Zone ID of the remote end of a path</p> </li> <li> <p> <code>impact_level</code>: The impact level of a path</p> </li> </ul> <p>When you filter on <code>impact_level</code>, Network Flow Monitor compares the filter with the most severe impact level for the path over the time period of the query, and the traffic and round-trip time that Network Flow Monitor returns for each path still cover the full time period. Paths that have no impact data don't match an <code>impact_level</code> filter, including a <code>NOT_EQUALS</code> filter. Network Flow Monitor doesn't filter the subnet pairs within a path by impact level.</p>
            limit: <p>The maximum number of top paths that you want the query to return.</p>

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
            req: "OperationRequest[capo_networkflowmonitor.types.start_query_performance_monitor_input.StartQueryPerformanceMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.start_query_performance_monitor_output.StartQueryPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.start_query_performance_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.start_query_performance_monitor.start_query_performance_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartQueryPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.start_query_performance_monitor_input.StartQueryPerformanceMonitorInput = {
            "monitor_name": monitor_name,
            "start_time": start_time,
            "end_time": end_time,
            "query_type": query_type,
        }
        if filter_parameters is not None:
            input_["filter_parameters"] = filter_parameters
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_query_performance_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.stop_query_performance_monitor_output.StopQueryPerformanceMonitorOutput":
        """<p>Stop a query for the Network Flow Monitor query interface, for a specified query ID and performance monitor. Use the same query ID that you used for the corresponding API call to start the query, <code>StartQueryPerformanceMonitor</code>.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>

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
            req: "OperationRequest[capo_networkflowmonitor.types.stop_query_performance_monitor_input.StopQueryPerformanceMonitorInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.stop_query_performance_monitor_output.StopQueryPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.stop_query_performance_monitor

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.stop_query_performance_monitor.stop_query_performance_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopQueryPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.stop_query_performance_monitor_input.StopQueryPerformanceMonitorInput = {
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


class AsyncPerformanceMonitorResource:
    def __init__(self, service: AsyncNetworkFlowMonitorClient) -> None:
        self._service = service

    async def put(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        targets: "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        scope_arn: Optional["capo_networkflowmonitor.types.arn.Arn"] = None,
        client_token: Optional[
            "capo_networkflowmonitor.types.uuid_string.UuidString"
        ] = None,
        tags: Optional["capo_networkflowmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkflowmonitor.types.create_performance_monitor_output.CreatePerformanceMonitorOutput":
        """<p>Create a performance monitor to monitor the traffic of the Amazon Virtual Private Clouds (VPCs) that you specify as targets, to determine whether the Amazon Web Services network is causing issues for your workloads. With a performance monitor, you can identify network degradation across paths between Availability Zones and across Amazon Web Services Regions.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            scope_arn: <p>The Amazon Resource Name (ARN) of the scope for the performance monitor.</p>
            targets: <p>The resources to monitor. Each target identifies a resource, currently a VPC, for which you can track network performance. For a VPC, specify the VPC ARN.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. If the token matches a previous request, the service ignores the request without returning an error. Don't reuse the same client token for other API requests.</p>
            tags: <p>The tags for a performance monitor. You can add a maximum of 200 tags.</p>

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
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.create_performance_monitor_input.CreatePerformanceMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.create_performance_monitor_output.CreatePerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.create_performance_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.create_performance_monitor.async_create_performance_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreatePerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.create_performance_monitor_input.CreatePerformanceMonitorInput = {
            "monitor_name": monitor_name,
            "targets": targets,
        }
        if scope_arn is not None:
            input_["scope_arn"] = scope_arn
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
    ) -> "capo_networkflowmonitor.types.get_performance_monitor_output.GetPerformanceMonitorOutput":
        """<p>Returns information about a performance monitor, including the resources that it monitors, its status, and the tags for the monitor.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_performance_monitor_input.GetPerformanceMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_performance_monitor_output.GetPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_performance_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_performance_monitor.async_get_performance_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.get_performance_monitor_input.GetPerformanceMonitorInput = {
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
        targets_to_add: Optional[
            "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
        ] = None,
        targets_to_remove: Optional[
            "capo_networkflowmonitor.types.performance_monitor_targets.PerformanceMonitorTargets"
        ] = None,
        client_token: Optional[
            "capo_networkflowmonitor.types.uuid_string.UuidString"
        ] = None,
    ) -> "capo_networkflowmonitor.types.update_performance_monitor_output.UpdatePerformanceMonitorOutput":
        """<p>Update a performance monitor, to add or remove the resources that the monitor tracks network performance for.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            targets_to_add: <p>The resources to add to the performance monitor.</p>
            targets_to_remove: <p>The resources to remove from the performance monitor.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. If the token matches a previous request, the service ignores the request without returning an error. Don't reuse the same client token for other API requests.</p>

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
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.update_performance_monitor_input.UpdatePerformanceMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.update_performance_monitor_output.UpdatePerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.update_performance_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.update_performance_monitor.async_update_performance_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdatePerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.update_performance_monitor_input.UpdatePerformanceMonitorInput = {
            "monitor_name": monitor_name
        }
        if targets_to_add is not None:
            input_["targets_to_add"] = targets_to_add
        if targets_to_remove is not None:
            input_["targets_to_remove"] = targets_to_remove
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
    ) -> "capo_networkflowmonitor.types.delete_performance_monitor_output.DeletePerformanceMonitorOutput":
        """<p>Delete a performance monitor. Network Flow Monitor stops tracking network performance for the resources that the monitor included.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>

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
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.delete_performance_monitor_input.DeletePerformanceMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.delete_performance_monitor_output.DeletePerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.delete_performance_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.delete_performance_monitor.async_delete_performance_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.delete_performance_monitor_input.DeletePerformanceMonitorInput = {
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
        monitor_type: Optional[
            "capo_networkflowmonitor.types.performance_monitor_type.PerformanceMonitorType"
        ] = None,
    ) -> "capo_networkflowmonitor.types.list_performance_monitors_output.ListPerformanceMonitorsOutput":
        """<p>Returns a list of the performance monitors in an account. You can optionally return only the monitors that have a specific status or type.</p> <p>Results are paginated. Use the <code>nextToken</code> parameter to return additional results.</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of performance monitors that you want to return with this call. If you don't specify a value, the default is 25.</p>
            monitor_status: <p>The status of the performance monitors that you want to return. If you don't specify a status, Network Flow Monitor returns performance monitors with any status.</p>
            monitor_type: <p>The type of the performance monitors that you want to return. If you don't specify a type, Network Flow Monitor returns performance monitors of any type.</p>

        Raises:
            capo_networkflowmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_networkflowmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_networkflowmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_networkflowmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_networkflowmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.list_performance_monitors_input.ListPerformanceMonitorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.list_performance_monitors_output.ListPerformanceMonitorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.list_performance_monitors

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.list_performance_monitors.async_list_performance_monitors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPerformanceMonitors")
        )
        input_: capo_networkflowmonitor.types.list_performance_monitors_input.ListPerformanceMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if monitor_status is not None:
            input_["monitor_status"] = monitor_status
        if monitor_type is not None:
            input_["monitor_type"] = monitor_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_query_results_performance_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_networkflowmonitor.types.query_max_results.QueryMaxResults"
        ] = None,
    ) -> "capo_networkflowmonitor.types.get_query_results_performance_monitor_output.GetQueryResultsPerformanceMonitorOutput":
        """<p>Returns the results of a query for the Network Flow Monitor query interface, for a specified query ID and performance monitor. This call returns the top paths for a performance monitor.</p> <p>Create a query with <a href="https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StartQueryPerformanceMonitor.html"> StartQueryPerformanceMonitor</a>, and then use the query ID with this call to return the results.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>
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
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_query_results_performance_monitor_input.GetQueryResultsPerformanceMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_query_results_performance_monitor_output.GetQueryResultsPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_performance_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_performance_monitor.async_get_query_results_performance_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQueryResultsPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.get_query_results_performance_monitor_input.GetQueryResultsPerformanceMonitorInput = {
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

    async def get_query_status_performance_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.get_query_status_performance_monitor_output.GetQueryStatusPerformanceMonitorOutput":
        """<p>Returns the current status of a query for the Network Flow Monitor query interface, for a specified query ID and performance monitor. This call returns the query status for the top paths for a performance monitor.</p> <p>When you run a query, use this call to check the status of the query to make sure that the query has <code>SUCCEEDED</code> before you review the results. Use the same query ID that you used for the corresponding API call to start (create) the query, <code>StartQueryPerformanceMonitor</code>.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>

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
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.get_query_status_performance_monitor_input.GetQueryStatusPerformanceMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.get_query_status_performance_monitor_output.GetQueryStatusPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_performance_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_performance_monitor.async_get_query_status_performance_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetQueryStatusPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.get_query_status_performance_monitor_input.GetQueryStatusPerformanceMonitorInput = {
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

    async def start_query_performance_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        query_type: "capo_networkflowmonitor.types.performance_monitor_query_type.PerformanceMonitorQueryType",
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
        filter_parameters: Optional[
            "capo_networkflowmonitor.types.filter_parameters.FilterParameters"
        ] = None,
        limit: Optional["capo_networkflowmonitor.types.query_limit.QueryLimit"] = None,
    ) -> "capo_networkflowmonitor.types.start_query_performance_monitor_output.StartQueryPerformanceMonitorOutput":
        """<p>Create a query that you can use with the Network Flow Monitor query interface to return the top paths for a performance monitor. Specify the performance monitor that you want to create the query for.</p> <p>The call returns a query ID that you can use with <a href="https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_GetQueryResultsPerformanceMonitor.html"> GetQueryResultsPerformanceMonitor</a> to return the results of the query.</p> <p>Top paths in Network Flow Monitor are the network paths used by the traffic for the resources that a performance monitor tracks, ranked by impact score and then by traffic volume. Each path includes the traffic and round-trip time for the path, together with a breakdown of the subnet pairs that the path includes.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            start_time: <p>The timestamp that is the date and time that is the beginning of the period that you want to retrieve results for with your query.</p>
            end_time: <p>The timestamp that is the date and time end of the period that you want to retrieve results for with your query.</p>
            query_type: <p>The type of query that you want to create. Specify <code>TOP_PATHS</code> to return the top paths for the performance monitor.</p>
            filter_parameters: <p>The filters for the query, to return a subset of the top paths. For a <code>TOP_PATHS</code> query, you can filter on the following fields:</p> <ul> <li> <p> <code>local_az_id</code>: The Availability Zone ID of the local end of a path</p> </li> <li> <p> <code>remote_az_id</code>: The Availability Zone ID of the remote end of a path</p> </li> <li> <p> <code>impact_level</code>: The impact level of a path</p> </li> </ul> <p>When you filter on <code>impact_level</code>, Network Flow Monitor compares the filter with the most severe impact level for the path over the time period of the query, and the traffic and round-trip time that Network Flow Monitor returns for each path still cover the full time period. Paths that have no impact data don't match an <code>impact_level</code> filter, including a <code>NOT_EQUALS</code> filter. Network Flow Monitor doesn't filter the subnet pairs within a path by impact level.</p>
            limit: <p>The maximum number of top paths that you want the query to return.</p>

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
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.start_query_performance_monitor_input.StartQueryPerformanceMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.start_query_performance_monitor_output.StartQueryPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.start_query_performance_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.start_query_performance_monitor.async_start_query_performance_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartQueryPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.start_query_performance_monitor_input.StartQueryPerformanceMonitorInput = {
            "monitor_name": monitor_name,
            "start_time": start_time,
            "end_time": end_time,
            "query_type": query_type,
        }
        if filter_parameters is not None:
            input_["filter_parameters"] = filter_parameters
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_query_performance_monitor(
        self,
        monitor_name: "capo_networkflowmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncNetworkFlowMonitorClientConfig] = None,
    ) -> "capo_networkflowmonitor.types.stop_query_performance_monitor_output.StopQueryPerformanceMonitorOutput":
        """<p>Stop a query for the Network Flow Monitor query interface, for a specified query ID and performance monitor. Use the same query ID that you used for the corresponding API call to start the query, <code>StartQueryPerformanceMonitor</code>.</p>

        Args:
            monitor_name: <p>The name of the performance monitor.</p>
            query_id: <p>The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to start a query.</p>

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
            req: "AsyncOperationRequest[capo_networkflowmonitor.types.stop_query_performance_monitor_input.StopQueryPerformanceMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkflowmonitor.types.stop_query_performance_monitor_output.StopQueryPerformanceMonitorOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.stop_query_performance_monitor

            (
                output,
                http_response,
            ) = await capo_networkflowmonitor._operations.network_flow_monitor.stop_query_performance_monitor.async_stop_query_performance_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopQueryPerformanceMonitor")
        )
        input_: capo_networkflowmonitor.types.stop_query_performance_monitor_input.StopQueryPerformanceMonitorInput = {
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
