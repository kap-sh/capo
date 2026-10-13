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
    import capo_arc_zonal_shift.types.autoshift_execution_status
    import capo_arc_zonal_shift.types.autoshift_summary
    import capo_arc_zonal_shift.types.list_autoshifts_request
    import capo_arc_zonal_shift.types.list_autoshifts_response
    import capo_arc_zonal_shift.types.max_results
    from capo_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
        ARCZonalShiftClientConfig,
    )
    from capo_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
        AsyncARCZonalShiftClientConfig,
    )


class Autoshift:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service

    def list_autoshifts(
        self,
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
        next_token: Optional[str] = None,
        status: Optional[
            "capo_arc_zonal_shift.types.autoshift_execution_status.AutoshiftExecutionStatus"
        ] = None,
        max_results: Optional[
            "capo_arc_zonal_shift.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_arc_zonal_shift.types.list_autoshifts_response.ListAutoshiftsResponse":
        """<p>Returns the autoshifts for an Amazon Web Services Region. By default, the call returns only <code>ACTIVE</code> autoshifts. Optionally, you can specify the <code>status</code> parameter to return <code>COMPLETED</code> autoshifts. </p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            status: <p>The status of the autoshift.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_zonal_shift.types.list_autoshifts_request.ListAutoshiftsRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.list_autoshifts_response.ListAutoshiftsResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.list_autoshifts

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.list_autoshifts.list_autoshifts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAutoshifts")
        )
        input_: capo_arc_zonal_shift.types.list_autoshifts_request.ListAutoshiftsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAutoshift:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service

    async def list_autoshifts(
        self,
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        next_token: Optional[str] = None,
        status: Optional[
            "capo_arc_zonal_shift.types.autoshift_execution_status.AutoshiftExecutionStatus"
        ] = None,
        max_results: Optional[
            "capo_arc_zonal_shift.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_arc_zonal_shift.types.list_autoshifts_response.ListAutoshiftsResponse":
        """<p>Returns the autoshifts for an Amazon Web Services Region. By default, the call returns only <code>ACTIVE</code> autoshifts. Optionally, you can specify the <code>status</code> parameter to return <code>COMPLETED</code> autoshifts. </p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            status: <p>The status of the autoshift.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.list_autoshifts_request.ListAutoshiftsRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.list_autoshifts_response.ListAutoshiftsResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.list_autoshifts

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.list_autoshifts.async_list_autoshifts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAutoshifts")
        )
        input_: capo_arc_zonal_shift.types.list_autoshifts_request.ListAutoshiftsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
