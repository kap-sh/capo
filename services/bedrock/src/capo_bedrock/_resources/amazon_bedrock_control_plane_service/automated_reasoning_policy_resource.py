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
    import capo_bedrock.types.automated_reasoning_check_result
    import capo_bedrock.types.automated_reasoning_check_translation_confidence
    import capo_bedrock.types.automated_reasoning_policy_annotation_list
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_id
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_type
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_source
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_summary
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_type
    import capo_bedrock.types.automated_reasoning_policy_definition
    import capo_bedrock.types.automated_reasoning_policy_description
    import capo_bedrock.types.automated_reasoning_policy_hash
    import capo_bedrock.types.automated_reasoning_policy_name
    import capo_bedrock.types.automated_reasoning_policy_summary
    import capo_bedrock.types.automated_reasoning_policy_test_case
    import capo_bedrock.types.automated_reasoning_policy_test_case_id
    import capo_bedrock.types.automated_reasoning_policy_test_case_id_list
    import capo_bedrock.types.automated_reasoning_policy_test_guard_content
    import capo_bedrock.types.automated_reasoning_policy_test_query_content
    import capo_bedrock.types.automated_reasoning_policy_test_result
    import capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_request
    import capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_response
    import capo_bedrock.types.create_automated_reasoning_policy_request
    import capo_bedrock.types.create_automated_reasoning_policy_response
    import capo_bedrock.types.create_automated_reasoning_policy_test_case_request
    import capo_bedrock.types.create_automated_reasoning_policy_test_case_response
    import capo_bedrock.types.create_automated_reasoning_policy_version_request
    import capo_bedrock.types.create_automated_reasoning_policy_version_response
    import capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_request
    import capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_response
    import capo_bedrock.types.delete_automated_reasoning_policy_request
    import capo_bedrock.types.delete_automated_reasoning_policy_response
    import capo_bedrock.types.delete_automated_reasoning_policy_test_case_request
    import capo_bedrock.types.delete_automated_reasoning_policy_test_case_response
    import capo_bedrock.types.export_automated_reasoning_policy_version_request
    import capo_bedrock.types.export_automated_reasoning_policy_version_response
    import capo_bedrock.types.get_automated_reasoning_policy_annotations_request
    import capo_bedrock.types.get_automated_reasoning_policy_annotations_response
    import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_request
    import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response
    import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_request
    import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response
    import capo_bedrock.types.get_automated_reasoning_policy_next_scenario_request
    import capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response
    import capo_bedrock.types.get_automated_reasoning_policy_request
    import capo_bedrock.types.get_automated_reasoning_policy_response
    import capo_bedrock.types.get_automated_reasoning_policy_test_case_request
    import capo_bedrock.types.get_automated_reasoning_policy_test_case_response
    import capo_bedrock.types.get_automated_reasoning_policy_test_result_request
    import capo_bedrock.types.get_automated_reasoning_policy_test_result_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.list_automated_reasoning_policies_request
    import capo_bedrock.types.list_automated_reasoning_policies_response
    import capo_bedrock.types.list_automated_reasoning_policy_build_workflows_request
    import capo_bedrock.types.list_automated_reasoning_policy_build_workflows_response
    import capo_bedrock.types.list_automated_reasoning_policy_test_cases_request
    import capo_bedrock.types.list_automated_reasoning_policy_test_cases_response
    import capo_bedrock.types.list_automated_reasoning_policy_test_results_request
    import capo_bedrock.types.list_automated_reasoning_policy_test_results_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request
    import capo_bedrock.types.start_automated_reasoning_policy_build_workflow_response
    import capo_bedrock.types.start_automated_reasoning_policy_test_workflow_request
    import capo_bedrock.types.start_automated_reasoning_policy_test_workflow_response
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.timestamp
    import capo_bedrock.types.update_automated_reasoning_policy_annotations_request
    import capo_bedrock.types.update_automated_reasoning_policy_annotations_response
    import capo_bedrock.types.update_automated_reasoning_policy_request
    import capo_bedrock.types.update_automated_reasoning_policy_response
    import capo_bedrock.types.update_automated_reasoning_policy_test_case_request
    import capo_bedrock.types.update_automated_reasoning_policy_test_case_response
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class AutomatedReasoningPolicyResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        policy_definition: Optional[
            "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_response.CreateAutomatedReasoningPolicyResponse":
        """<p>Creates an Automated Reasoning policy for Amazon Bedrock Guardrails. Automated Reasoning policies use mathematical techniques to detect hallucinations, suggest corrections, and highlight unstated assumptions in the responses of your GenAI application.</p> <p>To create a policy, you upload a source document that describes the rules that you're encoding. Automated Reasoning extracts important concepts from the source document that will become variables in the policy and infers policy rules.</p>

        Args:
            name: <p>A unique name for the Automated Reasoning policy. The name must be between 1 and 63 characters and can contain letters, numbers, hyphens, and underscores.</p>
            description: <p>A description of the Automated Reasoning policy. Use this to provide context about the policy's purpose and the types of validations it performs.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>
            policy_definition: <p>The policy definition that contains the formal logic rules, variables, and custom variable types used to validate foundation model responses in your application.</p>
            kms_key_id: <p>The identifier of the KMS key to use for encrypting the automated reasoning policy and its associated artifacts. If you don't specify a KMS key, Amazon Bedrock uses an KMS managed key for encryption. For enhanced security and control, you can specify a customer managed KMS key.</p>
            tags: <p>A list of tags to associate with the Automated Reasoning policy. Tags help you organize and manage your policies.</p>

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
            req: "OperationRequest[capo_bedrock.types.create_automated_reasoning_policy_request.CreateAutomatedReasoningPolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_response.CreateAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy.create_automated_reasoning_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.create_automated_reasoning_policy_request.CreateAutomatedReasoningPolicyRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_automated_reasoning_policy_request

            return capo_bedrock.types.create_automated_reasoning_policy_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock.types.create_automated_reasoning_policy_response.CreateAutomatedReasoningPolicyResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_automated_reasoning_policy_response

            return capo_bedrock.types.create_automated_reasoning_policy_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAutomatedReasoningPolicy",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock.types.create_automated_reasoning_policy_request.CreateAutomatedReasoningPolicyRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if policy_definition is not None:
            input_["policy_definition"] = policy_definition
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
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
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_response.GetAutomatedReasoningPolicyResponse":
        """<p>Retrieves details about an Automated Reasoning policy or policy version. Returns information including the policy definition, metadata, and timestamps.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to retrieve. Can be either the unversioned ARN for the draft policy or an ARN for a specific policy version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_automated_reasoning_policy_request.GetAutomatedReasoningPolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_response.GetAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy.get_automated_reasoning_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_response.GetAutomatedReasoningPolicyResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_response

            return capo_bedrock.types.get_automated_reasoning_policy_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicy", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_request.GetAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn
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
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        policy_definition: "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        name: Optional[
            "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
        ] = None,
        description: Optional[
            "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
        ] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_response.UpdateAutomatedReasoningPolicyResponse":
        """<p>Updates an existing Automated Reasoning policy with new rules, variables, or configuration. This creates a new version of the policy while preserving the previous version.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to update. This must be the ARN of a draft policy.</p>
            policy_definition: <p>The updated policy definition containing the formal logic rules, variables, and types.</p>
            name: <p>The updated name for the Automated Reasoning policy.</p>
            description: <p>The updated description for the Automated Reasoning policy.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.update_automated_reasoning_policy_request.UpdateAutomatedReasoningPolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_response.UpdateAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy.update_automated_reasoning_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.update_automated_reasoning_policy_request.UpdateAutomatedReasoningPolicyRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.update_automated_reasoning_policy_request

            return capo_bedrock.types.update_automated_reasoning_policy_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock.types.update_automated_reasoning_policy_response.UpdateAutomatedReasoningPolicyResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.update_automated_reasoning_policy_response

            return capo_bedrock.types.update_automated_reasoning_policy_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAutomatedReasoningPolicy",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock.types.update_automated_reasoning_policy_request.UpdateAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn,
            "policy_definition": policy_definition,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_response.DeleteAutomatedReasoningPolicyResponse":
        """<p>Deletes an Automated Reasoning policy or policy version. This operation is idempotent. If you delete a policy more than once, each call succeeds. Deleting a policy removes it permanently and cannot be undone.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to delete.</p>
            force: <p>Specifies whether to force delete the automated reasoning policy even if it has active resources. When <code>false</code>, Amazon Bedrock validates if all artifacts have been deleted (e.g. policy version, test case, test result) for a policy before deletion. When <code>true</code>, Amazon Bedrock will delete the policy and all its artifacts without validation. Default is <code>false</code>. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_request.DeleteAutomatedReasoningPolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_response.DeleteAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy.delete_automated_reasoning_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAutomatedReasoningPolicy")
        )
        input_: capo_bedrock.types.delete_automated_reasoning_policy_request.DeleteAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn
        }
        if force is not None:
            input_["force"] = force

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
        policy_arn: Optional[
            "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
        ] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policies_response.ListAutomatedReasoningPoliciesResponse":
        """<p>Lists all Automated Reasoning policies in your account, with optional filtering by policy ARN. This helps you manage and discover existing policies.</p>

        Args:
            policy_arn: <p>Optional filter to list only the policy versions with the specified Amazon Resource Name (ARN). If not provided, the DRAFT versions for all policies are listed.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of policies to return in a single call.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_automated_reasoning_policies_request.ListAutomatedReasoningPoliciesRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policies_response.ListAutomatedReasoningPoliciesResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policies

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policies.list_automated_reasoning_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.list_automated_reasoning_policies_response.ListAutomatedReasoningPoliciesResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.list_automated_reasoning_policies_response

            return capo_bedrock.types.list_automated_reasoning_policies_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListAutomatedReasoningPolicies", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.list_automated_reasoning_policies_request.ListAutomatedReasoningPoliciesRequest = {}
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
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

    def cancel_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_response.CancelAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Cancels a running Automated Reasoning policy build workflow. This stops the policy generation process and prevents further processing of the source documents.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to cancel.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to cancel. You can get this ID from the StartAutomatedReasoningPolicyBuildWorkflow response or by listing build workflows.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_request.CancelAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_response.CancelAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.cancel_automated_reasoning_policy_build_workflow

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.cancel_automated_reasoning_policy_build_workflow.cancel_automated_reasoning_policy_build_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CancelAutomatedReasoningPolicyBuildWorkflow"),
        )
        input_: capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_request.CancelAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent",
        expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        query_content: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        confidence_threshold: Optional[
            "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
        ] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_test_case_response.CreateAutomatedReasoningPolicyTestCaseResponse":
        """<p>Creates a test for an Automated Reasoning policy. Tests validate that your policy works as expected by providing sample inputs and expected outcomes. Use tests to verify policy behavior before deploying to production.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create the test.</p>
            guard_content: <p>The output content that's validated by the Automated Reasoning policy. This represents the foundation model response that will be checked for accuracy.</p>
            query_content: <p>The input query or prompt that generated the content. This provides context for the validation.</p>
            expected_aggregated_findings_result: <p>The expected result of the Automated Reasoning check. Valid values include: , TOO_COMPLEX, and NO_TRANSLATIONS.</p> <ul> <li> <p> <code>VALID</code> - The claims are true. The claims are implied by the premises and the Automated Reasoning policy. Given the Automated Reasoning policy and premises, it is not possible for these claims to be false. In other words, there are no alternative answers that are true that contradict the claims.</p> </li> <li> <p> <code>INVALID</code> - The claims are false. The claims are not implied by the premises and Automated Reasoning policy. Furthermore, there exists different claims that are consistent with the premises and Automated Reasoning policy.</p> </li> <li> <p> <code>SATISFIABLE</code> - The claims can be true or false. It depends on what assumptions are made for the claim to be implied from the premises and Automated Reasoning policy rules. In this situation, different assumptions can make input claims false and alternative claims true.</p> </li> <li> <p> <code>IMPOSSIBLE</code> - Automated Reasoning can’t make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.</p> </li> <li> <p> <code>TRANSLATION_AMBIGUOUS</code> - Detected an ambiguity in the translation meant it would be unsound to continue with validity checking. Additional context or follow-up questions might be needed to get translation to succeed.</p> </li> <li> <p> <code>TOO_COMPLEX</code> - The input contains too much information for Automated Reasoning to process within its latency limits.</p> </li> <li> <p> <code>NO_TRANSLATIONS</code> - Identifies that some or all of the input prompt wasn't translated into logic. This can happen if the input isn't relevant to the Automated Reasoning policy, or if the policy doesn't have variables to model relevant input. If Automated Reasoning can't translate anything, you get a single <code>NO_TRANSLATIONS</code> finding. You might also see a <code>NO_TRANSLATIONS</code> (along with other findings) if some part of the validation isn't translated.</p> </li> </ul>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>
            confidence_threshold: <p>The minimum confidence level for logic validation. Content that meets the threshold is considered a high-confidence finding that can be validated.</p>

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
            req: "OperationRequest[capo_bedrock.types.create_automated_reasoning_policy_test_case_request.CreateAutomatedReasoningPolicyTestCaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_test_case_response.CreateAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_test_case

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_test_case.create_automated_reasoning_policy_test_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.create_automated_reasoning_policy_test_case_request.CreateAutomatedReasoningPolicyTestCaseRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_automated_reasoning_policy_test_case_request

            return capo_bedrock.types.create_automated_reasoning_policy_test_case_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAutomatedReasoningPolicyTestCase", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock.types.create_automated_reasoning_policy_test_case_request.CreateAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "guard_content": guard_content,
            "expected_aggregated_findings_result": expected_aggregated_findings_result,
        }
        if query_content is not None:
            input_["query_content"] = query_content
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_automated_reasoning_policy_version(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        last_updated_definition_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_version_response.CreateAutomatedReasoningPolicyVersionResponse":
        """<p>Creates a new version of an existing Automated Reasoning policy. This allows you to iterate on your policy rules while maintaining previous versions for rollback or comparison purposes.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create a version.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>
            last_updated_definition_hash: <p>The hash of the current policy definition used as a concurrency token to ensure the policy hasn't been modified since you last retrieved it.</p>
            tags: <p>A list of tags to associate with the policy version.</p>

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
            req: "OperationRequest[capo_bedrock.types.create_automated_reasoning_policy_version_request.CreateAutomatedReasoningPolicyVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_version_response.CreateAutomatedReasoningPolicyVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_version

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_version.create_automated_reasoning_policy_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.create_automated_reasoning_policy_version_response.CreateAutomatedReasoningPolicyVersionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_automated_reasoning_policy_version_response

            return capo_bedrock.types.create_automated_reasoning_policy_version_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAutomatedReasoningPolicyVersion", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.create_automated_reasoning_policy_version_request.CreateAutomatedReasoningPolicyVersionRequest = {
            "policy_arn": policy_arn,
            "last_updated_definition_hash": last_updated_definition_hash,
        }
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

    def delete_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_response.DeleteAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Deletes an Automated Reasoning policy build workflow and its associated artifacts. This permanently removes the workflow history and any generated assets.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to delete.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to delete.</p>
            last_updated_at: <p>The timestamp when the build workflow was last updated. This is used for optimistic concurrency control to prevent accidental deletion of workflows that have been modified.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_request.DeleteAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_response.DeleteAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_build_workflow

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_build_workflow.delete_automated_reasoning_policy_build_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteAutomatedReasoningPolicyBuildWorkflow"),
        )
        input_: capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_request.DeleteAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "last_updated_at": last_updated_at,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_test_case_response.DeleteAutomatedReasoningPolicyTestCaseResponse":
        """<p>Deletes an Automated Reasoning policy test. This operation is idempotent; if you delete a test more than once, each call succeeds.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to delete.</p>
            last_updated_at: <p>The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_test_case_request.DeleteAutomatedReasoningPolicyTestCaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_test_case_response.DeleteAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_test_case

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_test_case.delete_automated_reasoning_policy_test_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAutomatedReasoningPolicyTestCase")
        )
        input_: capo_bedrock.types.delete_automated_reasoning_policy_test_case_request.DeleteAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
            "last_updated_at": last_updated_at,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_automated_reasoning_policy_version(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.export_automated_reasoning_policy_version_response.ExportAutomatedReasoningPolicyVersionResponse":
        """<p>Exports the policy definition for an Automated Reasoning policy version. Returns the complete policy definition including rules, variables, and custom variable types in a structured format.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to export. Can be either the unversioned ARN for the draft policy or a versioned ARN for a specific policy version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.export_automated_reasoning_policy_version_request.ExportAutomatedReasoningPolicyVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.export_automated_reasoning_policy_version_response.ExportAutomatedReasoningPolicyVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.export_automated_reasoning_policy_version

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.export_automated_reasoning_policy_version.export_automated_reasoning_policy_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.export_automated_reasoning_policy_version_response.ExportAutomatedReasoningPolicyVersionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.export_automated_reasoning_policy_version_response

            return capo_bedrock.types.export_automated_reasoning_policy_version_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ExportAutomatedReasoningPolicyVersion", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.export_automated_reasoning_policy_version_request.ExportAutomatedReasoningPolicyVersionRequest = {
            "policy_arn": policy_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_automated_reasoning_policy_annotations(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_annotations_response.GetAutomatedReasoningPolicyAnnotationsResponse":
        """<p>Retrieves the current annotations for an Automated Reasoning policy build workflow. Annotations contain corrections to the rules, variables and types to be applied to the policy.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose annotations you want to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_automated_reasoning_policy_annotations_request.GetAutomatedReasoningPolicyAnnotationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_annotations_response.GetAutomatedReasoningPolicyAnnotationsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_annotations

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_annotations.get_automated_reasoning_policy_annotations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_annotations_response.GetAutomatedReasoningPolicyAnnotationsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_annotations_response

            return capo_bedrock.types.get_automated_reasoning_policy_annotations_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyAnnotations", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_annotations_request.GetAutomatedReasoningPolicyAnnotationsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.GetAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Retrieves detailed information about an Automated Reasoning policy build workflow, including its status, configuration, and metadata.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_automated_reasoning_policy_build_workflow_request.GetAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.GetAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow.get_automated_reasoning_policy_build_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.GetAutomatedReasoningPolicyBuildWorkflowResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response

            return capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyBuildWorkflow", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_build_workflow_request.GetAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_automated_reasoning_policy_build_workflow_result_assets(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        asset_type: "capo_bedrock.types.automated_reasoning_policy_build_result_asset_type.AutomatedReasoningPolicyBuildResultAssetType",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        asset_id: Optional[
            "capo_bedrock.types.automated_reasoning_policy_build_result_asset_id.AutomatedReasoningPolicyBuildResultAssetId"
        ] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse":
        """<p>Retrieves the resulting assets from a completed Automated Reasoning policy build workflow, including build logs, quality reports, and generated policy artifacts.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow assets you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose result assets you want to retrieve.</p>
            asset_type: <p>The type of asset to retrieve (e.g., BUILD_LOG, QUALITY_REPORT, POLICY_DEFINITION, GENERATED_TEST_CASES, POLICY_SCENARIOS, FIDELITY_REPORT, ASSET_MANIFEST, SOURCE_DOCUMENT).</p>
            asset_id: <p>The unique identifier of the specific asset to retrieve when multiple assets of the same type exist. This is required when retrieving SOURCE_DOCUMENT assets, as multiple source documents may have been used in the workflow. The asset ID can be obtained from the asset manifest.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_request.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow_result_assets

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow_result_assets.get_automated_reasoning_policy_build_workflow_result_assets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response

            return capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyBuildWorkflowResultAssets",
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_request.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "asset_type": asset_type,
        }
        if asset_id is not None:
            input_["asset_id"] = asset_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_automated_reasoning_policy_next_scenario(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.GetAutomatedReasoningPolicyNextScenarioResponse":
        """<p>Retrieves the next test scenario for validating an Automated Reasoning policy. This is used during the interactive policy refinement process to test policy behavior.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which you want to get the next test scenario.</p>
            build_workflow_id: <p>The unique identifier of the build workflow associated with the test scenarios.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_automated_reasoning_policy_next_scenario_request.GetAutomatedReasoningPolicyNextScenarioRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.GetAutomatedReasoningPolicyNextScenarioResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_next_scenario

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_next_scenario.get_automated_reasoning_policy_next_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.GetAutomatedReasoningPolicyNextScenarioResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response

            return capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyNextScenario", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_next_scenario_request.GetAutomatedReasoningPolicyNextScenarioRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_test_case_response.GetAutomatedReasoningPolicyTestCaseResponse":
        """<p>Retrieves details about a specific Automated Reasoning policy test.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_automated_reasoning_policy_test_case_request.GetAutomatedReasoningPolicyTestCaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_test_case_response.GetAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_case

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_case.get_automated_reasoning_policy_test_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_test_case_response.GetAutomatedReasoningPolicyTestCaseResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_test_case_response

            return capo_bedrock.types.get_automated_reasoning_policy_test_case_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyTestCase", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_test_case_request.GetAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_automated_reasoning_policy_test_result(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_test_result_response.GetAutomatedReasoningPolicyTestResultResponse":
        """<p>Retrieves the test result for a specific Automated Reasoning policy test. Returns detailed validation findings and execution status.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>
            build_workflow_id: <p>The build workflow identifier. The build workflow must display a <code>COMPLETED</code> status to get results.</p>
            test_case_id: <p>The unique identifier of the test for which to retrieve results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_automated_reasoning_policy_test_result_request.GetAutomatedReasoningPolicyTestResultRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_test_result_response.GetAutomatedReasoningPolicyTestResultResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_result

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_result.get_automated_reasoning_policy_test_result(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_test_result_response.GetAutomatedReasoningPolicyTestResultResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_test_result_response

            return capo_bedrock.types.get_automated_reasoning_policy_test_result_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyTestResult", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_test_result_request.GetAutomatedReasoningPolicyTestResultRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "test_case_id": test_case_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_automated_reasoning_policy_build_workflows(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_build_workflows_response.ListAutomatedReasoningPolicyBuildWorkflowsResponse":
        """<p>Lists all build workflows for an Automated Reasoning policy, showing the history of policy creation and modification attempts.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflows you want to list.</p>
            next_token: <p>A pagination token from a previous request to continue listing build workflows from where the previous request left off.</p>
            max_results: <p>The maximum number of build workflows to return in a single response. Valid range is 1-100.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_automated_reasoning_policy_build_workflows_request.ListAutomatedReasoningPolicyBuildWorkflowsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_build_workflows_response.ListAutomatedReasoningPolicyBuildWorkflowsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_build_workflows

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_build_workflows.list_automated_reasoning_policy_build_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAutomatedReasoningPolicyBuildWorkflows"),
        )
        input_: capo_bedrock.types.list_automated_reasoning_policy_build_workflows_request.ListAutomatedReasoningPolicyBuildWorkflowsRequest = {
            "policy_arn": policy_arn
        }
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

    def list_automated_reasoning_policy_test_cases(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.ListAutomatedReasoningPolicyTestCasesResponse":
        """<p>Lists tests for an Automated Reasoning policy. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to list tests.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of tests to return in a single call.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_automated_reasoning_policy_test_cases_request.ListAutomatedReasoningPolicyTestCasesRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.ListAutomatedReasoningPolicyTestCasesResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_cases

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_cases.list_automated_reasoning_policy_test_cases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.ListAutomatedReasoningPolicyTestCasesResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.list_automated_reasoning_policy_test_cases_response

            return capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListAutomatedReasoningPolicyTestCases", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.list_automated_reasoning_policy_test_cases_request.ListAutomatedReasoningPolicyTestCasesRequest = {
            "policy_arn": policy_arn
        }
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

    def list_automated_reasoning_policy_test_results(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_test_results_response.ListAutomatedReasoningPolicyTestResultsResponse":
        """<p>Lists test results for an Automated Reasoning policy, showing how the policy performed against various test scenarios and validation checks.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose test results you want to list.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose test results you want to list.</p>
            next_token: <p>A pagination token from a previous request to continue listing test results from where the previous request left off.</p>
            max_results: <p>The maximum number of test results to return in a single response. Valid range is 1-100.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_automated_reasoning_policy_test_results_request.ListAutomatedReasoningPolicyTestResultsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_test_results_response.ListAutomatedReasoningPolicyTestResultsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_results

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_results.list_automated_reasoning_policy_test_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.list_automated_reasoning_policy_test_results_response.ListAutomatedReasoningPolicyTestResultsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.list_automated_reasoning_policy_test_results_response

            return capo_bedrock.types.list_automated_reasoning_policy_test_results_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListAutomatedReasoningPolicyTestResults", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.list_automated_reasoning_policy_test_results_request.ListAutomatedReasoningPolicyTestResultsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }
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

    def start_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_type: "capo_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType",
        source_content: "capo_bedrock.types.automated_reasoning_policy_build_workflow_source.AutomatedReasoningPolicyBuildWorkflowSource",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.start_automated_reasoning_policy_build_workflow_response.StartAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Starts a new build workflow for an Automated Reasoning policy. This initiates the process of analyzing source documents and generating policy rules, variables, and types.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to start the build workflow.</p>
            build_workflow_type: <p>The type of build workflow to start (e.g., DOCUMENT_INGESTION for processing new documents, POLICY_REPAIR for fixing existing policies).</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>
            source_content: <p>The source content for the build workflow, such as documents to analyze or repair instructions for existing policies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.StartAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.start_automated_reasoning_policy_build_workflow_response.StartAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_build_workflow

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_build_workflow.start_automated_reasoning_policy_build_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.StartAutomatedReasoningPolicyBuildWorkflowRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request

            return capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartAutomatedReasoningPolicyBuildWorkflow", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.StartAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_type": build_workflow_type,
            "source_content": source_content,
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

    def start_automated_reasoning_policy_test_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        test_case_ids: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_case_id_list.AutomatedReasoningPolicyTestCaseIdList"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.start_automated_reasoning_policy_test_workflow_response.StartAutomatedReasoningPolicyTestWorkflowResponse":
        """<p>Initiates a test workflow to validate Automated Reasoning policy tests. The workflow executes the specified tests against the policy and generates validation results.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to test.</p>
            build_workflow_id: <p>The build workflow identifier. The build workflow must show a <code>COMPLETED</code> status before running tests.</p>
            test_case_ids: <p>The list of test identifiers to run. If not provided, all tests for the policy are run.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.start_automated_reasoning_policy_test_workflow_request.StartAutomatedReasoningPolicyTestWorkflowRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.start_automated_reasoning_policy_test_workflow_response.StartAutomatedReasoningPolicyTestWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_test_workflow

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_test_workflow.start_automated_reasoning_policy_test_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartAutomatedReasoningPolicyTestWorkflow"),
        )
        input_: capo_bedrock.types.start_automated_reasoning_policy_test_workflow_request.StartAutomatedReasoningPolicyTestWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }
        if test_case_ids is not None:
            input_["test_case_ids"] = test_case_ids
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

    def update_automated_reasoning_policy_annotations(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        annotations: "capo_bedrock.types.automated_reasoning_policy_annotation_list.AutomatedReasoningPolicyAnnotationList",
        last_updated_annotation_set_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_annotations_response.UpdateAutomatedReasoningPolicyAnnotationsResponse":
        """<p>Updates the annotations for an Automated Reasoning policy build workflow. This allows you to modify extracted rules, variables, and types before finalizing the policy.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to update.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose annotations you want to update.</p>
            annotations: <p>The updated annotations containing modified rules, variables, and types for the policy.</p>
            last_updated_annotation_set_hash: <p>The hash value of the annotation set that you're updating. This is used for optimistic concurrency control to prevent conflicting updates.</p>

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
            req: "OperationRequest[capo_bedrock.types.update_automated_reasoning_policy_annotations_request.UpdateAutomatedReasoningPolicyAnnotationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_annotations_response.UpdateAutomatedReasoningPolicyAnnotationsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_annotations

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_annotations.update_automated_reasoning_policy_annotations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.update_automated_reasoning_policy_annotations_request.UpdateAutomatedReasoningPolicyAnnotationsRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.update_automated_reasoning_policy_annotations_request

            return capo_bedrock.types.update_automated_reasoning_policy_annotations_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAutomatedReasoningPolicyAnnotations", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock.types.update_automated_reasoning_policy_annotations_request.UpdateAutomatedReasoningPolicyAnnotationsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "annotations": annotations,
            "last_updated_annotation_set_hash": last_updated_annotation_set_hash,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        query_content: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
        ] = None,
        confidence_threshold: Optional[
            "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_test_case_response.UpdateAutomatedReasoningPolicyTestCaseResponse":
        """<p>Updates an existing Automated Reasoning policy test. You can modify the content, query, expected result, and confidence threshold.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to update.</p>
            guard_content: <p>The updated content to be validated by the Automated Reasoning policy.</p>
            query_content: <p>The updated input query or prompt that generated the content.</p>
            last_updated_at: <p>The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.</p>
            expected_aggregated_findings_result: <p>The updated expected result of the Automated Reasoning check.</p>
            confidence_threshold: <p>The updated minimum confidence level for logic validation. If null is provided, the threshold will be removed.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.update_automated_reasoning_policy_test_case_request.UpdateAutomatedReasoningPolicyTestCaseRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_test_case_response.UpdateAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_test_case

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_test_case.update_automated_reasoning_policy_test_case(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.update_automated_reasoning_policy_test_case_request.UpdateAutomatedReasoningPolicyTestCaseRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.update_automated_reasoning_policy_test_case_request

            return capo_bedrock.types.update_automated_reasoning_policy_test_case_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAutomatedReasoningPolicyTestCase", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock.types.update_automated_reasoning_policy_test_case_request.UpdateAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
            "guard_content": guard_content,
            "last_updated_at": last_updated_at,
            "expected_aggregated_findings_result": expected_aggregated_findings_result,
        }
        if query_content is not None:
            input_["query_content"] = query_content
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
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


class AsyncAutomatedReasoningPolicyResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        policy_definition: Optional[
            "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_response.CreateAutomatedReasoningPolicyResponse":
        """<p>Creates an Automated Reasoning policy for Amazon Bedrock Guardrails. Automated Reasoning policies use mathematical techniques to detect hallucinations, suggest corrections, and highlight unstated assumptions in the responses of your GenAI application.</p> <p>To create a policy, you upload a source document that describes the rules that you're encoding. Automated Reasoning extracts important concepts from the source document that will become variables in the policy and infers policy rules.</p>

        Args:
            name: <p>A unique name for the Automated Reasoning policy. The name must be between 1 and 63 characters and can contain letters, numbers, hyphens, and underscores.</p>
            description: <p>A description of the Automated Reasoning policy. Use this to provide context about the policy's purpose and the types of validations it performs.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>
            policy_definition: <p>The policy definition that contains the formal logic rules, variables, and custom variable types used to validate foundation model responses in your application.</p>
            kms_key_id: <p>The identifier of the KMS key to use for encrypting the automated reasoning policy and its associated artifacts. If you don't specify a KMS key, Amazon Bedrock uses an KMS managed key for encryption. For enhanced security and control, you can specify a customer managed KMS key.</p>
            tags: <p>A list of tags to associate with the Automated Reasoning policy. Tags help you organize and manage your policies.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.create_automated_reasoning_policy_request.CreateAutomatedReasoningPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_response.CreateAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy.async_create_automated_reasoning_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.create_automated_reasoning_policy_request.CreateAutomatedReasoningPolicyRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_automated_reasoning_policy_request

            return capo_bedrock.types.create_automated_reasoning_policy_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock.types.create_automated_reasoning_policy_response.CreateAutomatedReasoningPolicyResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_automated_reasoning_policy_response

            return capo_bedrock.types.create_automated_reasoning_policy_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAutomatedReasoningPolicy",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock.types.create_automated_reasoning_policy_request.CreateAutomatedReasoningPolicyRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if policy_definition is not None:
            input_["policy_definition"] = policy_definition
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
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
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_response.GetAutomatedReasoningPolicyResponse":
        """<p>Retrieves details about an Automated Reasoning policy or policy version. Returns information including the policy definition, metadata, and timestamps.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to retrieve. Can be either the unversioned ARN for the draft policy or an ARN for a specific policy version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_request.GetAutomatedReasoningPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_response.GetAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy.async_get_automated_reasoning_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_response.GetAutomatedReasoningPolicyResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_response

            return capo_bedrock.types.get_automated_reasoning_policy_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicy", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_request.GetAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn
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
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        policy_definition: "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        name: Optional[
            "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
        ] = None,
        description: Optional[
            "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
        ] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_response.UpdateAutomatedReasoningPolicyResponse":
        """<p>Updates an existing Automated Reasoning policy with new rules, variables, or configuration. This creates a new version of the policy while preserving the previous version.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to update. This must be the ARN of a draft policy.</p>
            policy_definition: <p>The updated policy definition containing the formal logic rules, variables, and types.</p>
            name: <p>The updated name for the Automated Reasoning policy.</p>
            description: <p>The updated description for the Automated Reasoning policy.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_automated_reasoning_policy_request.UpdateAutomatedReasoningPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_response.UpdateAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy.async_update_automated_reasoning_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.update_automated_reasoning_policy_request.UpdateAutomatedReasoningPolicyRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.update_automated_reasoning_policy_request

            return capo_bedrock.types.update_automated_reasoning_policy_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock.types.update_automated_reasoning_policy_response.UpdateAutomatedReasoningPolicyResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.update_automated_reasoning_policy_response

            return capo_bedrock.types.update_automated_reasoning_policy_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAutomatedReasoningPolicy",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock.types.update_automated_reasoning_policy_request.UpdateAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn,
            "policy_definition": policy_definition,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_response.DeleteAutomatedReasoningPolicyResponse":
        """<p>Deletes an Automated Reasoning policy or policy version. This operation is idempotent. If you delete a policy more than once, each call succeeds. Deleting a policy removes it permanently and cannot be undone.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to delete.</p>
            force: <p>Specifies whether to force delete the automated reasoning policy even if it has active resources. When <code>false</code>, Amazon Bedrock validates if all artifacts have been deleted (e.g. policy version, test case, test result) for a policy before deletion. When <code>true</code>, Amazon Bedrock will delete the policy and all its artifacts without validation. Default is <code>false</code>. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_request.DeleteAutomatedReasoningPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_response.DeleteAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy.async_delete_automated_reasoning_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAutomatedReasoningPolicy")
        )
        input_: capo_bedrock.types.delete_automated_reasoning_policy_request.DeleteAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn
        }
        if force is not None:
            input_["force"] = force

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
        policy_arn: Optional[
            "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
        ] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policies_response.ListAutomatedReasoningPoliciesResponse":
        """<p>Lists all Automated Reasoning policies in your account, with optional filtering by policy ARN. This helps you manage and discover existing policies.</p>

        Args:
            policy_arn: <p>Optional filter to list only the policy versions with the specified Amazon Resource Name (ARN). If not provided, the DRAFT versions for all policies are listed.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of policies to return in a single call.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_automated_reasoning_policies_request.ListAutomatedReasoningPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policies_response.ListAutomatedReasoningPoliciesResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policies

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policies.async_list_automated_reasoning_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.list_automated_reasoning_policies_response.ListAutomatedReasoningPoliciesResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.list_automated_reasoning_policies_response

            return capo_bedrock.types.list_automated_reasoning_policies_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListAutomatedReasoningPolicies", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.list_automated_reasoning_policies_request.ListAutomatedReasoningPoliciesRequest = {}
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
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

    async def cancel_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_response.CancelAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Cancels a running Automated Reasoning policy build workflow. This stops the policy generation process and prevents further processing of the source documents.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to cancel.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to cancel. You can get this ID from the StartAutomatedReasoningPolicyBuildWorkflow response or by listing build workflows.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_request.CancelAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_response.CancelAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.cancel_automated_reasoning_policy_build_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.cancel_automated_reasoning_policy_build_workflow.async_cancel_automated_reasoning_policy_build_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CancelAutomatedReasoningPolicyBuildWorkflow"),
        )
        input_: capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_request.CancelAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent",
        expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        query_content: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        confidence_threshold: Optional[
            "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
        ] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_test_case_response.CreateAutomatedReasoningPolicyTestCaseResponse":
        """<p>Creates a test for an Automated Reasoning policy. Tests validate that your policy works as expected by providing sample inputs and expected outcomes. Use tests to verify policy behavior before deploying to production.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create the test.</p>
            guard_content: <p>The output content that's validated by the Automated Reasoning policy. This represents the foundation model response that will be checked for accuracy.</p>
            query_content: <p>The input query or prompt that generated the content. This provides context for the validation.</p>
            expected_aggregated_findings_result: <p>The expected result of the Automated Reasoning check. Valid values include: , TOO_COMPLEX, and NO_TRANSLATIONS.</p> <ul> <li> <p> <code>VALID</code> - The claims are true. The claims are implied by the premises and the Automated Reasoning policy. Given the Automated Reasoning policy and premises, it is not possible for these claims to be false. In other words, there are no alternative answers that are true that contradict the claims.</p> </li> <li> <p> <code>INVALID</code> - The claims are false. The claims are not implied by the premises and Automated Reasoning policy. Furthermore, there exists different claims that are consistent with the premises and Automated Reasoning policy.</p> </li> <li> <p> <code>SATISFIABLE</code> - The claims can be true or false. It depends on what assumptions are made for the claim to be implied from the premises and Automated Reasoning policy rules. In this situation, different assumptions can make input claims false and alternative claims true.</p> </li> <li> <p> <code>IMPOSSIBLE</code> - Automated Reasoning can’t make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.</p> </li> <li> <p> <code>TRANSLATION_AMBIGUOUS</code> - Detected an ambiguity in the translation meant it would be unsound to continue with validity checking. Additional context or follow-up questions might be needed to get translation to succeed.</p> </li> <li> <p> <code>TOO_COMPLEX</code> - The input contains too much information for Automated Reasoning to process within its latency limits.</p> </li> <li> <p> <code>NO_TRANSLATIONS</code> - Identifies that some or all of the input prompt wasn't translated into logic. This can happen if the input isn't relevant to the Automated Reasoning policy, or if the policy doesn't have variables to model relevant input. If Automated Reasoning can't translate anything, you get a single <code>NO_TRANSLATIONS</code> finding. You might also see a <code>NO_TRANSLATIONS</code> (along with other findings) if some part of the validation isn't translated.</p> </li> </ul>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>
            confidence_threshold: <p>The minimum confidence level for logic validation. Content that meets the threshold is considered a high-confidence finding that can be validated.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.create_automated_reasoning_policy_test_case_request.CreateAutomatedReasoningPolicyTestCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_test_case_response.CreateAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_test_case

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_test_case.async_create_automated_reasoning_policy_test_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.create_automated_reasoning_policy_test_case_request.CreateAutomatedReasoningPolicyTestCaseRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_automated_reasoning_policy_test_case_request

            return capo_bedrock.types.create_automated_reasoning_policy_test_case_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAutomatedReasoningPolicyTestCase", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock.types.create_automated_reasoning_policy_test_case_request.CreateAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "guard_content": guard_content,
            "expected_aggregated_findings_result": expected_aggregated_findings_result,
        }
        if query_content is not None:
            input_["query_content"] = query_content
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_automated_reasoning_policy_version(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        last_updated_definition_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_version_response.CreateAutomatedReasoningPolicyVersionResponse":
        """<p>Creates a new version of an existing Automated Reasoning policy. This allows you to iterate on your policy rules while maintaining previous versions for rollback or comparison purposes.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create a version.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>
            last_updated_definition_hash: <p>The hash of the current policy definition used as a concurrency token to ensure the policy hasn't been modified since you last retrieved it.</p>
            tags: <p>A list of tags to associate with the policy version.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.create_automated_reasoning_policy_version_request.CreateAutomatedReasoningPolicyVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_version_response.CreateAutomatedReasoningPolicyVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_version

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_version.async_create_automated_reasoning_policy_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.create_automated_reasoning_policy_version_response.CreateAutomatedReasoningPolicyVersionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.create_automated_reasoning_policy_version_response

            return capo_bedrock.types.create_automated_reasoning_policy_version_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateAutomatedReasoningPolicyVersion", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.create_automated_reasoning_policy_version_request.CreateAutomatedReasoningPolicyVersionRequest = {
            "policy_arn": policy_arn,
            "last_updated_definition_hash": last_updated_definition_hash,
        }
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

    async def delete_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_response.DeleteAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Deletes an Automated Reasoning policy build workflow and its associated artifacts. This permanently removes the workflow history and any generated assets.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to delete.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to delete.</p>
            last_updated_at: <p>The timestamp when the build workflow was last updated. This is used for optimistic concurrency control to prevent accidental deletion of workflows that have been modified.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_request.DeleteAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_response.DeleteAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_build_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_build_workflow.async_delete_automated_reasoning_policy_build_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteAutomatedReasoningPolicyBuildWorkflow"),
        )
        input_: capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_request.DeleteAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "last_updated_at": last_updated_at,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_test_case_response.DeleteAutomatedReasoningPolicyTestCaseResponse":
        """<p>Deletes an Automated Reasoning policy test. This operation is idempotent; if you delete a test more than once, each call succeeds.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to delete.</p>
            last_updated_at: <p>The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_test_case_request.DeleteAutomatedReasoningPolicyTestCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_test_case_response.DeleteAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_test_case

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_test_case.async_delete_automated_reasoning_policy_test_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAutomatedReasoningPolicyTestCase")
        )
        input_: capo_bedrock.types.delete_automated_reasoning_policy_test_case_request.DeleteAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
            "last_updated_at": last_updated_at,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_automated_reasoning_policy_version(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.export_automated_reasoning_policy_version_response.ExportAutomatedReasoningPolicyVersionResponse":
        """<p>Exports the policy definition for an Automated Reasoning policy version. Returns the complete policy definition including rules, variables, and custom variable types in a structured format.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to export. Can be either the unversioned ARN for the draft policy or a versioned ARN for a specific policy version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.export_automated_reasoning_policy_version_request.ExportAutomatedReasoningPolicyVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.export_automated_reasoning_policy_version_response.ExportAutomatedReasoningPolicyVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.export_automated_reasoning_policy_version

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.export_automated_reasoning_policy_version.async_export_automated_reasoning_policy_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.export_automated_reasoning_policy_version_response.ExportAutomatedReasoningPolicyVersionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.export_automated_reasoning_policy_version_response

            return capo_bedrock.types.export_automated_reasoning_policy_version_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ExportAutomatedReasoningPolicyVersion", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.export_automated_reasoning_policy_version_request.ExportAutomatedReasoningPolicyVersionRequest = {
            "policy_arn": policy_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_annotations(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_annotations_response.GetAutomatedReasoningPolicyAnnotationsResponse":
        """<p>Retrieves the current annotations for an Automated Reasoning policy build workflow. Annotations contain corrections to the rules, variables and types to be applied to the policy.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose annotations you want to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_annotations_request.GetAutomatedReasoningPolicyAnnotationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_annotations_response.GetAutomatedReasoningPolicyAnnotationsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_annotations

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_annotations.async_get_automated_reasoning_policy_annotations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_annotations_response.GetAutomatedReasoningPolicyAnnotationsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_annotations_response

            return capo_bedrock.types.get_automated_reasoning_policy_annotations_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyAnnotations", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_annotations_request.GetAutomatedReasoningPolicyAnnotationsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.GetAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Retrieves detailed information about an Automated Reasoning policy build workflow, including its status, configuration, and metadata.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_build_workflow_request.GetAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.GetAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow.async_get_automated_reasoning_policy_build_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.GetAutomatedReasoningPolicyBuildWorkflowResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response

            return capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyBuildWorkflow", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_build_workflow_request.GetAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_build_workflow_result_assets(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        asset_type: "capo_bedrock.types.automated_reasoning_policy_build_result_asset_type.AutomatedReasoningPolicyBuildResultAssetType",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        asset_id: Optional[
            "capo_bedrock.types.automated_reasoning_policy_build_result_asset_id.AutomatedReasoningPolicyBuildResultAssetId"
        ] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse":
        """<p>Retrieves the resulting assets from a completed Automated Reasoning policy build workflow, including build logs, quality reports, and generated policy artifacts.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow assets you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose result assets you want to retrieve.</p>
            asset_type: <p>The type of asset to retrieve (e.g., BUILD_LOG, QUALITY_REPORT, POLICY_DEFINITION, GENERATED_TEST_CASES, POLICY_SCENARIOS, FIDELITY_REPORT, ASSET_MANIFEST, SOURCE_DOCUMENT).</p>
            asset_id: <p>The unique identifier of the specific asset to retrieve when multiple assets of the same type exist. This is required when retrieving SOURCE_DOCUMENT assets, as multiple source documents may have been used in the workflow. The asset ID can be obtained from the asset manifest.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_request.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow_result_assets

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow_result_assets.async_get_automated_reasoning_policy_build_workflow_result_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response

            return capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyBuildWorkflowResultAssets",
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_request.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "asset_type": asset_type,
        }
        if asset_id is not None:
            input_["asset_id"] = asset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_next_scenario(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.GetAutomatedReasoningPolicyNextScenarioResponse":
        """<p>Retrieves the next test scenario for validating an Automated Reasoning policy. This is used during the interactive policy refinement process to test policy behavior.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which you want to get the next test scenario.</p>
            build_workflow_id: <p>The unique identifier of the build workflow associated with the test scenarios.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_next_scenario_request.GetAutomatedReasoningPolicyNextScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.GetAutomatedReasoningPolicyNextScenarioResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_next_scenario

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_next_scenario.async_get_automated_reasoning_policy_next_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.GetAutomatedReasoningPolicyNextScenarioResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response

            return capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyNextScenario", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_next_scenario_request.GetAutomatedReasoningPolicyNextScenarioRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_test_case_response.GetAutomatedReasoningPolicyTestCaseResponse":
        """<p>Retrieves details about a specific Automated Reasoning policy test.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_test_case_request.GetAutomatedReasoningPolicyTestCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_test_case_response.GetAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_case

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_case.async_get_automated_reasoning_policy_test_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_test_case_response.GetAutomatedReasoningPolicyTestCaseResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_test_case_response

            return capo_bedrock.types.get_automated_reasoning_policy_test_case_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyTestCase", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_test_case_request.GetAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_test_result(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_test_result_response.GetAutomatedReasoningPolicyTestResultResponse":
        """<p>Retrieves the test result for a specific Automated Reasoning policy test. Returns detailed validation findings and execution status.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>
            build_workflow_id: <p>The build workflow identifier. The build workflow must display a <code>COMPLETED</code> status to get results.</p>
            test_case_id: <p>The unique identifier of the test for which to retrieve results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_test_result_request.GetAutomatedReasoningPolicyTestResultRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_test_result_response.GetAutomatedReasoningPolicyTestResultResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_result

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_result.async_get_automated_reasoning_policy_test_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.get_automated_reasoning_policy_test_result_response.GetAutomatedReasoningPolicyTestResultResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.get_automated_reasoning_policy_test_result_response

            return capo_bedrock.types.get_automated_reasoning_policy_test_result_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetAutomatedReasoningPolicyTestResult", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.get_automated_reasoning_policy_test_result_request.GetAutomatedReasoningPolicyTestResultRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "test_case_id": test_case_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_automated_reasoning_policy_build_workflows(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_build_workflows_response.ListAutomatedReasoningPolicyBuildWorkflowsResponse":
        """<p>Lists all build workflows for an Automated Reasoning policy, showing the history of policy creation and modification attempts.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflows you want to list.</p>
            next_token: <p>A pagination token from a previous request to continue listing build workflows from where the previous request left off.</p>
            max_results: <p>The maximum number of build workflows to return in a single response. Valid range is 1-100.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_automated_reasoning_policy_build_workflows_request.ListAutomatedReasoningPolicyBuildWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_build_workflows_response.ListAutomatedReasoningPolicyBuildWorkflowsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_build_workflows

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_build_workflows.async_list_automated_reasoning_policy_build_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAutomatedReasoningPolicyBuildWorkflows"),
        )
        input_: capo_bedrock.types.list_automated_reasoning_policy_build_workflows_request.ListAutomatedReasoningPolicyBuildWorkflowsRequest = {
            "policy_arn": policy_arn
        }
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

    async def list_automated_reasoning_policy_test_cases(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.ListAutomatedReasoningPolicyTestCasesResponse":
        """<p>Lists tests for an Automated Reasoning policy. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to list tests.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of tests to return in a single call.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_automated_reasoning_policy_test_cases_request.ListAutomatedReasoningPolicyTestCasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.ListAutomatedReasoningPolicyTestCasesResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_cases

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_cases.async_list_automated_reasoning_policy_test_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.ListAutomatedReasoningPolicyTestCasesResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.list_automated_reasoning_policy_test_cases_response

            return capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListAutomatedReasoningPolicyTestCases", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.list_automated_reasoning_policy_test_cases_request.ListAutomatedReasoningPolicyTestCasesRequest = {
            "policy_arn": policy_arn
        }
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

    async def list_automated_reasoning_policy_test_results(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_test_results_response.ListAutomatedReasoningPolicyTestResultsResponse":
        """<p>Lists test results for an Automated Reasoning policy, showing how the policy performed against various test scenarios and validation checks.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose test results you want to list.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose test results you want to list.</p>
            next_token: <p>A pagination token from a previous request to continue listing test results from where the previous request left off.</p>
            max_results: <p>The maximum number of test results to return in a single response. Valid range is 1-100.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_automated_reasoning_policy_test_results_request.ListAutomatedReasoningPolicyTestResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_test_results_response.ListAutomatedReasoningPolicyTestResultsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_results

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_results.async_list_automated_reasoning_policy_test_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock.types.list_automated_reasoning_policy_test_results_response.ListAutomatedReasoningPolicyTestResultsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock.types.list_automated_reasoning_policy_test_results_response

            return capo_bedrock.types.list_automated_reasoning_policy_test_results_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListAutomatedReasoningPolicyTestResults", redact_output=_redact_output
            ),
        )
        input_: capo_bedrock.types.list_automated_reasoning_policy_test_results_request.ListAutomatedReasoningPolicyTestResultsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }
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

    async def start_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_type: "capo_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType",
        source_content: "capo_bedrock.types.automated_reasoning_policy_build_workflow_source.AutomatedReasoningPolicyBuildWorkflowSource",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.start_automated_reasoning_policy_build_workflow_response.StartAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Starts a new build workflow for an Automated Reasoning policy. This initiates the process of analyzing source documents and generating policy rules, variables, and types.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to start the build workflow.</p>
            build_workflow_type: <p>The type of build workflow to start (e.g., DOCUMENT_INGESTION for processing new documents, POLICY_REPAIR for fixing existing policies).</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>
            source_content: <p>The source content for the build workflow, such as documents to analyze or repair instructions for existing policies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.StartAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.start_automated_reasoning_policy_build_workflow_response.StartAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_build_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_build_workflow.async_start_automated_reasoning_policy_build_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.StartAutomatedReasoningPolicyBuildWorkflowRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request

            return capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartAutomatedReasoningPolicyBuildWorkflow", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.StartAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_type": build_workflow_type,
            "source_content": source_content,
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

    async def start_automated_reasoning_policy_test_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        test_case_ids: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_case_id_list.AutomatedReasoningPolicyTestCaseIdList"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.start_automated_reasoning_policy_test_workflow_response.StartAutomatedReasoningPolicyTestWorkflowResponse":
        """<p>Initiates a test workflow to validate Automated Reasoning policy tests. The workflow executes the specified tests against the policy and generates validation results.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to test.</p>
            build_workflow_id: <p>The build workflow identifier. The build workflow must show a <code>COMPLETED</code> status before running tests.</p>
            test_case_ids: <p>The list of test identifiers to run. If not provided, all tests for the policy are run.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.start_automated_reasoning_policy_test_workflow_request.StartAutomatedReasoningPolicyTestWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.start_automated_reasoning_policy_test_workflow_response.StartAutomatedReasoningPolicyTestWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_test_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_test_workflow.async_start_automated_reasoning_policy_test_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartAutomatedReasoningPolicyTestWorkflow"),
        )
        input_: capo_bedrock.types.start_automated_reasoning_policy_test_workflow_request.StartAutomatedReasoningPolicyTestWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }
        if test_case_ids is not None:
            input_["test_case_ids"] = test_case_ids
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

    async def update_automated_reasoning_policy_annotations(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        annotations: "capo_bedrock.types.automated_reasoning_policy_annotation_list.AutomatedReasoningPolicyAnnotationList",
        last_updated_annotation_set_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_annotations_response.UpdateAutomatedReasoningPolicyAnnotationsResponse":
        """<p>Updates the annotations for an Automated Reasoning policy build workflow. This allows you to modify extracted rules, variables, and types before finalizing the policy.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to update.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose annotations you want to update.</p>
            annotations: <p>The updated annotations containing modified rules, variables, and types for the policy.</p>
            last_updated_annotation_set_hash: <p>The hash value of the annotation set that you're updating. This is used for optimistic concurrency control to prevent conflicting updates.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.update_automated_reasoning_policy_annotations_request.UpdateAutomatedReasoningPolicyAnnotationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_annotations_response.UpdateAutomatedReasoningPolicyAnnotationsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_annotations

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_annotations.async_update_automated_reasoning_policy_annotations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.update_automated_reasoning_policy_annotations_request.UpdateAutomatedReasoningPolicyAnnotationsRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.update_automated_reasoning_policy_annotations_request

            return capo_bedrock.types.update_automated_reasoning_policy_annotations_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAutomatedReasoningPolicyAnnotations", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock.types.update_automated_reasoning_policy_annotations_request.UpdateAutomatedReasoningPolicyAnnotationsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "annotations": annotations,
            "last_updated_annotation_set_hash": last_updated_annotation_set_hash,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        query_content: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
        ] = None,
        confidence_threshold: Optional[
            "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_test_case_response.UpdateAutomatedReasoningPolicyTestCaseResponse":
        """<p>Updates an existing Automated Reasoning policy test. You can modify the content, query, expected result, and confidence threshold.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to update.</p>
            guard_content: <p>The updated content to be validated by the Automated Reasoning policy.</p>
            query_content: <p>The updated input query or prompt that generated the content.</p>
            last_updated_at: <p>The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.</p>
            expected_aggregated_findings_result: <p>The updated expected result of the Automated Reasoning check.</p>
            confidence_threshold: <p>The updated minimum confidence level for logic validation. If null is provided, the threshold will be removed.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_automated_reasoning_policy_test_case_request.UpdateAutomatedReasoningPolicyTestCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_test_case_response.UpdateAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_test_case

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_test_case.async_update_automated_reasoning_policy_test_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock.types.update_automated_reasoning_policy_test_case_request.UpdateAutomatedReasoningPolicyTestCaseRequest",
        ) -> dict[str, Any]:
            import capo_bedrock.types.update_automated_reasoning_policy_test_case_request

            return capo_bedrock.types.update_automated_reasoning_policy_test_case_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateAutomatedReasoningPolicyTestCase", redact_input=_redact_input
            ),
        )
        input_: capo_bedrock.types.update_automated_reasoning_policy_test_case_request.UpdateAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
            "guard_content": guard_content,
            "last_updated_at": last_updated_at,
            "expected_aggregated_findings_result": expected_aggregated_findings_result,
        }
        if query_content is not None:
            input_["query_content"] = query_content
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
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
