from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_iotfleetwise._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iotfleetwise.types.create_signal_catalog_request
    import capo_iotfleetwise.types.create_signal_catalog_response
    import capo_iotfleetwise.types.delete_signal_catalog_request
    import capo_iotfleetwise.types.delete_signal_catalog_response
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.formatted_vss
    import capo_iotfleetwise.types.get_signal_catalog_request
    import capo_iotfleetwise.types.get_signal_catalog_response
    import capo_iotfleetwise.types.import_signal_catalog_request
    import capo_iotfleetwise.types.import_signal_catalog_response
    import capo_iotfleetwise.types.list_signal_catalog_nodes_request
    import capo_iotfleetwise.types.list_signal_catalog_nodes_response
    import capo_iotfleetwise.types.list_signal_catalogs_request
    import capo_iotfleetwise.types.list_signal_catalogs_response
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.node
    import capo_iotfleetwise.types.node_paths
    import capo_iotfleetwise.types.nodes
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.signal_catalog_summary
    import capo_iotfleetwise.types.signal_node_type
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.update_signal_catalog_request
    import capo_iotfleetwise.types.update_signal_catalog_response
    from capo_iotfleetwise._services.async_io_t_fleet_wise import (
        AsyncIoTFleetWiseClient,
        AsyncIoTFleetWiseClientConfig,
    )
    from capo_iotfleetwise._services.io_t_fleet_wise import (
        IoTFleetWiseClient,
        IoTFleetWiseClientConfig,
    )


