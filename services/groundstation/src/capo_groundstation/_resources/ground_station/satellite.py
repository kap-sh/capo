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
    import capo_groundstation.types.get_satellite_request
    import capo_groundstation.types.get_satellite_response
    import capo_groundstation.types.list_satellites_request
    import capo_groundstation.types.list_satellites_response
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.satellite_list_item
    import capo_groundstation.types.uuid
    from capo_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from capo_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class Satellite:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def read(
        self,
        satellite_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_satellite_response.GetSatelliteResponse":
        """<p>Returns a satellite.</p>

        Args:
            satellite_id: <p>UUID of a satellite.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.get_satellite_request.GetSatelliteRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.get_satellite_response.GetSatelliteResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_satellite

            output, http_response = (
                capo_groundstation._operations.ground_station.get_satellite.get_satellite(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSatellite")
        )
        input_: capo_groundstation.types.get_satellite_request.GetSatelliteRequest = {
            "satellite_id": satellite_id
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
    ) -> "capo_groundstation.types.list_satellites_response.ListSatellitesResponse":
        """<p>Returns a list of satellites.</p>

        Args:
            max_results: <p>Maximum number of satellites returned.</p>
            next_token: <p>Next token that can be supplied in the next call to get the next page of satellites.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.list_satellites_request.ListSatellitesRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.list_satellites_response.ListSatellitesResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_satellites

            output, http_response = (
                capo_groundstation._operations.ground_station.list_satellites.list_satellites(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSatellites")
        )
        input_: capo_groundstation.types.list_satellites_request.ListSatellitesRequest = {}
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


class AsyncSatellite:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def read(
        self,
        satellite_id: "capo_groundstation.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_satellite_response.GetSatelliteResponse":
        """<p>Returns a satellite.</p>

        Args:
            satellite_id: <p>UUID of a satellite.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_satellite_request.GetSatelliteRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_satellite_response.GetSatelliteResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_satellite

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_satellite.async_get_satellite(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSatellite")
        )
        input_: capo_groundstation.types.get_satellite_request.GetSatelliteRequest = {
            "satellite_id": satellite_id
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
    ) -> "capo_groundstation.types.list_satellites_response.ListSatellitesResponse":
        """<p>Returns a list of satellites.</p>

        Args:
            max_results: <p>Maximum number of satellites returned.</p>
            next_token: <p>Next token that can be supplied in the next call to get the next page of satellites.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_satellites_request.ListSatellitesRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_satellites_response.ListSatellitesResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_satellites

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_satellites.async_list_satellites(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSatellites")
        )
        input_: capo_groundstation.types.list_satellites_request.ListSatellitesRequest = {}
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
