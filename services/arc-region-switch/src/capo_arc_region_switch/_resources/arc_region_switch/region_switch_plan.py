from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from capo_arc_region_switch._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_arc_region_switch.types.abbreviated_plan
    import capo_arc_region_switch.types.associated_alarm_map
    import capo_arc_region_switch.types.create_plan_request
    import capo_arc_region_switch.types.create_plan_response
    import capo_arc_region_switch.types.delete_plan_request
    import capo_arc_region_switch.types.delete_plan_response
    import capo_arc_region_switch.types.get_plan_request
    import capo_arc_region_switch.types.get_plan_response
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.list_plans_request
    import capo_arc_region_switch.types.list_plans_response
    import capo_arc_region_switch.types.list_tags_for_resource_request
    import capo_arc_region_switch.types.list_tags_for_resource_response
    import capo_arc_region_switch.types.max_results
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.plan_name
    import capo_arc_region_switch.types.recovery_approach
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.region_list
    import capo_arc_region_switch.types.report_configuration
    import capo_arc_region_switch.types.tag_keys
    import capo_arc_region_switch.types.tag_resource_request
    import capo_arc_region_switch.types.tag_resource_response
    import capo_arc_region_switch.types.tags
    import capo_arc_region_switch.types.trigger_list
    import capo_arc_region_switch.types.untag_resource_request
    import capo_arc_region_switch.types.untag_resource_response
    import capo_arc_region_switch.types.update_plan_request
    import capo_arc_region_switch.types.update_plan_response
    import capo_arc_region_switch.types.workflow_list
    from capo_arc_region_switch._services.arc_regionswitch import (
        ARCRegionswitchClient,
        ARCRegionswitchClientConfig,
    )
    from capo_arc_region_switch._services.async_arc_regionswitch import (
        AsyncARCRegionswitchClient,
        AsyncARCRegionswitchClientConfig,
    )


