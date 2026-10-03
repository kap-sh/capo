from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Optional

import capo_internetmonitor._auth._signers
import capo_internetmonitor._auth._sigv4
from capo_internetmonitor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_internetmonitor.types.account_id
    import capo_internetmonitor.types.create_monitor_input
    import capo_internetmonitor.types.create_monitor_output
    import capo_internetmonitor.types.delete_monitor_input
    import capo_internetmonitor.types.delete_monitor_output
    import capo_internetmonitor.types.filter_parameters
    import capo_internetmonitor.types.get_monitor_input
    import capo_internetmonitor.types.get_monitor_output
    import capo_internetmonitor.types.get_query_results_input
    import capo_internetmonitor.types.get_query_results_output
    import capo_internetmonitor.types.get_query_status_input
    import capo_internetmonitor.types.get_query_status_output
    import capo_internetmonitor.types.health_events_config
    import capo_internetmonitor.types.internet_measurements_log_delivery
    import capo_internetmonitor.types.list_monitors_input
    import capo_internetmonitor.types.list_monitors_output
    import capo_internetmonitor.types.max_city_networks_to_monitor
    import capo_internetmonitor.types.max_results
    import capo_internetmonitor.types.monitor
    import capo_internetmonitor.types.monitor_config_state
    import capo_internetmonitor.types.query_max_results
    import capo_internetmonitor.types.query_type
    import capo_internetmonitor.types.resource_name
    import capo_internetmonitor.types.set_of_ar_ns
    import capo_internetmonitor.types.start_query_input
    import capo_internetmonitor.types.start_query_output
    import capo_internetmonitor.types.stop_query_input
    import capo_internetmonitor.types.stop_query_output
    import capo_internetmonitor.types.tag_map
    import capo_internetmonitor.types.traffic_percentage_to_monitor
    import capo_internetmonitor.types.update_monitor_input
    import capo_internetmonitor.types.update_monitor_output
    from capo_internetmonitor._services.async_internet_monitor import (
        AsyncInternetMonitorClient,
        AsyncInternetMonitorClientConfig,
    )
    from capo_internetmonitor._services.internet_monitor import (
        InternetMonitorClient,
        InternetMonitorClientConfig,
    )


