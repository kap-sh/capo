from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_groundstation._auth._signers
import capo_groundstation._auth._sigv4
from capo_groundstation._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_groundstation.types.create_dataflow_endpoint_group_v2_request
    import capo_groundstation.types.create_dataflow_endpoint_group_v2_response
    import capo_groundstation.types.create_endpoint_details_list
    import capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds
    import capo_groundstation.types.tags_map
    from capo_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from capo_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class DataflowEndpointGroupV2:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        endpoints: "capo_groundstation.types.create_endpoint_details_list.CreateEndpointDetailsList",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.create_dataflow_endpoint_group_v2_response.CreateDataflowEndpointGroupV2Response":
        """<p>Creates a <code>DataflowEndpoint</code> group containing the specified list of Ground Station Agent based endpoints.</p> <p>The <code>name</code> field in each endpoint is used in your mission profile <code> DataflowEndpointConfig</code> to specify which endpoints to use during a contact.</p> <p>When a contact uses multiple <code>DataflowEndpointConfig</code> objects, each <code> Config</code> must match a <code>DataflowEndpoint</code> in the same group.</p>

        Args:
            endpoints: <p>Dataflow endpoint group's endpoint definitions</p>
            contact_pre_pass_duration_seconds: <p> Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A <a href="https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state. </p>
            contact_post_pass_duration_seconds: <p> Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A <a href="https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state. </p>
            tags: <p>Tags of a V2 dataflow endpoint group.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.create_dataflow_endpoint_group_v2_request.CreateDataflowEndpointGroupV2Request]",
        ) -> OperationResponse[
            "capo_groundstation.types.create_dataflow_endpoint_group_v2_response.CreateDataflowEndpointGroupV2Response"
        ]:
            import capo_groundstation._operations.ground_station.create_dataflow_endpoint_group_v2

            output, http_response = (
                capo_groundstation._operations.ground_station.create_dataflow_endpoint_group_v2.create_dataflow_endpoint_group_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.create_dataflow_endpoint_group_v2_request.CreateDataflowEndpointGroupV2Request = {
            "endpoints": endpoints
        }
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDataflowEndpointGroupV2:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        endpoints: "capo_groundstation.types.create_endpoint_details_list.CreateEndpointDetailsList",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.create_dataflow_endpoint_group_v2_response.CreateDataflowEndpointGroupV2Response":
        """<p>Creates a <code>DataflowEndpoint</code> group containing the specified list of Ground Station Agent based endpoints.</p> <p>The <code>name</code> field in each endpoint is used in your mission profile <code> DataflowEndpointConfig</code> to specify which endpoints to use during a contact.</p> <p>When a contact uses multiple <code>DataflowEndpointConfig</code> objects, each <code> Config</code> must match a <code>DataflowEndpoint</code> in the same group.</p>

        Args:
            endpoints: <p>Dataflow endpoint group's endpoint definitions</p>
            contact_pre_pass_duration_seconds: <p> Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A <a href="https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state. </p>
            contact_post_pass_duration_seconds: <p> Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A <a href="https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state. </p>
            tags: <p>Tags of a V2 dataflow endpoint group.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.create_dataflow_endpoint_group_v2_request.CreateDataflowEndpointGroupV2Request]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.create_dataflow_endpoint_group_v2_response.CreateDataflowEndpointGroupV2Response"
        ]:
            import capo_groundstation._operations.ground_station.create_dataflow_endpoint_group_v2

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.create_dataflow_endpoint_group_v2.async_create_dataflow_endpoint_group_v2(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.create_dataflow_endpoint_group_v2_request.CreateDataflowEndpointGroupV2Request = {
            "endpoints": endpoints
        }
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
