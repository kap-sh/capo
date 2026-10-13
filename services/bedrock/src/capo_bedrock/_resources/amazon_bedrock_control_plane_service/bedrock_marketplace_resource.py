from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock._auth._signers
import capo_bedrock._auth._sigv4
from capo_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock.types.accept_eula
    import capo_bedrock.types.arn
    import capo_bedrock.types.create_marketplace_model_endpoint_request
    import capo_bedrock.types.create_marketplace_model_endpoint_response
    import capo_bedrock.types.delete_marketplace_model_endpoint_request
    import capo_bedrock.types.delete_marketplace_model_endpoint_response
    import capo_bedrock.types.deregister_marketplace_model_endpoint_request
    import capo_bedrock.types.deregister_marketplace_model_endpoint_response
    import capo_bedrock.types.endpoint_config
    import capo_bedrock.types.endpoint_name
    import capo_bedrock.types.get_marketplace_model_endpoint_request
    import capo_bedrock.types.get_marketplace_model_endpoint_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.list_marketplace_model_endpoints_request
    import capo_bedrock.types.list_marketplace_model_endpoints_response
    import capo_bedrock.types.marketplace_model_endpoint_summary
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_source_identifier
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.register_marketplace_model_endpoint_request
    import capo_bedrock.types.register_marketplace_model_endpoint_response
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.update_marketplace_model_endpoint_request
    import capo_bedrock.types.update_marketplace_model_endpoint_response
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class BedrockMarketplaceResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_marketplace_model_endpoint(
        self,
        model_source_identifier: "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        endpoint_config: "capo_bedrock.types.endpoint_config.EndpointConfig",
        endpoint_name: "capo_bedrock.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        accept_eula: Optional["capo_bedrock.types.accept_eula.AcceptEula"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse":
        """<p>Creates an endpoint for a model from Amazon Bedrock Marketplace. The endpoint is hosted by Amazon SageMaker.</p>

        Args:
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that you want to deploy to the endpoint.</p>
            endpoint_config: <p>The configuration for the endpoint, including the number and type of instances to use.</p>
            accept_eula: <p>Indicates whether you accept the end-user license agreement (EULA) for the model. Set to <code>true</code> to accept the EULA.</p>
            endpoint_name: <p>The name of the endpoint. This name must be unique within your Amazon Web Services account and region.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>
            tags: <p>An array of key-value pairs to apply to the underlying Amazon SageMaker endpoint. You can use these tags to organize and identify your Amazon Web Services resources.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint.create_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest = {
            "model_source_identifier": model_source_identifier,
            "endpoint_config": endpoint_config,
            "endpoint_name": endpoint_name,
        }
        if accept_eula is not None:
            input_["accept_eula"] = accept_eula
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse":
        """<p>Deletes an endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint.delete_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse":
        """<p>Deregisters an endpoint for a model from Amazon Bedrock Marketplace. This operation removes the endpoint's association with Amazon Bedrock but does not delete the underlying Amazon SageMaker endpoint.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to deregister.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint.deregister_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse":
        """<p>Retrieves details about a specific endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to get information about.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint.get_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_marketplace_model_endpoints(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        model_source_equals: Optional[
            "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier"
        ] = None,
    ) -> "capo_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse":
        """<p>Lists the endpoints for models from Amazon Bedrock Marketplace in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. If more results are available, the operation returns a <code>NextToken</code> value.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous <code>ListMarketplaceModelEndpoints</code> call.</p>
            model_source_equals: <p>If specified, only endpoints for the given model source identifier are returned.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints.list_marketplace_model_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMarketplaceModelEndpoints")
        )
        input_: capo_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if model_source_equals is not None:
            input_["model_source_equals"] = model_source_equals

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_marketplace_model_endpoint(
        self,
        endpoint_identifier: "capo_bedrock.types.arn.Arn",
        model_source_identifier: "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse":
        """<p>Registers an existing Amazon SageMaker endpoint with Amazon Bedrock Marketplace, allowing it to be used with Amazon Bedrock APIs.</p>

        Args:
            endpoint_identifier: <p>The ARN of the Amazon SageMaker endpoint you want to register with Amazon Bedrock Marketplace.</p>
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on the endpoint.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint.register_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest = {
            "endpoint_identifier": endpoint_identifier,
            "model_source_identifier": model_source_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        endpoint_config: "capo_bedrock.types.endpoint_config.EndpointConfig",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse":
        """<p>Updates the configuration of an existing endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to update.</p>
            endpoint_config: <p>The new configuration for the endpoint, including the number and type of instances to use.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint.update_marketplace_model_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn,
            "endpoint_config": endpoint_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncBedrockMarketplaceResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_marketplace_model_endpoint(
        self,
        model_source_identifier: "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        endpoint_config: "capo_bedrock.types.endpoint_config.EndpointConfig",
        endpoint_name: "capo_bedrock.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        accept_eula: Optional["capo_bedrock.types.accept_eula.AcceptEula"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse":
        """<p>Creates an endpoint for a model from Amazon Bedrock Marketplace. The endpoint is hosted by Amazon SageMaker.</p>

        Args:
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that you want to deploy to the endpoint.</p>
            endpoint_config: <p>The configuration for the endpoint, including the number and type of instances to use.</p>
            accept_eula: <p>Indicates whether you accept the end-user license agreement (EULA) for the model. Set to <code>true</code> to accept the EULA.</p>
            endpoint_name: <p>The name of the endpoint. This name must be unique within your Amazon Web Services account and region.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>
            tags: <p>An array of key-value pairs to apply to the underlying Amazon SageMaker endpoint. You can use these tags to organize and identify your Amazon Web Services resources.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint.async_create_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest = {
            "model_source_identifier": model_source_identifier,
            "endpoint_config": endpoint_config,
            "endpoint_name": endpoint_name,
        }
        if accept_eula is not None:
            input_["accept_eula"] = accept_eula
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse":
        """<p>Deletes an endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint.async_delete_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse":
        """<p>Deregisters an endpoint for a model from Amazon Bedrock Marketplace. This operation removes the endpoint's association with Amazon Bedrock but does not delete the underlying Amazon SageMaker endpoint.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to deregister.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint.async_deregister_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse":
        """<p>Retrieves details about a specific endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to get information about.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint.async_get_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_marketplace_model_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        model_source_equals: Optional[
            "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier"
        ] = None,
    ) -> "capo_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse":
        """<p>Lists the endpoints for models from Amazon Bedrock Marketplace in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. If more results are available, the operation returns a <code>NextToken</code> value.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous <code>ListMarketplaceModelEndpoints</code> call.</p>
            model_source_equals: <p>If specified, only endpoints for the given model source identifier are returned.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints.async_list_marketplace_model_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMarketplaceModelEndpoints")
        )
        input_: capo_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if model_source_equals is not None:
            input_["model_source_equals"] = model_source_equals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_marketplace_model_endpoint(
        self,
        endpoint_identifier: "capo_bedrock.types.arn.Arn",
        model_source_identifier: "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse":
        """<p>Registers an existing Amazon SageMaker endpoint with Amazon Bedrock Marketplace, allowing it to be used with Amazon Bedrock APIs.</p>

        Args:
            endpoint_identifier: <p>The ARN of the Amazon SageMaker endpoint you want to register with Amazon Bedrock Marketplace.</p>
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on the endpoint.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint.async_register_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest = {
            "endpoint_identifier": endpoint_identifier,
            "model_source_identifier": model_source_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        endpoint_config: "capo_bedrock.types.endpoint_config.EndpointConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse":
        """<p>Updates the configuration of an existing endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to update.</p>
            endpoint_config: <p>The new configuration for the endpoint, including the number and type of instances to use.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint.async_update_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateMarketplaceModelEndpoint")
        )
        input_: capo_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn,
            "endpoint_config": endpoint_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
