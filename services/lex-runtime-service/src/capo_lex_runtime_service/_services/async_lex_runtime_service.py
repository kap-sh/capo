"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#AWSDeepSenseRunTimeService``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_lex_runtime_service._auth._signers
import capo_lex_runtime_service._auth._sigv4
from capo_lex_runtime_service._auth._identity import Credentials
from capo_lex_runtime_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lex_runtime_service._auth._zapros_handler import AuthMiddleware
from capo_lex_runtime_service._body import Body
from capo_lex_runtime_service._iter import ensure_async_iterator
from capo_lex_runtime_service._services._aws_config import aaws_config
from capo_lex_runtime_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.accept
    import capo_lex_runtime_service.types.active_contexts_list
    import capo_lex_runtime_service.types.blob_stream
    import capo_lex_runtime_service.types.bot_alias
    import capo_lex_runtime_service.types.bot_name
    import capo_lex_runtime_service.types.delete_session_request
    import capo_lex_runtime_service.types.delete_session_response
    import capo_lex_runtime_service.types.dialog_action
    import capo_lex_runtime_service.types.get_session_request
    import capo_lex_runtime_service.types.get_session_response
    import capo_lex_runtime_service.types.http_content_type
    import capo_lex_runtime_service.types.intent_summary_checkpoint_label
    import capo_lex_runtime_service.types.intent_summary_list
    import capo_lex_runtime_service.types.post_content_request
    import capo_lex_runtime_service.types.post_content_response
    import capo_lex_runtime_service.types.post_text_request
    import capo_lex_runtime_service.types.post_text_response
    import capo_lex_runtime_service.types.put_session_request
    import capo_lex_runtime_service.types.put_session_response
    import capo_lex_runtime_service.types.string_map
    import capo_lex_runtime_service.types.synthesized_json_active_contexts_string
    import capo_lex_runtime_service.types.synthesized_json_attributes_string
    import capo_lex_runtime_service.types.text
    import capo_lex_runtime_service.types.user_id


class AsyncLexRuntimeServiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncLexRuntimeServiceClient:
    """A client for the ``LexRuntimeService`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncLexRuntimeServiceClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncLexRuntimeServiceClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLexRuntimeServiceClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def delete_session(
        self,
        bot_name: "capo_lex_runtime_service.types.bot_name.BotName",
        bot_alias: "capo_lex_runtime_service.types.bot_alias.BotAlias",
        user_id: "capo_lex_runtime_service.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncLexRuntimeServiceClientConfig] = None,
    ) -> "capo_lex_runtime_service.types.delete_session_response.DeleteSessionResponse":
        """<p>Removes session information for a specified bot, alias, and user ID. </p>

        Args:
            bot_name: <p>The name of the bot that contains the session data.</p>
            bot_alias: <p>The alias in use for the bot that contains the session data.</p>
            user_id: <p>The identifier of the user associated with the session data.</p>

        Raises:
            capo_lex_runtime_service.errors.bad_request_exception.BadRequestException: <p> Request validation failed, there is no usable message in the context, or the bot build failed, is still in progress, or contains unbuilt changes. </p>
            capo_lex_runtime_service.errors.conflict_exception.ConflictException: <p> Two clients are using the same AWS account, Amazon Lex bot, and user ID. </p>
            capo_lex_runtime_service.errors.internal_failure_exception.InternalFailureException: <p>Internal service error. Retry the call.</p>
            capo_lex_runtime_service.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded a limit.</p>
            capo_lex_runtime_service.errors.not_found_exception.NotFoundException: <p>The resource (such as the Amazon Lex bot or an alias) that is referred to is not found.</p>
            capo_lex_runtime_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_runtime_service.types.delete_session_request.DeleteSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_runtime_service.types.delete_session_response.DeleteSessionResponse"
        ]:
            import capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.delete_session

            (
                output,
                http_response,
            ) = await capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.delete_session.async_delete_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_service.types.delete_session_request.DeleteSessionRequest = {
            "bot_name": bot_name,
            "bot_alias": bot_alias,
            "user_id": user_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session(
        self,
        bot_name: "capo_lex_runtime_service.types.bot_name.BotName",
        bot_alias: "capo_lex_runtime_service.types.bot_alias.BotAlias",
        user_id: "capo_lex_runtime_service.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncLexRuntimeServiceClientConfig] = None,
        checkpoint_label_filter: Optional[
            "capo_lex_runtime_service.types.intent_summary_checkpoint_label.IntentSummaryCheckpointLabel"
        ] = None,
    ) -> "capo_lex_runtime_service.types.get_session_response.GetSessionResponse":
        """<p>Returns session information for a specified bot, alias, and user ID.</p>

        Args:
            bot_name: <p>The name of the bot that contains the session data.</p>
            bot_alias: <p>The alias in use for the bot that contains the session data.</p>
            user_id: <p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. </p>
            checkpoint_label_filter: <p>A string used to filter the intents returned in the <code>recentIntentSummaryView</code> structure. </p> <p>When you specify a filter, only intents with their <code>checkpointLabel</code> field set to that string are returned.</p>

        Raises:
            capo_lex_runtime_service.errors.bad_request_exception.BadRequestException: <p> Request validation failed, there is no usable message in the context, or the bot build failed, is still in progress, or contains unbuilt changes. </p>
            capo_lex_runtime_service.errors.internal_failure_exception.InternalFailureException: <p>Internal service error. Retry the call.</p>
            capo_lex_runtime_service.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded a limit.</p>
            capo_lex_runtime_service.errors.not_found_exception.NotFoundException: <p>The resource (such as the Amazon Lex bot or an alias) that is referred to is not found.</p>
            capo_lex_runtime_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_runtime_service.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_runtime_service.types.get_session_response.GetSessionResponse"
        ]:
            import capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.get_session

            (
                output,
                http_response,
            ) = await capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_service.types.get_session_request.GetSessionRequest = {
            "bot_name": bot_name,
            "bot_alias": bot_alias,
            "user_id": user_id,
        }
        if checkpoint_label_filter is not None:
            input_["checkpoint_label_filter"] = checkpoint_label_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def post_content(
        self,
        bot_name: "capo_lex_runtime_service.types.bot_name.BotName",
        bot_alias: "capo_lex_runtime_service.types.bot_alias.BotAlias",
        user_id: "capo_lex_runtime_service.types.user_id.UserId",
        content_type: "capo_lex_runtime_service.types.http_content_type.HttpContentType",
        input_stream: Body[AsyncIterator[bytes]] | AsyncIterator[bytes] | bytes,
        *,
        config_overrides: Optional[AsyncLexRuntimeServiceClientConfig] = None,
        session_attributes: Optional[
            "capo_lex_runtime_service.types.synthesized_json_attributes_string.SynthesizedJsonAttributesString"
        ] = None,
        request_attributes: Optional[
            "capo_lex_runtime_service.types.synthesized_json_attributes_string.SynthesizedJsonAttributesString"
        ] = None,
        accept: Optional["capo_lex_runtime_service.types.accept.Accept"] = None,
        active_contexts: Optional[
            "capo_lex_runtime_service.types.synthesized_json_active_contexts_string.SynthesizedJsonActiveContextsString"
        ] = None,
    ) -> "AsyncGenerator[capo_lex_runtime_service.types.post_content_response.PostContentResponse]":
        """<p> Sends user input (text or speech) to Amazon Lex. Clients use this API to send text and audio requests to Amazon Lex at runtime. Amazon Lex interprets the user input using the machine learning model that it built for the bot. </p> <p>The <code>PostContent</code> operation supports audio input at 8kHz and 16kHz. You can use 8kHz audio to achieve higher speech recognition accuracy in telephone audio applications. </p> <p> In response, Amazon Lex returns the next message to convey to the user. Consider the following example messages: </p> <ul> <li> <p> For a user input "I would like a pizza," Amazon Lex might return a response with a message eliciting slot data (for example, <code>PizzaSize</code>): "What size pizza would you like?". </p> </li> <li> <p> After the user provides all of the pizza order information, Amazon Lex might return a response with a message to get user confirmation: "Order the pizza?". </p> </li> <li> <p> After the user replies "Yes" to the confirmation prompt, Amazon Lex might return a conclusion statement: "Thank you, your cheese pizza has been ordered.". </p> </li> </ul> <p> Not all Amazon Lex messages require a response from the user. For example, conclusion statements do not require a response. Some messages require only a yes or no response. In addition to the <code>message</code>, Amazon Lex provides additional context about the message in the response that you can use to enhance client behavior, such as displaying the appropriate client user interface. Consider the following examples: </p> <ul> <li> <p> If the message is to elicit slot data, Amazon Lex returns the following context information: </p> <ul> <li> <p> <code>x-amz-lex-dialog-state</code> header set to <code>ElicitSlot</code> </p> </li> <li> <p> <code>x-amz-lex-intent-name</code> header set to the intent name in the current context </p> </li> <li> <p> <code>x-amz-lex-slot-to-elicit</code> header set to the slot name for which the <code>message</code> is eliciting information </p> </li> <li> <p> <code>x-amz-lex-slots</code> header set to a map of slots configured for the intent with their current values </p> </li> </ul> </li> <li> <p> If the message is a confirmation prompt, the <code>x-amz-lex-dialog-state</code> header is set to <code>Confirmation</code> and the <code>x-amz-lex-slot-to-elicit</code> header is omitted. </p> </li> <li> <p> If the message is a clarification prompt configured for the intent, indicating that the user intent is not understood, the <code>x-amz-dialog-state</code> header is set to <code>ElicitIntent</code> and the <code>x-amz-slot-to-elicit</code> header is omitted. </p> </li> </ul> <p> In addition, Amazon Lex also returns your application-specific <code>sessionAttributes</code>. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html">Managing Conversation Context</a>. </p>

        Args:
            bot_name: <p>Name of the Amazon Lex bot.</p>
            bot_alias: <p>Alias of the Amazon Lex bot.</p>
            user_id: <p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. At runtime, each request must contain the <code>userID</code> field.</p> <p>To decide the user ID to use for your application, consider the following factors.</p> <ul> <li> <p>The <code>userID</code> field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.</p> </li> <li> <p>If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.</p> </li> <li> <p>If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.</p> </li> <li> <p>A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.</p> </li> </ul>
            session_attributes: <p>You pass this value as the <code>x-amz-lex-session-attributes</code> HTTP header.</p> <p>Application-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the <code>sessionAttributes</code> and <code>requestAttributes</code> headers is limited to 12 KB.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs">Setting Session Attributes</a>.</p>
            request_attributes: <p>You pass this value as the <code>x-amz-lex-request-attributes</code> HTTP header.</p> <p>Request-specific information passed between Amazon Lex and a client application. The value must be a JSON serialized and base64 encoded map with string keys and values. The total size of the <code>requestAttributes</code> and <code>sessionAttributes</code> headers is limited to 12 KB.</p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes with the prefix <code>x-amz-lex:</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs">Setting Request Attributes</a>.</p>
            content_type: <p> You pass this value as the <code>Content-Type</code> HTTP header. </p> <p> Indicates the audio format or text. The header value must start with one of the following prefixes: </p> <ul> <li> <p>PCM format, audio data must be in little-endian byte order.</p> <ul> <li> <p>audio/l16; rate=16000; channels=1</p> </li> <li> <p>audio/x-l16; sample-rate=16000; channel-count=1</p> </li> <li> <p>audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false </p> </li> </ul> </li> <li> <p>Opus format</p> <ul> <li> <p>audio/x-cbr-opus-with-preamble; preamble-size=0; bit-rate=256000; frame-size-milliseconds=4</p> </li> </ul> </li> <li> <p>Text format</p> <ul> <li> <p>text/plain; charset=utf-8</p> </li> </ul> </li> </ul>
            accept: <p> You pass this value as the <code>Accept</code> HTTP header. </p> <p> The message Amazon Lex returns in the response can be either text or speech based on the <code>Accept</code> HTTP header value in the request. </p> <ul> <li> <p> If the value is <code>text/plain; charset=utf-8</code>, Amazon Lex returns text in the response. </p> </li> <li> <p> If the value begins with <code>audio/</code>, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech (using the configuration you specified in the <code>Accept</code> header). For example, if you specify <code>audio/mpeg</code> as the value, Amazon Lex returns speech in the MPEG format.</p> </li> <li> <p>If the value is <code>audio/pcm</code>, the speech returned is <code>audio/pcm</code> in 16-bit, little endian format. </p> </li> <li> <p>The following are the accepted values:</p> <ul> <li> <p>audio/mpeg</p> </li> <li> <p>audio/ogg</p> </li> <li> <p>audio/pcm</p> </li> <li> <p>text/plain; charset=utf-8</p> </li> <li> <p>audio/* (defaults to mpeg)</p> </li> </ul> </li> </ul>
            input_stream: <p> User input in PCM or Opus audio format or text format as described in the <code>Content-Type</code> HTTP header. </p> <p>You can stream audio data to Amazon Lex or you can create a local buffer that captures all of the audio data before sending. In general, you get better performance if you stream audio data rather than buffering the data locally.</p>
            active_contexts: <p>A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,</p> <p>If you don't specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.</p>

        Raises:
            capo_lex_runtime_service.errors.bad_gateway_exception.BadGatewayException: <p>Either the Amazon Lex bot is still building, or one of the dependent services (Amazon Polly, AWS Lambda) failed with an internal service error.</p>
            capo_lex_runtime_service.errors.bad_request_exception.BadRequestException: <p> Request validation failed, there is no usable message in the context, or the bot build failed, is still in progress, or contains unbuilt changes. </p>
            capo_lex_runtime_service.errors.conflict_exception.ConflictException: <p> Two clients are using the same AWS account, Amazon Lex bot, and user ID. </p>
            capo_lex_runtime_service.errors.dependency_failed_exception.DependencyFailedException: <p> One of the dependencies, such as AWS Lambda or Amazon Polly, threw an exception. For example, </p> <ul> <li> <p>If Amazon Lex does not have sufficient permissions to call a Lambda function.</p> </li> <li> <p>If a Lambda function takes longer than 30 seconds to execute.</p> </li> <li> <p>If a fulfillment Lambda function returns a <code>Delegate</code> dialog action without removing any slot values.</p> </li> </ul>
            capo_lex_runtime_service.errors.internal_failure_exception.InternalFailureException: <p>Internal service error. Retry the call.</p>
            capo_lex_runtime_service.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded a limit.</p>
            capo_lex_runtime_service.errors.loop_detected_exception.LoopDetectedException: <p>This exception is not used.</p>
            capo_lex_runtime_service.errors.not_acceptable_exception.NotAcceptableException: <p>The accept header in the request does not have a valid value.</p>
            capo_lex_runtime_service.errors.not_found_exception.NotFoundException: <p>The resource (such as the Amazon Lex bot or an alias) that is referred to is not found.</p>
            capo_lex_runtime_service.errors.request_timeout_exception.RequestTimeoutException: <p>The input speech is too long.</p>
            capo_lex_runtime_service.errors.unsupported_media_type_exception.UnsupportedMediaTypeException: <p>The Content-Type header (<code>PostContent</code> API) has an invalid value. </p>
            capo_lex_runtime_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_runtime_service.types.post_content_request.PostContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_runtime_service.types.post_content_response.PostContentResponse"
        ]:
            import capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.post_content

            (
                output,
                http_response,
            ) = await capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.post_content.async_post_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_service.types.post_content_request.PostContentRequest = {
            "bot_name": bot_name,
            "bot_alias": bot_alias,
            "user_id": user_id,
            "content_type": content_type,
            "input_stream": ensure_async_iterator(input_stream),
        }
        if session_attributes is not None:
            input_["session_attributes"] = session_attributes
        if request_attributes is not None:
            input_["request_attributes"] = request_attributes
        if accept is not None:
            input_["accept"] = accept
        if active_contexts is not None:
            input_["active_contexts"] = active_contexts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def post_text(
        self,
        bot_name: "capo_lex_runtime_service.types.bot_name.BotName",
        bot_alias: "capo_lex_runtime_service.types.bot_alias.BotAlias",
        user_id: "capo_lex_runtime_service.types.user_id.UserId",
        input_text: "capo_lex_runtime_service.types.text.Text",
        *,
        config_overrides: Optional[AsyncLexRuntimeServiceClientConfig] = None,
        session_attributes: Optional[
            "capo_lex_runtime_service.types.string_map.StringMap"
        ] = None,
        request_attributes: Optional[
            "capo_lex_runtime_service.types.string_map.StringMap"
        ] = None,
        active_contexts: Optional[
            "capo_lex_runtime_service.types.active_contexts_list.ActiveContextsList"
        ] = None,
    ) -> "capo_lex_runtime_service.types.post_text_response.PostTextResponse":
        """<p>Sends user input to Amazon Lex. Client applications can use this API to send requests to Amazon Lex at runtime. Amazon Lex then interprets the user input using the machine learning model it built for the bot. </p> <p> In response, Amazon Lex returns the next <code>message</code> to convey to the user an optional <code>responseCard</code> to display. Consider the following example messages: </p> <ul> <li> <p> For a user input "I would like a pizza", Amazon Lex might return a response with a message eliciting slot data (for example, PizzaSize): "What size pizza would you like?" </p> </li> <li> <p> After the user provides all of the pizza order information, Amazon Lex might return a response with a message to obtain user confirmation "Proceed with the pizza order?". </p> </li> <li> <p> After the user replies to a confirmation prompt with a "yes", Amazon Lex might return a conclusion statement: "Thank you, your cheese pizza has been ordered.". </p> </li> </ul> <p> Not all Amazon Lex messages require a user response. For example, a conclusion statement does not require a response. Some messages require only a "yes" or "no" user response. In addition to the <code>message</code>, Amazon Lex provides additional context about the message in the response that you might use to enhance client behavior, for example, to display the appropriate client user interface. These are the <code>slotToElicit</code>, <code>dialogState</code>, <code>intentName</code>, and <code>slots</code> fields in the response. Consider the following examples: </p> <ul> <li> <p>If the message is to elicit slot data, Amazon Lex returns the following context information:</p> <ul> <li> <p> <code>dialogState</code> set to ElicitSlot </p> </li> <li> <p> <code>intentName</code> set to the intent name in the current context </p> </li> <li> <p> <code>slotToElicit</code> set to the slot name for which the <code>message</code> is eliciting information </p> </li> <li> <p> <code>slots</code> set to a map of slots, configured for the intent, with currently known values </p> </li> </ul> </li> <li> <p> If the message is a confirmation prompt, the <code>dialogState</code> is set to ConfirmIntent and <code>SlotToElicit</code> is set to null. </p> </li> <li> <p>If the message is a clarification prompt (configured for the intent) that indicates that user intent is not understood, the <code>dialogState</code> is set to ElicitIntent and <code>slotToElicit</code> is set to null. </p> </li> </ul> <p> In addition, Amazon Lex also returns your application-specific <code>sessionAttributes</code>. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html">Managing Conversation Context</a>. </p>

        Args:
            bot_name: <p>The name of the Amazon Lex bot.</p>
            bot_alias: <p>The alias of the Amazon Lex bot.</p>
            user_id: <p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. At runtime, each request must contain the <code>userID</code> field.</p> <p>To decide the user ID to use for your application, consider the following factors.</p> <ul> <li> <p>The <code>userID</code> field must not contain any personally identifiable information of the user, for example, name, personal identification numbers, or other end user personal information.</p> </li> <li> <p>If you want a user to start a conversation on one device and continue on another device, use a user-specific identifier.</p> </li> <li> <p>If you want the same user to be able to have two independent conversations on two different devices, choose a device-specific identifier.</p> </li> <li> <p>A user can't have two independent conversations with two different versions of the same bot. For example, a user can't have a conversation with the PROD and BETA versions of the same bot. If you anticipate that a user will need to have conversation with two different versions, for example, while testing, include the bot alias in the user ID to separate the two conversations.</p> </li> </ul>
            session_attributes: <p>Application-specific information passed between Amazon Lex and a client application.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-session-attribs">Setting Session Attributes</a>.</p>
            request_attributes: <p>Request-specific information passed between Amazon Lex and a client application.</p> <p>The namespace <code>x-amz-lex:</code> is reserved for special attributes. Don't create any request attributes with the prefix <code>x-amz-lex:</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#context-mgmt-request-attribs">Setting Request Attributes</a>.</p>
            input_text: <p>The text that the user entered (Amazon Lex interprets this text).</p>
            active_contexts: <p>A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,</p> <p>If you don't specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.</p>

        Raises:
            capo_lex_runtime_service.errors.bad_gateway_exception.BadGatewayException: <p>Either the Amazon Lex bot is still building, or one of the dependent services (Amazon Polly, AWS Lambda) failed with an internal service error.</p>
            capo_lex_runtime_service.errors.bad_request_exception.BadRequestException: <p> Request validation failed, there is no usable message in the context, or the bot build failed, is still in progress, or contains unbuilt changes. </p>
            capo_lex_runtime_service.errors.conflict_exception.ConflictException: <p> Two clients are using the same AWS account, Amazon Lex bot, and user ID. </p>
            capo_lex_runtime_service.errors.dependency_failed_exception.DependencyFailedException: <p> One of the dependencies, such as AWS Lambda or Amazon Polly, threw an exception. For example, </p> <ul> <li> <p>If Amazon Lex does not have sufficient permissions to call a Lambda function.</p> </li> <li> <p>If a Lambda function takes longer than 30 seconds to execute.</p> </li> <li> <p>If a fulfillment Lambda function returns a <code>Delegate</code> dialog action without removing any slot values.</p> </li> </ul>
            capo_lex_runtime_service.errors.internal_failure_exception.InternalFailureException: <p>Internal service error. Retry the call.</p>
            capo_lex_runtime_service.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded a limit.</p>
            capo_lex_runtime_service.errors.loop_detected_exception.LoopDetectedException: <p>This exception is not used.</p>
            capo_lex_runtime_service.errors.not_found_exception.NotFoundException: <p>The resource (such as the Amazon Lex bot or an alias) that is referred to is not found.</p>
            capo_lex_runtime_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_runtime_service.types.post_text_request.PostTextRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_runtime_service.types.post_text_response.PostTextResponse"
        ]:
            import capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.post_text

            (
                output,
                http_response,
            ) = await capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.post_text.async_post_text(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_service.types.post_text_request.PostTextRequest = {
            "bot_name": bot_name,
            "bot_alias": bot_alias,
            "user_id": user_id,
            "input_text": input_text,
        }
        if session_attributes is not None:
            input_["session_attributes"] = session_attributes
        if request_attributes is not None:
            input_["request_attributes"] = request_attributes
        if active_contexts is not None:
            input_["active_contexts"] = active_contexts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def put_session(
        self,
        bot_name: "capo_lex_runtime_service.types.bot_name.BotName",
        bot_alias: "capo_lex_runtime_service.types.bot_alias.BotAlias",
        user_id: "capo_lex_runtime_service.types.user_id.UserId",
        *,
        config_overrides: Optional[AsyncLexRuntimeServiceClientConfig] = None,
        session_attributes: Optional[
            "capo_lex_runtime_service.types.string_map.StringMap"
        ] = None,
        dialog_action: Optional[
            "capo_lex_runtime_service.types.dialog_action.DialogAction"
        ] = None,
        recent_intent_summary_view: Optional[
            "capo_lex_runtime_service.types.intent_summary_list.IntentSummaryList"
        ] = None,
        accept: Optional["capo_lex_runtime_service.types.accept.Accept"] = None,
        active_contexts: Optional[
            "capo_lex_runtime_service.types.active_contexts_list.ActiveContextsList"
        ] = None,
    ) -> "AsyncGenerator[capo_lex_runtime_service.types.put_session_response.PutSessionResponse]":
        """<p>Creates a new session or modifies an existing session with an Amazon Lex bot. Use this operation to enable your application to set the state of the bot.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/how-session-api.html">Managing Sessions</a>.</p>

        Args:
            bot_name: <p>The name of the bot that contains the session data.</p>
            bot_alias: <p>The alias in use for the bot that contains the session data.</p>
            user_id: <p>The ID of the client application user. Amazon Lex uses this to identify a user's conversation with your bot. </p>
            session_attributes: <p>Map of key/value pairs representing the session-specific context information. It contains application information passed between Amazon Lex and a client application.</p>
            dialog_action: <p>Sets the next action that the bot should take to fulfill the conversation.</p>
            recent_intent_summary_view: <p>A summary of the recent intents for the bot. You can use the intent summary view to set a checkpoint label on an intent and modify attributes of intents. You can also use it to remove or add intent summary objects to the list.</p> <p>An intent that you modify or add to the list must make sense for the bot. For example, the intent name must be valid for the bot. You must provide valid values for:</p> <ul> <li> <p> <code>intentName</code> </p> </li> <li> <p>slot names</p> </li> <li> <p> <code>slotToElict</code> </p> </li> </ul> <p>If you send the <code>recentIntentSummaryView</code> parameter in a <code>PutSession</code> request, the contents of the new summary view replaces the old summary view. For example, if a <code>GetSession</code> request returns three intents in the summary view and you call <code>PutSession</code> with one intent in the summary view, the next call to <code>GetSession</code> will only return one intent.</p>
            accept: <p>The message that Amazon Lex returns in the response can be either text or speech based depending on the value of this field.</p> <ul> <li> <p>If the value is <code>text/plain; charset=utf-8</code>, Amazon Lex returns text in the response.</p> </li> <li> <p>If the value begins with <code>audio/</code>, Amazon Lex returns speech in the response. Amazon Lex uses Amazon Polly to generate the speech in the configuration that you specify. For example, if you specify <code>audio/mpeg</code> as the value, Amazon Lex returns speech in the MPEG format.</p> </li> <li> <p>If the value is <code>audio/pcm</code>, the speech is returned as <code>audio/pcm</code> in 16-bit, little endian format.</p> </li> <li> <p>The following are the accepted values:</p> <ul> <li> <p> <code>audio/mpeg</code> </p> </li> <li> <p> <code>audio/ogg</code> </p> </li> <li> <p> <code>audio/pcm</code> </p> </li> <li> <p> <code>audio/*</code> (defaults to mpeg)</p> </li> <li> <p> <code>text/plain; charset=utf-8</code> </p> </li> </ul> </li> </ul>
            active_contexts: <p>A list of contexts active for the request. A context can be activated when a previous intent is fulfilled, or by including the context in the request,</p> <p>If you don't specify a list of contexts, Amazon Lex will use the current list of contexts for the session. If you specify an empty list, all contexts for the session are cleared.</p>

        Raises:
            capo_lex_runtime_service.errors.bad_gateway_exception.BadGatewayException: <p>Either the Amazon Lex bot is still building, or one of the dependent services (Amazon Polly, AWS Lambda) failed with an internal service error.</p>
            capo_lex_runtime_service.errors.bad_request_exception.BadRequestException: <p> Request validation failed, there is no usable message in the context, or the bot build failed, is still in progress, or contains unbuilt changes. </p>
            capo_lex_runtime_service.errors.conflict_exception.ConflictException: <p> Two clients are using the same AWS account, Amazon Lex bot, and user ID. </p>
            capo_lex_runtime_service.errors.dependency_failed_exception.DependencyFailedException: <p> One of the dependencies, such as AWS Lambda or Amazon Polly, threw an exception. For example, </p> <ul> <li> <p>If Amazon Lex does not have sufficient permissions to call a Lambda function.</p> </li> <li> <p>If a Lambda function takes longer than 30 seconds to execute.</p> </li> <li> <p>If a fulfillment Lambda function returns a <code>Delegate</code> dialog action without removing any slot values.</p> </li> </ul>
            capo_lex_runtime_service.errors.internal_failure_exception.InternalFailureException: <p>Internal service error. Retry the call.</p>
            capo_lex_runtime_service.errors.limit_exceeded_exception.LimitExceededException: <p>Exceeded a limit.</p>
            capo_lex_runtime_service.errors.not_acceptable_exception.NotAcceptableException: <p>The accept header in the request does not have a valid value.</p>
            capo_lex_runtime_service.errors.not_found_exception.NotFoundException: <p>The resource (such as the Amazon Lex bot or an alias) that is referred to is not found.</p>
            capo_lex_runtime_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_runtime_service.types.put_session_request.PutSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_runtime_service.types.put_session_response.PutSessionResponse"
        ]:
            import capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.put_session

            (
                output,
                http_response,
            ) = await capo_lex_runtime_service._operations.aws_deep_sense_run_time_service.put_session.async_put_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_runtime_service.types.put_session_request.PutSessionRequest = {
            "bot_name": bot_name,
            "bot_alias": bot_alias,
            "user_id": user_id,
        }
        if session_attributes is not None:
            input_["session_attributes"] = session_attributes
        if dialog_action is not None:
            input_["dialog_action"] = dialog_action
        if recent_intent_summary_view is not None:
            input_["recent_intent_summary_view"] = recent_intent_summary_view
        if accept is not None:
            input_["accept"] = accept
        if active_contexts is not None:
            input_["active_contexts"] = active_contexts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
