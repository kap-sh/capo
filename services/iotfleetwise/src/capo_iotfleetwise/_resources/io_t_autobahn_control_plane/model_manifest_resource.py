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
    import capo_iotfleetwise.types.create_model_manifest_request
    import capo_iotfleetwise.types.create_model_manifest_response
    import capo_iotfleetwise.types.delete_model_manifest_request
    import capo_iotfleetwise.types.delete_model_manifest_response
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.get_model_manifest_request
    import capo_iotfleetwise.types.get_model_manifest_response
    import capo_iotfleetwise.types.list_model_manifest_nodes_request
    import capo_iotfleetwise.types.list_model_manifest_nodes_response
    import capo_iotfleetwise.types.list_model_manifests_request
    import capo_iotfleetwise.types.list_model_manifests_response
    import capo_iotfleetwise.types.list_of_strings
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.manifest_status
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.model_manifest_summary
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.node
    import capo_iotfleetwise.types.node_paths
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.update_model_manifest_request
    import capo_iotfleetwise.types.update_model_manifest_response
    from capo_iotfleetwise._services.async_io_t_fleet_wise import (
        AsyncIoTFleetWiseClient,
        AsyncIoTFleetWiseClientConfig,
    )
    from capo_iotfleetwise._services.io_t_fleet_wise import (
        IoTFleetWiseClient,
        IoTFleetWiseClientConfig,
    )


