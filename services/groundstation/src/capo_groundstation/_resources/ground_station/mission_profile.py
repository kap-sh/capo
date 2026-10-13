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
    import capo_groundstation.types.config_arn
    import capo_groundstation.types.create_mission_profile_request
    import capo_groundstation.types.dataflow_edge_list
    import capo_groundstation.types.delete_mission_profile_request
    import capo_groundstation.types.duration_in_seconds
    import capo_groundstation.types.get_mission_profile_request
    import capo_groundstation.types.get_mission_profile_response
    import capo_groundstation.types.kms_key
    import capo_groundstation.types.list_mission_profiles_request
    import capo_groundstation.types.list_mission_profiles_response
    import capo_groundstation.types.mission_profile_id_response
    import capo_groundstation.types.mission_profile_list_item
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.positive_duration_in_seconds
    import capo_groundstation.types.role_arn
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.update_mission_profile_request
    import capo_groundstation.types.uuid
    from capo_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from capo_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class MissionProfile:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_groundstation.types.safe_name.SafeName",
        minimum_viable_contact_duration_seconds: "capo_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds",
        dataflow_edges: "capo_groundstation.types.dataflow_edge_list.DataflowEdgeList",
        tracking_config_arn: "capo_groundstation.types.config_arn.ConfigArn",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        telemetry_sink_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
        streams_kms_key: Optional["capo_groundstation.types.kms_key.KmsKey"] = None,
        streams_kms_role: Optional["capo_groundstation.types.role_arn.RoleArn"] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Creates a mission profile.</p> <p> <code>dataflowEdges</code> is a list of lists of strings. Each lower level list of strings has two elements: a <i>from</i> ARN and a <i>to</i> ARN.</p>

        Args:
            name: <p>Name of a mission profile.</p>
            contact_pre_pass_duration_seconds: <p>Amount of time prior to contact start you'd like to receive a Ground Station Contact State Change event indicating an upcoming pass.</p>
            contact_post_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            minimum_viable_contact_duration_seconds: <p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>
            dataflow_edges: <p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>
            tracking_config_arn: <p>ARN of a tracking <code>Config</code>.</p>
            telemetry_sink_config_arn: <p>ARN of a telemetry sink <code>Config</code>.</p>
            tags: <p>Tags assigned to a mission profile.</p>
            streams_kms_key: <p>KMS key to use for encrypting streams.</p>
            streams_kms_role: <p>Role to use for encrypting streams with KMS key.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.create_mission_profile_request.CreateMissionProfileRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.create_mission_profile

            output, http_response = (
                capo_groundstation._operations.ground_station.create_mission_profile.create_mission_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateMissionProfile")
        )
        input_: capo_groundstation.types.create_mission_profile_request.CreateMissionProfileRequest = {
            "name": name,
            "minimum_viable_contact_duration_seconds": minimum_viable_contact_duration_seconds,
            "dataflow_edges": dataflow_edges,
            "tracking_config_arn": tracking_config_arn,
        }
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if telemetry_sink_config_arn is not None:
            input_["telemetry_sink_config_arn"] = telemetry_sink_config_arn
        if tags is not None:
            input_["tags"] = tags
        if streams_kms_key is not None:
            input_["streams_kms_key"] = streams_kms_key
        if streams_kms_role is not None:
            input_["streams_kms_role"] = streams_kms_role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_mission_profile_response.GetMissionProfileResponse":
        """<p>Returns a mission profile.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.get_mission_profile_request.GetMissionProfileRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.get_mission_profile_response.GetMissionProfileResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_mission_profile

            output, http_response = (
                capo_groundstation._operations.ground_station.get_mission_profile.get_mission_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMissionProfile")
        )
        input_: capo_groundstation.types.get_mission_profile_request.GetMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
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
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        name: Optional["capo_groundstation.types.safe_name.SafeName"] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        minimum_viable_contact_duration_seconds: Optional[
            "capo_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds"
        ] = None,
        dataflow_edges: Optional[
            "capo_groundstation.types.dataflow_edge_list.DataflowEdgeList"
        ] = None,
        tracking_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        telemetry_sink_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        streams_kms_key: Optional["capo_groundstation.types.kms_key.KmsKey"] = None,
        streams_kms_role: Optional["capo_groundstation.types.role_arn.RoleArn"] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Updates a mission profile.</p> <p>Updating a mission profile will not update the execution parameters for existing future contacts.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>
            name: <p>Name of a mission profile.</p>
            contact_pre_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            contact_post_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            minimum_viable_contact_duration_seconds: <p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>
            dataflow_edges: <p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>
            tracking_config_arn: <p>ARN of a tracking <code>Config</code>.</p>
            telemetry_sink_config_arn: <p>ARN of a telemetry sink <code>Config</code>.</p>
            streams_kms_key: <p>KMS key to use for encrypting streams.</p>
            streams_kms_role: <p>Role to use for encrypting streams with KMS key.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.update_mission_profile_request.UpdateMissionProfileRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_mission_profile

            output, http_response = (
                capo_groundstation._operations.ground_station.update_mission_profile.update_mission_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMissionProfile")
        )
        input_: capo_groundstation.types.update_mission_profile_request.UpdateMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
        }
        if name is not None:
            input_["name"] = name
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if minimum_viable_contact_duration_seconds is not None:
            input_["minimum_viable_contact_duration_seconds"] = (
                minimum_viable_contact_duration_seconds
            )
        if dataflow_edges is not None:
            input_["dataflow_edges"] = dataflow_edges
        if tracking_config_arn is not None:
            input_["tracking_config_arn"] = tracking_config_arn
        if telemetry_sink_config_arn is not None:
            input_["telemetry_sink_config_arn"] = telemetry_sink_config_arn
        if streams_kms_key is not None:
            input_["streams_kms_key"] = streams_kms_key
        if streams_kms_role is not None:
            input_["streams_kms_role"] = streams_kms_role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Deletes a mission profile.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.delete_mission_profile_request.DeleteMissionProfileRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.delete_mission_profile

            output, http_response = (
                capo_groundstation._operations.ground_station.delete_mission_profile.delete_mission_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMissionProfile")
        )
        input_: capo_groundstation.types.delete_mission_profile_request.DeleteMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
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
        config_overrides: Optional[GroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_mission_profiles_response.ListMissionProfilesResponse":
        """<p>Returns a list of mission profiles.</p>

        Args:
            max_results: <p>Maximum number of mission profiles returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListMissionProfiles</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.list_mission_profiles_request.ListMissionProfilesRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.list_mission_profiles_response.ListMissionProfilesResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_mission_profiles

            output, http_response = (
                capo_groundstation._operations.ground_station.list_mission_profiles.list_mission_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMissionProfiles")
        )
        input_: capo_groundstation.types.list_mission_profiles_request.ListMissionProfilesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMissionProfile:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_groundstation.types.safe_name.SafeName",
        minimum_viable_contact_duration_seconds: "capo_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds",
        dataflow_edges: "capo_groundstation.types.dataflow_edge_list.DataflowEdgeList",
        tracking_config_arn: "capo_groundstation.types.config_arn.ConfigArn",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        telemetry_sink_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
        streams_kms_key: Optional["capo_groundstation.types.kms_key.KmsKey"] = None,
        streams_kms_role: Optional["capo_groundstation.types.role_arn.RoleArn"] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Creates a mission profile.</p> <p> <code>dataflowEdges</code> is a list of lists of strings. Each lower level list of strings has two elements: a <i>from</i> ARN and a <i>to</i> ARN.</p>

        Args:
            name: <p>Name of a mission profile.</p>
            contact_pre_pass_duration_seconds: <p>Amount of time prior to contact start you'd like to receive a Ground Station Contact State Change event indicating an upcoming pass.</p>
            contact_post_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            minimum_viable_contact_duration_seconds: <p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>
            dataflow_edges: <p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>
            tracking_config_arn: <p>ARN of a tracking <code>Config</code>.</p>
            telemetry_sink_config_arn: <p>ARN of a telemetry sink <code>Config</code>.</p>
            tags: <p>Tags assigned to a mission profile.</p>
            streams_kms_key: <p>KMS key to use for encrypting streams.</p>
            streams_kms_role: <p>Role to use for encrypting streams with KMS key.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.create_mission_profile_request.CreateMissionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.create_mission_profile

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.create_mission_profile.async_create_mission_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateMissionProfile")
        )
        input_: capo_groundstation.types.create_mission_profile_request.CreateMissionProfileRequest = {
            "name": name,
            "minimum_viable_contact_duration_seconds": minimum_viable_contact_duration_seconds,
            "dataflow_edges": dataflow_edges,
            "tracking_config_arn": tracking_config_arn,
        }
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if telemetry_sink_config_arn is not None:
            input_["telemetry_sink_config_arn"] = telemetry_sink_config_arn
        if tags is not None:
            input_["tags"] = tags
        if streams_kms_key is not None:
            input_["streams_kms_key"] = streams_kms_key
        if streams_kms_role is not None:
            input_["streams_kms_role"] = streams_kms_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_mission_profile_response.GetMissionProfileResponse":
        """<p>Returns a mission profile.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_mission_profile_request.GetMissionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_mission_profile_response.GetMissionProfileResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_mission_profile

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_mission_profile.async_get_mission_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMissionProfile")
        )
        input_: capo_groundstation.types.get_mission_profile_request.GetMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
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
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        name: Optional["capo_groundstation.types.safe_name.SafeName"] = None,
        contact_pre_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        contact_post_pass_duration_seconds: Optional[
            "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
        ] = None,
        minimum_viable_contact_duration_seconds: Optional[
            "capo_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds"
        ] = None,
        dataflow_edges: Optional[
            "capo_groundstation.types.dataflow_edge_list.DataflowEdgeList"
        ] = None,
        tracking_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        telemetry_sink_config_arn: Optional[
            "capo_groundstation.types.config_arn.ConfigArn"
        ] = None,
        streams_kms_key: Optional["capo_groundstation.types.kms_key.KmsKey"] = None,
        streams_kms_role: Optional["capo_groundstation.types.role_arn.RoleArn"] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Updates a mission profile.</p> <p>Updating a mission profile will not update the execution parameters for existing future contacts.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>
            name: <p>Name of a mission profile.</p>
            contact_pre_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            contact_post_pass_duration_seconds: <p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>
            minimum_viable_contact_duration_seconds: <p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>
            dataflow_edges: <p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>
            tracking_config_arn: <p>ARN of a tracking <code>Config</code>.</p>
            telemetry_sink_config_arn: <p>ARN of a telemetry sink <code>Config</code>.</p>
            streams_kms_key: <p>KMS key to use for encrypting streams.</p>
            streams_kms_role: <p>Role to use for encrypting streams with KMS key.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_mission_profile_request.UpdateMissionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_mission_profile

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_mission_profile.async_update_mission_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMissionProfile")
        )
        input_: capo_groundstation.types.update_mission_profile_request.UpdateMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
        }
        if name is not None:
            input_["name"] = name
        if contact_pre_pass_duration_seconds is not None:
            input_["contact_pre_pass_duration_seconds"] = (
                contact_pre_pass_duration_seconds
            )
        if contact_post_pass_duration_seconds is not None:
            input_["contact_post_pass_duration_seconds"] = (
                contact_post_pass_duration_seconds
            )
        if minimum_viable_contact_duration_seconds is not None:
            input_["minimum_viable_contact_duration_seconds"] = (
                minimum_viable_contact_duration_seconds
            )
        if dataflow_edges is not None:
            input_["dataflow_edges"] = dataflow_edges
        if tracking_config_arn is not None:
            input_["tracking_config_arn"] = tracking_config_arn
        if telemetry_sink_config_arn is not None:
            input_["telemetry_sink_config_arn"] = telemetry_sink_config_arn
        if streams_kms_key is not None:
            input_["streams_kms_key"] = streams_kms_key
        if streams_kms_role is not None:
            input_["streams_kms_role"] = streams_kms_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        mission_profile_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> (
        "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
    ):
        """<p>Deletes a mission profile.</p>

        Args:
            mission_profile_id: <p>UUID of a mission profile.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.delete_mission_profile_request.DeleteMissionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.mission_profile_id_response.MissionProfileIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.delete_mission_profile

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.delete_mission_profile.async_delete_mission_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMissionProfile")
        )
        input_: capo_groundstation.types.delete_mission_profile_request.DeleteMissionProfileRequest = {
            "mission_profile_id": mission_profile_id
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
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_mission_profiles_response.ListMissionProfilesResponse":
        """<p>Returns a list of mission profiles.</p>

        Args:
            max_results: <p>Maximum number of mission profiles returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListMissionProfiles</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_mission_profiles_request.ListMissionProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_mission_profiles_response.ListMissionProfilesResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_mission_profiles

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_mission_profiles.async_list_mission_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMissionProfiles")
        )
        input_: capo_groundstation.types.list_mission_profiles_request.ListMissionProfilesRequest = {}
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
