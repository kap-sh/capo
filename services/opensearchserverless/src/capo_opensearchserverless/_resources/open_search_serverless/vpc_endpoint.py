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
    import capo_opensearchserverless.types.create_vpc_endpoint_request
    import capo_opensearchserverless.types.create_vpc_endpoint_response
    import capo_opensearchserverless.types.delete_vpc_endpoint_request
    import capo_opensearchserverless.types.delete_vpc_endpoint_response
    import capo_opensearchserverless.types.list_vpc_endpoints_request
    import capo_opensearchserverless.types.list_vpc_endpoints_response
    import capo_opensearchserverless.types.security_group_ids
    import capo_opensearchserverless.types.subnet_ids
    import capo_opensearchserverless.types.vpc_endpoint_filters
    import capo_opensearchserverless.types.vpc_endpoint_id
    import capo_opensearchserverless.types.vpc_endpoint_name
    import capo_opensearchserverless.types.vpc_id
    from capo_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from capo_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class VpcEndpoint:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName",
        vpc_id: "capo_opensearchserverless.types.vpc_id.VpcId",
        subnet_ids: "capo_opensearchserverless.types.subnet_ids.SubnetIds",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        security_group_ids: Optional[
            "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an OpenSearch Serverless-managed interface VPC endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            name: <p>The name of the interface endpoint.</p>
            vpc_id: <p>The ID of the VPC from which you'll access OpenSearch Serverless.</p>
            subnet_ids: <p>The ID of one or more subnets from which you'll access OpenSearch Serverless.</p>
            security_group_ids: <p>The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint.create_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {
            "name": name,
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
        }
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
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
        id: "capo_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an OpenSearch Serverless-managed interface endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            id: <p>The VPC endpoint identifier.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint.delete_vpc_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {
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
        vpc_endpoint_filters: Optional[
            "capo_opensearchserverless.types.vpc_endpoint_filters.VpcEndpointFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse":
        """<p>Returns the OpenSearch Serverless-managed interface VPC endpoints associated with the current account. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            vpc_endpoint_filters: <p>Filter the results according to the current status of the VPC endpoint. Possible statuses are <code>CREATING</code>, <code>DELETING</code>, <code>UPDATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>
            next_token: <p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page. </p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> OperationResponse[
            "capo_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints

            output, http_response = (
                capo_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints.list_vpc_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}
        if vpc_endpoint_filters is not None:
            input_["vpc_endpoint_filters"] = vpc_endpoint_filters
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


class AsyncVpcEndpoint:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName",
        vpc_id: "capo_opensearchserverless.types.vpc_id.VpcId",
        subnet_ids: "capo_opensearchserverless.types.subnet_ids.SubnetIds",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        security_group_ids: Optional[
            "capo_opensearchserverless.types.security_group_ids.SecurityGroupIds"
        ] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse":
        """<p>Creates an OpenSearch Serverless-managed interface VPC endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            name: <p>The name of the interface endpoint.</p>
            vpc_id: <p>The ID of the VPC from which you'll access OpenSearch Serverless.</p>
            subnet_ids: <p>The ID of one or more subnets from which you'll access OpenSearch Serverless.</p>
            security_group_ids: <p>The unique identifiers of the security groups that define the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Thrown when you attempt to create more resources than the service allows based on service quotas.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.create_vpc_endpoint_response.CreateVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.create_vpc_endpoint.async_create_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.create_vpc_endpoint_request.CreateVpcEndpointRequest = {
            "name": name,
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
        }
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
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
        id: "capo_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "capo_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse":
        """<p>Deletes an OpenSearch Serverless-managed interface endpoint. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            id: <p>The VPC endpoint identifier.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_opensearchserverless.errors.conflict_exception.ConflictException: <p>When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE_FAILED state.</p>
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Thrown when accessing or deleting a resource that does not exist.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.delete_vpc_endpoint_response.DeleteVpcEndpointResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.delete_vpc_endpoint.async_delete_vpc_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.delete_vpc_endpoint_request.DeleteVpcEndpointRequest = {
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
        vpc_endpoint_filters: Optional[
            "capo_opensearchserverless.types.vpc_endpoint_filters.VpcEndpointFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse":
        """<p>Returns the OpenSearch Serverless-managed interface VPC endpoints associated with the current account. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html">Access Amazon OpenSearch Serverless using an interface endpoint</a>.</p>

        Args:
            vpc_endpoint_filters: <p>Filter the results according to the current status of the VPC endpoint. Possible statuses are <code>CREATING</code>, <code>DELETING</code>, <code>UPDATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>
            next_token: <p>If your initial <code>ListVpcEndpoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVpcEndpoints</code> operations, which returns results in the next page. </p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>

        Raises:
            capo_opensearchserverless.errors.internal_server_exception.InternalServerException: <p>Thrown when an error internal to the service occurs while processing a request.</p>
            capo_opensearchserverless.errors.validation_exception.ValidationException: <p>Thrown when the HTTP request contains invalid input or is missing required input.</p>
            capo_opensearchserverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_opensearchserverless.types.list_vpc_endpoints_response.ListVpcEndpointsResponse"
        ]:
            import capo_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints

            (
                output,
                http_response,
            ) = await capo_opensearchserverless._operations.open_search_serverless.list_vpc_endpoints.async_list_vpc_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_opensearchserverless.types.list_vpc_endpoints_request.ListVpcEndpointsRequest = {}
        if vpc_endpoint_filters is not None:
            input_["vpc_endpoint_filters"] = vpc_endpoint_filters
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
