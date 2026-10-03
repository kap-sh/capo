from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
from capo_bedrock_agentcore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_profile_id
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.save_browser_session_profile_request
    import capo_bedrock_agentcore.types.save_browser_session_profile_response
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class BrowserProfileResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def save_browser_session_profile(
        self,
        profile_identifier: "capo_bedrock_agentcore.types.browser_profile_id.BrowserProfileId",
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse":
        """<p>Saves the current state of a browser session as a reusable profile in Amazon Bedrock AgentCore. A browser profile captures persistent browser data such as cookies and local storage from an active session, enabling you to reuse this data in future browser sessions.</p> <p>To save a browser session profile, you must specify the profile identifier, browser identifier, and session ID. The session must be active when saving the profile. Once saved, the profile can be used with the <code>StartBrowserSession</code> operation to initialize new sessions with the stored browser state.</p> <p>Browser profiles are useful for scenarios that require persistent authentication, maintaining user preferences across sessions, or continuing tasks that depend on previously stored browser data.</p> <p>The following operations are related to <code>SaveBrowserSessionProfile</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            profile_identifier: <p>The unique identifier for the browser profile. This identifier is used to reference the profile when starting new browser sessions. The identifier must follow the pattern of an alphanumeric name (up to 48 characters) followed by a hyphen and a 10-character alphanumeric suffix.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session from which to save the profile.</p>
            session_id: <p>The unique identifier of the browser session from which to save the profile. The session must be active when saving the profile.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

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
            req: "OperationRequest[capo_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile.save_browser_session_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest = {
            "profile_identifier": profile_identifier,
            "browser_identifier": browser_identifier,
            "session_id": session_id,
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
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


class AsyncBrowserProfileResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def save_browser_session_profile(
        self,
        profile_identifier: "capo_bedrock_agentcore.types.browser_profile_id.BrowserProfileId",
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse":
        """<p>Saves the current state of a browser session as a reusable profile in Amazon Bedrock AgentCore. A browser profile captures persistent browser data such as cookies and local storage from an active session, enabling you to reuse this data in future browser sessions.</p> <p>To save a browser session profile, you must specify the profile identifier, browser identifier, and session ID. The session must be active when saving the profile. Once saved, the profile can be used with the <code>StartBrowserSession</code> operation to initialize new sessions with the stored browser state.</p> <p>Browser profiles are useful for scenarios that require persistent authentication, maintaining user preferences across sessions, or continuing tasks that depend on previously stored browser data.</p> <p>The following operations are related to <code>SaveBrowserSessionProfile</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            profile_identifier: <p>The unique identifier for the browser profile. This identifier is used to reference the profile when starting new browser sessions. The identifier must follow the pattern of an alphanumeric name (up to 48 characters) followed by a hyphen and a 10-character alphanumeric suffix.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session from which to save the profile.</p>
            session_id: <p>The unique identifier of the browser session from which to save the profile. The session must be active when saving the profile.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

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
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile.async_save_browser_session_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest = {
            "profile_identifier": profile_identifier,
            "browser_identifier": browser_identifier,
            "session_id": session_id,
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
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
