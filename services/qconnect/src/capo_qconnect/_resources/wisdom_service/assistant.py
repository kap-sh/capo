from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_qconnect._auth._signers
import capo_qconnect._auth._sigv4
from capo_qconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_configuration_data
    import capo_qconnect.types.ai_agent_type
    import capo_qconnect.types.ai_prompt_type
    import capo_qconnect.types.assistant_summary
    import capo_qconnect.types.assistant_type
    import capo_qconnect.types.client_token
    import capo_qconnect.types.content_feedback_data
    import capo_qconnect.types.create_assistant_request
    import capo_qconnect.types.create_assistant_response
    import capo_qconnect.types.delete_assistant_request
    import capo_qconnect.types.delete_assistant_response
    import capo_qconnect.types.description
    import capo_qconnect.types.get_assistant_request
    import capo_qconnect.types.get_assistant_response
    import capo_qconnect.types.get_recommendations_request
    import capo_qconnect.types.get_recommendations_response
    import capo_qconnect.types.knowledge_base_search_type
    import capo_qconnect.types.list_assistants_request
    import capo_qconnect.types.list_assistants_response
    import capo_qconnect.types.list_models_request
    import capo_qconnect.types.list_models_response
    import capo_qconnect.types.max_results
    import capo_qconnect.types.model_lifecycle
    import capo_qconnect.types.model_summary
    import capo_qconnect.types.name
    import capo_qconnect.types.next_token
    import capo_qconnect.types.non_empty_sensitive_string
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.notify_recommendations_received_request
    import capo_qconnect.types.notify_recommendations_received_response
    import capo_qconnect.types.put_feedback_request
    import capo_qconnect.types.put_feedback_response
    import capo_qconnect.types.query_assistant_request
    import capo_qconnect.types.query_assistant_response
    import capo_qconnect.types.query_condition_expression
    import capo_qconnect.types.query_input_data
    import capo_qconnect.types.query_text
    import capo_qconnect.types.recommendation_id_list
    import capo_qconnect.types.recommendation_type
    import capo_qconnect.types.remove_assistant_ai_agent_request
    import capo_qconnect.types.remove_assistant_ai_agent_response
    import capo_qconnect.types.result_data
    import capo_qconnect.types.retrieval_configuration
    import capo_qconnect.types.retrieve_request
    import capo_qconnect.types.retrieve_response
    import capo_qconnect.types.search_expression
    import capo_qconnect.types.search_sessions_request
    import capo_qconnect.types.search_sessions_response
    import capo_qconnect.types.server_side_encryption_configuration
    import capo_qconnect.types.session_summary
    import capo_qconnect.types.tags
    import capo_qconnect.types.target_type
    import capo_qconnect.types.update_assistant_ai_agent_request
    import capo_qconnect.types.update_assistant_ai_agent_response
    import capo_qconnect.types.uuid
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.wait_time_seconds
    from capo_qconnect._services.async_q_connect import (
        AsyncQConnectClient,
        AsyncQConnectClientConfig,
    )
    from capo_qconnect._services.q_connect import QConnectClient, QConnectClientConfig


