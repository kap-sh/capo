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
    import capo_groundstation.types.config_capability_type
    import capo_groundstation.types.config_id_response
    import capo_groundstation.types.config_list_item
    import capo_groundstation.types.config_type_data
    import capo_groundstation.types.create_config_request
    import capo_groundstation.types.delete_config_request
    import capo_groundstation.types.get_config_request
    import capo_groundstation.types.get_config_response
    import capo_groundstation.types.list_configs_request
    import capo_groundstation.types.list_configs_response
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.update_config_request
    import capo_groundstation.types.uuid
    from capo_groundstation._services.async_ground_station import (
        AsyncGroundStationClient,
        AsyncGroundStationClientConfig,
    )
    from capo_groundstation._services.ground_station import (
        GroundStationClient,
        GroundStationClientConfig,
    )


class Config:
    def __init__(self, service: GroundStationClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_groundstation.types.safe_name.SafeName",
        config_data: "capo_groundstation.types.config_type_data.ConfigTypeData",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Creates a <code>Config</code> with the specified <code>configData</code> parameters.</p> <p>Only one type of <code>configData</code> can be specified.</p>

        Args:
            name: <p>Name of a <code>Config</code>.</p>
            config_data: <p>Parameters of a <code>Config</code>.</p>
            tags: <p>Tags assigned to a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.create_config_request.CreateConfigRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.create_config

            output, http_response = (
                capo_groundstation._operations.ground_station.create_config.create_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfig")
        )
        input_: capo_groundstation.types.create_config_request.CreateConfigRequest = {
            "name": name,
            "config_data": config_data,
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
        config_id: "capo_groundstation.types.uuid.Uuid",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_config_response.GetConfigResponse":
        """<p>Returns <code>Config</code> information.</p> <p>Only one <code>Config</code> response can be returned.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.get_config_request.GetConfigRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.get_config_response.GetConfigResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_config

            output, http_response = (
                capo_groundstation._operations.ground_station.get_config.get_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfig")
        )
        input_: capo_groundstation.types.get_config_request.GetConfigRequest = {
            "config_id": config_id,
            "config_type": config_type,
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
        config_id: "capo_groundstation.types.uuid.Uuid",
        name: "capo_groundstation.types.safe_name.SafeName",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        config_data: "capo_groundstation.types.config_type_data.ConfigTypeData",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Updates the <code>Config</code> used when scheduling contacts.</p> <p>Updating a <code>Config</code> will not update the execution parameters for existing future contacts scheduled with this <code>Config</code>.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            name: <p>Name of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>
            config_data: <p>Parameters of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.update_config_request.UpdateConfigRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_config

            output, http_response = (
                capo_groundstation._operations.ground_station.update_config.update_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfig")
        )
        input_: capo_groundstation.types.update_config_request.UpdateConfigRequest = {
            "config_id": config_id,
            "name": name,
            "config_type": config_type,
            "config_data": config_data,
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
        config_id: "capo_groundstation.types.uuid.Uuid",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        *,
        config_overrides: Optional[GroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Deletes a <code>Config</code>.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.delete_config_request.DeleteConfigRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.delete_config

            output, http_response = (
                capo_groundstation._operations.ground_station.delete_config.delete_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfig")
        )
        input_: capo_groundstation.types.delete_config_request.DeleteConfigRequest = {
            "config_id": config_id,
            "config_type": config_type,
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
    ) -> "capo_groundstation.types.list_configs_response.ListConfigsResponse":
        """<p>Returns a list of <code>Config</code> objects.</p>

        Args:
            max_results: <p>Maximum number of <code>Configs</code> returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListConfigs</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_groundstation.types.list_configs_request.ListConfigsRequest]",
        ) -> OperationResponse[
            "capo_groundstation.types.list_configs_response.ListConfigsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_configs

            output, http_response = (
                capo_groundstation._operations.ground_station.list_configs.list_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfigs")
        )
        input_: capo_groundstation.types.list_configs_request.ListConfigsRequest = {}
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


class AsyncConfig:
    def __init__(self, service: AsyncGroundStationClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_groundstation.types.safe_name.SafeName",
        config_data: "capo_groundstation.types.config_type_data.ConfigTypeData",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
        tags: Optional["capo_groundstation.types.tags_map.TagsMap"] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Creates a <code>Config</code> with the specified <code>configData</code> parameters.</p> <p>Only one type of <code>configData</code> can be specified.</p>

        Args:
            name: <p>Name of a <code>Config</code>.</p>
            config_data: <p>Parameters of a <code>Config</code>.</p>
            tags: <p>Tags assigned to a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Account limits for this resource have been exceeded.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.create_config_request.CreateConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.create_config

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.create_config.async_create_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfig")
        )
        input_: capo_groundstation.types.create_config_request.CreateConfigRequest = {
            "name": name,
            "config_data": config_data,
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
        config_id: "capo_groundstation.types.uuid.Uuid",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.get_config_response.GetConfigResponse":
        """<p>Returns <code>Config</code> information.</p> <p>Only one <code>Config</code> response can be returned.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.get_config_request.GetConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.get_config_response.GetConfigResponse"
        ]:
            import capo_groundstation._operations.ground_station.get_config

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.get_config.async_get_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfig")
        )
        input_: capo_groundstation.types.get_config_request.GetConfigRequest = {
            "config_id": config_id,
            "config_type": config_type,
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
        config_id: "capo_groundstation.types.uuid.Uuid",
        name: "capo_groundstation.types.safe_name.SafeName",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        config_data: "capo_groundstation.types.config_type_data.ConfigTypeData",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Updates the <code>Config</code> used when scheduling contacts.</p> <p>Updating a <code>Config</code> will not update the execution parameters for existing future contacts scheduled with this <code>Config</code>.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            name: <p>Name of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>
            config_data: <p>Parameters of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.update_config_request.UpdateConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.update_config

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.update_config.async_update_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfig")
        )
        input_: capo_groundstation.types.update_config_request.UpdateConfigRequest = {
            "config_id": config_id,
            "name": name,
            "config_type": config_type,
            "config_data": config_data,
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
        config_id: "capo_groundstation.types.uuid.Uuid",
        config_type: "capo_groundstation.types.config_capability_type.ConfigCapabilityType",
        *,
        config_overrides: Optional[AsyncGroundStationClientConfig] = None,
    ) -> "capo_groundstation.types.config_id_response.ConfigIdResponse":
        """<p>Deletes a <code>Config</code>.</p>

        Args:
            config_id: <p>UUID of a <code>Config</code>.</p>
            config_type: <p>Type of a <code>Config</code>.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.delete_config_request.DeleteConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.config_id_response.ConfigIdResponse"
        ]:
            import capo_groundstation._operations.ground_station.delete_config

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.delete_config.async_delete_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfig")
        )
        input_: capo_groundstation.types.delete_config_request.DeleteConfigRequest = {
            "config_id": config_id,
            "config_type": config_type,
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
    ) -> "capo_groundstation.types.list_configs_response.ListConfigsResponse":
        """<p>Returns a list of <code>Config</code> objects.</p>

        Args:
            max_results: <p>Maximum number of <code>Configs</code> returned.</p>
            next_token: <p>Next token returned in the request of a previous <code>ListConfigs</code> call. Used to get the next page of results.</p>

        Raises:
            capo_groundstation.errors.dependency_exception.DependencyException: <p>Dependency encountered an error.</p>
            capo_groundstation.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters are not valid.</p>
            capo_groundstation.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_groundstation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_groundstation.types.list_configs_request.ListConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_groundstation.types.list_configs_response.ListConfigsResponse"
        ]:
            import capo_groundstation._operations.ground_station.list_configs

            (
                output,
                http_response,
            ) = await capo_groundstation._operations.ground_station.list_configs.async_list_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfigs")
        )
        input_: capo_groundstation.types.list_configs_request.ListConfigsRequest = {}
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
