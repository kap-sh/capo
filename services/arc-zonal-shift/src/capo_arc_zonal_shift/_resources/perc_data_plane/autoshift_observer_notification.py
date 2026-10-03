from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_arc_zonal_shift._auth._signers
import capo_arc_zonal_shift._auth._sigv4
from capo_arc_zonal_shift._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.autoshift_observer_notification_status
    import capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_request
    import capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_response
    import capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_request
    import capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_response
    from capo_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
        ARCZonalShiftClientConfig,
    )
    from capo_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
        AsyncARCZonalShiftClientConfig,
    )


class AutoshiftObserverNotification:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service

    def get_autoshift_observer_notification_status(
        self, *, config_overrides: Optional[ARCZonalShiftClientConfig] = None
    ) -> "capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_response.GetAutoshiftObserverNotificationStatusResponse":
        """<p>Returns the status of the autoshift observer notification. Autoshift observer notifications notify you through Amazon EventBridge when there is an autoshift event for zonal autoshift. The status can be <code>ENABLED</code> or <code>DISABLED</code>. When <code>ENABLED</code>, a notification is sent when an autoshift is triggered. When <code>DISABLED</code>, notifications are not sent. </p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_request.GetAutoshiftObserverNotificationStatusRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_response.GetAutoshiftObserverNotificationStatusResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.get_autoshift_observer_notification_status

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.get_autoshift_observer_notification_status.get_autoshift_observer_notification_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_request.GetAutoshiftObserverNotificationStatusRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_autoshift_observer_notification_status(
        self,
        status: "capo_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_response.UpdateAutoshiftObserverNotificationStatusResponse":
        """<p>Update the status of autoshift observer notification. Autoshift observer notification enables you to be notified, through Amazon EventBridge, when there is an autoshift event for zonal autoshift.</p> <p>If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html#ZAShiftNotification"> Notifications for practice runs and autoshifts</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            status: <p>The status to set for autoshift observer notification. If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the Amazon EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift. </p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_request.UpdateAutoshiftObserverNotificationStatusRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_response.UpdateAutoshiftObserverNotificationStatusResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.update_autoshift_observer_notification_status

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.update_autoshift_observer_notification_status.update_autoshift_observer_notification_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_request.UpdateAutoshiftObserverNotificationStatusRequest = {
            "status": status
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAutoshiftObserverNotification:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service

    async def get_autoshift_observer_notification_status(
        self, *, config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None
    ) -> "capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_response.GetAutoshiftObserverNotificationStatusResponse":
        """<p>Returns the status of the autoshift observer notification. Autoshift observer notifications notify you through Amazon EventBridge when there is an autoshift event for zonal autoshift. The status can be <code>ENABLED</code> or <code>DISABLED</code>. When <code>ENABLED</code>, a notification is sent when an autoshift is triggered. When <code>DISABLED</code>, notifications are not sent. </p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_request.GetAutoshiftObserverNotificationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_response.GetAutoshiftObserverNotificationStatusResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.get_autoshift_observer_notification_status

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.get_autoshift_observer_notification_status.async_get_autoshift_observer_notification_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_request.GetAutoshiftObserverNotificationStatusRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_autoshift_observer_notification_status(
        self,
        status: "capo_arc_zonal_shift.types.autoshift_observer_notification_status.AutoshiftObserverNotificationStatus",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_response.UpdateAutoshiftObserverNotificationStatusResponse":
        """<p>Update the status of autoshift observer notification. Autoshift observer notification enables you to be notified, through Amazon EventBridge, when there is an autoshift event for zonal autoshift.</p> <p>If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.html#ZAShiftNotification"> Notifications for practice runs and autoshifts</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            status: <p>The status to set for autoshift observer notification. If the status is <code>ENABLED</code>, ARC includes all autoshift events when you use the Amazon EventBridge pattern <code>Autoshift In Progress</code>. When the status is <code>DISABLED</code>, ARC includes only autoshift events for autoshifts when one or more of your resources is included in the autoshift. </p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_request.UpdateAutoshiftObserverNotificationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_response.UpdateAutoshiftObserverNotificationStatusResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.update_autoshift_observer_notification_status

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.update_autoshift_observer_notification_status.async_update_autoshift_observer_notification_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_request.UpdateAutoshiftObserverNotificationStatusRequest = {
            "status": status
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
