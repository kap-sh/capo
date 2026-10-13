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
    import capo_notifications.types.deregister_notification_hub_request
    import capo_notifications.types.deregister_notification_hub_response
    import capo_notifications.types.list_notification_hubs_request
    import capo_notifications.types.list_notification_hubs_response
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_hub_overview
    import capo_notifications.types.region
    import capo_notifications.types.register_notification_hub_request
    import capo_notifications.types.register_notification_hub_response
    from capo_notifications._services.async_notifications import (
        AsyncNotificationsClient,
        AsyncNotificationsClientConfig,
    )
    from capo_notifications._services.notifications import (
        NotificationsClient,
        NotificationsClientConfig,
    )


class NotificationHub:
    def __init__(self, service: NotificationsClient) -> None:
        self._service = service

    def put(
        self,
        notification_hub_region: "capo_notifications.types.region.Region",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse":
        """<p>Registers a <code>NotificationHub</code> in the specified Region.</p> <p>There is a maximum of one <code>NotificationHub</code> per Region. You can have a maximum of 3 <code>NotificationHub</code> resources at a time.</p>

        Args:
            notification_hub_region: <p>The Region of the <code>NotificationHub</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse"
        ]:
            import capo_notifications._operations.notifications.register_notification_hub

            output, http_response = (
                capo_notifications._operations.notifications.register_notification_hub.register_notification_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterNotificationHub")
        )
        input_: capo_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest = {
            "notification_hub_region": notification_hub_region
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
        notification_hub_region: "capo_notifications.types.region.Region",
        *,
        config_overrides: Optional[NotificationsClientConfig] = None,
    ) -> "capo_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse":
        """<p>Deregisters a <code>NotificationHub</code> in the specified Region.</p> <note> <p>You can't deregister the last <code>NotificationHub</code> in the account. <code>NotificationEvents</code> stored in the deregistered <code>NotificationHub</code> are no longer visible. Recreating a new <code>NotificationHub</code> in the same Region restores access to those <code>NotificationEvents</code>.</p> </note>

        Args:
            notification_hub_region: <p>The <code>NotificationHub</code> Region.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse"
        ]:
            import capo_notifications._operations.notifications.deregister_notification_hub

            output, http_response = (
                capo_notifications._operations.notifications.deregister_notification_hub.deregister_notification_hub(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterNotificationHub")
        )
        input_: capo_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest = {
            "notification_hub_region": notification_hub_region
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
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse":
        """<p>Returns a list of <code>NotificationHubs</code>.</p>

        Args:
            max_results: <p>The maximum number of records to list in a single response.</p>
            next_token: <p>A pagination token. Set to null to start listing notification hubs from the start.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest]",
        ) -> OperationResponse[
            "capo_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse"
        ]:
            import capo_notifications._operations.notifications.list_notification_hubs

            output, http_response = (
                capo_notifications._operations.notifications.list_notification_hubs.list_notification_hubs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListNotificationHubs")
        )
        input_: capo_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest = {}
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


class AsyncNotificationHub:
    def __init__(self, service: AsyncNotificationsClient) -> None:
        self._service = service

    async def put(
        self,
        notification_hub_region: "capo_notifications.types.region.Region",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "capo_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse":
        """<p>Registers a <code>NotificationHub</code> in the specified Region.</p> <p>There is a maximum of one <code>NotificationHub</code> per Region. You can have a maximum of 3 <code>NotificationHub</code> resources at a time.</p>

        Args:
            notification_hub_region: <p>The Region of the <code>NotificationHub</code>.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.register_notification_hub_response.RegisterNotificationHubResponse"
        ]:
            import capo_notifications._operations.notifications.register_notification_hub

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.register_notification_hub.async_register_notification_hub(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RegisterNotificationHub")
        )
        input_: capo_notifications.types.register_notification_hub_request.RegisterNotificationHubRequest = {
            "notification_hub_region": notification_hub_region
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
        notification_hub_region: "capo_notifications.types.region.Region",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "capo_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse":
        """<p>Deregisters a <code>NotificationHub</code> in the specified Region.</p> <note> <p>You can't deregister the last <code>NotificationHub</code> in the account. <code>NotificationEvents</code> stored in the deregistered <code>NotificationHub</code> are no longer visible. Recreating a new <code>NotificationHub</code> in the same Region restores access to those <code>NotificationEvents</code>.</p> </note>

        Args:
            notification_hub_region: <p>The <code>NotificationHub</code> Region.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.deregister_notification_hub_response.DeregisterNotificationHubResponse"
        ]:
            import capo_notifications._operations.notifications.deregister_notification_hub

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.deregister_notification_hub.async_deregister_notification_hub(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeregisterNotificationHub")
        )
        input_: capo_notifications.types.deregister_notification_hub_request.DeregisterNotificationHubRequest = {
            "notification_hub_region": notification_hub_region
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
        max_results: Optional[int] = None,
        next_token: Optional["capo_notifications.types.next_token.NextToken"] = None,
    ) -> "capo_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse":
        """<p>Returns a list of <code>NotificationHubs</code>.</p>

        Args:
            max_results: <p>The maximum number of records to list in a single response.</p>
            next_token: <p>A pagination token. Set to null to start listing notification hubs from the start.</p>

        Raises:
            capo_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            capo_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            capo_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            capo_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest]",
        ) -> AsyncOperationResponse[
            "capo_notifications.types.list_notification_hubs_response.ListNotificationHubsResponse"
        ]:
            import capo_notifications._operations.notifications.list_notification_hubs

            (
                output,
                http_response,
            ) = await capo_notifications._operations.notifications.list_notification_hubs.async_list_notification_hubs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListNotificationHubs")
        )
        input_: capo_notifications.types.list_notification_hubs_request.ListNotificationHubsRequest = {}
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
