from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_bedrock_agent_runtime._auth._signers
import capo_bedrock_agent_runtime._auth._sigv4
from capo_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.create_session_request
    import capo_bedrock_agent_runtime.types.create_session_response
    import capo_bedrock_agent_runtime.types.delete_session_request
    import capo_bedrock_agent_runtime.types.delete_session_response
    import capo_bedrock_agent_runtime.types.end_session_request
    import capo_bedrock_agent_runtime.types.end_session_response
    import capo_bedrock_agent_runtime.types.get_session_request
    import capo_bedrock_agent_runtime.types.get_session_response
    import capo_bedrock_agent_runtime.types.kms_key_arn
    import capo_bedrock_agent_runtime.types.list_sessions_request
    import capo_bedrock_agent_runtime.types.list_sessions_response
    import capo_bedrock_agent_runtime.types.max_results
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.session_identifier
    import capo_bedrock_agent_runtime.types.session_metadata_map
    import capo_bedrock_agent_runtime.types.session_summary
    import capo_bedrock_agent_runtime.types.tags_map
    import capo_bedrock_agent_runtime.types.update_session_request
    import capo_bedrock_agent_runtime.types.update_session_response
    from capo_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from capo_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class SessionResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        session_metadata: Optional[
            "capo_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
        ] = None,
        encryption_key_arn: Optional[
            "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agent_runtime.types.tags_map.TagsMap"] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.create_session_response.CreateSessionResponse"
    ):
        """<p>Creates a session to temporarily store conversations for generative AI (GenAI) applications built with open-source frameworks such as LangGraph and LlamaIndex. Sessions enable you to save the state of conversations at checkpoints, with the added security and infrastructure of Amazon Web Services. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p> <p>By default, Amazon Bedrock uses Amazon Web Services-managed keys for session encryption, including session metadata, or you can use your own KMS key. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html">Amazon Bedrock session encryption</a>.</p> <note> <p> You use a session to store state and conversation history for generative AI applications built with open-source frameworks. For Amazon Bedrock Agents, the service automatically manages conversation context and associates them with the agent-specific sessionId you specify in the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> API operation. </p> </note> <p>Related APIs:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListSessions.html">ListSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html">GetSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html">EndSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteSession.html">DeleteSession</a> </p> </li> </ul>

        Args:
            session_metadata: <p>A map of key-value pairs containing attributes to be persisted across the session. For example, the user's ID, their language preference, and the type of device they are using.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to use to encrypt the session data. The user or role creating the session must have permission to use the key. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html">Amazon Bedrock session encryption</a>. </p>
            tags: <p>Specify the key-value pairs for the tags that you want to attach to the session.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.create_session_request.CreateSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.create_session_response.CreateSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.create_session

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.create_session.create_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.create_session_request.CreateSessionRequest = {}
        if session_metadata is not None:
            input_["session_metadata"] = session_metadata
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
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
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_session_response.GetSessionResponse":
        """<p>Retrieves details about a specific session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>A unique identifier for the session to retrieve. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.get_session_request.GetSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.get_session_response.GetSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_session

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_session_request.GetSessionRequest = {
            "session_identifier": session_identifier
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
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        session_metadata: Optional[
            "capo_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
        ] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.update_session_response.UpdateSessionResponse"
    ):
        """<p>Updates the metadata or encryption settings of a session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_metadata: <p>A map of key-value pairs containing attributes to be persisted across the session. For example the user's ID, their language preference, and the type of device they are using.</p>
            session_identifier: <p>The unique identifier of the session to modify. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.update_session_request.UpdateSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.update_session_response.UpdateSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.update_session

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.update_session.update_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.update_session_request.UpdateSessionRequest = {
            "session_identifier": session_identifier
        }
        if session_metadata is not None:
            input_["session_metadata"] = session_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.delete_session_response.DeleteSessionResponse"
    ):
        """<p>Deletes a session that you ended. You can't delete a session with an <code>ACTIVE</code> status. To delete an active session, you must first end it with the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html">EndSession</a> API operation. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>The unique identifier for the session to be deleted. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.delete_session_request.DeleteSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.delete_session_response.DeleteSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_session

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_session.delete_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.delete_session_request.DeleteSessionRequest = {
            "session_identifier": session_identifier
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
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists all sessions in your Amazon Web Services account. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results. </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_sessions

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.list_sessions_request.ListSessionsRequest = {}
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

    def end_session(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.end_session_response.EndSessionResponse":
        """<p>Ends the session. After you end a session, you can still access its content but you can’t add to it. To delete the session and it's content, you use the DeleteSession API operation. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>The unique identifier for the session to end. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agent_runtime.types.end_session_request.EndSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agent_runtime.types.end_session_response.EndSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.end_session

            output, http_response = (
                capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.end_session.end_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.end_session_request.EndSessionRequest = {
            "session_identifier": session_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncSessionResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_metadata: Optional[
            "capo_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
        ] = None,
        encryption_key_arn: Optional[
            "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agent_runtime.types.tags_map.TagsMap"] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.create_session_response.CreateSessionResponse"
    ):
        """<p>Creates a session to temporarily store conversations for generative AI (GenAI) applications built with open-source frameworks such as LangGraph and LlamaIndex. Sessions enable you to save the state of conversations at checkpoints, with the added security and infrastructure of Amazon Web Services. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p> <p>By default, Amazon Bedrock uses Amazon Web Services-managed keys for session encryption, including session metadata, or you can use your own KMS key. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html">Amazon Bedrock session encryption</a>.</p> <note> <p> You use a session to store state and conversation history for generative AI applications built with open-source frameworks. For Amazon Bedrock Agents, the service automatically manages conversation context and associates them with the agent-specific sessionId you specify in the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> API operation. </p> </note> <p>Related APIs:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListSessions.html">ListSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html">GetSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html">EndSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteSession.html">DeleteSession</a> </p> </li> </ul>

        Args:
            session_metadata: <p>A map of key-value pairs containing attributes to be persisted across the session. For example, the user's ID, their language preference, and the type of device they are using.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to use to encrypt the session data. The user or role creating the session must have permission to use the key. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html">Amazon Bedrock session encryption</a>. </p>
            tags: <p>Specify the key-value pairs for the tags that you want to attach to the session.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.create_session_request.CreateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.create_session_response.CreateSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.create_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.create_session.async_create_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.create_session_request.CreateSessionRequest = {}
        if session_metadata is not None:
            input_["session_metadata"] = session_metadata
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
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
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_session_response.GetSessionResponse":
        """<p>Retrieves details about a specific session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>A unique identifier for the session to retrieve. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_session_response.GetSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_session_request.GetSessionRequest = {
            "session_identifier": session_identifier
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
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_metadata: Optional[
            "capo_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
        ] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.update_session_response.UpdateSessionResponse"
    ):
        """<p>Updates the metadata or encryption settings of a session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_metadata: <p>A map of key-value pairs containing attributes to be persisted across the session. For example the user's ID, their language preference, and the type of device they are using.</p>
            session_identifier: <p>The unique identifier of the session to modify. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.update_session_request.UpdateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.update_session_response.UpdateSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.update_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.update_session.async_update_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.update_session_request.UpdateSessionRequest = {
            "session_identifier": session_identifier
        }
        if session_metadata is not None:
            input_["session_metadata"] = session_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.delete_session_response.DeleteSessionResponse"
    ):
        """<p>Deletes a session that you ended. You can't delete a session with an <code>ACTIVE</code> status. To delete an active session, you must first end it with the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html">EndSession</a> API operation. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>The unique identifier for the session to be deleted. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.delete_session_request.DeleteSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.delete_session_response.DeleteSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_session.async_delete_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.delete_session_request.DeleteSessionRequest = {
            "session_identifier": session_identifier
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
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists all sessions in your Amazon Web Services account. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results. </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_sessions

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.list_sessions_request.ListSessionsRequest = {}
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

    async def end_session(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.end_session_response.EndSessionResponse":
        """<p>Ends the session. After you end a session, you can still access its content but you can’t add to it. To delete the session and it's content, you use the DeleteSession API operation. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>The unique identifier for the session to end. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.end_session_request.EndSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.end_session_response.EndSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.end_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.end_session.async_end_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.end_session_request.EndSessionRequest = {
            "session_identifier": session_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
