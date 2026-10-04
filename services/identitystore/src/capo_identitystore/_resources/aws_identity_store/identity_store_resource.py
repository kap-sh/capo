from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_identitystore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_identitystore.types.describe_identity_store_request
    import capo_identitystore.types.describe_identity_store_response
    import capo_identitystore.types.identity_store
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.list_identity_stores_request
    import capo_identitystore.types.list_identity_stores_response
    import capo_identitystore.types.max_results
    import capo_identitystore.types.network_configuration
    import capo_identitystore.types.next_token
    import capo_identitystore.types.update_identity_store_request
    import capo_identitystore.types.update_identity_store_response
    from capo_identitystore._services.async_identitystore import (
        AsyncidentitystoreClient,
        AsyncidentitystoreClientConfig,
    )
    from capo_identitystore._services.identitystore import (
        identitystoreClient,
        identitystoreClientConfig,
    )


class IdentityStoreResource:
    def __init__(self, service: identitystoreClient) -> None:
        self._service = service

    def read(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.describe_identity_store_response.DescribeIdentityStoreResponse":
        """<p>Retrieves details about the specified identity store, including its Amazon Resource Name (ARN) and network configuration.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.describe_identity_store_request.DescribeIdentityStoreRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.describe_identity_store_response.DescribeIdentityStoreResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.describe_identity_store

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.describe_identity_store.describe_identity_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.describe_identity_store_request.DescribeIdentityStoreRequest = {
            "identity_store_id": identity_store_id
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
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        network_configuration: Optional[
            "capo_identitystore.types.network_configuration.NetworkConfiguration"
        ] = None,
    ) -> "capo_identitystore.types.update_identity_store_response.UpdateIdentityStoreResponse":
        """<p>Updates the configuration of the specified identity store, including its network configuration.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            network_configuration: <p>The network configuration to apply to the identity store. This controls whether access through a virtual private cloud (VPC) endpoint is required and the source VPCs and IP addresses that are allowed to access the identity store.</p> <p>When you provide <code>NetworkConfiguration</code> in a request, the service performs a full replacement of the identity store's current network configuration with the values you specify. Any values that you omit are cleared. To preserve or change the allowed source VPCs or IP address ranges, include the complete set of values that you want in the request. To clear a list, omit it; an empty list is not accepted.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.update_identity_store_request.UpdateIdentityStoreRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.update_identity_store_response.UpdateIdentityStoreResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.update_identity_store

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.update_identity_store.update_identity_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.update_identity_store_request.UpdateIdentityStoreRequest = {
            "identity_store_id": identity_store_id
        }
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration

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
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "capo_identitystore.types.list_identity_stores_response.ListIdentityStoresResponse":
        """<p>Lists the identity stores that you have access to. This operation returns only the identity store ID and Amazon Resource Name (ARN) of each identity store. To obtain additional information about an identity store, call <code>DescribeIdentityStore</code>.</p> <p>This operation returns results in paginated form. Use the <code>NextToken</code> parameter to retrieve additional pages of results.</p>

        Args:
            max_results: <p>The maximum number of results to return per request. This parameter is used in all <code> List</code> operations to specify how many results to return on one page. If you don't specify a value, the operation uses a default page size.</p>
            next_token: <p>The pagination token used for the <code>ListIdentityStores</code> API operation. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to retrieve the next page of results.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_identitystore.types.list_identity_stores_request.ListIdentityStoresRequest]",
        ) -> OperationResponse[
            "capo_identitystore.types.list_identity_stores_response.ListIdentityStoresResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_identity_stores

            output, http_response = (
                capo_identitystore._operations.aws_identity_store.list_identity_stores.list_identity_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.list_identity_stores_request.ListIdentityStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncIdentityStoreResource:
    def __init__(self, service: AsyncidentitystoreClient) -> None:
        self._service = service

    async def read(
        self,
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "capo_identitystore.types.describe_identity_store_response.DescribeIdentityStoreResponse":
        """<p>Retrieves details about the specified identity store, including its Amazon Resource Name (ARN) and network configuration.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.describe_identity_store_request.DescribeIdentityStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.describe_identity_store_response.DescribeIdentityStoreResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.describe_identity_store

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.describe_identity_store.async_describe_identity_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.describe_identity_store_request.DescribeIdentityStoreRequest = {
            "identity_store_id": identity_store_id
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
        identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        network_configuration: Optional[
            "capo_identitystore.types.network_configuration.NetworkConfiguration"
        ] = None,
    ) -> "capo_identitystore.types.update_identity_store_response.UpdateIdentityStoreResponse":
        """<p>Updates the configuration of the specified identity store, including its network configuration.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>
            network_configuration: <p>The network configuration to apply to the identity store. This controls whether access through a virtual private cloud (VPC) endpoint is required and the source VPCs and IP addresses that are allowed to access the identity store.</p> <p>When you provide <code>NetworkConfiguration</code> in a request, the service performs a full replacement of the identity store's current network configuration with the values you specify. Any values that you omit are cleared. To preserve or change the allowed source VPCs or IP address ranges, include the complete set of values that you want in the request. To clear a list, omit it; an empty list is not accepted.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            capo_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.update_identity_store_request.UpdateIdentityStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.update_identity_store_response.UpdateIdentityStoreResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.update_identity_store

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.update_identity_store.async_update_identity_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.update_identity_store_request.UpdateIdentityStoreRequest = {
            "identity_store_id": identity_store_id
        }
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration

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
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        max_results: Optional["capo_identitystore.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_identitystore.types.next_token.NextToken"] = None,
    ) -> "capo_identitystore.types.list_identity_stores_response.ListIdentityStoresResponse":
        """<p>Lists the identity stores that you have access to. This operation returns only the identity store ID and Amazon Resource Name (ARN) of each identity store. To obtain additional information about an identity store, call <code>DescribeIdentityStore</code>.</p> <p>This operation returns results in paginated form. Use the <code>NextToken</code> parameter to retrieve additional pages of results.</p>

        Args:
            max_results: <p>The maximum number of results to return per request. This parameter is used in all <code> List</code> operations to specify how many results to return on one page. If you don't specify a value, the operation uses a default page size.</p>
            next_token: <p>The pagination token used for the <code>ListIdentityStores</code> API operation. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to retrieve the next page of results.</p>

        Raises:
            capo_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            capo_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            capo_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            capo_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_identitystore.types.list_identity_stores_request.ListIdentityStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_identitystore.types.list_identity_stores_response.ListIdentityStoresResponse"
        ]:
            import capo_identitystore._operations.aws_identity_store.list_identity_stores

            (
                output,
                http_response,
            ) = await capo_identitystore._operations.aws_identity_store.list_identity_stores.async_list_identity_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_identitystore.types.list_identity_stores_request.ListIdentityStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
