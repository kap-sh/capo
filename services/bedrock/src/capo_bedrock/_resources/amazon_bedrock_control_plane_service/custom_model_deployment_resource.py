from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock._auth._signers
import capo_bedrock._auth._sigv4
from capo_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock.types.create_custom_model_deployment_request
    import capo_bedrock.types.create_custom_model_deployment_response
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_deployment_description
    import capo_bedrock.types.custom_model_deployment_identifier
    import capo_bedrock.types.custom_model_deployment_status
    import capo_bedrock.types.custom_model_deployment_summary
    import capo_bedrock.types.delete_custom_model_deployment_request
    import capo_bedrock.types.delete_custom_model_deployment_response
    import capo_bedrock.types.get_custom_model_deployment_request
    import capo_bedrock.types.get_custom_model_deployment_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.list_custom_model_deployments_request
    import capo_bedrock.types.list_custom_model_deployments_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_deployment_name
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.sort_models_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.timestamp
    import capo_bedrock.types.update_custom_model_deployment_request
    import capo_bedrock.types.update_custom_model_deployment_response
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class CustomModelDeploymentResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_custom_model_deployment(
        self,
        model_deployment_name: "capo_bedrock.types.model_deployment_name.ModelDeploymentName",
        model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.custom_model_deployment_description.CustomModelDeploymentDescription"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_custom_model_deployment_response.CreateCustomModelDeploymentResponse":
        """<p>Deploys a custom model for on-demand inference in Amazon Bedrock. After you deploy your custom model, you use the deployment's Amazon Resource Name (ARN) as the <code>modelId</code> parameter when you submit prompts and generate responses with model inference.</p> <p> For more information about setting up on-demand inference for custom models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Set up inference for a custom model</a>. </p> <p>The following actions are related to the <code>CreateCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            model_deployment_name: <p>The name for the custom model deployment. The name must be unique within your Amazon Web Services account and Region.</p>
            model_arn: <p>The Amazon Resource Name (ARN) of the custom model to deploy for on-demand inference. The custom model must be in the <code>Active</code> state.</p>
            description: <p>A description for the custom model deployment to help you identify its purpose.</p>
            tags: <p>Tags to assign to the custom model deployment. You can use tags to organize and track your Amazon Web Services resources for cost allocation and management purposes.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_custom_model_deployment_request.CreateCustomModelDeploymentRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_custom_model_deployment_response.CreateCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model_deployment

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model_deployment.create_custom_model_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_custom_model_deployment_request.CreateCustomModelDeploymentRequest = {
            "model_deployment_name": model_deployment_name,
            "model_arn": model_arn,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
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

    def delete_custom_model_deployment(
        self,
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_custom_model_deployment_response.DeleteCustomModelDeploymentResponse":
        """<p>Deletes a custom model deployment. This operation stops the deployment and removes it from your account. After deletion, the deployment ARN can no longer be used for inference requests.</p> <p>The following actions are related to the <code>DeleteCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> </ul>

        Args:
            custom_model_deployment_identifier: <p>The Amazon Resource Name (ARN) or name of the custom model deployment to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_custom_model_deployment_request.DeleteCustomModelDeploymentRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_custom_model_deployment_response.DeleteCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model_deployment

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model_deployment.delete_custom_model_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_custom_model_deployment_request.DeleteCustomModelDeploymentRequest = {
            "custom_model_deployment_identifier": custom_model_deployment_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_custom_model_deployment(
        self,
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_custom_model_deployment_response.GetCustomModelDeploymentResponse":
        """<p>Retrieves information about a custom model deployment, including its status, configuration, and metadata. Use this operation to monitor the deployment status and retrieve details needed for inference requests.</p> <p>The following actions are related to the <code>GetCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            custom_model_deployment_identifier: <p>The Amazon Resource Name (ARN) or name of the custom model deployment to retrieve information about.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_custom_model_deployment_request.GetCustomModelDeploymentRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_custom_model_deployment_response.GetCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model_deployment

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model_deployment.get_custom_model_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_custom_model_deployment_request.GetCustomModelDeploymentRequest = {
            "custom_model_deployment_identifier": custom_model_deployment_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_custom_model_deployments(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        created_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        created_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.model_deployment_name.ModelDeploymentName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
        status_equals: Optional[
            "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
        ] = None,
        model_arn_equals: Optional[
            "capo_bedrock.types.custom_model_arn.CustomModelArn"
        ] = None,
    ) -> "capo_bedrock.types.list_custom_model_deployments_response.ListCustomModelDeploymentsResponse":
        """<p>Lists custom model deployments in your account. You can filter the results by creation time, name, status, and associated model. Use this operation to manage and monitor your custom model deployments.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>The following actions are related to the <code>ListCustomModelDeployments</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            created_before: <p>Filters deployments created before the specified date and time.</p>
            created_after: <p>Filters deployments created after the specified date and time.</p>
            name_contains: <p>Filters deployments whose names contain the specified string. </p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. Use this token to retrieve additional results when the response is truncated.</p>
            sort_by: <p>The field to sort the results by. The only supported value is <code>CreationTime</code>.</p>
            sort_order: <p>The sort order for the results. Valid values are <code>Ascending</code> and <code>Descending</code>. Default is <code>Descending</code>.</p>
            status_equals: <p>Filters deployments by status. Valid values are <code>CREATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>
            model_arn_equals: <p>Filters deployments by the Amazon Resource Name (ARN) of the associated custom model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_custom_model_deployments_request.ListCustomModelDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_custom_model_deployments_response.ListCustomModelDeploymentsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_model_deployments

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_model_deployments.list_custom_model_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_custom_model_deployments_request.ListCustomModelDeploymentsRequest = {}
        if created_before is not None:
            input_["created_before"] = created_before
        if created_after is not None:
            input_["created_after"] = created_after
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if model_arn_equals is not None:
            input_["model_arn_equals"] = model_arn_equals

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_custom_model_deployment(
        self,
        model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn",
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.update_custom_model_deployment_response.UpdateCustomModelDeploymentResponse":
        """<p> Updates a custom model deployment with a new custom model. This allows you to deploy updated models without creating new deployment endpoints. </p>

        Args:
            model_arn: <p> ARN of the new custom model to deploy. This replaces the currently deployed model. </p>
            custom_model_deployment_identifier: <p> Identifier of the custom model deployment to update with the new custom model. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.update_custom_model_deployment_request.UpdateCustomModelDeploymentRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.update_custom_model_deployment_response.UpdateCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_custom_model_deployment

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.update_custom_model_deployment.update_custom_model_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.update_custom_model_deployment_request.UpdateCustomModelDeploymentRequest = {
            "model_arn": model_arn,
            "custom_model_deployment_identifier": custom_model_deployment_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCustomModelDeploymentResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_custom_model_deployment(
        self,
        model_deployment_name: "capo_bedrock.types.model_deployment_name.ModelDeploymentName",
        model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.custom_model_deployment_description.CustomModelDeploymentDescription"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_custom_model_deployment_response.CreateCustomModelDeploymentResponse":
        """<p>Deploys a custom model for on-demand inference in Amazon Bedrock. After you deploy your custom model, you use the deployment's Amazon Resource Name (ARN) as the <code>modelId</code> parameter when you submit prompts and generate responses with model inference.</p> <p> For more information about setting up on-demand inference for custom models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Set up inference for a custom model</a>. </p> <p>The following actions are related to the <code>CreateCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            model_deployment_name: <p>The name for the custom model deployment. The name must be unique within your Amazon Web Services account and Region.</p>
            model_arn: <p>The Amazon Resource Name (ARN) of the custom model to deploy for on-demand inference. The custom model must be in the <code>Active</code> state.</p>
            description: <p>A description for the custom model deployment to help you identify its purpose.</p>
            tags: <p>Tags to assign to the custom model deployment. You can use tags to organize and track your Amazon Web Services resources for cost allocation and management purposes.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_custom_model_deployment_request.CreateCustomModelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_custom_model_deployment_response.CreateCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model_deployment

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model_deployment.async_create_custom_model_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_custom_model_deployment_request.CreateCustomModelDeploymentRequest = {
            "model_deployment_name": model_deployment_name,
            "model_arn": model_arn,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
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

    async def delete_custom_model_deployment(
        self,
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_custom_model_deployment_response.DeleteCustomModelDeploymentResponse":
        """<p>Deletes a custom model deployment. This operation stops the deployment and removes it from your account. After deletion, the deployment ARN can no longer be used for inference requests.</p> <p>The following actions are related to the <code>DeleteCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> </ul>

        Args:
            custom_model_deployment_identifier: <p>The Amazon Resource Name (ARN) or name of the custom model deployment to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_custom_model_deployment_request.DeleteCustomModelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_custom_model_deployment_response.DeleteCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model_deployment

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model_deployment.async_delete_custom_model_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_custom_model_deployment_request.DeleteCustomModelDeploymentRequest = {
            "custom_model_deployment_identifier": custom_model_deployment_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_custom_model_deployment(
        self,
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_custom_model_deployment_response.GetCustomModelDeploymentResponse":
        """<p>Retrieves information about a custom model deployment, including its status, configuration, and metadata. Use this operation to monitor the deployment status and retrieve details needed for inference requests.</p> <p>The following actions are related to the <code>GetCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            custom_model_deployment_identifier: <p>The Amazon Resource Name (ARN) or name of the custom model deployment to retrieve information about.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_custom_model_deployment_request.GetCustomModelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_custom_model_deployment_response.GetCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model_deployment

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model_deployment.async_get_custom_model_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_custom_model_deployment_request.GetCustomModelDeploymentRequest = {
            "custom_model_deployment_identifier": custom_model_deployment_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_model_deployments(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        created_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        created_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.model_deployment_name.ModelDeploymentName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
        status_equals: Optional[
            "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
        ] = None,
        model_arn_equals: Optional[
            "capo_bedrock.types.custom_model_arn.CustomModelArn"
        ] = None,
    ) -> "capo_bedrock.types.list_custom_model_deployments_response.ListCustomModelDeploymentsResponse":
        """<p>Lists custom model deployments in your account. You can filter the results by creation time, name, status, and associated model. Use this operation to manage and monitor your custom model deployments.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>The following actions are related to the <code>ListCustomModelDeployments</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            created_before: <p>Filters deployments created before the specified date and time.</p>
            created_after: <p>Filters deployments created after the specified date and time.</p>
            name_contains: <p>Filters deployments whose names contain the specified string. </p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. Use this token to retrieve additional results when the response is truncated.</p>
            sort_by: <p>The field to sort the results by. The only supported value is <code>CreationTime</code>.</p>
            sort_order: <p>The sort order for the results. Valid values are <code>Ascending</code> and <code>Descending</code>. Default is <code>Descending</code>.</p>
            status_equals: <p>Filters deployments by status. Valid values are <code>CREATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>
            model_arn_equals: <p>Filters deployments by the Amazon Resource Name (ARN) of the associated custom model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_custom_model_deployments_request.ListCustomModelDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_custom_model_deployments_response.ListCustomModelDeploymentsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_model_deployments

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_model_deployments.async_list_custom_model_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_custom_model_deployments_request.ListCustomModelDeploymentsRequest = {}
        if created_before is not None:
            input_["created_before"] = created_before
        if created_after is not None:
            input_["created_after"] = created_after
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if model_arn_equals is not None:
            input_["model_arn_equals"] = model_arn_equals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_custom_model_deployment(
        self,
        model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn",
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.update_custom_model_deployment_response.UpdateCustomModelDeploymentResponse":
        """<p> Updates a custom model deployment with a new custom model. This allows you to deploy updated models without creating new deployment endpoints. </p>

        Args:
            model_arn: <p> ARN of the new custom model to deploy. This replaces the currently deployed model. </p>
            custom_model_deployment_identifier: <p> Identifier of the custom model deployment to update with the new custom model. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_custom_model_deployment_request.UpdateCustomModelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_custom_model_deployment_response.UpdateCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_custom_model_deployment

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_custom_model_deployment.async_update_custom_model_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.update_custom_model_deployment_request.UpdateCustomModelDeploymentRequest = {
            "model_arn": model_arn,
            "custom_model_deployment_identifier": custom_model_deployment_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
