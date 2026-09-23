"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#AWSDeepSenseRunTimeServiceApi2_0``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_lex_runtime_v2._auth._signers
import capo_lex_runtime_v2._auth._sigv4
from capo_lex_runtime_v2._auth._identity import Credentials
from capo_lex_runtime_v2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lex_runtime_v2._auth._zapros_handler import AuthMiddleware
from capo_lex_runtime_v2._body import Body
from capo_lex_runtime_v2._iter import ensure_sync_iterator
from capo_lex_runtime_v2._services._aws_config import aws_config
from capo_lex_runtime_v2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.blob_stream
    import capo_lex_runtime_v2.types.bot_alias_identifier
    import capo_lex_runtime_v2.types.bot_identifier
    import capo_lex_runtime_v2.types.conversation_mode
    import capo_lex_runtime_v2.types.delete_session_request
    import capo_lex_runtime_v2.types.delete_session_response
    import capo_lex_runtime_v2.types.get_session_request
    import capo_lex_runtime_v2.types.get_session_response
    import capo_lex_runtime_v2.types.locale_id
    import capo_lex_runtime_v2.types.messages
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.put_session_request
    import capo_lex_runtime_v2.types.put_session_response
    import capo_lex_runtime_v2.types.recognize_text_request
    import capo_lex_runtime_v2.types.recognize_text_response
    import capo_lex_runtime_v2.types.recognize_utterance_request
    import capo_lex_runtime_v2.types.recognize_utterance_response
    import capo_lex_runtime_v2.types.sensitive_non_empty_string
    import capo_lex_runtime_v2.types.session_id
    import capo_lex_runtime_v2.types.session_state
    import capo_lex_runtime_v2.types.start_conversation_request
    import capo_lex_runtime_v2.types.start_conversation_request_event_stream
    import capo_lex_runtime_v2.types.start_conversation_response
    import capo_lex_runtime_v2.types.string_map
    import capo_lex_runtime_v2.types.text


