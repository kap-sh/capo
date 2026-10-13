from __future__ import annotations

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
    import capo_bedrock.types.delete_resource_policy_request
    import capo_bedrock.types.delete_resource_policy_response
    import capo_bedrock.types.get_resource_policy_request
    import capo_bedrock.types.get_resource_policy_response
    import capo_bedrock.types.put_resource_policy_request
    import capo_bedrock.types.put_resource_policy_response
    import capo_bedrock.types.resource_policy_document
    import capo_bedrock.types.resource_policy_resource_arn
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class ResourcePolicyResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def delete_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a previously created Bedrock resource policy.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteResourcePolicy")
        )
        input_: capo_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Gets the resource policy document for a Bedrock resource</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetResourcePolicy")
        )
        input_: capo_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        resource_policy: "capo_bedrock.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Adds a resource policy for a Bedrock resource.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
            resource_policy: <p>The JSON string representing the Bedrock resource policy.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutResourcePolicy")
        )
        input_: capo_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "resource_policy": resource_policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncResourcePolicyResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def delete_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a previously created Bedrock resource policy.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteResourcePolicy")
        )
        input_: capo_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Gets the resource policy document for a Bedrock resource</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetResourcePolicy")
        )
        input_: capo_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        resource_policy: "capo_bedrock.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Adds a resource policy for a Bedrock resource.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
            resource_policy: <p>The JSON string representing the Bedrock resource policy.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutResourcePolicy")
        )
        input_: capo_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "resource_policy": resource_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
