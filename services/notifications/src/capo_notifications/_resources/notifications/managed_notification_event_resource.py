from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Any, Optional

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
    import capo_notifications.types.account_id
    import capo_notifications.types.get_managed_notification_event_request
    import capo_notifications.types.get_managed_notification_event_response
    import capo_notifications.types.list_managed_notification_events_request
    import capo_notifications.types.list_managed_notification_events_response
    import capo_notifications.types.locale_code
    import capo_notifications.types.managed_notification_event_arn
    import capo_notifications.types.managed_notification_event_overview
    import capo_notifications.types.next_token
    import capo_notifications.types.organizational_unit_id
    import capo_notifications.types.source
    from capo_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from capo_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class ManagedNotificationEventResource:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def read(
        self,
        arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "capo_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse":
        """<p>Returns a specified <code>ManagedNotificationEvent</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>ManagedNotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse"
        ]:
            import capo_notifications._operations.notifications.get_managed_notification_event

            output, http_response = (
                capo_notifications._operations.notifications.get_managed_notification_event.get_managed_notification_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse",
        ) -> dict[str, Any]:
            import capo_notifications.types.get_managed_notification_event_response

            return capo_notifications.types.get_managed_notification_event_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetManagedNotificationEvent", redact_output=_redact_output
            ),
        )
        input_: capo_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest = {
            "arn": arn
        }
        if locale is not None:
            input_["locale"] = locale

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
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
        source: Optional["capo_notifications.types.source.Source"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
        related_account: Optional[
            "capo_notifications.types.account_id.AccountId"
        ] = None,
        include_sensitive_events: Optional[bool] = None,
    ) -> "capo_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse":
        """<p>Returns a list of Managed Notification Events according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved NotificationEvent. The default locale is English (en_US).</p>
            source: <p>The Amazon Web Services service the event originates from. For example aws.cloudwatch.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call. Next token uses Base64 encoding.</p>
            organizational_unit_id: <p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>
            related_account: <p>The Amazon Web Services account ID associated with the Managed Notification Events.</p>
            include_sensitive_events: <p>Specifies whether to include sensitive events in the result. By default, only non-sensitive events are returned. The <code>notifications:AccessSensitiveEvents</code> permission controls access to sensitive events.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse"
        ]:
            import capo_notifications._operations.notifications.list_managed_notification_events

            output, http_response = (
                capo_notifications._operations.notifications.list_managed_notification_events.list_managed_notification_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListManagedNotificationEvents")
        )
        input_: capo_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest = {}
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if source is not None:
            input_["source"] = source
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id
        if related_account is not None:
            input_["related_account"] = related_account
        if include_sensitive_events is not None:
            input_["include_sensitive_events"] = include_sensitive_events

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncManagedNotificationEventResource:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def read(
        self,
        arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "capo_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse":
        """<p>Returns a specified <code>ManagedNotificationEvent</code>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>ManagedNotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse"
        ]:
            import capo_notifications._operations.notifications.get_managed_notification_event

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.get_managed_notification_event.async_get_managed_notification_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_notifications.types.get_managed_notification_event_response.GetManagedNotificationEventResponse",
        ) -> dict[str, Any]:
            import capo_notifications.types.get_managed_notification_event_response

            return capo_notifications.types.get_managed_notification_event_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "GetManagedNotificationEvent", redact_output=_redact_output
            ),
        )
        input_: capo_notifications.types.get_managed_notification_event_request.GetManagedNotificationEventRequest = {
            "arn": arn
        }
        if locale is not None:
            input_["locale"] = locale

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
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
        source: Optional["capo_notifications.types.source.Source"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
        related_account: Optional[
            "capo_notifications.types.account_id.AccountId"
        ] = None,
        include_sensitive_events: Optional[bool] = None,
    ) -> "capo_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse":
        """<p>Returns a list of Managed Notification Events according to specified filters, ordered by creation time in reverse chronological order (newest first).</p>

        Args:
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved NotificationEvent. The default locale is English (en_US).</p>
            source: <p>The Amazon Web Services service the event originates from. For example aws.cloudwatch.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call. Next token uses Base64 encoding.</p>
            organizational_unit_id: <p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>
            related_account: <p>The Amazon Web Services account ID associated with the Managed Notification Events.</p>
            include_sensitive_events: <p>Specifies whether to include sensitive events in the result. By default, only non-sensitive events are returned. The <code>notifications:AccessSensitiveEvents</code> permission controls access to sensitive events.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.list_managed_notification_events_response.ListManagedNotificationEventsResponse"
        ]:
            import capo_notifications._operations.notifications.list_managed_notification_events

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.list_managed_notification_events.async_list_managed_notification_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListManagedNotificationEvents")
        )
        input_: capo_notifications.types.list_managed_notification_events_request.ListManagedNotificationEventsRequest = {}
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if source is not None:
            input_["source"] = source
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id
        if related_account is not None:
            input_["related_account"] = related_account
        if include_sensitive_events is not None:
            input_["include_sensitive_events"] = include_sensitive_events

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
