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
    import capo_networkflowmonitor.types.create_scope_input
    import capo_networkflowmonitor.types.create_scope_output
    import capo_networkflowmonitor.types.delete_scope_input
    import capo_networkflowmonitor.types.delete_scope_output
    import capo_networkflowmonitor.types.destination_category
    import capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_input
    import capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_output
    import capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_input
    import capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_output
    import capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_input
    import capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_output
    import capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_input
    import capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_output
    import capo_networkflowmonitor.types.get_scope_input
    import capo_networkflowmonitor.types.get_scope_output
    import capo_networkflowmonitor.types.limit
    import capo_networkflowmonitor.types.list_scopes_input
    import capo_networkflowmonitor.types.list_scopes_output
    import capo_networkflowmonitor.types.max_results
    import capo_networkflowmonitor.types.scope_id
    import capo_networkflowmonitor.types.scope_summary
    import capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_input
    import capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_output
    import capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_input
    import capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_output
    import capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_input
    import capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_output
    import capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_input
    import capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_output
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.target_resource_list
    import capo_networkflowmonitor.types.update_scope_input
    import capo_networkflowmonitor.types.update_scope_output
    import capo_networkflowmonitor.types.uuid_string
    import capo_networkflowmonitor.types.workload_insights_metric
    import capo_networkflowmonitor.types.workload_insights_top_contributors_data_point
    import capo_networkflowmonitor.types.workload_insights_top_contributors_row
    from capo_networkflowmonitor._services.async_network_flow_monitor import (
        AsyncNetworkFlowMonitorClient,
        AsyncNetworkFlowMonitorClientConfig,
    )
    from capo_networkflowmonitor._services.network_flow_monitor import (
        NetworkFlowMonitorClient,
        NetworkFlowMonitorClientConfig,
    )


class ScopeResource:
    def __init__(self, service: NetworkFlowMonitorClient) -> None:
        self._service = service

    def create(
        self,
        targets: "capo_networkflowmonitor.types.target_resource_list.TargetResourceList",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.create_scope_input.CreateScopeInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.create_scope_output.CreateScopeOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.create_scope

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.create_scope.create_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.create_scope_input.CreateScopeInput = {
            "targets": targets
        }
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
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_scope_input.GetScopeInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_scope_output.GetScopeOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_scope

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_scope.get_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_scope_input.GetScopeInput = {
            "scope_id": scope_id
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
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.update_scope_input.UpdateScopeInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.update_scope_output.UpdateScopeOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.update_scope

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.update_scope.update_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.update_scope_input.UpdateScopeInput = {
            "scope_id": scope_id
        }
        if resources_to_add is not None:
            input_["resources_to_add"] = resources_to_add
        if resources_to_delete is not None:
            input_["resources_to_delete"] = resources_to_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.delete_scope_input.DeleteScopeInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.delete_scope_output.DeleteScopeOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.delete_scope

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.delete_scope.delete_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.delete_scope_input.DeleteScopeInput = {
            "scope_id": scope_id
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.list_scopes_input.ListScopesInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.list_scopes_output.ListScopesOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.list_scopes

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.list_scopes.list_scopes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.list_scopes_input.ListScopesInput = {}
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

    def get_query_results_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_input.GetQueryResultsWorkloadInsightsTopContributorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_output.GetQueryResultsWorkloadInsightsTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_workload_insights_top_contributors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_workload_insights_top_contributors.get_query_results_workload_insights_top_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_input.GetQueryResultsWorkloadInsightsTopContributorsInput = {
            "scope_id": scope_id,
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

    def get_query_results_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_input.GetQueryResultsWorkloadInsightsTopContributorsDataInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_output.GetQueryResultsWorkloadInsightsTopContributorsDataOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_workload_insights_top_contributors_data

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_query_results_workload_insights_top_contributors_data.get_query_results_workload_insights_top_contributors_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_results_workload_insights_top_contributors_data_input.GetQueryResultsWorkloadInsightsTopContributorsDataInput = {
            "scope_id": scope_id,
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

    def get_query_status_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_input.GetQueryStatusWorkloadInsightsTopContributorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_output.GetQueryStatusWorkloadInsightsTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_workload_insights_top_contributors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_workload_insights_top_contributors.get_query_status_workload_insights_top_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_input.GetQueryStatusWorkloadInsightsTopContributorsInput = {
            "scope_id": scope_id,
            "query_id": query_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_status_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_input.GetQueryStatusWorkloadInsightsTopContributorsDataInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_output.GetQueryStatusWorkloadInsightsTopContributorsDataOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_workload_insights_top_contributors_data

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.get_query_status_workload_insights_top_contributors_data.get_query_status_workload_insights_top_contributors_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.get_query_status_workload_insights_top_contributors_data_input.GetQueryStatusWorkloadInsightsTopContributorsDataInput = {
            "scope_id": scope_id,
            "query_id": query_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_query_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        metric_name: "capo_networkflowmonitor.types.workload_insights_metric.WorkloadInsightsMetric",
        destination_category: "capo_networkflowmonitor.types.destination_category.DestinationCategory",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_input.StartQueryWorkloadInsightsTopContributorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_output.StartQueryWorkloadInsightsTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.start_query_workload_insights_top_contributors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.start_query_workload_insights_top_contributors.start_query_workload_insights_top_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_input.StartQueryWorkloadInsightsTopContributorsInput = {
            "scope_id": scope_id,
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

    def start_query_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        metric_name: "capo_networkflowmonitor.types.workload_insights_metric.WorkloadInsightsMetric",
        destination_category: "capo_networkflowmonitor.types.destination_category.DestinationCategory",
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_input.StartQueryWorkloadInsightsTopContributorsDataInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_output.StartQueryWorkloadInsightsTopContributorsDataOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.start_query_workload_insights_top_contributors_data

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.start_query_workload_insights_top_contributors_data.start_query_workload_insights_top_contributors_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.start_query_workload_insights_top_contributors_data_input.StartQueryWorkloadInsightsTopContributorsDataInput = {
            "scope_id": scope_id,
            "start_time": start_time,
            "end_time": end_time,
            "metric_name": metric_name,
            "destination_category": destination_category,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_query_workload_insights_top_contributors(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_input.StopQueryWorkloadInsightsTopContributorsInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_output.StopQueryWorkloadInsightsTopContributorsOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.stop_query_workload_insights_top_contributors

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.stop_query_workload_insights_top_contributors.stop_query_workload_insights_top_contributors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_input.StopQueryWorkloadInsightsTopContributorsInput = {
            "scope_id": scope_id,
            "query_id": query_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_query_workload_insights_top_contributors_data(
        self,
        scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId",
        query_id: str,
        *,
        config_overrides: Optional[NetworkFlowMonitorClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_input.StopQueryWorkloadInsightsTopContributorsDataInput]",
        ) -> OperationResponse[
            "capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_output.StopQueryWorkloadInsightsTopContributorsDataOutput"
        ]:
            import capo_networkflowmonitor._operations.network_flow_monitor.stop_query_workload_insights_top_contributors_data

            output, http_response = (
                capo_networkflowmonitor._operations.network_flow_monitor.stop_query_workload_insights_top_contributors_data.stop_query_workload_insights_top_contributors_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_networkflowmonitor.types.stop_query_workload_insights_top_contributors_data_input.StopQueryWorkloadInsightsTopContributorsDataInput = {
            "scope_id": scope_id,
            "query_id": query_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncScopeResource:
    def __init__(self, service: AsyncNetworkFlowMonitorClient) -> None:
        self._service = service

    async def create(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def update(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
