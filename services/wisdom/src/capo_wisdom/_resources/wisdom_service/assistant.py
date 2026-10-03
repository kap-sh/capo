from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_wisdom._auth._signers
import capo_wisdom._auth._sigv4
from capo_wisdom._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_wisdom.types.assistant_summary
    import capo_wisdom.types.assistant_type
    import capo_wisdom.types.client_token
    import capo_wisdom.types.create_assistant_request
    import capo_wisdom.types.create_assistant_response
    import capo_wisdom.types.delete_assistant_request
    import capo_wisdom.types.delete_assistant_response
    import capo_wisdom.types.description
    import capo_wisdom.types.get_assistant_request
    import capo_wisdom.types.get_assistant_response
    import capo_wisdom.types.get_recommendations_request
    import capo_wisdom.types.get_recommendations_response
    import capo_wisdom.types.list_assistants_request
    import capo_wisdom.types.list_assistants_response
    import capo_wisdom.types.max_results
    import capo_wisdom.types.name
    import capo_wisdom.types.next_token
    import capo_wisdom.types.notify_recommendations_received_request
    import capo_wisdom.types.notify_recommendations_received_response
    import capo_wisdom.types.query_assistant_request
    import capo_wisdom.types.query_assistant_response
    import capo_wisdom.types.query_text
    import capo_wisdom.types.recommendation_id_list
    import capo_wisdom.types.result_data
    import capo_wisdom.types.search_expression
    import capo_wisdom.types.search_sessions_request
    import capo_wisdom.types.search_sessions_response
    import capo_wisdom.types.server_side_encryption_configuration
    import capo_wisdom.types.session_summary
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid_or_arn
    import capo_wisdom.types.wait_time_seconds
    from capo_wisdom._services.async_wisdom import (
        AsyncWisdomClient,
        AsyncWisdomClientConfig,
    )
    from capo_wisdom._services.wisdom import WisdomClient, WisdomClientConfig