class MonitorResource:
    def __init__(self, service: InternetMonitorClient) -> None:
        self._service = service

    def put(
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
        """<p>Creates a monitor in Amazon CloudWatch Internet Monitor. A monitor is built based on information from the application resources that you add: VPCs, Network Load Balancers (NLBs), Amazon CloudFront distributions, and Amazon WorkSpaces directories. Internet Monitor then publishes internet measurements from Amazon Web Services that are specific to the <i>city-networks</i>. That is, the locations and ASNs (typically internet service providers or ISPs), where clients access your application. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html">Using Amazon CloudWatch Internet Monitor</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>When you create a monitor, you choose the percentage of traffic that you want to monitor. You can also set a maximum limit for the number of city-networks where client traffic is monitored, that caps the total traffic that Internet Monitor monitors. A city-network maximum is the limit of city-networks, but you only pay for the number of city-networks that are actually monitored. You can update your monitor at any time to change the percentage of traffic to monitor or the city-networks maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html">Choosing a city-network maximum value</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            monitor_name: <p>The name of the monitor. </p>
            resources: <p>The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.</p> <p>You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.</p> <note> <p>If you add only Amazon VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.</p> </note>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>
            tags: <p>The tags for a monitor. You can add a maximum of 50 tags in Internet Monitor.</p>
            max_city_networks_to_monitor: <p>The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html">Choosing a city-network maximum value </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            internet_measurements_log_delivery: <p>Publish internet measurements for Internet Monitor to an Amazon S3 bucket in addition to CloudWatch Logs.</p>
            traffic_percentage_to_monitor: <p>The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            health_events_config: <p>Defines the threshold percentages and other configuration information for when Amazon CloudWatch Internet Monitor creates a health event. Internet Monitor creates a health event when an internet issue that affects your application end users has a health score percentage that is at or below a specific threshold, and, sometimes, when other criteria are met.</p> <p>If you don't set a health event threshold, the default value is 95%.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[InternetMonitorClientConfig] = None,
        linked_account_id: Optional[
            "capo_internetmonitor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_internetmonitor.types.get_monitor_output.GetMonitorOutput":
        """<p>Gets information about a monitor in Amazon CloudWatch Internet Monitor based on a monitor name. The information returned includes the Amazon Resource Name (ARN), create time, modified time, resources included in the monitor, and status information.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            linked_account_id: <p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def update(
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
        """<p>Updates a monitor. You can update a monitor to change the percentage of traffic to monitor or the maximum number of city-networks (locations and ASNs), to add or remove resources, or to change the status of the monitor. Note that you can't change the name of a monitor.</p> <p>The city-network maximum that you choose is the limit, but you only pay for the number of city-networks that are actually monitored. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html">Choosing a city-network maximum value</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            monitor_name: <p>The name of the monitor. </p>
            resources_to_add: <p>The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.</p> <p>You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.</p> <note> <p>If you add only Amazon Virtual Private Clouds resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.</p> </note>
            resources_to_remove: <p>The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).</p>
            status: <p>The status for a monitor. The accepted values for <code>Status</code> with the <code>UpdateMonitor</code> API call are the following: <code>ACTIVE</code> and <code>INACTIVE</code>. The following values are <i>not</i> accepted: <code>PENDING</code>, and <code>ERROR</code>.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. You should not reuse the same client token for other API requests.</p>
            max_city_networks_to_monitor: <p>The maximum number of city-networks to monitor for your application. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.</p>
            internet_measurements_log_delivery: <p>Publish internet measurements for Internet Monitor to another location, such as an Amazon S3 bucket. The measurements are also published to Amazon CloudWatch Logs.</p>
            traffic_percentage_to_monitor: <p>The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            health_events_config: <p>The list of health score thresholds. A threshold percentage for health scores, along with other configuration information, determines when Internet Monitor creates a health event when there's an internet issue that affects your application end users.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def list(
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
        """<p>Lists all of your monitors for Amazon CloudWatch Internet Monitor and their statuses, along with the Amazon Resource Name (ARN) and name of each monitor.</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of monitor objects that you want to return with this call.</p>
            monitor_status: <p>The status of a monitor. This includes the status of the data processing for the monitor and the status of the monitor itself.</p> <p>For information about the statuses for a monitor, see <a href="https://docs.aws.amazon.com/internet-monitor/latest/api/API_Monitor.html"> Monitor</a>.</p>
            include_linked_accounts: <p>A boolean option that you can set to <code>TRUE</code> to include monitors for linked accounts in a list of monitors, when you've set up cross-account sharing in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
        """<p>Return the data for a query with the Amazon CloudWatch Internet Monitor query interface. Specify the query that you want to return results for by providing a <code>QueryId</code> and a monitor name.</p> <p>For more information about using the query interface, including examples, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
        """<p>Start a query to return data for a specific query type for the Amazon CloudWatch Internet Monitor query interface. Specify a time period for the data that you want returned by using <code>StartTime</code> and <code>EndTime</code>. You filter the query results to return by providing parameters that you specify with <code>FilterParameters</code>.</p> <p>For more information about using the query interface, including examples, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Args:
            monitor_name: <p>The name of the monitor to query.</p>
            start_time: <p>The timestamp that is the beginning of the period that you want to retrieve data for with your query.</p>
            end_time: <p>The timestamp that is the end of the period that you want to retrieve data for with your query.</p>
            query_type: <p>The type of query to run. The following are the three types of queries that you can run using the Internet Monitor query interface:</p> <ul> <li> <p> <code>MEASUREMENTS</code>: Provides availability score, performance score, total traffic, and round-trip times, at 5 minute intervals.</p> </li> <li> <p> <code>TOP_LOCATIONS</code>: Provides availability score, performance score, total traffic, and time to first byte (TTFB) information, for the top location and ASN combinations that you're monitoring, by traffic volume.</p> </li> <li> <p> <code>TOP_LOCATION_DETAILS</code>: Provides TTFB for Amazon CloudFront, your current configuration, and the best performing EC2 configuration, at 1 hour intervals.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS</code>: Provides TTFB, using a 30-day weighted average, for all traffic in each Amazon Web Services location that is monitored.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS_DETAILS</code>: Provides TTFB, using a 30-day weighted average, for each top location, for a proposed Amazon Web Services location. Must provide an Amazon Web Services location to search.</p> </li> <li> <p> <code>ROUTING_SUGGESTIONS</code>: Provides the predicted average round-trip time (RTT) from an IP prefix toward an Amazon Web Services location for a DNS resolver. The RTT is calculated at one hour intervals, over a one hour period.</p> </li> </ul> <p>For lists of the fields returned with each query type and more information about how each type of query is performed, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html"> Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>
            filter_parameters: <p>The <code>FilterParameters</code> field that you use with Amazon CloudWatch Internet Monitor queries is a string the defines how you want a query to be filtered. The filter parameters that you can specify depend on the query type, since each query type returns a different set of Internet Monitor data.</p> <p>For more information about specifying filter parameters, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>
            linked_account_id: <p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncMonitorResource:
    def __init__(self, service: AsyncInternetMonitorClient) -> None:
        self._service = service

    async def put(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
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
        """<p>Creates a monitor in Amazon CloudWatch Internet Monitor. A monitor is built based on information from the application resources that you add: VPCs, Network Load Balancers (NLBs), Amazon CloudFront distributions, and Amazon WorkSpaces directories. Internet Monitor then publishes internet measurements from Amazon Web Services that are specific to the <i>city-networks</i>. That is, the locations and ASNs (typically internet service providers or ISPs), where clients access your application. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html">Using Amazon CloudWatch Internet Monitor</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>When you create a monitor, you choose the percentage of traffic that you want to monitor. You can also set a maximum limit for the number of city-networks where client traffic is monitored, that caps the total traffic that Internet Monitor monitors. A city-network maximum is the limit of city-networks, but you only pay for the number of city-networks that are actually monitored. You can update your monitor at any time to change the percentage of traffic to monitor or the city-networks maximum. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html">Choosing a city-network maximum value</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            monitor_name: <p>The name of the monitor. </p>
            resources: <p>The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.</p> <p>You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.</p> <note> <p>If you add only Amazon VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.</p> </note>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>
            tags: <p>The tags for a monitor. You can add a maximum of 50 tags in Internet Monitor.</p>
            max_city_networks_to_monitor: <p>The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html">Choosing a city-network maximum value </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            internet_measurements_log_delivery: <p>Publish internet measurements for Internet Monitor to an Amazon S3 bucket in addition to CloudWatch Logs.</p>
            traffic_percentage_to_monitor: <p>The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            health_events_config: <p>Defines the threshold percentages and other configuration information for when Amazon CloudWatch Internet Monitor creates a health event. Internet Monitor creates a health event when an internet issue that affects your application end users has a health score percentage that is at or below a specific threshold, and, sometimes, when other criteria are met.</p> <p>If you don't set a health event threshold, the default value is 95%.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.conflict_exception.ConflictException: <p>The requested resource is in use.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.create_monitor_input.CreateMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.create_monitor_output.CreateMonitorOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.create_monitor

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.create_monitor.async_create_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
        linked_account_id: Optional[
            "capo_internetmonitor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_internetmonitor.types.get_monitor_output.GetMonitorOutput":
        """<p>Gets information about a monitor in Amazon CloudWatch Internet Monitor based on a monitor name. The information returned includes the Amazon Resource Name (ARN), create time, modified time, resources included in the monitor, and status information.</p>

        Args:
            monitor_name: <p>The name of the monitor.</p>
            linked_account_id: <p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.get_monitor_input.GetMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.get_monitor_output.GetMonitorOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.get_monitor

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.get_monitor.async_get_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_internetmonitor.types.get_monitor_input.GetMonitorInput = {
            "monitor_name": monitor_name
        }
        if linked_account_id is not None:
            input_["linked_account_id"] = linked_account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
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
        """<p>Updates a monitor. You can update a monitor to change the percentage of traffic to monitor or the maximum number of city-networks (locations and ASNs), to add or remove resources, or to change the status of the monitor. Note that you can't change the name of a monitor.</p> <p>The city-network maximum that you choose is the limit, but you only pay for the number of city-networks that are actually monitored. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html">Choosing a city-network maximum value</a> in the <i>Amazon CloudWatch User Guide</i>.</p>

        Args:
            monitor_name: <p>The name of the monitor. </p>
            resources_to_add: <p>The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.</p> <p>You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.</p> <note> <p>If you add only Amazon Virtual Private Clouds resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.</p> </note>
            resources_to_remove: <p>The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).</p>
            status: <p>The status for a monitor. The accepted values for <code>Status</code> with the <code>UpdateMonitor</code> API call are the following: <code>ACTIVE</code> and <code>INACTIVE</code>. The following values are <i>not</i> accepted: <code>PENDING</code>, and <code>ERROR</code>.</p>
            client_token: <p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. You should not reuse the same client token for other API requests.</p>
            max_city_networks_to_monitor: <p>The maximum number of city-networks to monitor for your application. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.</p>
            internet_measurements_log_delivery: <p>Publish internet measurements for Internet Monitor to another location, such as an Amazon S3 bucket. The measurements are also published to Amazon CloudWatch Logs.</p>
            traffic_percentage_to_monitor: <p>The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>
            health_events_config: <p>The list of health score thresholds. A threshold percentage for health scores, along with other configuration information, determines when Internet Monitor creates a health event when there's an internet issue that affects your application end users.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request specifies a resource that doesn't exist.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.update_monitor_input.UpdateMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.update_monitor_output.UpdateMonitorOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.update_monitor

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.update_monitor.async_update_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.delete_monitor_input.DeleteMonitorInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.delete_monitor_output.DeleteMonitorOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.delete_monitor

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.delete_monitor.async_delete_monitor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_internetmonitor.types.delete_monitor_input.DeleteMonitorInput = {
            "monitor_name": monitor_name
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
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.max_results.MaxResults"
        ] = None,
        monitor_status: Optional[str] = None,
        include_linked_accounts: Optional[bool] = None,
    ) -> "capo_internetmonitor.types.list_monitors_output.ListMonitorsOutput":
        """<p>Lists all of your monitors for Amazon CloudWatch Internet Monitor and their statuses, along with the Amazon Resource Name (ARN) and name of each monitor.</p>

        Args:
            next_token: <p>The token for the next set of results. You receive this token from a previous call.</p>
            max_results: <p>The number of monitor objects that you want to return with this call.</p>
            monitor_status: <p>The status of a monitor. This includes the status of the data processing for the monitor and the status of the monitor itself.</p> <p>For information about the statuses for a monitor, see <a href="https://docs.aws.amazon.com/internet-monitor/latest/api/API_Monitor.html"> Monitor</a>.</p>
            include_linked_accounts: <p>A boolean option that you can set to <code>TRUE</code> to include monitors for linked accounts in a list of monitors, when you've set up cross-account sharing in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.list_monitors_input.ListMonitorsInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.list_monitors_output.ListMonitorsOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.list_monitors

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.list_monitors.async_list_monitors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_internetmonitor.types.list_monitors_input.ListMonitorsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if monitor_status is not None:
            input_["monitor_status"] = monitor_status
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_query_results(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_internetmonitor.types.query_max_results.QueryMaxResults"
        ] = None,
    ) -> "capo_internetmonitor.types.get_query_results_output.GetQueryResultsOutput":
        """<p>Return the data for a query with the Amazon CloudWatch Internet Monitor query interface. Specify the query that you want to return results for by providing a <code>QueryId</code> and a monitor name.</p> <p>For more information about using the query interface, including examples, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

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

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.get_query_results_input.GetQueryResultsInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.get_query_results_output.GetQueryResultsOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.get_query_results

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.get_query_results.async_get_query_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_internetmonitor.types.get_query_results_input.GetQueryResultsInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }
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

    async def get_query_status(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.get_query_status_input.GetQueryStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.get_query_status_output.GetQueryStatusOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.get_query_status

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.get_query_status.async_get_query_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_internetmonitor.types.get_query_status_input.GetQueryStatusInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_query(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        query_type: "capo_internetmonitor.types.query_type.QueryType",
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
        filter_parameters: Optional[
            "capo_internetmonitor.types.filter_parameters.FilterParameters"
        ] = None,
        linked_account_id: Optional[
            "capo_internetmonitor.types.account_id.AccountId"
        ] = None,
    ) -> "capo_internetmonitor.types.start_query_output.StartQueryOutput":
        """<p>Start a query to return data for a specific query type for the Amazon CloudWatch Internet Monitor query interface. Specify a time period for the data that you want returned by using <code>StartTime</code> and <code>EndTime</code>. You filter the query results to return by providing parameters that you specify with <code>FilterParameters</code>.</p> <p>For more information about using the query interface, including examples, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Args:
            monitor_name: <p>The name of the monitor to query.</p>
            start_time: <p>The timestamp that is the beginning of the period that you want to retrieve data for with your query.</p>
            end_time: <p>The timestamp that is the end of the period that you want to retrieve data for with your query.</p>
            query_type: <p>The type of query to run. The following are the three types of queries that you can run using the Internet Monitor query interface:</p> <ul> <li> <p> <code>MEASUREMENTS</code>: Provides availability score, performance score, total traffic, and round-trip times, at 5 minute intervals.</p> </li> <li> <p> <code>TOP_LOCATIONS</code>: Provides availability score, performance score, total traffic, and time to first byte (TTFB) information, for the top location and ASN combinations that you're monitoring, by traffic volume.</p> </li> <li> <p> <code>TOP_LOCATION_DETAILS</code>: Provides TTFB for Amazon CloudFront, your current configuration, and the best performing EC2 configuration, at 1 hour intervals.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS</code>: Provides TTFB, using a 30-day weighted average, for all traffic in each Amazon Web Services location that is monitored.</p> </li> <li> <p> <code>OVERALL_TRAFFIC_SUGGESTIONS_DETAILS</code>: Provides TTFB, using a 30-day weighted average, for each top location, for a proposed Amazon Web Services location. Must provide an Amazon Web Services location to search.</p> </li> <li> <p> <code>ROUTING_SUGGESTIONS</code>: Provides the predicted average round-trip time (RTT) from an IP prefix toward an Amazon Web Services location for a DNS resolver. The RTT is calculated at one hour intervals, over a one hour period.</p> </li> </ul> <p>For lists of the fields returned with each query type and more information about how each type of query is performed, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html"> Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>
            filter_parameters: <p>The <code>FilterParameters</code> field that you use with Amazon CloudWatch Internet Monitor queries is a string the defines how you want a query to be filtered. The filter parameters that you can specify depend on the query type, since each query type returns a different set of Internet Monitor data.</p> <p>For more information about specifying filter parameters, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html">Using the Amazon CloudWatch Internet Monitor query interface</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>
            linked_account_id: <p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>

        Raises:
            capo_internetmonitor.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permission to perform this action.</p>
            capo_internetmonitor.errors.internal_server_exception.InternalServerException: <p>An internal error occurred.</p>
            capo_internetmonitor.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeded a service quota.</p>
            capo_internetmonitor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_internetmonitor.errors.validation_exception.ValidationException: <p>Invalid request.</p>
            capo_internetmonitor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.start_query_input.StartQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.start_query_output.StartQueryOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.start_query

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.start_query.async_start_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_query(
        self,
        monitor_name: "capo_internetmonitor.types.resource_name.ResourceName",
        query_id: str,
        *,
        config_overrides: Optional[AsyncInternetMonitorClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_internetmonitor.types.stop_query_input.StopQueryInput]",
        ) -> AsyncOperationResponse[
            "capo_internetmonitor.types.stop_query_output.StopQueryOutput"
        ]:
            import capo_internetmonitor._operations.internet_monitor20210603.stop_query

            (
                output,
                http_response,
            ) = await capo_internetmonitor._operations.internet_monitor20210603.stop_query.async_stop_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_internetmonitor.types.stop_query_input.StopQueryInput = {
            "monitor_name": monitor_name,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
