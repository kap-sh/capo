from __future__ import annotations

import datetime
import uuid
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
    import capo_groundstation.types.cancel_contact_request
    import capo_groundstation.types.client_token
    import capo_groundstation.types.contact_data
    import capo_groundstation.types.contact_id_response
    import capo_groundstation.types.contact_version
    import capo_groundstation.types.describe_contact_request
    import capo_groundstation.types.describe_contact_response
    import capo_groundstation.types.describe_contact_version_request
    import capo_groundstation.types.describe_contact_version_response
    import capo_groundstation.types.ephemeris_filter
    import capo_groundstation.types.ground_station_name
    import capo_groundstation.types.list_contact_versions_request
    import capo_groundstation.types.list_contact_versions_response
    import capo_groundstation.types.list_contacts_request
    import capo_groundstation.types.list_contacts_response
    import capo_groundstation.types.mission_profile_arn
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.reserve_contact_request
    import capo_groundstation.types.satellite_arn
    import capo_groundstation.types.status_list
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.tracking_overrides
    import capo_groundstation.types.update_contact_request
    import capo_groundstation.types.update_contact_response
    import capo_groundstation.types.uuid
    import capo_groundstation.types.version_id
    from capo_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from capo_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class Contact:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        mission_profile_arn: "capo_groundstation.types.mission_profile_arn.MissionProfileArn",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        ground_station: "capo_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
        tracking_overrides: Optional[
            "capo_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
    ) -> "capo_groundstation.types.contact_id_response.ContactIdResponse":
        """<p>Reserves a contact using specified parameters.</p>

        Args:
            mission_profile_arn: <p>ARN of a mission profile.</p>
            satellite_arn: <p>ARN of a satellite</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            tags: <p>Tags assigned to a contact.</p>
            tracking_overrides: <p>Tracking configuration overrides for the contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.reserve_contact_request.ReserveContactRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.reserve_contact

            output, http_response = (
                capo_groundstation._operations.ground_station.reserve_contact.reserve_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.reserve_contact_request.ReserveContactRequest = {
            "mission_profile_arn": mission_profile_arn,
            "start_time": start_time,
            "end_time": end_time,
            "ground_station": ground_station,
        }
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        if tags is not None:
            input_["tags"] = tags
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.describe_contact_response.DescribeContactResponse":
        """<p>Describes an existing contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.describe_contact_request.DescribeContactRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.describe_contact_response.DescribeContactResponse"
        ]:
            import capo_groundstation._operations.ground_station.describe_contact

            output, http_response = (
                capo_groundstation._operations.ground_station.describe_contact.describe_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.describe_contact_request.DescribeContactRequest = {
            "contact_id": contact_id
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
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        client_token: Optional[
            "capo_groundstation.types.client_token.ClientToken"
        ] = None,
        tracking_overrides: Optional[
            "capo_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
    ) -> "capo_groundstation.types.update_contact_response.UpdateContactResponse":
        """<p>Updates a specific contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 64 ASCII characters. It is generated by the client to ensure idempotent operations, allowing safe retries without unintended side effects.</p>
            satellite_arn: <p>ARN of a satellite.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.update_contact_request.UpdateContactRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.update_contact_response.UpdateContactResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_contact

            output, http_response = (
                capo_groundstation._operations.ground_station.update_contact.update_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.update_contact_request.UpdateContactRequest = {
            "contact_id": contact_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.contact_id_response.ContactIdResponse":
        """<p>Cancels or stops a contact with a specified contact ID based on its position in the <a href="https://docs.aws.amazon.com/ground-station/latest/ug/contacts.lifecycle.html">contact lifecycle</a>.</p> <p>For contacts that:</p> <ul> <li> <p>Have yet to start, the contact will be cancelled.</p> </li> <li> <p>Have started but have yet to finish, the contact will be stopped.</p> </li> </ul>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.cancel_contact_request.CancelContactRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.cancel_contact

            output, http_response = (
                capo_groundstation._operations.ground_station.cancel_contact.cancel_contact(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.cancel_contact_request.CancelContactRequest = {
            "contact_id": contact_id
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
        status_list: "capo_groundstation.types.status_list.StatusList",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
        ground_station: Optional[
            "capo_groundstation.types.ground_station_name.GroundStationName"
        ] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        mission_profile_arn: Optional[
            "capo_groundstation.types.mission_profile_arn.MissionProfileArn"
        ] = None,
        ephemeris: Optional[
            "capo_groundstation.types.ephemeris_filter.EphemerisFilter"
        ] = None,
    ) -> "capo_groundstation.types.list_contacts_response.ListContactsResponse":
        """<p>Returns a list of contacts.</p> <p>If <code>statusList</code> contains AVAILABLE, the request must include <code> groundStation</code>, <code>missionprofileArn</code>, and <code>satelliteArn</code>. </p>

        Args:
            max_results: <p>Maximum number of contacts returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContacts</code> call. Used to get the next page of results.</p>
            status_list: <p>Status of a contact reservation.</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            satellite_arn: <p>ARN of a satellite.</p>
            mission_profile_arn: <p>ARN of a mission profile.</p>
            ephemeris: <p>Filter for selecting contacts that use a specific ephemeris".</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.list_contacts_request.ListContactsRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.list_contacts_response.ListContactsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_contacts

            output, http_response = (
                capo_groundstation._operations.ground_station.list_contacts.list_contacts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.list_contacts_request.ListContactsRequest = {
            "status_list": status_list,
            "start_time": start_time,
            "end_time": end_time,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if ground_station is not None:
            input_["ground_station"] = ground_station
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        if mission_profile_arn is not None:
            input_["mission_profile_arn"] = mission_profile_arn
        if ephemeris is not None:
            input_["ephemeris"] = ephemeris

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_contact_version(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        version_id: "capo_groundstation.types.version_id.VersionId",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse":
        """<p>Describes a specific version of a contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            version_id: <p>Version ID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse"
        ]:
            import capo_groundstation._operations.ground_station.describe_contact_version

            output, http_response = (
                capo_groundstation._operations.ground_station.describe_contact_version.describe_contact_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest = {
            "contact_id": contact_id,
            "version_id": version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_contact_versions(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_contact_versions_response.ListContactVersionsResponse":
        """<p>Returns a list of versions for a specified contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            max_results: <p>Maximum number of contact versions returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContactVersions</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.list_contact_versions_request.ListContactVersionsRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.list_contact_versions_response.ListContactVersionsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_contact_versions

            output, http_response = (
                capo_groundstation._operations.ground_station.list_contact_versions.list_contact_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.list_contact_versions_request.ListContactVersionsRequest = {
            "contact_id": contact_id
        }
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


class AsyncContact:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        mission_profile_arn: "capo_groundstation.types.mission_profile_arn.MissionProfileArn",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        ground_station: "capo_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
        tracking_overrides: Optional[
            "capo_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
    ) -> "capo_groundstation.types.contact_id_response.ContactIdResponse":
        """<p>Reserves a contact using specified parameters.</p>

        Args:
            mission_profile_arn: <p>ARN of a mission profile.</p>
            satellite_arn: <p>ARN of a satellite</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            tags: <p>Tags assigned to a contact.</p>
            tracking_overrides: <p>Tracking configuration overrides for the contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.reserve_contact_request.ReserveContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.reserve_contact

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.reserve_contact.async_reserve_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.reserve_contact_request.ReserveContactRequest = {
            "mission_profile_arn": mission_profile_arn,
            "start_time": start_time,
            "end_time": end_time,
            "ground_station": ground_station,
        }
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        if tags is not None:
            input_["tags"] = tags
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.describe_contact_response.DescribeContactResponse":
        """<p>Describes an existing contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.describe_contact_request.DescribeContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.describe_contact_response.DescribeContactResponse"
        ]:
            import capo_groundstation._operations.ground_station.describe_contact

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.describe_contact.async_describe_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.describe_contact_request.DescribeContactRequest = {
            "contact_id": contact_id
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
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        client_token: Optional[
            "capo_groundstation.types.client_token.ClientToken"
        ] = None,
        tracking_overrides: Optional[
            "capo_groundstation.types.tracking_overrides.TrackingOverrides"
        ] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
    ) -> "capo_groundstation.types.update_contact_response.UpdateContactResponse":
        """<p>Updates a specific contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            client_token: <p>A client token is a unique, case-sensitive string of up to 64 ASCII characters. It is generated by the client to ensure idempotent operations, allowing safe retries without unintended side effects.</p>
            satellite_arn: <p>ARN of a satellite.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_contact_request.UpdateContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.update_contact_response.UpdateContactResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_contact

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_contact.async_update_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.update_contact_request.UpdateContactRequest = {
            "contact_id": contact_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tracking_overrides is not None:
            input_["tracking_overrides"] = tracking_overrides
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.contact_id_response.ContactIdResponse":
        """<p>Cancels or stops a contact with a specified contact ID based on its position in the <a href="https://docs.aws.amazon.com/ground-station/latest/ug/contacts.lifecycle.html">contact lifecycle</a>.</p> <p>For contacts that:</p> <ul> <li> <p>Have yet to start, the contact will be cancelled.</p> </li> <li> <p>Have started but have yet to finish, the contact will be stopped.</p> </li> </ul>

        Args:
            contact_id: <p>UUID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.cancel_contact_request.CancelContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.contact_id_response.ContactIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.cancel_contact

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.cancel_contact.async_cancel_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.cancel_contact_request.CancelContactRequest = {
            "contact_id": contact_id
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
        status_list: "capo_groundstation.types.status_list.StatusList",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
        ground_station: Optional[
            "capo_groundstation.types.ground_station_name.GroundStationName"
        ] = None,
        satellite_arn: Optional[
            "capo_groundstation.types.satellite_arn.satelliteArn"
        ] = None,
        mission_profile_arn: Optional[
            "capo_groundstation.types.mission_profile_arn.MissionProfileArn"
        ] = None,
        ephemeris: Optional[
            "capo_groundstation.types.ephemeris_filter.EphemerisFilter"
        ] = None,
    ) -> "capo_groundstation.types.list_contacts_response.ListContactsResponse":
        """<p>Returns a list of contacts.</p> <p>If <code>statusList</code> contains AVAILABLE, the request must include <code> groundStation</code>, <code>missionprofileArn</code>, and <code>satelliteArn</code>. </p>

        Args:
            max_results: <p>Maximum number of contacts returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContacts</code> call. Used to get the next page of results.</p>
            status_list: <p>Status of a contact reservation.</p>
            start_time: <p>Start time of a contact in UTC.</p>
            end_time: <p>End time of a contact in UTC.</p>
            ground_station: <p>Name of a ground station.</p>
            satellite_arn: <p>ARN of a satellite.</p>
            mission_profile_arn: <p>ARN of a mission profile.</p>
            ephemeris: <p>Filter for selecting contacts that use a specific ephemeris".</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_contacts_request.ListContactsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_contacts_response.ListContactsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_contacts

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_contacts.async_list_contacts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.list_contacts_request.ListContactsRequest = {
            "status_list": status_list,
            "start_time": start_time,
            "end_time": end_time,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if ground_station is not None:
            input_["ground_station"] = ground_station
        if satellite_arn is not None:
            input_["satellite_arn"] = satellite_arn
        if mission_profile_arn is not None:
            input_["mission_profile_arn"] = mission_profile_arn
        if ephemeris is not None:
            input_["ephemeris"] = ephemeris

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_contact_version(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        version_id: "capo_groundstation.types.version_id.VersionId",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse":
        """<p>Describes a specific version of a contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            version_id: <p>Version ID of a contact.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.describe_contact_version_response.DescribeContactVersionResponse"
        ]:
            import capo_groundstation._operations.ground_station.describe_contact_version

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.describe_contact_version.async_describe_contact_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.describe_contact_version_request.DescribeContactVersionRequest = {
            "contact_id": contact_id,
            "version_id": version_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_contact_versions(
        self,
        contact_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_contact_versions_response.ListContactVersionsResponse":
        """<p>Returns a list of versions for a specified contact.</p>

        Args:
            contact_id: <p>UUID of a contact.</p>
            max_results: <p>Maximum number of contact versions returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListContactVersions</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_contact_versions_request.ListContactVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_contact_versions_response.ListContactVersionsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_contact_versions

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_contact_versions.async_list_contact_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_groundstation.types.list_contact_versions_request.ListContactVersionsRequest = {
            "contact_id": contact_id
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