class Assistant:
    def __init__(self, service: WisdomClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_wisdom.types.name.Name",
        type: "capo_wisdom.types.assistant_type.AssistantType",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        client_token: Optional["capo_wisdom.types.client_token.ClientToken"] = None,
        description: Optional["capo_wisdom.types.description.Description"] = None,
        tags: Optional["capo_wisdom.types.tags.Tags"] = None,
        server_side_encryption_configuration: Optional[
            "capo_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
    ) -> "capo_wisdom.types.create_assistant_response.CreateAssistantResponse":
        """<p>Creates an Amazon Connect Wisdom assistant.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the assistant.</p>
            type: <p>The type of assistant.</p>
            description: <p>The description of the assistant.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html">Enable Amazon Connect Wisdom for your instance</a>.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wisdom.types.create_assistant_request.CreateAssistantRequest]",
        ) -> OperationResponse[
            "capo_wisdom.types.create_assistant_response.CreateAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.create_assistant

            output, http_response = (
                capo_wisdom._operations.wisdom_service.create_assistant.create_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.create_assistant_request.CreateAssistantRequest = {
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
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_assistant_response.GetAssistantResponse":
        """<p>Retrieves information about an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wisdom.types.get_assistant_request.GetAssistantRequest]",
        ) -> OperationResponse[
            "capo_wisdom.types.get_assistant_response.GetAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_assistant

            output, http_response = (
                capo_wisdom._operations.wisdom_service.get_assistant.get_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.get_assistant_request.GetAssistantRequest = {
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
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
    ) -> "capo_wisdom.types.delete_assistant_response.DeleteAssistantResponse":
        """<p>Deletes an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wisdom.types.delete_assistant_request.DeleteAssistantRequest]",
        ) -> OperationResponse[
            "capo_wisdom.types.delete_assistant_response.DeleteAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.delete_assistant

            output, http_response = (
                capo_wisdom._operations.wisdom_service.delete_assistant.delete_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.delete_assistant_request.DeleteAssistantRequest = {
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
        config_overrides: Optional[WisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.list_assistants_response.ListAssistantsResponse":
        """<p>Lists information about assistants.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wisdom.types.list_assistants_request.ListAssistantsRequest]",
        ) -> OperationResponse[
            "capo_wisdom.types.list_assistants_response.ListAssistantsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_assistants

            output, http_response = (
                capo_wisdom._operations.wisdom_service.list_assistants.list_assistants(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.list_assistants_request.ListAssistantsRequest = {}
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
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
        wait_time_seconds: Optional[
            "capo_wisdom.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "capo_wisdom.types.get_recommendations_response.GetRecommendationsResponse":
        """<p>Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_NotifyRecommendationsReceived.html">NotifyRecommendationsReceived</a>. This API supports long-polling behavior with the <code>waitTimeSeconds</code> parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QueryAssistant.html">QueryAssistant</a>.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            wait_time_seconds: <p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wisdom.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_wisdom.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_recommendations

            output, http_response = (
                capo_wisdom._operations.wisdom_service.get_recommendations.get_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.get_recommendations_request.GetRecommendationsRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def notify_recommendations_received(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        recommendation_ids: "capo_wisdom.types.recommendation_id_list.RecommendationIdList",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
    ) -> "capo_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse":
        """<p>Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a> and a <code>waitTimeSeconds</code> input for long-polling behavior and avoiding duplicate recommendations.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            recommendation_ids: <p>The identifiers of the recommendations.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest]",
        ) -> OperationResponse[
            "capo_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.notify_recommendations_received

            output, http_response = (
                capo_wisdom._operations.wisdom_service.notify_recommendations_received.notify_recommendations_received(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest = {
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

    def query_assistant(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        query_text: "capo_wisdom.types.query_text.QueryText",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.query_assistant_response.QueryAssistantResponse":
        """<p>Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a>. </p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_text: <p>The text to search for.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wisdom.types.query_assistant_request.QueryAssistantRequest]",
        ) -> OperationResponse[
            "capo_wisdom.types.query_assistant_response.QueryAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.query_assistant

            output, http_response = (
                capo_wisdom._operations.wisdom_service.query_assistant.query_assistant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.query_assistant_request.QueryAssistantRequest = {
            "assistant_id": assistant_id,
            "query_text": query_text,
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

    def search_sessions(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_wisdom.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[WisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.search_sessions_response.SearchSessionsResponse":
        """<p>Searches for sessions.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_wisdom.types.search_sessions_request.SearchSessionsRequest]",
        ) -> OperationResponse[
            "capo_wisdom.types.search_sessions_response.SearchSessionsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.search_sessions

            output, http_response = (
                capo_wisdom._operations.wisdom_service.search_sessions.search_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.search_sessions_request.SearchSessionsRequest = {
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


class AsyncAssistant:
    def __init__(self, service: AsyncWisdomClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_wisdom.types.name.Name",
        type: "capo_wisdom.types.assistant_type.AssistantType",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        client_token: Optional["capo_wisdom.types.client_token.ClientToken"] = None,
        description: Optional["capo_wisdom.types.description.Description"] = None,
        tags: Optional["capo_wisdom.types.tags.Tags"] = None,
        server_side_encryption_configuration: Optional[
            "capo_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
    ) -> "capo_wisdom.types.create_assistant_response.CreateAssistantResponse":
        """<p>Creates an Amazon Connect Wisdom assistant.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the assistant.</p>
            type: <p>The type of assistant.</p>
            description: <p>The description of the assistant.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html">Enable Amazon Connect Wisdom for your instance</a>.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.create_assistant_request.CreateAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.create_assistant_response.CreateAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.create_assistant

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.create_assistant.async_create_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.create_assistant_request.CreateAssistantRequest = {
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
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_assistant_response.GetAssistantResponse":
        """<p>Retrieves information about an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_assistant_request.GetAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_assistant_response.GetAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_assistant

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_assistant.async_get_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.get_assistant_request.GetAssistantRequest = {
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
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.delete_assistant_response.DeleteAssistantResponse":
        """<p>Deletes an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.delete_assistant_request.DeleteAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.delete_assistant_response.DeleteAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.delete_assistant

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.delete_assistant.async_delete_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.delete_assistant_request.DeleteAssistantRequest = {
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
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.list_assistants_response.ListAssistantsResponse":
        """<p>Lists information about assistants.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.list_assistants_request.ListAssistantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.list_assistants_response.ListAssistantsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_assistants

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.list_assistants.async_list_assistants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.list_assistants_request.ListAssistantsRequest = {}
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
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
        wait_time_seconds: Optional[
            "capo_wisdom.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "capo_wisdom.types.get_recommendations_response.GetRecommendationsResponse":
        """<p>Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_NotifyRecommendationsReceived.html">NotifyRecommendationsReceived</a>. This API supports long-polling behavior with the <code>waitTimeSeconds</code> parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QueryAssistant.html">QueryAssistant</a>.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            wait_time_seconds: <p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_recommendations

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_recommendations.async_get_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.get_recommendations_request.GetRecommendationsRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def notify_recommendations_received(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        recommendation_ids: "capo_wisdom.types.recommendation_id_list.RecommendationIdList",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse":
        """<p>Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a> and a <code>waitTimeSeconds</code> input for long-polling behavior and avoiding duplicate recommendations.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            recommendation_ids: <p>The identifiers of the recommendations.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.notify_recommendations_received

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.notify_recommendations_received.async_notify_recommendations_received(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest = {
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

    async def query_assistant(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        query_text: "capo_wisdom.types.query_text.QueryText",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.query_assistant_response.QueryAssistantResponse":
        """<p>Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a>. </p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_text: <p>The text to search for.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.query_assistant_request.QueryAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.query_assistant_response.QueryAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.query_assistant

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.query_assistant.async_query_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.query_assistant_request.QueryAssistantRequest = {
            "assistant_id": assistant_id,
            "query_text": query_text,
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

    async def search_sessions(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_wisdom.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.search_sessions_response.SearchSessionsResponse":
        """<p>Searches for sessions.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.search_sessions_request.SearchSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.search_sessions_response.SearchSessionsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.search_sessions

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.search_sessions.async_search_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_wisdom.types.search_sessions_request.SearchSessionsRequest = {
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
