from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_neptune_graph._auth._signers
import capo_neptune_graph._auth._sigv4
from capo_neptune_graph._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_neptune_graph.types.blank_node_handling
    import capo_neptune_graph.types.cancel_export_task_input
    import capo_neptune_graph.types.cancel_export_task_output
    import capo_neptune_graph.types.cancel_import_task_input
    import capo_neptune_graph.types.cancel_import_task_output
    import capo_neptune_graph.types.create_graph_using_import_task_input
    import capo_neptune_graph.types.create_graph_using_import_task_output
    import capo_neptune_graph.types.export_filter
    import capo_neptune_graph.types.export_format
    import capo_neptune_graph.types.export_task_id
    import capo_neptune_graph.types.export_task_summary
    import capo_neptune_graph.types.format
    import capo_neptune_graph.types.get_export_task_input
    import capo_neptune_graph.types.get_export_task_output
    import capo_neptune_graph.types.get_import_task_input
    import capo_neptune_graph.types.get_import_task_output
    import capo_neptune_graph.types.graph_identifier
    import capo_neptune_graph.types.graph_name
    import capo_neptune_graph.types.import_options
    import capo_neptune_graph.types.import_task_summary
    import capo_neptune_graph.types.kms_key_arn
    import capo_neptune_graph.types.list_export_tasks_input
    import capo_neptune_graph.types.list_export_tasks_output
    import capo_neptune_graph.types.list_import_tasks_input
    import capo_neptune_graph.types.list_import_tasks_output
    import capo_neptune_graph.types.max_results
    import capo_neptune_graph.types.pagination_token
    import capo_neptune_graph.types.parquet_type
    import capo_neptune_graph.types.provisioned_memory
    import capo_neptune_graph.types.replica_count
    import capo_neptune_graph.types.role_arn
    import capo_neptune_graph.types.start_export_task_input
    import capo_neptune_graph.types.start_export_task_output
    import capo_neptune_graph.types.start_import_task_input
    import capo_neptune_graph.types.start_import_task_output
    import capo_neptune_graph.types.tag_map
    import capo_neptune_graph.types.task_id
    import capo_neptune_graph.types.vector_search_configuration
    from capo_neptune_graph._services.async_neptune_graph import (
        AsyncNeptuneGraphClient,
        AsyncNeptuneGraphClientConfig,
    )
    from capo_neptune_graph._services.neptune_graph import (
        NeptuneGraphClient,
        NeptuneGraphClientConfig,
    )


