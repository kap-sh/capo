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
    import capo_bedrock_agentcore.types.browser_action
    import capo_bedrock_agentcore.types.browser_enterprise_policies
    import capo_bedrock_agentcore.types.browser_extensions
    import capo_bedrock_agentcore.types.browser_profile_configuration
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.browser_session_status
    import capo_bedrock_agentcore.types.browser_session_timeout
    import capo_bedrock_agentcore.types.certificates
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.get_browser_session_request
    import capo_bedrock_agentcore.types.get_browser_session_response
    import capo_bedrock_agentcore.types.invoke_browser_request
    import capo_bedrock_agentcore.types.invoke_browser_response
    import capo_bedrock_agentcore.types.list_browser_sessions_request
    import capo_bedrock_agentcore.types.list_browser_sessions_response
    import capo_bedrock_agentcore.types.max_results
    import capo_bedrock_agentcore.types.name
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.proxy_configuration
    import capo_bedrock_agentcore.types.start_browser_session_request
    import capo_bedrock_agentcore.types.start_browser_session_response
    import capo_bedrock_agentcore.types.stop_browser_session_request
    import capo_bedrock_agentcore.types.stop_browser_session_response
    import capo_bedrock_agentcore.types.stream_update
    import capo_bedrock_agentcore.types.tools_file_system_configurations
    import capo_bedrock_agentcore.types.update_browser_stream_request
    import capo_bedrock_agentcore.types.update_browser_stream_response
    import capo_bedrock_agentcore.types.view_port
    from capo_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from capo_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class BrowserSessionResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def read(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse":
        """<p>Retrieves detailed information about a specific browser session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, associated streams, and metadata.</p> <p>To get a browser session, you must specify both the browser identifier and the session ID. The response includes information about the session's viewport configuration, timeout settings, and stream endpoints.</p> <p>The following operations are related to <code>GetBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html">ListBrowserSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session.get_browser_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def invoke_browser(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        action: "capo_bedrock_agentcore.types.browser_action.BrowserAction",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse":
        """<p>Invokes an operating system-level action on a browser session in Amazon Bedrock AgentCore. This operation provides direct OS-level control over browser sessions, enabling mouse actions, keyboard input, and screenshots that the WebSocket-based Chrome DevTools Protocol (CDP) cannot handle — such as interacting with print dialogs, context menus, and JavaScript alerts.</p> <p>You send a request with exactly one action in the <code>BrowserAction</code> union, and receive a corresponding result in the <code>BrowserActionResult</code> union.</p> <p>The following operations are related to <code>InvokeBrowser</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with <code>StartBrowserSession</code>.</p>
            session_id: <p>The unique identifier of the browser session on which to perform the action. This must be an active session created with <code>StartBrowserSession</code>.</p>
            action: <p>The browser action to perform. Exactly one member of the <code>BrowserAction</code> union must be set per request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser.invoke_browser(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
            "action": action,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_browser_sessions(
        self,
        browser_identifier: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse":
        """<p>Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by browser identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListBrowserSessions</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions.list_browser_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest = {
            "browser_identifier": browser_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_browser_session(
        self,
        browser_identifier: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        name: Optional["capo_bedrock_agentcore.types.name.Name"] = None,
        session_timeout_seconds: Optional[
            "capo_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"
        ] = None,
        view_port: Optional["capo_bedrock_agentcore.types.view_port.ViewPort"] = None,
        extensions: Optional[
            "capo_bedrock_agentcore.types.browser_extensions.BrowserExtensions"
        ] = None,
        profile_configuration: Optional[
            "capo_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"
        ] = None,
        proxy_configuration: Optional[
            "capo_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"
        ] = None,
        enterprise_policies: Optional[
            "capo_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse":
        """<p>Creates and initializes a browser session in Amazon Bedrock AgentCore. The session enables agents to navigate and interact with web content, extract information from websites, and perform web-based tasks as part of their response generation.</p> <p>To create a session, you must specify a browser identifier and a name. You can also configure the viewport dimensions to control the visible area of web content. The session remains active until it times out or you explicitly stop it using the <code>StopBrowserSession</code> operation.</p> <p>The following operations are related to <code>StartBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html">UpdateBrowserStream</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html">SaveBrowserSessionProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeBrowser.html">InvokeBrowser</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.</p>
            name: <p>The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            view_port: <p>The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.</p>
            extensions: <p>A list of browser extensions to load into the browser session.</p>
            profile_configuration: <p>The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.</p>
            proxy_configuration: <p>Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via Amazon Web Services Secrets Manager and domain-based routing rules. Requires <code>secretsmanager:GetSecretValue</code> IAM permission for the specified secret ARNs.</p>
            enterprise_policies: <p>A list of files containing enterprise policies for the browser.</p>
            certificates: <p>A list of certificates to install in the browser session.</p>
            filesystem_configurations: <p>The file system configurations to mount into the browser session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session.start_browser_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest = {
            "browser_identifier": browser_identifier
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if name is not None:
            input_["name"] = name
        if session_timeout_seconds is not None:
            input_["session_timeout_seconds"] = session_timeout_seconds
        if view_port is not None:
            input_["view_port"] = view_port
        if extensions is not None:
            input_["extensions"] = extensions
        if profile_configuration is not None:
            input_["profile_configuration"] = profile_configuration
        if proxy_configuration is not None:
            input_["proxy_configuration"] = proxy_configuration
        if enterprise_policies is not None:
            input_["enterprise_policies"] = enterprise_policies
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    def stop_browser_session(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse":
        """<p>Terminates an active browser session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a browser session, you must specify both the browser identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartBrowserSession</code>.</p> <p>The following operations are related to <code>StopBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session.stop_browser_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest = {
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

    def update_browser_stream(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        stream_update: "capo_bedrock_agentcore.types.stream_update.StreamUpdate",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse":
        """<p>Updates a browser stream. To use this operation, you must have permissions to perform the bedrock:UpdateBrowserStream action.</p>

        Args:
            browser_identifier: <p>The identifier of the browser.</p>
            session_id: <p>The identifier of the browser session.</p>
            stream_update: <p>The update to apply to the browser stream.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream.update_browser_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
            "stream_update": stream_update,
        }
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


class AsyncBrowserSessionResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def read(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse":
        """<p>Retrieves detailed information about a specific browser session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, associated streams, and metadata.</p> <p>To get a browser session, you must specify both the browser identifier and the session ID. The response includes information about the session's viewport configuration, timeout settings, and stream endpoints.</p> <p>The following operations are related to <code>GetBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html">ListBrowserSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session.async_get_browser_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def invoke_browser(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        action: "capo_bedrock_agentcore.types.browser_action.BrowserAction",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse":
        """<p>Invokes an operating system-level action on a browser session in Amazon Bedrock AgentCore. This operation provides direct OS-level control over browser sessions, enabling mouse actions, keyboard input, and screenshots that the WebSocket-based Chrome DevTools Protocol (CDP) cannot handle — such as interacting with print dialogs, context menus, and JavaScript alerts.</p> <p>You send a request with exactly one action in the <code>BrowserAction</code> union, and receive a corresponding result in the <code>BrowserActionResult</code> union.</p> <p>The following operations are related to <code>InvokeBrowser</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with <code>StartBrowserSession</code>.</p>
            session_id: <p>The unique identifier of the browser session on which to perform the action. This must be an active session created with <code>StartBrowserSession</code>.</p>
            action: <p>The browser action to perform. Exactly one member of the <code>BrowserAction</code> union must be set per request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser.async_invoke_browser(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
            "action": action,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_browser_sessions(
        self,
        browser_identifier: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse":
        """<p>Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by browser identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListBrowserSessions</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions.async_list_browser_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest = {
            "browser_identifier": browser_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_browser_session(
        self,
        browser_identifier: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        name: Optional["capo_bedrock_agentcore.types.name.Name"] = None,
        session_timeout_seconds: Optional[
            "capo_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"
        ] = None,
        view_port: Optional["capo_bedrock_agentcore.types.view_port.ViewPort"] = None,
        extensions: Optional[
            "capo_bedrock_agentcore.types.browser_extensions.BrowserExtensions"
        ] = None,
        profile_configuration: Optional[
            "capo_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"
        ] = None,
        proxy_configuration: Optional[
            "capo_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"
        ] = None,
        enterprise_policies: Optional[
            "capo_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse":
        """<p>Creates and initializes a browser session in Amazon Bedrock AgentCore. The session enables agents to navigate and interact with web content, extract information from websites, and perform web-based tasks as part of their response generation.</p> <p>To create a session, you must specify a browser identifier and a name. You can also configure the viewport dimensions to control the visible area of web content. The session remains active until it times out or you explicitly stop it using the <code>StopBrowserSession</code> operation.</p> <p>The following operations are related to <code>StartBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html">UpdateBrowserStream</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html">SaveBrowserSessionProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeBrowser.html">InvokeBrowser</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.</p>
            name: <p>The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            view_port: <p>The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.</p>
            extensions: <p>A list of browser extensions to load into the browser session.</p>
            profile_configuration: <p>The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.</p>
            proxy_configuration: <p>Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via Amazon Web Services Secrets Manager and domain-based routing rules. Requires <code>secretsmanager:GetSecretValue</code> IAM permission for the specified secret ARNs.</p>
            enterprise_policies: <p>A list of files containing enterprise policies for the browser.</p>
            certificates: <p>A list of certificates to install in the browser session.</p>
            filesystem_configurations: <p>The file system configurations to mount into the browser session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session.async_start_browser_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest = {
            "browser_identifier": browser_identifier
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if name is not None:
            input_["name"] = name
        if session_timeout_seconds is not None:
            input_["session_timeout_seconds"] = session_timeout_seconds
        if view_port is not None:
            input_["view_port"] = view_port
        if extensions is not None:
            input_["extensions"] = extensions
        if profile_configuration is not None:
            input_["profile_configuration"] = profile_configuration
        if proxy_configuration is not None:
            input_["proxy_configuration"] = proxy_configuration
        if enterprise_policies is not None:
            input_["enterprise_policies"] = enterprise_policies
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    async def stop_browser_session(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse":
        """<p>Terminates an active browser session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a browser session, you must specify both the browser identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartBrowserSession</code>.</p> <p>The following operations are related to <code>StopBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session.async_stop_browser_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest = {
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

    async def update_browser_stream(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        stream_update: "capo_bedrock_agentcore.types.stream_update.StreamUpdate",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse":
        """<p>Updates a browser stream. To use this operation, you must have permissions to perform the bedrock:UpdateBrowserStream action.</p>

        Args:
            browser_identifier: <p>The identifier of the browser.</p>
            session_id: <p>The identifier of the browser session.</p>
            stream_update: <p>The update to apply to the browser stream.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream

            (
                output,
                http_response,
            ) = await capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream.async_update_browser_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
            "stream_update": stream_update,
        }
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
