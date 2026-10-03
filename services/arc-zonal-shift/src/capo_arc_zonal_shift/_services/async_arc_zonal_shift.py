"""Generated from Smithy shape ``com.amazonaws.arczonalshift#PercDataPlane``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_arc_zonal_shift._auth._signers
import capo_arc_zonal_shift._auth._sigv4
from capo_arc_zonal_shift._auth._identity import Credentials
from capo_arc_zonal_shift._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_arc_zonal_shift._auth._zapros_handler import AuthMiddleware
from capo_arc_zonal_shift._pagination import resolve_path as _resolve_path
from capo_arc_zonal_shift._resources.perc_data_plane.autoshift import AsyncAutoshift
from capo_arc_zonal_shift._resources.perc_data_plane.autoshift_observer_notification import (
    AsyncAutoshiftObserverNotification,
)
from capo_arc_zonal_shift._resources.perc_data_plane.autoshift_trigger_resource import (
    AsyncAutoshiftTriggerResource,
)
from capo_arc_zonal_shift._resources.perc_data_plane.managed_resource import (
    AsyncManagedResource,
)
from capo_arc_zonal_shift._resources.perc_data_plane.practice_run_configuration_resource import (
    AsyncPracticeRunConfigurationResource,
)
from capo_arc_zonal_shift._resources.perc_data_plane.zonal_shift_resource import (
    AsyncZonalShiftResource,
)
from capo_arc_zonal_shift._resources.perc_data_plane.zonal_shifts import (
    AsyncZonalShifts,
)
from capo_arc_zonal_shift._services._aws_config import aaws_config
from capo_arc_zonal_shift._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.allowed_windows
    import capo_arc_zonal_shift.types.autoshift_execution_status
    import capo_arc_zonal_shift.types.autoshift_observer_notification_status
    import capo_arc_zonal_shift.types.autoshift_summary
    import capo_arc_zonal_shift.types.availability_zone
    import capo_arc_zonal_shift.types.blocked_dates
    import capo_arc_zonal_shift.types.blocked_windows
    import capo_arc_zonal_shift.types.blocking_alarms
    import capo_arc_zonal_shift.types.cancel_practice_run_request
    import capo_arc_zonal_shift.types.cancel_practice_run_response
    import capo_arc_zonal_shift.types.cancel_zonal_shift_request
    import capo_arc_zonal_shift.types.create_practice_run_configuration_request
    import capo_arc_zonal_shift.types.create_practice_run_configuration_response
    import capo_arc_zonal_shift.types.delete_practice_run_configuration_request
    import capo_arc_zonal_shift.types.delete_practice_run_configuration_response
    import capo_arc_zonal_shift.types.expires_in
    import capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_request
    import capo_arc_zonal_shift.types.get_autoshift_observer_notification_status_response
    import capo_arc_zonal_shift.types.get_managed_resource_request
    import capo_arc_zonal_shift.types.get_managed_resource_response
    import capo_arc_zonal_shift.types.list_autoshifts_request
    import capo_arc_zonal_shift.types.list_autoshifts_response
    import capo_arc_zonal_shift.types.list_managed_resources_request
    import capo_arc_zonal_shift.types.list_managed_resources_response
    import capo_arc_zonal_shift.types.list_zonal_shifts_request
    import capo_arc_zonal_shift.types.list_zonal_shifts_response
    import capo_arc_zonal_shift.types.managed_resource_summary
    import capo_arc_zonal_shift.types.max_results
    import capo_arc_zonal_shift.types.outcome_alarms
    import capo_arc_zonal_shift.types.resource_identifier
    import capo_arc_zonal_shift.types.start_practice_run_request
    import capo_arc_zonal_shift.types.start_practice_run_response
    import capo_arc_zonal_shift.types.start_zonal_shift_request
    import capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_request
    import capo_arc_zonal_shift.types.update_autoshift_observer_notification_status_response
    import capo_arc_zonal_shift.types.update_practice_run_configuration_request
    import capo_arc_zonal_shift.types.update_practice_run_configuration_response
    import capo_arc_zonal_shift.types.update_zonal_autoshift_configuration_request
    import capo_arc_zonal_shift.types.update_zonal_autoshift_configuration_response
    import capo_arc_zonal_shift.types.update_zonal_shift_request
    import capo_arc_zonal_shift.types.zonal_autoshift_status
    import capo_arc_zonal_shift.types.zonal_shift
    import capo_arc_zonal_shift.types.zonal_shift_comment
    import capo_arc_zonal_shift.types.zonal_shift_id
    import capo_arc_zonal_shift.types.zonal_shift_status
    import capo_arc_zonal_shift.types.zonal_shift_summary


class AsyncARCZonalShiftClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncARCZonalShiftClient:
    """A client for the ``ARCZonalShift`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncARCZonalShiftClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.autoshift = AsyncAutoshift(self)
        self.autoshift_observer_notification = AsyncAutoshiftObserverNotification(self)
        self.autoshift_trigger_resource = AsyncAutoshiftTriggerResource(self)
        self.managed_resource = AsyncManagedResource(self)
        self.practice_run_configuration_resource = (
            AsyncPracticeRunConfigurationResource(self)
        )
        self.zonal_shift_resource = AsyncZonalShiftResource(self)
        self.zonal_shifts = AsyncZonalShifts(self)

    def operation_options(
        self, config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncARCZonalShiftClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def iter_list_autoshifts(
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
    ) -> "AsyncIterator[capo_arc_zonal_shift.types.autoshift_summary.AutoshiftSummary]":
        _token = next_token
        while True:
            _response = await self.list_autoshifts(
                config_overrides=config_overrides,
                next_token=_token,
                status=status,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def get_managed_resource(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.get_managed_resource_response.GetManagedResourceResponse":
        """<p>Get information about a resource that's been registered for zonal shifts with Amazon Application Recovery Controller in this Amazon Web Services Region. Resources that are registered for zonal shifts are managed resources in ARC. You can start zonal shifts and configure zonal autoshift for managed resources.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that Amazon Web Services shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>Amazon Application Recovery Controller currently supports enabling the following resources for zonal shift and zonal autoshift:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.ec2-auto-scaling-groups.html">Amazon EC2 Auto Scaling groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.eks.html">Amazon Elastic Kubernetes Service</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.app-load-balancers.html">Application Load Balancer</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.network-load-balancers.html">Network Load Balancer</a> </p> </li> </ul>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.resource_not_found_exception.ResourceNotFoundException: <p>The input requested a resource that was not found.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.get_managed_resource_request.GetManagedResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.get_managed_resource_response.GetManagedResourceResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.get_managed_resource

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.get_managed_resource.async_get_managed_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.get_managed_resource_request.GetManagedResourceRequest = {
            "resource_identifier": resource_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_resources(
        self,
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_arc_zonal_shift.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_arc_zonal_shift.types.list_managed_resources_response.ListManagedResourcesResponse":
        """<p>Lists all the resources in your Amazon Web Services account in this Amazon Web Services Region that are managed for zonal shifts in Amazon Application Recovery Controller, and information about them. The information includes the zonal autoshift status for the resource, as well as the Amazon Resource Name (ARN), the Availability Zones that each resource is deployed in, and the resource name.</p>

        Args:
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>

        Raises:
            capo_arc_zonal_shift.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_arc_zonal_shift.errors.internal_server_exception.InternalServerException: <p>There was an internal server error.</p>
            capo_arc_zonal_shift.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_arc_zonal_shift.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_arc_zonal_shift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.list_managed_resources_request.ListManagedResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.list_managed_resources_response.ListManagedResourcesResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.list_managed_resources

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.list_managed_resources.async_list_managed_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.list_managed_resources_request.ListManagedResourcesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_managed_resources(
        self,
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_arc_zonal_shift.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_arc_zonal_shift.types.managed_resource_summary.ManagedResourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_managed_resources(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_zonal_autoshift_configuration(
        self,
        resource_identifier: "capo_arc_zonal_shift.types.resource_identifier.ResourceIdentifier",
        zonal_autoshift_status: "capo_arc_zonal_shift.types.zonal_autoshift_status.ZonalAutoshiftStatus",
        *,
        config_overrides: Optional[AsyncARCZonalShiftClientConfig] = None,
    ) -> "capo_arc_zonal_shift.types.update_zonal_autoshift_configuration_response.UpdateZonalAutoshiftConfigurationResponse":
        """<p>The zonal autoshift configuration for a resource includes the practice run configuration and the status for running autoshifts, zonal autoshift status. When a resource has a practice run configuration, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.</p> <p>You can update the zonal autoshift status to enable or disable zonal autoshift. When zonal autoshift is <code>ENABLED</code>, you authorize Amazon Web Services to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.</p>

        Args:
            resource_identifier: <p>The identifier for the resource that you want to update the zonal autoshift configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.</p>
            zonal_autoshift_status: <p>The zonal autoshift status for the resource that you want to update the zonal autoshift configuration for. Choose <code>ENABLED</code> to authorize Amazon Web Services to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.</p>

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
            req: "AsyncOperationRequest[capo_arc_zonal_shift.types.update_zonal_autoshift_configuration_request.UpdateZonalAutoshiftConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_zonal_shift.types.update_zonal_autoshift_configuration_response.UpdateZonalAutoshiftConfigurationResponse"
        ]:
            import capo_arc_zonal_shift._operations.perc_data_plane.update_zonal_autoshift_configuration

            (
                output,
                http_response,
            ) = await capo_arc_zonal_shift._operations.perc_data_plane.update_zonal_autoshift_configuration.async_update_zonal_autoshift_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_zonal_shift.types.update_zonal_autoshift_configuration_request.UpdateZonalAutoshiftConfigurationRequest = {
            "resource_identifier": resource_identifier,
            "zonal_autoshift_status": zonal_autoshift_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_practice_run_configuration(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def delete_practice_run_configuration(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def list_zonal_shifts(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def iter_list_zonal_shifts(
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
    ) -> "AsyncIterator[capo_arc_zonal_shift.types.zonal_shift_summary.ZonalShiftSummary]":
        _token = next_token
        while True:
            _response = await self.list_zonal_shifts(
                config_overrides=config_overrides,
                next_token=_token,
                status=status,
                max_results=max_results,
                resource_identifier=resource_identifier,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
