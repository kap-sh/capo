from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_application_signals._auth._signers
import capo_application_signals._auth._sigv4
from capo_application_signals._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_application_signals.types.attributes
    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.burn_rate_configurations
    import capo_application_signals.types.create_service_level_objective_input
    import capo_application_signals.types.create_service_level_objective_output
    import capo_application_signals.types.delete_service_level_objective_input
    import capo_application_signals.types.delete_service_level_objective_output
    import capo_application_signals.types.dependency_config
    import capo_application_signals.types.get_service_level_objective_input
    import capo_application_signals.types.get_service_level_objective_output
    import capo_application_signals.types.goal
    import capo_application_signals.types.list_service_level_objectives_input
    import capo_application_signals.types.list_service_level_objectives_max_results
    import capo_application_signals.types.list_service_level_objectives_output
    import capo_application_signals.types.metric_source
    import capo_application_signals.types.metric_source_types
    import capo_application_signals.types.next_token
    import capo_application_signals.types.operation_name
    import capo_application_signals.types.request_based_service_level_indicator_config
    import capo_application_signals.types.service_level_indicator_config
    import capo_application_signals.types.service_level_objective_description
    import capo_application_signals.types.service_level_objective_id
    import capo_application_signals.types.service_level_objective_name
    import capo_application_signals.types.service_level_objective_summary
    import capo_application_signals.types.tag_list
    import capo_application_signals.types.update_service_level_objective_input
    import capo_application_signals.types.update_service_level_objective_output
    from capo_application_signals._services.application_signals import (
        ApplicationSignalsClient,
        ApplicationSignalsClientConfig,
    )
    from capo_application_signals._services.async_application_signals import (
        AsyncApplicationSignalsClient,
        AsyncApplicationSignalsClientConfig,
    )


