from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agent._auth._signers
import capo_bedrock_agent._auth._sigv4
from capo_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.create_retrieval_instruction_request
    import capo_bedrock_agent.types.create_retrieval_instruction_response
    import capo_bedrock_agent.types.create_retrieval_instruction_version_request
    import capo_bedrock_agent.types.create_retrieval_instruction_version_response
    import capo_bedrock_agent.types.delete_retrieval_instruction_request
    import capo_bedrock_agent.types.delete_retrieval_instruction_response
    import capo_bedrock_agent.types.get_retrieval_instruction_request
    import capo_bedrock_agent.types.get_retrieval_instruction_response
    import capo_bedrock_agent.types.kms_key_arn
    import capo_bedrock_agent.types.list_retrieval_instruction_versions_request
    import capo_bedrock_agent.types.list_retrieval_instruction_versions_response
    import capo_bedrock_agent.types.list_retrieval_instructions_request
    import capo_bedrock_agent.types.list_retrieval_instructions_response
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.retrieval_instruction_content
    import capo_bedrock_agent.types.retrieval_instruction_description
    import capo_bedrock_agent.types.retrieval_instruction_id
    import capo_bedrock_agent.types.retrieval_instruction_max_results
    import capo_bedrock_agent.types.retrieval_instruction_name
    import capo_bedrock_agent.types.retrieval_instruction_numerical_version
    import capo_bedrock_agent.types.retrieval_instruction_status
    import capo_bedrock_agent.types.retrieval_instruction_summary
    import capo_bedrock_agent.types.retrieval_instruction_version_selector
    import capo_bedrock_agent.types.retrieval_instruction_version_summary
    import capo_bedrock_agent.types.tags_map
    import capo_bedrock_agent.types.update_retrieval_instruction_request
    import capo_bedrock_agent.types.update_retrieval_instruction_response
    from capo_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from capo_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class RetrievalInstructionResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bedrock_agent.types.retrieval_instruction_name.RetrievalInstructionName",
        instruction: "capo_bedrock_agent.types.retrieval_instruction_content.RetrievalInstructionContent",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_retrieval_instruction_response.CreateRetrievalInstructionResponse":
        """<p>Creates a new retrieval instruction. The retrieval instruction is usable once its status becomes ACTIVE. Use GetRetrievalInstruction to check whether it is ready.</p>

        Args:
            client_token: <p>A caller-supplied token that makes a retried create return the existing resource rather than a second one. The window is 8 hours.</p>
            name: <p>Specifies the name of the retrieval instruction.</p>
            instruction: <p>The instruction content, as a set of named fields. Get does not return this field until the create review passes.</p>
            description: <p>Specifies a description of the retrieval instruction.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of a customer managed AWS Key Management Service (AWS KMS) key used to encrypt the instruction content at rest. If you omit it, the service uses an AWS owned key. You fix the key at create and cannot change it later.</p>
            tags: <p>Tags for the retrieval instruction.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.create_retrieval_instruction_request.CreateRetrievalInstructionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_retrieval_instruction_response.CreateRetrievalInstructionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_retrieval_instruction

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_retrieval_instruction.create_retrieval_instruction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.create_retrieval_instruction_request.CreateRetrievalInstructionRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.create_retrieval_instruction_request

            return capo_bedrock_agent.types.create_retrieval_instruction_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.create_retrieval_instruction_response.CreateRetrievalInstructionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.create_retrieval_instruction_response

            return capo_bedrock_agent.types.create_retrieval_instruction_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRetrievalInstruction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.create_retrieval_instruction_request.CreateRetrievalInstructionRequest = {
            "name": name,
            "instruction": instruction,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
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
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        retrieval_instruction_version: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_version_selector.RetrievalInstructionVersionSelector"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_retrieval_instruction_response.GetRetrievalInstructionResponse":
        """<p>Gets a retrieval instruction. Also used to poll the terminal reporting of an asynchronous create or update.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction to get.</p>
            retrieval_instruction_version: <p>The version to return: a version number, or DRAFT for the retrieval instruction's current reviewed content. When omitted, DRAFT is used. This default is permanent: omitting retrievalInstructionVersion will never resolve to a numbered version.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.get_retrieval_instruction_request.GetRetrievalInstructionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.get_retrieval_instruction_response.GetRetrievalInstructionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_retrieval_instruction

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_retrieval_instruction.get_retrieval_instruction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.get_retrieval_instruction_response.GetRetrievalInstructionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.get_retrieval_instruction_response

            return capo_bedrock_agent.types.get_retrieval_instruction_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetRetrievalInstruction", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.get_retrieval_instruction_request.GetRetrievalInstructionRequest = {
            "retrieval_instruction_id": retrieval_instruction_id
        }
        if retrieval_instruction_version is not None:
            input_["retrieval_instruction_version"] = retrieval_instruction_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        instruction: "capo_bedrock_agent.types.retrieval_instruction_content.RetrievalInstructionContent",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_retrieval_instruction_response.UpdateRetrievalInstructionResponse":
        """<p>Updates the content of a retrieval instruction. The update is processed asynchronously; the stored content is a candidate until content review passes, and the served content does not change while the update is in flight. The service rejects the request with ConflictException while lastTransitionStatus is CREATING or UPDATING.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction to update.</p>
            instruction: <p>The replacement instruction content. This is a full replacement of all four fields, not a patch. During UPDATING, Get continues to return the previously-served content until the update review passes.</p>
            description: <p>A replacement description; applied together with the content when the review passes. Omit to clear.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.update_retrieval_instruction_request.UpdateRetrievalInstructionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.update_retrieval_instruction_response.UpdateRetrievalInstructionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_retrieval_instruction

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_retrieval_instruction.update_retrieval_instruction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.update_retrieval_instruction_request.UpdateRetrievalInstructionRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.update_retrieval_instruction_request

            return capo_bedrock_agent.types.update_retrieval_instruction_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.update_retrieval_instruction_response.UpdateRetrievalInstructionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.update_retrieval_instruction_response

            return capo_bedrock_agent.types.update_retrieval_instruction_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateRetrievalInstruction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.update_retrieval_instruction_request.UpdateRetrievalInstructionRequest = {
            "retrieval_instruction_id": retrieval_instruction_id,
            "instruction": instruction,
        }
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
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        retrieval_instruction_version: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_numerical_version.RetrievalInstructionNumericalVersion"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_retrieval_instruction_response.DeleteRetrievalInstructionResponse":
        """<p>Deletes a retrieval instruction or a single version of it. Omit retrievalInstructionVersion to delete the retrieval instruction itself; the service rejects that request with ConflictException while the retrieval instruction has versions or while lastTransitionStatus is CREATING or UPDATING. Specify retrievalInstructionVersion to delete only that version; the retrieval instruction and its other versions are unaffected.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction to delete.</p>
            retrieval_instruction_version: <p>The version to delete. Omit this field to delete the retrieval instruction itself, which you can do only when it has no versions; while any version exists the service rejects the request with ConflictException. You cannot delete DRAFT on its own; deleting the retrieval instruction removes it.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.delete_retrieval_instruction_request.DeleteRetrievalInstructionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.delete_retrieval_instruction_response.DeleteRetrievalInstructionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_retrieval_instruction

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_retrieval_instruction.delete_retrieval_instruction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRetrievalInstruction")
        )
        input_: capo_bedrock_agent.types.delete_retrieval_instruction_request.DeleteRetrievalInstructionRequest = {
            "retrieval_instruction_id": retrieval_instruction_id
        }
        if retrieval_instruction_version is not None:
            input_["retrieval_instruction_version"] = retrieval_instruction_version

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
        status: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_status.RetrievalInstructionStatus"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_max_results.RetrievalInstructionMaxResults"
        ] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_retrieval_instructions_response.ListRetrievalInstructionsResponse":
        """<p>Lists the retrieval instructions in the caller's account. Results are paginated. Use the nextToken parameter to retrieve additional results.</p>

        Args:
            status: <p>Return only instructions with this availability status.</p>
            max_results: <p>The maximum number of results to return in a single page. The effective upper bound is enforced service-side.</p>
            next_token: <p>The pagination token from a previous ListRetrievalInstructions response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_retrieval_instructions_request.ListRetrievalInstructionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_retrieval_instructions_response.ListRetrievalInstructionsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_retrieval_instructions

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_retrieval_instructions.list_retrieval_instructions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.list_retrieval_instructions_response.ListRetrievalInstructionsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.list_retrieval_instructions_response

            return capo_bedrock_agent.types.list_retrieval_instructions_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListRetrievalInstructions", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.list_retrieval_instructions_request.ListRetrievalInstructionsRequest = {}
        if status is not None:
            input_["status"] = status
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

    def create_retrieval_instruction_version(
        self,
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_retrieval_instruction_version_response.CreateRetrievalInstructionVersionResponse":
        """<p>Creates an immutable numbered version from the retrieval instruction's current reviewed content. The service creates the version synchronously.</p> <p>The service numbers versions from 1 and assigns them in order, never reusing a number.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction to version.</p>
            description: <p>A description of this version. Independent of the retrieval instruction's own description.</p>
            client_token: <p>A caller-supplied token that makes a retried call return the version created by the first call rather than a second version. The window is 8 hours.</p>

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
            req: "OperationRequest[capo_bedrock_agent.types.create_retrieval_instruction_version_request.CreateRetrievalInstructionVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.create_retrieval_instruction_version_response.CreateRetrievalInstructionVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_retrieval_instruction_version

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_retrieval_instruction_version.create_retrieval_instruction_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.create_retrieval_instruction_version_request.CreateRetrievalInstructionVersionRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.create_retrieval_instruction_version_request

            return capo_bedrock_agent.types.create_retrieval_instruction_version_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.create_retrieval_instruction_version_response.CreateRetrievalInstructionVersionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.create_retrieval_instruction_version_response

            return capo_bedrock_agent.types.create_retrieval_instruction_version_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRetrievalInstructionVersion",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.create_retrieval_instruction_version_request.CreateRetrievalInstructionVersionRequest = {
            "retrieval_instruction_id": retrieval_instruction_id
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_retrieval_instruction_versions(
        self,
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_max_results.RetrievalInstructionMaxResults"
        ] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_retrieval_instruction_versions_response.ListRetrievalInstructionVersionsResponse":
        """<p>Lists the numbered versions of a retrieval instruction, newest first. DRAFT is not listed; read it with GetRetrievalInstruction without retrievalInstructionVersion. Results are paginated. Use the nextToken parameter to retrieve additional results.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction whose versions to list.</p>
            max_results: <p>Specifies the maximum number of versions to return in a single page. The service enforces the effective upper bound.</p>
            next_token: <p>The pagination token from a previous ListRetrievalInstructionVersions response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent.types.list_retrieval_instruction_versions_request.ListRetrievalInstructionVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent.types.list_retrieval_instruction_versions_response.ListRetrievalInstructionVersionsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_retrieval_instruction_versions

            output, http_response = (
                capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_retrieval_instruction_versions.list_retrieval_instruction_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRetrievalInstructionVersions")
        )
        input_: capo_bedrock_agent.types.list_retrieval_instruction_versions_request.ListRetrievalInstructionVersionsRequest = {
            "retrieval_instruction_id": retrieval_instruction_id
        }
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


class AsyncRetrievalInstructionResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bedrock_agent.types.retrieval_instruction_name.RetrievalInstructionName",
        instruction: "capo_bedrock_agent.types.retrieval_instruction_content.RetrievalInstructionContent",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
        ] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agent.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agent.types.create_retrieval_instruction_response.CreateRetrievalInstructionResponse":
        """<p>Creates a new retrieval instruction. The retrieval instruction is usable once its status becomes ACTIVE. Use GetRetrievalInstruction to check whether it is ready.</p>

        Args:
            client_token: <p>A caller-supplied token that makes a retried create return the existing resource rather than a second one. The window is 8 hours.</p>
            name: <p>Specifies the name of the retrieval instruction.</p>
            instruction: <p>The instruction content, as a set of named fields. Get does not return this field until the create review passes.</p>
            description: <p>Specifies a description of the retrieval instruction.</p>
            customer_encryption_key_arn: <p>The Amazon Resource Name (ARN) of a customer managed AWS Key Management Service (AWS KMS) key used to encrypt the instruction content at rest. If you omit it, the service uses an AWS owned key. You fix the key at create and cannot change it later.</p>
            tags: <p>Tags for the retrieval instruction.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_retrieval_instruction_request.CreateRetrievalInstructionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_retrieval_instruction_response.CreateRetrievalInstructionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_retrieval_instruction

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_retrieval_instruction.async_create_retrieval_instruction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.create_retrieval_instruction_request.CreateRetrievalInstructionRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.create_retrieval_instruction_request

            return capo_bedrock_agent.types.create_retrieval_instruction_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.create_retrieval_instruction_response.CreateRetrievalInstructionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.create_retrieval_instruction_response

            return capo_bedrock_agent.types.create_retrieval_instruction_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRetrievalInstruction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.create_retrieval_instruction_request.CreateRetrievalInstructionRequest = {
            "name": name,
            "instruction": instruction,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
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
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        retrieval_instruction_version: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_version_selector.RetrievalInstructionVersionSelector"
        ] = None,
    ) -> "capo_bedrock_agent.types.get_retrieval_instruction_response.GetRetrievalInstructionResponse":
        """<p>Gets a retrieval instruction. Also used to poll the terminal reporting of an asynchronous create or update.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction to get.</p>
            retrieval_instruction_version: <p>The version to return: a version number, or DRAFT for the retrieval instruction's current reviewed content. When omitted, DRAFT is used. This default is permanent: omitting retrievalInstructionVersion will never resolve to a numbered version.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.get_retrieval_instruction_request.GetRetrievalInstructionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.get_retrieval_instruction_response.GetRetrievalInstructionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_retrieval_instruction

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_retrieval_instruction.async_get_retrieval_instruction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.get_retrieval_instruction_response.GetRetrievalInstructionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.get_retrieval_instruction_response

            return capo_bedrock_agent.types.get_retrieval_instruction_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetRetrievalInstruction", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.get_retrieval_instruction_request.GetRetrievalInstructionRequest = {
            "retrieval_instruction_id": retrieval_instruction_id
        }
        if retrieval_instruction_version is not None:
            input_["retrieval_instruction_version"] = retrieval_instruction_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        instruction: "capo_bedrock_agent.types.retrieval_instruction_content.RetrievalInstructionContent",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
        ] = None,
    ) -> "capo_bedrock_agent.types.update_retrieval_instruction_response.UpdateRetrievalInstructionResponse":
        """<p>Updates the content of a retrieval instruction. The update is processed asynchronously; the stored content is a candidate until content review passes, and the served content does not change while the update is in flight. The service rejects the request with ConflictException while lastTransitionStatus is CREATING or UPDATING.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction to update.</p>
            instruction: <p>The replacement instruction content. This is a full replacement of all four fields, not a patch. During UPDATING, Get continues to return the previously-served content until the update review passes.</p>
            description: <p>A replacement description; applied together with the content when the review passes. Omit to clear.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.update_retrieval_instruction_request.UpdateRetrievalInstructionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.update_retrieval_instruction_response.UpdateRetrievalInstructionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_retrieval_instruction

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.update_retrieval_instruction.async_update_retrieval_instruction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.update_retrieval_instruction_request.UpdateRetrievalInstructionRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.update_retrieval_instruction_request

            return capo_bedrock_agent.types.update_retrieval_instruction_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.update_retrieval_instruction_response.UpdateRetrievalInstructionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.update_retrieval_instruction_response

            return capo_bedrock_agent.types.update_retrieval_instruction_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateRetrievalInstruction",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.update_retrieval_instruction_request.UpdateRetrievalInstructionRequest = {
            "retrieval_instruction_id": retrieval_instruction_id,
            "instruction": instruction,
        }
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
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        retrieval_instruction_version: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_numerical_version.RetrievalInstructionNumericalVersion"
        ] = None,
    ) -> "capo_bedrock_agent.types.delete_retrieval_instruction_response.DeleteRetrievalInstructionResponse":
        """<p>Deletes a retrieval instruction or a single version of it. Omit retrievalInstructionVersion to delete the retrieval instruction itself; the service rejects that request with ConflictException while the retrieval instruction has versions or while lastTransitionStatus is CREATING or UPDATING. Specify retrievalInstructionVersion to delete only that version; the retrieval instruction and its other versions are unaffected.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction to delete.</p>
            retrieval_instruction_version: <p>The version to delete. Omit this field to delete the retrieval instruction itself, which you can do only when it has no versions; while any version exists the service rejects the request with ConflictException. You cannot delete DRAFT on its own; deleting the retrieval instruction removes it.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.delete_retrieval_instruction_request.DeleteRetrievalInstructionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.delete_retrieval_instruction_response.DeleteRetrievalInstructionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_retrieval_instruction

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_retrieval_instruction.async_delete_retrieval_instruction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRetrievalInstruction")
        )
        input_: capo_bedrock_agent.types.delete_retrieval_instruction_request.DeleteRetrievalInstructionRequest = {
            "retrieval_instruction_id": retrieval_instruction_id
        }
        if retrieval_instruction_version is not None:
            input_["retrieval_instruction_version"] = retrieval_instruction_version

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
        status: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_status.RetrievalInstructionStatus"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_max_results.RetrievalInstructionMaxResults"
        ] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_retrieval_instructions_response.ListRetrievalInstructionsResponse":
        """<p>Lists the retrieval instructions in the caller's account. Results are paginated. Use the nextToken parameter to retrieve additional results.</p>

        Args:
            status: <p>Return only instructions with this availability status.</p>
            max_results: <p>The maximum number of results to return in a single page. The effective upper bound is enforced service-side.</p>
            next_token: <p>The pagination token from a previous ListRetrievalInstructions response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_retrieval_instructions_request.ListRetrievalInstructionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_retrieval_instructions_response.ListRetrievalInstructionsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_retrieval_instructions

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_retrieval_instructions.async_list_retrieval_instructions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agent.types.list_retrieval_instructions_response.ListRetrievalInstructionsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.list_retrieval_instructions_response

            return capo_bedrock_agent.types.list_retrieval_instructions_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListRetrievalInstructions", redact_output=_redact_output),
        )
        input_: capo_bedrock_agent.types.list_retrieval_instructions_request.ListRetrievalInstructionsRequest = {}
        if status is not None:
            input_["status"] = status
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

    async def create_retrieval_instruction_version(
        self,
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        description: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_description.RetrievalInstructionDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agent.types.create_retrieval_instruction_version_response.CreateRetrievalInstructionVersionResponse":
        """<p>Creates an immutable numbered version from the retrieval instruction's current reviewed content. The service creates the version synchronously.</p> <p>The service numbers versions from 1 and assigns them in order, never reusing a number.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction to version.</p>
            description: <p>A description of this version. Independent of the retrieval instruction's own description.</p>
            client_token: <p>A caller-supplied token that makes a retried call return the version created by the first call rather than a second version. The window is 8 hours.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agent.types.create_retrieval_instruction_version_request.CreateRetrievalInstructionVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.create_retrieval_instruction_version_response.CreateRetrievalInstructionVersionResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_retrieval_instruction_version

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.create_retrieval_instruction_version.async_create_retrieval_instruction_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agent.types.create_retrieval_instruction_version_request.CreateRetrievalInstructionVersionRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.create_retrieval_instruction_version_request

            return capo_bedrock_agent.types.create_retrieval_instruction_version_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agent.types.create_retrieval_instruction_version_response.CreateRetrievalInstructionVersionResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agent.types.create_retrieval_instruction_version_response

            return capo_bedrock_agent.types.create_retrieval_instruction_version_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateRetrievalInstructionVersion",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agent.types.create_retrieval_instruction_version_request.CreateRetrievalInstructionVersionRequest = {
            "retrieval_instruction_id": retrieval_instruction_id
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_retrieval_instruction_versions(
        self,
        retrieval_instruction_id: "capo_bedrock_agent.types.retrieval_instruction_id.RetrievalInstructionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent.types.retrieval_instruction_max_results.RetrievalInstructionMaxResults"
        ] = None,
        next_token: Optional["capo_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "capo_bedrock_agent.types.list_retrieval_instruction_versions_response.ListRetrievalInstructionVersionsResponse":
        """<p>Lists the numbered versions of a retrieval instruction, newest first. DRAFT is not listed; read it with GetRetrievalInstruction without retrievalInstructionVersion. Results are paginated. Use the nextToken parameter to retrieve additional results.</p>

        Args:
            retrieval_instruction_id: <p>The identifier of the retrieval instruction whose versions to list.</p>
            max_results: <p>Specifies the maximum number of versions to return in a single page. The service enforces the effective upper bound.</p>
            next_token: <p>The pagination token from a previous ListRetrievalInstructionVersions response.</p>

        Raises:
            capo_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent.types.list_retrieval_instruction_versions_request.ListRetrievalInstructionVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent.types.list_retrieval_instruction_versions_response.ListRetrievalInstructionVersionsResponse"
        ]:
            import capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_retrieval_instruction_versions

            (
                output,
                http_response,
            ) = await capo_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_retrieval_instruction_versions.async_list_retrieval_instruction_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRetrievalInstructionVersions")
        )
        input_: capo_bedrock_agent.types.list_retrieval_instruction_versions_request.ListRetrievalInstructionVersionsRequest = {
            "retrieval_instruction_id": retrieval_instruction_id
        }
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
