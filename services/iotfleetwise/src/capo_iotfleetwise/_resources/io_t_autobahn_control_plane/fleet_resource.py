from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_iotfleetwise._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.create_fleet_request
    import capo_iotfleetwise.types.create_fleet_response
    import capo_iotfleetwise.types.delete_fleet_request
    import capo_iotfleetwise.types.delete_fleet_response
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.fleet_id
    import capo_iotfleetwise.types.fleet_summary
    import capo_iotfleetwise.types.get_fleet_request
    import capo_iotfleetwise.types.get_fleet_response
    import capo_iotfleetwise.types.list_fleets_request
    import capo_iotfleetwise.types.list_fleets_response
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.update_fleet_request
    import capo_iotfleetwise.types.update_fleet_response
    from capo_iotfleetwise._services.async_io_t_fleet_wise import (
        AsyncIoTFleetWiseClient,
        AsyncIoTFleetWiseClientConfig,
    )
    from capo_iotfleetwise._services.io_t_fleet_wise import (
        IoTFleetWiseClient,
        IoTFleetWiseClientConfig,
    )


class FleetResource:
    def __init__(self, service: IoTFleetWiseClient) -> None:
        self._service = service

    def put(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_fleet_response.CreateFleetResponse":
        """<p> Creates a fleet that represents a group of vehicles. </p> <note> <p>You must create both a signal catalog and vehicles before you can create a fleet. </p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html">Fleets</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The unique ID of the fleet to create. </p>
            description: <p> A brief description of the fleet to create. </p>
            signal_catalog_arn: <p> The Amazon Resource Name (ARN) of a signal catalog. </p>
            tags: <p>Metadata that can be used to manage the fleet.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.create_fleet_request.CreateFleetRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.create_fleet_response.CreateFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet.create_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_fleet_request.CreateFleetRequest = {
            "fleet_id": fleet_id,
            "signal_catalog_arn": signal_catalog_arn,
        }
        if description is not None:
            input_["description"] = description
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
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_fleet_response.GetFleetResponse":
        """<p> Retrieves information about a fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.get_fleet_request.GetFleetRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.get_fleet_response.GetFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet.get_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_fleet_request.GetFleetRequest = {
            "fleet_id": fleet_id
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
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
    ) -> "capo_iotfleetwise.types.update_fleet_response.UpdateFleetResponse":
        """<p> Updates the description of an existing fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to update. </p>
            description: <p> An updated description of the fleet. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.update_fleet_request.UpdateFleetRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.update_fleet_response.UpdateFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet.update_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_fleet_request.UpdateFleetRequest = {
            "fleet_id": fleet_id
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse":
        """<p> Deletes a fleet. Before you delete a fleet, all vehicles must be dissociated from the fleet. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-fleet-cli.html">Delete a fleet (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The ID of the fleet to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet.delete_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest = {
            "fleet_id": fleet_id
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
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_fleets_response.ListFleetsResponse":
        """<p> Retrieves information for each created fleet in an Amazon Web Services account. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: fleet ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_fleets_request.ListFleetsRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_fleets_response.ListFleetsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets.list_fleets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_fleets_request.ListFleetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFleetResource:
    def __init__(self, service: AsyncIoTFleetWiseClient) -> None:
        self._service = service

    async def put(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_fleet_response.CreateFleetResponse":
        """<p> Creates a fleet that represents a group of vehicles. </p> <note> <p>You must create both a signal catalog and vehicles before you can create a fleet. </p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html">Fleets</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The unique ID of the fleet to create. </p>
            description: <p> A brief description of the fleet to create. </p>
            signal_catalog_arn: <p> The Amazon Resource Name (ARN) of a signal catalog. </p>
            tags: <p>Metadata that can be used to manage the fleet.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_fleet_request.CreateFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_fleet_response.CreateFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_fleet.async_create_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_fleet_request.CreateFleetRequest = {
            "fleet_id": fleet_id,
            "signal_catalog_arn": signal_catalog_arn,
        }
        if description is not None:
            input_["description"] = description
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
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_fleet_response.GetFleetResponse":
        """<p> Retrieves information about a fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_fleet_request.GetFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_fleet_response.GetFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_fleet.async_get_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_fleet_request.GetFleetRequest = {
            "fleet_id": fleet_id
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
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
    ) -> "capo_iotfleetwise.types.update_fleet_response.UpdateFleetResponse":
        """<p> Updates the description of an existing fleet. </p>

        Args:
            fleet_id: <p> The ID of the fleet to update. </p>
            description: <p> An updated description of the fleet. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_fleet_request.UpdateFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_fleet_response.UpdateFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_fleet.async_update_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_fleet_request.UpdateFleetRequest = {
            "fleet_id": fleet_id
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse":
        """<p> Deletes a fleet. Before you delete a fleet, all vehicles must be dissociated from the fleet. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-fleet-cli.html">Delete a fleet (AWS CLI)</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            fleet_id: <p> The ID of the fleet to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_fleet_response.DeleteFleetResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_fleet.async_delete_fleet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_fleet_request.DeleteFleetRequest = {
            "fleet_id": fleet_id
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
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_fleets_response.ListFleetsResponse":
        """<p> Retrieves information for each created fleet in an Amazon Web Services account. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: fleet ID, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_fleets_request.ListFleetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_fleets_response.ListFleetsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_fleets.async_list_fleets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_fleets_request.ListFleetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
