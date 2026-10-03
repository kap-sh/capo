from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_opensearchserverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.create_index_request
    import capo_opensearchserverless.types.create_index_response
    import capo_opensearchserverless.types.delete_index_request
    import capo_opensearchserverless.types.delete_index_response
    import capo_opensearchserverless.types.get_index_request
    import capo_opensearchserverless.types.get_index_response
    import capo_opensearchserverless.types.index_name
    import capo_opensearchserverless.types.index_schema
    import capo_opensearchserverless.types.update_index_request
    import capo_opensearchserverless.types.update_index_response
    from capo_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from capo_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class Index:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def put(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        index_schema: Optional[
            "capo_opensearchserverless.types.index_schema.IndexSchema"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_index_response.CreateIndexResponse":
        """<p>Creates an index within an OpenSearch Serverless collection. Unlike other OpenSearch indexes, indexes created by this API are automatically configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a> in the <i>OpenSearch User Guide</i>.</p>

        Args:
            id: <p>The unique identifier of the collection in which to create the index.</p>
            index_name: <p>The name of the index to create. Index names must be lowercase and can't begin with underscores (_) or hyphens (-).</p>
            index_schema: <p>The JSON schema definition for the index, including field mappings and settings.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_index_request.CreateIndexRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_index_response.CreateIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_index

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_index.create_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_index_request.CreateIndexRequest = {
            "id": id,
            "index_name": index_name,
        }
        if index_schema is not None:
            input_["index_schema"] = index_schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_index_response.GetIndexResponse":
        """<p>Retrieves information about an index in an OpenSearch Serverless collection, including its schema definition. The index might be configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index.</p>
            index_name: <p>The name of the index to retrieve information about.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_index_request.GetIndexRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_index_response.GetIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_index

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_index.get_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_index_request.GetIndexRequest = {
            "id": id,
            "index_name": index_name,
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
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        index_schema: Optional[
            "capo_opensearchserverless.types.index_schema.IndexSchema"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_index_response.UpdateIndexResponse":
        """<p>Updates an existing index in an OpenSearch Serverless collection. This operation allows you to modify the index schema, including adding new fields or changing field mappings. You can also enable automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index to update.</p>
            index_name: <p>The name of the index to update.</p>
            index_schema: <p>The updated JSON schema definition for the index, including field mappings and settings. </p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_index_request.UpdateIndexRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_index_response.UpdateIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_index

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_index.update_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_index_request.UpdateIndexRequest = {
            "id": id,
            "index_name": index_name,
        }
        if index_schema is not None:
            input_["index_schema"] = index_schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.delete_index_response.DeleteIndexResponse":
        """<p>Deletes an index from an OpenSearch Serverless collection. Be aware that the index might be configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index to delete.</p>
            index_name: <p>The name of the index to delete.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_index_request.DeleteIndexRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_index_response.DeleteIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_index

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_index.delete_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_index_request.DeleteIndexRequest = {
            "id": id,
            "index_name": index_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncIndex:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def put(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        index_schema: Optional[
            "capo_opensearchserverless.types.index_schema.IndexSchema"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_index_response.CreateIndexResponse":
        """<p>Creates an index within an OpenSearch Serverless collection. Unlike other OpenSearch indexes, indexes created by this API are automatically configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a> in the <i>OpenSearch User Guide</i>.</p>

        Args:
            id: <p>The unique identifier of the collection in which to create the index.</p>
            index_name: <p>The name of the index to create. Index names must be lowercase and can't begin with underscores (_) or hyphens (-).</p>
            index_schema: <p>The JSON schema definition for the index, including field mappings and settings.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_index_request.CreateIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_index_response.CreateIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_index

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_index.async_create_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_index_request.CreateIndexRequest = {
            "id": id,
            "index_name": index_name,
        }
        if index_schema is not None:
            input_["index_schema"] = index_schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_index_response.GetIndexResponse":
        """<p>Retrieves information about an index in an OpenSearch Serverless collection, including its schema definition. The index might be configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index.</p>
            index_name: <p>The name of the index to retrieve information about.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.get_index_request.GetIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.get_index_response.GetIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_index

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.get_index.async_get_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.get_index_request.GetIndexRequest = {
            "id": id,
            "index_name": index_name,
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
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        index_schema: Optional[
            "capo_opensearchserverless.types.index_schema.IndexSchema"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_index_response.UpdateIndexResponse":
        """<p>Updates an existing index in an OpenSearch Serverless collection. This operation allows you to modify the index schema, including adding new fields or changing field mappings. You can also enable automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index to update.</p>
            index_name: <p>The name of the index to update.</p>
            index_schema: <p>The updated JSON schema definition for the index, including field mappings and settings. </p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.update_index_request.UpdateIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.update_index_response.UpdateIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_index

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.update_index.async_update_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_index_request.UpdateIndexRequest = {
            "id": id,
            "index_name": index_name,
        }
        if index_schema is not None:
            input_["index_schema"] = index_schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        index_name: "capo_opensearchserverless.types.index_name.IndexName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.delete_index_response.DeleteIndexResponse":
        """<p>Deletes an index from an OpenSearch Serverless collection. Be aware that the index might be configured to conduct automatic semantic enrichment ingestion and search. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html#serverless-semantic-enrichment">About automatic semantic enrichment</a>.</p>

        Args:
            id: <p>The unique identifier of the collection containing the index to delete.</p>
            index_name: <p>The name of the index to delete.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.delete_index_request.DeleteIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.delete_index_response.DeleteIndexResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_index

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.delete_index.async_delete_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_index_request.DeleteIndexRequest = {
            "id": id,
            "index_name": index_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
