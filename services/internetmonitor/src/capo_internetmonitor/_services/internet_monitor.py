"""Generated from Smithy shape ``com.amazonaws.internetmonitor#InternetMonitor20210603``."""

import datetime
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_internetmonitor._auth._signers
import capo_internetmonitor._auth._sigv4
from capo_internetmonitor._auth._identity import Credentials
from capo_internetmonitor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_internetmonitor._auth._zapros_handler import AuthMiddleware
from capo_internetmonitor._pagination import resolve_path as _resolve_path
from capo_internetmonitor._resources.internet_monitor20210603.internet_event_resource import (
    InternetEventResource,
)
from capo_internetmonitor._resources.internet_monitor20210603.monitor_resource import (
    MonitorResource,
)
from capo_internetmonitor._services._aws_config import aws_config
from capo_internetmonitor._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_internetmonitor.types.account_id
    import capo_internetmonitor.types.create_monitor_input
    import capo_internetmonitor.types.create_monitor_output
    import capo_internetmonitor.types.delete_monitor_input
    import capo_internetmonitor.types.delete_monitor_output
    import capo_internetmonitor.types.filter_parameters
    import capo_internetmonitor.types.get_health_event_input
    import capo_internetmonitor.types.get_health_event_output
    import capo_internetmonitor.types.get_internet_event_input
    import capo_internetmonitor.types.get_internet_event_output
    import capo_internetmonitor.types.get_monitor_input
    import capo_internetmonitor.types.get_monitor_output
    import capo_internetmonitor.types.get_query_results_input
    import capo_internetmonitor.types.get_query_results_output
    import capo_internetmonitor.types.get_query_status_input
    import capo_internetmonitor.types.get_query_status_output
    import capo_internetmonitor.types.health_event
    import capo_internetmonitor.types.health_event_name
    import capo_internetmonitor.types.health_event_status
    import capo_internetmonitor.types.health_events_config
    import capo_internetmonitor.types.internet_event_id
    import capo_internetmonitor.types.internet_event_max_results
    import capo_internetmonitor.types.internet_event_summary
    import capo_internetmonitor.types.internet_measurements_log_delivery
    import capo_internetmonitor.types.list_health_events_input
    import capo_internetmonitor.types.list_health_events_output
    import capo_internetmonitor.types.list_internet_events_input
    import capo_internetmonitor.types.list_internet_events_output
    import capo_internetmonitor.types.list_monitors_input
    import capo_internetmonitor.types.list_monitors_output
    import capo_internetmonitor.types.list_tags_for_resource_input
    import capo_internetmonitor.types.list_tags_for_resource_output
    import capo_internetmonitor.types.max_city_networks_to_monitor
    import capo_internetmonitor.types.max_results
    import capo_internetmonitor.types.monitor
    import capo_internetmonitor.types.monitor_arn
    import capo_internetmonitor.types.monitor_config_state
    import capo_internetmonitor.types.query_max_results
    import capo_internetmonitor.types.query_type
    import capo_internetmonitor.types.resource_name
    import capo_internetmonitor.types.set_of_ar_ns
    import capo_internetmonitor.types.start_query_input
    import capo_internetmonitor.types.start_query_output
    import capo_internetmonitor.types.stop_query_input
    import capo_internetmonitor.types.stop_query_output
    import capo_internetmonitor.types.tag_keys
    import capo_internetmonitor.types.tag_map
    import capo_internetmonitor.types.tag_resource_input
    import capo_internetmonitor.types.tag_resource_output
    import capo_internetmonitor.types.traffic_percentage_to_monitor
    import capo_internetmonitor.types.untag_resource_input
    import capo_internetmonitor.types.untag_resource_output
    import capo_internetmonitor.types.update_monitor_input
    import capo_internetmonitor.types.update_monitor_output


class InternetMonitorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class InternetMonitorClient:
    """A client for the ``InternetMonitor`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = InternetMonitorClientConfig(
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
        self.internet_event_resource = InternetEventResource(self)
        self.monitor_resource = MonitorResource(self)

    def operation_options(
        self, config_overrides: Optional[InternetMonitorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: InternetMonitorClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "capo_internetmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags for a resource. Tags are supported only for monitors in Amazon CloudWatch Internet Monitor.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a resource.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.bad_request_exception.BadRequestException: <p>A bad request was received.</p>
            capo_internetmonitor.errors.internal_server_error_exception.InternalServerErrorException: <p>There was an internal server error.</p>
            capo_internetmonitor.errors.not_found_exception.NotFoundException: <p>The request specifies something that doesn't exist.</p>
            capo_internetmonitor.errors.too_many_requests_exception.TooManyRequestsException: <p>There were too many requests.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.list_tags_for_resource

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn",
        tags: "capo_internetmonitor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "capo_internetmonitor.types.tag_resource_output.TagResourceOutput":
        """<p>Adds a tag to a resource. Tags are supported only for monitors in Amazon CloudWatch Internet Monitor. You can add a maximum of 50 tags in Internet Monitor.</p> <p>A minimum of one tag is required for this call. It returns an error if you use the <code>TagResource</code> request with 0 tags.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a tag that you add to a resource. Tags are supported only for monitors in Amazon CloudWatch Internet Monitor.</p>
            tags: <p>Tags that you add to a resource. You can add a maximum of 50 tags in Internet Monitor.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.bad_request_exception.BadRequestException: <p>A bad request was received.</p>
            capo_internetmonitor.errors.internal_server_error_exception.InternalServerErrorException: <p>There was an internal server error.</p>
            capo_internetmonitor.errors.not_found_exception.NotFoundException: <p>The request specifies something that doesn't exist.</p>
            capo_internetmonitor.errors.too_many_requests_exception.TooManyRequestsException: <p>There were too many requests.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.tag_resource

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_internetmonitor.types.monitor_arn.MonitorArn",
        tag_keys: "capo_internetmonitor.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "capo_internetmonitor.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a tag you remove a resource from.</p>
            tag_keys: <p>Tag keys that you remove from a resource.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.bad_request_exception.BadRequestException: <p>A bad request was received.</p>
            capo_internetmonitor.errors.internal_server_error_exception.InternalServerErrorException: <p>There was an internal server error.</p>
            capo_internetmonitor.errors.not_found_exception.NotFoundException: <p>The request specifies something that doesn't exist.</p>
            capo_internetmonitor.errors.too_many_requests_exception.TooManyRequestsException: <p>There were too many requests.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.untag_resource

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_internet_event(
        self,
        event_id: "capo_internetmonitor.types.internet_event_id.InternetEventId",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "capo_internetmonitor.types.get_internet_event_output.GetInternetEventOutput":
        """<p>Gets information that Amazon CloudWatch Internet Monitor has generated about an internet event. Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all Amazon Web Services customers. </p> <p>The information returned here includes the impacted location, when the event started and (if the event is over) ended, the type of event (<code>PERFORMANCE</code> or <code>AVAILABILITY</code>), and the status (<code>ACTIVE</code> or <code>RESOLVED</code>).</p>

        Args:
            event_id: <p>The <code>EventId</code> of the internet event to return information for. </p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.get_internet_event_input.GetInternetEventInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.get_internet_event_output.GetInternetEventOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.get_internet_event

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.get_internet_event.get_internet_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.get_internet_event_input.GetInternetEventInput = {
            "event_id": event_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_internet_events(
        self,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.internet_event_max_results.InternetEventMaxResults"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        event_status: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> "capo_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput":
        """<p>Lists internet events that cause performance or availability issues for client locations. Amazon CloudWatch Internet Monitor displays information about recent global health events, called internet events, on a global outages map that is available to all Amazon Web Services customers. </p> <p>You can constrain the list of internet events returned by providing a start time and end time to define a total time frame for events you want to list. Both start time and end time specify the time when an event started. End time is optional. If you don't include it, the default end time is the current time.</p> <p>You can also limit the events returned to a specific status (<code>ACTIVE</code> or <code>RESOLVED</code>) or type (<code>PERFORMANCE</code> or <code>AVAILABILITY</code>).</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>
            start_time: <p>The start time of the time window that you want to get a list of internet events for.</p>
            end_time: <p>The end time of the time window that you want to get a list of internet events for.</p>
            event_status: <p>The status of an internet event.</p>
            event_type: <p>The type of network impairment.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.list_internet_events_input.ListInternetEventsInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.list_internet_events_output.ListInternetEventsOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.list_internet_events

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.list_internet_events.list_internet_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.list_internet_events_input.ListInternetEventsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if event_status is not None:
            input_["event_status"] = event_status
        if event_type is not None:
            input_["event_type"] = event_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_internet_events(
        self,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.internet_event_max_results.InternetEventMaxResults"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        event_status: Optional[str] = None,
        event_type: Optional[str] = None,
    ) -> "Iterator[capo_internetmonitor.types.internet_event_summary.InternetEventSummary]":
        _token = next_token
        while True:
            _response = self.list_internet_events(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                start_time=start_time,
                end_time=end_time,
                event_status=event_status,
                event_type=event_type,
            )
            _page = _resolve_path(_response, ("internet_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_monitor(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        resources: Optional["capo_internetmonitor.types.set_of_ar_ns.SetOfARNs"] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_internetmonitor.types.tag_map.TagMap"] = None,
        max_city_networks_to_monitor: Optional[
            "capo_internetmonitor.types.max_city_networks_to_monitor.MaxCityNetworksToMonitor"
        ] = None,
        internet_measurements_log_delivery: Optional[
            "capo_internetmonitor.types.internet_measurements_log_delivery.InternetMeasurementsLogDelivery"
        ] = None,
        traffic_percentage_to_monitor: Optional[
            "capo_internetmonitor.types.traffic_percentage_to_monitor.TrafficPercentageToMonitor"
        ] = None,
        health_events_config: Optional[
            "capo_internetmonitor.types.health_events_config.HealthEventsConfig"
        ] = None,
    ) -> "capo_internetmonitor.types.create_monitor_output.CreateMonitorOutput":
        r"""<p>Creates a monitor in Amazon CloudWatch Internet Monitor. A monitor is built based on information from the application resources that you add: VPCs, Network Load Balancers (NLBs), Amazon CloudFront distributions, and Amazon WorkSpaces directories. Internet Monitor then publishes internet measurements from Amazon Web Services that are specific to the <i>city-networks</i>. That is, the locations and ASNs (typically internet service providers or ISPs), where clients access your application. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html\">Using Amazon CloudWatch Internet Monitor</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>When you create a monitor, you choose the percentage of traffic that you want to monitor. You can also set a maximum limit for the number of city-networks where client traffic is monitored, that caps the total traffic that Internet Monitor monitors. A city-network maximum is the limit of city-networks, but you only pay for the number of city-networks that are actually monitored. You can update your monitor at any time to change the percentage of traffic to monitor or the city-networks maximum. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html\">Choosing a city-network maximum value</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            monitor_name: <p>The name of the monitor. </p>
            resources: <p>The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.</p> <p>You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.</p> <note> <p>If you add only Amazon VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.</p> </note>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>
            tags: <p>The tags for a monitor. You can add a maximum of 50 tags in Internet Monitor.</p>
            max_city_networks_to_monitor: <p>The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.</p> <p>To learn more, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html\">Choosing a city-network maximum value </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            internet_measurements_log_delivery: <p>Publish internet measurements for Internet Monitor to an Amazon S3 bucket in addition to CloudWatch Logs.</p>
            traffic_percentage_to_monitor: <p>The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html\">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            health_events_config: <p>Defines the threshold percentages and other configuration information for when Amazon CloudWatch Internet Monitor creates a health event. Internet Monitor creates a health event when an internet issue that affects your application end users has a health score percentage that is at or below a specific threshold, and, sometimes, when other criteria are met.</p> <p>If you don't set a health event threshold, the default value is 95%.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview\"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.create_monitor

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.create_monitor.create_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.create_monitor_input.CreateMonitorInput = {
            "monitor_name": monitor_name
        }
        if resources is not None:
            input_["resources"] = resources
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if max_city_networks_to_monitor is not None:
            input_["max_city_networks_to_monitor"] = max_city_networks_to_monitor
        if internet_measurements_log_delivery is not None:
            input_["internet_measurements_log_delivery"] = (
                internet_measurements_log_delivery
            )
        if traffic_percentage_to_monitor is not None:
            input_["traffic_percentage_to_monitor"] = traffic_percentage_to_monitor
        if health_events_config is not None:
            input_["health_events_config"] = health_events_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_monitor(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        linked_account_id: Optional[
            "capo_internetmonitor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_internetmonitor.types.get_monitor_output.GetMonitorOutput":
        r"""<p>Gets information about a monitor in Amazon CloudWatch Internet Monitor based on a monitor name. The information returned includes the Amazon Resource Name (ARN), create time, modified time, resources included in the monitor, and status information.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            linked_account_id: <p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html\">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.get_monitor

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.get_monitor.get_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.get_monitor_input.GetMonitorInput = {
            "monitor_name": monitor_name
        }
        if linked_account_id is not None:
            input_["linked_account_id"] = linked_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_monitor(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        resources_to_add: Optional[
            "capo_internetmonitor.types.set_of_ar_ns.SetOfARNs"
        ] = None,
        resources_to_remove: Optional[
            "capo_internetmonitor.types.set_of_ar_ns.SetOfARNs"
        ] = None,
        status: Optional[
            "capo_internetmonitor.types.monitor_config_state.MonitorConfigState"
        ] = None,
        client_token: Optional[str] = None,
        max_city_networks_to_monitor: Optional[
            "capo_internetmonitor.types.max_city_networks_to_monitor.MaxCityNetworksToMonitor"
        ] = None,
        internet_measurements_log_delivery: Optional[
            "capo_internetmonitor.types.internet_measurements_log_delivery.InternetMeasurementsLogDelivery"
        ] = None,
        traffic_percentage_to_monitor: Optional[
            "capo_internetmonitor.types.traffic_percentage_to_monitor.TrafficPercentageToMonitor"
        ] = None,
        health_events_config: Optional[
            "capo_internetmonitor.types.health_events_config.HealthEventsConfig"
        ] = None,
    ) -> "capo_internetmonitor.types.update_monitor_output.UpdateMonitorOutput":
        r"""<p>Updates a monitor. You can update a monitor to change the percentage of traffic to monitor or the maximum number of city-networks (locations and ASNs), to add or remove resources, or to change the status of the monitor. Note that you can't change the name of a monitor.</p> <p>The city-network maximum that you choose is the limit, but you only pay for the number of city-networks that are actually monitored. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html\">Choosing a city-network maximum value</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            monitor_name: <p>The name of the monitor. </p>
            resources_to_add: <p>The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.</p> <p>You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.</p> <note> <p>If you add only Amazon Virtual Private Clouds resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.</p> </note>
            resources_to_remove: <p>The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).</p>
            status: <p>The status for a monitor. The accepted values for <code>Status</code> with the <code>UpdateMonitor</code> API call are the following: <code>ACTIVE</code> and <code>INACTIVE</code>. The following values are <i>not</i> accepted: <code>PENDING</code>, and <code>ERROR</code>.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. You should not reuse the same client token for other API requests.</p>
            max_city_networks_to_monitor: <p>The maximum number of city-networks to monitor for your application. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.</p>
            internet_measurements_log_delivery: <p>Publish internet measurements for Internet Monitor to another location, such as an Amazon S3 bucket. The measurements are also published to Amazon CloudWatch Logs.</p>
            traffic_percentage_to_monitor: <p>The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html\">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            health_events_config: <p>The list of health score thresholds. A threshold percentage for health scores, along with other configuration information, determines when Internet Monitor creates a health event when there's an internet issue that affects your application end users.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview\"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.update_monitor

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.update_monitor.update_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.update_monitor_input.UpdateMonitorInput = {
            "monitor_name": monitor_name
        }
        if resources_to_add is not None:
            input_["resources_to_add"] = resources_to_add
        if resources_to_remove is not None:
            input_["resources_to_remove"] = resources_to_remove
        if status is not None:
            input_["status"] = status
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if max_city_networks_to_monitor is not None:
            input_["max_city_networks_to_monitor"] = max_city_networks_to_monitor
        if internet_measurements_log_delivery is not None:
            input_["internet_measurements_log_delivery"] = (
                internet_measurements_log_delivery
            )
        if traffic_percentage_to_monitor is not None:
            input_["traffic_percentage_to_monitor"] = traffic_percentage_to_monitor
        if health_events_config is not None:
            input_["health_events_config"] = health_events_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_monitor(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "capo_internetmonitor.types.delete_monitor_output.DeleteMonitorOutput":
        """<p>Deletes a monitor in Amazon CloudWatch Internet Monitor. </p>

        Args:
            monitor_name: <p>The name of the monitor to delete.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.delete_monitor

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.delete_monitor.delete_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.delete_monitor_input.DeleteMonitorInput = {
            "monitor_name": monitor_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_monitors(
        self,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.max_results.MaxResults"
        ] = None,
        monitor_status: Optional[str] = None,
        include_linked_accounts: Optional[bool] = None,
    ) -> "capo_internetmonitor.types.list_monitors_output.ListMonitorsOutput":
        r"""<p>Lists all of your monitors for Amazon CloudWatch Internet Monitor and their statuses, along with the Amazon Resource Name (ARN) and name of each monitor.</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of monitor objects that you want to return with this call.</p>
            monitor_status: <p>The status of a monitor. This includes the status of the data processing for the monitor and the status of the monitor itself.</p> <p>For information about the statuses for a monitor, see <a href=\"https://docs.aws.amazon.com/internet-monitor/latest/api/API_Monitor.html\"> Monitor</a>.</p>
            include_linked_accounts: <p>A boolean option that you can set to <code>TRUE</code> to include monitors for linked accounts in a list of monitors, when you've set up cross-account sharing in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html\">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.list_monitors

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.list_monitors.list_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.list_monitors_input.ListMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if monitor_status is not None:
            input_["monitor_status"] = monitor_status
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_monitors(
        self,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.max_results.MaxResults"
        ] = None,
        monitor_status: Optional[str] = None,
        include_linked_accounts: Optional[bool] = None,
    ) -> "Iterator[capo_internetmonitor.types.monitor.Monitor]":
        _token = next_token
        while True:
            _response = self.list_monitors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                monitor_status=monitor_status,
                include_linked_accounts=include_linked_accounts,
            )
            _page = _resolve_path(_response, ("monitors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_query_results(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.query_max_results.QueryMaxResults"
        ] = None,
    ) -> "capo_internetmonitor.types.get_query_results_output.GetQueryResultsOutput":
        r"""<p>Return the data for a query with the Amazon CloudWatch Internet Monitor query interface. Specify the query that you want to return results for by providing a <code>QueryId</code> and a monitor name.</p> <p>For more information about using the query interface, including examples, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html\">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Args:
            monitor_name: <p>The name of the monitor to return data for.</p>
            query_id: <p>The ID of the query that you want to return data results for. A <code>QueryId</code> is an internally-generated identifier for a specific query.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of query results that you want to return with this call.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.get_query_results_input.GetQueryResultsInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.get_query_results_output.GetQueryResultsOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.get_query_results

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.get_query_results.get_query_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.get_query_results_input.GetQueryResultsInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_query_results(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.query_max_results.QueryMaxResults"
        ] = None,
    ) -> "Iterator[capo_internetmonitor.types.get_query_results_output.GetQueryResultsOutput]":
        _token = next_token
        while True:
            _response = self.get_query_results(
                monitor_name,
                query_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_query_status(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "capo_internetmonitor.types.get_query_status_output.GetQueryStatusOutput":
        """<p>Returns the current status of a query for the Amazon CloudWatch Internet Monitor query interface, for a specified query ID and monitor. When you run a query, check the status to make sure that the query has <code>SUCCEEDED</code> before you review the results.</p> <ul> <li> <p> <code>QUEUED</code>: The query is scheduled to run.</p> </li> <li> <p> <code>RUNNING</code>: The query is in progress but not complete.</p> </li> <li> <p> <code>SUCCEEDED</code>: The query completed sucessfully.</p> </li> <li> <p> <code>FAILED</code>: The query failed due to an error.</p> </li> <li> <p> <code>CANCELED</code>: The query was canceled.</p> </li> </ul>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            query_id: <p>The ID of the query that you want to return the status for. A <code>QueryId</code> is an internally-generated dentifier for a specific query.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.get_query_status_input.GetQueryStatusInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.get_query_status_output.GetQueryStatusOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.get_query_status

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.get_query_status.get_query_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.get_query_status_input.GetQueryStatusInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_query(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        query_type: "capo_internetmonitor.types.query_type.QueryType",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        filter_parameters: Optional[
            "capo_internetmonitor.types.filter_parameters.FilterParameters"
        ] = None,
        linked_account_id: Optional[
            "capo_internetmonitor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_internetmonitor.types.start_query_output.StartQueryOutput":
        r"""<p>Start a query to return data for a specific query type for the Amazon CloudWatch Internet Monitor query interface. Specify a time period for the data that you want returned by using <code>StartTime</code> and <code>EndTime</code>. You filter the query results to return by providing parameters that you specify with <code>FilterParameters</code>.</p> <p>For more information about using the query interface, including examples, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html\">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Args:
            monitor_name: <p>The name of the monitor to query.</p>
            start_time: <p>The timestamp that is the beginning of the period that you want to retrieve data for with your query.</p>
            end_time: <p>The timestamp that is the end of the period that you want to retrieve data for with your query.</p>
            query_type: <p>The type of query to run. The following are the three types of queries that you can run using the Internet Monitor query interface:</p> <ul> <li> <p> <code>MEASUREMENTS</code>: Provides availability score, performance score, total traffic, and round-trip times, at 5 minute intervals.</p> </li> <li> <p> <code>TOP_LOCATIONS</code>: Provides availability score, performance score, total traffic, and time to first byte (TTFB) information, for the top location and ASN combinations that you're monitoring, by traffic volume.</p> </li> <li> <p> <code>TOP_LOCATION_DETAILS</code>: Provides TTFB for Amazon CloudFront, your current configuration, and the best performing EC2 configuration, at 1 hour intervals.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS</code>: Provides TTFB, using a 30-day weighted average, for all traffic in each Amazon Web Services location that is monitored.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS_DETAILS</code>: Provides TTFB, using a 30-day weighted average, for each top location, for a proposed Amazon Web Services location. Must provide an Amazon Web Services location to search.</p> </li> <li> <p> <code>ROUTING_SUGGESTIONS</code>: Provides the predicted average round-trip time (RTT) from an IP prefix toward an Amazon Web Services location for a DNS resolver. The RTT is calculated at one hour intervals, over a one hour period.</p> </li> </ul> <p>For lists of the fields returned with each query type and more information about how each type of query is performed, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html\"> Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>
            filter_parameters: <p>The <code>FilterParameters</code> field that you use with Amazon CloudWatch Internet Monitor queries is a string the defines how you want a query to be filtered. The filter parameters that you can specify depend on the query type, since each query type returns a different set of Internet Monitor data.</p> <p>For more information about specifying filter parameters, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html\">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>
            linked_account_id: <p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html\">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.start_query_input.StartQueryInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.start_query_output.StartQueryOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.start_query

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.start_query.start_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.start_query_input.StartQueryInput = {
            "monitor_name": monitor_name,
            "start_time": start_time,
            "end_time": end_time,
            "query_type": query_type,
        }
        if filter_parameters is not None:
            input_["filter_parameters"] = filter_parameters
        if linked_account_id is not None:
            input_["linked_account_id"] = linked_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_query(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
    ) -> "capo_internetmonitor.types.stop_query_output.StopQueryOutput":
        """<p>Stop a query that is progress for a specific monitor.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            query_id: <p>The ID of the query that you want to stop. A <code>QueryId</code> is an internally-generated identifier for a specific query.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.stop_query_input.StopQueryInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.stop_query_output.StopQueryOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.stop_query

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.stop_query.stop_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.stop_query_input.StopQueryInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_health_event(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        event_id: "capo_internetmonitor.types.health_event_name.HealthEventName",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        linked_account_id: Optional[
            "capo_internetmonitor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_internetmonitor.types.get_health_event_output.GetHealthEventOutput":
        r"""<p>Gets information that Amazon CloudWatch Internet Monitor has created and stored about a health event for a specified monitor. This information includes the impacted locations, and all the information related to the event, by location.</p> <p>The information returned includes the impact on performance, availability, and round-trip time, information about the network providers (ASNs), the event type, and so on.</p> <p>Information rolled up at the global traffic level is also returned, including the impact type and total traffic impact.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            event_id: <p>The internally-generated identifier of a health event. Because <code>EventID</code> contains the forward slash (“/”) character, you must URL-encode the <code>EventID</code> field in the request URL.</p>
            linked_account_id: <p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html\">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.get_health_event_input.GetHealthEventInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.get_health_event_output.GetHealthEventOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.get_health_event

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.get_health_event.get_health_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.get_health_event_input.GetHealthEventInput = {
            "monitor_name": monitor_name,
            "event_id": event_id,
        }
        if linked_account_id is not None:
            input_["linked_account_id"] = linked_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_health_events(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.max_results.MaxResults"
        ] = None,
        event_status: Optional[
            "capo_internetmonitor.types.health_event_status.HealthEventStatus"
        ] = None,
        linked_account_id: Optional[
            "capo_internetmonitor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_internetmonitor.types.list_health_events_output.ListHealthEventsOutput":
        r"""<p>Lists all health events for a monitor in Amazon CloudWatch Internet Monitor. Returns information for health events including the event start and end times, and the status.</p> <note> <p>Health events that have start times during the time frame that is requested are not included in the list of health events.</p> </note>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            start_time: <p>The time when a health event started.</p>
            end_time: <p>The time when a health event ended. If the health event is still ongoing, then the end time is not set.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of health event objects that you want to return with this call. </p>
            event_status: <p>The status of a health event.</p>
            linked_account_id: <p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html\">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_internetmonitor.types.list_health_events_input.ListHealthEventsInput]",
        ) -> OperationResponse[
            "capo_internetmonitor.types.list_health_events_output.ListHealthEventsOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.list_health_events

            output, http_response = (
                capo_internetmonitor._operations.internet_monitor20210603.list_health_events.list_health_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_internetmonitor.types.list_health_events_input.ListHealthEventsInput = {
            "monitor_name": monitor_name
        }
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if event_status is not None:
            input_["event_status"] = event_status
        if linked_account_id is not None:
            input_["linked_account_id"] = linked_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_health_events(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.max_results.MaxResults"
        ] = None,
        event_status: Optional[
            "capo_internetmonitor.types.health_event_status.HealthEventStatus"
        ] = None,
        linked_account_id: Optional[
            "capo_internetmonitor.types.account_id.AccountId"
        ] = None,
    ) -> "Iterator[capo_internetmonitor.types.health_event.HealthEvent]":
        _token = next_token
        while True:
            _response = self.list_health_events(
                monitor_name,
                config_overrides=config_overrides,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                max_results=max_results,
                event_status=event_status,
                linked_account_id=linked_account_id,
            )
            _page = _resolve_path(_response, ("health_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
