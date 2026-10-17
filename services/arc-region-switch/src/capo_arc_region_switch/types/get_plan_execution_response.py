"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GetPlanExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_arc_region_switch.types.duration
    import capo_arc_region_switch.types.execution_action
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.execution_mode
    import capo_arc_region_switch.types.execution_state
    import capo_arc_region_switch.types.generated_report_details
    import capo_arc_region_switch.types.plan
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.step_states


class GetPlanExecutionResponse(TypedDict, closed=True):
    plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""
    execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId"
    """<p>The execution identifier of a plan execution.</p>"""
    version: NotRequired["str"]
    """<p>The version for the plan.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the plan execution was last updated.</p>"""
    comment: NotRequired["str"]
    """<p>A comment included on the plan execution.</p>"""
    start_time: "datetime.datetime"
    """<p>The time (UTC) when the plan execution started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time (UTC) when the plan execution ended.</p>"""
    mode: "capo_arc_region_switch.types.execution_mode.ExecutionMode"
    """<p>The plan execution mode. Valid values are <code>graceful</code>, for graceful executions, or <code>ungraceful</code>, for ungraceful executions.</p>"""
    execution_state: "capo_arc_region_switch.types.execution_state.ExecutionState"
    """<p>The plan execution state. Provides the state of a plan execution, for example, In Progress or Paused by Operator.</p>"""
    execution_action: "capo_arc_region_switch.types.execution_action.ExecutionAction"
    """<p>The plan execution action. Valid values are <code>activate</code>, to activate an Amazon Web Services Region, or <code>deactivate</code>, to deactivate a Region.</p>"""
    execution_region: "str"
    """<p>The Amazon Web Services Region for a plan execution.</p>"""
    recovery_execution_id: NotRequired["str"]
    """<p>The unique identifier of the most recent recovery execution. Required when starting a post-recovery execution.</p>"""
    step_states: NotRequired["capo_arc_region_switch.types.step_states.StepStates"]
    """<p>The states of the steps in the plan execution.</p>"""
    plan: NotRequired["capo_arc_region_switch.types.plan.Plan"]
    """<p>The details of the Region switch plan.</p>"""
    actual_recovery_time: NotRequired["capo_arc_region_switch.types.duration.Duration"]
    """<p>The actual recovery time that Region switch calculates for a plan execution. Actual recovery time includes the time for the plan to run added to the time elapsed until the application health alarms that you've specified are healthy again.</p>"""
    generated_report_details: NotRequired[
        "capo_arc_region_switch.types.generated_report_details.GeneratedReportDetails"
    ]
    """<p>Information about the location of a generated report, or the cause of its failure.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPlanExecutionResponse) -> dict:
    out: dict = {}
    out["planArn"] = value["plan_arn"]
    out["executionId"] = value["execution_id"]
    if "version" in value:
        out["version"] = value["version"]
    if "updated_at" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["updatedAt"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    import capo_arc_region_switch.types._prelude.timestamp

    out["startTime"] = (
        capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    )
    if "end_time" in value:
        import capo_arc_region_switch.types._prelude.timestamp

        out["endTime"] = (
            capo_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    import capo_arc_region_switch.types.execution_mode

    out["mode"] = capo_arc_region_switch.types.execution_mode.serialize_aws_json_1_0(
        value["mode"]
    )
    import capo_arc_region_switch.types.execution_state

    out["executionState"] = (
        capo_arc_region_switch.types.execution_state.serialize_aws_json_1_0(
            value["execution_state"]
        )
    )
    import capo_arc_region_switch.types.execution_action

    out["executionAction"] = (
        capo_arc_region_switch.types.execution_action.serialize_aws_json_1_0(
            value["execution_action"]
        )
    )
    out["executionRegion"] = value["execution_region"]
    if "recovery_execution_id" in value:
        out["recoveryExecutionId"] = value["recovery_execution_id"]
    if "step_states" in value:
        import capo_arc_region_switch.types.step_states

        out["stepStates"] = (
            capo_arc_region_switch.types.step_states.serialize_aws_json_1_0(
                value["step_states"]
            )
        )
    if "plan" in value:
        import capo_arc_region_switch.types.plan

        out["plan"] = capo_arc_region_switch.types.plan.serialize_aws_json_1_0(
            value["plan"]
        )
    if "actual_recovery_time" in value:
        out["actualRecoveryTime"] = value["actual_recovery_time"]
    if "generated_report_details" in value:
        import capo_arc_region_switch.types.generated_report_details

        out["generatedReportDetails"] = (
            capo_arc_region_switch.types.generated_report_details.serialize_aws_json_1_0(
                value["generated_report_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPlanExecutionResponse:
    out: GetPlanExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("planArn") is not None:
        out["plan_arn"] = data["planArn"]
    else:
        raise DeserializationError("GetPlanExecutionResponse.plan_arn required")
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("GetPlanExecutionResponse.execution_id required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("updatedAt") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["updated_at"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("startTime") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["start_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    else:
        raise DeserializationError("GetPlanExecutionResponse.start_time required")
    if data.get("endTime") is not None:
        import capo_arc_region_switch.types._prelude.timestamp

        out["end_time"] = (
            capo_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    if data.get("mode") is not None:
        import capo_arc_region_switch.types.execution_mode

        out["mode"] = (
            capo_arc_region_switch.types.execution_mode.deserialize_aws_json_1_0(
                data["mode"]
            )
        )
    else:
        raise DeserializationError("GetPlanExecutionResponse.mode required")
    if data.get("executionState") is not None:
        import capo_arc_region_switch.types.execution_state

        out["execution_state"] = (
            capo_arc_region_switch.types.execution_state.deserialize_aws_json_1_0(
                data["executionState"]
            )
        )
    else:
        raise DeserializationError("GetPlanExecutionResponse.execution_state required")
    if data.get("executionAction") is not None:
        import capo_arc_region_switch.types.execution_action

        out["execution_action"] = (
            capo_arc_region_switch.types.execution_action.deserialize_aws_json_1_0(
                data["executionAction"]
            )
        )
    else:
        raise DeserializationError("GetPlanExecutionResponse.execution_action required")
    if data.get("executionRegion") is not None:
        out["execution_region"] = data["executionRegion"]
    else:
        raise DeserializationError("GetPlanExecutionResponse.execution_region required")
    if data.get("recoveryExecutionId") is not None:
        out["recovery_execution_id"] = data["recoveryExecutionId"]
    if data.get("stepStates") is not None:
        import capo_arc_region_switch.types.step_states

        out["step_states"] = (
            capo_arc_region_switch.types.step_states.deserialize_aws_json_1_0(
                data["stepStates"]
            )
        )
    if data.get("plan") is not None:
        import capo_arc_region_switch.types.plan

        out["plan"] = capo_arc_region_switch.types.plan.deserialize_aws_json_1_0(
            data["plan"]
        )
    if data.get("actualRecoveryTime") is not None:
        out["actual_recovery_time"] = data["actualRecoveryTime"]
    if data.get("generatedReportDetails") is not None:
        import capo_arc_region_switch.types.generated_report_details

        out["generated_report_details"] = (
            capo_arc_region_switch.types.generated_report_details.deserialize_aws_json_1_0(
                data["generatedReportDetails"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
