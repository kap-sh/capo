from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
from capo_bedrock_agentcore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ab_test_description
    import capo_bedrock_agentcore.types.ab_test_evaluation_config
    import capo_bedrock_agentcore.types.ab_test_execution_status
    import capo_bedrock_agentcore.types.ab_test_id
    import capo_bedrock_agentcore.types.ab_test_name
    import capo_bedrock_agentcore.types.ab_test_summary
    import capo_bedrock_agentcore.types.batch_evaluation_description
    import capo_bedrock_agentcore.types.batch_evaluation_id
    import capo_bedrock_agentcore.types.batch_evaluation_name
    import capo_bedrock_agentcore.types.batch_evaluation_summary
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.create_ab_test_request
    import capo_bedrock_agentcore.types.create_ab_test_response
    import capo_bedrock_agentcore.types.data_source_config
    import capo_bedrock_agentcore.types.delete_ab_test_request
    import capo_bedrock_agentcore.types.delete_ab_test_response
    import capo_bedrock_agentcore.types.delete_batch_evaluation_request
    import capo_bedrock_agentcore.types.delete_batch_evaluation_response
    import capo_bedrock_agentcore.types.delete_recommendation_request
    import capo_bedrock_agentcore.types.delete_recommendation_response
    import capo_bedrock_agentcore.types.evaluate_request
    import capo_bedrock_agentcore.types.evaluate_response
    import capo_bedrock_agentcore.types.evaluation_input
    import capo_bedrock_agentcore.types.evaluation_metadata
    import capo_bedrock_agentcore.types.evaluation_reference_inputs
    import capo_bedrock_agentcore.types.evaluation_target
    import capo_bedrock_agentcore.types.evaluator_id
    import capo_bedrock_agentcore.types.evaluator_list
    import capo_bedrock_agentcore.types.gateway_arn
    import capo_bedrock_agentcore.types.gateway_filter
    import capo_bedrock_agentcore.types.get_ab_test_request
    import capo_bedrock_agentcore.types.get_ab_test_response
    import capo_bedrock_agentcore.types.get_batch_evaluation_request
    import capo_bedrock_agentcore.types.get_batch_evaluation_response
    import capo_bedrock_agentcore.types.get_recommendation_request
    import capo_bedrock_agentcore.types.get_recommendation_response
    import capo_bedrock_agentcore.types.insight_list
    import capo_bedrock_agentcore.types.kms_key_arn
    import capo_bedrock_agentcore.types.list_ab_tests_request
    import capo_bedrock_agentcore.types.list_ab_tests_response
    import capo_bedrock_agentcore.types.list_batch_evaluations_request
    import capo_bedrock_agentcore.types.list_batch_evaluations_response
    import capo_bedrock_agentcore.types.list_recommendations_request
    import capo_bedrock_agentcore.types.list_recommendations_response
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.output_config
    import capo_bedrock_agentcore.types.recommendation_config
    import capo_bedrock_agentcore.types.recommendation_description
    import capo_bedrock_agentcore.types.recommendation_id
    import capo_bedrock_agentcore.types.recommendation_name
    import capo_bedrock_agentcore.types.recommendation_status
    import capo_bedrock_agentcore.types.recommendation_summary
    import capo_bedrock_agentcore.types.recommendation_type
    import capo_bedrock_agentcore.types.role_arn
    import capo_bedrock_agentcore.types.start_batch_evaluation_request
    import capo_bedrock_agentcore.types.start_batch_evaluation_response
    import capo_bedrock_agentcore.types.start_recommendation_request
    import capo_bedrock_agentcore.types.start_recommendation_response
    import capo_bedrock_agentcore.types.stop_batch_evaluation_request
    import capo_bedrock_agentcore.types.stop_batch_evaluation_response
    import capo_bedrock_agentcore.types.tags_map
    import capo_bedrock_agentcore.types.update_ab_test_request
    import capo_bedrock_agentcore.types.update_ab_test_response
    import capo_bedrock_agentcore.types.variant_list
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class EvaluationResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def create_ab_test(
        self,
        name: "capo_bedrock_agentcore.types.ab_test_name.ABTestName",
        gateway_arn: "capo_bedrock_agentcore.types.gateway_arn.GatewayArn",
        variants: "capo_bedrock_agentcore.types.variant_list.VariantList",
        evaluation_config: "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig",
        role_arn: "capo_bedrock_agentcore.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
        ] = None,
        gateway_filter: Optional[
            "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
        ] = None,
        enable_on_create: Optional[bool] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse":
        """<p>Creates an A/B test for comparing agent configurations. A/B tests split traffic between a control variant and a treatment variant through a gateway, then evaluate performance using online evaluation configurations to determine which variant performs better.</p>

        Args:
            name: <p>The name of the A/B test. Must be unique within your account.</p>
            description: <p>The description of the A/B test.</p>
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.</p>
            variants: <p>The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.</p>
            gateway_filter: <p>Optional filter to restrict which gateway target paths are included in the A/B test.</p>
            evaluation_config: <p>The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.</p>
            role_arn: <p>The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.</p>
            enable_on_create: <p>Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>A map of tag keys and values to associate with the A/B test.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test.create_ab_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateABTest")
        )
        input_: capo_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest = {
            "name": name,
            "gateway_arn": gateway_arn,
            "variants": variants,
            "evaluation_config": evaluation_config,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if gateway_filter is not None:
            input_["gateway_filter"] = gateway_filter
        if enable_on_create is not None:
            input_["enable_on_create"] = enable_on_create
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

    def delete_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse":
        """<p>Deletes an A/B test and its associated gateway rules.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test.delete_ab_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteABTest")
        )
        input_: capo_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest = {
            "ab_test_id": ab_test_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse":
        """<p>Deletes a batch evaluation and its associated results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation.delete_batch_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBatchEvaluation")
        )
        input_: capo_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recommendation(
        self,
        recommendation_id: "capo_bedrock_agentcore.types.recommendation_id.RecommendationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse":
        """<p>Deletes a recommendation and its associated results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation.delete_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRecommendation")
        )
        input_: capo_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest = {
            "recommendation_id": recommendation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def evaluate(
        self,
        evaluator_id: "capo_bedrock_agentcore.types.evaluator_id.EvaluatorId",
        evaluation_input: "capo_bedrock_agentcore.types.evaluation_input.EvaluationInput",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        evaluation_target: Optional[
            "capo_bedrock_agentcore.types.evaluation_target.EvaluationTarget"
        ] = None,
        evaluation_reference_inputs: Optional[
            "capo_bedrock_agentcore.types.evaluation_reference_inputs.EvaluationReferenceInputs"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.evaluate_response.EvaluateResponse":
        """<p> Performs on-demand evaluation of agent traces using a specified evaluator. This synchronous API accepts traces in OpenTelemetry format and returns immediate scoring results with detailed explanations.</p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., <code>Builtin.Helpfulness</code>, <code>Builtin.Correctness</code>) or a custom evaluator Id created through the control plane API. </p>
            evaluation_input: <p> The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation. </p>
            evaluation_target: <p> The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions. </p>
            evaluation_reference_inputs: <p> Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID. </p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.duplicate_id_exception.DuplicateIdException: <p> An exception thrown when attempting to create a resource with an identifier that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.evaluate_request.EvaluateRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.evaluate_response.EvaluateResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate.evaluate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.evaluate_request.EvaluateRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.evaluate_request

            return capo_bedrock_agentcore.types.evaluate_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.evaluate_response.EvaluateResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.evaluate_response

            return capo_bedrock_agentcore.types.evaluate_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "Evaluate", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore.types.evaluate_request.EvaluateRequest = {
            "evaluator_id": evaluator_id,
            "evaluation_input": evaluation_input,
        }
        if evaluation_target is not None:
            input_["evaluation_target"] = evaluation_target
        if evaluation_reference_inputs is not None:
            input_["evaluation_reference_inputs"] = evaluation_reference_inputs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse":
        """<p>Retrieves detailed information about an A/B test, including its configuration, status, and statistical results.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test.get_ab_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetABTest")
        )
        input_: capo_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest = {
            "ab_test_id": ab_test_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse":
        """<p>Retrieves detailed information about a batch evaluation, including its status, configuration, results, and any error details.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation.get_batch_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_batch_evaluation_response

            return capo_bedrock_agentcore.types.get_batch_evaluation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetBatchEvaluation", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommendation(
        self,
        recommendation_id: "capo_bedrock_agentcore.types.recommendation_id.RecommendationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Retrieves detailed information about a recommendation, including its configuration, status, and results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation.get_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_recommendation_response

            return capo_bedrock_agentcore.types.get_recommendation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetRecommendation", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest = {
            "recommendation_id": recommendation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_ab_tests(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse":
        """<p>Lists all A/B tests in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests.list_ab_tests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListABTests")
        )
        input_: capo_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest = {}
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

    def list_batch_evaluations(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse":
        """<p>Lists all batch evaluations in the account, providing summary information about each evaluation's status and configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations.list_batch_evaluations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListBatchEvaluations")
        )
        input_: capo_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest = {}
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

    def list_recommendations(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status_filter: Optional[
            "capo_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Lists all recommendations in the account, with optional filtering by status.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            status_filter: <p>Optional filter to return only recommendations with the specified status.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations.list_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRecommendations")
        )
        input_: capo_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_batch_evaluation(
        self,
        batch_evaluation_name: "capo_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName",
        data_source_config: "capo_bedrock_agentcore.types.data_source_config.DataSourceConfig",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        evaluators: Optional[
            "capo_bedrock_agentcore.types.evaluator_list.EvaluatorList"
        ] = None,
        insights: Optional[
            "capo_bedrock_agentcore.types.insight_list.InsightList"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        evaluation_metadata: Optional[
            "capo_bedrock_agentcore.types.evaluation_metadata.EvaluationMetadata"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
        ] = None,
        output_config: Optional[
            "capo_bedrock_agentcore.types.output_config.OutputConfig"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse":
        """<p>Starts a batch evaluation job that evaluates agent performance across multiple sessions. Batch evaluations pull agent traces from CloudWatch Logs or an existing online evaluation configuration and run specified evaluators and insights against them.</p>

        Args:
            batch_evaluation_name: <p>The name of the batch evaluation. Must be unique within your account.</p>
            evaluators: <p>The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.</p>
            insights: <p>The list of insight analyses to run against sessions during the batch evaluation. Maximum of 10 insights.</p>
            data_source_config: <p>The data source configuration that specifies where to pull agent session traces from for evaluation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            evaluation_metadata: <p>Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.</p>
            tags: <p>A map of tag keys and values to associate with the batch evaluation.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt evaluation data. If provided, customer data is encrypted at rest with the specified key.</p>
            description: <p>The description of the batch evaluation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation.start_batch_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartBatchEvaluation")
        )
        input_: capo_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest = {
            "batch_evaluation_name": batch_evaluation_name,
            "data_source_config": data_source_config,
        }
        if evaluators is not None:
            input_["evaluators"] = evaluators
        if insights is not None:
            input_["insights"] = insights
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if evaluation_metadata is not None:
            input_["evaluation_metadata"] = evaluation_metadata
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if description is not None:
            input_["description"] = description
        if output_config is not None:
            input_["output_config"] = output_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_recommendation(
        self,
        name: "capo_bedrock_agentcore.types.recommendation_name.RecommendationName",
        type: "capo_bedrock_agentcore.types.recommendation_type.RecommendationType",
        recommendation_config: "capo_bedrock_agentcore.types.recommendation_config.RecommendationConfig",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.recommendation_description.RecommendationDescription"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse":
        """<p>Starts a recommendation job that analyzes agent traces and generates optimization suggestions for system prompts or tool descriptions to improve agent performance.</p>

        Args:
            name: <p>The name of the recommendation. Must be unique within your account.</p>
            description: <p>The description of the recommendation.</p>
            type: <p>The type of recommendation to generate. Valid values are <code>SYSTEM_PROMPT_RECOMMENDATION</code> for system prompt optimization or <code>TOOL_DESCRIPTION_RECOMMENDATION</code> for tool description optimization.</p>
            recommendation_config: <p>The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt recommendation data. If provided, customer data is encrypted at rest with the specified key.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>A map of tag keys and values to associate with the recommendation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation.start_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.start_recommendation_request

            return capo_bedrock_agentcore.types.start_recommendation_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.start_recommendation_response

            return capo_bedrock_agentcore.types.start_recommendation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartRecommendation",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest = {
            "name": name,
            "type": type,
            "recommendation_config": recommendation_config,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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

    def stop_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse":
        """<p>Stops a running batch evaluation. Sessions that have already been evaluated retain their results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to stop.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation.stop_batch_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopBatchEvaluation")
        )
        input_: capo_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        name: Optional["capo_bedrock_agentcore.types.ab_test_name.ABTestName"] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
        ] = None,
        variants: Optional[
            "capo_bedrock_agentcore.types.variant_list.VariantList"
        ] = None,
        gateway_filter: Optional[
            "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
        ] = None,
        evaluation_config: Optional[
            "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"
        ] = None,
        role_arn: Optional["capo_bedrock_agentcore.types.role_arn.RoleArn"] = None,
        execution_status: Optional[
            "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse":
        """<p>Updates an A/B test's configuration, including variants, traffic allocation, evaluation settings, or execution status.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            name: <p>The updated name of the A/B test.</p>
            description: <p>The updated description of the A/B test.</p>
            variants: <p>The updated list of variants.</p>
            gateway_filter: <p>The updated gateway filter.</p>
            evaluation_config: <p>The updated evaluation configuration.</p>
            role_arn: <p>The updated IAM role ARN.</p>
            execution_status: <p>The updated execution status to enable or disable the A/B test.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test.update_ab_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateABTest")
        )
        input_: capo_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest = {
            "ab_test_id": ab_test_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if variants is not None:
            input_["variants"] = variants
        if gateway_filter is not None:
            input_["gateway_filter"] = gateway_filter
        if evaluation_config is not None:
            input_["evaluation_config"] = evaluation_config
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if execution_status is not None:
            input_["execution_status"] = execution_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEvaluationResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def create_ab_test(
        self,
        name: "capo_bedrock_agentcore.types.ab_test_name.ABTestName",
        gateway_arn: "capo_bedrock_agentcore.types.gateway_arn.GatewayArn",
        variants: "capo_bedrock_agentcore.types.variant_list.VariantList",
        evaluation_config: "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig",
        role_arn: "capo_bedrock_agentcore.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
        ] = None,
        gateway_filter: Optional[
            "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
        ] = None,
        enable_on_create: Optional[bool] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse":
        """<p>Creates an A/B test for comparing agent configurations. A/B tests split traffic between a control variant and a treatment variant through a gateway, then evaluate performance using online evaluation configurations to determine which variant performs better.</p>

        Args:
            name: <p>The name of the A/B test. Must be unique within your account.</p>
            description: <p>The description of the A/B test.</p>
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.</p>
            variants: <p>The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.</p>
            gateway_filter: <p>Optional filter to restrict which gateway target paths are included in the A/B test.</p>
            evaluation_config: <p>The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.</p>
            role_arn: <p>The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.</p>
            enable_on_create: <p>Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>A map of tag keys and values to associate with the A/B test.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test.async_create_ab_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateABTest")
        )
        input_: capo_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest = {
            "name": name,
            "gateway_arn": gateway_arn,
            "variants": variants,
            "evaluation_config": evaluation_config,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if gateway_filter is not None:
            input_["gateway_filter"] = gateway_filter
        if enable_on_create is not None:
            input_["enable_on_create"] = enable_on_create
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

    async def delete_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse":
        """<p>Deletes an A/B test and its associated gateway rules.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test.async_delete_ab_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteABTest")
        )
        input_: capo_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest = {
            "ab_test_id": ab_test_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse":
        """<p>Deletes a batch evaluation and its associated results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation.async_delete_batch_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBatchEvaluation")
        )
        input_: capo_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_recommendation(
        self,
        recommendation_id: "capo_bedrock_agentcore.types.recommendation_id.RecommendationId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse":
        """<p>Deletes a recommendation and its associated results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation.async_delete_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRecommendation")
        )
        input_: capo_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest = {
            "recommendation_id": recommendation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def evaluate(
        self,
        evaluator_id: "capo_bedrock_agentcore.types.evaluator_id.EvaluatorId",
        evaluation_input: "capo_bedrock_agentcore.types.evaluation_input.EvaluationInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        evaluation_target: Optional[
            "capo_bedrock_agentcore.types.evaluation_target.EvaluationTarget"
        ] = None,
        evaluation_reference_inputs: Optional[
            "capo_bedrock_agentcore.types.evaluation_reference_inputs.EvaluationReferenceInputs"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.evaluate_response.EvaluateResponse":
        """<p> Performs on-demand evaluation of agent traces using a specified evaluator. This synchronous API accepts traces in OpenTelemetry format and returns immediate scoring results with detailed explanations.</p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., <code>Builtin.Helpfulness</code>, <code>Builtin.Correctness</code>) or a custom evaluator Id created through the control plane API. </p>
            evaluation_input: <p> The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation. </p>
            evaluation_target: <p> The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions. </p>
            evaluation_reference_inputs: <p> Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID. </p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.duplicate_id_exception.DuplicateIdException: <p> An exception thrown when attempting to create a resource with an identifier that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.evaluate_request.EvaluateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.evaluate_response.EvaluateResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate.async_evaluate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.evaluate_request.EvaluateRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.evaluate_request

            return capo_bedrock_agentcore.types.evaluate_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.evaluate_response.EvaluateResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.evaluate_response

            return capo_bedrock_agentcore.types.evaluate_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "Evaluate", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_bedrock_agentcore.types.evaluate_request.EvaluateRequest = {
            "evaluator_id": evaluator_id,
            "evaluation_input": evaluation_input,
        }
        if evaluation_target is not None:
            input_["evaluation_target"] = evaluation_target
        if evaluation_reference_inputs is not None:
            input_["evaluation_reference_inputs"] = evaluation_reference_inputs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse":
        """<p>Retrieves detailed information about an A/B test, including its configuration, status, and statistical results.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test.async_get_ab_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetABTest")
        )
        input_: capo_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest = {
            "ab_test_id": ab_test_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse":
        """<p>Retrieves detailed information about a batch evaluation, including its status, configuration, results, and any error details.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation.async_get_batch_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_batch_evaluation_response

            return capo_bedrock_agentcore.types.get_batch_evaluation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetBatchEvaluation", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_recommendation(
        self,
        recommendation_id: "capo_bedrock_agentcore.types.recommendation_id.RecommendationId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Retrieves detailed information about a recommendation, including its configuration, status, and results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation.async_get_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_recommendation_response

            return capo_bedrock_agentcore.types.get_recommendation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetRecommendation", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest = {
            "recommendation_id": recommendation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ab_tests(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse":
        """<p>Lists all A/B tests in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests.async_list_ab_tests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListABTests")
        )
        input_: capo_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest = {}
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

    async def list_batch_evaluations(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse":
        """<p>Lists all batch evaluations in the account, providing summary information about each evaluation's status and configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations.async_list_batch_evaluations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListBatchEvaluations")
        )
        input_: capo_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest = {}
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

    async def list_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status_filter: Optional[
            "capo_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Lists all recommendations in the account, with optional filtering by status.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            status_filter: <p>Optional filter to return only recommendations with the specified status.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations.async_list_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRecommendations")
        )
        input_: capo_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_batch_evaluation(
        self,
        batch_evaluation_name: "capo_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName",
        data_source_config: "capo_bedrock_agentcore.types.data_source_config.DataSourceConfig",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        evaluators: Optional[
            "capo_bedrock_agentcore.types.evaluator_list.EvaluatorList"
        ] = None,
        insights: Optional[
            "capo_bedrock_agentcore.types.insight_list.InsightList"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        evaluation_metadata: Optional[
            "capo_bedrock_agentcore.types.evaluation_metadata.EvaluationMetadata"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
        ] = None,
        output_config: Optional[
            "capo_bedrock_agentcore.types.output_config.OutputConfig"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse":
        """<p>Starts a batch evaluation job that evaluates agent performance across multiple sessions. Batch evaluations pull agent traces from CloudWatch Logs or an existing online evaluation configuration and run specified evaluators and insights against them.</p>

        Args:
            batch_evaluation_name: <p>The name of the batch evaluation. Must be unique within your account.</p>
            evaluators: <p>The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.</p>
            insights: <p>The list of insight analyses to run against sessions during the batch evaluation. Maximum of 10 insights.</p>
            data_source_config: <p>The data source configuration that specifies where to pull agent session traces from for evaluation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            evaluation_metadata: <p>Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.</p>
            tags: <p>A map of tag keys and values to associate with the batch evaluation.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt evaluation data. If provided, customer data is encrypted at rest with the specified key.</p>
            description: <p>The description of the batch evaluation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation.async_start_batch_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartBatchEvaluation")
        )
        input_: capo_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest = {
            "batch_evaluation_name": batch_evaluation_name,
            "data_source_config": data_source_config,
        }
        if evaluators is not None:
            input_["evaluators"] = evaluators
        if insights is not None:
            input_["insights"] = insights
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if evaluation_metadata is not None:
            input_["evaluation_metadata"] = evaluation_metadata
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if description is not None:
            input_["description"] = description
        if output_config is not None:
            input_["output_config"] = output_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_recommendation(
        self,
        name: "capo_bedrock_agentcore.types.recommendation_name.RecommendationName",
        type: "capo_bedrock_agentcore.types.recommendation_type.RecommendationType",
        recommendation_config: "capo_bedrock_agentcore.types.recommendation_config.RecommendationConfig",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.recommendation_description.RecommendationDescription"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse":
        """<p>Starts a recommendation job that analyzes agent traces and generates optimization suggestions for system prompts or tool descriptions to improve agent performance.</p>

        Args:
            name: <p>The name of the recommendation. Must be unique within your account.</p>
            description: <p>The description of the recommendation.</p>
            type: <p>The type of recommendation to generate. Valid values are <code>SYSTEM_PROMPT_RECOMMENDATION</code> for system prompt optimization or <code>TOOL_DESCRIPTION_RECOMMENDATION</code> for tool description optimization.</p>
            recommendation_config: <p>The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt recommendation data. If provided, customer data is encrypted at rest with the specified key.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>A map of tag keys and values to associate with the recommendation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation.async_start_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.start_recommendation_request

            return capo_bedrock_agentcore.types.start_recommendation_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.start_recommendation_response

            return capo_bedrock_agentcore.types.start_recommendation_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartRecommendation",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest = {
            "name": name,
            "type": type,
            "recommendation_config": recommendation_config,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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

    async def stop_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse":
        """<p>Stops a running batch evaluation. Sessions that have already been evaluated retain their results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to stop.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation.async_stop_batch_evaluation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopBatchEvaluation")
        )
        input_: capo_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        name: Optional["capo_bedrock_agentcore.types.ab_test_name.ABTestName"] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
        ] = None,
        variants: Optional[
            "capo_bedrock_agentcore.types.variant_list.VariantList"
        ] = None,
        gateway_filter: Optional[
            "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
        ] = None,
        evaluation_config: Optional[
            "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"
        ] = None,
        role_arn: Optional["capo_bedrock_agentcore.types.role_arn.RoleArn"] = None,
        execution_status: Optional[
            "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse":
        """<p>Updates an A/B test's configuration, including variants, traffic allocation, evaluation settings, or execution status.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            name: <p>The updated name of the A/B test.</p>
            description: <p>The updated description of the A/B test.</p>
            variants: <p>The updated list of variants.</p>
            gateway_filter: <p>The updated gateway filter.</p>
            evaluation_config: <p>The updated evaluation configuration.</p>
            role_arn: <p>The updated IAM role ARN.</p>
            execution_status: <p>The updated execution status to enable or disable the A/B test.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test.async_update_ab_test(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateABTest")
        )
        input_: capo_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest = {
            "ab_test_id": ab_test_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if variants is not None:
            input_["variants"] = variants
        if gateway_filter is not None:
            input_["gateway_filter"] = gateway_filter
        if evaluation_config is not None:
            input_["evaluation_config"] = evaluation_config
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if execution_status is not None:
            input_["execution_status"] = execution_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
