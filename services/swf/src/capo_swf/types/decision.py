"""Generated from Smithy shape ``com.amazonaws.swf#Decision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.cancel_timer_decision_attributes
    import capo_swf.types.cancel_workflow_execution_decision_attributes
    import capo_swf.types.complete_workflow_execution_decision_attributes
    import capo_swf.types.continue_as_new_workflow_execution_decision_attributes
    import capo_swf.types.decision_type
    import capo_swf.types.fail_workflow_execution_decision_attributes
    import capo_swf.types.record_marker_decision_attributes
    import capo_swf.types.request_cancel_activity_task_decision_attributes
    import capo_swf.types.request_cancel_external_workflow_execution_decision_attributes
    import capo_swf.types.schedule_activity_task_decision_attributes
    import capo_swf.types.schedule_lambda_function_decision_attributes
    import capo_swf.types.signal_external_workflow_execution_decision_attributes
    import capo_swf.types.start_child_workflow_execution_decision_attributes
    import capo_swf.types.start_timer_decision_attributes


class Decision(TypedDict, closed=True):
    decision_type: "capo_swf.types.decision_type.DecisionType"
    """<p>Specifies the type of the decision.</p>"""
    schedule_activity_task_decision_attributes: NotRequired[
        "capo_swf.types.schedule_activity_task_decision_attributes.ScheduleActivityTaskDecisionAttributes"
    ]
    """<p>Provides the details of the <code>ScheduleActivityTask</code> decision. It isn't set for other decision types.</p>"""
    request_cancel_activity_task_decision_attributes: NotRequired[
        "capo_swf.types.request_cancel_activity_task_decision_attributes.RequestCancelActivityTaskDecisionAttributes"
    ]
    """<p>Provides the details of the <code>RequestCancelActivityTask</code> decision. It isn't set for other decision types.</p>"""
    complete_workflow_execution_decision_attributes: NotRequired[
        "capo_swf.types.complete_workflow_execution_decision_attributes.CompleteWorkflowExecutionDecisionAttributes"
    ]
    """<p>Provides the details of the <code>CompleteWorkflowExecution</code> decision. It isn't set for other decision types.</p>"""
    fail_workflow_execution_decision_attributes: NotRequired[
        "capo_swf.types.fail_workflow_execution_decision_attributes.FailWorkflowExecutionDecisionAttributes"
    ]
    """<p>Provides the details of the <code>FailWorkflowExecution</code> decision. It isn't set for other decision types.</p>"""
    cancel_workflow_execution_decision_attributes: NotRequired[
        "capo_swf.types.cancel_workflow_execution_decision_attributes.CancelWorkflowExecutionDecisionAttributes"
    ]
    """<p>Provides the details of the <code>CancelWorkflowExecution</code> decision. It isn't set for other decision types.</p>"""
    continue_as_new_workflow_execution_decision_attributes: NotRequired[
        "capo_swf.types.continue_as_new_workflow_execution_decision_attributes.ContinueAsNewWorkflowExecutionDecisionAttributes"
    ]
    """<p>Provides the details of the <code>ContinueAsNewWorkflowExecution</code> decision. It isn't set for other decision types.</p>"""
    record_marker_decision_attributes: NotRequired[
        "capo_swf.types.record_marker_decision_attributes.RecordMarkerDecisionAttributes"
    ]
    """<p>Provides the details of the <code>RecordMarker</code> decision. It isn't set for other decision types.</p>"""
    start_timer_decision_attributes: NotRequired[
        "capo_swf.types.start_timer_decision_attributes.StartTimerDecisionAttributes"
    ]
    """<p>Provides the details of the <code>StartTimer</code> decision. It isn't set for other decision types.</p>"""
    cancel_timer_decision_attributes: NotRequired[
        "capo_swf.types.cancel_timer_decision_attributes.CancelTimerDecisionAttributes"
    ]
    """<p>Provides the details of the <code>CancelTimer</code> decision. It isn't set for other decision types.</p>"""
    signal_external_workflow_execution_decision_attributes: NotRequired[
        "capo_swf.types.signal_external_workflow_execution_decision_attributes.SignalExternalWorkflowExecutionDecisionAttributes"
    ]
    """<p>Provides the details of the <code>SignalExternalWorkflowExecution</code> decision. It isn't set for other decision types.</p>"""
    request_cancel_external_workflow_execution_decision_attributes: NotRequired[
        "capo_swf.types.request_cancel_external_workflow_execution_decision_attributes.RequestCancelExternalWorkflowExecutionDecisionAttributes"
    ]
    """<p>Provides the details of the <code>RequestCancelExternalWorkflowExecution</code> decision. It isn't set for other decision types.</p>"""
    start_child_workflow_execution_decision_attributes: NotRequired[
        "capo_swf.types.start_child_workflow_execution_decision_attributes.StartChildWorkflowExecutionDecisionAttributes"
    ]
    """<p>Provides the details of the <code>StartChildWorkflowExecution</code> decision. It isn't set for other decision types.</p>"""
    schedule_lambda_function_decision_attributes: NotRequired[
        "capo_swf.types.schedule_lambda_function_decision_attributes.ScheduleLambdaFunctionDecisionAttributes"
    ]
    """<p>Provides the details of the <code>ScheduleLambdaFunction</code> decision. It isn't set for other decision types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Decision) -> dict:
    out: dict = {}
    import capo_swf.types.decision_type

    out["decisionType"] = capo_swf.types.decision_type.serialize_aws_json_1_0(
        value["decision_type"]
    )
    if "schedule_activity_task_decision_attributes" in value:
        import capo_swf.types.schedule_activity_task_decision_attributes

        out["scheduleActivityTaskDecisionAttributes"] = (
            capo_swf.types.schedule_activity_task_decision_attributes.serialize_aws_json_1_0(
                value["schedule_activity_task_decision_attributes"]
            )
        )
    if "request_cancel_activity_task_decision_attributes" in value:
        import capo_swf.types.request_cancel_activity_task_decision_attributes

        out["requestCancelActivityTaskDecisionAttributes"] = (
            capo_swf.types.request_cancel_activity_task_decision_attributes.serialize_aws_json_1_0(
                value["request_cancel_activity_task_decision_attributes"]
            )
        )
    if "complete_workflow_execution_decision_attributes" in value:
        import capo_swf.types.complete_workflow_execution_decision_attributes

        out["completeWorkflowExecutionDecisionAttributes"] = (
            capo_swf.types.complete_workflow_execution_decision_attributes.serialize_aws_json_1_0(
                value["complete_workflow_execution_decision_attributes"]
            )
        )
    if "fail_workflow_execution_decision_attributes" in value:
        import capo_swf.types.fail_workflow_execution_decision_attributes

        out["failWorkflowExecutionDecisionAttributes"] = (
            capo_swf.types.fail_workflow_execution_decision_attributes.serialize_aws_json_1_0(
                value["fail_workflow_execution_decision_attributes"]
            )
        )
    if "cancel_workflow_execution_decision_attributes" in value:
        import capo_swf.types.cancel_workflow_execution_decision_attributes

        out["cancelWorkflowExecutionDecisionAttributes"] = (
            capo_swf.types.cancel_workflow_execution_decision_attributes.serialize_aws_json_1_0(
                value["cancel_workflow_execution_decision_attributes"]
            )
        )
    if "continue_as_new_workflow_execution_decision_attributes" in value:
        import capo_swf.types.continue_as_new_workflow_execution_decision_attributes

        out["continueAsNewWorkflowExecutionDecisionAttributes"] = (
            capo_swf.types.continue_as_new_workflow_execution_decision_attributes.serialize_aws_json_1_0(
                value["continue_as_new_workflow_execution_decision_attributes"]
            )
        )
    if "record_marker_decision_attributes" in value:
        import capo_swf.types.record_marker_decision_attributes

        out["recordMarkerDecisionAttributes"] = (
            capo_swf.types.record_marker_decision_attributes.serialize_aws_json_1_0(
                value["record_marker_decision_attributes"]
            )
        )
    if "start_timer_decision_attributes" in value:
        import capo_swf.types.start_timer_decision_attributes

        out["startTimerDecisionAttributes"] = (
            capo_swf.types.start_timer_decision_attributes.serialize_aws_json_1_0(
                value["start_timer_decision_attributes"]
            )
        )
    if "cancel_timer_decision_attributes" in value:
        import capo_swf.types.cancel_timer_decision_attributes

        out["cancelTimerDecisionAttributes"] = (
            capo_swf.types.cancel_timer_decision_attributes.serialize_aws_json_1_0(
                value["cancel_timer_decision_attributes"]
            )
        )
    if "signal_external_workflow_execution_decision_attributes" in value:
        import capo_swf.types.signal_external_workflow_execution_decision_attributes

        out["signalExternalWorkflowExecutionDecisionAttributes"] = (
            capo_swf.types.signal_external_workflow_execution_decision_attributes.serialize_aws_json_1_0(
                value["signal_external_workflow_execution_decision_attributes"]
            )
        )
    if "request_cancel_external_workflow_execution_decision_attributes" in value:
        import capo_swf.types.request_cancel_external_workflow_execution_decision_attributes

        out["requestCancelExternalWorkflowExecutionDecisionAttributes"] = (
            capo_swf.types.request_cancel_external_workflow_execution_decision_attributes.serialize_aws_json_1_0(
                value["request_cancel_external_workflow_execution_decision_attributes"]
            )
        )
    if "start_child_workflow_execution_decision_attributes" in value:
        import capo_swf.types.start_child_workflow_execution_decision_attributes

        out["startChildWorkflowExecutionDecisionAttributes"] = (
            capo_swf.types.start_child_workflow_execution_decision_attributes.serialize_aws_json_1_0(
                value["start_child_workflow_execution_decision_attributes"]
            )
        )
    if "schedule_lambda_function_decision_attributes" in value:
        import capo_swf.types.schedule_lambda_function_decision_attributes

        out["scheduleLambdaFunctionDecisionAttributes"] = (
            capo_swf.types.schedule_lambda_function_decision_attributes.serialize_aws_json_1_0(
                value["schedule_lambda_function_decision_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Decision:
    out: Decision = {}  # type: ignore[typeddict-item]
    if data.get("decisionType") is not None:
        import capo_swf.types.decision_type

        out["decision_type"] = capo_swf.types.decision_type.deserialize_aws_json_1_0(
            data["decisionType"]
        )
    else:
        import typing

        out["decision_type"] = typing.cast(
            "capo_swf.types.decision_type.DecisionType", ""
        )
    if data.get("scheduleActivityTaskDecisionAttributes") is not None:
        import capo_swf.types.schedule_activity_task_decision_attributes

        out["schedule_activity_task_decision_attributes"] = (
            capo_swf.types.schedule_activity_task_decision_attributes.deserialize_aws_json_1_0(
                data["scheduleActivityTaskDecisionAttributes"]
            )
        )
    if data.get("requestCancelActivityTaskDecisionAttributes") is not None:
        import capo_swf.types.request_cancel_activity_task_decision_attributes

        out["request_cancel_activity_task_decision_attributes"] = (
            capo_swf.types.request_cancel_activity_task_decision_attributes.deserialize_aws_json_1_0(
                data["requestCancelActivityTaskDecisionAttributes"]
            )
        )
    if data.get("completeWorkflowExecutionDecisionAttributes") is not None:
        import capo_swf.types.complete_workflow_execution_decision_attributes

        out["complete_workflow_execution_decision_attributes"] = (
            capo_swf.types.complete_workflow_execution_decision_attributes.deserialize_aws_json_1_0(
                data["completeWorkflowExecutionDecisionAttributes"]
            )
        )
    if data.get("failWorkflowExecutionDecisionAttributes") is not None:
        import capo_swf.types.fail_workflow_execution_decision_attributes

        out["fail_workflow_execution_decision_attributes"] = (
            capo_swf.types.fail_workflow_execution_decision_attributes.deserialize_aws_json_1_0(
                data["failWorkflowExecutionDecisionAttributes"]
            )
        )
    if data.get("cancelWorkflowExecutionDecisionAttributes") is not None:
        import capo_swf.types.cancel_workflow_execution_decision_attributes

        out["cancel_workflow_execution_decision_attributes"] = (
            capo_swf.types.cancel_workflow_execution_decision_attributes.deserialize_aws_json_1_0(
                data["cancelWorkflowExecutionDecisionAttributes"]
            )
        )
    if data.get("continueAsNewWorkflowExecutionDecisionAttributes") is not None:
        import capo_swf.types.continue_as_new_workflow_execution_decision_attributes

        out["continue_as_new_workflow_execution_decision_attributes"] = (
            capo_swf.types.continue_as_new_workflow_execution_decision_attributes.deserialize_aws_json_1_0(
                data["continueAsNewWorkflowExecutionDecisionAttributes"]
            )
        )
    if data.get("recordMarkerDecisionAttributes") is not None:
        import capo_swf.types.record_marker_decision_attributes

        out["record_marker_decision_attributes"] = (
            capo_swf.types.record_marker_decision_attributes.deserialize_aws_json_1_0(
                data["recordMarkerDecisionAttributes"]
            )
        )
    if data.get("startTimerDecisionAttributes") is not None:
        import capo_swf.types.start_timer_decision_attributes

        out["start_timer_decision_attributes"] = (
            capo_swf.types.start_timer_decision_attributes.deserialize_aws_json_1_0(
                data["startTimerDecisionAttributes"]
            )
        )
    if data.get("cancelTimerDecisionAttributes") is not None:
        import capo_swf.types.cancel_timer_decision_attributes

        out["cancel_timer_decision_attributes"] = (
            capo_swf.types.cancel_timer_decision_attributes.deserialize_aws_json_1_0(
                data["cancelTimerDecisionAttributes"]
            )
        )
    if data.get("signalExternalWorkflowExecutionDecisionAttributes") is not None:
        import capo_swf.types.signal_external_workflow_execution_decision_attributes

        out["signal_external_workflow_execution_decision_attributes"] = (
            capo_swf.types.signal_external_workflow_execution_decision_attributes.deserialize_aws_json_1_0(
                data["signalExternalWorkflowExecutionDecisionAttributes"]
            )
        )
    if data.get("requestCancelExternalWorkflowExecutionDecisionAttributes") is not None:
        import capo_swf.types.request_cancel_external_workflow_execution_decision_attributes

        out["request_cancel_external_workflow_execution_decision_attributes"] = (
            capo_swf.types.request_cancel_external_workflow_execution_decision_attributes.deserialize_aws_json_1_0(
                data["requestCancelExternalWorkflowExecutionDecisionAttributes"]
            )
        )
    if data.get("startChildWorkflowExecutionDecisionAttributes") is not None:
        import capo_swf.types.start_child_workflow_execution_decision_attributes

        out["start_child_workflow_execution_decision_attributes"] = (
            capo_swf.types.start_child_workflow_execution_decision_attributes.deserialize_aws_json_1_0(
                data["startChildWorkflowExecutionDecisionAttributes"]
            )
        )
    if data.get("scheduleLambdaFunctionDecisionAttributes") is not None:
        import capo_swf.types.schedule_lambda_function_decision_attributes

        out["schedule_lambda_function_decision_attributes"] = (
            capo_swf.types.schedule_lambda_function_decision_attributes.deserialize_aws_json_1_0(
                data["scheduleLambdaFunctionDecisionAttributes"]
            )
        )
    return out
