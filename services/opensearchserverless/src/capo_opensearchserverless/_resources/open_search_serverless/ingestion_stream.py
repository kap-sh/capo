from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_opensearchserverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.create_ingestion_stream_request
    import capo_opensearchserverless.types.create_ingestion_stream_response
    import capo_opensearchserverless.types.delete_ingestion_stream_request
    import capo_opensearchserverless.types.delete_ingestion_stream_response
    import capo_opensearchserverless.types.get_ingestion_stream_request
    import capo_opensearchserverless.types.get_ingestion_stream_response
    import capo_opensearchserverless.types.ingestion_index_name
    import capo_opensearchserverless.types.ingestion_stream_id
    import capo_opensearchserverless.types.ingestion_stream_name
    import capo_opensearchserverless.types.ingestion_stream_source
    import capo_opensearchserverless.types.ingestion_stream_summary
    import capo_opensearchserverless.types.list_ingestion_streams_request
    import capo_opensearchserverless.types.list_ingestion_streams_response
    import capo_opensearchserverless.types.role_arn
    import capo_opensearchserverless.types.tags
    from capo_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from capo_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class IngestionStream:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_stream_name: "capo_opensearchserverless.types.ingestion_stream_name.IngestionStreamName",
        index_name: "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName",
        source: "capo_opensearchserverless.types.ingestion_stream_source.IngestionStreamSource",
        role_arn: "capo_opensearchserverless.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        failure_index_name: Optional[
            "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
        ] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_ingestion_stream_response.CreateIngestionStreamResponse":
        """<p>Creates an ingestion stream that continuously ingests data from an Amazon S3 bucket into an index in an OpenSearch Serverless collection. An ingestion stream processes Amazon S3 event notifications delivered to an Amazon SQS queue and ingests new objects as they arrive. The stream continues to ingest data until you delete it. To perform a one-time bulk ingestion instead, use <code>CreateIngestionJob</code>.</p>

        Args:
            collection_id: <p>The unique identifier of the collection to ingest data into.</p>
            ingestion_stream_name: <p>The name of the ingestion stream. The name must be unique within the collection.</p>
            index_name: <p>The name of the index to ingest documents into.</p>
            failure_index_name: <p>The name of the index where documents that fail to be ingested are recorded.</p>
            source: <p>The Amazon S3 source to ingest data from, including the Amazon SQS queue that receives S3 event notifications.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that OpenSearch Serverless assumes to read data from the source. The role must be in the same account as the collection.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the ingestion stream.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_ingestion_stream_request.CreateIngestionStreamRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_ingestion_stream_response.CreateIngestionStreamResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_ingestion_stream

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_ingestion_stream.create_ingestion_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateIngestionStream")
        )
        input_: capo_opensearchserverless.types.create_ingestion_stream_request.CreateIngestionStreamRequest = {
            "collection_id": collection_id,
            "ingestion_stream_name": ingestion_stream_name,
            "index_name": index_name,
            "source": source,
            "role_arn": role_arn,
        }
        if failure_index_name is not None:
            input_["failure_index_name"] = failure_index_name
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_stream_id: "capo_opensearchserverless.types.ingestion_stream_id.IngestionStreamId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_ingestion_stream_response.GetIngestionStreamResponse":
        """<p>Returns information about an ingestion stream, including its configuration, status, and processing state.</p>

        Args:
            collection_id: <p>The unique identifier of the collection that the ingestion stream belongs to.</p>
            ingestion_stream_id: <p>The unique identifier of the ingestion stream to retrieve.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_ingestion_stream_request.GetIngestionStreamRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_ingestion_stream_response.GetIngestionStreamResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_ingestion_stream

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_ingestion_stream.get_ingestion_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIngestionStream")
        )
        input_: capo_opensearchserverless.types.get_ingestion_stream_request.GetIngestionStreamRequest = {
            "collection_id": collection_id,
            "ingestion_stream_id": ingestion_stream_id,
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
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_stream_id: "capo_opensearchserverless.types.ingestion_stream_id.IngestionStreamId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_ingestion_stream_response.DeleteIngestionStreamResponse":
        """<p>Deletes an ingestion stream. Documents that were already indexed by the stream remain in the index.</p>

        Args:
            collection_id: <p>The unique identifier of the collection that the ingestion stream belongs to.</p>
            ingestion_stream_id: <p>The unique identifier of the ingestion stream to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_ingestion_stream_request.DeleteIngestionStreamRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_ingestion_stream_response.DeleteIngestionStreamResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_ingestion_stream

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_ingestion_stream.delete_ingestion_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIngestionStream")
        )
        input_: capo_opensearchserverless.types.delete_ingestion_stream_request.DeleteIngestionStreamRequest = {
            "collection_id": collection_id,
            "ingestion_stream_id": ingestion_stream_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_ingestion_streams_response.ListIngestionStreamsResponse":
        """<p>Returns a list of ingestion streams in a collection.</p>

        Args:
            collection_id: <p>The unique identifier of the collection to list ingestion streams for.</p>
            next_token: <p>If your initial <code>ListIngestionStreams</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListIngestionStreams</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Valid values are 1–100. If you don't specify a value, the default is 100. You can use <code>nextToken</code> to get the next page of results.</p> <p>A response can contain fewer results than <code>maxResults</code>, or no results, and still include a <code>nextToken</code>. To retrieve all results, continue to make the call with the returned <code>nextToken</code> until no <code>nextToken</code> is returned.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_ingestion_streams_request.ListIngestionStreamsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_ingestion_streams_response.ListIngestionStreamsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_ingestion_streams

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_ingestion_streams.list_ingestion_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIngestionStreams")
        )
        input_: capo_opensearchserverless.types.list_ingestion_streams_request.ListIngestionStreamsRequest = {
            "collection_id": collection_id
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


class AsyncIngestionStream:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_stream_name: "capo_opensearchserverless.types.ingestion_stream_name.IngestionStreamName",
        index_name: "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName",
        source: "capo_opensearchserverless.types.ingestion_stream_source.IngestionStreamSource",
        role_arn: "capo_opensearchserverless.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        failure_index_name: Optional[
            "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
        ] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_ingestion_stream_response.CreateIngestionStreamResponse":
        """<p>Creates an ingestion stream that continuously ingests data from an Amazon S3 bucket into an index in an OpenSearch Serverless collection. An ingestion stream processes Amazon S3 event notifications delivered to an Amazon SQS queue and ingests new objects as they arrive. The stream continues to ingest data until you delete it. To perform a one-time bulk ingestion instead, use <code>CreateIngestionJob</code>.</p>

        Args:
            collection_id: <p>The unique identifier of the collection to ingest data into.</p>
            ingestion_stream_name: <p>The name of the ingestion stream. The name must be unique within the collection.</p>
            index_name: <p>The name of the index to ingest documents into.</p>
            failure_index_name: <p>The name of the index where documents that fail to be ingested are recorded.</p>
            source: <p>The Amazon S3 source to ingest data from, including the Amazon SQS queue that receives S3 event notifications.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that OpenSearch Serverless assumes to read data from the source. The role must be in the same account as the collection.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the ingestion stream.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_ingestion_stream_request.CreateIngestionStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_ingestion_stream_response.CreateIngestionStreamResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_ingestion_stream

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_ingestion_stream.async_create_ingestion_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateIngestionStream")
        )
        input_: capo_opensearchserverless.types.create_ingestion_stream_request.CreateIngestionStreamRequest = {
            "collection_id": collection_id,
            "ingestion_stream_name": ingestion_stream_name,
            "index_name": index_name,
            "source": source,
            "role_arn": role_arn,
        }
        if failure_index_name is not None:
            input_["failure_index_name"] = failure_index_name
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_stream_id: "capo_opensearchserverless.types.ingestion_stream_id.IngestionStreamId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_ingestion_stream_response.GetIngestionStreamResponse":
        """<p>Returns information about an ingestion stream, including its configuration, status, and processing state.</p>

        Args:
            collection_id: <p>The unique identifier of the collection that the ingestion stream belongs to.</p>
            ingestion_stream_id: <p>The unique identifier of the ingestion stream to retrieve.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.get_ingestion_stream_request.GetIngestionStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.get_ingestion_stream_response.GetIngestionStreamResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_ingestion_stream

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.get_ingestion_stream.async_get_ingestion_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIngestionStream")
        )
        input_: capo_opensearchserverless.types.get_ingestion_stream_request.GetIngestionStreamRequest = {
            "collection_id": collection_id,
            "ingestion_stream_id": ingestion_stream_id,
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
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_stream_id: "capo_opensearchserverless.types.ingestion_stream_id.IngestionStreamId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_ingestion_stream_response.DeleteIngestionStreamResponse":
        """<p>Deletes an ingestion stream. Documents that were already indexed by the stream remain in the index.</p>

        Args:
            collection_id: <p>The unique identifier of the collection that the ingestion stream belongs to.</p>
            ingestion_stream_id: <p>The unique identifier of the ingestion stream to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.delete_ingestion_stream_request.DeleteIngestionStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.delete_ingestion_stream_response.DeleteIngestionStreamResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_ingestion_stream

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.delete_ingestion_stream.async_delete_ingestion_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteIngestionStream")
        )
        input_: capo_opensearchserverless.types.delete_ingestion_stream_request.DeleteIngestionStreamRequest = {
            "collection_id": collection_id,
            "ingestion_stream_id": ingestion_stream_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_ingestion_streams_response.ListIngestionStreamsResponse":
        """<p>Returns a list of ingestion streams in a collection.</p>

        Args:
            collection_id: <p>The unique identifier of the collection to list ingestion streams for.</p>
            next_token: <p>If your initial <code>ListIngestionStreams</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListIngestionStreams</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Valid values are 1–100. If you don't specify a value, the default is 100. You can use <code>nextToken</code> to get the next page of results.</p> <p>A response can contain fewer results than <code>maxResults</code>, or no results, and still include a <code>nextToken</code>. To retrieve all results, continue to make the call with the returned <code>nextToken</code> until no <code>nextToken</code> is returned.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.list_ingestion_streams_request.ListIngestionStreamsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.list_ingestion_streams_response.ListIngestionStreamsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_ingestion_streams

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.list_ingestion_streams.async_list_ingestion_streams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIngestionStreams")
        )
        input_: capo_opensearchserverless.types.list_ingestion_streams_request.ListIngestionStreamsRequest = {
            "collection_id": collection_id
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
