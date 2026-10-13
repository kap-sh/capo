from __future__ import annotations

import datetime
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
    import capo_groundstation.types.antenna_list_item
    import capo_groundstation.types.ground_station_data
    import capo_groundstation.types.ground_station_name
    import capo_groundstation.types.ground_station_reservation_list_item
    import capo_groundstation.types.list_antennas_request
    import capo_groundstation.types.list_antennas_response
    import capo_groundstation.types.list_ground_station_reservations_request
    import capo_groundstation.types.list_ground_station_reservations_response
    import capo_groundstation.types.list_ground_stations_request
    import capo_groundstation.types.list_ground_stations_response
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.reservation_type_filter_list
    import capo_groundstation.types.uuid
    from capo_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from capo_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class GroundStationResource:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        satellite_id: Optional["capo_groundstation.types.uuid.Uuid"] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_ground_stations_response.ListGroundStationsResponse":
        """<p>Returns a list of ground stations. </p>

        Args:
            satellite_id: <p>Satellite ID to retrieve on-boarded ground stations.</p>
            max_results: <p>Maximum number of ground stations returned.</p>
            next_token: <p>Next token that can be supplied in the next call to get the next page of ground stations.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.list_ground_stations_request.ListGroundStationsRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.list_ground_stations_response.ListGroundStationsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_ground_stations

            output, http_response = (
                capo_groundstation._operations.ground_station.list_ground_stations.list_ground_stations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGroundStations")
        )
        input_: capo_groundstation.types.list_ground_stations_request.ListGroundStationsRequest = {}
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
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

    def list_antennas(
        self,
        ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_antennas_response.ListAntennasResponse":
        """<p>Returns a list of antennas at a specified ground station.</p>

        Args:
            ground_station_id: <p>ID of a ground station.</p>
            max_results: <p>Maximum number of antennas returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListAntennas</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.list_antennas_request.ListAntennasRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.list_antennas_response.ListAntennasResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_antennas

            output, http_response = (
                capo_groundstation._operations.ground_station.list_antennas.list_antennas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAntennas")
        )
        input_: capo_groundstation.types.list_antennas_request.ListAntennasRequest = {
            "ground_station_id": ground_station_id
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

    def list_ground_station_reservations(
        self,
        ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        reservation_types: Optional[
            "capo_groundstation.types.reservation_type_filter_list.ReservationTypeFilterList"
        ] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_ground_station_reservations_response.ListGroundStationReservationsResponse":
        """<p>Returns a list of reservations for a specified ground station.</p>

        Args:
            ground_station_id: <p>ID of a ground station.</p>
            start_time: <p>Start time of the reservation window in UTC.</p>
            end_time: <p>End time of the reservation window in UTC.</p>
            reservation_types: <p>Types of reservations to filter by.</p>
            max_results: <p>Maximum number of ground station reservations returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListGroundStationReservations</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.list_ground_station_reservations_request.ListGroundStationReservationsRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.list_ground_station_reservations_response.ListGroundStationReservationsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_ground_station_reservations

            output, http_response = (
                capo_groundstation._operations.ground_station.list_ground_station_reservations.list_ground_station_reservations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGroundStationReservations")
        )
        input_: capo_groundstation.types.list_ground_station_reservations_request.ListGroundStationReservationsRequest = {
            "ground_station_id": ground_station_id,
            "start_time": start_time,
            "end_time": end_time,
        }
        if reservation_types is not None:
            input_["reservation_types"] = reservation_types
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


class AsyncGroundStationResource:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        satellite_id: Optional["capo_groundstation.types.uuid.Uuid"] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_ground_stations_response.ListGroundStationsResponse":
        """<p>Returns a list of ground stations. </p>

        Args:
            satellite_id: <p>Satellite ID to retrieve on-boarded ground stations.</p>
            max_results: <p>Maximum number of ground stations returned.</p>
            next_token: <p>Next token that can be supplied in the next call to get the next page of ground stations.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_ground_stations_request.ListGroundStationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_ground_stations_response.ListGroundStationsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_ground_stations

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_ground_stations.async_list_ground_stations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGroundStations")
        )
        input_: capo_groundstation.types.list_ground_stations_request.ListGroundStationsRequest = {}
        if satellite_id is not None:
            input_["satellite_id"] = satellite_id
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

    async def list_antennas(
        self,
        ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_antennas_response.ListAntennasResponse":
        """<p>Returns a list of antennas at a specified ground station.</p>

        Args:
            ground_station_id: <p>ID of a ground station.</p>
            max_results: <p>Maximum number of antennas returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListAntennas</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_antennas_request.ListAntennasRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_antennas_response.ListAntennasResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_antennas

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_antennas.async_list_antennas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAntennas")
        )
        input_: capo_groundstation.types.list_antennas_request.ListAntennasRequest = {
            "ground_station_id": ground_station_id
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

    async def list_ground_station_reservations(
        self,
        ground_station_id: "capo_groundstation.types.ground_station_name.GroundStationName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        reservation_types: Optional[
            "capo_groundstation.types.reservation_type_filter_list.ReservationTypeFilterList"
        ] = None,
        max_results: Optional[
            "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_groundstation.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_groundstation.types.list_ground_station_reservations_response.ListGroundStationReservationsResponse":
        """<p>Returns a list of reservations for a specified ground station.</p>

        Args:
            ground_station_id: <p>ID of a ground station.</p>
            start_time: <p>Start time of the reservation window in UTC.</p>
            end_time: <p>End time of the reservation window in UTC.</p>
            reservation_types: <p>Types of reservations to filter by.</p>
            max_results: <p>Maximum number of ground station reservations returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListGroundStationReservations</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_ground_station_reservations_request.ListGroundStationReservationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_ground_station_reservations_response.ListGroundStationReservationsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_ground_station_reservations

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_ground_station_reservations.async_list_ground_station_reservations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGroundStationReservations")
        )
        input_: capo_groundstation.types.list_ground_station_reservations_request.ListGroundStationReservationsRequest = {
            "ground_station_id": ground_station_id,
            "start_time": start_time,
            "end_time": end_time,
        }
        if reservation_types is not None:
            input_["reservation_types"] = reservation_types
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