class RegionSwitchPlan:
    def __init__(self, service: ARCRegionswitchClient) -> None:
        self._service = service

    def create(
        self,
        workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList",
        execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn",
        name: "capo_arc_region_switch.types.plan_name.PlanName",
        regions: "capo_arc_region_switch.types.region_list.RegionList",
        recovery_approach: "capo_arc_region_switch.types.recovery_approach.RecoveryApproach",
        *,
        config_overrides: Optional[ARCRegionswitchClientConfig] = None,
        description: Optional[str] = None,
        recovery_time_objective_minutes: Optional[int] = None,
        associated_alarms: Optional[
            "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
        ] = None,
        triggers: Optional[
            "capo_arc_region_switch.types.trigger_list.TriggerList"
        ] = None,
        report_configuration: Optional[
            "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
        ] = None,
        service_quota_checks_enabled: Optional[bool] = None,
        primary_region: Optional["capo_arc_region_switch.types.region.Region"] = None,
        tags: Optional["capo_arc_region_switch.types.tags.Tags"] = None,
    ) -> "capo_arc_region_switch.types.create_plan_response.CreatePlanResponse":
        """<p>Creates a new Region switch plan. A plan defines the steps required to shift traffic from one Amazon Web Services Region to another.</p> <p>You must specify a name for the plan, the primary Region, and at least one additional Region. You can also provide a description, execution role, recovery time objective, associated alarms, triggers, and workflows that define the steps to execute during a Region switch.</p>

        Args:
            description: <p>The description of a Region switch plan.</p>
            workflows: <p>An array of workflows included in a Region switch plan.</p>
            execution_role: <p>An execution role is a way to categorize a Region switch plan.</p>
            recovery_time_objective_minutes: <p>Optionally, you can specify an recovery time objective for a Region switch plan, in minutes.</p>
            associated_alarms: <p>The alarms associated with a Region switch plan.</p>
            triggers: <p>The triggers associated with a Region switch plan.</p>
            service_quota_checks_enabled: <p>Specifies whether to enable service quota checks for the Region switch plan.</p>
            name: <p>The name of a Region switch plan.</p>
            regions: <p>An array that specifies the Amazon Web Services Regions for a Region switch plan. Specify two Regions.</p>
            recovery_approach: <p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>
            primary_region: <p>The primary Amazon Web Services Region for the application. This is the Region where the application normally runs before any Region switch occurs.</p>
            tags: <p>The tags to apply to the Region switch plan.</p>

        Raises:
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_region_switch.types.create_plan_request.CreatePlanRequest]",
        ) -> OperationResponse[
            "capo_arc_region_switch.types.create_plan_response.CreatePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.create_plan

            output, http_response = (
                capo_arc_region_switch._operations.arc_region_switch.create_plan.create_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_arc_region_switch.types.create_plan_request.CreatePlanRequest",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.create_plan_request

            return capo_arc_region_switch.types.create_plan_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_arc_region_switch.types.create_plan_response.CreatePlanResponse",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.create_plan_response

            return capo_arc_region_switch.types.create_plan_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePlan", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_arc_region_switch.types.create_plan_request.CreatePlanRequest = {
            "workflows": workflows,
            "execution_role": execution_role,
            "name": name,
            "regions": regions,
            "recovery_approach": recovery_approach,
        }
        if description is not None:
            input_["description"] = description
        if recovery_time_objective_minutes is not None:
            input_["recovery_time_objective_minutes"] = recovery_time_objective_minutes
        if associated_alarms is not None:
            input_["associated_alarms"] = associated_alarms
        if triggers is not None:
            input_["triggers"] = triggers
        if report_configuration is not None:
            input_["report_configuration"] = report_configuration
        if service_quota_checks_enabled is not None:
            input_["service_quota_checks_enabled"] = service_quota_checks_enabled
        if primary_region is not None:
            input_["primary_region"] = primary_region
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[ARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.get_plan_response.GetPlanResponse":
        """<p>Retrieves detailed information about a Region switch plan. You must specify the ARN of the plan.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>

        Raises:
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_region_switch.types.get_plan_request.GetPlanRequest]",
        ) -> OperationResponse[
            "capo_arc_region_switch.types.get_plan_response.GetPlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan

            output, http_response = (
                capo_arc_region_switch._operations.arc_region_switch.get_plan.get_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_arc_region_switch.types.get_plan_response.GetPlanResponse",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.get_plan_response

            return capo_arc_region_switch.types.get_plan_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPlan", redact_output=_redact_output)
        )
        input_: capo_arc_region_switch.types.get_plan_request.GetPlanRequest = {
            "arn": arn
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
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList",
        execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[ARCRegionswitchClientConfig] = None,
        description: Optional[str] = None,
        recovery_time_objective_minutes: Optional[int] = None,
        associated_alarms: Optional[
            "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
        ] = None,
        triggers: Optional[
            "capo_arc_region_switch.types.trigger_list.TriggerList"
        ] = None,
        report_configuration: Optional[
            "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
        ] = None,
        service_quota_checks_enabled: Optional[bool] = None,
    ) -> "capo_arc_region_switch.types.update_plan_response.UpdatePlanResponse":
        """<p>Updates an existing Region switch plan. You can modify the plan's description, workflows, execution role, recovery time objective, associated alarms, and triggers.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            description: <p>The updated description for the Region switch plan.</p>
            workflows: <p>The updated workflows for the Region switch plan.</p>
            execution_role: <p>The updated IAM role ARN that grants Region switch the permissions needed to execute the plan steps.</p>
            recovery_time_objective_minutes: <p>The updated target recovery time objective (RTO) in minutes for the plan.</p>
            associated_alarms: <p>The updated CloudWatch alarms associated with the plan.</p>
            triggers: <p>The updated conditions that can automatically trigger the execution of the plan.</p>
            report_configuration: <p>The updated report configuration for the plan.</p>
            service_quota_checks_enabled: <p>Specifies whether service quota checks are enabled for the Region switch plan.</p>

        Raises:
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_region_switch.types.update_plan_request.UpdatePlanRequest]",
        ) -> OperationResponse[
            "capo_arc_region_switch.types.update_plan_response.UpdatePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.update_plan

            output, http_response = (
                capo_arc_region_switch._operations.arc_region_switch.update_plan.update_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_arc_region_switch.types.update_plan_request.UpdatePlanRequest",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.update_plan_request

            return capo_arc_region_switch.types.update_plan_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_arc_region_switch.types.update_plan_response.UpdatePlanResponse",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.update_plan_response

            return capo_arc_region_switch.types.update_plan_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePlan", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_arc_region_switch.types.update_plan_request.UpdatePlanRequest = {
            "arn": arn,
            "workflows": workflows,
            "execution_role": execution_role,
        }
        if description is not None:
            input_["description"] = description
        if recovery_time_objective_minutes is not None:
            input_["recovery_time_objective_minutes"] = recovery_time_objective_minutes
        if associated_alarms is not None:
            input_["associated_alarms"] = associated_alarms
        if triggers is not None:
            input_["triggers"] = triggers
        if report_configuration is not None:
            input_["report_configuration"] = report_configuration
        if service_quota_checks_enabled is not None:
            input_["service_quota_checks_enabled"] = service_quota_checks_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[ARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.delete_plan_response.DeletePlanResponse":
        """<p>Deletes a Region switch plan. You must specify the ARN of the plan to delete.</p> <p>You cannot delete a plan that has an active execution in progress.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>

        Raises:
            capo_arc_region_switch.errors.illegal_state_exception.IllegalStateException: <p>The operation failed because the current state of the resource doesn't allow the operation to proceed.</p> <p>HTTP Status Code: 400</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_region_switch.types.delete_plan_request.DeletePlanRequest]",
        ) -> OperationResponse[
            "capo_arc_region_switch.types.delete_plan_response.DeletePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.delete_plan

            output, http_response = (
                capo_arc_region_switch._operations.arc_region_switch.delete_plan.delete_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePlan")
        )
        input_: capo_arc_region_switch.types.delete_plan_request.DeletePlanRequest = {
            "arn": arn
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
        config_overrides: Optional[ARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_plans_response.ListPlansResponse":
        """<p>Lists all Region switch plans in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_region_switch.types.list_plans_request.ListPlansRequest]",
        ) -> OperationResponse[
            "capo_arc_region_switch.types.list_plans_response.ListPlansResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plans

            output, http_response = (
                capo_arc_region_switch._operations.arc_region_switch.list_plans.list_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPlans")
        )
        input_: capo_arc_region_switch.types.list_plans_request.ListPlansRequest = {}
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

    def list_tags_for_resource(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[ARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to a Region switch resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_region_switch.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_arc_region_switch.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_tags_for_resource

            output, http_response = (
                capo_arc_region_switch._operations.arc_region_switch.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTagsForResource")
        )
        input_: capo_arc_region_switch.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
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
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        tags: "capo_arc_region_switch.types.tags.Tags",
        *,
        config_overrides: Optional[ARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a Region switch resource. You can assign metadata to your resources in the form of tags, which are key-value pairs.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for a tag that you add to a resource.</p>
            tags: <p>Tags that you add to a resource. You can add a maximum of 50 tags in Region switch.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_region_switch.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_arc_region_switch.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.tag_resource

            output, http_response = (
                capo_arc_region_switch._operations.arc_region_switch.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_arc_region_switch.types.tag_resource_request.TagResourceRequest = {
            "arn": arn,
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
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        resource_tag_keys: "capo_arc_region_switch.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[ARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a Region switch resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for a tag you remove a resource from.</p>
            resource_tag_keys: <p>Tag keys that you remove from a resource.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_arc_region_switch.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_arc_region_switch.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.untag_resource

            output, http_response = (
                capo_arc_region_switch._operations.arc_region_switch.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_arc_region_switch.types.untag_resource_request.UntagResourceRequest = {
            "arn": arn,
            "resource_tag_keys": resource_tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRegionSwitchPlan:
    def __init__(self, service: AsyncARCRegionswitchClient) -> None:
        self._service = service

    async def create(
        self,
        workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList",
        execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn",
        name: "capo_arc_region_switch.types.plan_name.PlanName",
        regions: "capo_arc_region_switch.types.region_list.RegionList",
        recovery_approach: "capo_arc_region_switch.types.recovery_approach.RecoveryApproach",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        description: Optional[str] = None,
        recovery_time_objective_minutes: Optional[int] = None,
        associated_alarms: Optional[
            "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
        ] = None,
        triggers: Optional[
            "capo_arc_region_switch.types.trigger_list.TriggerList"
        ] = None,
        report_configuration: Optional[
            "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
        ] = None,
        service_quota_checks_enabled: Optional[bool] = None,
        primary_region: Optional["capo_arc_region_switch.types.region.Region"] = None,
        tags: Optional["capo_arc_region_switch.types.tags.Tags"] = None,
    ) -> "capo_arc_region_switch.types.create_plan_response.CreatePlanResponse":
        """<p>Creates a new Region switch plan. A plan defines the steps required to shift traffic from one Amazon Web Services Region to another.</p> <p>You must specify a name for the plan, the primary Region, and at least one additional Region. You can also provide a description, execution role, recovery time objective, associated alarms, triggers, and workflows that define the steps to execute during a Region switch.</p>

        Args:
            description: <p>The description of a Region switch plan.</p>
            workflows: <p>An array of workflows included in a Region switch plan.</p>
            execution_role: <p>An execution role is a way to categorize a Region switch plan.</p>
            recovery_time_objective_minutes: <p>Optionally, you can specify an recovery time objective for a Region switch plan, in minutes.</p>
            associated_alarms: <p>The alarms associated with a Region switch plan.</p>
            triggers: <p>The triggers associated with a Region switch plan.</p>
            service_quota_checks_enabled: <p>Specifies whether to enable service quota checks for the Region switch plan.</p>
            name: <p>The name of a Region switch plan.</p>
            regions: <p>An array that specifies the Amazon Web Services Regions for a Region switch plan. Specify two Regions.</p>
            recovery_approach: <p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>
            primary_region: <p>The primary Amazon Web Services Region for the application. This is the Region where the application normally runs before any Region switch occurs.</p>
            tags: <p>The tags to apply to the Region switch plan.</p>

        Raises:
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.create_plan_request.CreatePlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.create_plan_response.CreatePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.create_plan

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.create_plan.async_create_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_arc_region_switch.types.create_plan_request.CreatePlanRequest",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.create_plan_request

            return capo_arc_region_switch.types.create_plan_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_arc_region_switch.types.create_plan_response.CreatePlanResponse",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.create_plan_response

            return capo_arc_region_switch.types.create_plan_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePlan", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_arc_region_switch.types.create_plan_request.CreatePlanRequest = {
            "workflows": workflows,
            "execution_role": execution_role,
            "name": name,
            "regions": regions,
            "recovery_approach": recovery_approach,
        }
        if description is not None:
            input_["description"] = description
        if recovery_time_objective_minutes is not None:
            input_["recovery_time_objective_minutes"] = recovery_time_objective_minutes
        if associated_alarms is not None:
            input_["associated_alarms"] = associated_alarms
        if triggers is not None:
            input_["triggers"] = triggers
        if report_configuration is not None:
            input_["report_configuration"] = report_configuration
        if service_quota_checks_enabled is not None:
            input_["service_quota_checks_enabled"] = service_quota_checks_enabled
        if primary_region is not None:
            input_["primary_region"] = primary_region
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.get_plan_response.GetPlanResponse":
        """<p>Retrieves detailed information about a Region switch plan. You must specify the ARN of the plan.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>

        Raises:
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.get_plan_request.GetPlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.get_plan_response.GetPlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.get_plan.async_get_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_arc_region_switch.types.get_plan_response.GetPlanResponse",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.get_plan_response

            return capo_arc_region_switch.types.get_plan_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPlan", redact_output=_redact_output)
        )
        input_: capo_arc_region_switch.types.get_plan_request.GetPlanRequest = {
            "arn": arn
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
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList",
        execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        description: Optional[str] = None,
        recovery_time_objective_minutes: Optional[int] = None,
        associated_alarms: Optional[
            "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
        ] = None,
        triggers: Optional[
            "capo_arc_region_switch.types.trigger_list.TriggerList"
        ] = None,
        report_configuration: Optional[
            "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
        ] = None,
        service_quota_checks_enabled: Optional[bool] = None,
    ) -> "capo_arc_region_switch.types.update_plan_response.UpdatePlanResponse":
        """<p>Updates an existing Region switch plan. You can modify the plan's description, workflows, execution role, recovery time objective, associated alarms, and triggers.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            description: <p>The updated description for the Region switch plan.</p>
            workflows: <p>The updated workflows for the Region switch plan.</p>
            execution_role: <p>The updated IAM role ARN that grants Region switch the permissions needed to execute the plan steps.</p>
            recovery_time_objective_minutes: <p>The updated target recovery time objective (RTO) in minutes for the plan.</p>
            associated_alarms: <p>The updated CloudWatch alarms associated with the plan.</p>
            triggers: <p>The updated conditions that can automatically trigger the execution of the plan.</p>
            report_configuration: <p>The updated report configuration for the plan.</p>
            service_quota_checks_enabled: <p>Specifies whether service quota checks are enabled for the Region switch plan.</p>

        Raises:
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.update_plan_request.UpdatePlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.update_plan_response.UpdatePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.update_plan

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.update_plan.async_update_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_arc_region_switch.types.update_plan_request.UpdatePlanRequest",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.update_plan_request

            return capo_arc_region_switch.types.update_plan_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_arc_region_switch.types.update_plan_response.UpdatePlanResponse",
        ) -> dict[str, Any]:
            import capo_arc_region_switch.types.update_plan_response

            return capo_arc_region_switch.types.update_plan_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePlan", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_arc_region_switch.types.update_plan_request.UpdatePlanRequest = {
            "arn": arn,
            "workflows": workflows,
            "execution_role": execution_role,
        }
        if description is not None:
            input_["description"] = description
        if recovery_time_objective_minutes is not None:
            input_["recovery_time_objective_minutes"] = recovery_time_objective_minutes
        if associated_alarms is not None:
            input_["associated_alarms"] = associated_alarms
        if triggers is not None:
            input_["triggers"] = triggers
        if report_configuration is not None:
            input_["report_configuration"] = report_configuration
        if service_quota_checks_enabled is not None:
            input_["service_quota_checks_enabled"] = service_quota_checks_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.delete_plan_response.DeletePlanResponse":
        """<p>Deletes a Region switch plan. You must specify the ARN of the plan to delete.</p> <p>You cannot delete a plan that has an active execution in progress.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>

        Raises:
            capo_arc_region_switch.errors.illegal_state_exception.IllegalStateException: <p>The operation failed because the current state of the resource doesn't allow the operation to proceed.</p> <p>HTTP Status Code: 400</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.delete_plan_request.DeletePlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.delete_plan_response.DeletePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.delete_plan

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.delete_plan.async_delete_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePlan")
        )
        input_: capo_arc_region_switch.types.delete_plan_request.DeletePlanRequest = {
            "arn": arn
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
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_plans_response.ListPlansResponse":
        """<p>Lists all Region switch plans in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_plans_request.ListPlansRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_plans_response.ListPlansResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plans

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_plans.async_list_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPlans")
        )
        input_: capo_arc_region_switch.types.list_plans_request.ListPlansRequest = {}
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

    async def list_tags_for_resource(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to a Region switch resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListTagsForResource")
        )
        input_: capo_arc_region_switch.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        tags: "capo_arc_region_switch.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a Region switch resource. You can assign metadata to your resources in the form of tags, which are key-value pairs.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for a tag that you add to a resource.</p>
            tags: <p>Tags that you add to a resource. You can add a maximum of 50 tags in Region switch.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.tag_resource

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_arc_region_switch.types.tag_resource_request.TagResourceRequest = {
            "arn": arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        resource_tag_keys: "capo_arc_region_switch.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a Region switch resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for a tag you remove a resource from.</p>
            resource_tag_keys: <p>Tag keys that you remove from a resource.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.untag_resource

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_arc_region_switch.types.untag_resource_request.UntagResourceRequest = {
            "arn": arn,
            "resource_tag_keys": resource_tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
