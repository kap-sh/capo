from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

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
    import capo_bedrock.types.create_prompt_router_request
    import capo_bedrock.types.create_prompt_router_response
    import capo_bedrock.types.delete_prompt_router_request
    import capo_bedrock.types.delete_prompt_router_response
    import capo_bedrock.types.get_prompt_router_request
    import capo_bedrock.types.get_prompt_router_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.list_prompt_routers_request
    import capo_bedrock.types.list_prompt_routers_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.prompt_router_arn
    import capo_bedrock.types.prompt_router_description
    import capo_bedrock.types.prompt_router_name
    import capo_bedrock.types.prompt_router_summary
    import capo_bedrock.types.prompt_router_target_model
    import capo_bedrock.types.prompt_router_target_models
    import capo_bedrock.types.prompt_router_type
    import capo_bedrock.types.routing_criteria
    import capo_bedrock.types.tag_list
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class PromptRouterResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create(
        self,
        prompt_router_name: "capo_bedrock.types.prompt_router_name.PromptRouterName",
        models: "capo_bedrock.types.prompt_router_target_models.PromptRouterTargetModels",
        routing_criteria: "capo_bedrock.types.routing_criteria.RoutingCriteria",
        fallback_model: "capo_bedrock.types.prompt_router_target_model.PromptRouterTargetModel",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "capo_bedrock.types.prompt_router_description.PromptRouterDescription"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse":
        """<p>Creates a prompt router that manages the routing of requests between multiple foundation models based on the routing criteria.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of your requests. If not specified, the Amazon Web Services SDK automatically generates one for you.</p>
            prompt_router_name: <p>The name of the prompt router. The name must be unique within your Amazon Web Services account in the current region.</p>
            models: <p>A list of foundation models that the prompt router can route requests to. At least one model must be specified.</p>
            description: <p>An optional description of the prompt router to help identify its purpose.</p>
            routing_criteria: <p>The criteria, which is the response quality difference, used to determine how incoming requests are routed to different models.</p>
            fallback_model: <p>The default model to use when the routing criteria is not met.</p>
            tags: <p>An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your Amazon Web Services resources.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router.create_prompt_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_prompt_router_request

            return capo_bedrock.types.create_prompt_router_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePromptRouter", redact_input=_redact_input),
        )
        input_: capo_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest = {
            "prompt_router_name": prompt_router_name,
            "models": models,
            "routing_criteria": routing_criteria,
            "fallback_model": fallback_model,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        prompt_router_arn: "capo_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_prompt_router_response.GetPromptRouterResponse":
        """<p>Retrieves details about a prompt router.</p>

        Args:
            prompt_router_arn: <p>The prompt router's ARN</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_prompt_router_request.GetPromptRouterRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_prompt_router_response.GetPromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router.get_prompt_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_prompt_router_response.GetPromptRouterResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_prompt_router_response

            return capo_bedrock.types.get_prompt_router_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPromptRouter", redact_output=_redact_output),
        )
        input_: capo_bedrock.types.get_prompt_router_request.GetPromptRouterRequest = {
            "prompt_router_arn": prompt_router_arn
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
        prompt_router_arn: "capo_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse":
        """<p>Deletes a specified prompt router. This action cannot be undone.</p>

        Args:
            prompt_router_arn: <p>The Amazon Resource Name (ARN) of the prompt router to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router.delete_prompt_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePromptRouter")
        )
        input_: capo_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest = {
            "prompt_router_arn": prompt_router_arn
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
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type: Optional["capo_bedrock.types.prompt_router_type.PromptRouterType"] = None,
    ) -> "capo_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse":
        """<p>Retrieves a list of prompt routers.</p>

        Args:
            max_results: <p>The maximum number of prompt routers to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            type: <p>The type of the prompt routers, such as whether it's default or custom.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers.list_prompt_routers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.list_prompt_routers_response

            return capo_bedrock.types.list_prompt_routers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPromptRouters", redact_output=_redact_output),
        )
        input_: capo_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPromptRouterResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create(
        self,
        prompt_router_name: "capo_bedrock.types.prompt_router_name.PromptRouterName",
        models: "capo_bedrock.types.prompt_router_target_models.PromptRouterTargetModels",
        routing_criteria: "capo_bedrock.types.routing_criteria.RoutingCriteria",
        fallback_model: "capo_bedrock.types.prompt_router_target_model.PromptRouterTargetModel",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "capo_bedrock.types.prompt_router_description.PromptRouterDescription"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse":
        """<p>Creates a prompt router that manages the routing of requests between multiple foundation models based on the routing criteria.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of your requests. If not specified, the Amazon Web Services SDK automatically generates one for you.</p>
            prompt_router_name: <p>The name of the prompt router. The name must be unique within your Amazon Web Services account in the current region.</p>
            models: <p>A list of foundation models that the prompt router can route requests to. At least one model must be specified.</p>
            description: <p>An optional description of the prompt router to help identify its purpose.</p>
            routing_criteria: <p>The criteria, which is the response quality difference, used to determine how incoming requests are routed to different models.</p>
            fallback_model: <p>The default model to use when the routing criteria is not met.</p>
            tags: <p>An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your Amazon Web Services resources.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router.async_create_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_prompt_router_request

            return capo_bedrock.types.create_prompt_router_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePromptRouter", redact_input=_redact_input),
        )
        input_: capo_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest = {
            "prompt_router_name": prompt_router_name,
            "models": models,
            "routing_criteria": routing_criteria,
            "fallback_model": fallback_model,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        prompt_router_arn: "capo_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_prompt_router_response.GetPromptRouterResponse":
        """<p>Retrieves details about a prompt router.</p>

        Args:
            prompt_router_arn: <p>The prompt router's ARN</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_prompt_router_request.GetPromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_prompt_router_response.GetPromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router.async_get_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_prompt_router_response.GetPromptRouterResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_prompt_router_response

            return capo_bedrock.types.get_prompt_router_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPromptRouter", redact_output=_redact_output),
        )
        input_: capo_bedrock.types.get_prompt_router_request.GetPromptRouterRequest = {
            "prompt_router_arn": prompt_router_arn
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
        prompt_router_arn: "capo_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse":
        """<p>Deletes a specified prompt router. This action cannot be undone.</p>

        Args:
            prompt_router_arn: <p>The Amazon Resource Name (ARN) of the prompt router to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router.async_delete_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePromptRouter")
        )
        input_: capo_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest = {
            "prompt_router_arn": prompt_router_arn
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
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type: Optional["capo_bedrock.types.prompt_router_type.PromptRouterType"] = None,
    ) -> "capo_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse":
        """<p>Retrieves a list of prompt routers.</p>

        Args:
            max_results: <p>The maximum number of prompt routers to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            type: <p>The type of the prompt routers, such as whether it's default or custom.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers.async_list_prompt_routers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.list_prompt_routers_response

            return capo_bedrock.types.list_prompt_routers_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPromptRouters", redact_output=_redact_output),
        )
        input_: capo_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
