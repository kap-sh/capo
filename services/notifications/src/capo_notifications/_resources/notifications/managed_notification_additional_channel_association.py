from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_notifications._auth._signers
import capo_notifications._auth._sigv4
from capo_notifications._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_notifications.types.associate_managed_notification_additional_channel_request
    import capo_notifications.types.associate_managed_notification_additional_channel_response
    import capo_notifications.types.channel_arn
    import capo_notifications.types.disassociate_managed_notification_additional_channel_request
    import capo_notifications.types.disassociate_managed_notification_additional_channel_response
    import capo_notifications.types.managed_notification_configuration_os_arn
    from capo_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from capo_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class ManagedNotificationAdditionalChannelAssociation:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self,
        channel_arn: "capo_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        is_sensitive_events_subscribed: Optional[bool] = None,
    ) -> "capo_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse":
        """<p>Associates an additional Channel with a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and email (notifications-contacts).</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the additional Channel.</p>
            is_sensitive_events_subscribed: <p>Specifies whether this channel is subscribed to sensitive events. The <code>notifications:SubscribeSensitiveEvents</code> permission controls access to sensitive events. Defaults to false.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse"
        ]:
            import capo_notifications._operations.notifications.associate_managed_notification_additional_channel

            output, http_response = (
                capo_notifications._operations.notifications.associate_managed_notification_additional_channel.associate_managed_notification_additional_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("AssociateManagedNotificationAdditionalChannel"),
        )
        input_: capo_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest = {
            "channel_arn": channel_arn,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }
        if is_sensitive_events_subscribed is not None:
            input_["is_sensitive_events_subscribed"] = is_sensitive_events_subscribed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        channel_arn: "capo_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse":
        """<p>Disassociates an additional Channel from a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the Managed Notification Configuration to associate with the additional Channel.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_managed_notification_additional_channel

            output, http_response = (
                capo_notifications._operations.notifications.disassociate_managed_notification_additional_channel.disassociate_managed_notification_additional_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisassociateManagedNotificationAdditionalChannel"),
        )
        input_: capo_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest = {
            "channel_arn": channel_arn,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncManagedNotificationAdditionalChannelAssociation:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self,
        channel_arn: "capo_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        is_sensitive_events_subscribed: Optional[bool] = None,
    ) -> "capo_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse":
        """<p>Associates an additional Channel with a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and email (notifications-contacts).</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to associate with the additional Channel.</p>
            is_sensitive_events_subscribed: <p>Specifies whether this channel is subscribed to sensitive events. The <code>notifications:SubscribeSensitiveEvents</code> permission controls access to sensitive events. Defaults to false.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.associate_managed_notification_additional_channel_response.AssociateManagedNotificationAdditionalChannelResponse"
        ]:
            import capo_notifications._operations.notifications.associate_managed_notification_additional_channel

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.associate_managed_notification_additional_channel.async_associate_managed_notification_additional_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("AssociateManagedNotificationAdditionalChannel"),
        )
        input_: capo_notifications.types.associate_managed_notification_additional_channel_request.AssociateManagedNotificationAdditionalChannelRequest = {
            "channel_arn": channel_arn,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }
        if is_sensitive_events_subscribed is not None:
            input_["is_sensitive_events_subscribed"] = is_sensitive_events_subscribed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        channel_arn: "capo_notifications.types.channel_arn.ChannelArn",
        managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse":
        """<p>Disassociates an additional Channel from a particular <code>ManagedNotificationConfiguration</code>.</p> <p>Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            channel_arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p>
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the Managed Notification Configuration to associate with the additional Channel.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.disassociate_managed_notification_additional_channel_response.DisassociateManagedNotificationAdditionalChannelResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_managed_notification_additional_channel

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.disassociate_managed_notification_additional_channel.async_disassociate_managed_notification_additional_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DisassociateManagedNotificationAdditionalChannel"),
        )
        input_: capo_notifications.types.disassociate_managed_notification_additional_channel_request.DisassociateManagedNotificationAdditionalChannelRequest = {
            "channel_arn": channel_arn,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
