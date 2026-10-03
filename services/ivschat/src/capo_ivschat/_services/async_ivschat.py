"""Generated from Smithy shape ``com.amazonaws.ivschat#AmazonInteractiveVideoServiceChat``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_ivschat._auth._signers
import capo_ivschat._auth._sigv4
from capo_ivschat._auth._identity import Credentials
from capo_ivschat._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ivschat._auth._zapros_handler import AuthMiddleware
from capo_ivschat._pagination import resolve_path as _resolve_path
from capo_ivschat._services._aws_config import aaws_config
from capo_ivschat._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_ivschat.types.chat_token_attributes
    import capo_ivschat.types.chat_token_capabilities
    import capo_ivschat.types.create_chat_token_request
    import capo_ivschat.types.create_chat_token_response
    import capo_ivschat.types.create_logging_configuration_request
    import capo_ivschat.types.create_logging_configuration_response
    import capo_ivschat.types.create_room_request
    import capo_ivschat.types.create_room_response
    import capo_ivschat.types.delete_logging_configuration_request
    import capo_ivschat.types.delete_message_request
    import capo_ivschat.types.delete_message_response
    import capo_ivschat.types.delete_room_request
    import capo_ivschat.types.destination_configuration
    import capo_ivschat.types.disconnect_user_request
    import capo_ivschat.types.disconnect_user_response
    import capo_ivschat.types.event_attributes
    import capo_ivschat.types.event_name
    import capo_ivschat.types.get_logging_configuration_request
    import capo_ivschat.types.get_logging_configuration_response
    import capo_ivschat.types.get_room_request
    import capo_ivschat.types.get_room_response
    import capo_ivschat.types.lambda_arn
    import capo_ivschat.types.list_logging_configurations_request
    import capo_ivschat.types.list_logging_configurations_response
    import capo_ivschat.types.list_rooms_request
    import capo_ivschat.types.list_rooms_response
    import capo_ivschat.types.list_tags_for_resource_request
    import capo_ivschat.types.list_tags_for_resource_response
    import capo_ivschat.types.logging_configuration_identifier
    import capo_ivschat.types.logging_configuration_identifier_list
    import capo_ivschat.types.logging_configuration_name
    import capo_ivschat.types.max_logging_configuration_results
    import capo_ivschat.types.max_room_results
    import capo_ivschat.types.message_id
    import capo_ivschat.types.message_review_handler
    import capo_ivschat.types.pagination_token
    import capo_ivschat.types.reason
    import capo_ivschat.types.resource_arn
    import capo_ivschat.types.room_identifier
    import capo_ivschat.types.room_max_message_length
    import capo_ivschat.types.room_max_message_rate_per_second
    import capo_ivschat.types.room_name
    import capo_ivschat.types.send_event_request
    import capo_ivschat.types.send_event_response
    import capo_ivschat.types.session_duration_in_minutes
    import capo_ivschat.types.tag_key_list
    import capo_ivschat.types.tag_resource_request
    import capo_ivschat.types.tag_resource_response
    import capo_ivschat.types.tags
    import capo_ivschat.types.untag_resource_request
    import capo_ivschat.types.untag_resource_response
    import capo_ivschat.types.update_logging_configuration_request
    import capo_ivschat.types.update_logging_configuration_response
    import capo_ivschat.types.update_room_request
    import capo_ivschat.types.update_room_response
    import capo_ivschat.types.user_id


class AsyncivschatClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncivschatClient:
    """A client for the ``ivschat`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncivschatClientConfig(
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
        self, config_overrides: Optional[AsyncivschatClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncivschatClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def create_chat_token(
        self,
        room_identifier: "capo_ivschat.types.room_identifier.RoomIdentifier",
        user_id: "capo_ivschat.types.user_id.UserID",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        capabilities: Optional[
            "capo_ivschat.types.chat_token_capabilities.ChatTokenCapabilities"
        ] = None,
        session_duration_in_minutes: Optional[
            "capo_ivschat.types.session_duration_in_minutes.SessionDurationInMinutes"
        ] = None,
        attributes: Optional[
            "capo_ivschat.types.chat_token_attributes.ChatTokenAttributes"
        ] = None,
    ) -> "capo_ivschat.types.create_chat_token_response.CreateChatTokenResponse":
        """<p>Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.</p> <p>Use the <code>capabilities</code> field to permit an end user to send messages or moderate a room.</p> <p>The <code>attributes</code> field securely attaches structured data to the chat session; the data is included within each message sent by the end user and received by other participants in the room. Common use cases for attributes include passing end-user profile data like an icon, display name, colors, badges, and other display features.</p> <p>Encryption keys are owned by Amazon IVS Chat and never used directly by your application.</p>

        Args:
            room_identifier: <p>Identifier of the room that the client is trying to access. Currently this must be an ARN. </p>
            user_id: <p>Application-provided ID that uniquely identifies the user associated with this token. This can be any UTF-8 encoded text.</p>
            capabilities: <p>Set of capabilities that the user is allowed to perform in the room. Default: None (the capability to view messages is implicitly included in all requests).</p>
            session_duration_in_minutes: <p>Session duration (in minutes), after which the session expires. Default: 60 (1 hour).</p>
            attributes: <p>Application-provided attributes to encode into the token and attach to a chat session. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.create_chat_token_request.CreateChatTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.create_chat_token_response.CreateChatTokenResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.create_chat_token

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.create_chat_token.async_create_chat_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.create_chat_token_request.CreateChatTokenRequest = {
            "room_identifier": room_identifier,
            "user_id": user_id,
        }
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if session_duration_in_minutes is not None:
            input_["session_duration_in_minutes"] = session_duration_in_minutes
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_logging_configuration(
        self,
        destination_configuration: "capo_ivschat.types.destination_configuration.DestinationConfiguration",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        name: Optional[
            "capo_ivschat.types.logging_configuration_name.LoggingConfigurationName"
        ] = None,
        tags: Optional["capo_ivschat.types.tags.Tags"] = None,
    ) -> "capo_ivschat.types.create_logging_configuration_response.CreateLoggingConfigurationResponse":
        """<p>Creates a logging configuration that allows clients to store and record sent messages.</p>

        Args:
            name: <p>Logging-configuration name. The value does not need to be unique.</p>
            destination_configuration: <p>A complex type that contains a destination configuration for where chat content will be logged. There can be only one type of destination (<code>cloudWatchLogs</code>, <code>firehose</code>, or <code>s3</code>) in a <code>destinationConfiguration</code>.</p>
            tags: <p>Tags to attach to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS Chat has no constraints on tags beyond what is documented there.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.conflict_exception.ConflictException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.create_logging_configuration_request.CreateLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.create_logging_configuration_response.CreateLoggingConfigurationResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.create_logging_configuration

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.create_logging_configuration.async_create_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.create_logging_configuration_request.CreateLoggingConfigurationRequest = {
            "destination_configuration": destination_configuration
        }
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_room(
        self,
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        name: Optional["capo_ivschat.types.room_name.RoomName"] = None,
        maximum_message_rate_per_second: Optional[
            "capo_ivschat.types.room_max_message_rate_per_second.RoomMaxMessageRatePerSecond"
        ] = None,
        maximum_message_length: Optional[
            "capo_ivschat.types.room_max_message_length.RoomMaxMessageLength"
        ] = None,
        message_review_handler: Optional[
            "capo_ivschat.types.message_review_handler.MessageReviewHandler"
        ] = None,
        tags: Optional["capo_ivschat.types.tags.Tags"] = None,
        logging_configuration_identifiers: Optional[
            "capo_ivschat.types.logging_configuration_identifier_list.LoggingConfigurationIdentifierList"
        ] = None,
    ) -> "capo_ivschat.types.create_room_response.CreateRoomResponse":
        """<p>Creates a room that allows clients to connect and pass messages.</p>

        Args:
            name: <p>Room name. The value does not need to be unique.</p>
            maximum_message_rate_per_second: <p>Maximum number of messages per second that can be sent to the room (by all clients). Default: 10. </p>
            maximum_message_length: <p>Maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: 500.</p>
            message_review_handler: <p>Configuration information for optional review of messages.</p>
            tags: <p>Tags to attach to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS Chat has no constraints beyond what is documented there.</p>
            logging_configuration_identifiers: <p>Array of logging-configuration identifiers attached to the room.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.conflict_exception.ConflictException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.create_room_request.CreateRoomRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.create_room_response.CreateRoomResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.create_room

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.create_room.async_create_room(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.create_room_request.CreateRoomRequest = {}
        if name is not None:
            input_["name"] = name
        if maximum_message_rate_per_second is not None:
            input_["maximum_message_rate_per_second"] = maximum_message_rate_per_second
        if maximum_message_length is not None:
            input_["maximum_message_length"] = maximum_message_length
        if message_review_handler is not None:
            input_["message_review_handler"] = message_review_handler
        if tags is not None:
            input_["tags"] = tags
        if logging_configuration_identifiers is not None:
            input_["logging_configuration_identifiers"] = (
                logging_configuration_identifiers
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_logging_configuration(
        self,
        identifier: "capo_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified logging configuration.</p>

        Args:
            identifier: <p>Identifier of the logging configuration to be deleted.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.conflict_exception.ConflictException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.delete_logging_configuration_request.DeleteLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.delete_logging_configuration

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.delete_logging_configuration.async_delete_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.delete_logging_configuration_request.DeleteLoggingConfigurationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_message(
        self,
        room_identifier: "capo_ivschat.types.room_identifier.RoomIdentifier",
        id: "capo_ivschat.types.message_id.MessageID",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        reason: Optional["capo_ivschat.types.reason.Reason"] = None,
    ) -> "capo_ivschat.types.delete_message_response.DeleteMessageResponse":
        """<p>Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s <code>EventName</code> is <code>aws:DELETE_MESSAGE</code>. This replicates the <a href="https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html"> DeleteMessage</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p>

        Args:
            room_identifier: <p>Identifier of the room where the message should be deleted. Currently this must be an ARN. </p>
            id: <p>ID of the message to be deleted. This is the <code>Id</code> field in the received message (see <a href="https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-message-subscribe.html"> Message (Subscribe)</a> in the Chat Messaging API).</p>
            reason: <p>Reason for deleting the message.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.throttling_exception.ThrottlingException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.delete_message_request.DeleteMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.delete_message_response.DeleteMessageResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.delete_message

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.delete_message.async_delete_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.delete_message_request.DeleteMessageRequest = {
            "room_identifier": room_identifier,
            "id": id,
        }
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_room(
        self,
        identifier: "capo_ivschat.types.room_identifier.RoomIdentifier",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified room.</p>

        Args:
            identifier: <p>Identifier of the room to be deleted. Currently this must be an ARN.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.delete_room_request.DeleteRoomRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.delete_room

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.delete_room.async_delete_room(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.delete_room_request.DeleteRoomRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disconnect_user(
        self,
        room_identifier: "capo_ivschat.types.room_identifier.RoomIdentifier",
        user_id: "capo_ivschat.types.user_id.UserID",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        reason: Optional["capo_ivschat.types.reason.Reason"] = None,
    ) -> "capo_ivschat.types.disconnect_user_response.DisconnectUserResponse":
        """<p>Disconnects all connections using a specified user ID from a room. This replicates the <a href="https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html"> DisconnectUser</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p>

        Args:
            room_identifier: <p>Identifier of the room from which the user's clients should be disconnected. Currently this must be an ARN.</p>
            user_id: <p>ID of the user (connection) to disconnect from the room.</p>
            reason: <p>Reason for disconnecting the user.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.throttling_exception.ThrottlingException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.disconnect_user_request.DisconnectUserRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.disconnect_user_response.DisconnectUserResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.disconnect_user

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.disconnect_user.async_disconnect_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.disconnect_user_request.DisconnectUserRequest = {
            "room_identifier": room_identifier,
            "user_id": user_id,
        }
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_logging_configuration(
        self,
        identifier: "capo_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
    ) -> "capo_ivschat.types.get_logging_configuration_response.GetLoggingConfigurationResponse":
        """<p>Gets the specified logging configuration.</p>

        Args:
            identifier: <p>Identifier of the logging configuration to be retrieved.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.get_logging_configuration_request.GetLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.get_logging_configuration_response.GetLoggingConfigurationResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.get_logging_configuration

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.get_logging_configuration.async_get_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.get_logging_configuration_request.GetLoggingConfigurationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_room(
        self,
        identifier: "capo_ivschat.types.room_identifier.RoomIdentifier",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
    ) -> "capo_ivschat.types.get_room_response.GetRoomResponse":
        """<p>Gets the specified room.</p>

        Args:
            identifier: <p>Identifier of the room for which the configuration is to be retrieved. Currently this must be an ARN.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.get_room_request.GetRoomRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.get_room_response.GetRoomResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.get_room

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.get_room.async_get_room(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.get_room_request.GetRoomRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_logging_configurations(
        self,
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        next_token: Optional[
            "capo_ivschat.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivschat.types.max_logging_configuration_results.MaxLoggingConfigurationResults"
        ] = None,
    ) -> "capo_ivschat.types.list_logging_configurations_response.ListLoggingConfigurationsResponse":
        """<p>Gets summary information about all your logging configurations in the AWS region where the API request is processed.</p>

        Args:
            next_token: <p>The first logging configurations to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of logging configurations to return. Default: 50.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.list_logging_configurations_request.ListLoggingConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.list_logging_configurations_response.ListLoggingConfigurationsResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.list_logging_configurations

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.list_logging_configurations.async_list_logging_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.list_logging_configurations_request.ListLoggingConfigurationsRequest = {}
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

    async def iter_list_logging_configurations(
        self,
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        next_token: Optional[
            "capo_ivschat.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivschat.types.max_logging_configuration_results.MaxLoggingConfigurationResults"
        ] = None,
    ) -> "AsyncIterator[capo_ivschat.types.list_logging_configurations_response.ListLoggingConfigurationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_logging_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_rooms(
        self,
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        name: Optional["capo_ivschat.types.room_name.RoomName"] = None,
        next_token: Optional[
            "capo_ivschat.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivschat.types.max_room_results.MaxRoomResults"
        ] = None,
        message_review_handler_uri: Optional[
            "capo_ivschat.types.lambda_arn.LambdaArn"
        ] = None,
        logging_configuration_identifier: Optional[
            "capo_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier"
        ] = None,
    ) -> "capo_ivschat.types.list_rooms_response.ListRoomsResponse":
        """<p>Gets summary information about all your rooms in the AWS region where the API request is processed. Results are sorted in descending order of <code>updateTime</code>.</p>

        Args:
            name: <p>Filters the list to match the specified room name.</p>
            next_token: <p>The first room to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>
            max_results: <p>Maximum number of rooms to return. Default: 50.</p>
            message_review_handler_uri: <p>Filters the list to match the specified message review handler URI.</p>
            logging_configuration_identifier: <p>Logging-configuration identifier.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.list_rooms_request.ListRoomsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.list_rooms_response.ListRoomsResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.list_rooms

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.list_rooms.async_list_rooms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.list_rooms_request.ListRoomsRequest = {}
        if name is not None:
            input_["name"] = name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if message_review_handler_uri is not None:
            input_["message_review_handler_uri"] = message_review_handler_uri
        if logging_configuration_identifier is not None:
            input_["logging_configuration_identifier"] = (
                logging_configuration_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_rooms(
        self,
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        name: Optional["capo_ivschat.types.room_name.RoomName"] = None,
        next_token: Optional[
            "capo_ivschat.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_ivschat.types.max_room_results.MaxRoomResults"
        ] = None,
        message_review_handler_uri: Optional[
            "capo_ivschat.types.lambda_arn.LambdaArn"
        ] = None,
        logging_configuration_identifier: Optional[
            "capo_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier"
        ] = None,
    ) -> "AsyncIterator[capo_ivschat.types.list_rooms_response.ListRoomsResponse]":
        _token = next_token
        while True:
            _response = await self.list_rooms(
                config_overrides=config_overrides,
                name=name,
                next_token=_token,
                max_results=max_results,
                message_review_handler_uri=message_review_handler_uri,
                logging_configuration_identifier=logging_configuration_identifier,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_ivschat.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
    ) -> (
        "capo_ivschat.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Gets information about AWS tags for the specified ARN.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be retrieved. The ARN must be URL-encoded.</p>

        Raises:
            capo_ivschat.errors.internal_server_exception.InternalServerException: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_event(
        self,
        room_identifier: "capo_ivschat.types.room_identifier.RoomIdentifier",
        event_name: "capo_ivschat.types.event_name.EventName",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        attributes: Optional[
            "capo_ivschat.types.event_attributes.EventAttributes"
        ] = None,
    ) -> "capo_ivschat.types.send_event_response.SendEventResponse":
        """<p>Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.</p>

        Args:
            room_identifier: <p>Identifier of the room to which the event will be sent. Currently this must be an ARN.</p>
            event_name: <p>Application-defined name of the event to send to clients.</p>
            attributes: <p>Application-defined metadata to attach to the event sent to clients. The maximum length of the metadata is 1 KB total.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.throttling_exception.ThrottlingException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.send_event_request.SendEventRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.send_event_response.SendEventResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.send_event

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.send_event.async_send_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.send_event_request.SendEventRequest = {
            "room_identifier": room_identifier,
            "event_name": event_name,
        }
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_ivschat.types.resource_arn.ResourceArn",
        tags: "capo_ivschat.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
    ) -> "capo_ivschat.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for the AWS resource with the specified ARN.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged. The ARN must be URL-encoded.</p>
            tags: <p>Array of tags to be added or updated. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS Chat has no constraints beyond what is documented there.</p>

        Raises:
            capo_ivschat.errors.internal_server_exception.InternalServerException: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.tag_resource

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_ivschat.types.resource_arn.ResourceArn",
        tag_keys: "capo_ivschat.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
    ) -> "capo_ivschat.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the resource with the specified ARN.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be untagged. The ARN must be URL-encoded.</p>
            tag_keys: <p>Array of tags to be removed. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS Chat has no constraints beyond what is documented there.</p>

        Raises:
            capo_ivschat.errors.internal_server_exception.InternalServerException: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.untag_resource

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_logging_configuration(
        self,
        identifier: "capo_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        name: Optional[
            "capo_ivschat.types.logging_configuration_name.LoggingConfigurationName"
        ] = None,
        destination_configuration: Optional[
            "capo_ivschat.types.destination_configuration.DestinationConfiguration"
        ] = None,
    ) -> "capo_ivschat.types.update_logging_configuration_response.UpdateLoggingConfigurationResponse":
        """<p>Updates a specified logging configuration.</p>

        Args:
            identifier: <p>Identifier of the logging configuration to be updated.</p>
            name: <p>Logging-configuration name. The value does not need to be unique.</p>
            destination_configuration: <p>A complex type that contains a destination configuration for where chat content will be logged. There can be only one type of destination (<code>cloudWatchLogs</code>, <code>firehose</code>, or <code>s3</code>) in a <code>destinationConfiguration</code>.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.conflict_exception.ConflictException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.update_logging_configuration_request.UpdateLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.update_logging_configuration_response.UpdateLoggingConfigurationResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.update_logging_configuration

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.update_logging_configuration.async_update_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.update_logging_configuration_request.UpdateLoggingConfigurationRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if destination_configuration is not None:
            input_["destination_configuration"] = destination_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_room(
        self,
        identifier: "capo_ivschat.types.room_identifier.RoomIdentifier",
        *,
        config_overrides: Optional[AsyncivschatClientConfig] = None,
        name: Optional["capo_ivschat.types.room_name.RoomName"] = None,
        maximum_message_rate_per_second: Optional[
            "capo_ivschat.types.room_max_message_rate_per_second.RoomMaxMessageRatePerSecond"
        ] = None,
        maximum_message_length: Optional[
            "capo_ivschat.types.room_max_message_length.RoomMaxMessageLength"
        ] = None,
        message_review_handler: Optional[
            "capo_ivschat.types.message_review_handler.MessageReviewHandler"
        ] = None,
        logging_configuration_identifiers: Optional[
            "capo_ivschat.types.logging_configuration_identifier_list.LoggingConfigurationIdentifierList"
        ] = None,
    ) -> "capo_ivschat.types.update_room_response.UpdateRoomResponse":
        """<p>Updates a room’s configuration.</p>

        Args:
            identifier: <p>Identifier of the room to be updated. Currently this must be an ARN.</p>
            name: <p>Room name. The value does not need to be unique.</p>
            maximum_message_rate_per_second: <p>Maximum number of messages per second that can be sent to the room (by all clients). Default: 10.</p>
            maximum_message_length: <p>The maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: 500.</p>
            message_review_handler: <p>Configuration information for optional review of messages. Specify an empty <code>uri</code> string to disassociate a message review handler from the specified room.</p>
            logging_configuration_identifiers: <p>Array of logging-configuration identifiers attached to the room.</p>

        Raises:
            capo_ivschat.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_ivschat.errors.pending_verification.PendingVerification: <p/>
            capo_ivschat.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_ivschat.errors.validation_exception.ValidationException: <p/>
            capo_ivschat.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ivschat.types.update_room_request.UpdateRoomRequest]",
        ) -> AsyncOperationResponse[
            "capo_ivschat.types.update_room_response.UpdateRoomResponse"
        ]:
            import capo_ivschat._operations.amazon_interactive_video_service_chat.update_room

            (
                output,
                http_response,
            ) = await capo_ivschat._operations.amazon_interactive_video_service_chat.update_room.async_update_room(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ivschat.types.update_room_request.UpdateRoomRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if maximum_message_rate_per_second is not None:
            input_["maximum_message_rate_per_second"] = maximum_message_rate_per_second
        if maximum_message_length is not None:
            input_["maximum_message_length"] = maximum_message_length
        if message_review_handler is not None:
            input_["message_review_handler"] = message_review_handler
        if logging_configuration_identifiers is not None:
            input_["logging_configuration_identifiers"] = (
                logging_configuration_identifiers
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
