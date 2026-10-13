from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_neptune_graph._auth._signers
import capo_neptune_graph._auth._sigv4
from capo_neptune_graph._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_neptune_graph.types.create_graph_input
    import capo_neptune_graph.types.create_graph_output
    import capo_neptune_graph.types.delete_graph_input
    import capo_neptune_graph.types.delete_graph_output
    import capo_neptune_graph.types.get_graph_input
    import capo_neptune_graph.types.get_graph_output
    import capo_neptune_graph.types.graph_identifier
    import capo_neptune_graph.types.graph_name
    import capo_neptune_graph.types.graph_summary
    import capo_neptune_graph.types.kms_key_arn
    import capo_neptune_graph.types.list_graphs_input
    import capo_neptune_graph.types.list_graphs_output
    import capo_neptune_graph.types.max_results
    import capo_neptune_graph.types.pagination_token
    import capo_neptune_graph.types.provisioned_memory
    import capo_neptune_graph.types.replica_count
    import capo_neptune_graph.types.reset_graph_input
    import capo_neptune_graph.types.reset_graph_output
    import capo_neptune_graph.types.restore_graph_from_snapshot_input
    import capo_neptune_graph.types.restore_graph_from_snapshot_output
    import capo_neptune_graph.types.snapshot_identifier
    import capo_neptune_graph.types.start_graph_input
    import capo_neptune_graph.types.start_graph_output
    import capo_neptune_graph.types.stop_graph_input
    import capo_neptune_graph.types.stop_graph_output
    import capo_neptune_graph.types.tag_map
    import capo_neptune_graph.types.update_graph_input
    import capo_neptune_graph.types.update_graph_output
    import capo_neptune_graph.types.vector_search_configuration
    from capo_neptune_graph._services.async_neptune_graph import (
        AsyncNeptuneGraphClient,
        AsyncNeptuneGraphClientConfig,
    )
    from capo_neptune_graph._services.neptune_graph import (
        NeptuneGraphClient,
        NeptuneGraphClientConfig,
    )


