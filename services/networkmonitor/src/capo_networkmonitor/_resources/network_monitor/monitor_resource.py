from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_networkmonitor._auth._signers
import capo_networkmonitor._auth._sigv4
from capo_networkmonitor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_networkmonitor.types.aggregation_period
    import capo_networkmonitor.types.create_monitor_input
    import capo_networkmonitor.types.create_monitor_output
    import capo_networkmonitor.types.create_monitor_probe_input_list
    import capo_networkmonitor.types.delete_monitor_input
    import capo_networkmonitor.types.delete_monitor_output
    import capo_networkmonitor.types.get_monitor_input
    import capo_networkmonitor.types.get_monitor_output
    import capo_networkmonitor.types.list_monitors_input
    import capo_networkmonitor.types.list_monitors_output
    import capo_networkmonitor.types.max_results
    import capo_networkmonitor.types.monitor_summary
    import capo_networkmonitor.types.pagination_token
    import capo_networkmonitor.types.resource_name
    import capo_networkmonitor.types.tag_map
    import capo_networkmonitor.types.update_monitor_input
    import capo_networkmonitor.types.update_monitor_output
    from capo_networkmonitor._services.async_network_monitor import (
        AsyncNetworkMonitorClient,
        AsyncNetworkMonitorClientConfig,
    )
    from capo_networkmonitor._services.network_monitor import (
        NetworkMonitorClient,
        NetworkMonitorClientConfig,
    )


