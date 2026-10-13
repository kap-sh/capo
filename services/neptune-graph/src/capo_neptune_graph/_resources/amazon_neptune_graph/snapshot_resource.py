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
    import capo_neptune_graph.types.create_graph_snapshot_input
    import capo_neptune_graph.types.create_graph_snapshot_output
    import capo_neptune_graph.types.delete_graph_snapshot_input
    import capo_neptune_graph.types.delete_graph_snapshot_output
    import capo_neptune_graph.types.get_graph_snapshot_input
    import capo_neptune_graph.types.get_graph_snapshot_output
    import capo_neptune_graph.types.graph_identifier
    import capo_neptune_graph.types.graph_snapshot_summary
    import capo_neptune_graph.types.list_graph_snapshots_input
    import capo_neptune_graph.types.list_graph_snapshots_output
    import capo_neptune_graph.types.max_results
    import capo_neptune_graph.types.pagination_token
    import capo_neptune_graph.types.snapshot_identifier
    import capo_neptune_graph.types.snapshot_name
    import capo_neptune_graph.types.tag_map
    from capo_neptune_graph._services.async_neptune_graph import (
        AsyncNeptuneGraphClient,
        AsyncNeptuneGraphClientConfig,
    )
    from capo_neptune_graph._services.neptune_graph import (
        NeptuneGraphClient,
        NeptuneGraphClientConfig,
    )


class SnapshotResource:
    def __init__(self, service: NeptuneGraphClient) -> None:
        self._service = service

    def create_graph_snapshot(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        snapshot_name: "capo_neptune_graph.types.snapshot_name.SnapshotName",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
    ) -> "capo_neptune_graph.types.create_graph_snapshot_output.CreateGraphSnapshotOutput":
        """<p>Creates a snapshot of the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            snapshot_name: <p>The snapshot name. For example: <code>my-snapshot-1</code>.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>

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
            req: "OperationRequest[capo_neptune_graph.types.create_graph_snapshot_input.CreateGraphSnapshotInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.create_graph_snapshot_output.CreateGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph_snapshot

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.create_graph_snapshot.create_graph_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGraphSnapshot")
        )
        input_: capo_neptune_graph.types.create_graph_snapshot_input.CreateGraphSnapshotInput = {
            "graph_identifier": graph_identifier,
            "snapshot_name": snapshot_name,
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

    def delete_graph_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.delete_graph_snapshot_output.DeleteGraphSnapshotOutput":
        """<p>Deletes the specified graph snapshot.</p>

        Args:
            snapshot_identifier: <p>ID of the graph snapshot to be deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.delete_graph_snapshot_input.DeleteGraphSnapshotInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.delete_graph_snapshot_output.DeleteGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.delete_graph_snapshot

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.delete_graph_snapshot.delete_graph_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGraphSnapshot")
        )
        input_: capo_neptune_graph.types.delete_graph_snapshot_input.DeleteGraphSnapshotInput = {
            "snapshot_identifier": snapshot_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_graph_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_graph_snapshot_output.GetGraphSnapshotOutput":
        """<p>Retrieves a specified graph snapshot.</p>

        Args:
            snapshot_identifier: <p>The ID of the snapshot to retrieve.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.get_graph_snapshot_input.GetGraphSnapshotInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.get_graph_snapshot_output.GetGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_graph_snapshot

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.get_graph_snapshot.get_graph_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetGraphSnapshot")
        )
        input_: capo_neptune_graph.types.get_graph_snapshot_input.GetGraphSnapshotInput = {
            "snapshot_identifier": snapshot_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_graph_snapshots(
        self,
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        graph_identifier: Optional[
            "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
        ] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_neptune_graph.types.list_graph_snapshots_output.ListGraphSnapshotsOutput"
    ):
        """<p>Lists available snapshots of a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.list_graph_snapshots_input.ListGraphSnapshotsInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.list_graph_snapshots_output.ListGraphSnapshotsOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_graph_snapshots

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.list_graph_snapshots.list_graph_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGraphSnapshots")
        )
        input_: capo_neptune_graph.types.list_graph_snapshots_input.ListGraphSnapshotsInput = {}
        if graph_identifier is not None:
            input_["graph_identifier"] = graph_identifier
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


class AsyncSnapshotResource:
    def __init__(self, service: AsyncNeptuneGraphClient) -> None:
        self._service = service

    async def create_graph_snapshot(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        snapshot_name: "capo_neptune_graph.types.snapshot_name.SnapshotName",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
    ) -> "capo_neptune_graph.types.create_graph_snapshot_output.CreateGraphSnapshotOutput":
        """<p>Creates a snapshot of the specific graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            snapshot_name: <p>The snapshot name. For example: <code>my-snapshot-1</code>.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>

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
            req: "AsyncOperationRequest[capo_neptune_graph.types.create_graph_snapshot_input.CreateGraphSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.create_graph_snapshot_output.CreateGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.create_graph_snapshot.async_create_graph_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGraphSnapshot")
        )
        input_: capo_neptune_graph.types.create_graph_snapshot_input.CreateGraphSnapshotInput = {
            "graph_identifier": graph_identifier,
            "snapshot_name": snapshot_name,
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

    async def delete_graph_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.delete_graph_snapshot_output.DeleteGraphSnapshotOutput":
        """<p>Deletes the specified graph snapshot.</p>

        Args:
            snapshot_identifier: <p>ID of the graph snapshot to be deleted.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.delete_graph_snapshot_input.DeleteGraphSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.delete_graph_snapshot_output.DeleteGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.delete_graph_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.delete_graph_snapshot.async_delete_graph_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGraphSnapshot")
        )
        input_: capo_neptune_graph.types.delete_graph_snapshot_input.DeleteGraphSnapshotInput = {
            "snapshot_identifier": snapshot_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_graph_snapshot(
        self,
        snapshot_identifier: "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_graph_snapshot_output.GetGraphSnapshotOutput":
        """<p>Retrieves a specified graph snapshot.</p>

        Args:
            snapshot_identifier: <p>The ID of the snapshot to retrieve.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_graph_snapshot_input.GetGraphSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_graph_snapshot_output.GetGraphSnapshotOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_graph_snapshot

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_graph_snapshot.async_get_graph_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetGraphSnapshot")
        )
        input_: capo_neptune_graph.types.get_graph_snapshot_input.GetGraphSnapshotInput = {
            "snapshot_identifier": snapshot_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_graph_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        graph_identifier: Optional[
            "capo_neptune_graph.types.graph_identifier.GraphIdentifier"
        ] = None,
        next_token: Optional[
            "capo_neptune_graph.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_neptune_graph.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_neptune_graph.types.list_graph_snapshots_output.ListGraphSnapshotsOutput"
    ):
        """<p>Lists available snapshots of a specified Neptune Analytics graph.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>
            max_results: <p>The total number of records to return in the command's output.</p> <p>If the total number of records available is more than the value specified, <code>nextToken</code> is provided in the command's output. To resume pagination, provide the <code>nextToken</code> output value in the <code>nextToken</code> argument of a subsequent command. Do not use the <code>nextToken</code> response element directly outside of the Amazon CLI.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_graph_snapshots_input.ListGraphSnapshotsInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_graph_snapshots_output.ListGraphSnapshotsOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_graph_snapshots

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_graph_snapshots.async_list_graph_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGraphSnapshots")
        )
        input_: capo_neptune_graph.types.list_graph_snapshots_input.ListGraphSnapshotsInput = {}
        if graph_identifier is not None:
            input_["graph_identifier"] = graph_identifier
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
