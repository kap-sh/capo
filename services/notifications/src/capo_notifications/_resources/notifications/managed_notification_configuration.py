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
    import capo_notifications.types.channel_identifier
    import capo_notifications.types.get_managed_notification_configuration_request
    import capo_notifications.types.get_managed_notification_configuration_response
    import capo_notifications.types.list_managed_notification_configurations_request
    import capo_notifications.types.list_managed_notification_configurations_response
    import capo_notifications.types.managed_notification_configuration_os_arn
    import capo_notifications.types.managed_notification_configuration_structure
    import capo_notifications.types.next_token
    from capo_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from capo_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class ManagedNotificationConfiguration:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def read(
        self,
        arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse":
        """<p>Returns a specified <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to return.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.get_managed_notification_configuration

            output, http_response = (
                capo_notifications._operations.notifications.get_managed_notification_configuration.get_managed_notification_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetManagedNotificationConfiguration")
        )
        input_: capo_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest = {
            "arn": arn
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
        config_overrides: Optional[NotificationsClientConfig] = None,
        channel_identifier: Optional[
            "capo_notifications.types.channel_identifier.ChannelIdentifier"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse":
        """<p>Returns a list of Managed Notification Configurations according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            channel_identifier: <p>The identifier or ARN of the notification channel to filter configurations by.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse"
        ]:
            import capo_notifications._operations.notifications.list_managed_notification_configurations

            output, http_response = (
                capo_notifications._operations.notifications.list_managed_notification_configurations.list_managed_notification_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListManagedNotificationConfigurations")
        )
        input_: capo_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest = {}
        if channel_identifier is not None:
            input_["channel_identifier"] = channel_identifier
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


class AsyncManagedNotificationConfiguration:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def read(
        self,
        arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "capo_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse":
        """<p>Returns a specified <code>ManagedNotificationConfiguration</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to return.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.get_managed_notification_configuration_response.GetManagedNotificationConfigurationResponse"
        ]:
            import capo_notifications._operations.notifications.get_managed_notification_configuration

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.get_managed_notification_configuration.async_get_managed_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetManagedNotificationConfiguration")
        )
        input_: capo_notifications.types.get_managed_notification_configuration_request.GetManagedNotificationConfigurationRequest = {
            "arn": arn
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
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        channel_identifier: Optional[
            "capo_notifications.types.channel_identifier.ChannelIdentifier"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse":
        """<p>Returns a list of Managed Notification Configurations according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            channel_identifier: <p>The identifier or ARN of the notification channel to filter configurations by.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.list_managed_notification_configurations_response.ListManagedNotificationConfigurationsResponse"
        ]:
            import capo_notifications._operations.notifications.list_managed_notification_configurations

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.list_managed_notification_configurations.async_list_managed_notification_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListManagedNotificationConfigurations")
        )
        input_: capo_notifications.types.list_managed_notification_configurations_request.ListManagedNotificationConfigurationsRequest = {}
        if channel_identifier is not None:
            input_["channel_identifier"] = channel_identifier
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
