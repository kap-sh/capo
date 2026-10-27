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
    import capo_opensearchserverless.types.cancel_ingestion_job_request
    import capo_opensearchserverless.types.cancel_ingestion_job_response
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.create_ingestion_job_request
    import capo_opensearchserverless.types.create_ingestion_job_response
    import capo_opensearchserverless.types.get_ingestion_job_request
    import capo_opensearchserverless.types.get_ingestion_job_response
    import capo_opensearchserverless.types.ingestion_index_name
    import capo_opensearchserverless.types.ingestion_job_id
    import capo_opensearchserverless.types.ingestion_job_name
    import capo_opensearchserverless.types.ingestion_job_source
    import capo_opensearchserverless.types.ingestion_job_summary
    import capo_opensearchserverless.types.list_ingestion_jobs_request
    import capo_opensearchserverless.types.list_ingestion_jobs_response
    import capo_opensearchserverless.types.tags
    from capo_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from capo_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class IngestionJob:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_job_name: "capo_opensearchserverless.types.ingestion_job_name.IngestionJobName",
        index_name: "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName",
        source: "capo_opensearchserverless.types.ingestion_job_source.IngestionJobSource",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        failure_index_name: Optional[
            "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
        ] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_ingestion_job_response.CreateIngestionJobResponse":
        """<p>Creates an ingestion job that performs a one-time bulk ingestion of data from an Amazon S3 bucket into an index in an OpenSearch Serverless collection. An ingestion job scans the source bucket, indexes the documents it finds, and then completes. To continuously ingest new data as it arrives, use <code>CreateIngestionStream</code> instead.</p>

        Args:
            collection_id: <p>The unique identifier of the collection to ingest data into.</p>
            ingestion_job_name: <p>The name of the ingestion job. The name must be unique within the collection.</p>
            index_name: <p>The name of the index to ingest documents into.</p>
            failure_index_name: <p>The name of the index where documents that fail to be ingested are recorded.</p>
            source: <p>The Amazon S3 source to ingest data from.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the ingestion job.</p>
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
            req: "OperationRequest[capo_opensearchserverless.types.create_ingestion_job_request.CreateIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_ingestion_job_response.CreateIngestionJobResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_ingestion_job

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_ingestion_job.create_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateIngestionJob")
        )
        input_: capo_opensearchserverless.types.create_ingestion_job_request.CreateIngestionJobRequest = {
            "collection_id": collection_id,
            "ingestion_job_name": ingestion_job_name,
            "index_name": index_name,
            "source": source,
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
        ingestion_job_id: "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_ingestion_job_response.GetIngestionJobResponse":
        """<p>Returns information about an ingestion job, including its configuration, status, and processing state.</p>

        Args:
            collection_id: <p>The unique identifier of the collection that the ingestion job belongs to.</p>
            ingestion_job_id: <p>The unique identifier of the ingestion job to retrieve.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.get_ingestion_job_request.GetIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.get_ingestion_job_response.GetIngestionJobResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_ingestion_job

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.get_ingestion_job.get_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIngestionJob")
        )
        input_: capo_opensearchserverless.types.get_ingestion_job_request.GetIngestionJobRequest = {
            "collection_id": collection_id,
            "ingestion_job_id": ingestion_job_id,
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
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_ingestion_jobs_response.ListIngestionJobsResponse":
        """<p>Returns a list of ingestion jobs in a collection.</p>

        Args:
            collection_id: <p>The unique identifier of the collection to list ingestion jobs for.</p>
            next_token: <p>If your initial <code>ListIngestionJobs</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListIngestionJobs</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Valid values are 1–100. If you don't specify a value, the default is 100. You can use <code>nextToken</code> to get the next page of results.</p> <p>A response can contain fewer results than <code>maxResults</code>, or no results, and still include a <code>nextToken</code>. To retrieve all results, continue to make the call with the returned <code>nextToken</code> until no <code>nextToken</code> is returned.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_ingestion_jobs_request.ListIngestionJobsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_ingestion_jobs_response.ListIngestionJobsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_ingestion_jobs

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_ingestion_jobs.list_ingestion_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIngestionJobs")
        )
        input_: capo_opensearchserverless.types.list_ingestion_jobs_request.ListIngestionJobsRequest = {
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

    def cancel_ingestion_job(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_job_id: "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.cancel_ingestion_job_response.CancelIngestionJobResponse":
        """<p>Cancels an in-progress ingestion job. Documents that were already indexed before the cancellation remain in the index.</p>

        Args:
            collection_id: <p>The unique identifier of the collection that the ingestion job belongs to.</p>
            ingestion_job_id: <p>The unique identifier of the ingestion job to cancel.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.cancel_ingestion_job_request.CancelIngestionJobRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.cancel_ingestion_job_response.CancelIngestionJobResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.cancel_ingestion_job

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.cancel_ingestion_job.cancel_ingestion_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelIngestionJob")
        )
        input_: capo_opensearchserverless.types.cancel_ingestion_job_request.CancelIngestionJobRequest = {
            "collection_id": collection_id,
            "ingestion_job_id": ingestion_job_id,
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


class AsyncIngestionJob:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_job_name: "capo_opensearchserverless.types.ingestion_job_name.IngestionJobName",
        index_name: "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName",
        source: "capo_opensearchserverless.types.ingestion_job_source.IngestionJobSource",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        failure_index_name: Optional[
            "capo_opensearchserverless.types.ingestion_index_name.IngestionIndexName"
        ] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_ingestion_job_response.CreateIngestionJobResponse":
        """<p>Creates an ingestion job that performs a one-time bulk ingestion of data from an Amazon S3 bucket into an index in an OpenSearch Serverless collection. An ingestion job scans the source bucket, indexes the documents it finds, and then completes. To continuously ingest new data as it arrives, use <code>CreateIngestionStream</code> instead.</p>

        Args:
            collection_id: <p>The unique identifier of the collection to ingest data into.</p>
            ingestion_job_name: <p>The name of the ingestion job. The name must be unique within the collection.</p>
            index_name: <p>The name of the index to ingest documents into.</p>
            failure_index_name: <p>The name of the index where documents that fail to be ingested are recorded.</p>
            source: <p>The Amazon S3 source to ingest data from.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the ingestion job.</p>
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
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_ingestion_job_request.CreateIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_ingestion_job_response.CreateIngestionJobResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_ingestion_job

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_ingestion_job.async_create_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateIngestionJob")
        )
        input_: capo_opensearchserverless.types.create_ingestion_job_request.CreateIngestionJobRequest = {
            "collection_id": collection_id,
            "ingestion_job_name": ingestion_job_name,
            "index_name": index_name,
            "source": source,
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
        ingestion_job_id: "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
    ) -> "capo_opensearchserverless.types.get_ingestion_job_response.GetIngestionJobResponse":
        """<p>Returns information about an ingestion job, including its configuration, status, and processing state.</p>

        Args:
            collection_id: <p>The unique identifier of the collection that the ingestion job belongs to.</p>
            ingestion_job_id: <p>The unique identifier of the ingestion job to retrieve.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.get_ingestion_job_request.GetIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.get_ingestion_job_response.GetIngestionJobResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.get_ingestion_job

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.get_ingestion_job.async_get_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetIngestionJob")
        )
        input_: capo_opensearchserverless.types.get_ingestion_job_request.GetIngestionJobRequest = {
            "collection_id": collection_id,
            "ingestion_job_id": ingestion_job_id,
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
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_ingestion_jobs_response.ListIngestionJobsResponse":
        """<p>Returns a list of ingestion jobs in a collection.</p>

        Args:
            collection_id: <p>The unique identifier of the collection to list ingestion jobs for.</p>
            next_token: <p>If your initial <code>ListIngestionJobs</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListIngestionJobs</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Valid values are 1–100. If you don't specify a value, the default is 100. You can use <code>nextToken</code> to get the next page of results.</p> <p>A response can contain fewer results than <code>maxResults</code>, or no results, and still include a <code>nextToken</code>. To retrieve all results, continue to make the call with the returned <code>nextToken</code> until no <code>nextToken</code> is returned.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.list_ingestion_jobs_request.ListIngestionJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.list_ingestion_jobs_response.ListIngestionJobsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_ingestion_jobs

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.list_ingestion_jobs.async_list_ingestion_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListIngestionJobs")
        )
        input_: capo_opensearchserverless.types.list_ingestion_jobs_request.ListIngestionJobsRequest = {
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

    async def cancel_ingestion_job(
        self,
        collection_id: "capo_opensearchserverless.types.collection_id.CollectionId",
        ingestion_job_id: "capo_opensearchserverless.types.ingestion_job_id.IngestionJobId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.cancel_ingestion_job_response.CancelIngestionJobResponse":
        """<p>Cancels an in-progress ingestion job. Documents that were already indexed before the cancellation remain in the index.</p>

        Args:
            collection_id: <p>The unique identifier of the collection that the ingestion job belongs to.</p>
            ingestion_job_id: <p>The unique identifier of the ingestion job to cancel.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.cancel_ingestion_job_request.CancelIngestionJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.cancel_ingestion_job_response.CancelIngestionJobResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.cancel_ingestion_job

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.cancel_ingestion_job.async_cancel_ingestion_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelIngestionJob")
        )
        input_: capo_opensearchserverless.types.cancel_ingestion_job_request.CancelIngestionJobRequest = {
            "collection_id": collection_id,
            "ingestion_job_id": ingestion_job_id,
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
