from __future__ import annotations

import datetime
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
    import capo_notifications.types.get_notification_event_request
    import capo_notifications.types.get_notification_event_response
    import capo_notifications.types.list_notification_events_request
    import capo_notifications.types.list_notification_events_response
    import capo_notifications.types.locale_code
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_event_arn
    import capo_notifications.types.notification_event_overview
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


class NotificationEventResource:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def read(
        self,
        arn: "capo_notifications.types.notification_event_arn.NotificationEventArn",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "capo_notifications.types.get_notification_event_response.GetNotificationEventResponse":
        """<p>Returns a specified <code>NotificationEvent</code>.</p> <important> <p>User Notifications stores notifications in the individual Regions you register as notification hubs and the Region of the source event rule. <code>GetNotificationEvent</code> only returns notifications stored in the same Region in which the action is called. User Notifications doesn't backfill notifications to new Regions selected as notification hubs. For this reason, we recommend that you make calls in your oldest registered notification hub. For more information, see <a href="https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html">Notification hubs</a> in the <i>Amazon Web Services User Notifications User Guide</i>.</p> </important>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English <code>en_US</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.get_notification_event_request.GetNotificationEventRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.get_notification_event_response.GetNotificationEventResponse"
        ]:
            import capo_notifications._operations.notifications.get_notification_event

            output, http_response = (
                capo_notifications._operations.notifications.get_notification_event.get_notification_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.get_notification_event_request.GetNotificationEventRequest = {
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
        include_child_events: Optional[bool] = None,
        aggregate_notification_event_arn: Optional[
            "capo_notifications.types.notification_event_arn.NotificationEventArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
    ) -> "capo_notifications.types.list_notification_events_response.ListNotificationEventsResponse":
        """<p>Returns a list of <code>NotificationEvents</code> according to specified filters, in reverse chronological order (newest first).</p> <important> <p>User Notifications stores notifications in the individual Regions you register as notification hubs and the Region of the source event rule. ListNotificationEvents only returns notifications stored in the same Region in which the action is called. User Notifications doesn't backfill notifications to new Regions selected as notification hubs. For this reason, we recommend that you make calls in your oldest registered notification hub. For more information, see <a href="https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html">Notification hubs</a> in the <i>Amazon Web Services User Notifications User Guide</i>.</p> </important>

        Args:
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>
            source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            include_child_events: <p>Include aggregated child events in the result.</p>
            aggregate_notification_event_arn: <p>The Amazon Resource Name (ARN) of the <code>aggregatedNotificationEventArn</code> to match.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>
            organizational_unit_id: <p>The unique identifier of the organizational unit used to filter notification events.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_notification_events_request.ListNotificationEventsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_notification_events_response.ListNotificationEventsResponse"
        ]:
            import capo_notifications._operations.notifications.list_notification_events

            output, http_response = (
                capo_notifications._operations.notifications.list_notification_events.list_notification_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.list_notification_events_request.ListNotificationEventsRequest = {}
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if source is not None:
            input_["source"] = source
        if include_child_events is not None:
            input_["include_child_events"] = include_child_events
        if aggregate_notification_event_arn is not None:
            input_["aggregate_notification_event_arn"] = (
                aggregate_notification_event_arn
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncNotificationEventResource:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def read(
        self,
        arn: "capo_notifications.types.notification_event_arn.NotificationEventArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        locale: Optional["capo_notifications.types.locale_code.LocaleCode"] = None,
    ) -> "capo_notifications.types.get_notification_event_response.GetNotificationEventResponse":
        """<p>Returns a specified <code>NotificationEvent</code>.</p> <important> <p>User Notifications stores notifications in the individual Regions you register as notification hubs and the Region of the source event rule. <code>GetNotificationEvent</code> only returns notifications stored in the same Region in which the action is called. User Notifications doesn't backfill notifications to new Regions selected as notification hubs. For this reason, we recommend that you make calls in your oldest registered notification hub. For more information, see <a href="https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html">Notification hubs</a> in the <i>Amazon Web Services User Notifications User Guide</i>.</p> </important>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the <code>NotificationEvent</code> to return.</p>
            locale: <p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English <code>en_US</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.get_notification_event_request.GetNotificationEventRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.get_notification_event_response.GetNotificationEventResponse"
        ]:
            import capo_notifications._operations.notifications.get_notification_event

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.get_notification_event.async_get_notification_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.get_notification_event_request.GetNotificationEventRequest = {
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
        include_child_events: Optional[bool] = None,
        aggregate_notification_event_arn: Optional[
            "capo_notifications.types.notification_event_arn.NotificationEventArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
        organizational_unit_id: Optional[
            "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
    ) -> "capo_notifications.types.list_notification_events_response.ListNotificationEventsResponse":
        """<p>Returns a list of <code>NotificationEvents</code> according to specified filters, in reverse chronological order (newest first).</p> <important> <p>User Notifications stores notifications in the individual Regions you register as notification hubs and the Region of the source event rule. ListNotificationEvents only returns notifications stored in the same Region in which the action is called. User Notifications doesn't backfill notifications to new Regions selected as notification hubs. For this reason, we recommend that you make calls in your oldest registered notification hub. For more information, see <a href="https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html">Notification hubs</a> in the <i>Amazon Web Services User Notifications User Guide</i>.</p> </important>

        Args:
            start_time: <p>The earliest time of events to return from this call.</p>
            end_time: <p>Latest time of events to return from this call.</p>
            locale: <p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>
            source: <p>The matched event source.</p> <p>Must match one of the valid EventBridge sources. Only Amazon Web Services service sourced events are supported. For example, <code>aws.ec2</code> and <code>aws.cloudwatch</code>. For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level">Event delivery from Amazon Web Services services</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            include_child_events: <p>Include aggregated child events in the result.</p>
            aggregate_notification_event_arn: <p>The Amazon Resource Name (ARN) of the <code>aggregatedNotificationEventArn</code> to match.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>
            organizational_unit_id: <p>The unique identifier of the organizational unit used to filter notification events.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.list_notification_events_request.ListNotificationEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.list_notification_events_response.ListNotificationEventsResponse"
        ]:
            import capo_notifications._operations.notifications.list_notification_events

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.list_notification_events.async_list_notification_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_notifications.types.list_notification_events_request.ListNotificationEventsRequest = {}
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if locale is not None:
            input_["locale"] = locale
        if source is not None:
            input_["source"] = source
        if include_child_events is not None:
            input_["include_child_events"] = include_child_events
        if aggregate_notification_event_arn is not None:
            input_["aggregate_notification_event_arn"] = (
                aggregate_notification_event_arn
            )
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