class GraphResource:
    def __init__(self, service: NeptuneGraphClient) -> None:
        self._service = service

    def create_graph(
        self,
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        provisioned_memory: "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
        public_connectivity: Optional[bool] = None,
        kms_key_identifier: Optional[
            "capo_neptune_graph.types.kms_key_arn.KmsKeyArn"
        ] = None,
        vector_search_configuration: Optional[
            "capo_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
        ] = None,
        replica_count: Optional[
            "capo_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.create_graph_output.CreateGraphOutput":
        """<p>Creates a new Neptune Analytics graph.</p>

        Args:
            graph_name: <p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            kms_key_identifier: <p>Specifies a KMS key to use to encrypt data in the new graph.</p>
            vector_search_configuration: <p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default = 1.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            deletion_protection: <p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.create_graph_input.CreateGraphInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.create_graph_output.CreateGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.create_graph.create_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGraph")
        )
        input_: capo_neptune_graph.types.create_graph_input.CreateGraphInput = {
            "graph_name": graph_name,
            "provisioned_memory": provisioned_memory,
        }
        if tags is not None:
            input_["tags"] = tags
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if vector_search_configuration is not None:
            input_["vector_search_configuration"] = vector_search_configuration
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.delete_graph_output.DeleteGraphOutput":
        """<p>Deletes the specified graph. Graphs cannot be deleted if delete-protection is enabled.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph is deleted. If <code>true</code> is specified, no graph snapshot is created. If <code>false</code> is specified, a graph snapshot is created before the graph is deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.delete_graph_input.DeleteGraphInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.delete_graph_output.DeleteGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.delete_graph

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.delete_graph.delete_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGraph")
        )
        input_: capo_neptune_graph.types.delete_graph_input.DeleteGraphInput = {
            "graph_identifier": graph_identifier,
            "skip_snapshot": skip_snapshot,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_graph_output.GetGraphOutput":
        """<p>Gets information about a specified graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.get_graph_input.GetGraphInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.get_graph_output.GetGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_graph

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.get_graph.get_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetGraph")
        )
        input_: capo_neptune_graph.types.get_graph_input.GetGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_graphs(
        self,
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "capo_neptune_graph.types.list_graphs_output.ListGraphsOutput":
        """<p>Lists available Neptune Analytics graphs.</p>

        Args:
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.list_graphs_input.ListGraphsInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.list_graphs_output.ListGraphsOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_graphs

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.list_graphs.list_graphs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGraphs")
        )
        input_: capo_neptune_graph.types.list_graphs_input.ListGraphsInput = {}
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

    def reset_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.reset_graph_output.ResetGraphOutput":
        """<p>Empties the data from a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>ID of the graph to reset.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph data is deleted. If set to <code>true</code>, no graph snapshot is created. If set to <code>false</code>, a graph snapshot is created before the data is deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.reset_graph_input.ResetGraphInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.reset_graph_output.ResetGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.reset_graph

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.reset_graph.reset_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ResetGraph")
        )
        input_: capo_neptune_graph.types.reset_graph_input.ResetGraphInput = {
            "graph_identifier": graph_identifier,
            "skip_snapshot": skip_snapshot,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_graph_from_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
        replica_count: Optional[
            "capo_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        public_connectivity: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput":
        """<p>Restores a graph from a snapshot.</p>

        Args:
            snapshot_identifier: <p>The ID of the snapshot in question.</p>
            graph_name: <p>A name for the new Neptune Analytics graph to be created from the snapshot.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>
            tags: <p>Adds metadata tags to the snapshot. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default =1</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot.restore_graph_from_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestoreGraphFromSnapshot")
        )
        input_: capo_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput = {
            "snapshot_identifier": snapshot_identifier,
            "graph_name": graph_name,
        }
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if tags is not None:
            input_["tags"] = tags
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.start_graph_output.StartGraphOutput":
        """<p>Starts the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.start_graph_input.StartGraphInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.start_graph_output.StartGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_graph

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.start_graph.start_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartGraph")
        )
        input_: capo_neptune_graph.types.start_graph_input.StartGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.stop_graph_output.StopGraphOutput":
        """<p>Stops the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.stop_graph_input.StopGraphInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.stop_graph_output.StopGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.stop_graph

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.stop_graph.stop_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopGraph")
        )
        input_: capo_neptune_graph.types.stop_graph_input.StopGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        public_connectivity: Optional[bool] = None,
        provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.update_graph_output.UpdateGraphOutput":
        """<p>Updates the configuration of a specified Neptune Analytics graph</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.update_graph_input.UpdateGraphInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.update_graph_output.UpdateGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.update_graph

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.update_graph.update_graph(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGraph")
        )
        input_: capo_neptune_graph.types.update_graph_input.UpdateGraphInput = {
            "graph_identifier": graph_identifier
        }
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGraphResource:
    def __init__(self, service: AsyncNeptuneGraphClient) -> None:
        self._service = service

    async def create_graph(
        self,
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        provisioned_memory: "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
        public_connectivity: Optional[bool] = None,
        kms_key_identifier: Optional[
            "capo_neptune_graph.types.kms_key_arn.KmsKeyArn"
        ] = None,
        vector_search_configuration: Optional[
            "capo_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
        ] = None,
        replica_count: Optional[
            "capo_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.create_graph_output.CreateGraphOutput":
        """<p>Creates a new Neptune Analytics graph.</p>

        Args:
            graph_name: <p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            kms_key_identifier: <p>Specifies a KMS key to use to encrypt data in the new graph.</p>
            vector_search_configuration: <p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default = 1.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            deletion_protection: <p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.create_graph_input.CreateGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.create_graph_output.CreateGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.create_graph.async_create_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGraph")
        )
        input_: capo_neptune_graph.types.create_graph_input.CreateGraphInput = {
            "graph_name": graph_name,
            "provisioned_memory": provisioned_memory,
        }
        if tags is not None:
            input_["tags"] = tags
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if vector_search_configuration is not None:
            input_["vector_search_configuration"] = vector_search_configuration
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.delete_graph_output.DeleteGraphOutput":
        """<p>Deletes the specified graph. Graphs cannot be deleted if delete-protection is enabled.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph is deleted. If <code>true</code> is specified, no graph snapshot is created. If <code>false</code> is specified, a graph snapshot is created before the graph is deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.delete_graph_input.DeleteGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.delete_graph_output.DeleteGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.delete_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.delete_graph.async_delete_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGraph")
        )
        input_: capo_neptune_graph.types.delete_graph_input.DeleteGraphInput = {
            "graph_identifier": graph_identifier,
            "skip_snapshot": skip_snapshot,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_graph_output.GetGraphOutput":
        """<p>Gets information about a specified graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_graph_input.GetGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_graph_output.GetGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_graph.async_get_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetGraph")
        )
        input_: capo_neptune_graph.types.get_graph_input.GetGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_graphs(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> "capo_neptune_graph.types.list_graphs_output.ListGraphsOutput":
        """<p>Lists available Neptune Analytics graphs.</p>

        Args:
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_graphs_input.ListGraphsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_graphs_output.ListGraphsOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_graphs

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_graphs.async_list_graphs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGraphs")
        )
        input_: capo_neptune_graph.types.list_graphs_input.ListGraphsInput = {}
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

    async def reset_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        skip_snapshot: bool,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.reset_graph_output.ResetGraphOutput":
        """<p>Empties the data from a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>ID of the graph to reset.</p>
            skip_snapshot: <p>Determines whether a final graph snapshot is created before the graph data is deleted. If set to <code>true</code>, no graph snapshot is created. If set to <code>false</code>, a graph snapshot is created before the data is deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.reset_graph_input.ResetGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.reset_graph_output.ResetGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.reset_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.reset_graph.async_reset_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ResetGraph")
        )
        input_: capo_neptune_graph.types.reset_graph_input.ResetGraphInput = {
            "graph_identifier": graph_identifier,
            "skip_snapshot": skip_snapshot,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_graph_from_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
        replica_count: Optional[
            "capo_neptune_graph.types.replica_count.ReplicaCount"
        ] = None,
        public_connectivity: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput":
        """<p>Restores a graph from a snapshot.</p>

        Args:
            snapshot_identifier: <p>The ID of the snapshot in question.</p>
            graph_name: <p>A name for the new Neptune Analytics graph to be created from the snapshot.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>
            tags: <p>Adds metadata tags to the snapshot. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            replica_count: <p>The number of replicas in other AZs. Min =0, Max = 2, Default =1</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.restore_graph_from_snapshot_output.RestoreGraphFromSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.restore_graph_from_snapshot.async_restore_graph_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestoreGraphFromSnapshot")
        )
        input_: capo_neptune_graph.types.restore_graph_from_snapshot_input.RestoreGraphFromSnapshotInput = {
            "snapshot_identifier": snapshot_identifier,
            "graph_name": graph_name,
        }
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
        if tags is not None:
            input_["tags"] = tags
        if replica_count is not None:
            input_["replica_count"] = replica_count
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.start_graph_output.StartGraphOutput":
        """<p>Starts the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.start_graph_input.StartGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.start_graph_output.StartGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.start_graph.async_start_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartGraph")
        )
        input_: capo_neptune_graph.types.start_graph_input.StartGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.stop_graph_output.StopGraphOutput":
        """<p>Stops the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.stop_graph_input.StopGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.stop_graph_output.StopGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.stop_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.stop_graph.async_stop_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopGraph")
        )
        input_: capo_neptune_graph.types.stop_graph_input.StopGraphInput = {
            "graph_identifier": graph_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_graph(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        public_connectivity: Optional[bool] = None,
        provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        deletion_protection: Optional[bool] = None,
    ) -> "capo_neptune_graph.types.update_graph_output.UpdateGraphOutput":
        """<p>Updates the configuration of a specified Neptune Analytics graph</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>
            provisioned_memory: <p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>
            deletion_protection: <p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.update_graph_input.UpdateGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.update_graph_output.UpdateGraphOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.update_graph

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.update_graph.async_update_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGraph")
        )
        input_: capo_neptune_graph.types.update_graph_input.UpdateGraphInput = {
            "graph_identifier": graph_identifier
        }
        if public_connectivity is not None:
            input_["public_connectivity"] = public_connectivity
        if provisioned_memory is not None:
            input_["provisioned_memory"] = provisioned_memory
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
