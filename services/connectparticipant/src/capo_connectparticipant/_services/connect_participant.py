"""Generated from Smithy shape ``com.amazonaws.connectparticipant#AmazonConnectParticipantServiceLambda``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_connectparticipant._auth._signers
import capo_connectparticipant._auth._sigv4
from capo_connectparticipant._auth._identity import Credentials
from capo_connectparticipant._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_connectparticipant._auth._zapros_handler import AuthMiddleware
from capo_connectparticipant._pagination import resolve_path as _resolve_path
from capo_connectparticipant._services._aws_config import aws_config
from capo_connectparticipant._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_connectparticipant.types.artifact_id
    import capo_connectparticipant.types.attachment_id_list
    import capo_connectparticipant.types.attachment_name
    import capo_connectparticipant.types.attachment_size_in_bytes
    import capo_connectparticipant.types.bool
    import capo_connectparticipant.types.cancel_participant_authentication_request
    import capo_connectparticipant.types.cancel_participant_authentication_response
    import capo_connectparticipant.types.chat_content
    import capo_connectparticipant.types.chat_content_type
    import capo_connectparticipant.types.client_token
    import capo_connectparticipant.types.complete_attachment_upload_request
    import capo_connectparticipant.types.complete_attachment_upload_response
    import capo_connectparticipant.types.connection_type_list
    import capo_connectparticipant.types.contact_id
    import capo_connectparticipant.types.content_type
    import capo_connectparticipant.types.create_participant_connection_request
    import capo_connectparticipant.types.create_participant_connection_response
    import capo_connectparticipant.types.describe_view_request
    import capo_connectparticipant.types.describe_view_response
    import capo_connectparticipant.types.disconnect_participant_request
    import capo_connectparticipant.types.disconnect_participant_response
    import capo_connectparticipant.types.get_attachment_request
    import capo_connectparticipant.types.get_attachment_response
    import capo_connectparticipant.types.get_authentication_url_request
    import capo_connectparticipant.types.get_authentication_url_response
    import capo_connectparticipant.types.get_transcript_request
    import capo_connectparticipant.types.get_transcript_response
    import capo_connectparticipant.types.max_results
    import capo_connectparticipant.types.next_token
    import capo_connectparticipant.types.non_empty_client_token
    import capo_connectparticipant.types.participant_token
    import capo_connectparticipant.types.redirect_uri
    import capo_connectparticipant.types.scan_direction
    import capo_connectparticipant.types.send_event_request
    import capo_connectparticipant.types.send_event_response
    import capo_connectparticipant.types.send_message_request
    import capo_connectparticipant.types.send_message_response
    import capo_connectparticipant.types.session_id
    import capo_connectparticipant.types.sort_key
    import capo_connectparticipant.types.start_attachment_upload_request
    import capo_connectparticipant.types.start_attachment_upload_response
    import capo_connectparticipant.types.start_position
    import capo_connectparticipant.types.url_expiry_in_seconds
    import capo_connectparticipant.types.view_token


class ConnectParticipantClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ConnectParticipantClient:
    """A client for the ``ConnectParticipant`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = ConnectParticipantClientConfig(
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
        self, config_overrides: Optional[ConnectParticipantClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ConnectParticipantClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def cancel_participant_authentication(
        self,
        session_id: "capo_connectparticipant.types.session_id.SessionId",
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
    ) -> "capo_connectparticipant.types.cancel_participant_authentication_response.CancelParticipantAuthenticationResponse":
        """<p>Cancels the authentication session. The opted out branch of the Authenticate Customer flow block will be taken.</p> <note> <p>The current supported channel is chat. This API is not supported for Apple Messages for Business, WhatsApp, or SMS chats.</p> </note> <note> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            session_id: <p>The <code>sessionId</code> provided in the <code>authenticationInitiated</code> event.</p>
            connection_token: <p>The authentication token associated with the participant's connection.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.cancel_participant_authentication_request.CancelParticipantAuthenticationRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.cancel_participant_authentication_response.CancelParticipantAuthenticationResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.cancel_participant_authentication

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.cancel_participant_authentication.cancel_participant_authentication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.cancel_participant_authentication_request.CancelParticipantAuthenticationRequest = {
            "session_id": session_id,
            "connection_token": connection_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def complete_attachment_upload(
        self,
        attachment_ids: "capo_connectparticipant.types.attachment_id_list.AttachmentIdList",
        client_token: "capo_connectparticipant.types.non_empty_client_token.NonEmptyClientToken",
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
    ) -> "capo_connectparticipant.types.complete_attachment_upload_response.CompleteAttachmentUploadResponse":
        """<p>Allows you to confirm that the attachment has been uploaded using the pre-signed URL provided in StartAttachmentUpload API. A conflict exception is thrown when an attachment with that identifier is already being uploaded.</p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p> <note> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            attachment_ids: <p>A list of unique identifiers for the attachments.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            connection_token: <p>The authentication token associated with the participant's connection.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.conflict_exception.ConflictException: <p>The requested operation conflicts with the current state of a service resource associated with the request. </p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of attachments per contact exceeds the quota.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.complete_attachment_upload_request.CompleteAttachmentUploadRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.complete_attachment_upload_response.CompleteAttachmentUploadResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.complete_attachment_upload

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.complete_attachment_upload.complete_attachment_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.complete_attachment_upload_request.CompleteAttachmentUploadRequest = {
            "attachment_ids": attachment_ids,
            "client_token": client_token,
            "connection_token": connection_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_participant_connection(
        self,
        participant_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
        type: Optional[
            "capo_connectparticipant.types.connection_type_list.ConnectionTypeList"
        ] = None,
        connect_participant: Optional["capo_connectparticipant.types.bool.Bool"] = None,
    ) -> "capo_connectparticipant.types.create_participant_connection_response.CreateParticipantConnectionResponse":
        """<p>Creates the participant's connection. </p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p> <p>For WebRTC security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-webrtc-security">Connect Customer WebRTC security best practices</a>. </p> <note> <p> <code>ParticipantToken</code> is used for invoking this API instead of <code>ConnectionToken</code>.</p> </note> <p>The participant token is valid for the lifetime of the participant – until they are part of a contact. For WebRTC participants, if they leave or are disconnected for 60 seconds, a new participant needs to be created using the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateParticipant.html">CreateParticipant</a> API. </p> <p> <b>For <code>WEBSOCKET</code> Type</b>: </p> <p>The response URL for has a connect expiry timeout of 100s. Clients must manually connect to the returned websocket URL and subscribe to the desired topic. </p> <p>For chat, you need to publish the following on the established websocket connection:</p> <p> <code>{"topic":"aws/subscribe","content":{"topics":["aws/chat"]}}</code> </p> <p>Upon websocket URL expiry, as specified in the response ConnectionExpiry parameter, clients need to call this API again to obtain a new websocket URL and perform the same steps as before.</p> <p>The expiry time for the connection token is different than the <code>ChatDurationInMinutes</code>. Expiry time for the connection token is 1 day.</p> <p> <b>For <code>WEBRTC_CONNECTION</code> Type</b>: </p> <p>The response includes connection data required for the client application to join the call using the Amazon Chime SDK client libraries. The WebRTCConnection response contains Meeting and Attendee information needed to establish the media connection. </p> <p>The attendee join token in WebRTCConnection response is valid for the lifetime of the participant in the call. If a participant leaves or is disconnected for 60 seconds, their participant credentials will no longer be valid, and a new participant will need to be created to rejoin the call. </p> <p> <b>Message streaming support</b>: This API can also be used together with the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html">StartContactStreaming</a> API to create a participant connection for chat contacts that are not using a websocket. For more information about message streaming, <a href="https://docs.aws.amazon.com/connect/latest/adminguide/chat-message-streaming.html">Enable real-time chat message streaming</a> in the <i>Amazon Connect Administrator Guide</i>.</p> <p> <b>Multi-user web, in-app, video calling support</b>: </p> <p>For WebRTC calls, this API is used in conjunction with the CreateParticipant API to enable multi-party calling. The StartWebRTCContact API creates the initial contact and routes it to an agent, while CreateParticipant adds additional participants to the ongoing call. For more information about multi-party WebRTC calls, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-multiuser-inapp.html">Enable multi-user web, in-app, and video calling</a> in the <i>Amazon Connect Administrator Guide</i>. </p> <p> <b>Feature specifications</b>: For information about feature specifications, such as the allowed number of open websocket connections per participant or maximum number of WebRTC participants, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#feature-limits">Feature specifications</a> in the <i>Amazon Connect Administrator Guide</i>. </p> <note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p> </note>

        Args:
            type: <p>Type of connection information required. If you need <code>CONNECTION_CREDENTIALS</code> along with marking participant as connected, pass <code>CONNECTION_CREDENTIALS</code> in <code>Type</code>.</p>
            participant_token: <p>This is a header parameter.</p> <p>The ParticipantToken as obtained from <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html">StartChatContact</a> API response.</p>
            connect_participant: <p>Amazon Connect Participant is used to mark the participant as connected for customer participant in message streaming, as well as for agent or manager participant in non-streaming chats.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.create_participant_connection_request.CreateParticipantConnectionRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.create_participant_connection_response.CreateParticipantConnectionResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.create_participant_connection

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.create_participant_connection.create_participant_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.create_participant_connection_request.CreateParticipantConnectionRequest = {
            "participant_token": participant_token
        }
        if type is not None:
            input_["type"] = type
        if connect_participant is not None:
            input_["connect_participant"] = connect_participant

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_view(
        self,
        view_token: "capo_connectparticipant.types.view_token.ViewToken",
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
    ) -> "capo_connectparticipant.types.describe_view_response.DescribeViewResponse":
        """<p>Retrieves the view for the specified view token.</p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p>

        Args:
            view_token: <p>An encrypted token originating from the interactive message of a ShowView block operation. Represents the desired view.</p>
            connection_token: <p>The connection token.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.describe_view_request.DescribeViewRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.describe_view_response.DescribeViewResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.describe_view

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.describe_view.describe_view(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.describe_view_request.DescribeViewRequest = {
            "view_token": view_token,
            "connection_token": connection_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disconnect_participant(
        self,
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
        client_token: Optional[
            "capo_connectparticipant.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_connectparticipant.types.disconnect_participant_response.DisconnectParticipantResponse":
        """<p>Disconnects a participant. </p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p> <note> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            connection_token: <p>The authentication token associated with the participant's connection.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.disconnect_participant_request.DisconnectParticipantRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.disconnect_participant_response.DisconnectParticipantResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.disconnect_participant

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.disconnect_participant.disconnect_participant(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.disconnect_participant_request.DisconnectParticipantRequest = {
            "connection_token": connection_token
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

    def get_attachment(
        self,
        attachment_id: "capo_connectparticipant.types.artifact_id.ArtifactId",
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
        url_expiry_in_seconds: Optional[
            "capo_connectparticipant.types.url_expiry_in_seconds.URLExpiryInSeconds"
        ] = None,
    ) -> "capo_connectparticipant.types.get_attachment_response.GetAttachmentResponse":
        """<p>Provides a pre-signed URL for download of a completed attachment. This is an asynchronous API for use with active contacts.</p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p> <note> <ul> <li> <p>The participant role <code>CUSTOM_BOT</code> is not permitted to access attachments customers may upload. An <code>AccessDeniedException</code> can indicate that the participant may be a CUSTOM_BOT, and it doesn't have access to attachments.</p> </li> <li> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </li> </ul> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            attachment_id: <p>A unique identifier for the attachment.</p>
            connection_token: <p>The authentication token associated with the participant's connection.</p>
            url_expiry_in_seconds: <p>The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.get_attachment_request.GetAttachmentRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.get_attachment_response.GetAttachmentResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.get_attachment

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.get_attachment.get_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.get_attachment_request.GetAttachmentRequest = {
            "attachment_id": attachment_id,
            "connection_token": connection_token,
        }
        if url_expiry_in_seconds is not None:
            input_["url_expiry_in_seconds"] = url_expiry_in_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_authentication_url(
        self,
        session_id: "capo_connectparticipant.types.session_id.SessionId",
        redirect_uri: "capo_connectparticipant.types.redirect_uri.RedirectURI",
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
    ) -> "capo_connectparticipant.types.get_authentication_url_response.GetAuthenticationUrlResponse":
        """<p>Retrieves the AuthenticationUrl for the current authentication session for the AuthenticateCustomer flow block. </p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>.</p> <note> <ul> <li> <p>This API can only be called within one minute of receiving the authenticationInitiated event.</p> </li> <li> <p>The current supported channel is chat. This API is not supported for Apple Messages for Business, WhatsApp, or SMS chats.</p> </li> </ul> </note> <note> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            session_id: <p>The sessionId provided in the authenticationInitiated event.</p>
            redirect_uri: <p>The URL where the customer will be redirected after Amazon Cognito authorizes the user.</p>
            connection_token: <p>The authentication token associated with the participant's connection.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.get_authentication_url_request.GetAuthenticationUrlRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.get_authentication_url_response.GetAuthenticationUrlResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.get_authentication_url

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.get_authentication_url.get_authentication_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.get_authentication_url_request.GetAuthenticationUrlRequest = {
            "session_id": session_id,
            "redirect_uri": redirect_uri,
            "connection_token": connection_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_transcript(
        self,
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
        contact_id: Optional[
            "capo_connectparticipant.types.contact_id.ContactId"
        ] = None,
        max_results: Optional[
            "capo_connectparticipant.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_connectparticipant.types.next_token.NextToken"
        ] = None,
        scan_direction: Optional[
            "capo_connectparticipant.types.scan_direction.ScanDirection"
        ] = None,
        sort_order: Optional["capo_connectparticipant.types.sort_key.SortKey"] = None,
        start_position: Optional[
            "capo_connectparticipant.types.start_position.StartPosition"
        ] = None,
    ) -> "capo_connectparticipant.types.get_transcript_response.GetTranscriptResponse":
        """<p>Retrieves a transcript of the session, including details about any attachments. For information about accessing past chat contact transcripts for a persistent chat, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html">Enable persistent chat</a>. </p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p> <p>If you have a process that consumes events in the transcript of an chat that has ended, note that chat transcripts contain the following event content types if the event has occurred during the chat session:</p> <ul> <li> <p> <code>application/vnd.amazonaws.connect.event.participant.invited</code> </p> </li> <li> <p> <code>application/vnd.amazonaws.connect.event.participant.joined</code> </p> </li> <li> <p> <code>application/vnd.amazonaws.connect.event.participant.left</code> </p> </li> <li> <p> <code>application/vnd.amazonaws.connect.event.chat.ended</code> </p> </li> <li> <p> <code>application/vnd.amazonaws.connect.event.transfer.succeeded</code> </p> </li> <li> <p> <code>application/vnd.amazonaws.connect.event.transfer.failed</code> </p> </li> </ul> <note> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            contact_id: <p>The contactId from the current contact chain for which transcript is needed.</p>
            max_results: <p>The maximum number of results to return in the page. Default: 10. </p>
            next_token: <p>The pagination token. Use the value returned previously in the next subsequent request to retrieve the next set of results.</p>
            scan_direction: <p>The direction from StartPosition from which to retrieve message. Default: BACKWARD when no StartPosition is provided, FORWARD with StartPosition. </p>
            sort_order: <p>The sort order for the records. Default: DESCENDING.</p>
            start_position: <p>A filtering option for where to start.</p>
            connection_token: <p>The authentication token associated with the participant's connection.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.get_transcript_request.GetTranscriptRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.get_transcript_response.GetTranscriptResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.get_transcript

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.get_transcript.get_transcript(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.get_transcript_request.GetTranscriptRequest = {
            "connection_token": connection_token
        }
        if contact_id is not None:
            input_["contact_id"] = contact_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if scan_direction is not None:
            input_["scan_direction"] = scan_direction
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if start_position is not None:
            input_["start_position"] = start_position

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_transcript(
        self,
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
        contact_id: Optional[
            "capo_connectparticipant.types.contact_id.ContactId"
        ] = None,
        max_results: Optional[
            "capo_connectparticipant.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_connectparticipant.types.next_token.NextToken"
        ] = None,
        scan_direction: Optional[
            "capo_connectparticipant.types.scan_direction.ScanDirection"
        ] = None,
        sort_order: Optional["capo_connectparticipant.types.sort_key.SortKey"] = None,
        start_position: Optional[
            "capo_connectparticipant.types.start_position.StartPosition"
        ] = None,
    ) -> "Iterator[capo_connectparticipant.types.get_transcript_response.GetTranscriptResponse]":
        _token = next_token
        while True:
            _response = self.get_transcript(
                connection_token,
                config_overrides=config_overrides,
                contact_id=contact_id,
                max_results=max_results,
                next_token=_token,
                scan_direction=scan_direction,
                sort_order=sort_order,
                start_position=start_position,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def send_event(
        self,
        content_type: "capo_connectparticipant.types.chat_content_type.ChatContentType",
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
        content: Optional[
            "capo_connectparticipant.types.chat_content.ChatContent"
        ] = None,
        client_token: Optional[
            "capo_connectparticipant.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_connectparticipant.types.send_event_response.SendEventResponse":
        r"""<note> <p>The <code>application/vnd.amazonaws.connect.event.connection.acknowledged</code> ContentType is no longer maintained since December 31, 2024. This event has been migrated to the <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html">CreateParticipantConnection</a> API using the <code>ConnectParticipant</code> field.</p> </note> <p>Sends an event. Message receipts are not supported when there are more than two active participants in the chat. Using the SendEvent API for message receipts when a supervisor is barged-in will result in a conflict exception.</p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p> <note> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            content_type: <p>The content type of the request. Supported types are:</p> <ul> <li> <p>application/vnd.amazonaws.connect.event.typing</p> </li> <li> <p>application/vnd.amazonaws.connect.event.connection.acknowledged (is no longer maintained since December 31, 2024) </p> </li> <li> <p>application/vnd.amazonaws.connect.event.message.delivered</p> </li> <li> <p>application/vnd.amazonaws.connect.event.message.read</p> </li> </ul>
            content: <p>The content of the event to be sent (for example, message text). For content related to message receipts, this is supported in the form of a JSON string.</p> <p>Sample Content: "{\"messageId\":\"11111111-aaaa-bbbb-cccc-EXAMPLE01234\"}"</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            connection_token: <p>The authentication token associated with the participant's connection.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.conflict_exception.ConflictException: <p>The requested operation conflicts with the current state of a service resource associated with the request. </p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.send_event_request.SendEventRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.send_event_response.SendEventResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.send_event

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.send_event.send_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.send_event_request.SendEventRequest = {
            "content_type": content_type,
            "connection_token": connection_token,
        }
        if content is not None:
            input_["content"] = content
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

    def send_message(
        self,
        content_type: "capo_connectparticipant.types.chat_content_type.ChatContentType",
        content: "capo_connectparticipant.types.chat_content.ChatContent",
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
        client_token: Optional[
            "capo_connectparticipant.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_connectparticipant.types.send_message_response.SendMessageResponse":
        """<p>Sends a message.</p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p> <note> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            content_type: <p>The type of the content. Possible types are <code>text/plain</code>, <code>text/markdown</code>, <code>application/json</code>, and <code>application/vnd.amazonaws.connect.message.interactive.response</code>. </p> <p>Supported types on the contact are configured through <code>SupportedMessagingContentTypes</code> on <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html">StartChatContact</a> and <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundChatContact.html">StartOutboundChatContact</a>.</p> <p> For Apple Messages for Business, SMS, and WhatsApp Business Messaging contacts, only <code>text/plain</code> is supported.</p>
            content: <p>The content of the message. </p> <ul> <li> <p>For <code>text/plain</code> and <code>text/markdown</code>, the Length Constraints are Minimum of 1, Maximum of 1024. </p> </li> <li> <p>For <code>application/json</code>, the Length Constraints are Minimum of 1, Maximum of 12000. </p> </li> <li> <p>For <code>application/vnd.amazonaws.connect.message.interactive.response</code>, the Length Constraints are Minimum of 1, Maximum of 12288.</p> </li> </ul>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            connection_token: <p>The authentication token associated with the connection.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.send_message_request.SendMessageRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.send_message_response.SendMessageResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.send_message

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.send_message.send_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.send_message_request.SendMessageRequest = {
            "content_type": content_type,
            "content": content,
            "connection_token": connection_token,
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

    def start_attachment_upload(
        self,
        content_type: "capo_connectparticipant.types.content_type.ContentType",
        attachment_size_in_bytes: "capo_connectparticipant.types.attachment_size_in_bytes.AttachmentSizeInBytes",
        attachment_name: "capo_connectparticipant.types.attachment_name.AttachmentName",
        client_token: "capo_connectparticipant.types.non_empty_client_token.NonEmptyClientToken",
        connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken",
        *,
        config_overrides: Optional[ConnectParticipantClientConfig] = None,
    ) -> "capo_connectparticipant.types.start_attachment_upload_response.StartAttachmentUploadResponse":
        """<p>Provides a pre-signed Amazon S3 URL in response for uploading the file directly to S3.</p> <p>For security recommendations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat">Connect Customer Chat security best practices</a>. </p> <note> <p> <code>ConnectionToken</code> is used for invoking this API instead of <code>ParticipantToken</code>.</p> </note> <p>The Amazon Connect Participant Service APIs do not use <a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html">Signature Version 4 authentication</a>.</p>

        Args:
            content_type: <p>Describes the MIME file type of the attachment. For a list of supported file types, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html">Feature specifications</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            attachment_size_in_bytes: <p>The size of the attachment in bytes.</p>
            attachment_name: <p>A case-sensitive name of the attachment being uploaded.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            connection_token: <p>The authentication token associated with the participant's connection.</p>

        Raises:
            capo_connectparticipant.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectparticipant.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Amazon Connect service.</p>
            capo_connectparticipant.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of attachments per contact exceeds the quota.</p>
            capo_connectparticipant.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_connectparticipant.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Amazon Connect.</p>
            capo_connectparticipant.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_connectparticipant.types.start_attachment_upload_request.StartAttachmentUploadRequest]",
        ) -> OperationResponse[
            "capo_connectparticipant.types.start_attachment_upload_response.StartAttachmentUploadResponse"
        ]:
            import capo_connectparticipant._operations.amazon_connect_participant_service_lambda.start_attachment_upload

            output, http_response = (
                capo_connectparticipant._operations.amazon_connect_participant_service_lambda.start_attachment_upload.start_attachment_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectparticipant.types.start_attachment_upload_request.StartAttachmentUploadRequest = {
            "content_type": content_type,
            "attachment_size_in_bytes": attachment_size_in_bytes,
            "attachment_name": attachment_name,
            "client_token": client_token,
            "connection_token": connection_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
