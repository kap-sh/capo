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
    import capo_bedrock_agentcore.types.agent_application_name
    import capo_bedrock_agentcore.types.agent_insight_archive_status
    import capo_bedrock_agentcore.types.agent_insight_id
    import capo_bedrock_agentcore.types.agent_insight_summary
    import capo_bedrock_agentcore.types.batch_evaluation_description
    import capo_bedrock_agentcore.types.batch_evaluation_id
    import capo_bedrock_agentcore.types.batch_evaluation_name
    import capo_bedrock_agentcore.types.batch_evaluation_summary
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.create_ab_test_request
    import capo_bedrock_agentcore.types.create_ab_test_response
    import capo_bedrock_agentcore.types.data_source_config
    import capo_bedrock_agentcore.types.dataset_execution_config
    import capo_bedrock_agentcore.types.dataset_generation_description
    import capo_bedrock_agentcore.types.dataset_generation_id
    import capo_bedrock_agentcore.types.dataset_generation_name
    import capo_bedrock_agentcore.types.dataset_generation_summary
    import capo_bedrock_agentcore.types.dataset_id
    import capo_bedrock_agentcore.types.delete_ab_test_request
    import capo_bedrock_agentcore.types.delete_ab_test_response
    import capo_bedrock_agentcore.types.delete_batch_evaluation_request
    import capo_bedrock_agentcore.types.delete_batch_evaluation_response
    import capo_bedrock_agentcore.types.delete_dataset_generation_request
    import capo_bedrock_agentcore.types.delete_dataset_generation_response
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
    import capo_bedrock_agentcore.types.generation_source
    import capo_bedrock_agentcore.types.get_ab_test_request
    import capo_bedrock_agentcore.types.get_ab_test_response
    import capo_bedrock_agentcore.types.get_agent_insight_request
    import capo_bedrock_agentcore.types.get_agent_insight_response
    import capo_bedrock_agentcore.types.get_batch_evaluation_request
    import capo_bedrock_agentcore.types.get_batch_evaluation_response
    import capo_bedrock_agentcore.types.get_dataset_generation_request
    import capo_bedrock_agentcore.types.get_dataset_generation_response
    import capo_bedrock_agentcore.types.get_recommendation_request
    import capo_bedrock_agentcore.types.get_recommendation_response
    import capo_bedrock_agentcore.types.insight_list
    import capo_bedrock_agentcore.types.kms_key_arn
    import capo_bedrock_agentcore.types.list_ab_tests_request
    import capo_bedrock_agentcore.types.list_ab_tests_response
    import capo_bedrock_agentcore.types.list_agent_insights_request
    import capo_bedrock_agentcore.types.list_agent_insights_response
    import capo_bedrock_agentcore.types.list_batch_evaluations_request
    import capo_bedrock_agentcore.types.list_batch_evaluations_response
    import capo_bedrock_agentcore.types.list_dataset_generations_request
    import capo_bedrock_agentcore.types.list_dataset_generations_response
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
    import capo_bedrock_agentcore.types.scenario_type
    import capo_bedrock_agentcore.types.start_batch_evaluation_request
    import capo_bedrock_agentcore.types.start_batch_evaluation_response
    import capo_bedrock_agentcore.types.start_dataset_generation_request
    import capo_bedrock_agentcore.types.start_dataset_generation_response
    import capo_bedrock_agentcore.types.start_recommendation_request
    import capo_bedrock_agentcore.types.start_recommendation_response
    import capo_bedrock_agentcore.types.stop_batch_evaluation_request
    import capo_bedrock_agentcore.types.stop_batch_evaluation_response
    import capo_bedrock_agentcore.types.tags_map
    import capo_bedrock_agentcore.types.update_ab_test_request
    import capo_bedrock_agentcore.types.update_ab_test_response
    import capo_bedrock_agentcore.types.update_agent_insight_request
    import capo_bedrock_agentcore.types.update_agent_insight_response
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

    def delete_dataset_generation(
        self,
        dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId",
        generation_id: "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_dataset_generation_response.DeleteDatasetGenerationResponse":
        """<p>Deletes the record of a dataset generation. The examples the generation added stay in the dataset's draft. To remove them, find them with the <code>generationIds</code> filter of <code>ListDatasetExamples</code>, then call <code>DeleteDatasetExamples</code>.</p>

        Args:
            dataset_id: <p>The unique identifier of the dataset.</p>
            generation_id: <p>The unique identifier of the dataset generation.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_dataset_generation_request.DeleteDatasetGenerationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_dataset_generation_response.DeleteDatasetGenerationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_dataset_generation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_dataset_generation.delete_dataset_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDatasetGeneration")
        )
        input_: capo_bedrock_agentcore.types.delete_dataset_generation_request.DeleteDatasetGenerationRequest = {
            "dataset_id": dataset_id,
            "generation_id": generation_id,
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

    def get_agent_insight(
        self,
        application_name: "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName",
        agent_insight_id: "capo_bedrock_agentcore.types.agent_insight_id.AgentInsightId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_agent_insight_response.GetAgentInsightResponse":
        """<p>Amazon Bedrock AgentCore Agent Insights identifies patterns detected across your agent sessions. Use Agent Insights to identify recurring issues and prioritize fixes.</p> <p>Retrieves detailed information about an Amazon Bedrock AgentCore Agent Insight, including its archive status, affected sessions, and, when applicable, the batch evaluation that produced it.</p>

        Args:
            application_name: <p>The application that the Agent Insight belongs to.</p>
            agent_insight_id: <p>The unique identifier of the Agent Insight to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_agent_insight_request.GetAgentInsightRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_agent_insight_response.GetAgentInsightResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_insight

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_insight.get_agent_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_agent_insight_response.GetAgentInsightResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_agent_insight_response

            return capo_bedrock_agentcore.types.get_agent_insight_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentInsight", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_agent_insight_request.GetAgentInsightRequest = {
            "application_name": application_name,
            "agent_insight_id": agent_insight_id,
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

    def get_dataset_generation(
        self,
        dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId",
        generation_id: "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_dataset_generation_response.GetDatasetGenerationResponse":
        """<p>Gets a dataset generation, including its status, the request it was started with, its progress counts, its redaction summary and its errors. Call this operation to track a generation that you started with <code>StartDatasetGeneration</code>.</p>

        Args:
            dataset_id: <p>The unique identifier of the dataset.</p>
            generation_id: <p>The unique identifier of the dataset generation.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore.types.get_dataset_generation_request.GetDatasetGenerationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_dataset_generation_response.GetDatasetGenerationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_dataset_generation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_dataset_generation.get_dataset_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDatasetGeneration")
        )
        input_: capo_bedrock_agentcore.types.get_dataset_generation_request.GetDatasetGenerationRequest = {
            "dataset_id": dataset_id,
            "generation_id": generation_id,
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

    def list_agent_insights(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        application_name: Optional[
            "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName"
        ] = None,
        batch_evaluation_id: Optional[
            "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
        ] = None,
        archive_status: Optional[
            "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_agent_insights_response.ListAgentInsightsResponse":
        """<p>Lists Amazon Bedrock AgentCore Agent Insight summaries in your account and Region. Use this operation to review patterns across sessions before you investigate or archive an insight. The response paginates the results. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            application_name: <p>Filters the results to Agent Insights for an application.</p>
            batch_evaluation_id: <p>Filters the results to Agent Insights produced by a batch evaluation.</p>
            archive_status: <p>Filters the results by archive status.</p>
            max_results: <p>The maximum number of Agent Insight summaries to return in one response. If you don't specify a value, the operation returns up to 50 summaries.</p>
            next_token: <p>A token to specify where to start paginating the results. This token is returned in a previous response.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_agent_insights_request.ListAgentInsightsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_agent_insights_response.ListAgentInsightsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_agent_insights

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_agent_insights.list_agent_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.list_agent_insights_response.ListAgentInsightsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.list_agent_insights_response

            return capo_bedrock_agentcore.types.list_agent_insights_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentInsights", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.list_agent_insights_request.ListAgentInsightsRequest = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if batch_evaluation_id is not None:
            input_["batch_evaluation_id"] = batch_evaluation_id
        if archive_status is not None:
            input_["archive_status"] = archive_status
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

    def list_dataset_generations(
        self,
        dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.list_dataset_generations_response.ListDatasetGenerationsResponse":
        """<p>Lists the generations for a dataset. AgentCore keeps a generation until you delete it with <code>DeleteDatasetGeneration</code> or delete the dataset. To get a generation's counts and the request it was started with, call <code>GetDatasetGeneration</code>.</p>

        Args:
            dataset_id: <p>The unique identifier of the dataset.</p>
            max_results: <p>The maximum number of results to return in the response. The default is 20. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore.types.list_dataset_generations_request.ListDatasetGenerationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_dataset_generations_response.ListDatasetGenerationsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_dataset_generations

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_dataset_generations.list_dataset_generations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDatasetGenerations")
        )
        input_: capo_bedrock_agentcore.types.list_dataset_generations_request.ListDatasetGenerationsRequest = {
            "dataset_id": dataset_id
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
        dataset_execution_config: Optional[
            "capo_bedrock_agentcore.types.dataset_execution_config.DatasetExecutionConfig"
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
            dataset_execution_config: <p>The configuration for running the scenarios in a dataset against an agent before evaluating the resulting sessions. When you specify this field, the batch evaluation runs each scenario in the dataset against the agent. It then evaluates the sessions that the agent produces. You must also specify <code>evaluators</code> and a <code>dataSourceConfig</code> that uses <code>cloudWatchLogs</code>. Configure <code>cloudWatchLogs</code> with the service name and log groups that the agent uses for its traces. You can't specify <code>insights</code> or an <code>onlineEvaluationConfigSource</code> data source with this field.</p>

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
        if dataset_execution_config is not None:
            input_["dataset_execution_config"] = dataset_execution_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_dataset_generation(
        self,
        dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId",
        name: "capo_bedrock_agentcore.types.dataset_generation_name.DatasetGenerationName",
        source: "capo_bedrock_agentcore.types.generation_source.GenerationSource",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.dataset_generation_description.DatasetGenerationDescription"
        ] = None,
        scenario_type: Optional[
            "capo_bedrock_agentcore.types.scenario_type.ScenarioType"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_dataset_generation_response.StartDatasetGenerationResponse":
        """<p>Starts a dataset generation, which creates examples for an existing dataset from your agent's traces. The dataset must be <code>ACTIVE</code>. Each generation produces one scenario type, set by <code>scenarioType</code>. When the generation finishes, AgentCore adds the examples to the dataset's draft. Examples that duplicate each other, or that duplicate examples already in the draft, are left out.</p> <p>A dataset can have only one generation in progress at a time. While it runs, requests that change the dataset's draft or publish a version are rejected with a <code>ConflictException</code>.</p> <p>AgentCore reads the traces with your credentials, so you need read access to the trace log groups, and to the dataset's KMS key if the dataset uses a customer managed key. The draft can hold at most 1,000 examples, including the examples this generation can add (<code>maxScenarios</code>).</p> <p>The operation returns immediately. To track progress, call <code>GetDatasetGeneration</code>.</p>

        Args:
            dataset_id: <p>The unique identifier of the dataset to add the generated examples to. The dataset must be <code>ACTIVE</code>.</p>
            name: <p>The name of the dataset generation. The generation ID starts with this name.</p>
            description: <p>A description of the dataset generation.</p>
            scenario_type: <p>The type of scenario to generate. If you don't specify a value, the generation produces <code>DYNAMIC</code> scenarios.</p>
            source: <p>Where the generation reads sessions from, and how it selects, samples, labels and redacts them.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore.types.start_dataset_generation_request.StartDatasetGenerationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_dataset_generation_response.StartDatasetGenerationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_dataset_generation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_dataset_generation.start_dataset_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartDatasetGeneration")
        )
        input_: capo_bedrock_agentcore.types.start_dataset_generation_request.StartDatasetGenerationRequest = {
            "dataset_id": dataset_id,
            "name": name,
            "source": source,
        }
        if description is not None:
            input_["description"] = description
        if scenario_type is not None:
            input_["scenario_type"] = scenario_type
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

    def update_agent_insight(
        self,
        application_name: "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName",
        agent_insight_id: "capo_bedrock_agentcore.types.agent_insight_id.AgentInsightId",
        archive_status: "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.update_agent_insight_response.UpdateAgentInsightResponse":
        """<p>Updates the archive status of an Amazon Bedrock AgentCore Agent Insight.</p>

        Args:
            application_name: <p>The application that the Agent Insight belongs to.</p>
            agent_insight_id: <p>The unique identifier of the Agent Insight to update.</p>
            archive_status: <p>The archive status to apply to the Agent Insight. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> - Marks the insight as active.</p> </li> <li> <p> <code>ARCHIVED</code> - Marks the insight as archived.</p> </li> </ul>

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
            req: "OperationRequest[capo_bedrock_agentcore.types.update_agent_insight_request.UpdateAgentInsightRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.update_agent_insight_response.UpdateAgentInsightResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_agent_insight

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_agent_insight.update_agent_insight(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAgentInsight")
        )
        input_: capo_bedrock_agentcore.types.update_agent_insight_request.UpdateAgentInsightRequest = {
            "application_name": application_name,
            "agent_insight_id": agent_insight_id,
            "archive_status": archive_status,
        }

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

    async def delete_dataset_generation(
        self,
        dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId",
        generation_id: "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_dataset_generation_response.DeleteDatasetGenerationResponse":
        """<p>Deletes the record of a dataset generation. The examples the generation added stay in the dataset's draft. To remove them, find them with the <code>generationIds</code> filter of <code>ListDatasetExamples</code>, then call <code>DeleteDatasetExamples</code>.</p>

        Args:
            dataset_id: <p>The unique identifier of the dataset.</p>
            generation_id: <p>The unique identifier of the dataset generation.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.delete_dataset_generation_request.DeleteDatasetGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.delete_dataset_generation_response.DeleteDatasetGenerationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_dataset_generation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_dataset_generation.async_delete_dataset_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteDatasetGeneration")
        )
        input_: capo_bedrock_agentcore.types.delete_dataset_generation_request.DeleteDatasetGenerationRequest = {
            "dataset_id": dataset_id,
            "generation_id": generation_id,
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

    async def get_agent_insight(
        self,
        application_name: "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName",
        agent_insight_id: "capo_bedrock_agentcore.types.agent_insight_id.AgentInsightId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_agent_insight_response.GetAgentInsightResponse":
        """<p>Amazon Bedrock AgentCore Agent Insights identifies patterns detected across your agent sessions. Use Agent Insights to identify recurring issues and prioritize fixes.</p> <p>Retrieves detailed information about an Amazon Bedrock AgentCore Agent Insight, including its archive status, affected sessions, and, when applicable, the batch evaluation that produced it.</p>

        Args:
            application_name: <p>The application that the Agent Insight belongs to.</p>
            agent_insight_id: <p>The unique identifier of the Agent Insight to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_agent_insight_request.GetAgentInsightRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_agent_insight_response.GetAgentInsightResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_insight

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_insight.async_get_agent_insight(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.get_agent_insight_response.GetAgentInsightResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.get_agent_insight_response

            return capo_bedrock_agentcore.types.get_agent_insight_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAgentInsight", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.get_agent_insight_request.GetAgentInsightRequest = {
            "application_name": application_name,
            "agent_insight_id": agent_insight_id,
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

    async def get_dataset_generation(
        self,
        dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId",
        generation_id: "capo_bedrock_agentcore.types.dataset_generation_id.DatasetGenerationId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_dataset_generation_response.GetDatasetGenerationResponse":
        """<p>Gets a dataset generation, including its status, the request it was started with, its progress counts, its redaction summary and its errors. Call this operation to track a generation that you started with <code>StartDatasetGeneration</code>.</p>

        Args:
            dataset_id: <p>The unique identifier of the dataset.</p>
            generation_id: <p>The unique identifier of the dataset generation.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_dataset_generation_request.GetDatasetGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_dataset_generation_response.GetDatasetGenerationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_dataset_generation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_dataset_generation.async_get_dataset_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDatasetGeneration")
        )
        input_: capo_bedrock_agentcore.types.get_dataset_generation_request.GetDatasetGenerationRequest = {
            "dataset_id": dataset_id,
            "generation_id": generation_id,
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

    async def list_agent_insights(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        application_name: Optional[
            "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName"
        ] = None,
        batch_evaluation_id: Optional[
            "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
        ] = None,
        archive_status: Optional[
            "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_agent_insights_response.ListAgentInsightsResponse":
        """<p>Lists Amazon Bedrock AgentCore Agent Insight summaries in your account and Region. Use this operation to review patterns across sessions before you investigate or archive an insight. The response paginates the results. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            application_name: <p>Filters the results to Agent Insights for an application.</p>
            batch_evaluation_id: <p>Filters the results to Agent Insights produced by a batch evaluation.</p>
            archive_status: <p>Filters the results by archive status.</p>
            max_results: <p>The maximum number of Agent Insight summaries to return in one response. If you don't specify a value, the operation returns up to 50 summaries.</p>
            next_token: <p>A token to specify where to start paginating the results. This token is returned in a previous response.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_agent_insights_request.ListAgentInsightsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_agent_insights_response.ListAgentInsightsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_agent_insights

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_agent_insights.async_list_agent_insights(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_bedrock_agentcore.types.list_agent_insights_response.ListAgentInsightsResponse",
        ) -> dict[str, Any]:
            import capo_bedrock_agentcore.types.list_agent_insights_response

            return capo_bedrock_agentcore.types.list_agent_insights_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListAgentInsights", redact_output=_redact_output),
        )
        input_: capo_bedrock_agentcore.types.list_agent_insights_request.ListAgentInsightsRequest = {}
        if application_name is not None:
            input_["application_name"] = application_name
        if batch_evaluation_id is not None:
            input_["batch_evaluation_id"] = batch_evaluation_id
        if archive_status is not None:
            input_["archive_status"] = archive_status
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

    async def list_dataset_generations(
        self,
        dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.list_dataset_generations_response.ListDatasetGenerationsResponse":
        """<p>Lists the generations for a dataset. AgentCore keeps a generation until you delete it with <code>DeleteDatasetGeneration</code> or delete the dataset. To get a generation's counts and the request it was started with, call <code>GetDatasetGeneration</code>.</p>

        Args:
            dataset_id: <p>The unique identifier of the dataset.</p>
            max_results: <p>The maximum number of results to return in the response. The default is 20. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_dataset_generations_request.ListDatasetGenerationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_dataset_generations_response.ListDatasetGenerationsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_dataset_generations

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_dataset_generations.async_list_dataset_generations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDatasetGenerations")
        )
        input_: capo_bedrock_agentcore.types.list_dataset_generations_request.ListDatasetGenerationsRequest = {
            "dataset_id": dataset_id
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
        dataset_execution_config: Optional[
            "capo_bedrock_agentcore.types.dataset_execution_config.DatasetExecutionConfig"
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
            dataset_execution_config: <p>The configuration for running the scenarios in a dataset against an agent before evaluating the resulting sessions. When you specify this field, the batch evaluation runs each scenario in the dataset against the agent. It then evaluates the sessions that the agent produces. You must also specify <code>evaluators</code> and a <code>dataSourceConfig</code> that uses <code>cloudWatchLogs</code>. Configure <code>cloudWatchLogs</code> with the service name and log groups that the agent uses for its traces. You can't specify <code>insights</code> or an <code>onlineEvaluationConfigSource</code> data source with this field.</p>

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
        if dataset_execution_config is not None:
            input_["dataset_execution_config"] = dataset_execution_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_dataset_generation(
        self,
        dataset_id: "capo_bedrock_agentcore.types.dataset_id.DatasetId",
        name: "capo_bedrock_agentcore.types.dataset_generation_name.DatasetGenerationName",
        source: "capo_bedrock_agentcore.types.generation_source.GenerationSource",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.dataset_generation_description.DatasetGenerationDescription"
        ] = None,
        scenario_type: Optional[
            "capo_bedrock_agentcore.types.scenario_type.ScenarioType"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_dataset_generation_response.StartDatasetGenerationResponse":
        """<p>Starts a dataset generation, which creates examples for an existing dataset from your agent's traces. The dataset must be <code>ACTIVE</code>. Each generation produces one scenario type, set by <code>scenarioType</code>. When the generation finishes, AgentCore adds the examples to the dataset's draft. Examples that duplicate each other, or that duplicate examples already in the draft, are left out.</p> <p>A dataset can have only one generation in progress at a time. While it runs, requests that change the dataset's draft or publish a version are rejected with a <code>ConflictException</code>.</p> <p>AgentCore reads the traces with your credentials, so you need read access to the trace log groups, and to the dataset's KMS key if the dataset uses a customer managed key. The draft can hold at most 1,000 examples, including the examples this generation can add (<code>maxScenarios</code>).</p> <p>The operation returns immediately. To track progress, call <code>GetDatasetGeneration</code>.</p>

        Args:
            dataset_id: <p>The unique identifier of the dataset to add the generated examples to. The dataset must be <code>ACTIVE</code>.</p>
            name: <p>The name of the dataset generation. The generation ID starts with this name.</p>
            description: <p>A description of the dataset generation.</p>
            scenario_type: <p>The type of scenario to generate. If you don't specify a value, the generation produces <code>DYNAMIC</code> scenarios.</p>
            source: <p>Where the generation reads sessions from, and how it selects, samples, labels and redacts them.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.start_dataset_generation_request.StartDatasetGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.start_dataset_generation_response.StartDatasetGenerationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_dataset_generation

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_dataset_generation.async_start_dataset_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartDatasetGeneration")
        )
        input_: capo_bedrock_agentcore.types.start_dataset_generation_request.StartDatasetGenerationRequest = {
            "dataset_id": dataset_id,
            "name": name,
            "source": source,
        }
        if description is not None:
            input_["description"] = description
        if scenario_type is not None:
            input_["scenario_type"] = scenario_type
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

    async def update_agent_insight(
        self,
        application_name: "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName",
        agent_insight_id: "capo_bedrock_agentcore.types.agent_insight_id.AgentInsightId",
        archive_status: "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.update_agent_insight_response.UpdateAgentInsightResponse":
        """<p>Updates the archive status of an Amazon Bedrock AgentCore Agent Insight.</p>

        Args:
            application_name: <p>The application that the Agent Insight belongs to.</p>
            agent_insight_id: <p>The unique identifier of the Agent Insight to update.</p>
            archive_status: <p>The archive status to apply to the Agent Insight. Valid values:</p> <ul> <li> <p> <code>ACTIVE</code> - Marks the insight as active.</p> </li> <li> <p> <code>ARCHIVED</code> - Marks the insight as archived.</p> </li> </ul>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.update_agent_insight_request.UpdateAgentInsightRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.update_agent_insight_response.UpdateAgentInsightResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_agent_insight

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_agent_insight.async_update_agent_insight(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAgentInsight")
        )
        input_: capo_bedrock_agentcore.types.update_agent_insight_request.UpdateAgentInsightRequest = {
            "application_name": application_name,
            "agent_insight_id": agent_insight_id,
            "archive_status": archive_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
