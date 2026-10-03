from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.create_evaluator_request
    import capo_bedrock_agentcore_control.types.create_evaluator_response
    import capo_bedrock_agentcore_control.types.custom_evaluator_name
    import capo_bedrock_agentcore_control.types.delete_evaluator_request
    import capo_bedrock_agentcore_control.types.delete_evaluator_response
    import capo_bedrock_agentcore_control.types.evaluator_config
    import capo_bedrock_agentcore_control.types.evaluator_description
    import capo_bedrock_agentcore_control.types.evaluator_id
    import capo_bedrock_agentcore_control.types.evaluator_level
    import capo_bedrock_agentcore_control.types.evaluator_summary
    import capo_bedrock_agentcore_control.types.get_evaluator_request
    import capo_bedrock_agentcore_control.types.get_evaluator_response
    import capo_bedrock_agentcore_control.types.included_data
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.list_evaluators_request
    import capo_bedrock_agentcore_control.types.list_evaluators_response
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.update_evaluator_request
    import capo_bedrock_agentcore_control.types.update_evaluator_response
    from capo_bedrock_agentcore_control._services.async_bedrock_agent_core_control import (
        AsyncBedrockAgentCoreControlClient,
        AsyncBedrockAgentCoreControlClientConfig,
    )
    from capo_bedrock_agentcore_control._services.bedrock_agent_core_control import (
        BedrockAgentCoreControlClient,
        BedrockAgentCoreControlClientConfig,
    )


