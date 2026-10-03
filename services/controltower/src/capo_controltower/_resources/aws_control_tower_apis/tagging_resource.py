from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_controltower._auth._signers
import capo_controltower._auth._sigv4
from capo_controltower._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.list_tags_for_resource_input
    import capo_controltower.types.list_tags_for_resource_output
    import capo_controltower.types.tag_keys
    import capo_controltower.types.tag_map
    import capo_controltower.types.tag_resource_input
    import capo_controltower.types.tag_resource_output
    import capo_controltower.types.untag_resource_input
    import capo_controltower.types.untag_resource_output
    from capo_controltower._services.async_control_tower import (
        AsyncControlTowerClient,
        AsyncControlTowerClientConfig,
    )
    from capo_controltower._services.control_tower import (
        ControlTowerClient,
        ControlTowerClientConfig,
    )


class TaggingResource:
    def __init__(self, service: ControlTowerClient) -> None:
        self._service = service

    def list(
        self,
        resource_arn: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns a list of tags associated with the resource. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p> The ARN of the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_tags_for_resource

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_controltower.types.arn.Arn",
        tags: "capo_controltower.types.tag_map.TagMap",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.tag_resource_output.TagResourceOutput":
        """<p>Applies tags to a resource. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged.</p>
            tags: <p>Tags to be applied to the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_controltower.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.tag_resource

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_controltower.types.arn.Arn",
        tag_keys: "capo_controltower.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[ControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from a resource. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>Tag keys to be removed from the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controltower.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_controltower.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.untag_resource

            output, http_response = (
                capo_controltower._operations.aws_control_tower_apis.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.untag_resource_input.UntagResourceInput = {
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
    def __init__(self, service: AsyncControlTowerClient) -> None:
        self._service = service

    async def list(
        self,
        resource_arn: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Returns a list of tags associated with the resource. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p> The ARN of the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_controltower.types.arn.Arn",
        tags: "capo_controltower.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.tag_resource_output.TagResourceOutput":
        """<p>Applies tags to a resource. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged.</p>
            tags: <p>Tags to be applied to the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.tag_resource

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_controltower.types.arn.Arn",
        tag_keys: "capo_controltower.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from a resource. For usage examples, see the <a href="https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>Tag keys to be removed from the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.untag_resource

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_controltower.types.untag_resource_input.UntagResourceInput = {
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
