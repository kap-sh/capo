from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_omics.types.list_tags_for_resource_request
    import capo_omics.types.list_tags_for_resource_response
    import capo_omics.types.tag_arn
    import capo_omics.types.tag_key_list
    import capo_omics.types.tag_map
    import capo_omics.types.tag_resource_request
    import capo_omics.types.tag_resource_response
    import capo_omics.types.untag_resource_request
    import capo_omics.types.untag_resource_response
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class TaggingResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def list(
        self,
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_omics._operations.omics.list_tags_for_resource

            output, http_response = (
                capo_omics._operations.omics.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTagsForResource")
        )
        input_: capo_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        tags: "capo_omics.types.tag_map.TagMap",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tags: <p>Tags for the resource.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_omics.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_omics._operations.omics.tag_resource

            output, http_response = (
                capo_omics._operations.omics.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_omics.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        tag_keys: "capo_omics.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tag_keys: <p>Keys of tags to remove.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_omics.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_omics._operations.omics.untag_resource

            output, http_response = (
                capo_omics._operations.omics.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_omics.types.untag_resource_request.UntagResourceRequest = {
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
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def list(
        self,
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_omics._operations.omics.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTagsForResource")
        )
        input_: capo_omics.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        tags: "capo_omics.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tags: <p>Tags for the resource.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_omics._operations.omics.tag_resource

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_omics.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_omics.types.tag_arn.TagArn",
        tag_keys: "capo_omics.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            resource_arn: <p>The resource's ARN.</p>
            tag_keys: <p>Keys of tags to remove.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_omics._operations.omics.untag_resource

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_omics.types.untag_resource_request.UntagResourceRequest = {
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
