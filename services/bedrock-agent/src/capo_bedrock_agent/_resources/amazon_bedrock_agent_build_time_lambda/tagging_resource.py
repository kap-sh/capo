from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock_agent._auth._signers
import capo_bedrock_agent._auth._sigv4
from capo_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent.types.list_tags_for_resource_request
    import capo_bedrock_agent.types.list_tags_for_resource_response
    import capo_bedrock_agent.types.tag_key_list
    import capo_bedrock_agent.types.tag_resource_request
    import capo_bedrock_agent.types.tag_resource_response
    import capo_bedrock_agent.types.taggable_resources_arn
    import capo_bedrock_agent.types.tags_map
    import capo_bedrock_agent.types.untag_resource_request
    import capo_bedrock_agent.types.untag_resource_response
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class TaggingResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all the tags for the resource you specify.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_tags_for_resource

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "capo_bedrock_agent.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.tag_resource_response.TagResourceResponse":
        """<p>Associate tags with a resource. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the Amazon Bedrock User Guide.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>An object containing key-value pairs that define the tags to attach to the resource.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.tag_resource

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "capo_bedrock_agent.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of keys of the tags to remove from the resource.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.untag_resource

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTaggingResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all the tags for the resource you specify.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "capo_bedrock_agent.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.tag_resource_response.TagResourceResponse":
        """<p>Associate tags with a resource. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the Amazon Bedrock User Guide.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>An object containing key-value pairs that define the tags to attach to the resource.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.tag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_bedrock_agent.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "capo_bedrock_agent.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "capo_bedrock_agent.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of keys of the tags to remove from the resource.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.untag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
