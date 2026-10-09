"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChimeMessagingService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_chime_sdk_messaging._auth._signers
import capo_chime_sdk_messaging._auth._sigv4
from capo_chime_sdk_messaging._auth._identity import Credentials
from capo_chime_sdk_messaging._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_chime_sdk_messaging._auth._zapros_handler import AuthMiddleware
from capo_chime_sdk_messaging._pagination import resolve_path as _resolve_path
from capo_chime_sdk_messaging._services._aws_config import aws_config
from capo_chime_sdk_messaging._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.associate_channel_flow_request
    import capo_chime_sdk_messaging.types.batch_create_channel_membership_request
    import capo_chime_sdk_messaging.types.batch_create_channel_membership_response
    import capo_chime_sdk_messaging.types.callback_id_type
    import capo_chime_sdk_messaging.types.channel_flow_callback_request
    import capo_chime_sdk_messaging.types.channel_flow_callback_response
    import capo_chime_sdk_messaging.types.channel_id
    import capo_chime_sdk_messaging.types.channel_member_arns
    import capo_chime_sdk_messaging.types.channel_membership_preferences
    import capo_chime_sdk_messaging.types.channel_membership_type
    import capo_chime_sdk_messaging.types.channel_message_callback
    import capo_chime_sdk_messaging.types.channel_message_persistence_type
    import capo_chime_sdk_messaging.types.channel_message_type
    import capo_chime_sdk_messaging.types.channel_mode
    import capo_chime_sdk_messaging.types.channel_moderator_arns
    import capo_chime_sdk_messaging.types.channel_privacy
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.client_request_token
    import capo_chime_sdk_messaging.types.content_type
    import capo_chime_sdk_messaging.types.create_channel_ban_request
    import capo_chime_sdk_messaging.types.create_channel_ban_response
    import capo_chime_sdk_messaging.types.create_channel_flow_request
    import capo_chime_sdk_messaging.types.create_channel_flow_response
    import capo_chime_sdk_messaging.types.create_channel_membership_request
    import capo_chime_sdk_messaging.types.create_channel_membership_response
    import capo_chime_sdk_messaging.types.create_channel_moderator_request
    import capo_chime_sdk_messaging.types.create_channel_moderator_response
    import capo_chime_sdk_messaging.types.create_channel_request
    import capo_chime_sdk_messaging.types.create_channel_response
    import capo_chime_sdk_messaging.types.delete_channel_ban_request
    import capo_chime_sdk_messaging.types.delete_channel_flow_request
    import capo_chime_sdk_messaging.types.delete_channel_membership_request
    import capo_chime_sdk_messaging.types.delete_channel_message_request
    import capo_chime_sdk_messaging.types.delete_channel_moderator_request
    import capo_chime_sdk_messaging.types.delete_channel_request
    import capo_chime_sdk_messaging.types.delete_messaging_streaming_configurations_request
    import capo_chime_sdk_messaging.types.describe_channel_ban_request
    import capo_chime_sdk_messaging.types.describe_channel_ban_response
    import capo_chime_sdk_messaging.types.describe_channel_flow_request
    import capo_chime_sdk_messaging.types.describe_channel_flow_response
    import capo_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_request
    import capo_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_response
    import capo_chime_sdk_messaging.types.describe_channel_membership_request
    import capo_chime_sdk_messaging.types.describe_channel_membership_response
    import capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request
    import capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response
    import capo_chime_sdk_messaging.types.describe_channel_moderator_request
    import capo_chime_sdk_messaging.types.describe_channel_moderator_response
    import capo_chime_sdk_messaging.types.describe_channel_request
    import capo_chime_sdk_messaging.types.describe_channel_response
    import capo_chime_sdk_messaging.types.disassociate_channel_flow_request
    import capo_chime_sdk_messaging.types.elastic_channel_configuration
    import capo_chime_sdk_messaging.types.expiration_settings
    import capo_chime_sdk_messaging.types.get_channel_membership_preferences_request
    import capo_chime_sdk_messaging.types.get_channel_membership_preferences_response
    import capo_chime_sdk_messaging.types.get_channel_message_request
    import capo_chime_sdk_messaging.types.get_channel_message_response
    import capo_chime_sdk_messaging.types.get_channel_message_status_request
    import capo_chime_sdk_messaging.types.get_channel_message_status_response
    import capo_chime_sdk_messaging.types.get_messaging_session_endpoint_request
    import capo_chime_sdk_messaging.types.get_messaging_session_endpoint_response
    import capo_chime_sdk_messaging.types.get_messaging_streaming_configurations_request
    import capo_chime_sdk_messaging.types.get_messaging_streaming_configurations_response
    import capo_chime_sdk_messaging.types.list_channel_bans_request
    import capo_chime_sdk_messaging.types.list_channel_bans_response
    import capo_chime_sdk_messaging.types.list_channel_flows_request
    import capo_chime_sdk_messaging.types.list_channel_flows_response
    import capo_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_request
    import capo_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_response
    import capo_chime_sdk_messaging.types.list_channel_memberships_request
    import capo_chime_sdk_messaging.types.list_channel_memberships_response
    import capo_chime_sdk_messaging.types.list_channel_messages_request
    import capo_chime_sdk_messaging.types.list_channel_messages_response
    import capo_chime_sdk_messaging.types.list_channel_moderators_request
    import capo_chime_sdk_messaging.types.list_channel_moderators_response
    import capo_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_request
    import capo_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_response
    import capo_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_request
    import capo_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_response
    import capo_chime_sdk_messaging.types.list_channels_request
    import capo_chime_sdk_messaging.types.list_channels_response
    import capo_chime_sdk_messaging.types.list_sub_channels_request
    import capo_chime_sdk_messaging.types.list_sub_channels_response
    import capo_chime_sdk_messaging.types.list_tags_for_resource_request
    import capo_chime_sdk_messaging.types.list_tags_for_resource_response
    import capo_chime_sdk_messaging.types.max_results
    import capo_chime_sdk_messaging.types.member_arns
    import capo_chime_sdk_messaging.types.message_attribute_map
    import capo_chime_sdk_messaging.types.message_id
    import capo_chime_sdk_messaging.types.metadata
    import capo_chime_sdk_messaging.types.network_type
    import capo_chime_sdk_messaging.types.next_token
    import capo_chime_sdk_messaging.types.non_empty_content
    import capo_chime_sdk_messaging.types.non_empty_resource_name
    import capo_chime_sdk_messaging.types.non_nullable_boolean
    import capo_chime_sdk_messaging.types.processor_list
    import capo_chime_sdk_messaging.types.push_notification_configuration
    import capo_chime_sdk_messaging.types.put_channel_expiration_settings_request
    import capo_chime_sdk_messaging.types.put_channel_expiration_settings_response
    import capo_chime_sdk_messaging.types.put_channel_membership_preferences_request
    import capo_chime_sdk_messaging.types.put_channel_membership_preferences_response
    import capo_chime_sdk_messaging.types.put_messaging_streaming_configurations_request
    import capo_chime_sdk_messaging.types.put_messaging_streaming_configurations_response
    import capo_chime_sdk_messaging.types.redact_channel_message_request
    import capo_chime_sdk_messaging.types.redact_channel_message_response
    import capo_chime_sdk_messaging.types.search_channels_request
    import capo_chime_sdk_messaging.types.search_channels_response
    import capo_chime_sdk_messaging.types.search_fields
    import capo_chime_sdk_messaging.types.send_channel_message_request
    import capo_chime_sdk_messaging.types.send_channel_message_response
    import capo_chime_sdk_messaging.types.sort_order
    import capo_chime_sdk_messaging.types.streaming_configuration_list
    import capo_chime_sdk_messaging.types.sub_channel_id
    import capo_chime_sdk_messaging.types.tag_key_list
    import capo_chime_sdk_messaging.types.tag_list
    import capo_chime_sdk_messaging.types.tag_resource_request
    import capo_chime_sdk_messaging.types.target_list
    import capo_chime_sdk_messaging.types.timestamp
    import capo_chime_sdk_messaging.types.untag_resource_request
    import capo_chime_sdk_messaging.types.update_channel_flow_request
    import capo_chime_sdk_messaging.types.update_channel_flow_response
    import capo_chime_sdk_messaging.types.update_channel_message_request
    import capo_chime_sdk_messaging.types.update_channel_message_response
    import capo_chime_sdk_messaging.types.update_channel_read_marker_request
    import capo_chime_sdk_messaging.types.update_channel_read_marker_response
    import capo_chime_sdk_messaging.types.update_channel_request
    import capo_chime_sdk_messaging.types.update_channel_response


class ChimeSDKMessagingClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ChimeSDKMessagingClient:
    """A client for the ``ChimeSDKMessaging`` service.

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
        self._config = ChimeSDKMessagingClientConfig(
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
        self, config_overrides: Optional[ChimeSDKMessagingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ChimeSDKMessagingClientConfig = config_overrides or {}
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

    def associate_channel_flow(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Associates a channel flow with a channel. Once associated, all messages to that channel go through channel flow processors. To stop processing, use the <code>DisassociateChannelFlow</code> API.</p> <note> <p>Only administrators or channel moderators can associate a channel flow. The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_flow_arn: <p>The ARN of the channel flow.</p>
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.associate_channel_flow_request.AssociateChannelFlowRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.associate_channel_flow

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.associate_channel_flow.associate_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.associate_channel_flow_request.AssociateChannelFlowRequest = {
            "channel_arn": channel_arn,
            "channel_flow_arn": channel_flow_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_create_channel_membership(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arns: "capo_chime_sdk_messaging.types.member_arns.MemberArns",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        type: Optional[
            "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
        ] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.batch_create_channel_membership_response.BatchCreateChannelMembershipResponse":
        """<p>Adds a specified number of users and bots to a channel. </p>

        Args:
            channel_arn: <p>The ARN of the channel to which you're adding users or bots.</p>
            type: <p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned. This is only supported by moderators.</p>
            member_arns: <p>The ARNs of the members you want to add to the channel. Only <code>AppInstanceUsers</code> and <code>AppInstanceBots</code> can be added as a channel member.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request. </p> <note> <p>Only required when creating membership in a SubChannel for a moderator in an elastic channel.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.batch_create_channel_membership_request.BatchCreateChannelMembershipRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.batch_create_channel_membership_response.BatchCreateChannelMembershipResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.batch_create_channel_membership

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.batch_create_channel_membership.batch_create_channel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.batch_create_channel_membership_request.BatchCreateChannelMembershipRequest = {
            "channel_arn": channel_arn,
            "member_arns": member_arns,
            "chime_bearer": chime_bearer,
        }
        if type is not None:
            input_["type"] = type
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def channel_flow_callback(
        self,
        callback_id: "capo_chime_sdk_messaging.types.callback_id_type.CallbackIdType",
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_message: "capo_chime_sdk_messaging.types.channel_message_callback.ChannelMessageCallback",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        delete_resource: Optional[
            "capo_chime_sdk_messaging.types.non_nullable_boolean.NonNullableBoolean"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.channel_flow_callback_response.ChannelFlowCallbackResponse":
        """<p>Calls back Amazon Chime SDK messaging with a processing response message. This should be invoked from the processor Lambda. This is a developer API.</p> <p>You can return one of the following processing responses:</p> <ul> <li> <p>Update message content or metadata</p> </li> <li> <p>Deny a message</p> </li> <li> <p>Make no changes to the message</p> </li> </ul>

        Args:
            callback_id: <p>The identifier passed to the processor by the service when invoked. Use the identifier to call back the service.</p>
            channel_arn: <p>The ARN of the channel.</p>
            delete_resource: <p>When a processor determines that a message needs to be <code>DENIED</code>, pass this parameter with a value of true.</p>
            channel_message: <p>Stores information about the processed message.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.channel_flow_callback_request.ChannelFlowCallbackRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.channel_flow_callback_response.ChannelFlowCallbackResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.channel_flow_callback

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.channel_flow_callback.channel_flow_callback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.channel_flow_callback_request.ChannelFlowCallbackRequest = {
            "callback_id": callback_id,
            "channel_arn": channel_arn,
            "channel_message": channel_message,
        }
        if delete_resource is not None:
            input_["delete_resource"] = delete_resource

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        name: "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName",
        client_request_token: "capo_chime_sdk_messaging.types.client_request_token.ClientRequestToken",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        mode: Optional[
            "capo_chime_sdk_messaging.types.channel_mode.ChannelMode"
        ] = None,
        privacy: Optional[
            "capo_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
        ] = None,
        metadata: Optional["capo_chime_sdk_messaging.types.metadata.Metadata"] = None,
        tags: Optional["capo_chime_sdk_messaging.types.tag_list.TagList"] = None,
        channel_id: Optional[
            "capo_chime_sdk_messaging.types.channel_id.ChannelId"
        ] = None,
        member_arns: Optional[
            "capo_chime_sdk_messaging.types.channel_member_arns.ChannelMemberArns"
        ] = None,
        moderator_arns: Optional[
            "capo_chime_sdk_messaging.types.channel_moderator_arns.ChannelModeratorArns"
        ] = None,
        elastic_channel_configuration: Optional[
            "capo_chime_sdk_messaging.types.elastic_channel_configuration.ElasticChannelConfiguration"
        ] = None,
        expiration_settings: Optional[
            "capo_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a channel to which you can add users and send messages.</p> <p> <b>Restriction</b>: You can't change a channel's privacy.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            app_instance_arn: <p>The ARN of the channel request.</p>
            name: <p>The name of the channel.</p>
            mode: <p>The channel mode: <code>UNRESTRICTED</code> or <code>RESTRICTED</code>. Administrators, moderators, and channel members can add themselves and other members to unrestricted channels. Only administrators and moderators can add members to restricted channels.</p>
            privacy: <p>The channel's privacy level: <code>PUBLIC</code> or <code>PRIVATE</code>. Private channels aren't discoverable by users outside the channel. Public channels are discoverable by anyone in the <code>AppInstance</code>.</p>
            metadata: <p>The metadata of the creation request. Limited to 1KB and UTF-8.</p>
            client_request_token: <p>The client token for the request. An <code>Idempotency</code> token.</p>
            tags: <p>The tags for the creation request.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            channel_id: <p>An ID for the channel being created. If you do not specify an ID, a UUID will be created for the channel.</p>
            member_arns: <p>The ARNs of the channel members in the request.</p>
            moderator_arns: <p>The ARNs of the channel moderators in the request.</p>
            elastic_channel_configuration: <p>The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million users, excluding moderators.</p>
            expiration_settings: <p>Settings that control the interval after which the channel is automatically deleted.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.create_channel_request.CreateChannelRequest = {
            "app_instance_arn": app_instance_arn,
            "name": name,
            "client_request_token": client_request_token,
            "chime_bearer": chime_bearer,
        }
        if mode is not None:
            input_["mode"] = mode
        if privacy is not None:
            input_["privacy"] = privacy
        if metadata is not None:
            input_["metadata"] = metadata
        if tags is not None:
            input_["tags"] = tags
        if channel_id is not None:
            input_["channel_id"] = channel_id
        if member_arns is not None:
            input_["member_arns"] = member_arns
        if moderator_arns is not None:
            input_["moderator_arns"] = moderator_arns
        if elastic_channel_configuration is not None:
            input_["elastic_channel_configuration"] = elastic_channel_configuration
        if expiration_settings is not None:
            input_["expiration_settings"] = expiration_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel_ban(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.create_channel_ban_response.CreateChannelBanResponse":
        """<p>Permanently bans a member from a channel. Moderators can't add banned members to a channel. To undo a ban, you first have to <code>DeleteChannelBan</code>, and then <code>CreateChannelMembership</code>. Bans are cleaned up when you delete users or channels.</p> <p>If you ban a user who is already part of a channel, that user is automatically kicked from the channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the ban request.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member being banned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.create_channel_ban_request.CreateChannelBanRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.create_channel_ban_response.CreateChannelBanResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel_ban

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel_ban.create_channel_ban(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.create_channel_ban_request.CreateChannelBanRequest = {
            "channel_arn": channel_arn,
            "member_arn": member_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel_flow(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        processors: "capo_chime_sdk_messaging.types.processor_list.ProcessorList",
        name: "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName",
        client_request_token: "capo_chime_sdk_messaging.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        tags: Optional["capo_chime_sdk_messaging.types.tag_list.TagList"] = None,
    ) -> "capo_chime_sdk_messaging.types.create_channel_flow_response.CreateChannelFlowResponse":
        """<p>Creates a channel flow, a container for processors. Processors are AWS Lambda functions that perform actions on chat messages, such as stripping out profanity. You can associate channel flows with channels, and the processors in the channel flow then take action on all messages sent to that channel. This is a developer API.</p> <p>Channel flows process the following items:</p> <ol> <li> <p>New and updated messages</p> </li> <li> <p>Persistent and non-persistent messages</p> </li> <li> <p>The Standard message type</p> </li> </ol> <note> <p>Channel flows don't process Control or System messages. For more information about the message types provided by Chime SDK messaging, refer to <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/using-the-messaging-sdk.html#msg-types">Message types</a> in the <i>Amazon Chime developer guide</i>.</p> </note>

        Args:
            app_instance_arn: <p>The ARN of the channel flow request.</p>
            processors: <p>Information about the processor Lambda functions.</p>
            name: <p>The name of the channel flow.</p>
            tags: <p>The tags for the creation request.</p>
            client_request_token: <p>The client token for the request. An Idempotency token.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.create_channel_flow_request.CreateChannelFlowRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.create_channel_flow_response.CreateChannelFlowResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel_flow

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel_flow.create_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.create_channel_flow_request.CreateChannelFlowRequest = {
            "app_instance_arn": app_instance_arn,
            "processors": processors,
            "name": name,
            "client_request_token": client_request_token,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel_membership(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        type: "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.create_channel_membership_response.CreateChannelMembershipResponse":
        """<p>Adds a member to a channel. The <code>InvitedBy</code> field in <code>ChannelMembership</code> is derived from the request header. A channel member can:</p> <ul> <li> <p>List messages</p> </li> <li> <p>Send messages</p> </li> <li> <p>Receive messages</p> </li> <li> <p>Edit their own messages</p> </li> <li> <p>Leave the channel</p> </li> </ul> <p>Privacy settings impact this action as follows:</p> <ul> <li> <p>Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.</p> </li> <li> <p>Private Channels: You must be a member to list or send messages.</p> </li> </ul> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUserArn</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel to which you're adding users.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member you want to add to the channel.</p>
            type: <p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned. This is only supported by moderators.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when creating membership in a SubChannel for a moderator in an elastic channel.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.create_channel_membership_request.CreateChannelMembershipRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.create_channel_membership_response.CreateChannelMembershipResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel_membership

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel_membership.create_channel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.create_channel_membership_request.CreateChannelMembershipRequest = {
            "channel_arn": channel_arn,
            "member_arn": member_arn,
            "type": type,
            "chime_bearer": chime_bearer,
        }
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel_moderator(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_moderator_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.create_channel_moderator_response.CreateChannelModeratorResponse":
        """<p>Creates a new <code>ChannelModerator</code>. A channel moderator can:</p> <ul> <li> <p>Add and remove other members of the channel.</p> </li> <li> <p>Add and remove other moderators of the channel.</p> </li> <li> <p>Add and remove user bans for the channel.</p> </li> <li> <p>Redact messages in the channel.</p> </li> <li> <p>List messages in the channel.</p> </li> </ul> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code>of the user that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_moderator_arn: <p>The <code>AppInstanceUserArn</code> of the moderator.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.create_channel_moderator_request.CreateChannelModeratorRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.create_channel_moderator_response.CreateChannelModeratorResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel_moderator

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.create_channel_moderator.create_channel_moderator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.create_channel_moderator_request.CreateChannelModeratorRequest = {
            "channel_arn": channel_arn,
            "channel_moderator_arn": channel_moderator_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Immediately makes a channel and its memberships inaccessible and marks them for deletion. This is an irreversible process.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUserArn</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel being deleted.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.delete_channel_request.DeleteChannelRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_ban(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Removes a member from a channel's ban list.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel from which the <code>AppInstanceUser</code> was banned.</p>
            member_arn: <p>The ARN of the <code>AppInstanceUser</code> that you want to reinstate.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.delete_channel_ban_request.DeleteChannelBanRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_ban

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_ban.delete_channel_ban(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.delete_channel_ban_request.DeleteChannelBanRequest = {
            "channel_arn": channel_arn,
            "member_arn": member_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_flow(
        self,
        channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Deletes a channel flow, an irreversible process. This is a developer API.</p> <note> <p> This API works only when the channel flow is not associated with any channel. To get a list of all channels that a channel flow is associated with, use the <code>ListChannelsAssociatedWithChannelFlow</code> API. Use the <code>DisassociateChannelFlow</code> API to disassociate a channel flow from all channels. </p> </note>

        Args:
            channel_flow_arn: <p>The ARN of the channel flow.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.delete_channel_flow_request.DeleteChannelFlowRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_flow

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_flow.delete_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.delete_channel_flow_request.DeleteChannelFlowRequest = {
            "channel_flow_arn": channel_flow_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_membership(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> None:
        """<p>Removes a member from a channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the <code>AppInstanceUserArn</code> of the user that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel from which you want to remove the user.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member that you're removing from the channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only for use by moderators.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.delete_channel_membership_request.DeleteChannelMembershipRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_membership

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_membership.delete_channel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.delete_channel_membership_request.DeleteChannelMembershipRequest = {
            "channel_arn": channel_arn,
            "member_arn": member_arn,
            "chime_bearer": chime_bearer,
        }
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_message(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "capo_chime_sdk_messaging.types.message_id.MessageId",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> None:
        """<p>Deletes a channel message. Only admins can perform this action. Deletion makes messages inaccessible immediately. A background process deletes any revisions created by <code>UpdateChannelMessage</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            message_id: <p>The ID of the message being deleted.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when deleting messages in a SubChannel that the user belongs to.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.delete_channel_message_request.DeleteChannelMessageRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_message

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_message.delete_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.delete_channel_message_request.DeleteChannelMessageRequest = {
            "channel_arn": channel_arn,
            "message_id": message_id,
            "chime_bearer": chime_bearer,
        }
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_moderator(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_moderator_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Deletes a channel moderator.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_moderator_arn: <p>The <code>AppInstanceUserArn</code> of the moderator being deleted.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.delete_channel_moderator_request.DeleteChannelModeratorRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_moderator

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_moderator.delete_channel_moderator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.delete_channel_moderator_request.DeleteChannelModeratorRequest = {
            "channel_arn": channel_arn,
            "channel_moderator_arn": channel_moderator_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_messaging_streaming_configurations(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Deletes the streaming configurations for an <code>AppInstance</code>. For more information, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html">Streaming messaging data</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>

        Args:
            app_instance_arn: <p>The ARN of the streaming configurations being deleted.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.delete_messaging_streaming_configurations_request.DeleteMessagingStreamingConfigurationsRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.delete_messaging_streaming_configurations

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.delete_messaging_streaming_configurations.delete_messaging_streaming_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.delete_messaging_streaming_configurations_request.DeleteMessagingStreamingConfigurationsRequest = {
            "app_instance_arn": app_instance_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.describe_channel_response.DescribeChannelResponse":
        """<p>Returns the full details of a channel in an Amazon Chime <code>AppInstance</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.describe_channel_request.DescribeChannelRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel.describe_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.describe_channel_request.DescribeChannelRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel_ban(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.describe_channel_ban_response.DescribeChannelBanResponse":
        """<p>Returns the full details of a channel ban.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel from which the user is banned.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member being banned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.describe_channel_ban_request.DescribeChannelBanRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.describe_channel_ban_response.DescribeChannelBanResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_ban

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_ban.describe_channel_ban(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.describe_channel_ban_request.DescribeChannelBanRequest = {
            "channel_arn": channel_arn,
            "member_arn": member_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel_flow(
        self,
        channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.describe_channel_flow_response.DescribeChannelFlowResponse":
        """<p>Returns the full details of a channel flow in an Amazon Chime <code>AppInstance</code>. This is a developer API.</p>

        Args:
            channel_flow_arn: <p>The ARN of the channel flow.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.describe_channel_flow_request.DescribeChannelFlowRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.describe_channel_flow_response.DescribeChannelFlowResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_flow

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_flow.describe_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.describe_channel_flow_request.DescribeChannelFlowRequest = {
            "channel_flow_arn": channel_flow_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel_membership(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.describe_channel_membership_response.DescribeChannelMembershipResponse":
        """<p>Returns the full details of a user's channel membership.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request. The response contains an <code>ElasticChannelConfiguration</code> object.</p> <note> <p>Only required to get a user’s SubChannel membership details.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.describe_channel_membership_request.DescribeChannelMembershipRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.describe_channel_membership_response.DescribeChannelMembershipResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_membership

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_membership.describe_channel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.describe_channel_membership_request.DescribeChannelMembershipRequest = {
            "channel_arn": channel_arn,
            "member_arn": member_arn,
            "chime_bearer": chime_bearer,
        }
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel_membership_for_app_instance_user(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        app_instance_user_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_response.DescribeChannelMembershipForAppInstanceUserResponse":
        """<p> Returns the details of a channel based on the membership of the specified <code>AppInstanceUser</code> or <code>AppInstanceBot</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel to which the user belongs.</p>
            app_instance_user_arn: <p>The ARN of the user or bot in a channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_request.DescribeChannelMembershipForAppInstanceUserRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_response.DescribeChannelMembershipForAppInstanceUserResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_membership_for_app_instance_user

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_membership_for_app_instance_user.describe_channel_membership_for_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_request.DescribeChannelMembershipForAppInstanceUserRequest = {
            "channel_arn": channel_arn,
            "app_instance_user_arn": app_instance_user_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel_moderated_by_app_instance_user(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        app_instance_user_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse":
        """<p>Returns the full details of a channel moderated by the specified <code>AppInstanceUser</code> or <code>AppInstanceBot</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the moderated channel.</p>
            app_instance_user_arn: <p>The ARN of the user or bot in the moderated channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request.DescribeChannelModeratedByAppInstanceUserRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_moderated_by_app_instance_user

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_moderated_by_app_instance_user.describe_channel_moderated_by_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request.DescribeChannelModeratedByAppInstanceUserRequest = {
            "channel_arn": channel_arn,
            "app_instance_user_arn": app_instance_user_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel_moderator(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_moderator_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.describe_channel_moderator_response.DescribeChannelModeratorResponse":
        """<p>Returns the full details of a single ChannelModerator.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the <code>AppInstanceUserArn</code> of the user that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_moderator_arn: <p>The <code>AppInstanceUserArn</code> of the channel moderator.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.describe_channel_moderator_request.DescribeChannelModeratorRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.describe_channel_moderator_response.DescribeChannelModeratorResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_moderator

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_moderator.describe_channel_moderator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.describe_channel_moderator_request.DescribeChannelModeratorRequest = {
            "channel_arn": channel_arn,
            "channel_moderator_arn": channel_moderator_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_channel_flow(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Disassociates a channel flow from all its channels. Once disassociated, all messages to that channel stop going through the channel flow processor.</p> <note> <p>Only administrators or channel moderators can disassociate a channel flow.</p> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_flow_arn: <p>The ARN of the channel flow.</p>
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.disassociate_channel_flow_request.DisassociateChannelFlowRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.disassociate_channel_flow

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.disassociate_channel_flow.disassociate_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.disassociate_channel_flow_request.DisassociateChannelFlowRequest = {
            "channel_arn": channel_arn,
            "channel_flow_arn": channel_flow_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel_membership_preferences(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.get_channel_membership_preferences_response.GetChannelMembershipPreferencesResponse":
        """<p>Gets the membership preferences of an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> for the specified channel. A user or a bot must be a member of the channel and own the membership in order to retrieve membership preferences. Users or bots in the <code>AppInstanceAdmin</code> and channel moderator roles can't retrieve preferences for other users or bots. Banned users or bots can't retrieve membership preferences for the channel from which they are banned.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member retrieving the preferences.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.get_channel_membership_preferences_request.GetChannelMembershipPreferencesRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.get_channel_membership_preferences_response.GetChannelMembershipPreferencesResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.get_channel_membership_preferences

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.get_channel_membership_preferences.get_channel_membership_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.get_channel_membership_preferences_request.GetChannelMembershipPreferencesRequest = {
            "channel_arn": channel_arn,
            "member_arn": member_arn,
            "chime_bearer": chime_bearer,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel_message(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "capo_chime_sdk_messaging.types.message_id.MessageId",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.get_channel_message_response.GetChannelMessageResponse":
        """<p>Gets the full details of a channel message.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            message_id: <p>The ID of the message.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting messages in a SubChannel that the user belongs to.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.get_channel_message_request.GetChannelMessageRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.get_channel_message_response.GetChannelMessageResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.get_channel_message

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.get_channel_message.get_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.get_channel_message_request.GetChannelMessageRequest = {
            "channel_arn": channel_arn,
            "message_id": message_id,
            "chime_bearer": chime_bearer,
        }
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel_message_status(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "capo_chime_sdk_messaging.types.message_id.MessageId",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.get_channel_message_status_response.GetChannelMessageStatusResponse":
        """<p>Gets message status for a specified <code>messageId</code>. Use this API to determine the intermediate status of messages going through channel flow processing. The API provides an alternative to retrieving message status if the event was not received because a client wasn't connected to a websocket. </p> <p>Messages can have any one of these statuses.</p> <dl> <dt>SENT</dt> <dd> <p>Message processed successfully</p> </dd> <dt>PENDING</dt> <dd> <p>Ongoing processing</p> </dd> <dt>FAILED</dt> <dd> <p>Processing failed</p> </dd> <dt>DENIED</dt> <dd> <p>Message denied by the processor</p> </dd> </dl> <note> <ul> <li> <p>This API does not return statuses for denied messages, because we don't store them once the processor denies them. </p> </li> <li> <p>Only the message sender can invoke this API.</p> </li> <li> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </li> </ul> </note>

        Args:
            channel_arn: <p>The ARN of the channel</p>
            message_id: <p>The ID of the message.</p>
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting message status in a SubChannel that the user belongs to.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.get_channel_message_status_request.GetChannelMessageStatusRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.get_channel_message_status_response.GetChannelMessageStatusResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.get_channel_message_status

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.get_channel_message_status.get_channel_message_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.get_channel_message_status_request.GetChannelMessageStatusRequest = {
            "channel_arn": channel_arn,
            "message_id": message_id,
            "chime_bearer": chime_bearer,
        }
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_messaging_session_endpoint(
        self,
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        network_type: Optional[
            "capo_chime_sdk_messaging.types.network_type.NetworkType"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.get_messaging_session_endpoint_response.GetMessagingSessionEndpointResponse":
        """<p>The details of the endpoint for the messaging session.</p>

        Args:
            network_type: <p>The type of network for the messaging session endpoint. Either IPv4 only or dual-stack (IPv4 and IPv6).</p>

        Raises:
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.get_messaging_session_endpoint_request.GetMessagingSessionEndpointRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.get_messaging_session_endpoint_response.GetMessagingSessionEndpointResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.get_messaging_session_endpoint

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.get_messaging_session_endpoint.get_messaging_session_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.get_messaging_session_endpoint_request.GetMessagingSessionEndpointRequest = {}
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_messaging_streaming_configurations(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.get_messaging_streaming_configurations_response.GetMessagingStreamingConfigurationsResponse":
        """<p>Retrieves the data streaming configuration for an <code>AppInstance</code>. For more information, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html">Streaming messaging data</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>

        Args:
            app_instance_arn: <p>The ARN of the streaming configurations.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.get_messaging_streaming_configurations_request.GetMessagingStreamingConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.get_messaging_streaming_configurations_response.GetMessagingStreamingConfigurationsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.get_messaging_streaming_configurations

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.get_messaging_streaming_configurations.get_messaging_streaming_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.get_messaging_streaming_configurations_request.GetMessagingStreamingConfigurationsRequest = {
            "app_instance_arn": app_instance_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_channel_bans(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channel_bans_response.ListChannelBansResponse":
        """<p>Lists all the users and bots banned from a particular channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            max_results: <p>The maximum number of bans that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested bans are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channel_bans_request.ListChannelBansRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channel_bans_response.ListChannelBansResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_bans

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_bans.list_channel_bans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channel_bans_request.ListChannelBansRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
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

    def iter_list_channel_bans(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channel_bans_response.ListChannelBansResponse]":
        _token = next_token
        while True:
            _response = self.list_channel_bans(
                channel_arn,
                chime_bearer,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channel_flows(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channel_flows_response.ListChannelFlowsResponse":
        """<p>Returns a paginated lists of all the channel flows created under a single Chime. This is a developer API.</p>

        Args:
            app_instance_arn: <p>The ARN of the app instance.</p>
            max_results: <p>The maximum number of channel flows that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested channel flows are returned.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channel_flows_request.ListChannelFlowsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channel_flows_response.ListChannelFlowsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_flows

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_flows.list_channel_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channel_flows_request.ListChannelFlowsRequest = {
            "app_instance_arn": app_instance_arn
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

    def iter_list_channel_flows(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channel_flows_response.ListChannelFlowsResponse]":
        _token = next_token
        while True:
            _response = self.list_channel_flows(
                app_instance_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channel_memberships(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        type: Optional[
            "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channel_memberships_response.ListChannelMembershipsResponse":
        """<p>Lists all channel memberships in a channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note> <p>If you want to list the channels to which a specific app instance user belongs, see the <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html">ListChannelMembershipsForAppInstanceUser</a> API.</p>

        Args:
            channel_arn: <p>The maximum number of channel memberships that you want returned.</p>
            type: <p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are returned as part of <code>ListChannelMemberships</code> if no type is specified. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>.</p>
            max_results: <p>The maximum number of channel memberships that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested channel memberships are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing a user's memberships in a particular sub-channel of an elastic channel.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channel_memberships_request.ListChannelMembershipsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channel_memberships_response.ListChannelMembershipsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_memberships

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_memberships.list_channel_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channel_memberships_request.ListChannelMembershipsRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
        }
        if type is not None:
            input_["type"] = type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_channel_memberships(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        type: Optional[
            "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channel_memberships_response.ListChannelMembershipsResponse]":
        _token = next_token
        while True:
            _response = self.list_channel_memberships(
                channel_arn,
                chime_bearer,
                config_overrides=config_overrides,
                type=type,
                max_results=max_results,
                next_token=_token,
                sub_channel_id=sub_channel_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channel_memberships_for_app_instance_user(
        self,
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        app_instance_user_arn: Optional[
            "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_response.ListChannelMembershipsForAppInstanceUserResponse":
        """<p> Lists all channels that an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> is a part of. Only an <code>AppInstanceAdmin</code> can call the API with a user ARN that is not their own. </p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            app_instance_user_arn: <p>The ARN of the user or bot.</p>
            max_results: <p>The maximum number of users that you want returned.</p>
            next_token: <p>The token returned from previous API requests until the number of channel memberships is reached.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_request.ListChannelMembershipsForAppInstanceUserRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_response.ListChannelMembershipsForAppInstanceUserResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_memberships_for_app_instance_user

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_memberships_for_app_instance_user.list_channel_memberships_for_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_request.ListChannelMembershipsForAppInstanceUserRequest = {
            "chime_bearer": chime_bearer
        }
        if app_instance_user_arn is not None:
            input_["app_instance_user_arn"] = app_instance_user_arn
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

    def iter_list_channel_memberships_for_app_instance_user(
        self,
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        app_instance_user_arn: Optional[
            "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_response.ListChannelMembershipsForAppInstanceUserResponse]":
        _token = next_token
        while True:
            _response = self.list_channel_memberships_for_app_instance_user(
                chime_bearer,
                config_overrides=config_overrides,
                app_instance_user_arn=app_instance_user_arn,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channel_messages(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sort_order: Optional[
            "capo_chime_sdk_messaging.types.sort_order.SortOrder"
        ] = None,
        not_before: Optional[
            "capo_chime_sdk_messaging.types.timestamp.Timestamp"
        ] = None,
        not_after: Optional[
            "capo_chime_sdk_messaging.types.timestamp.Timestamp"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channel_messages_response.ListChannelMessagesResponse":
        """<p>List all the messages in a channel. Returns a paginated list of <code>ChannelMessages</code>. By default, sorted by creation timestamp in descending order.</p> <note> <p>Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.</p> <p>Also, the <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            sort_order: <p>The order in which you want messages sorted. Default is Descending, based on time created.</p>
            not_before: <p>The initial or starting time stamp for your requested messages.</p>
            not_after: <p>The final or ending time stamp for your requested messages.</p>
            max_results: <p>The maximum number of messages that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested messages are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing the messages in a SubChannel that the user belongs to.</p> </note>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channel_messages_request.ListChannelMessagesRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channel_messages_response.ListChannelMessagesResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_messages

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_messages.list_channel_messages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channel_messages_request.ListChannelMessagesRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
        }
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if not_before is not None:
            input_["not_before"] = not_before
        if not_after is not None:
            input_["not_after"] = not_after
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_channel_messages(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sort_order: Optional[
            "capo_chime_sdk_messaging.types.sort_order.SortOrder"
        ] = None,
        not_before: Optional[
            "capo_chime_sdk_messaging.types.timestamp.Timestamp"
        ] = None,
        not_after: Optional[
            "capo_chime_sdk_messaging.types.timestamp.Timestamp"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channel_messages_response.ListChannelMessagesResponse]":
        _token = next_token
        while True:
            _response = self.list_channel_messages(
                channel_arn,
                chime_bearer,
                config_overrides=config_overrides,
                sort_order=sort_order,
                not_before=not_before,
                not_after=not_after,
                max_results=max_results,
                next_token=_token,
                sub_channel_id=sub_channel_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channel_moderators(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channel_moderators_response.ListChannelModeratorsResponse":
        """<p>Lists all the moderators for a channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            max_results: <p>The maximum number of moderators that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested moderators are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channel_moderators_request.ListChannelModeratorsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channel_moderators_response.ListChannelModeratorsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_moderators

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channel_moderators.list_channel_moderators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channel_moderators_request.ListChannelModeratorsRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
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

    def iter_list_channel_moderators(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channel_moderators_response.ListChannelModeratorsResponse]":
        _token = next_token
        while True:
            _response = self.list_channel_moderators(
                channel_arn,
                chime_bearer,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channels(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        privacy: Optional[
            "capo_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channels_response.ListChannelsResponse":
        """<p>Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.</p> <p class="title"> <b>Functionality & restrictions</b> </p> <ul> <li> <p>Use privacy = <code>PUBLIC</code> to retrieve all public channels in the account.</p> </li> <li> <p>Only an <code>AppInstanceAdmin</code> can set privacy = <code>PRIVATE</code> to list the private channels in an account.</p> </li> </ul> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            privacy: <p>The privacy setting. <code>PUBLIC</code> retrieves all the public channels. <code>PRIVATE</code> retrieves private channels. Only an <code>AppInstanceAdmin</code> can retrieve private channels. </p>
            max_results: <p>The maximum number of channels that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested channels are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channels

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channels_request.ListChannelsRequest = {
            "app_instance_arn": app_instance_arn,
            "chime_bearer": chime_bearer,
        }
        if privacy is not None:
            input_["privacy"] = privacy
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

    def iter_list_channels(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        privacy: Optional[
            "capo_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channels_response.ListChannelsResponse]":
        _token = next_token
        while True:
            _response = self.list_channels(
                app_instance_arn,
                chime_bearer,
                config_overrides=config_overrides,
                privacy=privacy,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channels_associated_with_channel_flow(
        self,
        channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_response.ListChannelsAssociatedWithChannelFlowResponse":
        """<p>Lists all channels associated with a specified channel flow. You can associate a channel flow with multiple channels, but you can only associate a channel with one channel flow. This is a developer API.</p>

        Args:
            channel_flow_arn: <p>The ARN of the channel flow.</p>
            max_results: <p>The maximum number of channels that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested channels are returned.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_request.ListChannelsAssociatedWithChannelFlowRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_response.ListChannelsAssociatedWithChannelFlowResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channels_associated_with_channel_flow

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channels_associated_with_channel_flow.list_channels_associated_with_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_request.ListChannelsAssociatedWithChannelFlowRequest = {
            "channel_flow_arn": channel_flow_arn
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

    def iter_list_channels_associated_with_channel_flow(
        self,
        channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_response.ListChannelsAssociatedWithChannelFlowResponse]":
        _token = next_token
        while True:
            _response = self.list_channels_associated_with_channel_flow(
                channel_flow_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channels_moderated_by_app_instance_user(
        self,
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        app_instance_user_arn: Optional[
            "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_response.ListChannelsModeratedByAppInstanceUserResponse":
        """<p>A list of the channels moderated by an <code>AppInstanceUser</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            app_instance_user_arn: <p>The ARN of the user or bot in the moderated channel.</p>
            max_results: <p>The maximum number of channels in the request.</p>
            next_token: <p>The token returned from previous API requests until the number of channels moderated by the user is reached.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_request.ListChannelsModeratedByAppInstanceUserRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_response.ListChannelsModeratedByAppInstanceUserResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_channels_moderated_by_app_instance_user

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_channels_moderated_by_app_instance_user.list_channels_moderated_by_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_request.ListChannelsModeratedByAppInstanceUserRequest = {
            "chime_bearer": chime_bearer
        }
        if app_instance_user_arn is not None:
            input_["app_instance_user_arn"] = app_instance_user_arn
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

    def iter_list_channels_moderated_by_app_instance_user(
        self,
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        app_instance_user_arn: Optional[
            "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_response.ListChannelsModeratedByAppInstanceUserResponse]":
        _token = next_token
        while True:
            _response = self.list_channels_moderated_by_app_instance_user(
                chime_bearer,
                config_overrides=config_overrides,
                app_instance_user_arn=app_instance_user_arn,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sub_channels(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.list_sub_channels_response.ListSubChannelsResponse":
        """<p>Lists all the SubChannels in an elastic channel when given a channel ID. Available only to the app instance admins and channel moderators of elastic channels.</p>

        Args:
            channel_arn: <p>The ARN of elastic channel.</p>
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>
            max_results: <p>The maximum number of sub-channels that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested sub-channels are returned.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_sub_channels_request.ListSubChannelsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_sub_channels_response.ListSubChannelsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_sub_channels

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_sub_channels.list_sub_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_sub_channels_request.ListSubChannelsRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
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

    def iter_list_sub_channels(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.list_sub_channels_response.ListSubChannelsResponse]":
        _token = next_token
        while True:
            _response = self.list_sub_channels(
                channel_arn,
                chime_bearer,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags applied to an Amazon Chime SDK messaging resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.list_tags_for_resource

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_channel_expiration_settings(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        chime_bearer: Optional[
            "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        expiration_settings: Optional[
            "capo_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.put_channel_expiration_settings_response.PutChannelExpirationSettingsResponse":
        """<p>Sets the number of days before the channel is automatically deleted.</p> <note> <ul> <li> <p>A background process deletes expired channels within 6 hours of expiration. Actual deletion times may vary.</p> </li> <li> <p>Expired channels that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.</p> </li> <li> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </li> </ul> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            expiration_settings: <p>Settings that control the interval after which a channel is deleted.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.put_channel_expiration_settings_request.PutChannelExpirationSettingsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.put_channel_expiration_settings_response.PutChannelExpirationSettingsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.put_channel_expiration_settings

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.put_channel_expiration_settings.put_channel_expiration_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.put_channel_expiration_settings_request.PutChannelExpirationSettingsRequest = {
            "channel_arn": channel_arn
        }
        if chime_bearer is not None:
            input_["chime_bearer"] = chime_bearer
        if expiration_settings is not None:
            input_["expiration_settings"] = expiration_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_channel_membership_preferences(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        preferences: "capo_chime_sdk_messaging.types.channel_membership_preferences.ChannelMembershipPreferences",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.put_channel_membership_preferences_response.PutChannelMembershipPreferencesResponse":
        """<p>Sets the membership preferences of an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> for the specified channel. The user or bot must be a member of the channel. Only the user or bot who owns the membership can set preferences. Users or bots in the <code>AppInstanceAdmin</code> and channel moderator roles can't set preferences for other users. Banned users or bots can't set membership preferences for the channel from which they are banned.</p> <note> <p>The x-amz-chime-bearer request header is mandatory. Use the ARN of an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            member_arn: <p>The ARN of the member setting the preferences.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            preferences: <p>The channel membership preferences of an <code>AppInstanceUser</code> .</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.put_channel_membership_preferences_request.PutChannelMembershipPreferencesRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.put_channel_membership_preferences_response.PutChannelMembershipPreferencesResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.put_channel_membership_preferences

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.put_channel_membership_preferences.put_channel_membership_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.put_channel_membership_preferences_request.PutChannelMembershipPreferencesRequest = {
            "channel_arn": channel_arn,
            "member_arn": member_arn,
            "chime_bearer": chime_bearer,
            "preferences": preferences,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_messaging_streaming_configurations(
        self,
        app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        streaming_configurations: "capo_chime_sdk_messaging.types.streaming_configuration_list.StreamingConfigurationList",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.put_messaging_streaming_configurations_response.PutMessagingStreamingConfigurationsResponse":
        """<p>Sets the data streaming configuration for an <code>AppInstance</code>. For more information, see <a href="https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html">Streaming messaging data</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>

        Args:
            app_instance_arn: <p>The ARN of the streaming configuration.</p>
            streaming_configurations: <p>The streaming configurations.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.put_messaging_streaming_configurations_request.PutMessagingStreamingConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.put_messaging_streaming_configurations_response.PutMessagingStreamingConfigurationsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.put_messaging_streaming_configurations

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.put_messaging_streaming_configurations.put_messaging_streaming_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.put_messaging_streaming_configurations_request.PutMessagingStreamingConfigurationsRequest = {
            "app_instance_arn": app_instance_arn,
            "streaming_configurations": streaming_configurations,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def redact_channel_message(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "capo_chime_sdk_messaging.types.message_id.MessageId",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.redact_channel_message_response.RedactChannelMessageResponse":
        """<p>Redacts message content and metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel containing the messages that you want to redact.</p>
            message_id: <p>The ID of the message being redacted.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.redact_channel_message_request.RedactChannelMessageRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.redact_channel_message_response.RedactChannelMessageResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.redact_channel_message

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.redact_channel_message.redact_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.redact_channel_message_request.RedactChannelMessageRequest = {
            "channel_arn": channel_arn,
            "message_id": message_id,
            "chime_bearer": chime_bearer,
        }
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_channels(
        self,
        fields: "capo_chime_sdk_messaging.types.search_fields.SearchFields",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        chime_bearer: Optional[
            "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> (
        "capo_chime_sdk_messaging.types.search_channels_response.SearchChannelsResponse"
    ):
        """<p>Allows the <code>ChimeBearer</code> to search channels by channel members. Users or bots can search across the channels that they belong to. Users in the <code>AppInstanceAdmin</code> role can search across all channels.</p> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> <note> <p>This operation isn't supported for <code>AppInstanceUsers</code> with a large number of memberships.</p> </note>

        Args:
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>
            fields: <p>A list of the <code>Field</code> objects in the channel being searched.</p>
            max_results: <p>The maximum number of channels that you want returned.</p>
            next_token: <p>The token returned from previous API requests until the number of channels is reached.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.search_channels_request.SearchChannelsRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.search_channels_response.SearchChannelsResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.search_channels

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.search_channels.search_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.search_channels_request.SearchChannelsRequest = {
            "fields": fields
        }
        if chime_bearer is not None:
            input_["chime_bearer"] = chime_bearer
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

    def iter_search_channels(
        self,
        fields: "capo_chime_sdk_messaging.types.search_fields.SearchFields",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        chime_bearer: Optional[
            "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "capo_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_chime_sdk_messaging.types.search_channels_response.SearchChannelsResponse]":
        _token = next_token
        while True:
            _response = self.search_channels(
                fields,
                config_overrides=config_overrides,
                chime_bearer=chime_bearer,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def send_channel_message(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        content: "capo_chime_sdk_messaging.types.non_empty_content.NonEmptyContent",
        type: "capo_chime_sdk_messaging.types.channel_message_type.ChannelMessageType",
        persistence: "capo_chime_sdk_messaging.types.channel_message_persistence_type.ChannelMessagePersistenceType",
        client_request_token: "capo_chime_sdk_messaging.types.client_request_token.ClientRequestToken",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        metadata: Optional["capo_chime_sdk_messaging.types.metadata.Metadata"] = None,
        push_notification: Optional[
            "capo_chime_sdk_messaging.types.push_notification_configuration.PushNotificationConfiguration"
        ] = None,
        message_attributes: Optional[
            "capo_chime_sdk_messaging.types.message_attribute_map.MessageAttributeMap"
        ] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
        content_type: Optional[
            "capo_chime_sdk_messaging.types.content_type.ContentType"
        ] = None,
        target: Optional[
            "capo_chime_sdk_messaging.types.target_list.TargetList"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.send_channel_message_response.SendChannelMessageResponse":
        """<p>Sends a message to a particular channel that the member is a part of.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> <p>Also, <code>STANDARD</code> messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.</p> <p> <code>CONTROL</code> messages are limited to 30 bytes and do not contain metadata.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            content: <p>The content of the channel message.</p>
            type: <p>The type of message, <code>STANDARD</code> or <code>CONTROL</code>.</p> <p> <code>STANDARD</code> messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.</p> <p> <code>CONTROL</code> messages are limited to 30 bytes and do not contain metadata.</p>
            persistence: <p>Boolean that controls whether the message is persisted on the back end. Required.</p>
            metadata: <p>The optional metadata for each message.</p>
            client_request_token: <p>The <code>Idempotency</code> token for each client request.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            push_notification: <p>The push notification configuration of the message.</p>
            message_attributes: <p>The attributes for the message, used for message filtering along with a <code>FilterRule</code> defined in the <code>PushNotificationPreferences</code>.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p>
            content_type: <p>The content type of the channel message.</p>
            target: <p>The target of a message. Must be a member of the channel, such as another user, a bot, or the sender. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see. </p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.send_channel_message_request.SendChannelMessageRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.send_channel_message_response.SendChannelMessageResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.send_channel_message

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.send_channel_message.send_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.send_channel_message_request.SendChannelMessageRequest = {
            "channel_arn": channel_arn,
            "content": content,
            "type": type,
            "persistence": persistence,
            "client_request_token": client_request_token,
            "chime_bearer": chime_bearer,
        }
        if metadata is not None:
            input_["metadata"] = metadata
        if push_notification is not None:
            input_["push_notification"] = push_notification
        if message_attributes is not None:
            input_["message_attributes"] = message_attributes
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id
        if content_type is not None:
            input_["content_type"] = content_type
        if target is not None:
            input_["target"] = target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        tags: "capo_chime_sdk_messaging.types.tag_list.TagList",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Applies the specified tags to the specified Amazon Chime SDK messaging resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tags: <p>The tag key-value pairs.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>The request exceeds the resource limit.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.tag_resource

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        tag_keys: "capo_chime_sdk_messaging.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Removes the specified tags from the specified Amazon Chime SDK messaging resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.untag_resource

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        name: Optional[
            "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
        ] = None,
        mode: Optional[
            "capo_chime_sdk_messaging.types.channel_mode.ChannelMode"
        ] = None,
        metadata: Optional["capo_chime_sdk_messaging.types.metadata.Metadata"] = None,
    ) -> "capo_chime_sdk_messaging.types.update_channel_response.UpdateChannelResponse":
        """<p>Update a channel's attributes.</p> <p> <b>Restriction</b>: You can't change a channel's privacy. </p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            name: <p>The name of the channel.</p>
            mode: <p>The mode of the update request.</p>
            metadata: <p>The metadata for the update request.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.update_channel

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.update_channel_request.UpdateChannelRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
        }
        if name is not None:
            input_["name"] = name
        if mode is not None:
            input_["mode"] = mode
        if metadata is not None:
            input_["metadata"] = metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel_flow(
        self,
        channel_flow_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        processors: "capo_chime_sdk_messaging.types.processor_list.ProcessorList",
        name: "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.update_channel_flow_response.UpdateChannelFlowResponse":
        """<p>Updates channel flow attributes. This is a developer API.</p>

        Args:
            channel_flow_arn: <p>The ARN of the channel flow.</p>
            processors: <p>Information about the processor Lambda functions </p>
            name: <p>The name of the channel flow.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.update_channel_flow_request.UpdateChannelFlowRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.update_channel_flow_response.UpdateChannelFlowResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.update_channel_flow

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.update_channel_flow.update_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.update_channel_flow_request.UpdateChannelFlowRequest = {
            "channel_flow_arn": channel_flow_arn,
            "processors": processors,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel_message(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "capo_chime_sdk_messaging.types.message_id.MessageId",
        content: "capo_chime_sdk_messaging.types.non_empty_content.NonEmptyContent",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        metadata: Optional["capo_chime_sdk_messaging.types.metadata.Metadata"] = None,
        sub_channel_id: Optional[
            "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
        content_type: Optional[
            "capo_chime_sdk_messaging.types.content_type.ContentType"
        ] = None,
    ) -> "capo_chime_sdk_messaging.types.update_channel_message_response.UpdateChannelMessageResponse":
        """<p>Updates the content of a message.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            message_id: <p>The ID string of the message being updated.</p>
            content: <p>The content of the channel message. </p>
            metadata: <p>The metadata of the message being updated.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when updating messages in a SubChannel that the user belongs to.</p> </note>
            content_type: <p>The content type of the channel message.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.update_channel_message_request.UpdateChannelMessageRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.update_channel_message_response.UpdateChannelMessageResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.update_channel_message

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.update_channel_message.update_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.update_channel_message_request.UpdateChannelMessageRequest = {
            "channel_arn": channel_arn,
            "message_id": message_id,
            "content": content,
            "chime_bearer": chime_bearer,
        }
        if metadata is not None:
            input_["metadata"] = metadata
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id
        if content_type is not None:
            input_["content_type"] = content_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel_read_marker(
        self,
        channel_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "capo_chime_sdk_messaging.types.update_channel_read_marker_response.UpdateChannelReadMarkerResponse":
        """<p>The details of the time when a user last read messages in a channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>

        Raises:
            capo_chime_sdk_messaging.errors.bad_request_exception.BadRequestException: <p>The input parameters don't match the service's restrictions.</p>
            capo_chime_sdk_messaging.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_chime_sdk_messaging.errors.forbidden_exception.ForbiddenException: <p>The client is permanently forbidden from making the request.</p>
            capo_chime_sdk_messaging.errors.service_failure_exception.ServiceFailureException: <p>The service encountered an unexpected error.</p>
            capo_chime_sdk_messaging.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable.</p>
            capo_chime_sdk_messaging.errors.throttled_client_exception.ThrottledClientException: <p>The client exceeded its request rate limit.</p>
            capo_chime_sdk_messaging.errors.unauthorized_client_exception.UnauthorizedClientException: <p>The client is not currently authorized to make the request.</p>
            capo_chime_sdk_messaging.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_chime_sdk_messaging.types.update_channel_read_marker_request.UpdateChannelReadMarkerRequest]",
        ) -> OperationResponse[
            "capo_chime_sdk_messaging.types.update_channel_read_marker_response.UpdateChannelReadMarkerResponse"
        ]:
            import capo_chime_sdk_messaging._operations.chime_messaging_service.update_channel_read_marker

            output, http_response = (
                capo_chime_sdk_messaging._operations.chime_messaging_service.update_channel_read_marker.update_channel_read_marker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_chime_sdk_messaging.types.update_channel_read_marker_request.UpdateChannelReadMarkerRequest = {
            "channel_arn": channel_arn,
            "chime_bearer": chime_bearer,
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
