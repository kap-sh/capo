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
    import capo_opensearchserverless.types.collection_group_capacity_limits
    import capo_opensearchserverless.types.collection_group_id
    import capo_opensearchserverless.types.collection_group_name
    import capo_opensearchserverless.types.create_collection_group_request
    import capo_opensearchserverless.types.create_collection_group_response
    import capo_opensearchserverless.types.delete_collection_group_request
    import capo_opensearchserverless.types.delete_collection_group_response
    import capo_opensearchserverless.types.list_collection_groups_request
    import capo_opensearchserverless.types.list_collection_groups_response
    import capo_opensearchserverless.types.serverless_generation
    import capo_opensearchserverless.types.standby_replicas
    import capo_opensearchserverless.types.tags
    import capo_opensearchserverless.types.update_collection_group_request
    import capo_opensearchserverless.types.update_collection_group_response
    from capo_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from capo_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class CollectionGroup:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_opensearchserverless.types.collection_group_name.CollectionGroupName",
        standby_replicas: "capo_opensearchserverless.types.standby_replicas.StandbyReplicas",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        capacity_limits: Optional[
            "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        generation: Optional[
            "capo_opensearchserverless.types.serverless_generation.ServerlessGeneration"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse":
        """<p>Creates a collection group within OpenSearch Serverless. Collection groups let you manage OpenSearch Compute Units (OCUs) at a group level, with multiple collections sharing the group's capacity limits.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups.html">Managing collection groups</a>.</p>

        Args:
            name: <p>The name of the collection group.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection group.</p>
            description: <p>A description of the collection group.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.</p>
            capacity_limits: <p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.</p>
            generation: <p>The generation of Amazon OpenSearch Serverless for the collection group. Valid values are <code>CLASSIC</code> and <code>NEXTGEN</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_collection_group

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_collection_group.create_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest = {
            "name": name,
            "standby_replicas": standby_replicas,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
        if generation is not None:
            input_["generation"] = generation
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
        id: "capo_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        capacity_limits: Optional[
            "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse":
        """<p>Updates the description and capacity limits of a collection group.</p>

        Args:
            id: <p>The unique identifier of the collection group to update.</p>
            description: <p>A new description for the collection group.</p>
            capacity_limits: <p>Updated capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_collection_group

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.update_collection_group.update_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
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
        id: "capo_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse":
        """<p>Deletes a collection group. You can only delete empty collection groups that contain no collections. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection group to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_collection_group

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_collection_group.delete_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest = {
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
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse":
        """<p>Returns a list of collection groups. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            next_token: <p>If your initial <code>ListCollectionGroups</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollectionGroups</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_collection_groups

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_collection_groups.list_collection_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest = {}
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


class AsyncCollectionGroup:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_opensearchserverless.types.collection_group_name.CollectionGroupName",
        standby_replicas: "capo_opensearchserverless.types.standby_replicas.StandbyReplicas",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["capo_opensearchserverless.types.tags.Tags"] = None,
        capacity_limits: Optional[
            "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        generation: Optional[
            "capo_opensearchserverless.types.serverless_generation.ServerlessGeneration"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse":
        """<p>Creates a collection group within OpenSearch Serverless. Collection groups let you manage OpenSearch Compute Units (OCUs) at a group level, with multiple collections sharing the group's capacity limits.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups.html">Managing collection groups</a>.</p>

        Args:
            name: <p>The name of the collection group.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection group.</p>
            description: <p>A description of the collection group.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.</p>
            capacity_limits: <p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.</p>
            generation: <p>The generation of Amazon OpenSearch Serverless for the collection group. Valid values are <code>CLASSIC</code> and <code>NEXTGEN</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_collection_group

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_collection_group.async_create_collection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest = {
            "name": name,
            "standby_replicas": standby_replicas,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
        if generation is not None:
            input_["generation"] = generation
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
        id: "capo_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        capacity_limits: Optional[
            "capo_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse":
        """<p>Updates the description and capacity limits of a collection group.</p>

        Args:
            id: <p>The unique identifier of the collection group to update.</p>
            description: <p>A new description for the collection group.</p>
            capacity_limits: <p>Updated capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.update_collection_group

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.update_collection_group.async_update_collection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if capacity_limits is not None:
            input_["capacity_limits"] = capacity_limits
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
        id: "capo_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse":
        """<p>Deletes a collection group. You can only delete empty collection groups that contain no collections. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection group to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_collection_group

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.delete_collection_group.async_delete_collection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest = {
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
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse":
        """<p>Returns a list of collection groups. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            next_token: <p>If your initial <code>ListCollectionGroups</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollectionGroups</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_collection_groups

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.list_collection_groups.async_list_collection_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest = {}
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