class LexRuntimeV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class LexRuntimeV2Client:
    """A client for the ``LexRuntimeV2`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = LexRuntimeV2ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[LexRuntimeV2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LexRuntimeV2ClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def delete_session(
        self,
        bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier",
        bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier",
        locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId",
        session_id: "capo_lex_runtime_v2.types.session_id.SessionId",
        *,
        config_overrides: Optional[LexRuntimeV2ClientConfig] = None,
    ) -> "capo_lex_runtime_v2.types.delete_session_response.DeleteSessionResponse":
        """<p>Removes session information for a specified bot, alias, and user ID. </p> <p>You can use this operation to restart a conversation with a bot. When you remove a session, the entire history of the session is removed so that you can start again.</p> <p>You don't need to delete a session. Sessions have a time limit and will expire. Set the session time limit when you create the bot. The default is 5 minutes, but you can specify anything between 1 minute and 24 hours.</p> <p>If you specify a bot or alias ID that doesn't exist, you receive a <code>BadRequestException.</code> </p> <p>If the locale doesn't exist in the bot, or if the locale hasn't been enables for the alias, you receive a <code>BadRequestException</code>.</p>

        Args:
            bot_id: <p>The identifier of the bot that contains the session data.</p>
            bot_alias_id: <p>The alias identifier in use for the bot that contains the session data.</p>
            locale_id: <p>The locale where the session is in use.</p>
            session_id: <p>The identifier of the session to delete.</p>

        Raises:
            capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException: <p></p>
            capo_lex_runtime_v2.errors.conflict_exception.ConflictException: <p></p>
            capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException: <p></p>
            capo_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException: <p></p>
            capo_lex_runtime_v2.errors.validation_exception.ValidationException: <p></p>
            capo_lex_runtime_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lex_runtime_v2.types.delete_session_request.DeleteSessionRequest]",
        ) -> OperationResponse[
            "capo_lex_runtime_v2.types.delete_session_response.DeleteSessionResponse"
        ]:
            import capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.delete_session

            output, http_response = (
                capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.delete_session.delete_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_v2.types.delete_session_request.DeleteSessionRequest = {
            "bot_id": bot_id,
            "bot_alias_id": bot_alias_id,
            "locale_id": locale_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_session(
        self,
        bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier",
        bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier",
        locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId",
        session_id: "capo_lex_runtime_v2.types.session_id.SessionId",
        *,
        config_overrides: Optional[LexRuntimeV2ClientConfig] = None,
    ) -> "capo_lex_runtime_v2.types.get_session_response.GetSessionResponse":
        """<p>Returns session information for a specified bot, alias, and user.</p> <p>For example, you can use this operation to retrieve session information for a user that has left a long-running session in use.</p> <p>If the bot, alias, or session identifier doesn't exist, Amazon Lex V2 returns a <code>BadRequestException</code>. If the locale doesn't exist or is not enabled for the alias, you receive a <code>BadRequestException</code>.</p>

        Args:
            bot_id: <p>The identifier of the bot that contains the session data.</p>
            bot_alias_id: <p>The alias identifier in use for the bot that contains the session data.</p>
            locale_id: <p>The locale where the session is in use.</p>
            session_id: <p>The identifier of the session to return.</p>

        Raises:
            capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException: <p></p>
            capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException: <p></p>
            capo_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException: <p></p>
            capo_lex_runtime_v2.errors.validation_exception.ValidationException: <p></p>
            capo_lex_runtime_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lex_runtime_v2.types.get_session_request.GetSessionRequest]",
        ) -> OperationResponse[
            "capo_lex_runtime_v2.types.get_session_response.GetSessionResponse"
        ]:
            import capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.get_session

            output, http_response = (
                capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_v2.types.get_session_request.GetSessionRequest = {
            "bot_id": bot_id,
            "bot_alias_id": bot_alias_id,
            "locale_id": locale_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def put_session(
        self,
        bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier",
        bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier",
        locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId",
        session_id: "capo_lex_runtime_v2.types.session_id.SessionId",
        session_state: "capo_lex_runtime_v2.types.session_state.SessionState",
        *,
        config_overrides: Optional[LexRuntimeV2ClientConfig] = None,
        messages: Optional["capo_lex_runtime_v2.types.messages.Messages"] = None,
        request_attributes: Optional[
            "capo_lex_runtime_v2.types.string_map.StringMap"
        ] = None,
        response_content_type: Optional[
            "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "Generator[capo_lex_runtime_v2.types.put_session_response.PutSessionResponse]":
        """<p>Creates a new session or modifies an existing session with an Amazon Lex V2 bot. Use this operation to enable your application to set the state of the bot.</p>

        Args:
            bot_id: <p>The identifier of the bot that receives the session data.</p>
            bot_alias_id: <p>The alias identifier of the bot that receives the session data.</p>
            locale_id: <p>The locale where the session is in use.</p>
            session_id: <p>The identifier of the session that receives the session data.</p>
            messages: <p>A list of messages to send to the user. Messages are sent in the order that they are defined in the list.</p>
            session_state: <p>Sets the state of the session with the user. You can use this to set the current intent, attributes, context, and dialog action. Use the dialog action to determine the next step that Amazon Lex V2 should use in the conversation with the user.</p>
            request_attributes: <p>Request-specific information passed between Amazon Lex V2 and the client application.</p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes with the prefix <code>x-amz-lex:</code>.</p>
            response_content_type: <p>The message that Amazon Lex V2 returns in the response can be either text or speech depending on the value of this parameter. </p> <ul> <li> <p>If the value is <code>text/plain; charset=utf-8</code>, Amazon Lex V2 returns text in the response.</p> </li> </ul>

        Raises:
            capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException: <p></p>
            capo_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException: <p></p>
            capo_lex_runtime_v2.errors.conflict_exception.ConflictException: <p></p>
            capo_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException: <p></p>
            capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException: <p></p>
            capo_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException: <p></p>
            capo_lex_runtime_v2.errors.validation_exception.ValidationException: <p></p>
            capo_lex_runtime_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lex_runtime_v2.types.put_session_request.PutSessionRequest]",
        ) -> OperationResponse[
            "capo_lex_runtime_v2.types.put_session_response.PutSessionResponse"
        ]:
            import capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.put_session

            output, http_response = (
                capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.put_session.put_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_v2.types.put_session_request.PutSessionRequest = {
            "bot_id": bot_id,
            "bot_alias_id": bot_alias_id,
            "locale_id": locale_id,
            "session_id": session_id,
            "session_state": session_state,
        }
        if messages is not None:
            input_["messages"] = messages
        if request_attributes is not None:
            input_["request_attributes"] = request_attributes
        if response_content_type is not None:
            input_["response_content_type"] = response_content_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def recognize_text(
        self,
        bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier",
        bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier",
        locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId",
        session_id: "capo_lex_runtime_v2.types.session_id.SessionId",
        text: "capo_lex_runtime_v2.types.text.Text",
        *,
        config_overrides: Optional[LexRuntimeV2ClientConfig] = None,
        session_state: Optional[
            "capo_lex_runtime_v2.types.session_state.SessionState"
        ] = None,
        request_attributes: Optional[
            "capo_lex_runtime_v2.types.string_map.StringMap"
        ] = None,
    ) -> "capo_lex_runtime_v2.types.recognize_text_response.RecognizeTextResponse":
        r"""<p>Sends user input to Amazon Lex V2. Client applications use this API to send requests to Amazon Lex V2 at runtime. Amazon Lex V2 then interprets the user input using the machine learning model that it build for the bot.</p> <p>In response, Amazon Lex V2 returns the next message to convey to the user and an optional response card to display.</p> <p>If the optional post-fulfillment response is specified, the messages are returned as follows. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/API_PostFulfillmentStatusSpecification.html\">PostFulfillmentStatusSpecification</a>.</p> <ul> <li> <p> <b>Success message</b> - Returned if the Lambda function completes successfully and the intent state is fulfilled or ready fulfillment if the message is present.</p> </li> <li> <p> <b>Failed message</b> - The failed message is returned if the Lambda function throws an exception or if the Lambda function returns a failed intent state without a message.</p> </li> <li> <p> <b>Timeout message</b> - If you don't configure a timeout message and a timeout, and the Lambda function doesn't return within 30 seconds, the timeout message is returned. If you configure a timeout, the timeout message is returned when the period times out. </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete.html\">Completion message</a>.</p>

        Args:
            bot_id: <p>The identifier of the bot that processes the request.</p>
            bot_alias_id: <p>The alias identifier in use for the bot that processes the request.</p>
            locale_id: <p>The locale where the session is in use.</p>
            session_id: <p>The identifier of the user session that is having the conversation.</p>
            text: <p>The text that the user entered. Amazon Lex V2 interprets this text.</p>
            session_state: <p>The current state of the dialog between the user and the bot.</p>
            request_attributes: <p>Request-specific information passed between the client application and Amazon Lex V2 </p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes with the prefix <code>x-amz-lex:</code>.</p>

        Raises:
            capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException: <p></p>
            capo_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException: <p></p>
            capo_lex_runtime_v2.errors.conflict_exception.ConflictException: <p></p>
            capo_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException: <p></p>
            capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException: <p></p>
            capo_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException: <p></p>
            capo_lex_runtime_v2.errors.validation_exception.ValidationException: <p></p>
            capo_lex_runtime_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lex_runtime_v2.types.recognize_text_request.RecognizeTextRequest]",
        ) -> OperationResponse[
            "capo_lex_runtime_v2.types.recognize_text_response.RecognizeTextResponse"
        ]:
            import capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.recognize_text

            output, http_response = (
                capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.recognize_text.recognize_text(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_v2.types.recognize_text_request.RecognizeTextRequest = {
            "bot_id": bot_id,
            "bot_alias_id": bot_alias_id,
            "locale_id": locale_id,
            "session_id": session_id,
            "text": text,
        }
        if session_state is not None:
            input_["session_state"] = session_state
        if request_attributes is not None:
            input_["request_attributes"] = request_attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def recognize_utterance(
        self,
        bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier",
        bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier",
        locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId",
        session_id: "capo_lex_runtime_v2.types.session_id.SessionId",
        request_content_type: "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[LexRuntimeV2ClientConfig] = None,
        session_state: Optional[
            "capo_lex_runtime_v2.types.sensitive_non_empty_string.SensitiveNonEmptyString"
        ] = None,
        request_attributes: Optional[
            "capo_lex_runtime_v2.types.sensitive_non_empty_string.SensitiveNonEmptyString"
        ] = None,
        response_content_type: Optional[
            "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString"
        ] = None,
        input_stream: Optional[Body[Iterator[bytes]] | Iterator[bytes] | bytes] = None,
    ) -> "Generator[capo_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse]":
        r"""<p>Sends user input to Amazon Lex V2. You can send text or speech. Clients use this API to send text and audio requests to Amazon Lex V2 at runtime. Amazon Lex V2 interprets the user input using the machine learning model built for the bot.</p> <p>The following request fields must be compressed with gzip and then base64 encoded before you send them to Amazon Lex V2. </p> <ul> <li> <p>requestAttributes</p> </li> <li> <p>sessionState</p> </li> </ul> <p>The following response fields are compressed using gzip and then base64 encoded by Amazon Lex V2. Before you can use these fields, you must decode and decompress them. </p> <ul> <li> <p>inputTranscript</p> </li> <li> <p>interpretations</p> </li> <li> <p>messages</p> </li> <li> <p>requestAttributes</p> </li> <li> <p>sessionState</p> </li> </ul> <p>The example contains a Java application that compresses and encodes a Java object to send to Amazon Lex V2, and a second that decodes and decompresses a response from Amazon Lex V2.</p> <p>If the optional post-fulfillment response is specified, the messages are returned as follows. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/API_PostFulfillmentStatusSpecification.html\">PostFulfillmentStatusSpecification</a>.</p> <ul> <li> <p> <b>Success message</b> - Returned if the Lambda function completes successfully and the intent state is fulfilled or ready fulfillment if the message is present.</p> </li> <li> <p> <b>Failed message</b> - The failed message is returned if the Lambda function throws an exception or if the Lambda function returns a failed intent state without a message.</p> </li> <li> <p> <b>Timeout message</b> - If you don't configure a timeout message and a timeout, and the Lambda function doesn't return within 30 seconds, the timeout message is returned. If you configure a timeout, the timeout message is returned when the period times out. </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete.html\">Completion message</a>.</p>

        Args:
            bot_id: <p>The identifier of the bot that should receive the request.</p>
            bot_alias_id: <p>The alias identifier in use for the bot that should receive the request.</p>
            locale_id: <p>The locale where the session is in use.</p>
            session_id: <p>The identifier of the session in use.</p>
            session_state: <p>Sets the state of the session with the user. You can use this to set the current intent, attributes, context, and dialog action. Use the dialog action to determine the next step that Amazon Lex V2 should use in the conversation with the user.</p> <p>The <code>sessionState</code> field must be compressed using gzip and then base64 encoded before sending to Amazon Lex V2.</p>
            request_attributes: <p>Request-specific information passed between the client application and Amazon Lex V2 </p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes for prefix <code>x-amz-lex:</code>.</p> <p>The <code>requestAttributes</code> field must be compressed using gzip and then base64 encoded before sending to Amazon Lex V2.</p>
            request_content_type: <p>Indicates the format for audio input or that the content is text. The header must start with one of the following prefixes:</p> <ul> <li> <p>PCM format, audio data must be in little-endian byte order.</p> <ul> <li> <p>audio/l16; rate=16000; channels=1</p> </li> <li> <p>audio/x-l16; sample-rate=16000; channel-count=1</p> </li> <li> <p>audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false</p> </li> </ul> </li> <li> <p>Opus format</p> <ul> <li> <p>audio/x-cbr-opus-with-preamble;preamble-size=0;bit-rate=256000;frame-size-milliseconds=4</p> </li> </ul> </li> <li> <p>Text format</p> <ul> <li> <p>text/plain; charset=utf-8</p> </li> </ul> </li> </ul>
            response_content_type: <p>The message that Amazon Lex V2 returns in the response can be either text or speech based on the <code>responseContentType</code> value.</p> <ul> <li> <p>If the value is <code>text/plain;charset=utf-8</code>, Amazon Lex V2 returns text in the response.</p> </li> <li> <p>If the value begins with <code>audio/</code>, Amazon Lex V2 returns speech in the response. Amazon Lex V2 uses Amazon Polly to generate the speech using the configuration that you specified in the <code>responseContentType</code> parameter. For example, if you specify <code>audio/mpeg</code> as the value, Amazon Lex V2 returns speech in the MPEG format.</p> </li> <li> <p>If the value is <code>audio/pcm</code>, the speech returned is <code>audio/pcm</code> at 16 KHz in 16-bit, little-endian format.</p> </li> <li> <p>The following are the accepted values:</p> <ul> <li> <p>audio/mpeg</p> </li> <li> <p>audio/ogg</p> </li> <li> <p>audio/pcm (16 KHz)</p> </li> <li> <p>audio/* (defaults to mpeg)</p> </li> <li> <p>text/plain; charset=utf-8</p> </li> </ul> </li> </ul>
            input_stream: <p>User input in PCM or Opus audio format or text format as described in the <code>requestContentType</code> parameter.</p>

        Raises:
            capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException: <p></p>
            capo_lex_runtime_v2.errors.bad_gateway_exception.BadGatewayException: <p></p>
            capo_lex_runtime_v2.errors.conflict_exception.ConflictException: <p></p>
            capo_lex_runtime_v2.errors.dependency_failed_exception.DependencyFailedException: <p></p>
            capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException: <p></p>
            capo_lex_runtime_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p></p>
            capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException: <p></p>
            capo_lex_runtime_v2.errors.validation_exception.ValidationException: <p></p>
            capo_lex_runtime_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest]",
        ) -> OperationResponse[
            "capo_lex_runtime_v2.types.recognize_utterance_response.RecognizeUtteranceResponse"
        ]:
            import capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.recognize_utterance

            output, http_response = (
                capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.recognize_utterance.recognize_utterance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_v2.types.recognize_utterance_request.RecognizeUtteranceRequest = {
            "bot_id": bot_id,
            "bot_alias_id": bot_alias_id,
            "locale_id": locale_id,
            "session_id": session_id,
            "request_content_type": request_content_type,
        }
        if session_state is not None:
            input_["session_state"] = session_state
        if request_attributes is not None:
            input_["request_attributes"] = request_attributes
        if response_content_type is not None:
            input_["response_content_type"] = response_content_type
        if input_stream is not None:
            input_["input_stream"] = ensure_sync_iterator(input_stream)

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    @contextmanager
    def start_conversation(
        self,
        bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier",
        bot_alias_id: "capo_lex_runtime_v2.types.bot_alias_identifier.BotAliasIdentifier",
        locale_id: "capo_lex_runtime_v2.types.locale_id.LocaleId",
        session_id: "capo_lex_runtime_v2.types.session_id.SessionId",
        request_event_stream: "Iterator[capo_lex_runtime_v2.types.start_conversation_request_event_stream._StartConversationRequestEventStream] | capo_lex_runtime_v2.types.start_conversation_request_event_stream._StartConversationRequestEventStream",
        *,
        config_overrides: Optional[LexRuntimeV2ClientConfig] = None,
        conversation_mode: Optional[
            "capo_lex_runtime_v2.types.conversation_mode.ConversationMode"
        ] = None,
    ) -> "Generator[capo_lex_runtime_v2.types.start_conversation_response.StartConversationResponse]":
        r"""<p>Starts an HTTP/2 bidirectional event stream that enables you to send audio, text, or DTMF input in real time. After your application starts a conversation, users send input to Amazon Lex V2 as a stream of events. Amazon Lex V2 processes the incoming events and responds with streaming text or audio events. </p> <p>Audio input must be in the following format: <code>audio/lpcm sample-rate=8000 sample-size-bits=16 channel-count=1; is-big-endian=false</code>.</p> <p>If the optional post-fulfillment response is specified, the messages are returned as follows. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/API_PostFulfillmentStatusSpecification.html\">PostFulfillmentStatusSpecification</a>.</p> <ul> <li> <p> <b>Success message</b> - Returned if the Lambda function completes successfully and the intent state is fulfilled or ready fulfillment if the message is present.</p> </li> <li> <p> <b>Failed message</b> - The failed message is returned if the Lambda function throws an exception or if the Lambda function returns a failed intent state without a message.</p> </li> <li> <p> <b>Timeout message</b> - If you don't configure a timeout message and a timeout, and the Lambda function doesn't return within 30 seconds, the timeout message is returned. If you configure a timeout, the timeout message is returned when the period times out. </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete.html\">Completion message</a>.</p> <p>If the optional update message is configured, it is played at the specified frequency while the Lambda function is running and the update message state is active. If the fulfillment update message is not active, the Lambda function runs with a 30 second timeout. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-update.html\">Update message </a> </p> <p>The <code>StartConversation</code> operation is supported only in the following SDKs: </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/goto/SdkForCpp/runtime.lex.v2-2020-08-07/StartConversation\">AWS SDK for C++</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/goto/SdkForJavaV2/runtime.lex.v2-2020-08-07/StartConversation\">AWS SDK for Java V2</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/goto/SdkForRubyV3/runtime.lex.v2-2020-08-07/StartConversation\">AWS SDK for Ruby V3</a> </p> </li> </ul>

        Args:
            bot_id: <p>The identifier of the bot to process the request.</p>
            bot_alias_id: <p>The alias identifier in use for the bot that processes the request.</p>
            locale_id: <p>The locale where the session is in use.</p>
            session_id: <p>The identifier of the user session that is having the conversation.</p>
            conversation_mode: <p>The conversation type that you are using the Amazon Lex V2. If the conversation mode is <code>AUDIO</code> you can send both audio and DTMF information. If the mode is <code>TEXT</code> you can only send text.</p>
            request_event_stream: <p>Represents the stream of events to Amazon Lex V2 from your application. The events are encoded as HTTP/2 data frames.</p>

        Raises:
            capo_lex_runtime_v2.errors.access_denied_exception.AccessDeniedException: <p></p>
            capo_lex_runtime_v2.errors.internal_server_exception.InternalServerException: <p></p>
            capo_lex_runtime_v2.errors.throttling_exception.ThrottlingException: <p></p>
            capo_lex_runtime_v2.errors.validation_exception.ValidationException: <p></p>
            capo_lex_runtime_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lex_runtime_v2.types.start_conversation_request.StartConversationRequest]",
        ) -> OperationResponse[
            "capo_lex_runtime_v2.types.start_conversation_response.StartConversationResponse"
        ]:
            import capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.start_conversation

            output, http_response = (
                capo_lex_runtime_v2._operations.aws_deep_sense_run_time_service_api2_0.start_conversation.start_conversation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_v2.types.start_conversation_request.StartConversationRequest = {
            "bot_id": bot_id,
            "bot_alias_id": bot_alias_id,
            "locale_id": locale_id,
            "session_id": session_id,
            "request_event_stream": ensure_sync_iterator(request_event_stream),
        }
        if conversation_mode is not None:
            input_["conversation_mode"] = conversation_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