class ModelManifestResource:
    def __init__(self, service: IoTFleetWiseClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        nodes: "capo_iotfleetwise.types.list_of_strings.listOfStrings",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_model_manifest_response.CreateModelManifestResponse":
        """<p> Creates a vehicle model (model manifest) that specifies signals (attributes, branches, sensors, and actuators). </p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-models.html">Vehicle models</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            name: <p> The name of the vehicle model to create.</p>
            description: <p> A brief description of the vehicle model. </p>
            nodes: <p> A list of nodes, which are a general abstraction of signals. </p>
            signal_catalog_arn: <p> The Amazon Resource Name (ARN) of a signal catalog. </p>
            tags: <p>Metadata that can be used to manage the vehicle model.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.create_model_manifest_request.CreateModelManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.create_model_manifest_response.CreateModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_model_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_model_manifest.create_model_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_model_manifest_request.CreateModelManifestRequest = {
            "name": name,
            "nodes": nodes,
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
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_model_manifest_response.GetModelManifestResponse":
        """<p> Retrieves information about a vehicle model (model manifest). </p>

        Args:
            name: <p> The name of the vehicle model to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.get_model_manifest_request.GetModelManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.get_model_manifest_response.GetModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_model_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_model_manifest.get_model_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_model_manifest_request.GetModelManifestRequest = {
            "name": name
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
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        nodes_to_add: Optional["capo_iotfleetwise.types.node_paths.NodePaths"] = None,
        nodes_to_remove: Optional[
            "capo_iotfleetwise.types.node_paths.NodePaths"
        ] = None,
        status: Optional[
            "capo_iotfleetwise.types.manifest_status.ManifestStatus"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_model_manifest_response.UpdateModelManifestResponse":
        """<p> Updates a vehicle model (model manifest). If created vehicles are associated with a vehicle model, it can't be updated.</p>

        Args:
            name: <p> The name of the vehicle model to update. </p>
            description: <p> A brief description of the vehicle model. </p>
            nodes_to_add: <p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to add to the vehicle model. </p>
            nodes_to_remove: <p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to remove from the vehicle model. </p>
            status: <p> The state of the vehicle model. If the status is <code>ACTIVE</code>, the vehicle model can't be edited. If the status is <code>DRAFT</code>, you can edit the vehicle model. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.update_model_manifest_request.UpdateModelManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.update_model_manifest_response.UpdateModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_model_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_model_manifest.update_model_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_model_manifest_request.UpdateModelManifestRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes_to_add is not None:
            input_["nodes_to_add"] = nodes_to_add
        if nodes_to_remove is not None:
            input_["nodes_to_remove"] = nodes_to_remove
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_model_manifest_response.DeleteModelManifestResponse":
        """<p> Deletes a vehicle model (model manifest).</p>

        Args:
            name: <p> The name of the model manifest to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.delete_model_manifest_request.DeleteModelManifestRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.delete_model_manifest_response.DeleteModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_model_manifest

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_model_manifest.delete_model_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_model_manifest_request.DeleteModelManifestRequest = {
            "name": name
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
        signal_catalog_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_model_manifests_response.ListModelManifestsResponse":
        """<p> Retrieves a list of vehicle models (model manifests). </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            signal_catalog_arn: <p> The ARN of a signal catalog. If you specify a signal catalog, only the vehicle models associated with it are returned.</p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: model manifest name, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_model_manifests_request.ListModelManifestsRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_model_manifests_response.ListModelManifestsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifests

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifests.list_model_manifests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_model_manifests_request.ListModelManifestsRequest = {}
        if signal_catalog_arn is not None:
            input_["signal_catalog_arn"] = signal_catalog_arn
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

    def list_model_manifest_nodes(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_model_manifest_nodes_response.ListModelManifestNodesResponse":
        """<p> Lists information about nodes specified in a vehicle model (model manifest). </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the vehicle model to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_model_manifest_nodes_request.ListModelManifestNodesRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_model_manifest_nodes_response.ListModelManifestNodesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifest_nodes

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifest_nodes.list_model_manifest_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_model_manifest_nodes_request.ListModelManifestNodesRequest = {
            "name": name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncModelManifestResource:
    def __init__(self, service: AsyncIoTFleetWiseClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        nodes: "capo_iotfleetwise.types.list_of_strings.listOfStrings",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_model_manifest_response.CreateModelManifestResponse":
        """<p> Creates a vehicle model (model manifest) that specifies signals (attributes, branches, sensors, and actuators). </p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-models.html">Vehicle models</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p>

        Args:
            name: <p> The name of the vehicle model to create.</p>
            description: <p> A brief description of the vehicle model. </p>
            nodes: <p> A list of nodes, which are a general abstraction of signals. </p>
            signal_catalog_arn: <p> The Amazon Resource Name (ARN) of a signal catalog. </p>
            tags: <p>Metadata that can be used to manage the vehicle model.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_model_manifest_request.CreateModelManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_model_manifest_response.CreateModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_model_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_model_manifest.async_create_model_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.create_model_manifest_request.CreateModelManifestRequest = {
            "name": name,
            "nodes": nodes,
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
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_model_manifest_response.GetModelManifestResponse":
        """<p> Retrieves information about a vehicle model (model manifest). </p>

        Args:
            name: <p> The name of the vehicle model to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_model_manifest_request.GetModelManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_model_manifest_response.GetModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_model_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_model_manifest.async_get_model_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_model_manifest_request.GetModelManifestRequest = {
            "name": name
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
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        nodes_to_add: Optional["capo_iotfleetwise.types.node_paths.NodePaths"] = None,
        nodes_to_remove: Optional[
            "capo_iotfleetwise.types.node_paths.NodePaths"
        ] = None,
        status: Optional[
            "capo_iotfleetwise.types.manifest_status.ManifestStatus"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_model_manifest_response.UpdateModelManifestResponse":
        """<p> Updates a vehicle model (model manifest). If created vehicles are associated with a vehicle model, it can't be updated.</p>

        Args:
            name: <p> The name of the vehicle model to update. </p>
            description: <p> A brief description of the vehicle model. </p>
            nodes_to_add: <p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to add to the vehicle model. </p>
            nodes_to_remove: <p> A list of <code>fullyQualifiedName</code> of nodes, which are a general abstraction of signals, to remove from the vehicle model. </p>
            status: <p> The state of the vehicle model. If the status is <code>ACTIVE</code>, the vehicle model can't be edited. If the status is <code>DRAFT</code>, you can edit the vehicle model. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_model_manifest_request.UpdateModelManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_model_manifest_response.UpdateModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_model_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_model_manifest.async_update_model_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_model_manifest_request.UpdateModelManifestRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes_to_add is not None:
            input_["nodes_to_add"] = nodes_to_add
        if nodes_to_remove is not None:
            input_["nodes_to_remove"] = nodes_to_remove
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.delete_model_manifest_response.DeleteModelManifestResponse":
        """<p> Deletes a vehicle model (model manifest).</p>

        Args:
            name: <p> The name of the model manifest to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_model_manifest_request.DeleteModelManifestRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_model_manifest_response.DeleteModelManifestResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_model_manifest

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_model_manifest.async_delete_model_manifest(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_model_manifest_request.DeleteModelManifestRequest = {
            "name": name
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
        signal_catalog_arn: Optional["capo_iotfleetwise.types.arn.arn"] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        list_response_scope: Optional[
            "capo_iotfleetwise.types.list_response_scope.ListResponseScope"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_model_manifests_response.ListModelManifestsResponse":
        """<p> Retrieves a list of vehicle models (model manifests). </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            signal_catalog_arn: <p> The ARN of a signal catalog. If you specify a signal catalog, only the vehicle models associated with it are returned.</p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            list_response_scope: <p>When you set the <code>listResponseScope</code> parameter to <code>METADATA_ONLY</code>, the list response includes: model manifest name, Amazon Resource Name (ARN), creation time, and last modification time.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_model_manifests_request.ListModelManifestsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_model_manifests_response.ListModelManifestsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifests

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifests.async_list_model_manifests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_model_manifests_request.ListModelManifestsRequest = {}
        if signal_catalog_arn is not None:
            input_["signal_catalog_arn"] = signal_catalog_arn
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

    async def list_model_manifest_nodes(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_model_manifest_nodes_response.ListModelManifestNodesResponse":
        """<p> Lists information about nodes specified in a vehicle model (model manifest). </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the vehicle model to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_model_manifest_nodes_request.ListModelManifestNodesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_model_manifest_nodes_response.ListModelManifestNodesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifest_nodes

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_model_manifest_nodes.async_list_model_manifest_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_model_manifest_nodes_request.ListModelManifestNodesRequest = {
            "name": name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
