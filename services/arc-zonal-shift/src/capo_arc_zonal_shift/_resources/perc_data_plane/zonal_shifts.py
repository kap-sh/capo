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
    import capo_arc_zonal_shift.types.availability_zone
    import capo_arc_zonal_shift.types.expires_in
    import capo_arc_zonal_shift.types.list_zonal_shifts_request
    import capo_arc_zonal_shift.types.list_zonal_shifts_response
    import capo_arc_zonal_shift.types.max_results
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.start_practice_run_request
    import capo_arc_zonal_shift.types.start_practice_run_response
    import capo_arc_zonal_shift.types.start_zonal_shift_request
    import capo_arc_zonal_shift.types.zonal_shift
    import capo_arc_zonal_shift.types.zonal_shift_comment
    import capo_arc_zonal_shift.types.zonal_shift_status
    import capo_arc_zonal_shift.types.zonal_shift_summary
    from capo_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
        ARCZonalShiftClientConfig,
    )
    from capo_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
        AsyncARCZonalShiftClientConfig,
    )


class ZonalShifts:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service

    def list(
        self,
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
        next_token: Optional[str] = None,
        status: Optional[
            "capo_arc_zonal_shift.types.zonal_shift_status.ZonalShiftStatus"
        ] = None,
        max_results: Optional[
            "capo_arc_zonal_shift.types.max_results.MaxResults"
        ] = None,
        resource_identifier: Optional[
            "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
        ] = None,
    ) -> (
        "capo_arc_zonal_shift.types.list_zonal_shifts_response.ListZonalShiftsResponse"
    ):
        """<p>Lists all active and completed zonal shifts in Amazon Application Recovery Controller in your Amazon Web Services account in this Amazon Web Services Region. <code>ListZonalShifts</code> returns customer-initiated zonal shifts, as well as practice run zonal shifts that ARC started on your behalf for zonal autoshift.</p> <p>For more information about listing autoshifts, see <a href="https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListAutoshifts.html">"&gt;ListAutoshifts</a>.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            status: <p>A status for a zonal shift.</p> <p>The <code>Status</code> for a zonal shift can have one of the following values:</p> <ul> <li> <p> <b>ACTIVE</b>: The zonal shift has been started and is active.</p> </li> <li> <p> <b>EXPIRED</b>: The zonal shift has expired (the expiry time was exceeded).</p> </li> <li> <p> <b>CANCELED</b>: The zonal shift was canceled.</p> </li> </ul>
            max_results: <p>The number of objects that you want to return with this call.</p>
            resource_identifier: <p>The identifier for the resource that you want to list zonal shifts for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_zonal_shift.types.list_zonal_shifts_request.ListZonalShiftsRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.list_zonal_shifts_response.ListZonalShiftsResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.list_zonal_shifts

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.list_zonal_shifts.list_zonal_shifts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.list_zonal_shifts_request.ListZonalShiftsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_practice_run(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone",
        comment: "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.start_practice_run_response.StartPracticeRunResponse":
        """<p>Start an on-demand practice run zonal shift in Amazon Application Recovery Controller. With zonal autoshift enabled, you can start an on-demand practice run to verify preparedness at any time. Amazon Web Services also runs automated practice runs about weekly when you have enabled zonal autoshift.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html"> Considerations when you configure zonal autoshift</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to start a practice run zonal shift for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>
            away_from: <p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is shifted away from for the resource that you specify for the practice run.</p>
            comment: <p>The initial comment that you enter about the practice run. Be aware that this comment can be overwritten by Amazon Web Services if the automatic check for balanced capacity fails. For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html"> Capacity checks for practice runs</a> in the Amazon Application Recovery Controller Developer Guide. </p>

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
            req: "OperationRequest[capo_arc_zonal_shift.types.start_practice_run_request.StartPracticeRunRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.start_practice_run_response.StartPracticeRunResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.start_practice_run

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.start_practice_run.start_practice_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.start_practice_run_request.StartPracticeRunRequest = {
            "resource_identifier": resource_identifier,
            "away_from": away_from,
            "comment": comment,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_zonal_shift(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone",
        expires_in: "capo_arc_zonal_shift.types.expires_in.ExpiresIn",
        comment: "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>You start a zonal shift to temporarily move load balancer traffic away from an Availability Zone in an Amazon Web Services Region, to help your application recover immediately, for example, from a developer's bad code deployment or from an Amazon Web Services infrastructure failure in a single Availability Zone. You can start a zonal shift in ARC only for managed resources in your Amazon Web Services account in an Amazon Web Services Region. Resources are automatically registered with ARC by Amazon Web Services services.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul> <p>When you start a zonal shift, traffic for the resource is no longer routed to the Availability Zone. The zonal shift is created immediately in ARC. However, it can take a short time, typically up to a few minutes, for existing, in-progress connections in the Availability Zone to complete.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html">Zonal shift</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that Amazon Web Services shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul>
            away_from: <p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the Amazon Web Services Region.</p>
            expires_in: <p>The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).</p> <p>If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.</p> <p>To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:</p> <ul> <li> <p> <b>A lowercase letter m:</b> To specify that the value is in minutes.</p> </li> <li> <p> <b>A lowercase letter h:</b> To specify that the value is in hours.</p> </li> </ul> <p>For example: <code>20h</code> means the zonal shift expires in 20 hours. <code>120m</code> means the zonal shift expires in 120 minutes (2 hours).</p>
            comment: <p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.</p>

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
            req: "OperationRequest[capo_arc_zonal_shift.types.start_zonal_shift_request.StartZonalShiftRequest]",
        ) -> OperationResponse["capo_arc_zonal_shift.types.zonal_shift.ZonalShift"]:
            import capo_arc_zonal_shift._operations.perc_data_plane.start_zonal_shift

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.start_zonal_shift.start_zonal_shift(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.start_zonal_shift_request.StartZonalShiftRequest = {
            "resource_identifier": resource_identifier,
            "away_from": away_from,
            "expires_in": expires_in,
            "comment": comment,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncZonalShifts:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        next_token: Optional[str] = None,
        status: Optional[
            "capo_arc_zonal_shift.types.zonal_shift_status.ZonalShiftStatus"
        ] = None,
        max_results: Optional[
            "capo_arc_zonal_shift.types.max_results.MaxResults"
        ] = None,
        resource_identifier: Optional[
            "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier"
        ] = None,
    ) -> (
        "capo_arc_zonal_shift.types.list_zonal_shifts_response.ListZonalShiftsResponse"
    ):
        """<p>Lists all active and completed zonal shifts in Amazon Application Recovery Controller in your Amazon Web Services account in this Amazon Web Services Region. <code>ListZonalShifts</code> returns customer-initiated zonal shifts, as well as practice run zonal shifts that ARC started on your behalf for zonal autoshift.</p> <p>For more information about listing autoshifts, see <a href="https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListAutoshifts.html">"&gt;ListAutoshifts</a>.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            status: <p>A status for a zonal shift.</p> <p>The <code>Status</code> for a zonal shift can have one of the following values:</p> <ul> <li> <p> <b>ACTIVE</b>: The zonal shift has been started and is active.</p> </li> <li> <p> <b>EXPIRED</b>: The zonal shift has expired (the expiry time was exceeded).</p> </li> <li> <p> <b>CANCELED</b>: The zonal shift was canceled.</p> </li> </ul>
            max_results: <p>The number of objects that you want to return with this call.</p>
            resource_identifier: <p>The identifier for the resource that you want to list zonal shifts for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.list_zonal_shifts_request.ListZonalShiftsRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.list_zonal_shifts_response.ListZonalShiftsResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.list_zonal_shifts

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.list_zonal_shifts.async_list_zonal_shifts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.list_zonal_shifts_request.ListZonalShiftsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_practice_run(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone",
        comment: "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.start_practice_run_response.StartPracticeRunResponse":
        """<p>Start an on-demand practice run zonal shift in Amazon Application Recovery Controller. With zonal autoshift enabled, you can start an on-demand practice run to verify preparedness at any time. Amazon Web Services also runs automated practice runs about weekly when you have enabled zonal autoshift.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html"> Considerations when you configure zonal autoshift</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to start a practice run zonal shift for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>
            away_from: <p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is shifted away from for the resource that you specify for the practice run.</p>
            comment: <p>The initial comment that you enter about the practice run. Be aware that this comment can be overwritten by Amazon Web Services if the automatic check for balanced capacity fails. For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.capacity-check.html"> Capacity checks for practice runs</a> in the Amazon Application Recovery Controller Developer Guide. </p>

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
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.start_practice_run_request.StartPracticeRunRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.start_practice_run_response.StartPracticeRunResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.start_practice_run

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.start_practice_run.async_start_practice_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.start_practice_run_request.StartPracticeRunRequest = {
            "resource_identifier": resource_identifier,
            "away_from": away_from,
            "comment": comment,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_zonal_shift(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        away_from: "capo_arc_zonal_shift.types.availability_zone.AvailabilityZone",
        expires_in: "capo_arc_zonal_shift.types.expires_in.ExpiresIn",
        comment: "capo_arc_zonal_shift.types.zonal_shift_comment.ZonalShiftComment",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.zonal_shift.ZonalShift":
        """<p>You start a zonal shift to temporarily move load balancer traffic away from an Availability Zone in an Amazon Web Services Region, to help your application recover immediately, for example, from a developer's bad code deployment or from an Amazon Web Services infrastructure failure in a single Availability Zone. You can start a zonal shift in ARC only for managed resources in your Amazon Web Services account in an Amazon Web Services Region. Resources are automatically registered with ARC by Amazon Web Services services.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul> <p>When you start a zonal shift, traffic for the resource is no longer routed to the Availability Zone. The zonal shift is created immediately in ARC. However, it can take a short time, typically up to a few minutes, for existing, in-progress connections in the Availability Zone to complete.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html">Zonal shift</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that Amazon Web Services shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul>
            away_from: <p>The Availability Zone (for example, <code>use1-az1</code>) that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the Amazon Web Services Region.</p>
            expires_in: <p>The length of time that you want a zonal shift to be active, which ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).</p> <p>If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you're ready to restore traffic to the Availability Zone.</p> <p>To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:</p> <ul> <li> <p> <b>A lowercase letter m:</b> To specify that the value is in minutes.</p> </li> <li> <p> <b>A lowercase letter h:</b> To specify that the value is in hours.</p> </li> </ul> <p>For example: <code>20h</code> means the zonal shift expires in 20 hours. <code>120m</code> means the zonal shift expires in 120 minutes (2 hours).</p>
            comment: <p>A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string.</p>

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
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.start_zonal_shift_request.StartZonalShiftRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.zonal_shift.ZonalShift"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.start_zonal_shift

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.start_zonal_shift.async_start_zonal_shift(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.start_zonal_shift_request.StartZonalShiftRequest = {
            "resource_identifier": resource_identifier,
            "away_from": away_from,
            "expires_in": expires_in,
            "comment": comment,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