class Assistant:
    def __init__(self, service: QConnectClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_qconnect.types.name.Name",
        type: "capo_qconnect.types.assistant_type.AssistantType",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
        server_side_encryption_configuration: Optional[
            "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.create_assistant_response.CreateAssistantResponse":
        """<p>Creates an Amazon Q in Connect assistant.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the assistant.</p>
            type: <p>The type of assistant.</p>
            description: <p>The description of the assistant.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect. To use Amazon Q in Connect with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.create_assistant_request.CreateAssistantRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.create_assistant_response.CreateAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_assistant

            output, http_response = (
                capo_qconnect._operations.wisdom_service.create_assistant.create_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.create_assistant_request.CreateAssistantRequest = {
            "name": name,
            "type": type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_assistant_response.GetAssistantResponse":
        """<p>Retrieves information about an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.get_assistant_request.GetAssistantRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.get_assistant_response.GetAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_assistant

            output, http_response = (
                capo_qconnect._operations.wisdom_service.get_assistant.get_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.get_assistant_request.GetAssistantRequest = {
            "assistant_id": assistant_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_assistant_response.DeleteAssistantResponse":
        """<p>Deletes an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.delete_assistant_request.DeleteAssistantRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.delete_assistant_response.DeleteAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_assistant

            output, http_response = (
                capo_qconnect._operations.wisdom_service.delete_assistant.delete_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_assistant_request.DeleteAssistantRequest = {
            "assistant_id": assistant_id
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
        config_overrides: Optional[QConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_assistants_response.ListAssistantsResponse":
        """<p>Lists information about assistants.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.list_assistants_request.ListAssistantsRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.list_assistants_response.ListAssistantsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_assistants

            output, http_response = (
                capo_qconnect._operations.wisdom_service.list_assistants.list_assistants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.list_assistants_request.ListAssistantsRequest = {}
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

    def get_recommendations(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        wait_time_seconds: Optional[
            "capo_qconnect.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
        next_chunk_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        recommendation_type: Optional[
            "capo_qconnect.types.recommendation_type.RecommendationType"
        ] = None,
    ) -> "capo_qconnect.types.get_recommendations_response.GetRecommendationsResponse":
        """<important> <p>This API will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024, you will need to create a new Assistant in the Connect Customer console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.</p> </important> <p>Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_NotifyRecommendationsReceived.html">NotifyRecommendationsReceived</a>. This API supports long-polling behavior with the <code>waitTimeSeconds</code> parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_QueryAssistant.html">QueryAssistant</a>.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            wait_time_seconds: <p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>
            next_chunk_token: <p>The token for the next set of chunks. Use the value returned in the previous response in the next request to retrieve the next set of chunks.</p>
            recommendation_type: <p>The type of recommendation being requested.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_recommendations

            output, http_response = (
                capo_qconnect._operations.wisdom_service.get_recommendations.get_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.get_recommendations_request.GetRecommendationsRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds
        if next_chunk_token is not None:
            input_["next_chunk_token"] = next_chunk_token
        if recommendation_type is not None:
            input_["recommendation_type"] = recommendation_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_models(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        ai_prompt_type: Optional[
            "capo_qconnect.types.ai_prompt_type.AIPromptType"
        ] = None,
        model_lifecycle: Optional[
            "capo_qconnect.types.model_lifecycle.ModelLifecycle"
        ] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_models_response.ListModelsResponse":
        """<p>Lists the models available to an Amazon Q in Connect assistant in the assistant's Amazon Web Services Region. The available models are determined by the region of the specified assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. The assistant's region determines which models are available.</p>
            ai_prompt_type: <p>The type of the AI Prompt to filter models by. When specified, only models that support the given AI Prompt type are returned.</p>
            model_lifecycle: <p>The lifecycle status of models to filter by. When specified, only models with the given lifecycle status are returned.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.list_models_request.ListModelsRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.list_models_response.ListModelsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_models

            output, http_response = (
                capo_qconnect._operations.wisdom_service.list_models.list_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.list_models_request.ListModelsRequest = {
            "assistant_id": assistant_id
        }
        if ai_prompt_type is not None:
            input_["ai_prompt_type"] = ai_prompt_type
        if model_lifecycle is not None:
            input_["model_lifecycle"] = model_lifecycle
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

    def notify_recommendations_received(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        recommendation_ids: "capo_qconnect.types.recommendation_id_list.RecommendationIdList",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse":
        """<p>Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a> and a <code>waitTimeSeconds</code> input for long-polling behavior and avoiding duplicate recommendations.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            recommendation_ids: <p>The identifiers of the recommendations.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.notify_recommendations_received

            output, http_response = (
                capo_qconnect._operations.wisdom_service.notify_recommendations_received.notify_recommendations_received(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
            "recommendation_ids": recommendation_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_feedback(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        target_id: "capo_qconnect.types.uuid.Uuid",
        target_type: "capo_qconnect.types.target_type.TargetType",
        content_feedback: "capo_qconnect.types.content_feedback_data.ContentFeedbackData",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.put_feedback_response.PutFeedbackResponse":
        """<p>Provides feedback against the specified assistant for the specified target. This API only supports generative targets.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant.</p>
            target_id: <p>The identifier of the feedback target.</p>
            target_type: <p>The type of the feedback target.</p>
            content_feedback: <p>Information about the feedback provided.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.put_feedback_request.PutFeedbackRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.put_feedback_response.PutFeedbackResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.put_feedback

            output, http_response = (
                capo_qconnect._operations.wisdom_service.put_feedback.put_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.put_feedback_request.PutFeedbackRequest = {
            "assistant_id": assistant_id,
            "target_id": target_id,
            "target_type": target_type,
            "content_feedback": content_feedback,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def query_assistant(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        query_text: Optional["capo_qconnect.types.query_text.QueryText"] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        session_id: Optional["capo_qconnect.types.uuid_or_arn.UuidOrArn"] = None,
        query_condition: Optional[
            "capo_qconnect.types.query_condition_expression.QueryConditionExpression"
        ] = None,
        query_input_data: Optional[
            "capo_qconnect.types.query_input_data.QueryInputData"
        ] = None,
        override_knowledge_base_search_type: Optional[
            "capo_qconnect.types.knowledge_base_search_type.KnowledgeBaseSearchType"
        ] = None,
    ) -> "capo_qconnect.types.query_assistant_response.QueryAssistantResponse":
        """<important> <p>This API will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024, you will need to create a new Assistant in the Connect Customer console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.</p> </important> <p>Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a>. </p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_text: <p>The text to search for.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            session_id: <p>The identifier of the Amazon Q in Connect session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_condition: <p>Information about how to query content.</p>
            query_input_data: <p>Information about the query.</p>
            override_knowledge_base_search_type: <p>The search type to be used against the Knowledge Base for this request. The values can be <code>SEMANTIC</code> which uses vector embeddings or <code>HYBRID</code> which use vector embeddings and raw text.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.query_assistant_request.QueryAssistantRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.query_assistant_response.QueryAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.query_assistant

            output, http_response = (
                capo_qconnect._operations.wisdom_service.query_assistant.query_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.query_assistant_request.QueryAssistantRequest = {
            "assistant_id": assistant_id
        }
        if query_text is not None:
            input_["query_text"] = query_text
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if session_id is not None:
            input_["session_id"] = session_id
        if query_condition is not None:
            input_["query_condition"] = query_condition
        if query_input_data is not None:
            input_["query_input_data"] = query_input_data
        if override_knowledge_base_search_type is not None:
            input_["override_knowledge_base_search_type"] = (
                override_knowledge_base_search_type
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_assistant_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_type: "capo_qconnect.types.ai_agent_type.AIAgentType",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        orchestrator_use_case: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_qconnect.types.remove_assistant_ai_agent_response.RemoveAssistantAIAgentResponse":
        """<p>Removes the AI Agent that is set for use by default on an Amazon Q in Connect Assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_type: <p>The type of the AI Agent being removed for use by default from the Amazon Q in Connect Assistant.</p>
            orchestrator_use_case: <p>The orchestrator use case for the AI Agent being removed.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.remove_assistant_ai_agent_request.RemoveAssistantAIAgentRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.remove_assistant_ai_agent_response.RemoveAssistantAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.remove_assistant_ai_agent

            output, http_response = (
                capo_qconnect._operations.wisdom_service.remove_assistant_ai_agent.remove_assistant_ai_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.remove_assistant_ai_agent_request.RemoveAssistantAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_type": ai_agent_type,
        }
        if orchestrator_use_case is not None:
            input_["orchestrator_use_case"] = orchestrator_use_case

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def retrieve(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        retrieval_configuration: "capo_qconnect.types.retrieval_configuration.RetrievalConfiguration",
        retrieval_query: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
    ) -> "capo_qconnect.types.retrieve_response.RetrieveResponse":
        """<p>Retrieves content from knowledge sources based on a query.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant for content retrieval.</p>
            retrieval_configuration: <p>The configuration for the content retrieval operation.</p>
            retrieval_query: <p>The query for content retrieval.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.dependency_failed_exception.DependencyFailedException: <p>The request failed because it depends on another request that failed.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.retrieve_request.RetrieveRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.retrieve_response.RetrieveResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.retrieve

            output, http_response = (
                capo_qconnect._operations.wisdom_service.retrieve.retrieve(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.retrieve_request.RetrieveRequest = {
            "assistant_id": assistant_id,
            "retrieval_configuration": retrieval_configuration,
            "retrieval_query": retrieval_query,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_sessions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_sessions_response.SearchSessionsResponse":
        """<p>Searches for sessions.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.search_sessions_request.SearchSessionsRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.search_sessions_response.SearchSessionsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_sessions

            output, http_response = (
                capo_qconnect._operations.wisdom_service.search_sessions.search_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.search_sessions_request.SearchSessionsRequest = {
            "assistant_id": assistant_id,
            "search_expression": search_expression,
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

    def update_assistant_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_type: "capo_qconnect.types.ai_agent_type.AIAgentType",
        configuration: "capo_qconnect.types.ai_agent_configuration_data.AIAgentConfigurationData",
        *,
        config_overrides: Optional[QConnectClientConfig] = None,
        orchestrator_use_case: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_qconnect.types.update_assistant_ai_agent_response.UpdateAssistantAIAgentResponse":
        """<p>Updates the AI Agent that is set for use by default on an Amazon Q in Connect Assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_type: <p>The type of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.</p>
            configuration: <p>The configuration of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.</p>
            orchestrator_use_case: <p>The orchestrator use case for the AI Agent being added.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qconnect.types.update_assistant_ai_agent_request.UpdateAssistantAIAgentRequest]",
        ) -> OperationResponse[
            "capo_qconnect.types.update_assistant_ai_agent_response.UpdateAssistantAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_assistant_ai_agent

            output, http_response = (
                capo_qconnect._operations.wisdom_service.update_assistant_ai_agent.update_assistant_ai_agent(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.update_assistant_ai_agent_request.UpdateAssistantAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_type": ai_agent_type,
            "configuration": configuration,
        }
        if orchestrator_use_case is not None:
            input_["orchestrator_use_case"] = orchestrator_use_case

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAssistant:
    def __init__(self, service: AsyncQConnectClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_qconnect.types.name.Name",
        type: "capo_qconnect.types.assistant_type.AssistantType",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
        server_side_encryption_configuration: Optional[
            "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.create_assistant_response.CreateAssistantResponse":
        """<p>Creates an Amazon Q in Connect assistant.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the assistant.</p>
            type: <p>The type of assistant.</p>
            description: <p>The description of the assistant.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect. To use Amazon Q in Connect with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_assistant_request.CreateAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_assistant_response.CreateAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_assistant

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_assistant.async_create_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.create_assistant_request.CreateAssistantRequest = {
            "name": name,
            "type": type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_assistant_response.GetAssistantResponse":
        """<p>Retrieves information about an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_assistant_request.GetAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_assistant_response.GetAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_assistant

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_assistant.async_get_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.get_assistant_request.GetAssistantRequest = {
            "assistant_id": assistant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_assistant_response.DeleteAssistantResponse":
        """<p>Deletes an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_assistant_request.DeleteAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_assistant_response.DeleteAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_assistant

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_assistant.async_delete_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_assistant_request.DeleteAssistantRequest = {
            "assistant_id": assistant_id
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
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_assistants_response.ListAssistantsResponse":
        """<p>Lists information about assistants.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_assistants_request.ListAssistantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_assistants_response.ListAssistantsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_assistants

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_assistants.async_list_assistants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.list_assistants_request.ListAssistantsRequest = {}
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

    async def get_recommendations(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        wait_time_seconds: Optional[
            "capo_qconnect.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
        next_chunk_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        recommendation_type: Optional[
            "capo_qconnect.types.recommendation_type.RecommendationType"
        ] = None,
    ) -> "capo_qconnect.types.get_recommendations_response.GetRecommendationsResponse":
        """<important> <p>This API will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024, you will need to create a new Assistant in the Connect Customer console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.</p> </important> <p>Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_NotifyRecommendationsReceived.html">NotifyRecommendationsReceived</a>. This API supports long-polling behavior with the <code>waitTimeSeconds</code> parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_QueryAssistant.html">QueryAssistant</a>.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            wait_time_seconds: <p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>
            next_chunk_token: <p>The token for the next set of chunks. Use the value returned in the previous response in the next request to retrieve the next set of chunks.</p>
            recommendation_type: <p>The type of recommendation being requested.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_recommendations

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_recommendations.async_get_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.get_recommendations_request.GetRecommendationsRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds
        if next_chunk_token is not None:
            input_["next_chunk_token"] = next_chunk_token
        if recommendation_type is not None:
            input_["recommendation_type"] = recommendation_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_models(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        ai_prompt_type: Optional[
            "capo_qconnect.types.ai_prompt_type.AIPromptType"
        ] = None,
        model_lifecycle: Optional[
            "capo_qconnect.types.model_lifecycle.ModelLifecycle"
        ] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_models_response.ListModelsResponse":
        """<p>Lists the models available to an Amazon Q in Connect assistant in the assistant's Amazon Web Services Region. The available models are determined by the region of the specified assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. The assistant's region determines which models are available.</p>
            ai_prompt_type: <p>The type of the AI Prompt to filter models by. When specified, only models that support the given AI Prompt type are returned.</p>
            model_lifecycle: <p>The lifecycle status of models to filter by. When specified, only models with the given lifecycle status are returned.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_models_request.ListModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_models_response.ListModelsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_models

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_models.async_list_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.list_models_request.ListModelsRequest = {
            "assistant_id": assistant_id
        }
        if ai_prompt_type is not None:
            input_["ai_prompt_type"] = ai_prompt_type
        if model_lifecycle is not None:
            input_["model_lifecycle"] = model_lifecycle
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

    async def notify_recommendations_received(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        recommendation_ids: "capo_qconnect.types.recommendation_id_list.RecommendationIdList",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse":
        """<p>Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a> and a <code>waitTimeSeconds</code> input for long-polling behavior and avoiding duplicate recommendations.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            recommendation_ids: <p>The identifiers of the recommendations.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.notify_recommendations_received

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.notify_recommendations_received.async_notify_recommendations_received(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
            "recommendation_ids": recommendation_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_feedback(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        target_id: "capo_qconnect.types.uuid.Uuid",
        target_type: "capo_qconnect.types.target_type.TargetType",
        content_feedback: "capo_qconnect.types.content_feedback_data.ContentFeedbackData",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.put_feedback_response.PutFeedbackResponse":
        """<p>Provides feedback against the specified assistant for the specified target. This API only supports generative targets.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant.</p>
            target_id: <p>The identifier of the feedback target.</p>
            target_type: <p>The type of the feedback target.</p>
            content_feedback: <p>Information about the feedback provided.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.put_feedback_request.PutFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.put_feedback_response.PutFeedbackResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.put_feedback

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.put_feedback.async_put_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.put_feedback_request.PutFeedbackRequest = {
            "assistant_id": assistant_id,
            "target_id": target_id,
            "target_type": target_type,
            "content_feedback": content_feedback,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def query_assistant(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        query_text: Optional["capo_qconnect.types.query_text.QueryText"] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        session_id: Optional["capo_qconnect.types.uuid_or_arn.UuidOrArn"] = None,
        query_condition: Optional[
            "capo_qconnect.types.query_condition_expression.QueryConditionExpression"
        ] = None,
        query_input_data: Optional[
            "capo_qconnect.types.query_input_data.QueryInputData"
        ] = None,
        override_knowledge_base_search_type: Optional[
            "capo_qconnect.types.knowledge_base_search_type.KnowledgeBaseSearchType"
        ] = None,
    ) -> "capo_qconnect.types.query_assistant_response.QueryAssistantResponse":
        """<important> <p>This API will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024, you will need to create a new Assistant in the Connect Customer console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.</p> </important> <p>Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a>. </p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_text: <p>The text to search for.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            session_id: <p>The identifier of the Amazon Q in Connect session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_condition: <p>Information about how to query content.</p>
            query_input_data: <p>Information about the query.</p>
            override_knowledge_base_search_type: <p>The search type to be used against the Knowledge Base for this request. The values can be <code>SEMANTIC</code> which uses vector embeddings or <code>HYBRID</code> which use vector embeddings and raw text.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.query_assistant_request.QueryAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.query_assistant_response.QueryAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.query_assistant

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.query_assistant.async_query_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.query_assistant_request.QueryAssistantRequest = {
            "assistant_id": assistant_id
        }
        if query_text is not None:
            input_["query_text"] = query_text
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if session_id is not None:
            input_["session_id"] = session_id
        if query_condition is not None:
            input_["query_condition"] = query_condition
        if query_input_data is not None:
            input_["query_input_data"] = query_input_data
        if override_knowledge_base_search_type is not None:
            input_["override_knowledge_base_search_type"] = (
                override_knowledge_base_search_type
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_assistant_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_type: "capo_qconnect.types.ai_agent_type.AIAgentType",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        orchestrator_use_case: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_qconnect.types.remove_assistant_ai_agent_response.RemoveAssistantAIAgentResponse":
        """<p>Removes the AI Agent that is set for use by default on an Amazon Q in Connect Assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_type: <p>The type of the AI Agent being removed for use by default from the Amazon Q in Connect Assistant.</p>
            orchestrator_use_case: <p>The orchestrator use case for the AI Agent being removed.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.remove_assistant_ai_agent_request.RemoveAssistantAIAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.remove_assistant_ai_agent_response.RemoveAssistantAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.remove_assistant_ai_agent

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.remove_assistant_ai_agent.async_remove_assistant_ai_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.remove_assistant_ai_agent_request.RemoveAssistantAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_type": ai_agent_type,
        }
        if orchestrator_use_case is not None:
            input_["orchestrator_use_case"] = orchestrator_use_case

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retrieve(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        retrieval_configuration: "capo_qconnect.types.retrieval_configuration.RetrievalConfiguration",
        retrieval_query: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.retrieve_response.RetrieveResponse":
        """<p>Retrieves content from knowledge sources based on a query.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant for content retrieval.</p>
            retrieval_configuration: <p>The configuration for the content retrieval operation.</p>
            retrieval_query: <p>The query for content retrieval.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.dependency_failed_exception.DependencyFailedException: <p>The request failed because it depends on another request that failed.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.retrieve_request.RetrieveRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.retrieve_response.RetrieveResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.retrieve

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.retrieve.async_retrieve(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.retrieve_request.RetrieveRequest = {
            "assistant_id": assistant_id,
            "retrieval_configuration": retrieval_configuration,
            "retrieval_query": retrieval_query,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_sessions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_sessions_response.SearchSessionsResponse":
        """<p>Searches for sessions.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.search_sessions_request.SearchSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.search_sessions_response.SearchSessionsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_sessions

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.search_sessions.async_search_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.search_sessions_request.SearchSessionsRequest = {
            "assistant_id": assistant_id,
            "search_expression": search_expression,
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

    async def update_assistant_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_type: "capo_qconnect.types.ai_agent_type.AIAgentType",
        configuration: "capo_qconnect.types.ai_agent_configuration_data.AIAgentConfigurationData",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        orchestrator_use_case: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_qconnect.types.update_assistant_ai_agent_response.UpdateAssistantAIAgentResponse":
        """<p>Updates the AI Agent that is set for use by default on an Amazon Q in Connect Assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_type: <p>The type of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.</p>
            configuration: <p>The configuration of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.</p>
            orchestrator_use_case: <p>The orchestrator use case for the AI Agent being added.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_assistant_ai_agent_request.UpdateAssistantAIAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_assistant_ai_agent_response.UpdateAssistantAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_assistant_ai_agent

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_assistant_ai_agent.async_update_assistant_ai_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qconnect.types.update_assistant_ai_agent_request.UpdateAssistantAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_type": ai_agent_type,
            "configuration": configuration,
        }
        if orchestrator_use_case is not None:
            input_["orchestrator_use_case"] = orchestrator_use_case

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