class ServiceLevelObjectiveResource:
    def __init__(self, service: ApplicationSignalsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        description: Optional[
            "capo_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
        ] = None,
        sli_config: Optional[
            "capo_application_signals.types.service_level_indicator_config.ServiceLevelIndicatorConfig"
        ] = None,
        request_based_sli_config: Optional[
            "capo_application_signals.types.request_based_service_level_indicator_config.RequestBasedServiceLevelIndicatorConfig"
        ] = None,
        goal: Optional["capo_application_signals.types.goal.Goal"] = None,
        tags: Optional["capo_application_signals.types.tag_list.TagList"] = None,
        burn_rate_configurations: Optional[
            "capo_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
        ] = None,
        create_recommended_slo: Optional[bool] = None,
        auto_investigation_enabled: Optional[bool] = None,
    ) -> "capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput":
        """<p>Creates a service level objective (SLO), which can help you ensure that your critical business operations are meeting customer expectations. Use SLOs to set and track specific target levels for the reliability and availability of your applications and services. SLOs use service level indicators (SLIs) to calculate whether the application is performing at the level that you want.</p> <p>Create an SLO to set a target for a service or operation’s availability or latency. CloudWatch measures this target frequently you can find whether it has been breached. </p> <p>The target performance quality that is defined for an SLO is the <i>attainment goal</i>.</p> <p>You can set SLO targets for your applications that are discovered by Application Signals, using critical metrics such as latency and availability. You can also set SLOs against any CloudWatch metric or math expression that produces a time series.</p> <note> <p>You can't create an SLO for a service operation that was discovered by Application Signals until after that operation has reported standard metrics to Application Signals.</p> </note> <p>When you create an SLO, you specify whether it is a <i>period-based SLO</i> or a <i>request-based SLO</i>. Each type of SLO has a different way of evaluating your application's performance against its attainment goal.</p> <ul> <li> <p>A <i>period-based SLO</i> uses defined <i>periods</i> of time within a specified total time interval. For each period of time, Application Signals determines whether the application met its goal. The attainment rate is calculated as the <code>number of good periods/number of total periods</code>.</p> <p>For example, for a period-based SLO, meeting an attainment goal of 99.9% means that within your interval, your application must meet its performance goal during at least 99.9% of the time periods.</p> </li> <li> <p>A <i>request-based SLO</i> doesn't use pre-defined periods of time. Instead, the SLO measures <code>number of good requests/number of total requests</code> during the interval. At any time, you can find the ratio of good requests to total requests for the interval up to the time stamp that you specify, and measure that ratio against the goal set in your SLO.</p> </li> </ul> <p>After you have created an SLO, you can retrieve error budget reports for it. An <i>error budget</i> is the amount of time or amount of requests that your application can be non-compliant with the SLO's goal, and still have your application meet the goal.</p> <ul> <li> <p>For a period-based SLO, the error budget starts at a number defined by the highest number of periods that can fail to meet the threshold, while still meeting the overall goal. The <i>remaining error budget</i> decreases with every failed period that is recorded. The error budget within one interval can never increase.</p> <p>For example, an SLO with a threshold that 99.95% of requests must be completed under 2000ms every month translates to an error budget of 21.9 minutes of downtime per month.</p> </li> <li> <p>For a request-based SLO, the remaining error budget is dynamic and can increase or decrease, depending on the ratio of good requests to total requests.</p> </li> </ul> <p>For more information about SLOs, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html"> Service level objectives (SLOs)</a>. </p> <p>When you perform a <code>CreateServiceLevelObjective</code> operation, Application Signals creates the <i>AWSServiceRoleForCloudWatchApplicationSignals</i> service-linked role, if it doesn't already exist in your account. This service- linked role has the following permissions:</p> <ul> <li> <p> <code>xray:GetServiceGraph</code> </p> </li> <li> <p> <code>logs:StartQuery</code> </p> </li> <li> <p> <code>logs:GetQueryResults</code> </p> </li> <li> <p> <code>cloudwatch:GetMetricData</code> </p> </li> <li> <p> <code>cloudwatch:ListMetrics</code> </p> </li> <li> <p> <code>tag:GetResources</code> </p> </li> <li> <p> <code>autoscaling:DescribeAutoScalingGroups</code> </p> </li> </ul>

        Args:
            name: <p>A name for this SLO.</p>
            description: <p>An optional description for this SLO.</p>
            sli_config: <p>If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>RequestBasedSliConfig</code> and <code>SliConfig</code> in the same operation.</p>
            request_based_sli_config: <p>If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>RequestBasedSliConfig</code> and <code>SliConfig</code> in the same operation.</p>
            goal: <p>This structure contains the attributes that determine the goal of the SLO.</p>
            tags: <p>A list of key-value pairs to associate with the SLO. You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p>
            burn_rate_configurations: <p>Use this array to create <i>burn rates</i> for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>
            create_recommended_slo: <p>Set this to <code>true</code> to create a recommended SLO out of the box. When set to <code>true</code>, you don't need to specify the <code>MetricThreshold</code> or <code>ComparisonOperator</code> in the <code>SliConfig</code> or <code>RequestBasedSliConfig</code>. The default value is <code>false</code>.</p> <p>This is supported for SLOs on a service, service operation, or a dependency.</p>
            auto_investigation_enabled: Indicates whether DevOps Agent will automatically investigate this SLO when it is breached

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_application_signals.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.create_service_level_objective

            output, http_response = (
                capo_application_signals._operations.application_signals.create_service_level_objective.create_service_level_objective(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sli_config is not None:
            input_["sli_config"] = sli_config
        if request_based_sli_config is not None:
            input_["request_based_sli_config"] = request_based_sli_config
        if goal is not None:
            input_["goal"] = goal
        if tags is not None:
            input_["tags"] = tags
        if burn_rate_configurations is not None:
            input_["burn_rate_configurations"] = burn_rate_configurations
        if create_recommended_slo is not None:
            input_["create_recommended_slo"] = create_recommended_slo
        if auto_investigation_enabled is not None:
            input_["auto_investigation_enabled"] = auto_investigation_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.get_service_level_objective_output.GetServiceLevelObjectiveOutput":
        """<p>Returns information about one SLO created in the account. </p>

        Args:
            id: <p>The ARN or name of the SLO that you want to retrieve information about. You can find the ARNs of SLOs by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListServiceLevelObjectives.html">ListServiceLevelObjectives</a> operation.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.get_service_level_objective_input.GetServiceLevelObjectiveInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.get_service_level_objective_output.GetServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.get_service_level_objective

            output, http_response = (
                capo_application_signals._operations.application_signals.get_service_level_objective.get_service_level_objective(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.get_service_level_objective_input.GetServiceLevelObjectiveInput = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        description: Optional[
            "capo_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
        ] = None,
        sli_config: Optional[
            "capo_application_signals.types.service_level_indicator_config.ServiceLevelIndicatorConfig"
        ] = None,
        request_based_sli_config: Optional[
            "capo_application_signals.types.request_based_service_level_indicator_config.RequestBasedServiceLevelIndicatorConfig"
        ] = None,
        goal: Optional["capo_application_signals.types.goal.Goal"] = None,
        burn_rate_configurations: Optional[
            "capo_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
        ] = None,
        auto_investigation_enabled: Optional[bool] = None,
    ) -> "capo_application_signals.types.update_service_level_objective_output.UpdateServiceLevelObjectiveOutput":
        """<p>Updates an existing service level objective (SLO). If you omit parameters, the previous values of those parameters are retained. </p> <p>You cannot change from a period-based SLO to a request-based SLO, or change from a request-based SLO to a period-based SLO.</p>

        Args:
            id: <p>The Amazon Resource Name (ARN) or name of the service level objective that you want to update.</p>
            description: <p>An optional description for the SLO.</p>
            sli_config: <p>If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p>
            request_based_sli_config: <p>If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>SliConfig</code> and <code>RequestBasedSliConfig</code> in the same operation.</p>
            goal: <p>A structure that contains the attributes that determine the goal of the SLO. This includes the time period for evaluation and the attainment threshold.</p>
            burn_rate_configurations: <p>Use this array to create <i>burn rates</i> for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>
            auto_investigation_enabled: Indicates whether DevOps Agent will automatically investigate this SLO when it is breached

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.update_service_level_objective_input.UpdateServiceLevelObjectiveInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.update_service_level_objective_output.UpdateServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.update_service_level_objective

            output, http_response = (
                capo_application_signals._operations.application_signals.update_service_level_objective.update_service_level_objective(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.update_service_level_objective_input.UpdateServiceLevelObjectiveInput = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if sli_config is not None:
            input_["sli_config"] = sli_config
        if request_based_sli_config is not None:
            input_["request_based_sli_config"] = request_based_sli_config
        if goal is not None:
            input_["goal"] = goal
        if burn_rate_configurations is not None:
            input_["burn_rate_configurations"] = burn_rate_configurations
        if auto_investigation_enabled is not None:
            input_["auto_investigation_enabled"] = auto_investigation_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.delete_service_level_objective_output.DeleteServiceLevelObjectiveOutput":
        """<p>Deletes the specified service level objective.</p>

        Args:
            id: <p>The ARN or name of the service level objective to delete.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.delete_service_level_objective_input.DeleteServiceLevelObjectiveInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.delete_service_level_objective_output.DeleteServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.delete_service_level_objective

            output, http_response = (
                capo_application_signals._operations.application_signals.delete_service_level_objective.delete_service_level_objective(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.delete_service_level_objective_input.DeleteServiceLevelObjectiveInput = {
            "id": id
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
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        key_attributes: Optional[
            "capo_application_signals.types.attributes.Attributes"
        ] = None,
        operation_name: Optional[
            "capo_application_signals.types.operation_name.OperationName"
        ] = None,
        dependency_config: Optional[
            "capo_application_signals.types.dependency_config.DependencyConfig"
        ] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_level_objectives_max_results.ListServiceLevelObjectivesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        metric_source_types: Optional[
            "capo_application_signals.types.metric_source_types.MetricSourceTypes"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        slo_owner_aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        metric_source: Optional[
            "capo_application_signals.types.metric_source.MetricSource"
        ] = None,
    ) -> "capo_application_signals.types.list_service_level_objectives_output.ListServiceLevelObjectivesOutput":
        """<p>Returns a list of SLOs created in this account.</p>

        Args:
            key_attributes: <p>You can use this optional field to specify which services you want to retrieve SLO information for.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            operation_name: <p>The name of the operation that this SLO is associated with.</p>
            dependency_config: <p>Identifies the dependency using the <code>DependencyKeyAttributes</code> and <code>DependencyOperationName</code>. </p>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives.</p>
            metric_source_types: <p>Use this optional field to only include SLOs with the specified metric source types in the output. Supported types are:</p> <ul> <li> <p>Service operation</p> </li> <li> <p>Service dependency</p> </li> <li> <p>Service</p> </li> <li> <p>CloudWatch metric</p> </li> <li> <p>AppMonitor</p> </li> <li> <p>Canary</p> </li> </ul>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include SLO from source accounts in the returned data. </p> <p>When you are monitoring an account, you can use Amazon Web Services account ID in <code>KeyAttribute</code> filter for service source account and <code>SloOwnerawsaccountID</code> for SLO source account with <code>IncludeLinkedAccounts</code> to filter the returned data to only a single source account. </p>
            slo_owner_aws_account_id: <p>SLO's Amazon Web Services account ID.</p>
            metric_source: <p>Identifies the metric source to filter SLOs by.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_level_objectives_input.ListServiceLevelObjectivesInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_level_objectives_output.ListServiceLevelObjectivesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_level_objectives

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_level_objectives.list_service_level_objectives(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_level_objectives_input.ListServiceLevelObjectivesInput = {}
        if key_attributes is not None:
            input_["key_attributes"] = key_attributes
        if operation_name is not None:
            input_["operation_name"] = operation_name
        if dependency_config is not None:
            input_["dependency_config"] = dependency_config
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if metric_source_types is not None:
            input_["metric_source_types"] = metric_source_types
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if slo_owner_aws_account_id is not None:
            input_["slo_owner_aws_account_id"] = slo_owner_aws_account_id
        if metric_source is not None:
            input_["metric_source"] = metric_source

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceLevelObjectiveResource:
    def __init__(self, service: AsyncApplicationSignalsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName",
        *,
        config_overrides: Optional[AsyncApplicationSignalsClientConfig] = None,
        description: Optional[
            "capo_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
        ] = None,
        sli_config: Optional[
            "capo_application_signals.types.service_level_indicator_config.ServiceLevelIndicatorConfig"
        ] = None,
        request_based_sli_config: Optional[
            "capo_application_signals.types.request_based_service_level_indicator_config.RequestBasedServiceLevelIndicatorConfig"
        ] = None,
        goal: Optional["capo_application_signals.types.goal.Goal"] = None,
        tags: Optional["capo_application_signals.types.tag_list.TagList"] = None,
        burn_rate_configurations: Optional[
            "capo_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
        ] = None,
        create_recommended_slo: Optional[bool] = None,
        auto_investigation_enabled: Optional[bool] = None,
    ) -> "capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput":
        """<p>Creates a service level objective (SLO), which can help you ensure that your critical business operations are meeting customer expectations. Use SLOs to set and track specific target levels for the reliability and availability of your applications and services. SLOs use service level indicators (SLIs) to calculate whether the application is performing at the level that you want.</p> <p>Create an SLO to set a target for a service or operation’s availability or latency. CloudWatch measures this target frequently you can find whether it has been breached. </p> <p>The target performance quality that is defined for an SLO is the <i>attainment goal</i>.</p> <p>You can set SLO targets for your applications that are discovered by Application Signals, using critical metrics such as latency and availability. You can also set SLOs against any CloudWatch metric or math expression that produces a time series.</p> <note> <p>You can't create an SLO for a service operation that was discovered by Application Signals until after that operation has reported standard metrics to Application Signals.</p> </note> <p>When you create an SLO, you specify whether it is a <i>period-based SLO</i> or a <i>request-based SLO</i>. Each type of SLO has a different way of evaluating your application's performance against its attainment goal.</p> <ul> <li> <p>A <i>period-based SLO</i> uses defined <i>periods</i> of time within a specified total time interval. For each period of time, Application Signals determines whether the application met its goal. The attainment rate is calculated as the <code>number of good periods/number of total periods</code>.</p> <p>For example, for a period-based SLO, meeting an attainment goal of 99.9% means that within your interval, your application must meet its performance goal during at least 99.9% of the time periods.</p> </li> <li> <p>A <i>request-based SLO</i> doesn't use pre-defined periods of time. Instead, the SLO measures <code>number of good requests/number of total requests</code> during the interval. At any time, you can find the ratio of good requests to total requests for the interval up to the time stamp that you specify, and measure that ratio against the goal set in your SLO.</p> </li> </ul> <p>After you have created an SLO, you can retrieve error budget reports for it. An <i>error budget</i> is the amount of time or amount of requests that your application can be non-compliant with the SLO's goal, and still have your application meet the goal.</p> <ul> <li> <p>For a period-based SLO, the error budget starts at a number defined by the highest number of periods that can fail to meet the threshold, while still meeting the overall goal. The <i>remaining error budget</i> decreases with every failed period that is recorded. The error budget within one interval can never increase.</p> <p>For example, an SLO with a threshold that 99.95% of requests must be completed under 2000ms every month translates to an error budget of 21.9 minutes of downtime per month.</p> </li> <li> <p>For a request-based SLO, the remaining error budget is dynamic and can increase or decrease, depending on the ratio of good requests to total requests.</p> </li> </ul> <p>For more information about SLOs, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html"> Service level objectives (SLOs)</a>. </p> <p>When you perform a <code>CreateServiceLevelObjective</code> operation, Application Signals creates the <i>AWSServiceRoleForCloudWatchApplicationSignals</i> service-linked role, if it doesn't already exist in your account. This service- linked role has the following permissions:</p> <ul> <li> <p> <code>xray:GetServiceGraph</code> </p> </li> <li> <p> <code>logs:StartQuery</code> </p> </li> <li> <p> <code>logs:GetQueryResults</code> </p> </li> <li> <p> <code>cloudwatch:GetMetricData</code> </p> </li> <li> <p> <code>cloudwatch:ListMetrics</code> </p> </li> <li> <p> <code>tag:GetResources</code> </p> </li> <li> <p> <code>autoscaling:DescribeAutoScalingGroups</code> </p> </li> </ul>

        Args:
            name: <p>A name for this SLO.</p>
            description: <p>An optional description for this SLO.</p>
            sli_config: <p>If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>RequestBasedSliConfig</code> and <code>SliConfig</code> in the same operation.</p>
            request_based_sli_config: <p>If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>RequestBasedSliConfig</code> and <code>SliConfig</code> in the same operation.</p>
            goal: <p>This structure contains the attributes that determine the goal of the SLO.</p>
            tags: <p>A list of key-value pairs to associate with the SLO. You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p>
            burn_rate_configurations: <p>Use this array to create <i>burn rates</i> for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>
            create_recommended_slo: <p>Set this to <code>true</code> to create a recommended SLO out of the box. When set to <code>true</code>, you don't need to specify the <code>MetricThreshold</code> or <code>ComparisonOperator</code> in the <code>SliConfig</code> or <code>RequestBasedSliConfig</code>. The default value is <code>false</code>.</p> <p>This is supported for SLOs on a service, service operation, or a dependency.</p>
            auto_investigation_enabled: Indicates whether DevOps Agent will automatically investigate this SLO when it is breached

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_application_signals.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput]",
        ) -> AsyncOperationResponse[
            "capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.create_service_level_objective

            (
                output,
                http_response,
            ) = await capo_application_signals._operations.application_signals.create_service_level_objective.async_create_service_level_objective(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sli_config is not None:
            input_["sli_config"] = sli_config
        if request_based_sli_config is not None:
            input_["request_based_sli_config"] = request_based_sli_config
        if goal is not None:
            input_["goal"] = goal
        if tags is not None:
            input_["tags"] = tags
        if burn_rate_configurations is not None:
            input_["burn_rate_configurations"] = burn_rate_configurations
        if create_recommended_slo is not None:
            input_["create_recommended_slo"] = create_recommended_slo
        if auto_investigation_enabled is not None:
            input_["auto_investigation_enabled"] = auto_investigation_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[AsyncApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.get_service_level_objective_output.GetServiceLevelObjectiveOutput":
        """<p>Returns information about one SLO created in the account. </p>

        Args:
            id: <p>The ARN or name of the SLO that you want to retrieve information about. You can find the ARNs of SLOs by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListServiceLevelObjectives.html">ListServiceLevelObjectives</a> operation.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_signals.types.get_service_level_objective_input.GetServiceLevelObjectiveInput]",
        ) -> AsyncOperationResponse[
            "capo_application_signals.types.get_service_level_objective_output.GetServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.get_service_level_objective

            (
                output,
                http_response,
            ) = await capo_application_signals._operations.application_signals.get_service_level_objective.async_get_service_level_objective(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.get_service_level_objective_input.GetServiceLevelObjectiveInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[AsyncApplicationSignalsClientConfig] = None,
        description: Optional[
            "capo_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
        ] = None,
        sli_config: Optional[
            "capo_application_signals.types.service_level_indicator_config.ServiceLevelIndicatorConfig"
        ] = None,
        request_based_sli_config: Optional[
            "capo_application_signals.types.request_based_service_level_indicator_config.RequestBasedServiceLevelIndicatorConfig"
        ] = None,
        goal: Optional["capo_application_signals.types.goal.Goal"] = None,
        burn_rate_configurations: Optional[
            "capo_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
        ] = None,
        auto_investigation_enabled: Optional[bool] = None,
    ) -> "capo_application_signals.types.update_service_level_objective_output.UpdateServiceLevelObjectiveOutput":
        """<p>Updates an existing service level objective (SLO). If you omit parameters, the previous values of those parameters are retained. </p> <p>You cannot change from a period-based SLO to a request-based SLO, or change from a request-based SLO to a period-based SLO.</p>

        Args:
            id: <p>The Amazon Resource Name (ARN) or name of the service level objective that you want to update.</p>
            description: <p>An optional description for the SLO.</p>
            sli_config: <p>If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p>
            request_based_sli_config: <p>If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>SliConfig</code> and <code>RequestBasedSliConfig</code> in the same operation.</p>
            goal: <p>A structure that contains the attributes that determine the goal of the SLO. This includes the time period for evaluation and the attainment threshold.</p>
            burn_rate_configurations: <p>Use this array to create <i>burn rates</i> for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>
            auto_investigation_enabled: Indicates whether DevOps Agent will automatically investigate this SLO when it is breached

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_signals.types.update_service_level_objective_input.UpdateServiceLevelObjectiveInput]",
        ) -> AsyncOperationResponse[
            "capo_application_signals.types.update_service_level_objective_output.UpdateServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.update_service_level_objective

            (
                output,
                http_response,
            ) = await capo_application_signals._operations.application_signals.update_service_level_objective.async_update_service_level_objective(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.update_service_level_objective_input.UpdateServiceLevelObjectiveInput = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if sli_config is not None:
            input_["sli_config"] = sli_config
        if request_based_sli_config is not None:
            input_["request_based_sli_config"] = request_based_sli_config
        if goal is not None:
            input_["goal"] = goal
        if burn_rate_configurations is not None:
            input_["burn_rate_configurations"] = burn_rate_configurations
        if auto_investigation_enabled is not None:
            input_["auto_investigation_enabled"] = auto_investigation_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[AsyncApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.delete_service_level_objective_output.DeleteServiceLevelObjectiveOutput":
        """<p>Deletes the specified service level objective.</p>

        Args:
            id: <p>The ARN or name of the service level objective to delete.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_signals.types.delete_service_level_objective_input.DeleteServiceLevelObjectiveInput]",
        ) -> AsyncOperationResponse[
            "capo_application_signals.types.delete_service_level_objective_output.DeleteServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.delete_service_level_objective

            (
                output,
                http_response,
            ) = await capo_application_signals._operations.application_signals.delete_service_level_objective.async_delete_service_level_objective(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.delete_service_level_objective_input.DeleteServiceLevelObjectiveInput = {
            "id": id
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
        config_overrides: Optional[AsyncApplicationSignalsClientConfig] = None,
        key_attributes: Optional[
            "capo_application_signals.types.attributes.Attributes"
        ] = None,
        operation_name: Optional[
            "capo_application_signals.types.operation_name.OperationName"
        ] = None,
        dependency_config: Optional[
            "capo_application_signals.types.dependency_config.DependencyConfig"
        ] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_level_objectives_max_results.ListServiceLevelObjectivesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        metric_source_types: Optional[
            "capo_application_signals.types.metric_source_types.MetricSourceTypes"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        slo_owner_aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        metric_source: Optional[
            "capo_application_signals.types.metric_source.MetricSource"
        ] = None,
    ) -> "capo_application_signals.types.list_service_level_objectives_output.ListServiceLevelObjectivesOutput":
        """<p>Returns a list of SLOs created in this account.</p>

        Args:
            key_attributes: <p>You can use this optional field to specify which services you want to retrieve SLO information for.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            operation_name: <p>The name of the operation that this SLO is associated with.</p>
            dependency_config: <p>Identifies the dependency using the <code>DependencyKeyAttributes</code> and <code>DependencyOperationName</code>. </p>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives.</p>
            metric_source_types: <p>Use this optional field to only include SLOs with the specified metric source types in the output. Supported types are:</p> <ul> <li> <p>Service operation</p> </li> <li> <p>Service dependency</p> </li> <li> <p>Service</p> </li> <li> <p>CloudWatch metric</p> </li> <li> <p>AppMonitor</p> </li> <li> <p>Canary</p> </li> </ul>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include SLO from source accounts in the returned data. </p> <p>When you are monitoring an account, you can use Amazon Web Services account ID in <code>KeyAttribute</code> filter for service source account and <code>SloOwnerawsaccountID</code> for SLO source account with <code>IncludeLinkedAccounts</code> to filter the returned data to only a single source account. </p>
            slo_owner_aws_account_id: <p>SLO's Amazon Web Services account ID.</p>
            metric_source: <p>Identifies the metric source to filter SLOs by.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_application_signals.types.list_service_level_objectives_input.ListServiceLevelObjectivesInput]",
        ) -> AsyncOperationResponse[
            "capo_application_signals.types.list_service_level_objectives_output.ListServiceLevelObjectivesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_level_objectives

            (
                output,
                http_response,
            ) = await capo_application_signals._operations.application_signals.list_service_level_objectives.async_list_service_level_objectives(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_level_objectives_input.ListServiceLevelObjectivesInput = {}
        if key_attributes is not None:
            input_["key_attributes"] = key_attributes
        if operation_name is not None:
            input_["operation_name"] = operation_name
        if dependency_config is not None:
            input_["dependency_config"] = dependency_config
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if metric_source_types is not None:
            input_["metric_source_types"] = metric_source_types
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if slo_owner_aws_account_id is not None:
            input_["slo_owner_aws_account_id"] = slo_owner_aws_account_id
        if metric_source is not None:
            input_["metric_source"] = metric_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
