from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_notifications._auth._signers
import capo_notifications._auth._sigv4
from capo_notifications._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_notifications.types.associate_channel_request
    import capo_notifications.types.associate_channel_response
    import capo_notifications.types.channel_arn
    import capo_notifications.types.disassociate_channel_request
    import capo_notifications.types.disassociate_channel_response
    import capo_notifications.types.list_channels_request
    import capo_notifications.types.list_channels_response
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_configuration_arn
    from capo_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from capo_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class Channel:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self,
        arn: "capo_notifications.types.channel_arn.ChannelArn",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.associate_channel_response.AssociateChannelResponse":
        """<p>Associates a delivery <a href="https://docs.aws.amazon.com/notifications/latest/userguide/managing-delivery-channels.html">Channel</a> with a particular <code>NotificationConfiguration</code>. Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>NotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and notifications-contacts.</p>
            notification_configuration_arn: <p>The ARN of the <code>NotificationConfiguration</code> to associate with the Channel.</p>

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
            req: "OperationRequest[capo_notifications.types.associate_channel_request.AssociateChannelRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.associate_channel_response.AssociateChannelResponse"
        ]:
            import capo_notifications._operations.notifications.associate_channel

            output, http_response = (
                capo_notifications._operations.notifications.associate_channel.associate_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.associate_channel_request.AssociateChannelRequest = {
            "arn": arn,
            "notification_configuration_arn": notification_configuration_arn,
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
        arn: "capo_notifications.types.channel_arn.ChannelArn",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_channel_response.DisassociateChannelResponse":
        """<p>Disassociates a Channel from a specified <code>NotificationConfiguration</code>. Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Channel to disassociate.</p>
            notification_configuration_arn: <p>The ARN of the <code>NotificationConfiguration</code> to disassociate.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.disassociate_channel_request.DisassociateChannelRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.disassociate_channel_response.DisassociateChannelResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_channel

            output, http_response = (
                capo_notifications._operations.notifications.disassociate_channel.disassociate_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.disassociate_channel_request.DisassociateChannelRequest = {
            "arn": arn,
            "notification_configuration_arn": notification_configuration_arn,
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
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_channels_response.ListChannelsResponse":
        """<p>Returns a list of Channels for a <code>NotificationConfiguration</code>.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>
            max_results: <p>The maximum number of results to be returned in this call. The default value is 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListNotificationEvents call. <code>NextToken</code> uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_notifications._operations.notifications.list_channels

            output, http_response = (
                capo_notifications._operations.notifications.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.list_channels_request.ListChannelsRequest = {
            "notification_configuration_arn": notification_configuration_arn
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


class AsyncChannel:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self,
        arn: "capo_notifications.types.channel_arn.ChannelArn",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "capo_notifications.types.associate_channel_response.AssociateChannelResponse":
        """<p>Associates a delivery <a href="https://docs.aws.amazon.com/notifications/latest/userguide/managing-delivery-channels.html">Channel</a> with a particular <code>NotificationConfiguration</code>. Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>NotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and notifications-contacts.</p>
            notification_configuration_arn: <p>The ARN of the <code>NotificationConfiguration</code> to associate with the Channel.</p>

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
            req: "AsyncOperationRequest[capo_notifications.types.associate_channel_request.AssociateChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.associate_channel_response.AssociateChannelResponse"
        ]:
            import capo_notifications._operations.notifications.associate_channel

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.associate_channel.async_associate_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.associate_channel_request.AssociateChannelRequest = {
            "arn": arn,
            "notification_configuration_arn": notification_configuration_arn,
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
        arn: "capo_notifications.types.channel_arn.ChannelArn",
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "capo_notifications.types.disassociate_channel_response.DisassociateChannelResponse":
        """<p>Disassociates a Channel from a specified <code>NotificationConfiguration</code>. Supported Channels include Amazon Q Developer in chat applications, the Console Mobile Application, and emails (notifications-contacts).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Channel to disassociate.</p>
            notification_configuration_arn: <p>The ARN of the <code>NotificationConfiguration</code> to disassociate.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.disassociate_channel_request.DisassociateChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.disassociate_channel_response.DisassociateChannelResponse"
        ]:
            import capo_notifications._operations.notifications.disassociate_channel

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.disassociate_channel.async_disassociate_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.disassociate_channel_request.DisassociateChannelRequest = {
            "arn": arn,
            "notification_configuration_arn": notification_configuration_arn,
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
        notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_channels_response.ListChannelsResponse":
        """<p>Returns a list of Channels for a <code>NotificationConfiguration</code>.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>
            max_results: <p>The maximum number of results to be returned in this call. The default value is 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListNotificationEvents call. <code>NextToken</code> uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.list_channels_request.ListChannelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_notifications._operations.notifications.list_channels

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.list_channels.async_list_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.list_channels_request.ListChannelsRequest = {
            "notification_configuration_arn": notification_configuration_arn
        }
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
