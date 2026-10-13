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
    import capo_networkmonitor.types.create_probe_input
    import capo_networkmonitor.types.create_probe_output
    import capo_networkmonitor.types.delete_probe_input
    import capo_networkmonitor.types.delete_probe_output
    import capo_networkmonitor.types.destination
    import capo_networkmonitor.types.get_probe_input
    import capo_networkmonitor.types.get_probe_output
    import capo_networkmonitor.types.packet_size
    import capo_networkmonitor.types.port
    import capo_networkmonitor.types.probe_id
    import capo_networkmonitor.types.probe_input
    import capo_networkmonitor.types.probe_state
    import capo_networkmonitor.types.protocol
    import capo_networkmonitor.types.resource_name
    import capo_networkmonitor.types.tag_map
    import capo_networkmonitor.types.update_probe_input
    import capo_networkmonitor.types.update_probe_output
    from capo_networkmonitor._services.async_network_monitor import (
        AsyncNetworkMonitorClient,
        AsyncNetworkMonitorClientConfig,
    )
    from capo_networkmonitor._services.network_monitor import (
        NetworkMonitorClient,
        NetworkMonitorClientConfig,
    )


class ProbeResource:
    def __init__(self, service: NetworkMonitorClient) -> None:
        self._service = service

    def create(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        probe: "capo_networkmonitor.types.probe_input.ProbeInput",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkmonitor.types.create_probe_output.CreateProbeOutput":
        """<p>Create a probe within a monitor. Once you create a probe, and it begins monitoring your network traffic, you'll incur billing charges for that probe. This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. Note the name of the <code>monitorName</code> you want to create the probe for.</p>

        Args:
            monitor_name: <p>The name of the monitor to associated with the probe. </p>
            probe: <p>Describes the details of an individual probe for a monitor.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the probe.</p>

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
            req: "OperationRequest[capo_networkmonitor.types.create_probe_input.CreateProbeInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.create_probe_output.CreateProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.create_probe

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.create_probe.create_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateProbe")
        )
        input_: capo_networkmonitor.types.create_probe_input.CreateProbeInput = {
            "monitor_name": monitor_name,
            "probe": probe,
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
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.get_probe_output.GetProbeOutput":
        """<p>Returns the details about a probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p>

        Args:
            monitor_name: <p>The name of the monitor associated with the probe. Run <code>ListMonitors</code> to get a list of monitor names.</p>
            probe_id: <p>The ID of the probe to get information about. Run <code>GetMonitor</code> action to get a list of probes and probe IDs for the monitor.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_networkmonitor.types.get_probe_input.GetProbeInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.get_probe_output.GetProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.get_probe

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.get_probe.get_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetProbe")
        )
        input_: capo_networkmonitor.types.get_probe_input.GetProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
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
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
        state: Optional["capo_networkmonitor.types.probe_state.ProbeState"] = None,
        destination: Optional[
            "capo_networkmonitor.types.destination.Destination"
        ] = None,
        destination_port: Optional["capo_networkmonitor.types.port.Port"] = None,
        protocol: Optional["capo_networkmonitor.types.protocol.Protocol"] = None,
        packet_size: Optional[
            "capo_networkmonitor.types.packet_size.PacketSize"
        ] = None,
    ) -> "capo_networkmonitor.types.update_probe_output.UpdateProbeOutput":
        """<p>Updates a monitor probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p> <p>You can update the following para create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>state</code>—The state of the probe.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name of the monitor that the probe was updated for.</p>
            probe_id: <p>The ID of the probe to update.</p>
            state: <p>The state of the probe update.</p>
            destination: <p>The updated IP address for the probe destination. This must be either an IPv4 or IPv6 address.</p>
            destination_port: <p>The updated port for the probe destination. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>
            protocol: <p>The updated network protocol for the destination. This can be either <code>TCP</code> or <code>ICMP</code>. If the protocol is <code>TCP</code>, then <code>port</code> is also required.</p>
            packet_size: <p>he updated packets size for network traffic between the source and destination. This must be a number between <code>56</code> and <code>8500</code>.</p>

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
            req: "OperationRequest[capo_networkmonitor.types.update_probe_input.UpdateProbeInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.update_probe_output.UpdateProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.update_probe

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.update_probe.update_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateProbe")
        )
        input_: capo_networkmonitor.types.update_probe_input.UpdateProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
        }
        if state is not None:
            input_["state"] = state
        if destination is not None:
            input_["destination"] = destination
        if destination_port is not None:
            input_["destination_port"] = destination_port
        if protocol is not None:
            input_["protocol"] = protocol
        if packet_size is not None:
            input_["packet_size"] = packet_size

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
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[NetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.delete_probe_output.DeleteProbeOutput":
        """<p>Deletes the specified probe. Once a probe is deleted you'll no longer incur any billing fees for that probe.</p> <p>This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. You can only delete a single probe at a time using this action. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>
            probe_id: <p>The ID of the probe to delete. </p>

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
            req: "OperationRequest[capo_networkmonitor.types.delete_probe_input.DeleteProbeInput]",
        ) -> OperationResponse[
            "capo_networkmonitor.types.delete_probe_output.DeleteProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.delete_probe

            output, http_response = (
                capo_networkmonitor._operations.network_monitor.delete_probe.delete_probe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteProbe")
        )
        input_: capo_networkmonitor.types.delete_probe_input.DeleteProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncProbeResource:
    def __init__(self, service: AsyncNetworkMonitorClient) -> None:
        self._service = service

    async def create(
        self,
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        probe: "capo_networkmonitor.types.probe_input.ProbeInput",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_networkmonitor.types.tag_map.TagMap"] = None,
    ) -> "capo_networkmonitor.types.create_probe_output.CreateProbeOutput":
        """<p>Create a probe within a monitor. Once you create a probe, and it begins monitoring your network traffic, you'll incur billing charges for that probe. This action requires the <code>monitorName</code> parameter. Run <code>ListMonitors</code> to get a list of monitor names. Note the name of the <code>monitorName</code> you want to create the probe for.</p>

        Args:
            monitor_name: <p>The name of the monitor to associated with the probe. </p>
            probe: <p>Describes the details of an individual probe for a monitor.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>
            tags: <p>The list of key-value pairs created and assigned to the probe.</p>

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
            req: "AsyncOperationRequest[capo_networkmonitor.types.create_probe_input.CreateProbeInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.create_probe_output.CreateProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.create_probe

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.create_probe.async_create_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateProbe")
        )
        input_: capo_networkmonitor.types.create_probe_input.CreateProbeInput = {
            "monitor_name": monitor_name,
            "probe": probe,
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
        monitor_name: "capo_networkmonitor.types.resource_name.ResourceName",
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.get_probe_output.GetProbeOutput":
        """<p>Returns the details about a probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p>

        Args:
            monitor_name: <p>The name of the monitor associated with the probe. Run <code>ListMonitors</code> to get a list of monitor names.</p>
            probe_id: <p>The ID of the probe to get information about. Run <code>GetMonitor</code> action to get a list of probes and probe IDs for the monitor.</p>

        Raises:
            capo_networkmonitor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_networkmonitor.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_networkmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_networkmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling</p>
            capo_networkmonitor.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_networkmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_networkmonitor.types.get_probe_input.GetProbeInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.get_probe_output.GetProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.get_probe

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.get_probe.async_get_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetProbe")
        )
        input_: capo_networkmonitor.types.get_probe_input.GetProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
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
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
        state: Optional["capo_networkmonitor.types.probe_state.ProbeState"] = None,
        destination: Optional[
            "capo_networkmonitor.types.destination.Destination"
        ] = None,
        destination_port: Optional["capo_networkmonitor.types.port.Port"] = None,
        protocol: Optional["capo_networkmonitor.types.protocol.Protocol"] = None,
        packet_size: Optional[
            "capo_networkmonitor.types.packet_size.PacketSize"
        ] = None,
    ) -> "capo_networkmonitor.types.update_probe_output.UpdateProbeOutput":
        """<p>Updates a monitor probe. This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. </p> <p>You can update the following para create a monitor with probes using this command. For each probe, you define the following:</p> <ul> <li> <p> <code>state</code>—The state of the probe.</p> </li> <li> <p> <code>destination</code>— The target destination IP address for the probe.</p> </li> <li> <p> <code>destinationPort</code>—Required only if the protocol is <code>TCP</code>.</p> </li> <li> <p> <code>protocol</code>—The communication protocol between the source and destination. This will be either <code>TCP</code> or <code>ICMP</code>.</p> </li> <li> <p> <code>packetSize</code>—The size of the packets. This must be a number between <code>56</code> and <code>8500</code>.</p> </li> <li> <p>(Optional) <code>tags</code> —Key-value pairs created and assigned to the probe.</p> </li> </ul>

        Args:
            monitor_name: <p>The name of the monitor that the probe was updated for.</p>
            probe_id: <p>The ID of the probe to update.</p>
            state: <p>The state of the probe update.</p>
            destination: <p>The updated IP address for the probe destination. This must be either an IPv4 or IPv6 address.</p>
            destination_port: <p>The updated port for the probe destination. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>
            protocol: <p>The updated network protocol for the destination. This can be either <code>TCP</code> or <code>ICMP</code>. If the protocol is <code>TCP</code>, then <code>port</code> is also required.</p>
            packet_size: <p>he updated packets size for network traffic between the source and destination. This must be a number between <code>56</code> and <code>8500</code>.</p>

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
            req: "AsyncOperationRequest[capo_networkmonitor.types.update_probe_input.UpdateProbeInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.update_probe_output.UpdateProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.update_probe

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.update_probe.async_update_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateProbe")
        )
        input_: capo_networkmonitor.types.update_probe_input.UpdateProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
        }
        if state is not None:
            input_["state"] = state
        if destination is not None:
            input_["destination"] = destination
        if destination_port is not None:
            input_["destination_port"] = destination_port
        if protocol is not None:
            input_["protocol"] = protocol
        if packet_size is not None:
            input_["packet_size"] = packet_size

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
        probe_id: "capo_networkmonitor.types.probe_id.ProbeId",
        *,
        config_overrides: Optional[AsyncNetworkMonitorClientConfig] = None,
    ) -> "capo_networkmonitor.types.delete_probe_output.DeleteProbeOutput":
        """<p>Deletes the specified probe. Once a probe is deleted you'll no longer incur any billing fees for that probe.</p> <p>This action requires both the <code>monitorName</code> and <code>probeId</code> parameters. Run <code>ListMonitors</code> to get a list of monitor names. Run <code>GetMonitor</code> to get a list of probes and probe IDs. You can only delete a single probe at a time using this action. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete. </p>
            probe_id: <p>The ID of the probe to delete. </p>

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
            req: "AsyncOperationRequest[capo_networkmonitor.types.delete_probe_input.DeleteProbeInput]",
        ) -> AsyncOperationResponse[
            "capo_networkmonitor.types.delete_probe_output.DeleteProbeOutput"
        ]:
            import capo_networkmonitor._operations.network_monitor.delete_probe

            (
                output,
                http_response,
            ) = await capo_networkmonitor._operations.network_monitor.delete_probe.async_delete_probe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteProbe")
        )
        input_: capo_networkmonitor.types.delete_probe_input.DeleteProbeInput = {
            "monitor_name": monitor_name,
            "probe_id": probe_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
