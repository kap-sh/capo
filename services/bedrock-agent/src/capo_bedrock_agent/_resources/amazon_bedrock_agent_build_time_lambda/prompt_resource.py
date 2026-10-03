from __future__ import annotations

import uuid
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
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.create_prompt_request
    import capo_bedrock_agent.types.create_prompt_response
    import capo_bedrock_agent.types.create_prompt_version_request
    import capo_bedrock_agent.types.create_prompt_version_response
    import capo_bedrock_agent.types.delete_prompt_request
    import capo_bedrock_agent.types.delete_prompt_response
    import capo_bedrock_agent.types.get_prompt_request
    import capo_bedrock_agent.types.get_prompt_response
    import capo_bedrock_agent.types.included_data
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.list_prompts_request
    import capo_bedrock_agent.types.list_prompts_response
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.numerical_version
    import capo_bedrock_agent.types.prompt_description
    import capo_bedrock_agent.types.prompt_identifier
    import capo_bedrock_agent.types.prompt_name
    import capo_bedrock_agent.types.prompt_summary
    import capo_bedrock_agent.types.prompt_variant_list
    import capo_bedrock_agent.types.prompt_variant_name
    import capo_bedrock_agent.types.tags_map
    import capo_bedrock_agent.types.update_prompt_request
    import capo_bedrock_agent.types.update_prompt_response
    import capo_bedrock_agent.types.version
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class PromptResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock_agent.types.prompt_name.PromptName",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "capo_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "capo_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_prompt_response.CreatePromptResponse":
        """<p>Creates a prompt in your prompt library that you can add to a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management in Amazon Bedrock</a>, <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html">Create a prompt using Prompt management</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html">Prompt flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the prompt. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_prompt_request.CreatePromptRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_prompt_response.CreatePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt.create_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_prompt_request.CreatePromptRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_version: Optional["capo_bedrock_agent.types.version.Version"] = None,
        included_data: Optional[
            "capo_bedrock_agent.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_prompt_response.GetPromptResponse":
        """<p>Retrieves information about the working draft (<code>DRAFT</code> version) of a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html">View information about prompts using Prompt management</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-view.html">View information about a version of your prompt</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt about which you want to retrieve information. Omit this field to return information about the working draft of the prompt.</p>
            included_data: <p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_prompt_request.GetPromptRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_prompt_response.GetPromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt.get_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_prompt_request.GetPromptRequest = {
            "prompt_identifier": prompt_identifier
        }
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        name: "capo_bedrock_agent.types.prompt_name.PromptName",
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "capo_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "capo_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_prompt_response.UpdatePromptResponse":
        """<p>Modifies a prompt in your prompt library. Include both fields that you want to keep and fields that you want to replace. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management in Amazon Bedrock</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-edit">Edit prompts in your prompt library</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            prompt_identifier: <p>The unique identifier of the prompt.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.update_prompt_request.UpdatePromptRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_prompt_response.UpdatePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt.update_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_prompt_request.UpdatePromptRequest = {
            "name": name,
            "prompt_identifier": prompt_identifier,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_version: Optional[
            "capo_bedrock_agent.types.numerical_version.NumericalVersion"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_prompt_response.DeletePromptResponse":
        """<p>Deletes a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-delete.html">Delete prompts from the Prompt management tool</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-delete.html">Delete a version of a prompt from the Prompt management tool</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt to delete. To delete the prompt, omit this field.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.delete_prompt_request.DeletePromptRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_prompt_response.DeletePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt.delete_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_prompt_request.DeletePromptRequest = {
            "prompt_identifier": prompt_identifier
        }
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version

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
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        prompt_identifier: Optional[
            "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_prompts_response.ListPromptsResponse":
        """<p>Returns either information about the working draft (<code>DRAFT</code> version) of each prompt in an account, or information about of all versions of a prompt, depending on whether you include the <code>promptIdentifier</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html">View information about prompts using Prompt management</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt for whose versions you want to return information. Omit this field to list information about all prompts in an account.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_prompts_request.ListPromptsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_prompts_response.ListPromptsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts.list_prompts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_prompts_request.ListPromptsRequest = {}
        if prompt_identifier is not None:
            input_["prompt_identifier"] = prompt_identifier
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

    def create_prompt_version(
        self,
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse":
        """<p>Creates a static snapshot of your prompt that can be deployed to production. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html">Deploy prompts using Prompt management by creating versions</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt that you want to create a version of.</p>
            description: <p>A description for the version of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the version of the prompt. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version.create_prompt_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest = {
            "prompt_identifier": prompt_identifier
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPromptResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock_agent.types.prompt_name.PromptName",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "capo_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "capo_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_prompt_response.CreatePromptResponse":
        """<p>Creates a prompt in your prompt library that you can add to a flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management in Amazon Bedrock</a>, <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html">Create a prompt using Prompt management</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html">Prompt flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the prompt. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_prompt_request.CreatePromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_prompt_response.CreatePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt.async_create_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_prompt_request.CreatePromptRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        prompt_version: Optional["capo_bedrock_agent.types.version.Version"] = None,
        included_data: Optional[
            "capo_bedrock_agent.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_prompt_response.GetPromptResponse":
        """<p>Retrieves information about the working draft (<code>DRAFT</code> version) of a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html">View information about prompts using Prompt management</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-view.html">View information about a version of your prompt</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt about which you want to retrieve information. Omit this field to return information about the working draft of the prompt.</p>
            included_data: <p>Controls the scope of data returned. Set to <code>METADATA_ONLY</code> to return only resource metadata. Set to <code>ALL_DATA</code> or omit this field to return the full response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_prompt_request.GetPromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_prompt_response.GetPromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_prompt.async_get_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.get_prompt_request.GetPromptRequest = {
            "prompt_identifier": prompt_identifier
        }
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version
        if included_data is not None:
            input_["included_data"] = included_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        name: "capo_bedrock_agent.types.prompt_name.PromptName",
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        default_variant: Optional[
            "capo_bedrock_agent.types.prompt_variant_name.PromptVariantName"
        ] = None,
        variants: Optional[
            "capo_bedrock_agent.types.prompt_variant_list.PromptVariantList"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_prompt_response.UpdatePromptResponse":
        """<p>Modifies a prompt in your prompt library. Include both fields that you want to keep and fields that you want to replace. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html">Prompt management in Amazon Bedrock</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-edit">Edit prompts in your prompt library</a> in the Amazon Bedrock User Guide.</p>

        Args:
            name: <p>A name for the prompt.</p>
            description: <p>A description for the prompt.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>
            default_variant: <p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html">PromptVariant</a> object.</p>
            variants: <p>A list of objects, each containing details about a variant of the prompt.</p>
            prompt_identifier: <p>The unique identifier of the prompt.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_prompt_request.UpdatePromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_prompt_response.UpdatePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_prompt.async_update_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.update_prompt_request.UpdatePromptRequest = {
            "name": name,
            "prompt_identifier": prompt_identifier,
        }
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if default_variant is not None:
            input_["default_variant"] = default_variant
        if variants is not None:
            input_["variants"] = variants

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        prompt_version: Optional[
            "capo_bedrock_agent.types.numerical_version.NumericalVersion"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_prompt_response.DeletePromptResponse":
        """<p>Deletes a prompt or a version of it, depending on whether you include the <code>promptVersion</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-delete.html">Delete prompts from the Prompt management tool</a> and <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html#prompt-management-versions-delete.html">Delete a version of a prompt from the Prompt management tool</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt.</p>
            prompt_version: <p>The version of the prompt to delete. To delete the prompt, omit this field.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_prompt_request.DeletePromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_prompt_response.DeletePromptResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_prompt.async_delete_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.delete_prompt_request.DeletePromptRequest = {
            "prompt_identifier": prompt_identifier
        }
        if prompt_version is not None:
            input_["prompt_version"] = prompt_version

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
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        prompt_identifier: Optional[
            "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier"
        ] = None,
        max_results: Optional["capo_bedrock_agent.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_prompts_response.ListPromptsResponse":
        """<p>Returns either information about the working draft (<code>DRAFT</code> version) of each prompt in an account, or information about of all versions of a prompt, depending on whether you include the <code>promptIdentifier</code> field or not. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-manage.html#prompt-management-view.html">View information about prompts using Prompt management</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt for whose versions you want to return information. Omit this field to list information about all prompts in an account.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_prompts_request.ListPromptsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_prompts_response.ListPromptsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_prompts.async_list_prompts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.list_prompts_request.ListPromptsRequest = {}
        if prompt_identifier is not None:
            input_["prompt_identifier"] = prompt_identifier
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

    async def create_prompt_version(
        self,
        prompt_identifier: "capo_bedrock_agent.types.prompt_identifier.PromptIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.prompt_description.PromptDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse":
        """<p>Creates a static snapshot of your prompt that can be deployed to production. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html">Deploy prompts using Prompt management by creating versions</a> in the Amazon Bedrock User Guide.</p>

        Args:
            prompt_identifier: <p>The unique identifier of the prompt that you want to create a version of.</p>
            description: <p>A description for the version of the prompt.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>Any tags that you want to attach to the version of the prompt. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources in Amazon Bedrock</a>.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_prompt_version_response.CreatePromptVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_prompt_version.async_create_prompt_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent.types.create_prompt_version_request.CreatePromptVersionRequest = {
            "prompt_identifier": prompt_identifier
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
