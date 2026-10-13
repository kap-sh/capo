from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_groundstation._auth._signers
import capo_groundstation._auth._sigv4
from capo_groundstation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_groundstation.types.agent_details
    import capo_groundstation.types.aggregate_status
    import capo_groundstation.types.component_status_list
    import capo_groundstation.types.discovery_data
    import capo_groundstation.types.get_agent_configuration_request
    import capo_groundstation.types.get_agent_configuration_response
    import capo_groundstation.types.register_agent_request
    import capo_groundstation.types.register_agent_response
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.update_agent_status_request
    import capo_groundstation.types.update_agent_status_response
    import capo_groundstation.types.uuid
    from capo_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from capo_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class Agent:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        discovery_data: "capo_groundstation.types.discovery_data.DiscoveryData",
        agent_details: "capo_groundstation.types.agent_details.AgentDetails",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.register_agent_response.RegisterAgentResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p> Registers a new agent with AWS Ground Station. </p>

        Args:
            discovery_data: <p>Data for associating an agent with the capabilities it is managing.</p>
            agent_details: <p>Detailed information about the agent being registered.</p>
            tags: <p>Tags assigned to an <code>Agent</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.register_agent_request.RegisterAgentRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.register_agent_response.RegisterAgentResponse"
        ]:
            import capo_groundstation._operations.ground_station.register_agent

            output, http_response = (
                capo_groundstation._operations.ground_station.register_agent.register_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterAgent")
        )
        input_: capo_groundstation.types.register_agent_request.RegisterAgentRequest = {
            "discovery_data": discovery_data,
            "agent_details": agent_details,
        }
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
        agent_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Gets the latest configuration information for a registered agent.</p>

        Args:
            agent_id: <p>UUID of agent to get configuration information for.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_agent_configuration

            output, http_response = (
                capo_groundstation._operations.ground_station.get_agent_configuration.get_agent_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAgentConfiguration")
        )
        input_: capo_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest = {
            "agent_id": agent_id
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
        agent_id: "capo_groundstation.types.uuid.Uuid",
        task_id: "capo_groundstation.types.uuid.Uuid",
        aggregate_status: "capo_groundstation.types.aggregate_status.AggregateStatus",
        component_statuses: "capo_groundstation.types.component_status_list.ComponentStatusList",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Update the status of the agent.</p>

        Args:
            agent_id: <p>UUID of agent to update.</p>
            task_id: <p>GUID of agent task.</p>
            aggregate_status: <p>Aggregate status for agent.</p>
            component_statuses: <p>List of component statuses for agent.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_agent_status

            output, http_response = (
                capo_groundstation._operations.ground_station.update_agent_status.update_agent_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAgentStatus")
        )
        input_: capo_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest = {
            "agent_id": agent_id,
            "task_id": task_id,
            "aggregate_status": aggregate_status,
            "component_statuses": component_statuses,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAgent:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        discovery_data: "capo_groundstation.types.discovery_data.DiscoveryData",
        agent_details: "capo_groundstation.types.agent_details.AgentDetails",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.register_agent_response.RegisterAgentResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p> Registers a new agent with AWS Ground Station. </p>

        Args:
            discovery_data: <p>Data for associating an agent with the capabilities it is managing.</p>
            agent_details: <p>Detailed information about the agent being registered.</p>
            tags: <p>Tags assigned to an <code>Agent</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.register_agent_request.RegisterAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.register_agent_response.RegisterAgentResponse"
        ]:
            import capo_groundstation._operations.ground_station.register_agent

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.register_agent.async_register_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterAgent")
        )
        input_: capo_groundstation.types.register_agent_request.RegisterAgentRequest = {
            "discovery_data": discovery_data,
            "agent_details": agent_details,
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

    async def read(
        self,
        agent_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Gets the latest configuration information for a registered agent.</p>

        Args:
            agent_id: <p>UUID of agent to get configuration information for.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_agent_configuration_response.GetAgentConfigurationResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_agent_configuration

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_agent_configuration.async_get_agent_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAgentConfiguration")
        )
        input_: capo_groundstation.types.get_agent_configuration_request.GetAgentConfigurationRequest = {
            "agent_id": agent_id
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
        agent_id: "capo_groundstation.types.uuid.Uuid",
        task_id: "capo_groundstation.types.uuid.Uuid",
        aggregate_status: "capo_groundstation.types.aggregate_status.AggregateStatus",
        component_statuses: "capo_groundstation.types.component_status_list.ComponentStatusList",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse":
        """<note> <p> For use by AWS Ground Station Agent and shouldn't be called directly.</p> </note> <p>Update the status of the agent.</p>

        Args:
            agent_id: <p>UUID of agent to update.</p>
            task_id: <p>GUID of agent task.</p>
            aggregate_status: <p>Aggregate status for agent.</p>
            component_statuses: <p>List of component statuses for agent.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.update_agent_status_response.UpdateAgentStatusResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_agent_status

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_agent_status.async_update_agent_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAgentStatus")
        )
        input_: capo_groundstation.types.update_agent_status_request.UpdateAgentStatusRequest = {
            "agent_id": agent_id,
            "task_id": task_id,
            "aggregate_status": aggregate_status,
            "component_statuses": component_statuses,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