class MonitorResource:
    def __init__(self, service: NetworkMonitorClient) -> None:
        self._service = service

    def put(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        probes: Optional[
            "capo_networkmonitor.types.create_monitor_probe_input_list.CreateMonitorProbeInputList"
        ] = None,
        aggregation_period: Optional[
            "capo_networkmonitor.types.aggregation_period.AggregationPeriod"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkmonitor.types.create_monitor_output.CreateMonitorOutput":
        """<p>Creates a monitor between a source subnet and destination IP address. Within a monitor you'll create one or more probes that monitor network traffic between your source Amazon Web Services VPC subnets and your destination IP addresses. Each probe then aggregates and sends metrics to Amazon CloudWatch.</p> <p>You can also create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>source</code>—The subnet IDs where the probes will be created.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name identifying the monitor. It can contain only letters, underscores (_), or dashes (-), and can be up to 200 characters.</p>
            probes: <p>Displays a list of all of the probes created for a monitor.</p>
            aggregation_period: <p>The time, in seconds, that metrics are aggregated and sent to Amazon CloudWatch. Valid values are either <code>30</code> or <code>60</code>. <code>60</code> is the default if no period is chosen.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the monitor.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.create_monitor

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.create_monitor.create_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateMonitor")
        )
        input_: capo_networkmonitor.types.create_monitor_input.CreateMonitorInput = {
            "monitor_name": monitor_name
        }
        if probes is not None:
            input_["probes"] = probes
        if aggregation_period is not None:
            input_["aggregation_period"] = aggregation_period
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
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.get_monitor_output.GetMonitorOutput":
        """<p>Returns details about a specific monitor. </p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor that details are returned for.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.get_monitor

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.get_monitor.get_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMonitor")
        )
        input_: capo_networkmonitor.types.get_monitor_input.GetMonitorInput = {
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
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        aggregation_period: "capo_networkmonitor.types.aggregation_period.AggregationPeriod",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.update_monitor_output.UpdateMonitorOutput":
        """<p>Updates the <code>aggregationPeriod</code> for a monitor. Monitors support an <code>aggregationPeriod</code> of either <code>30</code> or <code>60</code> seconds. This action requires the <code>monitorName</code> and <code>probeId</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to update. </p>
            aggregation_period: <p>The aggregation time, in seconds, to change to. This must be either <code>30</code> or <code>60</code>. </p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.update_monitor

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.update_monitor.update_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMonitor")
        )
        input_: capo_networkmonitor.types.update_monitor_input.UpdateMonitorInput = {
            "monitor_name": monitor_name,
            "aggregation_period": aggregation_period,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput":
        """<p>Deletes a specified monitor.</p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.delete_monitor

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.delete_monitor.delete_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMonitor")
        )
        input_: capo_networkmonitor.types.delete_monitor_input.DeleteMonitorInput = {
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
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        next_token: Optional[
            "capo_networkmonitor.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_networkmonitor.types.max_results.MaxResults"
        ] = None,
        state: Optional[str] = None,
    ) -> "capo_networkmonitor.types.list_monitors_output.ListMonitorsOutput":
        """<p>Returns a list of all of your monitors.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            state: <p>The list of all monitors and their states.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.list_monitors

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.list_monitors.list_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMonitors")
        )
        input_: capo_networkmonitor.types.list_monitors_input.ListMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if state is not None:
            input_["state"] = state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMonitorResource:
    def __init__(self, service: AsyncNetworkMonitorClient) -> None:
        self._service = service

    async def put(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
        probes: Optional[
            "capo_networkmonitor.types.create_monitor_probe_input_list.CreateMonitorProbeInputList"
        ] = None,
        aggregation_period: Optional[
            "capo_networkmonitor.types.aggregation_period.AggregationPeriod"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkmonitor.types.create_monitor_output.CreateMonitorOutput":
        """<p>Creates a monitor between a source subnet and destination IP address. Within a monitor you'll create one or more probes that monitor network traffic between your source Amazon Web Services VPC subnets and your destination IP addresses. Each probe then aggregates and sends metrics to Amazon CloudWatch.</p> <p>You can also create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>source</code>—The subnet IDs where the probes will be created.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name identifying the monitor. It can contain only letters, underscores (_), or dashes (-), and can be up to 200 characters.</p>
            probes: <p>Displays a list of all of the probes created for a monitor.</p>
            aggregation_period: <p>The time, in seconds, that metrics are aggregated and sent to Amazon CloudWatch. Valid values are either <code>30</code> or <code>60</code>. <code>60</code> is the default if no period is chosen.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the monitor.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.create_monitor

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.create_monitor.async_create_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateMonitor")
        )
        input_: capo_networkmonitor.types.create_monitor_input.CreateMonitorInput = {
            "monitor_name": monitor_name
        }
        if probes is not None:
            input_["probes"] = probes
        if aggregation_period is not None:
            input_["aggregation_period"] = aggregation_period
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
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.get_monitor_output.GetMonitorOutput":
        """<p>Returns details about a specific monitor. </p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor that details are returned for.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.get_monitor

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.get_monitor.async_get_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMonitor")
        )
        input_: capo_networkmonitor.types.get_monitor_input.GetMonitorInput = {
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
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        aggregation_period: "capo_networkmonitor.types.aggregation_period.AggregationPeriod",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.update_monitor_output.UpdateMonitorOutput":
        """<p>Updates the <code>aggregationPeriod</code> for a monitor. Monitors support an <code>aggregationPeriod</code> of either <code>30</code> or <code>60</code> seconds. This action requires the <code>monitorName</code> and <code>probeId</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to update. </p>
            aggregation_period: <p>The aggregation time, in seconds, to change to. This must be either <code>30</code> or <code>60</code>. </p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.update_monitor

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.update_monitor.async_update_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMonitor")
        )
        input_: capo_networkmonitor.types.update_monitor_input.UpdateMonitorInput = {
            "monitor_name": monitor_name,
            "aggregation_period": aggregation_period,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput":
        """<p>Deletes a specified monitor.</p> <p>This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.delete_monitor

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.delete_monitor.async_delete_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMonitor")
        )
        input_: capo_networkmonitor.types.delete_monitor_input.DeleteMonitorInput = {
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
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
        next_token: Optional[
            "capo_networkmonitor.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_networkmonitor.types.max_results.MaxResults"
        ] = None,
        state: Optional[str] = None,
    ) -> "capo_networkmonitor.types.list_monitors_output.ListMonitorsOutput":
        """<p>Returns a list of all of your monitors.</p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>
            state: <p>The list of all monitors and their states.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.list_monitors

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.list_monitors.async_list_monitors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMonitors")
        )
        input_: capo_networkmonitor.types.list_monitors_input.ListMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if state is not None:
            input_["state"] = state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
