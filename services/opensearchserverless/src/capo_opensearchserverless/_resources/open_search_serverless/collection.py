from __future__ import annotations

import uuid
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
    import capo_opensearchserverless.types.client_token
    import capo_opensearchserverless.types.collection_filters
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.collection_name
    import capo_opensearchserverless.types.collection_type
    import capo_opensearchserverless.types.create_collection_request
    import capo_opensearchserverless.types.create_collection_response
    import capo_opensearchserverless.types.delete_collection_request
    import capo_opensearchserverless.types.delete_collection_response
    import capo_opensearchserverless.types.deletion_protection
    import capo_opensearchserverless.types.encryption_config
    import capo_opensearchserverless.types.list_collections_request
    import capo_opensearchserverless.types.list_collections_response
    import capo_opensearchserverless.types.standby_replicas
    import capo_opensearchserverless.types.tags
    import capo_opensearchserverless.types.update_collection_request
    import capo_opensearchserverless.types.update_collection_response
    import capo_opensearchserverless.types.vector_options
    from capo_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from capo_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class Collection:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_opensearchserverless.types.collection_name.CollectionName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        type: Optional[
            "capo_opensearchserverless.types.collection_type.CollectionType"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        standby_replicas: Optional[
            "capo_opensearchserverless.types.standby_replicas.StandbyReplicas"
        ] = None,
        vector_options: Optional[
            "capo_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        collection_group_name: Optional[
            "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
        ] = None,
        encryption_config: Optional[
            "capo_opensearchserverless.types.encryption_config.EncryptionConfig"
        ] = None,
        deletion_protection: Optional[
            "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_collection_response.CreateCollectionResponse":
        """<p>Creates a new OpenSearch Serverless collection. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            name: <p>Name of the collection.</p>
            type: <p>The type of collection.</p>
            description: <p>Description of the collection.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            collection_group_name: <p>The name of the collection group to associate with the collection.</p>
            encryption_config: <p>Encryption settings for the collection.</p>
            deletion_protection: <p>Indicates whether to enable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.ocu_limit_exceeded_exception.OcuLimitExceededException: <p>Thrown when the collection you're attempting to create results in a number of search or indexing OCUs that exceeds the account limit. </p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_collection_request.CreateCollectionRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_collection_response.CreateCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_collection

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_collection.create_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_collection_request.CreateCollectionRequest = {
            "name": name
        }
        if type is not None:
            input_["type"] = type
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if standby_replicas is not None:
            input_["standby_replicas"] = standby_replicas
        if vector_options is not None:
            input_["vector_options"] = vector_options
        if collection_group_name is not None:
            input_["collection_group_name"] = collection_group_name
        if encryption_config is not None:
            input_["encryption_config"] = encryption_config
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
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

    def update(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        vector_options: Optional[
            "capo_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        deletion_protection: Optional[
            "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_collection_response.UpdateCollectionResponse":
        """<p>Updates an OpenSearch Serverless collection.</p>

        Args:
            id: <p>The unique identifier of the collection.</p>
            description: <p>A description of the collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            deletion_protection: <p>Indicates whether to enable or disable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_collection_request.UpdateCollectionRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_collection_response.UpdateCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_collection

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_collection.update_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_collection_request.UpdateCollectionRequest = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if vector_options is not None:
            input_["vector_options"] = vector_options
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
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

    def delete(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse":
        """<p>Deletes an OpenSearch Serverless collection. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection. For example, <code>1iu5usc406kd</code>. The ID is part of the collection endpoint. You can also retrieve it using the <a href="https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html">ListCollections</a> API.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_collection

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_collection.delete_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest = {
            "id": id
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
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        collection_filters: Optional[
            "capo_opensearchserverless.types.collection_filters.CollectionFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_collections_response.ListCollectionsResponse":
        """<p>Lists all OpenSearch Serverless collections. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p> <note> <p>Make sure to include an empty request body {} if you don't include any collection filters in the request.</p> </note>

        Args:
            collection_filters: <p> A list of filter names and values that you can use for requests.</p>
            next_token: <p>If your initial <code>ListCollections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollections</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_collections_request.ListCollectionsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_collections_response.ListCollectionsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_collections

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_collections.list_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_collections_request.ListCollectionsRequest = {}
        if collection_filters is not None:
            input_["collection_filters"] = collection_filters
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


class AsyncCollection:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_opensearchserverless.types.collection_name.CollectionName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        type: Optional[
            "capo_opensearchserverless.types.collection_type.CollectionType"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        standby_replicas: Optional[
            "capo_opensearchserverless.types.standby_replicas.StandbyReplicas"
        ] = None,
        vector_options: Optional[
            "capo_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        collection_group_name: Optional[
            "capo_opensearchserverless.types.collection_group_name.CollectionGroupName"
        ] = None,
        encryption_config: Optional[
            "capo_opensearchserverless.types.encryption_config.EncryptionConfig"
        ] = None,
        deletion_protection: Optional[
            "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_collection_response.CreateCollectionResponse":
        """<p>Creates a new OpenSearch Serverless collection. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            name: <p>Name of the collection.</p>
            type: <p>The type of collection.</p>
            description: <p>Description of the collection.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            collection_group_name: <p>The name of the collection group to associate with the collection.</p>
            encryption_config: <p>Encryption settings for the collection.</p>
            deletion_protection: <p>Indicates whether to enable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.ocu_limit_exceeded_exception.OcuLimitExceededException: <p>Thrown when the collection you're attempting to create results in a number of search or indexing OCUs that exceeds the account limit. </p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_collection_request.CreateCollectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_collection_response.CreateCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_collection

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_collection.async_create_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_collection_request.CreateCollectionRequest = {
            "name": name
        }
        if type is not None:
            input_["type"] = type
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if standby_replicas is not None:
            input_["standby_replicas"] = standby_replicas
        if vector_options is not None:
            input_["vector_options"] = vector_options
        if collection_group_name is not None:
            input_["collection_group_name"] = collection_group_name
        if encryption_config is not None:
            input_["encryption_config"] = encryption_config
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
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

    async def update(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        vector_options: Optional[
            "capo_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        deletion_protection: Optional[
            "capo_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_collection_response.UpdateCollectionResponse":
        """<p>Updates an OpenSearch Serverless collection.</p>

        Args:
            id: <p>The unique identifier of the collection.</p>
            description: <p>A description of the collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            deletion_protection: <p>Indicates whether to enable or disable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.update_collection_request.UpdateCollectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.update_collection_response.UpdateCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_collection

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.update_collection.async_update_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_collection_request.UpdateCollectionRequest = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if vector_options is not None:
            input_["vector_options"] = vector_options
        if deletion_protection is not None:
            input_["deletion_protection"] = deletion_protection
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

    async def delete(
        self,
        id: "capo_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse":
        """<p>Deletes an OpenSearch Serverless collection. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection. For example, <code>1iu5usc406kd</code>. The ID is part of the collection endpoint. You can also retrieve it using the <a href="https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html">ListCollections</a> API.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_collection

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.delete_collection.async_delete_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest = {
            "id": id
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
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        collection_filters: Optional[
            "capo_opensearchserverless.types.collection_filters.CollectionFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_collections_response.ListCollectionsResponse":
        """<p>Lists all OpenSearch Serverless collections. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p> <note> <p>Make sure to include an empty request body {} if you don't include any collection filters in the request.</p> </note>

        Args:
            collection_filters: <p> A list of filter names and values that you can use for requests.</p>
            next_token: <p>If your initial <code>ListCollections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollections</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.list_collections_request.ListCollectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.list_collections_response.ListCollectionsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_collections

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.list_collections.async_list_collections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_collections_request.ListCollectionsRequest = {}
        if collection_filters is not None:
            input_["collection_filters"] = collection_filters
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
