"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.alarm_state_information_list
    import capo_ssm.types.automation_execution_id
    import capo_ssm.types.automation_execution_status
    import capo_ssm.types.automation_parameter_key
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.automation_subtype
    import capo_ssm.types.boolean
    import capo_ssm.types.change_request_name
    import capo_ssm.types.date_time
    import capo_ssm.types.document_name
    import capo_ssm.types.document_version
    import capo_ssm.types.execution_mode
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.progress_counters
    import capo_ssm.types.resolved_targets
    import capo_ssm.types.runbooks
    import capo_ssm.types.step_execution_list
    import capo_ssm.types.string
    import capo_ssm.types.target_locations
    import capo_ssm.types.target_locations_url
    import capo_ssm.types.target_maps
    import capo_ssm.types.targets
    import capo_ssm.types.targets_summary


class AutomationExecution(TypedDict, closed=True):
    automation_execution_id: NotRequired[
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    ]
    """<p>The execution ID.</p>"""
    document_name: NotRequired["capo_ssm.types.document_name.DocumentName"]
    """<p>The name of the Automation runbook used during the execution.</p>"""
    document_version: NotRequired["capo_ssm.types.document_version.DocumentVersion"]
    """<p>The version of the document to use during execution.</p>"""
    execution_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the execution started.</p>"""
    execution_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the execution finished.</p>"""
    automation_execution_status: NotRequired[
        "capo_ssm.types.automation_execution_status.AutomationExecutionStatus"
    ]
    """<p>The execution status of the Automation.</p>"""
    step_executions: NotRequired["capo_ssm.types.step_execution_list.StepExecutionList"]
    """<p>A list of details about the current state of all steps that comprise an execution. An Automation runbook contains a list of steps that are run in order.</p>"""
    step_executions_truncated: "capo_ssm.types.boolean.Boolean"
    """<p>A boolean value that indicates if the response contains the full list of the Automation step executions. If true, use the DescribeAutomationStepExecutions API operation to get the full list of step executions.</p>"""
    parameters: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The key-value map of execution parameters, which were supplied when calling <a>StartAutomationExecution</a>.</p>"""
    outputs: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>The list of execution outputs as defined in the Automation runbook.</p>"""
    failure_message: NotRequired["capo_ssm.types.string.String"]
    """<p>A message describing why an execution has failed, if the status is set to Failed.</p>"""
    warning_message: NotRequired["capo_ssm.types.string.String"]
    """<p>A message that describes a non-critical issue that occurred during the automation execution.</p>"""
    mode: NotRequired["capo_ssm.types.execution_mode.ExecutionMode"]
    """<p>The automation execution mode.</p>"""
    parent_automation_execution_id: NotRequired[
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    ]
    """<p>The AutomationExecutionId of the parent automation.</p>"""
    executed_by: NotRequired["capo_ssm.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the user who ran the automation.</p>"""
    current_step_name: NotRequired["capo_ssm.types.string.String"]
    """<p>The name of the step that is currently running.</p>"""
    current_action: NotRequired["capo_ssm.types.string.String"]
    """<p>The action of the step that is currently running.</p>"""
    target_parameter_name: NotRequired[
        "capo_ssm.types.automation_parameter_key.AutomationParameterKey"
    ]
    """<p>The parameter name.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The specified targets.</p>"""
    target_maps: NotRequired["capo_ssm.types.target_maps.TargetMaps"]
    """<p>The specified key-value mapping of document parameters to target resources.</p>"""
    resolved_targets: NotRequired["capo_ssm.types.resolved_targets.ResolvedTargets"]
    """<p>A list of resolved targets in the rate control execution.</p>"""
    max_concurrency: NotRequired["capo_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The <code>MaxConcurrency</code> value specified by the user when the execution started.</p>"""
    max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The MaxErrors value specified by the user when the execution started.</p>"""
    target: NotRequired["capo_ssm.types.string.String"]
    """<p>The target of the execution.</p>"""
    target_locations: NotRequired["capo_ssm.types.target_locations.TargetLocations"]
    """<p>The combination of Amazon Web Services Regions and/or Amazon Web Services accounts where you want to run the Automation.</p>"""
    progress_counters: NotRequired["capo_ssm.types.progress_counters.ProgressCounters"]
    """<p>An aggregate of step execution statuses displayed in the Amazon Web Services Systems Manager console for a multi-Region and multi-account Automation execution.</p>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm applied to your automation.</p>"""
    triggered_alarms: NotRequired[
        "capo_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarm that was invoked by the automation.</p>"""
    target_locations_url: NotRequired[
        "capo_ssm.types.target_locations_url.TargetLocationsURL"
    ]
    """<p>A publicly accessible URL for a file that contains the <code>TargetLocations</code> body. Currently, only files in presigned Amazon S3 buckets are supported</p>"""
    automation_subtype: NotRequired[
        "capo_ssm.types.automation_subtype.AutomationSubtype"
    ]
    """<p>The subtype of the Automation operation. Currently, the only supported value is <code>ChangeRequest</code>.</p>"""
    scheduled_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the Automation operation is scheduled to start.</p>"""
    runbooks: NotRequired["capo_ssm.types.runbooks.Runbooks"]
    """<p>Information about the Automation runbooks that are run as part of a runbook workflow.</p> <note> <p>The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.</p> </note>"""
    ops_item_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The ID of an OpsItem that is created to represent a Change Manager change request.</p>"""
    association_id: NotRequired["capo_ssm.types.string.String"]
    """<p>The ID of a State Manager association used in the Automation operation.</p>"""
    change_request_name: NotRequired[
        "capo_ssm.types.change_request_name.ChangeRequestName"
    ]
    """<p>The name of the Change Manager change request.</p>"""
    variables: NotRequired[
        "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
    ]
    """<p>Variables defined for the automation.</p>"""
    targets_summary: NotRequired["capo_ssm.types.targets_summary.TargetsSummary"]
    """<p>A summary of the child executions that a rate control execution started for its targets. This field is returned only for rate control executions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecution) -> dict:
    out: dict = {}
    if "automation_execution_id" in value:
        out["AutomationExecutionId"] = value["automation_execution_id"]
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "document_version" in value:
        out["DocumentVersion"] = value["document_version"]
    if "execution_start_time" in value:
        import capo_ssm.types.date_time

        out["ExecutionStartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["execution_start_time"]
        )
    if "execution_end_time" in value:
        import capo_ssm.types.date_time

        out["ExecutionEndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["execution_end_time"]
        )
    if "automation_execution_status" in value:
        import capo_ssm.types.automation_execution_status

        out["AutomationExecutionStatus"] = (
            capo_ssm.types.automation_execution_status.serialize_aws_json_1_1(
                value["automation_execution_status"]
            )
        )
    if "step_executions" in value:
        import capo_ssm.types.step_execution_list

        out["StepExecutions"] = (
            capo_ssm.types.step_execution_list.serialize_aws_json_1_1(
                value["step_executions"]
            )
        )
    out["StepExecutionsTruncated"] = value.get("step_executions_truncated", False)
    if "parameters" in value:
        import capo_ssm.types.automation_parameter_map

        out["Parameters"] = (
            capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    if "outputs" in value:
        import capo_ssm.types.automation_parameter_map

        out["Outputs"] = capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
            value["outputs"]
        )
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "warning_message" in value:
        out["WarningMessage"] = value["warning_message"]
    if "mode" in value:
        import capo_ssm.types.execution_mode

        out["Mode"] = capo_ssm.types.execution_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    if "parent_automation_execution_id" in value:
        out["ParentAutomationExecutionId"] = value["parent_automation_execution_id"]
    if "executed_by" in value:
        out["ExecutedBy"] = value["executed_by"]
    if "current_step_name" in value:
        out["CurrentStepName"] = value["current_step_name"]
    if "current_action" in value:
        out["CurrentAction"] = value["current_action"]
    if "target_parameter_name" in value:
        out["TargetParameterName"] = value["target_parameter_name"]
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "target_maps" in value:
        import capo_ssm.types.target_maps

        out["TargetMaps"] = capo_ssm.types.target_maps.serialize_aws_json_1_1(
            value["target_maps"]
        )
    if "resolved_targets" in value:
        import capo_ssm.types.resolved_targets

        out["ResolvedTargets"] = capo_ssm.types.resolved_targets.serialize_aws_json_1_1(
            value["resolved_targets"]
        )
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "target" in value:
        out["Target"] = value["target"]
    if "target_locations" in value:
        import capo_ssm.types.target_locations

        out["TargetLocations"] = capo_ssm.types.target_locations.serialize_aws_json_1_1(
            value["target_locations"]
        )
    if "progress_counters" in value:
        import capo_ssm.types.progress_counters

        out["ProgressCounters"] = (
            capo_ssm.types.progress_counters.serialize_aws_json_1_1(
                value["progress_counters"]
            )
        )
    if "alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "triggered_alarms" in value:
        import capo_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            capo_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    if "target_locations_url" in value:
        out["TargetLocationsURL"] = value["target_locations_url"]
    if "automation_subtype" in value:
        import capo_ssm.types.automation_subtype

        out["AutomationSubtype"] = (
            capo_ssm.types.automation_subtype.serialize_aws_json_1_1(
                value["automation_subtype"]
            )
        )
    if "scheduled_time" in value:
        import capo_ssm.types.date_time

        out["ScheduledTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["scheduled_time"]
        )
    if "runbooks" in value:
        import capo_ssm.types.runbooks

        out["Runbooks"] = capo_ssm.types.runbooks.serialize_aws_json_1_1(
            value["runbooks"]
        )
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "change_request_name" in value:
        out["ChangeRequestName"] = value["change_request_name"]
    if "variables" in value:
        import capo_ssm.types.automation_parameter_map

        out["Variables"] = (
            capo_ssm.types.automation_parameter_map.serialize_aws_json_1_1(
                value["variables"]
            )
        )
    if "targets_summary" in value:
        import capo_ssm.types.targets_summary

        out["TargetsSummary"] = capo_ssm.types.targets_summary.serialize_aws_json_1_1(
            value["targets_summary"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecution:
    out: AutomationExecution = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecutionId") is not None:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    if data.get("DocumentVersion") is not None:
        out["document_version"] = data["DocumentVersion"]
    if data.get("ExecutionStartTime") is not None:
        import capo_ssm.types.date_time

        out["execution_start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExecutionStartTime"]
        )
    if data.get("ExecutionEndTime") is not None:
        import capo_ssm.types.date_time

        out["execution_end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ExecutionEndTime"]
        )
    if data.get("AutomationExecutionStatus") is not None:
        import capo_ssm.types.automation_execution_status

        out["automation_execution_status"] = (
            capo_ssm.types.automation_execution_status.deserialize_aws_json_1_1(
                data["AutomationExecutionStatus"]
            )
        )
    if data.get("StepExecutions") is not None:
        import capo_ssm.types.step_execution_list

        out["step_executions"] = (
            capo_ssm.types.step_execution_list.deserialize_aws_json_1_1(
                data["StepExecutions"]
            )
        )
    if data.get("StepExecutionsTruncated") is not None:
        out["step_executions_truncated"] = data["StepExecutionsTruncated"]
    else:
        out["step_executions_truncated"] = False
    if data.get("Parameters") is not None:
        import capo_ssm.types.automation_parameter_map

        out["parameters"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("Outputs") is not None:
        import capo_ssm.types.automation_parameter_map

        out["outputs"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if data.get("FailureMessage") is not None:
        out["failure_message"] = data["FailureMessage"]
    if data.get("WarningMessage") is not None:
        out["warning_message"] = data["WarningMessage"]
    if data.get("Mode") is not None:
        import capo_ssm.types.execution_mode

        out["mode"] = capo_ssm.types.execution_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    if data.get("ParentAutomationExecutionId") is not None:
        out["parent_automation_execution_id"] = data["ParentAutomationExecutionId"]
    if data.get("ExecutedBy") is not None:
        out["executed_by"] = data["ExecutedBy"]
    if data.get("CurrentStepName") is not None:
        out["current_step_name"] = data["CurrentStepName"]
    if data.get("CurrentAction") is not None:
        out["current_action"] = data["CurrentAction"]
    if data.get("TargetParameterName") is not None:
        out["target_parameter_name"] = data["TargetParameterName"]
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("TargetMaps") is not None:
        import capo_ssm.types.target_maps

        out["target_maps"] = capo_ssm.types.target_maps.deserialize_aws_json_1_1(
            data["TargetMaps"]
        )
    if data.get("ResolvedTargets") is not None:
        import capo_ssm.types.resolved_targets

        out["resolved_targets"] = (
            capo_ssm.types.resolved_targets.deserialize_aws_json_1_1(
                data["ResolvedTargets"]
            )
        )
    if data.get("MaxConcurrency") is not None:
        out["max_concurrency"] = data["MaxConcurrency"]
    if data.get("MaxErrors") is not None:
        out["max_errors"] = data["MaxErrors"]
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    if data.get("TargetLocations") is not None:
        import capo_ssm.types.target_locations

        out["target_locations"] = (
            capo_ssm.types.target_locations.deserialize_aws_json_1_1(
                data["TargetLocations"]
            )
        )
    if data.get("ProgressCounters") is not None:
        import capo_ssm.types.progress_counters

        out["progress_counters"] = (
            capo_ssm.types.progress_counters.deserialize_aws_json_1_1(
                data["ProgressCounters"]
            )
        )
    if data.get("AlarmConfiguration") is not None:
        import capo_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if data.get("TriggeredAlarms") is not None:
        import capo_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            capo_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    if data.get("TargetLocationsURL") is not None:
        out["target_locations_url"] = data["TargetLocationsURL"]
    if data.get("AutomationSubtype") is not None:
        import capo_ssm.types.automation_subtype

        out["automation_subtype"] = (
            capo_ssm.types.automation_subtype.deserialize_aws_json_1_1(
                data["AutomationSubtype"]
            )
        )
    if data.get("ScheduledTime") is not None:
        import capo_ssm.types.date_time

        out["scheduled_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ScheduledTime"]
        )
    if data.get("Runbooks") is not None:
        import capo_ssm.types.runbooks

        out["runbooks"] = capo_ssm.types.runbooks.deserialize_aws_json_1_1(
            data["Runbooks"]
        )
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    if data.get("ChangeRequestName") is not None:
        out["change_request_name"] = data["ChangeRequestName"]
    if data.get("Variables") is not None:
        import capo_ssm.types.automation_parameter_map

        out["variables"] = (
            capo_ssm.types.automation_parameter_map.deserialize_aws_json_1_1(
                data["Variables"]
            )
        )
    if data.get("TargetsSummary") is not None:
        import capo_ssm.types.targets_summary

        out["targets_summary"] = (
            capo_ssm.types.targets_summary.deserialize_aws_json_1_1(
                data["TargetsSummary"]
            )
        )
    return out