class TaskResource:
    def __init__(self, service: NeptuneGraphClient) -> None:
        self._service = service

    def cancel_export_task(
        self,
        task_identifier: "capo_neptune_graph.types.export_task_id.ExportTaskId",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.cancel_export_task_output.CancelExportTaskOutput":
        """<p>Cancel the specified export task.</p>

        Args:
            task_identifier: <p>The unique identifier of the export task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.cancel_export_task_input.CancelExportTaskInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.cancel_export_task_output.CancelExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.cancel_export_task

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.cancel_export_task.cancel_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.cancel_export_task_input.CancelExportTaskInput = {
            "task_identifier": task_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_import_task(
        self,
        task_identifier: "capo_neptune_graph.types.task_id.TaskId",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.cancel_import_task_output.CancelImportTaskOutput":
        """<p>Deletes the specified import task.</p>

        Args:
            task_identifier: <p>The unique identifier of the import task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.cancel_import_task_input.CancelImportTaskInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.cancel_import_task_output.CancelImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.cancel_import_task

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.cancel_import_task.cancel_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.cancel_import_task_input.CancelImportTaskInput = {
            "task_identifier": task_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_graph_using_import_task(
        self,
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        source: str,
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
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
        import_options: Optional[
            "capo_neptune_graph.types.import_options.ImportOptions"
        ] = None,
        max_provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        min_provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        fail_on_error: Optional[bool] = None,
        format: Optional["capo_neptune_graph.types.format.Format"] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        blank_node_handling: Optional[
            "capo_neptune_graph.types.blank_node_handling.BlankNodeHandling"
        ] = None,
    ) -> "capo_neptune_graph.types.create_graph_using_import_task_output.CreateGraphUsingImportTaskOutput":
        """<p>Creates a new Neptune Analytics graph and imports data into it, either from Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune database snapshot.</p> <p>The data can be loaded from files in S3 that in either the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV format</a> or the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher load format</a>.</p>

        Args:
            graph_name: <p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>
            kms_key_identifier: <p>Specifies a KMS key to use to encrypt data imported into the new graph.</p>
            vector_search_configuration: <p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535 </p>
            replica_count: <p>The number of replicas in other AZs to provision on the new graph after import. Default = 1, Min = 0, Max = 2.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            deletion_protection: <p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>
            import_options: <p>Contains options for controlling the import process. For example, if the <code>failOnError</code> key is set to <code>false</code>, the import skips problem data and attempts to continue (whereas if set to <code>true</code>, the default, or if omitted, the import operation halts immediately when an error is encountered.</p>
            max_provisioned_memory: <p>The maximum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 1024, or the approved upper limit for your account.</p> <p> If both the minimum and maximum values are specified, the final <code>provisioned-memory</code> will be chosen per the actual size of your imported data. If neither value is specified, 128 m-NCUs are used.</p>
            min_provisioned_memory: <p>The minimum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 16</p>
            fail_on_error: <p>If set to <code>true</code>, the task halts when an import error is encountered. If set to <code>false</code>, the task skips the data that caused the error and continues if possible.</p>
            source: <p>A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>
            format: <p>Specifies the format of S3 data to be imported. Valid values are <code>CSV</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV format</a>, <code>OPEN_CYPHER</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher load format</a>, or <code>ntriples</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html">RDF n-triples</a> format.</p>
            parquet_type: <p>The parquet type of the import task.</p>
            blank_node_handling: <p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling">Handling RDF values</a>.</p>
            role_arn: <p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.create_graph_using_import_task_input.CreateGraphUsingImportTaskInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.create_graph_using_import_task_output.CreateGraphUsingImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph_using_import_task

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.create_graph_using_import_task.create_graph_using_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.create_graph_using_import_task_input.CreateGraphUsingImportTaskInput = {
            "graph_name": graph_name,
            "source": source,
            "role_arn": role_arn,
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
        if import_options is not None:
            input_["import_options"] = import_options
        if max_provisioned_memory is not None:
            input_["max_provisioned_memory"] = max_provisioned_memory
        if min_provisioned_memory is not None:
            input_["min_provisioned_memory"] = min_provisioned_memory
        if fail_on_error is not None:
            input_["fail_on_error"] = fail_on_error
        if format is not None:
            input_["format"] = format
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if blank_node_handling is not None:
            input_["blank_node_handling"] = blank_node_handling

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_export_task(
        self,
        task_identifier: "capo_neptune_graph.types.export_task_id.ExportTaskId",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_export_task_output.GetExportTaskOutput":
        """<p>Retrieves a specified export task.</p>

        Args:
            task_identifier: <p>The unique identifier of the export task.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.get_export_task_input.GetExportTaskInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.get_export_task_output.GetExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_export_task

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.get_export_task.get_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_export_task_input.GetExportTaskInput = {
            "task_identifier": task_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_import_task(
        self,
        task_identifier: "capo_neptune_graph.types.task_id.TaskId",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_import_task_output.GetImportTaskOutput":
        """<p>Retrieves a specified import task.</p>

        Args:
            task_identifier: <p>The unique identifier of the import task.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.get_import_task_input.GetImportTaskInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.get_import_task_output.GetImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_import_task

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.get_import_task.get_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_import_task_input.GetImportTaskInput = {
            "task_identifier": task_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_export_tasks(
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
    ) -> "capo_neptune_graph.types.list_export_tasks_output.ListExportTasksOutput":
        """<p>Retrieves a list of export tasks.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate input.</p>
            max_results: <p>The maximum number of export tasks to return.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.list_export_tasks_input.ListExportTasksInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.list_export_tasks_output.ListExportTasksOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_export_tasks

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.list_export_tasks.list_export_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_export_tasks_input.ListExportTasksInput = {}
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

    def list_import_tasks(
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
    ) -> "capo_neptune_graph.types.list_import_tasks_output.ListImportTasksOutput":
        """<p>Lists import tasks.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph. When provided, the service returns only import tasks associated with this graph. If not specified, the service returns all import tasks.</p>
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
            req: "OperationRequest[capo_neptune_graph.types.list_import_tasks_input.ListImportTasksInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.list_import_tasks_output.ListImportTasksOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_import_tasks

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.list_import_tasks.list_import_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_import_tasks_input.ListImportTasksInput = {}
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

    def start_export_task(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
        format: "capo_neptune_graph.types.export_format.ExportFormat",
        destination: str,
        kms_key_identifier: "capo_neptune_graph.types.kms_key_arn.KmsKeyArn",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        export_filter: Optional[
            "capo_neptune_graph.types.export_filter.ExportFilter"
        ] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
    ) -> "capo_neptune_graph.types.start_export_task_output.StartExportTaskOutput":
        """<p>Export data from an existing Neptune Analytics graph to Amazon S3. The graph state should be <code>AVAILABLE</code>.</p>

        Args:
            graph_identifier: <p>The source graph identifier of the export task.</p>
            role_arn: <p>The ARN of the IAM role that will allow data to be exported to the destination.</p>
            format: <p>The format of the export task.</p>
            destination: <p>The Amazon S3 URI where data will be exported to.</p>
            kms_key_identifier: <p>The KMS key identifier of the export task.</p>
            parquet_type: <p>The parquet type of the export task.</p>
            export_filter: <p>The export filter of the export task.</p>
            tags: <p>Tags to be applied to the export task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.start_export_task_input.StartExportTaskInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.start_export_task_output.StartExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_export_task

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.start_export_task.start_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.start_export_task_input.StartExportTaskInput = {
            "graph_identifier": graph_identifier,
            "role_arn": role_arn,
            "format": format,
            "destination": destination,
            "kms_key_identifier": kms_key_identifier,
        }
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if export_filter is not None:
            input_["export_filter"] = export_filter
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_import_task(
        self,
        source: str,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[NeptuneGraphClientConfig] = None,
        import_options: Optional[
            "capo_neptune_graph.types.import_options.ImportOptions"
        ] = None,
        fail_on_error: Optional[bool] = None,
        format: Optional["capo_neptune_graph.types.format.Format"] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        blank_node_handling: Optional[
            "capo_neptune_graph.types.blank_node_handling.BlankNodeHandling"
        ] = None,
    ) -> "capo_neptune_graph.types.start_import_task_output.StartImportTaskOutput":
        """<p>Import data into existing Neptune Analytics graph from Amazon Simple Storage Service (S3). The graph needs to be empty and in the AVAILABLE state.</p>

        Args:
            fail_on_error: <p>If set to true, the task halts when an import error is encountered. If set to false, the task skips the data that caused the error and continues if possible.</p>
            source: <p>A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>
            format: <p>Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identifies the openCypher load format.</p>
            parquet_type: <p>The parquet type of the import task.</p>
            blank_node_handling: <p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling">Handling RDF values</a>.</p>
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            role_arn: <p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_neptune_graph.types.start_import_task_input.StartImportTaskInput]",
        ) -> OperationResponse[
            "capo_neptune_graph.types.start_import_task_output.StartImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_import_task

            output, http_response = (
                capo_neptune_graph._operations.amazon_neptune_graph.start_import_task.start_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.start_import_task_input.StartImportTaskInput = {
            "source": source,
            "graph_identifier": graph_identifier,
            "role_arn": role_arn,
        }
        if import_options is not None:
            input_["import_options"] = import_options
        if fail_on_error is not None:
            input_["fail_on_error"] = fail_on_error
        if format is not None:
            input_["format"] = format
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if blank_node_handling is not None:
            input_["blank_node_handling"] = blank_node_handling

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTaskResource:
    def __init__(self, service: AsyncNeptuneGraphClient) -> None:
        self._service = service

    async def cancel_export_task(
        self,
        task_identifier: "capo_neptune_graph.types.export_task_id.ExportTaskId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.cancel_export_task_output.CancelExportTaskOutput":
        """<p>Cancel the specified export task.</p>

        Args:
            task_identifier: <p>The unique identifier of the export task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.cancel_export_task_input.CancelExportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.cancel_export_task_output.CancelExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.cancel_export_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.cancel_export_task.async_cancel_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.cancel_export_task_input.CancelExportTaskInput = {
            "task_identifier": task_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_import_task(
        self,
        task_identifier: "capo_neptune_graph.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.cancel_import_task_output.CancelImportTaskOutput":
        """<p>Deletes the specified import task.</p>

        Args:
            task_identifier: <p>The unique identifier of the import task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.cancel_import_task_input.CancelImportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.cancel_import_task_output.CancelImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.cancel_import_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.cancel_import_task.async_cancel_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.cancel_import_task_input.CancelImportTaskInput = {
            "task_identifier": task_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_graph_using_import_task(
        self,
        graph_name: "capo_neptune_graph.types.graph_name.GraphName",
        source: str,
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
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
        import_options: Optional[
            "capo_neptune_graph.types.import_options.ImportOptions"
        ] = None,
        max_provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        min_provisioned_memory: Optional[
            "capo_neptune_graph.types.provisioned_memory.ProvisionedMemory"
        ] = None,
        fail_on_error: Optional[bool] = None,
        format: Optional["capo_neptune_graph.types.format.Format"] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        blank_node_handling: Optional[
            "capo_neptune_graph.types.blank_node_handling.BlankNodeHandling"
        ] = None,
    ) -> "capo_neptune_graph.types.create_graph_using_import_task_output.CreateGraphUsingImportTaskOutput":
        """<p>Creates a new Neptune Analytics graph and imports data into it, either from Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune database snapshot.</p> <p>The data can be loaded from files in S3 that in either the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV format</a> or the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher load format</a>.</p>

        Args:
            graph_name: <p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>
            tags: <p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>
            public_connectivity: <p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>
            kms_key_identifier: <p>Specifies a KMS key to use to encrypt data imported into the new graph.</p>
            vector_search_configuration: <p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535 </p>
            replica_count: <p>The number of replicas in other AZs to provision on the new graph after import. Default = 1, Min = 0, Max = 2.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>
            deletion_protection: <p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>
            import_options: <p>Contains options for controlling the import process. For example, if the <code>failOnError</code> key is set to <code>false</code>, the import skips problem data and attempts to continue (whereas if set to <code>true</code>, the default, or if omitted, the import operation halts immediately when an error is encountered.</p>
            max_provisioned_memory: <p>The maximum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 1024, or the approved upper limit for your account.</p> <p> If both the minimum and maximum values are specified, the final <code>provisioned-memory</code> will be chosen per the actual size of your imported data. If neither value is specified, 128 m-NCUs are used.</p>
            min_provisioned_memory: <p>The minimum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 16</p>
            fail_on_error: <p>If set to <code>true</code>, the task halts when an import error is encountered. If set to <code>false</code>, the task skips the data that caused the error and continues if possible.</p>
            source: <p>A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>
            format: <p>Specifies the format of S3 data to be imported. Valid values are <code>CSV</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV format</a>, <code>OPEN_CYPHER</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher load format</a>, or <code>ntriples</code>, which identifies the <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html">RDF n-triples</a> format.</p>
            parquet_type: <p>The parquet type of the import task.</p>
            blank_node_handling: <p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling">Handling RDF values</a>.</p>
            role_arn: <p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota was exceeded.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.create_graph_using_import_task_input.CreateGraphUsingImportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.create_graph_using_import_task_output.CreateGraphUsingImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.create_graph_using_import_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.create_graph_using_import_task.async_create_graph_using_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.create_graph_using_import_task_input.CreateGraphUsingImportTaskInput = {
            "graph_name": graph_name,
            "source": source,
            "role_arn": role_arn,
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
        if import_options is not None:
            input_["import_options"] = import_options
        if max_provisioned_memory is not None:
            input_["max_provisioned_memory"] = max_provisioned_memory
        if min_provisioned_memory is not None:
            input_["min_provisioned_memory"] = min_provisioned_memory
        if fail_on_error is not None:
            input_["fail_on_error"] = fail_on_error
        if format is not None:
            input_["format"] = format
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if blank_node_handling is not None:
            input_["blank_node_handling"] = blank_node_handling

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_export_task(
        self,
        task_identifier: "capo_neptune_graph.types.export_task_id.ExportTaskId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_export_task_output.GetExportTaskOutput":
        """<p>Retrieves a specified export task.</p>

        Args:
            task_identifier: <p>The unique identifier of the export task.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_export_task_input.GetExportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_export_task_output.GetExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_export_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_export_task.async_get_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_export_task_input.GetExportTaskInput = {
            "task_identifier": task_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_import_task(
        self,
        task_identifier: "capo_neptune_graph.types.task_id.TaskId",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
    ) -> "capo_neptune_graph.types.get_import_task_output.GetImportTaskOutput":
        """<p>Retrieves a specified import task.</p>

        Args:
            task_identifier: <p>The unique identifier of the import task.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.get_import_task_input.GetImportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.get_import_task_output.GetImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.get_import_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.get_import_task.async_get_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.get_import_task_input.GetImportTaskInput = {
            "task_identifier": task_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_export_tasks(
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
    ) -> "capo_neptune_graph.types.list_export_tasks_output.ListExportTasksOutput":
        """<p>Retrieves a list of export tasks.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            next_token: <p>Pagination token used to paginate input.</p>
            max_results: <p>The maximum number of export tasks to return.</p>

        Raises:
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_export_tasks_input.ListExportTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_export_tasks_output.ListExportTasksOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_export_tasks

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_export_tasks.async_list_export_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_export_tasks_input.ListExportTasksInput = {}
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

    async def list_import_tasks(
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
    ) -> "capo_neptune_graph.types.list_import_tasks_output.ListImportTasksOutput":
        """<p>Lists import tasks.</p>

        Args:
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph. When provided, the service returns only import tasks associated with this graph. If not specified, the service returns all import tasks.</p>
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
            req: "AsyncOperationRequest[capo_neptune_graph.types.list_import_tasks_input.ListImportTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.list_import_tasks_output.ListImportTasksOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.list_import_tasks

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.list_import_tasks.async_list_import_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.list_import_tasks_input.ListImportTasksInput = {}
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

    async def start_export_task(
        self,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
        format: "capo_neptune_graph.types.export_format.ExportFormat",
        destination: str,
        kms_key_identifier: "capo_neptune_graph.types.kms_key_arn.KmsKeyArn",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        export_filter: Optional[
            "capo_neptune_graph.types.export_filter.ExportFilter"
        ] = None,
        tags: Optional["capo_neptune_graph.types.tag_map.TagMap"] = None,
    ) -> "capo_neptune_graph.types.start_export_task_output.StartExportTaskOutput":
        """<p>Export data from an existing Neptune Analytics graph to Amazon S3. The graph state should be <code>AVAILABLE</code>.</p>

        Args:
            graph_identifier: <p>The source graph identifier of the export task.</p>
            role_arn: <p>The ARN of the IAM role that will allow data to be exported to the destination.</p>
            format: <p>The format of the export task.</p>
            destination: <p>The Amazon S3 URI where data will be exported to.</p>
            kms_key_identifier: <p>The KMS key identifier of the export task.</p>
            parquet_type: <p>The parquet type of the export task.</p>
            export_filter: <p>The export filter of the export task.</p>
            tags: <p>Tags to be applied to the export task.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.start_export_task_input.StartExportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.start_export_task_output.StartExportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_export_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.start_export_task.async_start_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.start_export_task_input.StartExportTaskInput = {
            "graph_identifier": graph_identifier,
            "role_arn": role_arn,
            "format": format,
            "destination": destination,
            "kms_key_identifier": kms_key_identifier,
        }
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if export_filter is not None:
            input_["export_filter"] = export_filter
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import_task(
        self,
        source: str,
        graph_identifier: "capo_neptune_graph.types.graph_identifier.GraphIdentifier",
        role_arn: "capo_neptune_graph.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncNeptuneGraphClientConfig] = None,
        import_options: Optional[
            "capo_neptune_graph.types.import_options.ImportOptions"
        ] = None,
        fail_on_error: Optional[bool] = None,
        format: Optional["capo_neptune_graph.types.format.Format"] = None,
        parquet_type: Optional[
            "capo_neptune_graph.types.parquet_type.ParquetType"
        ] = None,
        blank_node_handling: Optional[
            "capo_neptune_graph.types.blank_node_handling.BlankNodeHandling"
        ] = None,
    ) -> "capo_neptune_graph.types.start_import_task_output.StartImportTaskOutput":
        """<p>Import data into existing Neptune Analytics graph from Amazon Simple Storage Service (S3). The graph needs to be empty and in the AVAILABLE state.</p>

        Args:
            fail_on_error: <p>If set to true, the task halts when an import error is encountered. If set to false, the task skips the data that caused the error and continues if possible.</p>
            source: <p>A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>
            format: <p>Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identifies the openCypher load format.</p>
            parquet_type: <p>The parquet type of the import task.</p>
            blank_node_handling: <p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href="https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling">Handling RDF values</a>.</p>
            graph_identifier: <p>The unique identifier of the Neptune Analytics graph.</p>
            role_arn: <p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>

        Raises:
            capo_neptune_graph.errors.conflict_exception.ConflictException: <p>Raised when a conflict is encountered.</p>
            capo_neptune_graph.errors.internal_server_exception.InternalServerException: <p>A failure occurred on the server.</p>
            capo_neptune_graph.errors.resource_not_found_exception.ResourceNotFoundException: <p>A specified resource could not be located.</p>
            capo_neptune_graph.errors.throttling_exception.ThrottlingException: <p>The exception was interrupted by throttling.</p>
            capo_neptune_graph.errors.validation_exception.ValidationException: <p>A resource could not be validated.</p>
            capo_neptune_graph.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_neptune_graph.types.start_import_task_input.StartImportTaskInput]",
        ) -> AsyncOperationResponse[
            "capo_neptune_graph.types.start_import_task_output.StartImportTaskOutput"
        ]:
            import capo_neptune_graph._operations.amazon_neptune_graph.start_import_task

            (
                output,
                http_response,
            ) = await capo_neptune_graph._operations.amazon_neptune_graph.start_import_task.async_start_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_neptune_graph.types.start_import_task_input.StartImportTaskInput = {
            "source": source,
            "graph_identifier": graph_identifier,
            "role_arn": role_arn,
        }
        if import_options is not None:
            input_["import_options"] = import_options
        if fail_on_error is not None:
            input_["fail_on_error"] = fail_on_error
        if format is not None:
            input_["format"] = format
        if parquet_type is not None:
            input_["parquet_type"] = parquet_type
        if blank_node_handling is not None:
            input_["blank_node_handling"] = blank_node_handling

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