class SignalCatalogResource:
    def __init__(self, service: IoTFleetWiseClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        nodes: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_signal_catalog_response.CreateSignalCatalogResponse":
        """<p> Creates a collection of standardized signals that can be reused to create vehicle models.</p>

        Args:
            name: <p> The name of the signal catalog to create. </p>
            description: <p>A brief description of the signal catalog.</p>
            nodes: <p> A list of information about nodes, which are a general abstraction of signals. For more information, see the API data type.</p>
            tags: <p>Metadata that can be used to manage the signal catalog.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_node_exception.InvalidNodeException: <p>The specified node type doesn't match the expected node type for a node. You can specify the node type as branch, sensor, actuator, or attribute.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.create_signal_catalog_request.CreateSignalCatalogRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.create_signal_catalog_response.CreateSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_signal_catalog

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_signal_catalog.create_signal_catalog(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateSignalCatalog")
        )
        input_: capo_iotfleetwise.types.create_signal_catalog_request.CreateSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes is not None:
            input_["nodes"] = nodes
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
    ) -> "capo_iotfleetwise.types.get_signal_catalog_response.GetSignalCatalogResponse":
        """<p> Retrieves information about a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.get_signal_catalog_request.GetSignalCatalogRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.get_signal_catalog_response.GetSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_signal_catalog

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_signal_catalog.get_signal_catalog(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSignalCatalog")
        )
        input_: capo_iotfleetwise.types.get_signal_catalog_request.GetSignalCatalogRequest = {
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
        nodes_to_add: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        nodes_to_update: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        nodes_to_remove: Optional[
            "capo_iotfleetwise.types.node_paths.NodePaths"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_signal_catalog_response.UpdateSignalCatalogResponse":
        """<p> Updates a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to update. </p>
            description: <p> A brief description of the signal catalog to update.</p>
            nodes_to_add: <p> A list of information about nodes to add to the signal catalog. </p>
            nodes_to_update: <p> A list of information about nodes to update in the signal catalog. </p>
            nodes_to_remove: <p> A list of <code>fullyQualifiedName</code> of nodes to remove from the signal catalog. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_node_exception.InvalidNodeException: <p>The specified node type doesn't match the expected node type for a node. You can specify the node type as branch, sensor, actuator, or attribute.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.update_signal_catalog_request.UpdateSignalCatalogRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.update_signal_catalog_response.UpdateSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_signal_catalog

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_signal_catalog.update_signal_catalog(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateSignalCatalog")
        )
        input_: capo_iotfleetwise.types.update_signal_catalog_request.UpdateSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes_to_add is not None:
            input_["nodes_to_add"] = nodes_to_add
        if nodes_to_update is not None:
            input_["nodes_to_update"] = nodes_to_update
        if nodes_to_remove is not None:
            input_["nodes_to_remove"] = nodes_to_remove

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
    ) -> "capo_iotfleetwise.types.delete_signal_catalog_response.DeleteSignalCatalogResponse":
        """<p> Deletes a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.delete_signal_catalog_request.DeleteSignalCatalogRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.delete_signal_catalog_response.DeleteSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_signal_catalog

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_signal_catalog.delete_signal_catalog(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSignalCatalog")
        )
        input_: capo_iotfleetwise.types.delete_signal_catalog_request.DeleteSignalCatalogRequest = {
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
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_signal_catalogs_response.ListSignalCatalogsResponse":
        """<p> Lists all the created signal catalogs in an Amazon Web Services account. </p> <p>You can use to list information about each signal (node) specified in a signal catalog.</p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_signal_catalogs_request.ListSignalCatalogsRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_signal_catalogs_response.ListSignalCatalogsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalogs

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalogs.list_signal_catalogs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSignalCatalogs")
        )
        input_: capo_iotfleetwise.types.list_signal_catalogs_request.ListSignalCatalogsRequest = {}
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

    def import_signal_catalog(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        vss: Optional["capo_iotfleetwise.types.formatted_vss.FormattedVss"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.import_signal_catalog_response.ImportSignalCatalogResponse":
        """<p> Creates a signal catalog using your existing VSS formatted content from your local device. </p>

        Args:
            name: <p>The name of the signal catalog to import.</p>
            description: <p> A brief description of the signal catalog. </p>
            vss: <p>The contents of the Vehicle Signal Specification (VSS) configuration. VSS is a precise language used to describe and model signals in vehicle networks.</p>
            tags: <p>Metadata that can be used to manage the signal catalog.</p>

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
            req: "OperationRequest[capo_iotfleetwise.types.import_signal_catalog_request.ImportSignalCatalogRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.import_signal_catalog_response.ImportSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_signal_catalog

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_signal_catalog.import_signal_catalog(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ImportSignalCatalog")
        )
        input_: capo_iotfleetwise.types.import_signal_catalog_request.ImportSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if vss is not None:
            input_["vss"] = vss
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_signal_catalog_nodes(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        signal_node_type: Optional[
            "capo_iotfleetwise.types.signal_node_type.SignalNodeType"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_signal_catalog_nodes_response.ListSignalCatalogNodesResponse":
        """<p> Lists of information about the signals (nodes) specified in a signal catalog. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the signal catalog to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            signal_node_type: <p>The type of node in the signal catalog.</p>

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
            req: "OperationRequest[capo_iotfleetwise.types.list_signal_catalog_nodes_request.ListSignalCatalogNodesRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_signal_catalog_nodes_response.ListSignalCatalogNodesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalog_nodes

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalog_nodes.list_signal_catalog_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSignalCatalogNodes")
        )
        input_: capo_iotfleetwise.types.list_signal_catalog_nodes_request.ListSignalCatalogNodesRequest = {
            "name": name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if signal_node_type is not None:
            input_["signal_node_type"] = signal_node_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSignalCatalogResource:
    def __init__(self, service: AsyncIoTFleetWiseClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        nodes: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.create_signal_catalog_response.CreateSignalCatalogResponse":
        """<p> Creates a collection of standardized signals that can be reused to create vehicle models.</p>

        Args:
            name: <p> The name of the signal catalog to create. </p>
            description: <p>A brief description of the signal catalog.</p>
            nodes: <p> A list of information about nodes, which are a general abstraction of signals. For more information, see the API data type.</p>
            tags: <p>Metadata that can be used to manage the signal catalog.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_node_exception.InvalidNodeException: <p>The specified node type doesn't match the expected node type for a node. You can specify the node type as branch, sensor, actuator, or attribute.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.create_signal_catalog_request.CreateSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.create_signal_catalog_response.CreateSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_signal_catalog.async_create_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateSignalCatalog")
        )
        input_: capo_iotfleetwise.types.create_signal_catalog_request.CreateSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes is not None:
            input_["nodes"] = nodes
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
    ) -> "capo_iotfleetwise.types.get_signal_catalog_response.GetSignalCatalogResponse":
        """<p> Retrieves information about a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to retrieve information about. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.get_signal_catalog_request.GetSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.get_signal_catalog_response.GetSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_signal_catalog.async_get_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSignalCatalog")
        )
        input_: capo_iotfleetwise.types.get_signal_catalog_request.GetSignalCatalogRequest = {
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
        nodes_to_add: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        nodes_to_update: Optional["capo_iotfleetwise.types.nodes.Nodes"] = None,
        nodes_to_remove: Optional[
            "capo_iotfleetwise.types.node_paths.NodePaths"
        ] = None,
    ) -> "capo_iotfleetwise.types.update_signal_catalog_response.UpdateSignalCatalogResponse":
        """<p> Updates a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to update. </p>
            description: <p> A brief description of the signal catalog to update.</p>
            nodes_to_add: <p> A list of information about nodes to add to the signal catalog. </p>
            nodes_to_update: <p> A list of information about nodes to update in the signal catalog. </p>
            nodes_to_remove: <p> A list of <code>fullyQualifiedName</code> of nodes to remove from the signal catalog. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.invalid_node_exception.InvalidNodeException: <p>The specified node type doesn't match the expected node type for a node. You can specify the node type as branch, sensor, actuator, or attribute.</p>
            capo_iotfleetwise.errors.invalid_signals_exception.InvalidSignalsException: <p>The request couldn't be completed because it contains signals that aren't valid.</p>
            capo_iotfleetwise.errors.limit_exceeded_exception.LimitExceededException: <p>A service quota was exceeded. </p>
            capo_iotfleetwise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource wasn't found.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.update_signal_catalog_request.UpdateSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.update_signal_catalog_response.UpdateSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_signal_catalog.async_update_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateSignalCatalog")
        )
        input_: capo_iotfleetwise.types.update_signal_catalog_request.UpdateSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if nodes_to_add is not None:
            input_["nodes_to_add"] = nodes_to_add
        if nodes_to_update is not None:
            input_["nodes_to_update"] = nodes_to_update
        if nodes_to_remove is not None:
            input_["nodes_to_remove"] = nodes_to_remove

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
    ) -> "capo_iotfleetwise.types.delete_signal_catalog_response.DeleteSignalCatalogResponse":
        """<p> Deletes a signal catalog. </p>

        Args:
            name: <p> The name of the signal catalog to delete. </p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.conflict_exception.ConflictException: <p>The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.delete_signal_catalog_request.DeleteSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.delete_signal_catalog_response.DeleteSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_signal_catalog.async_delete_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteSignalCatalog")
        )
        input_: capo_iotfleetwise.types.delete_signal_catalog_request.DeleteSignalCatalogRequest = {
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
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
    ) -> "capo_iotfleetwise.types.list_signal_catalogs_response.ListSignalCatalogsResponse":
        """<p> Lists all the created signal catalogs in an Amazon Web Services account. </p> <p>You can use to list information about each signal (node) specified in a signal catalog.</p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>

        Raises:
            capo_iotfleetwise.errors.internal_server_exception.InternalServerException: <p>The request couldn't be completed because the server temporarily failed.</p>
            capo_iotfleetwise.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_iotfleetwise.errors.throttling_exception.ThrottlingException: <p>The request couldn't be completed due to throttling.</p>
            capo_iotfleetwise.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_iotfleetwise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_signal_catalogs_request.ListSignalCatalogsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_signal_catalogs_response.ListSignalCatalogsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalogs

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalogs.async_list_signal_catalogs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSignalCatalogs")
        )
        input_: capo_iotfleetwise.types.list_signal_catalogs_request.ListSignalCatalogsRequest = {}
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

    async def import_signal_catalog(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        description: Optional["capo_iotfleetwise.types.description.description"] = None,
        vss: Optional["capo_iotfleetwise.types.formatted_vss.FormattedVss"] = None,
        tags: Optional["capo_iotfleetwise.types.tag_list.TagList"] = None,
    ) -> "capo_iotfleetwise.types.import_signal_catalog_response.ImportSignalCatalogResponse":
        """<p> Creates a signal catalog using your existing VSS formatted content from your local device. </p>

        Args:
            name: <p>The name of the signal catalog to import.</p>
            description: <p> A brief description of the signal catalog. </p>
            vss: <p>The contents of the Vehicle Signal Specification (VSS) configuration. VSS is a precise language used to describe and model signals in vehicle networks.</p>
            tags: <p>Metadata that can be used to manage the signal catalog.</p>

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
            req: "AsyncOperationRequest[capo_iotfleetwise.types.import_signal_catalog_request.ImportSignalCatalogRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.import_signal_catalog_response.ImportSignalCatalogResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_signal_catalog

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.import_signal_catalog.async_import_signal_catalog(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ImportSignalCatalog")
        )
        input_: capo_iotfleetwise.types.import_signal_catalog_request.ImportSignalCatalogRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if vss is not None:
            input_["vss"] = vss
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_signal_catalog_nodes(
        self,
        name: "capo_iotfleetwise.types.resource_name.resourceName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
        next_token: Optional["capo_iotfleetwise.types.next_token.nextToken"] = None,
        max_results: Optional["capo_iotfleetwise.types.max_results.maxResults"] = None,
        signal_node_type: Optional[
            "capo_iotfleetwise.types.signal_node_type.SignalNodeType"
        ] = None,
    ) -> "capo_iotfleetwise.types.list_signal_catalog_nodes_response.ListSignalCatalogNodesResponse":
        """<p> Lists of information about the signals (nodes) specified in a signal catalog. </p> <note> <p>This API operation uses pagination. Specify the <code>nextToken</code> parameter in the request to return more results.</p> </note>

        Args:
            name: <p> The name of the signal catalog to list information about. </p>
            next_token: <p>A pagination token for the next set of results.</p> <p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next set of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value. </p>
            max_results: <p>The maximum number of items to return, between 1 and 100, inclusive.</p>
            signal_node_type: <p>The type of node in the signal catalog.</p>

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
            req: "AsyncOperationRequest[capo_iotfleetwise.types.list_signal_catalog_nodes_request.ListSignalCatalogNodesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotfleetwise.types.list_signal_catalog_nodes_response.ListSignalCatalogNodesResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalog_nodes

            (
                output,
                http_response,
            ) = await capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_signal_catalog_nodes.async_list_signal_catalog_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSignalCatalogNodes")
        )
        input_: capo_iotfleetwise.types.list_signal_catalog_nodes_request.ListSignalCatalogNodesRequest = {
            "name": name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if signal_node_type is not None:
            input_["signal_node_type"] = signal_node_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
