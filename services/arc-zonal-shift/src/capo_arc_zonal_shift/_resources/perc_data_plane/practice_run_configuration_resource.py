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
    import capo_arc_zonal_shift.types.allowed_windows
    import capo_arc_zonal_shift.types.blocked_dates
    import capo_arc_zonal_shift.types.blocked_windows
    import capo_arc_zonal_shift.types.blocking_alarms
    import capo_arc_zonal_shift.types.create_practice_run_configuration_request
    import capo_arc_zonal_shift.types.create_practice_run_configuration_response
    import capo_arc_zonal_shift.types.delete_practice_run_configuration_request
    import capo_arc_zonal_shift.types.delete_practice_run_configuration_response
    import capo_arc_zonal_shift.types.outcome_alarms
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.update_practice_run_configuration_request
    import capo_arc_zonal_shift.types.update_practice_run_configuration_response
    from capo_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
        ARCZonalShiftClientConfig,
    )
    from capo_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
        AsyncARCZonalShiftClientConfig,
    )


class PracticeRunConfigurationResource:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service

    def update(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
        blocked_windows: Optional[
            "capo_arc_zonal_shift.types.blocked_windows.BlockedWindows"
        ] = None,
        blocked_dates: Optional[
            "capo_arc_zonal_shift.types.blocked_dates.BlockedDates"
        ] = None,
        blocking_alarms: Optional[
            "capo_arc_zonal_shift.types.blocking_alarms.BlockingAlarms"
        ] = None,
        allowed_windows: Optional[
            "capo_arc_zonal_shift.types.allowed_windows.AllowedWindows"
        ] = None,
        outcome_alarms: Optional[
            "capo_arc_zonal_shift.types.outcome_alarms.OutcomeAlarms"
        ] = None,
    ) -> "capo_arc_zonal_shift.types.update_practice_run_configuration_response.UpdatePracticeRunConfigurationResponse":
        """<p>Update a practice run configuration to change one or more of the following: add, change, or remove the blocking alarm; change the outcome alarm; or add, change, or remove blocking dates or time windows.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to update the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>
            blocked_windows: <p>Add, change, or remove windows of days and times for when you can, optionally, block ARC from starting a practice run for a resource.</p> <p>The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.</p> <p>For example, say you run business report summaries three days a week. For this scenario, you might set the following recurring days and times as blocked windows, for example: <code>MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30</code>.</p>
            blocked_dates: <p>Add, change, or remove blocked dates for a practice run in zonal autoshift.</p> <p>Optionally, you can block practice runs for specific calendar dates. The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.</p> <p>For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for <code>2024-05-01</code>.</p>
            blocking_alarms: <p>Add, change, or remove the Amazon CloudWatch alarms that you optionally specify as the blocking alarms for practice runs.</p>
            allowed_windows: <p>Add, change, or remove windows of days and times for when you can, optionally, allow ARC to start a practice run for a resource.</p> <p>The format for allowed windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple allowed windows with spaces.</p> <p>For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: <code>Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00</code>.</p> <important> <p>The <code>allowedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>
            outcome_alarms: <p>Specify one or more Amazon CloudWatch alarms as the outcome alarms for practice runs.</p>

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
            req: "OperationRequest[capo_arc_zonal_shift.types.update_practice_run_configuration_request.UpdatePracticeRunConfigurationRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.update_practice_run_configuration_response.UpdatePracticeRunConfigurationResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.update_practice_run_configuration

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.update_practice_run_configuration.update_practice_run_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.update_practice_run_configuration_request.UpdatePracticeRunConfigurationRequest = {
            "resource_identifier": resource_identifier
        }
        if blocked_windows is not None:
            input_["blocked_windows"] = blocked_windows
        if blocked_dates is not None:
            input_["blocked_dates"] = blocked_dates
        if blocking_alarms is not None:
            input_["blocking_alarms"] = blocking_alarms
        if allowed_windows is not None:
            input_["allowed_windows"] = allowed_windows
        if outcome_alarms is not None:
            input_["outcome_alarms"] = outcome_alarms

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.delete_practice_run_configuration_response.DeletePracticeRunConfigurationResponse":
        """<p>Deletes the practice run configuration for a resource. Before you can delete a practice run configuration for a resource., you must disable zonal autoshift for the resource. Practice runs must be configured for zonal autoshift to be enabled.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to delete the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>

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
            req: "OperationRequest[capo_arc_zonal_shift.types.delete_practice_run_configuration_request.DeletePracticeRunConfigurationRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.delete_practice_run_configuration_response.DeletePracticeRunConfigurationResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.delete_practice_run_configuration

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.delete_practice_run_configuration.delete_practice_run_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.delete_practice_run_configuration_request.DeletePracticeRunConfigurationRequest = {
            "resource_identifier": resource_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_practice_run_configuration(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        outcome_alarms: "capo_arc_zonal_shift.types.outcome_alarms.OutcomeAlarms",
        *,
        config_overrides: Optional[ARCZonalShiftClientConfig] = None,
        blocked_windows: Optional[
            "capo_arc_zonal_shift.types.blocked_windows.BlockedWindows"
        ] = None,
        blocked_dates: Optional[
            "capo_arc_zonal_shift.types.blocked_dates.BlockedDates"
        ] = None,
        blocking_alarms: Optional[
            "capo_arc_zonal_shift.types.blocking_alarms.BlockingAlarms"
        ] = None,
        allowed_windows: Optional[
            "capo_arc_zonal_shift.types.allowed_windows.AllowedWindows"
        ] = None,
    ) -> "capo_arc_zonal_shift.types.create_practice_run_configuration_response.CreatePracticeRunConfigurationResponse":
        """<p>A practice run configuration for zonal autoshift is required when you enable zonal autoshift. A practice run configuration includes specifications for blocked dates and blocked time windows, and for Amazon CloudWatch alarms that you create to use with practice runs. The alarms that you specify are an <i>outcome alarm</i>, to monitor application health during practice runs and, optionally, a <i>blocking alarm</i>, to block practice runs from starting.</p> <p>When a resource has a practice run configuration, ARC starts zonal shifts for the resource weekly, to shift traffic for practice runs. Practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html"> Considerations when you configure zonal autoshift</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            resource_identifier: <p>The identifier of the resource that Amazon Web Services shifts traffic for with a practice run zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul>
            blocked_windows: <p>Optionally, you can block ARC from starting practice runs for specific windows of days and times. </p> <p>The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.</p> <p>For example, say you run business report summaries three days a week. For this scenario, you could set the following recurring days and times as blocked windows, for example: <code>Mon:00:00-Mon:10:00 Wed-20:30-Wed:21:30 Fri-20:30-Fri:21:30</code>.</p> <important> <p>The <code>blockedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>
            blocked_dates: <p>Optionally, you can block ARC from starting practice runs for a resource on specific calendar dates.</p> <p>The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.</p> <p>For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for <code>2024-05-01</code>.</p>
            blocking_alarms: <p> <i>Blocking alarms</i> for practice runs are optional alarms that you can specify that block practice runs when one or more of the alarms is in an <code>ALARM</code> state.</p>
            allowed_windows: <p>Optionally, you can allow ARC to start practice runs for specific windows of days and times. </p> <p>The format for allowed windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple allowed windows with spaces.</p> <p>For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: <code>Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00</code>.</p> <important> <p>The <code>allowedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>
            outcome_alarms: <p> <i>Outcome alarms</i> for practice runs are alarms that you specify that end a practice run when one or more of the alarms is in an <code>ALARM</code> state.</p> <p>Configure one or more of these alarms to monitor the health of your application when traffic is shifted away from an Availability Zone during each practice run. You should configure these alarms to go into an <code>ALARM</code> state if you want to stop a zonal shift, to let traffic for the resource return to the original Availability Zone.</p>

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
            req: "OperationRequest[capo_arc_zonal_shift.types.create_practice_run_configuration_request.CreatePracticeRunConfigurationRequest]",
        ) -> OperationResponse[
            "capo_arc_zonal_shift.types.create_practice_run_configuration_response.CreatePracticeRunConfigurationResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.create_practice_run_configuration

            output, http_response = (
                capo_arc_zonal_shift._operations.perc_data_plane.create_practice_run_configuration.create_practice_run_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.create_practice_run_configuration_request.CreatePracticeRunConfigurationRequest = {
            "resource_identifier": resource_identifier,
            "outcome_alarms": outcome_alarms,
        }
        if blocked_windows is not None:
            input_["blocked_windows"] = blocked_windows
        if blocked_dates is not None:
            input_["blocked_dates"] = blocked_dates
        if blocking_alarms is not None:
            input_["blocking_alarms"] = blocking_alarms
        if allowed_windows is not None:
            input_["allowed_windows"] = allowed_windows

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPracticeRunConfigurationResource:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service

    async def update(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        blocked_windows: Optional[
            "capo_arc_zonal_shift.types.blocked_windows.BlockedWindows"
        ] = None,
        blocked_dates: Optional[
            "capo_arc_zonal_shift.types.blocked_dates.BlockedDates"
        ] = None,
        blocking_alarms: Optional[
            "capo_arc_zonal_shift.types.blocking_alarms.BlockingAlarms"
        ] = None,
        allowed_windows: Optional[
            "capo_arc_zonal_shift.types.allowed_windows.AllowedWindows"
        ] = None,
        outcome_alarms: Optional[
            "capo_arc_zonal_shift.types.outcome_alarms.OutcomeAlarms"
        ] = None,
    ) -> "capo_arc_zonal_shift.types.update_practice_run_configuration_response.UpdatePracticeRunConfigurationResponse":
        """<p>Update a practice run configuration to change one or more of the following: add, change, or remove the blocking alarm; change the outcome alarm; or add, change, or remove blocking dates or time windows.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to update the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>
            blocked_windows: <p>Add, change, or remove windows of days and times for when you can, optionally, block ARC from starting a practice run for a resource.</p> <p>The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.</p> <p>For example, say you run business report summaries three days a week. For this scenario, you might set the following recurring days and times as blocked windows, for example: <code>MON-20:30-21:30 WED-20:30-21:30 FRI-20:30-21:30</code>.</p>
            blocked_dates: <p>Add, change, or remove blocked dates for a practice run in zonal autoshift.</p> <p>Optionally, you can block practice runs for specific calendar dates. The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.</p> <p>For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for <code>2024-05-01</code>.</p>
            blocking_alarms: <p>Add, change, or remove the Amazon CloudWatch alarms that you optionally specify as the blocking alarms for practice runs.</p>
            allowed_windows: <p>Add, change, or remove windows of days and times for when you can, optionally, allow ARC to start a practice run for a resource.</p> <p>The format for allowed windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple allowed windows with spaces.</p> <p>For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: <code>Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00</code>.</p> <important> <p>The <code>allowedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>
            outcome_alarms: <p>Specify one or more Amazon CloudWatch alarms as the outcome alarms for practice runs.</p>

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
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.update_practice_run_configuration_request.UpdatePracticeRunConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.update_practice_run_configuration_response.UpdatePracticeRunConfigurationResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.update_practice_run_configuration

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.update_practice_run_configuration.async_update_practice_run_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.update_practice_run_configuration_request.UpdatePracticeRunConfigurationRequest = {
            "resource_identifier": resource_identifier
        }
        if blocked_windows is not None:
            input_["blocked_windows"] = blocked_windows
        if blocked_dates is not None:
            input_["blocked_dates"] = blocked_dates
        if blocking_alarms is not None:
            input_["blocking_alarms"] = blocking_alarms
        if allowed_windows is not None:
            input_["allowed_windows"] = allowed_windows
        if outcome_alarms is not None:
            input_["outcome_alarms"] = outcome_alarms

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.delete_practice_run_configuration_response.DeletePracticeRunConfigurationResponse":
        """<p>Deletes the practice run configuration for a resource. Before you can delete a practice run configuration for a resource., you must disable zonal autoshift for the resource. Practice runs must be configured for zonal autoshift to be enabled.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to delete the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>

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
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.delete_practice_run_configuration_request.DeletePracticeRunConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.delete_practice_run_configuration_response.DeletePracticeRunConfigurationResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.delete_practice_run_configuration

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.delete_practice_run_configuration.async_delete_practice_run_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.delete_practice_run_configuration_request.DeletePracticeRunConfigurationRequest = {
            "resource_identifier": resource_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_practice_run_configuration(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        outcome_alarms: "capo_arc_zonal_shift.types.outcome_alarms.OutcomeAlarms",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        blocked_windows: Optional[
            "capo_arc_zonal_shift.types.blocked_windows.BlockedWindows"
        ] = None,
        blocked_dates: Optional[
            "capo_arc_zonal_shift.types.blocked_dates.BlockedDates"
        ] = None,
        blocking_alarms: Optional[
            "capo_arc_zonal_shift.types.blocking_alarms.BlockingAlarms"
        ] = None,
        allowed_windows: Optional[
            "capo_arc_zonal_shift.types.allowed_windows.AllowedWindows"
        ] = None,
    ) -> "capo_arc_zonal_shift.types.create_practice_run_configuration_response.CreatePracticeRunConfigurationResponse":
        """<p>A practice run configuration for zonal autoshift is required when you enable zonal autoshift. A practice run configuration includes specifications for blocked dates and blocked time windows, and for Amazon CloudWatch alarms that you create to use with practice runs. The alarms that you specify are an <i>outcome alarm</i>, to monitor application health during practice runs and, optionally, a <i>blocking alarm</i>, to block practice runs from starting.</p> <p>When a resource has a practice run configuration, ARC starts zonal shifts for the resource weekly, to shift traffic for practice runs. Practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html"> Considerations when you configure zonal autoshift</a> in the Amazon Application Recovery Controller Developer Guide.</p>

        Args:
            resource_identifier: <p>The identifier of the resource that Amazon Web Services shifts traffic for with a practice run zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul>
            blocked_windows: <p>Optionally, you can block ARC from starting practice runs for specific windows of days and times. </p> <p>The format for blocked windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple blocked windows with spaces.</p> <p>For example, say you run business report summaries three days a week. For this scenario, you could set the following recurring days and times as blocked windows, for example: <code>Mon:00:00-Mon:10:00 Wed-20:30-Wed:21:30 Fri-20:30-Fri:21:30</code>.</p> <important> <p>The <code>blockedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>
            blocked_dates: <p>Optionally, you can block ARC from starting practice runs for a resource on specific calendar dates.</p> <p>The format for blocked dates is: YYYY-MM-DD. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Separate multiple blocked dates with spaces.</p> <p>For example, if you have an application update scheduled to launch on May 1, 2024, and you don't want practice runs to shift traffic away at that time, you could set a blocked date for <code>2024-05-01</code>.</p>
            blocking_alarms: <p> <i>Blocking alarms</i> for practice runs are optional alarms that you can specify that block practice runs when one or more of the alarms is in an <code>ALARM</code> state.</p>
            allowed_windows: <p>Optionally, you can allow ARC to start practice runs for specific windows of days and times. </p> <p>The format for allowed windows is: DAY:HH:SS-DAY:HH:SS. Keep in mind, when you specify dates, that dates and times for practice runs are in UTC. Also, be aware of potential time adjustments that might be required for daylight saving time differences. Separate multiple allowed windows with spaces.</p> <p>For example, say you want to allow practice runs only on Wednesdays and Fridays from noon to 5 p.m. For this scenario, you could set the following recurring days and times as allowed windows, for example: <code>Wed-12:00-Wed:17:00 Fri-12:00-Fri:17:00</code>.</p> <important> <p>The <code>allowedWindows</code> have to start and end on the same day. Windows that span multiple days aren't supported.</p> </important>
            outcome_alarms: <p> <i>Outcome alarms</i> for practice runs are alarms that you specify that end a practice run when one or more of the alarms is in an <code>ALARM</code> state.</p> <p>Configure one or more of these alarms to monitor the health of your application when traffic is shifted away from an Availability Zone during each practice run. You should configure these alarms to go into an <code>ALARM</code> state if you want to stop a zonal shift, to let traffic for the resource return to the original Availability Zone.</p>

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
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.create_practice_run_configuration_request.CreatePracticeRunConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.create_practice_run_configuration_response.CreatePracticeRunConfigurationResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.create_practice_run_configuration

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.create_practice_run_configuration.async_create_practice_run_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.create_practice_run_configuration_request.CreatePracticeRunConfigurationRequest = {
            "resource_identifier": resource_identifier,
            "outcome_alarms": outcome_alarms,
        }
        if blocked_windows is not None:
            input_["blocked_windows"] = blocked_windows
        if blocked_dates is not None:
            input_["blocked_dates"] = blocked_dates
        if blocking_alarms is not None:
            input_["blocking_alarms"] = blocking_alarms
        if allowed_windows is not None:
            input_["allowed_windows"] = allowed_windows

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