class Evaluator:
    def __init__(self, service: BedrockAgentCoreControlClient) -> None:
        self._service = service

    def create(
        self,
        evaluator_name: "capo_bedrock_agentcore_control.types.custom_evaluator_name.CustomEvaluatorName",
        evaluator_config: "capo_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig",
        level: "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_evaluator_response.CreateEvaluatorResponse":
        """<p> Creates a custom evaluator for agent quality assessment. Custom evaluators can use either LLM-as-a-Judge configurations with user-defined prompts, rating scales, and model settings, or code-based configurations with customer-managed Lambda functions to evaluate agent performance at tool call, trace, or session levels. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            evaluator_name: <p> The name of the evaluator. Must be unique within your account. </p>
            description: <p> The description of the evaluator that explains its purpose and evaluation criteria. </p>
            evaluator_config: <p> The configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function. </p>
            level: <p> The evaluation level that determines the scope of evaluation. Valid values are <code>TOOL_CALL</code> for individual tool invocations, <code>TRACE</code> for single request-response interactions, or <code>SESSION</code> for entire conversation sessions. </p>
            kms_key_arn: <p> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data, including instructions and rating scale. If you don't specify a KMS key, the evaluator data is encrypted with an Amazon Web Services owned key. Only symmetric encryption KMS keys are supported. For more information, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html">Encryption at rest for AgentCore Evaluations</a>. </p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Evaluator. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_evaluator_request.CreateEvaluatorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_evaluator_response.CreateEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_evaluator

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_evaluator.create_evaluator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_evaluator_request.CreateEvaluatorRequest = {
            "evaluator_name": evaluator_name,
            "evaluator_config": evaluator_config,
            "level": level,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        included_data: Optional[
            "capo_bedrock_agentcore_control.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_evaluator_response.GetEvaluatorResponse":
        """<p> Retrieves detailed information about an evaluator, including its configuration, status, and metadata. Works with both built-in and custom evaluators. </p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to retrieve. Can be a built-in evaluator ID (e.g., Builtin.Helpfulness) or a custom evaluator ID. </p>
            included_data: <p> Controls which data is returned in the response. <code>ALL_DATA</code> (default) returns the full evaluator including decrypted instructions and rating scale. For evaluators encrypted with a customer managed KMS key, this requires <code>kms:Decrypt</code> permission on the key. <code>METADATA_ONLY</code> returns evaluator metadata and model configuration without instructions or rating scale, and does not require any KMS permissions. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_evaluator_request.GetEvaluatorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_evaluator_response.GetEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_evaluator

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_evaluator.get_evaluator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_evaluator_request.GetEvaluatorRequest = {
            "evaluator_id": evaluator_id
        }
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
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
        ] = None,
        evaluator_config: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig"
        ] = None,
        level: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_evaluator_response.UpdateEvaluatorResponse":
        """<p> Updates a custom evaluator's configuration, description, or evaluation level. Built-in evaluators cannot be updated. The evaluator must not be locked for modification. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            evaluator_id: <p> The unique identifier of the evaluator to update. </p>
            description: <p> The updated description of the evaluator. </p>
            evaluator_config: <p> The updated configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function. </p>
            level: <p> The updated evaluation level (<code>TOOL_CALL</code>, <code>TRACE</code>, or <code>SESSION</code>) that determines the scope of evaluation. </p>
            kms_key_arn: <p> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data. Specify a new key ARN to rotate the encryption key, or specify a key ARN to add encryption to an evaluator that was previously created without one. When you rotate to a new key, the service decrypts the existing data with the old key and re-encrypts it with the new key. Only symmetric encryption KMS keys are supported. For more information, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html">Encryption at rest for AgentCore Evaluations</a>. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_evaluator_request.UpdateEvaluatorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_evaluator_response.UpdateEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_evaluator

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_evaluator.update_evaluator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_evaluator_request.UpdateEvaluatorRequest = {
            "evaluator_id": evaluator_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if evaluator_config is not None:
            input_["evaluator_config"] = evaluator_config
        if level is not None:
            input_["level"] = level
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_evaluator_response.DeleteEvaluatorResponse":
        """<p> Deletes a custom evaluator. Builtin evaluators cannot be deleted. The evaluator must not be referenced by any active online evaluation configurations. </p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to delete. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_evaluator_request.DeleteEvaluatorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_evaluator_response.DeleteEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_evaluator

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_evaluator.delete_evaluator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_evaluator_request.DeleteEvaluatorRequest = {
            "evaluator_id": evaluator_id
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
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_evaluators_response.ListEvaluatorsResponse":
        """<p> Lists all available evaluators, including both builtin evaluators provided by the service and custom evaluators created by the user. </p>

        Args:
            next_token: <p> The pagination token from a previous request to retrieve the next page of results. </p>
            max_results: <p> The maximum number of evaluators to return in a single response. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_evaluators_request.ListEvaluatorsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_evaluators_response.ListEvaluatorsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_evaluators

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_evaluators.list_evaluators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_evaluators_request.ListEvaluatorsRequest = {}
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


class AsyncEvaluator:
    def __init__(self, service: AsyncBedrockAgentCoreControlClient) -> None:
        self._service = service

    async def create(
        self,
        evaluator_name: "capo_bedrock_agentcore_control.types.custom_evaluator_name.CustomEvaluatorName",
        evaluator_config: "capo_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig",
        level: "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_evaluator_response.CreateEvaluatorResponse":
        """<p> Creates a custom evaluator for agent quality assessment. Custom evaluators can use either LLM-as-a-Judge configurations with user-defined prompts, rating scales, and model settings, or code-based configurations with customer-managed Lambda functions to evaluate agent performance at tool call, trace, or session levels. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            evaluator_name: <p> The name of the evaluator. Must be unique within your account. </p>
            description: <p> The description of the evaluator that explains its purpose and evaluation criteria. </p>
            evaluator_config: <p> The configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function. </p>
            level: <p> The evaluation level that determines the scope of evaluation. Valid values are <code>TOOL_CALL</code> for individual tool invocations, <code>TRACE</code> for single request-response interactions, or <code>SESSION</code> for entire conversation sessions. </p>
            kms_key_arn: <p> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data, including instructions and rating scale. If you don't specify a KMS key, the evaluator data is encrypted with an Amazon Web Services owned key. Only symmetric encryption KMS keys are supported. For more information, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html">Encryption at rest for AgentCore Evaluations</a>. </p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Evaluator. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.create_evaluator_request.CreateEvaluatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.create_evaluator_response.CreateEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_evaluator

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_evaluator.async_create_evaluator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_evaluator_request.CreateEvaluatorRequest = {
            "evaluator_name": evaluator_name,
            "evaluator_config": evaluator_config,
            "level": level,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        included_data: Optional[
            "capo_bedrock_agentcore_control.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_evaluator_response.GetEvaluatorResponse":
        """<p> Retrieves detailed information about an evaluator, including its configuration, status, and metadata. Works with both built-in and custom evaluators. </p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to retrieve. Can be a built-in evaluator ID (e.g., Builtin.Helpfulness) or a custom evaluator ID. </p>
            included_data: <p> Controls which data is returned in the response. <code>ALL_DATA</code> (default) returns the full evaluator including decrypted instructions and rating scale. For evaluators encrypted with a customer managed KMS key, this requires <code>kms:Decrypt</code> permission on the key. <code>METADATA_ONLY</code> returns evaluator metadata and model configuration without instructions or rating scale, and does not require any KMS permissions. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.get_evaluator_request.GetEvaluatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.get_evaluator_response.GetEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_evaluator

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_evaluator.async_get_evaluator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_evaluator_request.GetEvaluatorRequest = {
            "evaluator_id": evaluator_id
        }
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
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
        ] = None,
        evaluator_config: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig"
        ] = None,
        level: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_evaluator_response.UpdateEvaluatorResponse":
        """<p> Updates a custom evaluator's configuration, description, or evaluation level. Built-in evaluators cannot be updated. The evaluator must not be locked for modification. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            evaluator_id: <p> The unique identifier of the evaluator to update. </p>
            description: <p> The updated description of the evaluator. </p>
            evaluator_config: <p> The updated configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function. </p>
            level: <p> The updated evaluation level (<code>TOOL_CALL</code>, <code>TRACE</code>, or <code>SESSION</code>) that determines the scope of evaluation. </p>
            kms_key_arn: <p> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data. Specify a new key ARN to rotate the encryption key, or specify a key ARN to add encryption to an evaluator that was previously created without one. When you rotate to a new key, the service decrypts the existing data with the old key and re-encrypts it with the new key. Only symmetric encryption KMS keys are supported. For more information, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html">Encryption at rest for AgentCore Evaluations</a>. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.update_evaluator_request.UpdateEvaluatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.update_evaluator_response.UpdateEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_evaluator

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_evaluator.async_update_evaluator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_evaluator_request.UpdateEvaluatorRequest = {
            "evaluator_id": evaluator_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if evaluator_config is not None:
            input_["evaluator_config"] = evaluator_config
        if level is not None:
            input_["level"] = level
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_evaluator_response.DeleteEvaluatorResponse":
        """<p> Deletes a custom evaluator. Builtin evaluators cannot be deleted. The evaluator must not be referenced by any active online evaluation configurations. </p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to delete. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.delete_evaluator_request.DeleteEvaluatorRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.delete_evaluator_response.DeleteEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_evaluator

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_evaluator.async_delete_evaluator(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_evaluator_request.DeleteEvaluatorRequest = {
            "evaluator_id": evaluator_id
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
        config_overrides: Optional[AsyncBedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_evaluators_response.ListEvaluatorsResponse":
        """<p> Lists all available evaluators, including both builtin evaluators provided by the service and custom evaluators created by the user. </p>

        Args:
            next_token: <p> The pagination token from a previous request to retrieve the next page of results. </p>
            max_results: <p> The maximum number of evaluators to return in a single response. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore_control.types.list_evaluators_request.ListEvaluatorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore_control.types.list_evaluators_response.ListEvaluatorsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_evaluators

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_evaluators.async_list_evaluators(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_evaluators_request.ListEvaluatorsRequest = {}
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
