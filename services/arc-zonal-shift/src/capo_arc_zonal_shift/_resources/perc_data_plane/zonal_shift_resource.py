from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_arc_zonal_shift._auth._signers
import capo_arc_zonal_shift._auth._sigv4
from capo_arc_zonal_shift._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.cancel_practice_run_request
    import capo_arc_zonal_shift.types.cancel_practice_run_response
    import capo_arc_zonal_shift.types.cancel_zonal_shift_request
    import capo_arc_zonal_shift.types.expires_in
    import capo_arc_zonal_shift.types.update_zonal_shift_request
    import capo_arc_zonal_shift.types.zonal_shift
    import capo_arc_zonal_shift.types.zonal_shift_comment
    import capo_arc_zonal_shift.types.zonal_shift_id
    from capo_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
        ARCZonalShiftClientConfig,
    )
    from capo_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
        AsyncARCZonalShiftClientConfig,
    )


class ZonalShiftResource:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service

    def cancel_practice_run(
        self,
        zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.cancel_practice_run_response.CancelPracticeRunResponse":
        """<p>Cancel an in-progress practice run zonal shift in Amazon Application Recovery Controller.</p>

        Args:
            zonal_shift_id: <p>The identifier of a practice run zonal shift in Amazon Application Recovery Controller that you want to cancel.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.resource_not_found_exception.ResourceNotFoundException: <p>The input requested a resource that was not found.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_zonal_shift.types.cancel_practice_run_request.CancelPracticeRunRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.cancel_practice_run_response.CancelPracticeRunResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.cancel_practice_run

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.cancel_practice_run.cancel_practice_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelPracticeRun")
        )
        input_: capo_arc_zonal_shift.types.cancel_practice_run_request.CancelPracticeRunRequest = {
            "zonal_shift_id": zonal_shift_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_zonal_shift(
        self,
        zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>Cancel a zonal shift in Amazon Application Recovery Controller. To cancel the zonal shift, specify the zonal shift ID.</p> <p>A zonal shift can be one that you've started for a resource in your Amazon Web Services account in an Amazon Web Services Region, or it can be a zonal shift started by a practice run with zonal autoshift. </p>

        Args:
            zonal_shift_id: <p>The internally-generated identifier of a zonal shift.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.resource_not_found_exception.ResourceNotFoundException: <p>The input requested a resource that was not found.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_zonal_shift.types.cancel_zonal_shift_request.CancelZonalShiftRequest]",
        ) -> OperationResponse["capo_arc_zonal_shift.types.zonal_shift.ZonalShift"]:
            import capo_arc_zonal_shift._operations.perc_data_plane.cancel_zonal_shift

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.cancel_zonal_shift.cancel_zonal_shift(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelZonalShift")
        )
        input_: capo_arc_zonal_shift.types.cancel_zonal_shift_request.CancelZonalShiftRequest = {
            "zonal_shift_id": zonal_shift_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_zonal_shift(
        self,
        zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
        comment: Optional[
            "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
        ] = None,
        expires_in: Optional["capo_arc_zonal_shift.types.expires_in.ExpiresIn"] = None,
    ) -> "capo_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>Update an active zonal shift in Amazon Application Recovery Controller in your Amazon Web Services account. You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift.</p>

        Args:
            zonal_shift_id: <p>The identifier of a zonal shift.</p>
            comment: <p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.</p>
            expires_in: <p>The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).</p> <p>If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.</p> <p>To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:</p> <ul> <li> <p> <b>A lowercase letter m:</b> To specify that the value is in minutes.</p> </li> <li> <p> <b>A lowercase letter h:</b> To specify that the value is in hours.</p> </li> </ul> <p>For example: <code>20h</code> means the zonal shift expires in 20 hours. <code>120m</code> means the zonal shift expires in 120 minutes (2 hours).</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.resource_not_found_exception.ResourceNotFoundException: <p>The input requested a resource that was not found.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_zonal_shift.types.update_zonal_shift_request.UpdateZonalShiftRequest]",
        ) -> OperationResponse["capo_arc_zonal_shift.types.zonal_shift.ZonalShift"]:
            import capo_arc_zonal_shift._operations.perc_data_plane.update_zonal_shift

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.update_zonal_shift.update_zonal_shift(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateZonalShift")
        )
        input_: capo_arc_zonal_shift.types.update_zonal_shift_request.UpdateZonalShiftRequest = {
            "zonal_shift_id": zonal_shift_id
        }
        if comment is not None:
            input_["comment"] = comment
        if expires_in is not None:
            input_["expires_in"] = expires_in

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncZonalShiftResource:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service

    async def cancel_practice_run(
        self,
        zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.cancel_practice_run_response.CancelPracticeRunResponse":
        """<p>Cancel an in-progress practice run zonal shift in Amazon Application Recovery Controller.</p>

        Args:
            zonal_shift_id: <p>The identifier of a practice run zonal shift in Amazon Application Recovery Controller that you want to cancel.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.resource_not_found_exception.ResourceNotFoundException: <p>The input requested a resource that was not found.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.cancel_practice_run_request.CancelPracticeRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.cancel_practice_run_response.CancelPracticeRunResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.cancel_practice_run

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.cancel_practice_run.async_cancel_practice_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelPracticeRun")
        )
        input_: capo_arc_zonal_shift.types.cancel_practice_run_request.CancelPracticeRunRequest = {
            "zonal_shift_id": zonal_shift_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_zonal_shift(
        self,
        zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>Cancel a zonal shift in Amazon Application Recovery Controller. To cancel the zonal shift, specify the zonal shift ID.</p> <p>A zonal shift can be one that you've started for a resource in your Amazon Web Services account in an Amazon Web Services Region, or it can be a zonal shift started by a practice run with zonal autoshift. </p>

        Args:
            zonal_shift_id: <p>The internally-generated identifier of a zonal shift.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.resource_not_found_exception.ResourceNotFoundException: <p>The input requested a resource that was not found.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.cancel_zonal_shift_request.CancelZonalShiftRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.zonal_shift.ZonalShift"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.cancel_zonal_shift

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.cancel_zonal_shift.async_cancel_zonal_shift(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CancelZonalShift")
        )
        input_: capo_arc_zonal_shift.types.cancel_zonal_shift_request.CancelZonalShiftRequest = {
            "zonal_shift_id": zonal_shift_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_zonal_shift(
        self,
        zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        comment: Optional[
            "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment"
        ] = None,
        expires_in: Optional["capo_arc_zonal_shift.types.expires_in.ExpiresIn"] = None,
    ) -> "capo_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>Update an active zonal shift in Amazon Application Recovery Controller in your Amazon Web Services account. You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift.</p>

        Args:
            zonal_shift_id: <p>The identifier of a zonal shift.</p>
            comment: <p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.</p>
            expires_in: <p>The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).</p> <p>If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.</p> <p>To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:</p> <ul> <li> <p> <b>A lowercase letter m:</b> To specify that the value is in minutes.</p> </li> <li> <p> <b>A lowercase letter h:</b> To specify that the value is in hours.</p> </li> </ul> <p>For example: <code>20h</code> means the zonal shift expires in 20 hours. <code>120m</code> means the zonal shift expires in 120 minutes (2 hours).</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.resource_not_found_exception.ResourceNotFoundException: <p>The input requested a resource that was not found.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.update_zonal_shift_request.UpdateZonalShiftRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.zonal_shift.ZonalShift"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.update_zonal_shift

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.update_zonal_shift.async_update_zonal_shift(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateZonalShift")
        )
        input_: capo_arc_zonal_shift.types.update_zonal_shift_request.UpdateZonalShiftRequest = {
            "zonal_shift_id": zonal_shift_id
        }
        if comment is not None:
            input_["comment"] = comment
        if expires_in is not None:
            input_["expires_in"] = expires_in

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
