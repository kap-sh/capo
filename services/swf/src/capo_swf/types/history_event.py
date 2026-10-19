"""Generated from Smithy shape ``com.amazonaws.swf#HistoryEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.activity_task_cancel_requested_event_attributes
    import capo_swf.types.activity_task_canceled_event_attributes
    import capo_swf.types.activity_task_completed_event_attributes
    import capo_swf.types.activity_task_failed_event_attributes
    import capo_swf.types.activity_task_scheduled_event_attributes
    import capo_swf.types.activity_task_started_event_attributes
    import capo_swf.types.activity_task_timed_out_event_attributes
    import capo_swf.types.cancel_timer_failed_event_attributes
    import capo_swf.types.cancel_workflow_execution_failed_event_attributes
    import capo_swf.types.child_workflow_execution_canceled_event_attributes
    import capo_swf.types.child_workflow_execution_completed_event_attributes
    import capo_swf.types.child_workflow_execution_failed_event_attributes
    import capo_swf.types.child_workflow_execution_started_event_attributes
    import capo_swf.types.child_workflow_execution_terminated_event_attributes
    import capo_swf.types.child_workflow_execution_timed_out_event_attributes
    import capo_swf.types.complete_workflow_execution_failed_event_attributes
    import capo_swf.types.continue_as_new_workflow_execution_failed_event_attributes
    import capo_swf.types.decision_task_completed_event_attributes
    import capo_swf.types.decision_task_scheduled_event_attributes
    import capo_swf.types.decision_task_started_event_attributes
    import capo_swf.types.decision_task_timed_out_event_attributes
    import capo_swf.types.event_id
    import capo_swf.types.event_type
    import capo_swf.types.external_workflow_execution_cancel_requested_event_attributes
    import capo_swf.types.external_workflow_execution_signaled_event_attributes
    import capo_swf.types.fail_workflow_execution_failed_event_attributes
    import capo_swf.types.lambda_function_completed_event_attributes
    import capo_swf.types.lambda_function_failed_event_attributes
    import capo_swf.types.lambda_function_scheduled_event_attributes
    import capo_swf.types.lambda_function_started_event_attributes
    import capo_swf.types.lambda_function_timed_out_event_attributes
    import capo_swf.types.marker_recorded_event_attributes
    import capo_swf.types.record_marker_failed_event_attributes
    import capo_swf.types.request_cancel_activity_task_failed_event_attributes
    import capo_swf.types.request_cancel_external_workflow_execution_failed_event_attributes
    import capo_swf.types.request_cancel_external_workflow_execution_initiated_event_attributes
    import capo_swf.types.schedule_activity_task_failed_event_attributes
    import capo_swf.types.schedule_lambda_function_failed_event_attributes
    import capo_swf.types.signal_external_workflow_execution_failed_event_attributes
    import capo_swf.types.signal_external_workflow_execution_initiated_event_attributes
    import capo_swf.types.start_child_workflow_execution_failed_event_attributes
    import capo_swf.types.start_child_workflow_execution_initiated_event_attributes
    import capo_swf.types.start_lambda_function_failed_event_attributes
    import capo_swf.types.start_timer_failed_event_attributes
    import capo_swf.types.timer_canceled_event_attributes
    import capo_swf.types.timer_fired_event_attributes
    import capo_swf.types.timer_started_event_attributes
    import capo_swf.types.timestamp
    import capo_swf.types.workflow_execution_cancel_requested_event_attributes
    import capo_swf.types.workflow_execution_canceled_event_attributes
    import capo_swf.types.workflow_execution_completed_event_attributes
    import capo_swf.types.workflow_execution_continued_as_new_event_attributes
    import capo_swf.types.workflow_execution_failed_event_attributes
    import capo_swf.types.workflow_execution_signaled_event_attributes
    import capo_swf.types.workflow_execution_started_event_attributes
    import capo_swf.types.workflow_execution_terminated_event_attributes
    import capo_swf.types.workflow_execution_timed_out_event_attributes


class HistoryEvent(TypedDict, closed=True):
    event_timestamp: "capo_swf.types.timestamp.Timestamp"
    """<p>The date and time when the event occurred.</p>"""
    event_type: "capo_swf.types.event_type.EventType"
    """<p>The type of the history event.</p>"""
    event_id: "capo_swf.types.event_id.EventId"
    """<p>The system generated ID of the event. This ID uniquely identifies the event with in the workflow execution history.</p>"""
    workflow_execution_started_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_started_event_attributes.WorkflowExecutionStartedEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionStarted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    workflow_execution_completed_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_completed_event_attributes.WorkflowExecutionCompletedEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionCompleted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    complete_workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.complete_workflow_execution_failed_event_attributes.CompleteWorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>CompleteWorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_failed_event_attributes.WorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    fail_workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.fail_workflow_execution_failed_event_attributes.FailWorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>FailWorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    workflow_execution_timed_out_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_timed_out_event_attributes.WorkflowExecutionTimedOutEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionTimedOut</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    workflow_execution_canceled_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_canceled_event_attributes.WorkflowExecutionCanceledEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionCanceled</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    cancel_workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.cancel_workflow_execution_failed_event_attributes.CancelWorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>CancelWorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    workflow_execution_continued_as_new_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_continued_as_new_event_attributes.WorkflowExecutionContinuedAsNewEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionContinuedAsNew</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    continue_as_new_workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.continue_as_new_workflow_execution_failed_event_attributes.ContinueAsNewWorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>ContinueAsNewWorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    workflow_execution_terminated_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_terminated_event_attributes.WorkflowExecutionTerminatedEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionTerminated</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    workflow_execution_cancel_requested_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_cancel_requested_event_attributes.WorkflowExecutionCancelRequestedEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionCancelRequested</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    decision_task_scheduled_event_attributes: NotRequired[
        "capo_swf.types.decision_task_scheduled_event_attributes.DecisionTaskScheduledEventAttributes"
    ]
    """<p>If the event is of type <code>DecisionTaskScheduled</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    decision_task_started_event_attributes: NotRequired[
        "capo_swf.types.decision_task_started_event_attributes.DecisionTaskStartedEventAttributes"
    ]
    """<p>If the event is of type <code>DecisionTaskStarted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    decision_task_completed_event_attributes: NotRequired[
        "capo_swf.types.decision_task_completed_event_attributes.DecisionTaskCompletedEventAttributes"
    ]
    """<p>If the event is of type <code>DecisionTaskCompleted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    decision_task_timed_out_event_attributes: NotRequired[
        "capo_swf.types.decision_task_timed_out_event_attributes.DecisionTaskTimedOutEventAttributes"
    ]
    """<p>If the event is of type <code>DecisionTaskTimedOut</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    activity_task_scheduled_event_attributes: NotRequired[
        "capo_swf.types.activity_task_scheduled_event_attributes.ActivityTaskScheduledEventAttributes"
    ]
    """<p>If the event is of type <code>ActivityTaskScheduled</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    activity_task_started_event_attributes: NotRequired[
        "capo_swf.types.activity_task_started_event_attributes.ActivityTaskStartedEventAttributes"
    ]
    """<p>If the event is of type <code>ActivityTaskStarted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    activity_task_completed_event_attributes: NotRequired[
        "capo_swf.types.activity_task_completed_event_attributes.ActivityTaskCompletedEventAttributes"
    ]
    """<p>If the event is of type <code>ActivityTaskCompleted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    activity_task_failed_event_attributes: NotRequired[
        "capo_swf.types.activity_task_failed_event_attributes.ActivityTaskFailedEventAttributes"
    ]
    """<p>If the event is of type <code>ActivityTaskFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    activity_task_timed_out_event_attributes: NotRequired[
        "capo_swf.types.activity_task_timed_out_event_attributes.ActivityTaskTimedOutEventAttributes"
    ]
    """<p>If the event is of type <code>ActivityTaskTimedOut</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    activity_task_canceled_event_attributes: NotRequired[
        "capo_swf.types.activity_task_canceled_event_attributes.ActivityTaskCanceledEventAttributes"
    ]
    """<p>If the event is of type <code>ActivityTaskCanceled</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    activity_task_cancel_requested_event_attributes: NotRequired[
        "capo_swf.types.activity_task_cancel_requested_event_attributes.ActivityTaskCancelRequestedEventAttributes"
    ]
    """<p>If the event is of type <code>ActivityTaskcancelRequested</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    workflow_execution_signaled_event_attributes: NotRequired[
        "capo_swf.types.workflow_execution_signaled_event_attributes.WorkflowExecutionSignaledEventAttributes"
    ]
    """<p>If the event is of type <code>WorkflowExecutionSignaled</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    marker_recorded_event_attributes: NotRequired[
        "capo_swf.types.marker_recorded_event_attributes.MarkerRecordedEventAttributes"
    ]
    """<p>If the event is of type <code>MarkerRecorded</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    record_marker_failed_event_attributes: NotRequired[
        "capo_swf.types.record_marker_failed_event_attributes.RecordMarkerFailedEventAttributes"
    ]
    """<p>If the event is of type <code>DecisionTaskFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    timer_started_event_attributes: NotRequired[
        "capo_swf.types.timer_started_event_attributes.TimerStartedEventAttributes"
    ]
    """<p>If the event is of type <code>TimerStarted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    timer_fired_event_attributes: NotRequired[
        "capo_swf.types.timer_fired_event_attributes.TimerFiredEventAttributes"
    ]
    """<p>If the event is of type <code>TimerFired</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    timer_canceled_event_attributes: NotRequired[
        "capo_swf.types.timer_canceled_event_attributes.TimerCanceledEventAttributes"
    ]
    """<p>If the event is of type <code>TimerCanceled</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    start_child_workflow_execution_initiated_event_attributes: NotRequired[
        "capo_swf.types.start_child_workflow_execution_initiated_event_attributes.StartChildWorkflowExecutionInitiatedEventAttributes"
    ]
    """<p>If the event is of type <code>StartChildWorkflowExecutionInitiated</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    child_workflow_execution_started_event_attributes: NotRequired[
        "capo_swf.types.child_workflow_execution_started_event_attributes.ChildWorkflowExecutionStartedEventAttributes"
    ]
    """<p>If the event is of type <code>ChildWorkflowExecutionStarted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    child_workflow_execution_completed_event_attributes: NotRequired[
        "capo_swf.types.child_workflow_execution_completed_event_attributes.ChildWorkflowExecutionCompletedEventAttributes"
    ]
    """<p>If the event is of type <code>ChildWorkflowExecutionCompleted</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    child_workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.child_workflow_execution_failed_event_attributes.ChildWorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>ChildWorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    child_workflow_execution_timed_out_event_attributes: NotRequired[
        "capo_swf.types.child_workflow_execution_timed_out_event_attributes.ChildWorkflowExecutionTimedOutEventAttributes"
    ]
    """<p>If the event is of type <code>ChildWorkflowExecutionTimedOut</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    child_workflow_execution_canceled_event_attributes: NotRequired[
        "capo_swf.types.child_workflow_execution_canceled_event_attributes.ChildWorkflowExecutionCanceledEventAttributes"
    ]
    """<p>If the event is of type <code>ChildWorkflowExecutionCanceled</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    child_workflow_execution_terminated_event_attributes: NotRequired[
        "capo_swf.types.child_workflow_execution_terminated_event_attributes.ChildWorkflowExecutionTerminatedEventAttributes"
    ]
    """<p>If the event is of type <code>ChildWorkflowExecutionTerminated</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    signal_external_workflow_execution_initiated_event_attributes: NotRequired[
        "capo_swf.types.signal_external_workflow_execution_initiated_event_attributes.SignalExternalWorkflowExecutionInitiatedEventAttributes"
    ]
    """<p>If the event is of type <code>SignalExternalWorkflowExecutionInitiated</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    external_workflow_execution_signaled_event_attributes: NotRequired[
        "capo_swf.types.external_workflow_execution_signaled_event_attributes.ExternalWorkflowExecutionSignaledEventAttributes"
    ]
    """<p>If the event is of type <code>ExternalWorkflowExecutionSignaled</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    signal_external_workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.signal_external_workflow_execution_failed_event_attributes.SignalExternalWorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>SignalExternalWorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    external_workflow_execution_cancel_requested_event_attributes: NotRequired[
        "capo_swf.types.external_workflow_execution_cancel_requested_event_attributes.ExternalWorkflowExecutionCancelRequestedEventAttributes"
    ]
    """<p>If the event is of type <code>ExternalWorkflowExecutionCancelRequested</code> then this member is set and provides detailed information about the event. It isn't set for other event types. </p>"""
    request_cancel_external_workflow_execution_initiated_event_attributes: NotRequired[
        "capo_swf.types.request_cancel_external_workflow_execution_initiated_event_attributes.RequestCancelExternalWorkflowExecutionInitiatedEventAttributes"
    ]
    """<p>If the event is of type <code>RequestCancelExternalWorkflowExecutionInitiated</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    request_cancel_external_workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.request_cancel_external_workflow_execution_failed_event_attributes.RequestCancelExternalWorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>RequestCancelExternalWorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    schedule_activity_task_failed_event_attributes: NotRequired[
        "capo_swf.types.schedule_activity_task_failed_event_attributes.ScheduleActivityTaskFailedEventAttributes"
    ]
    """<p>If the event is of type <code>ScheduleActivityTaskFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    request_cancel_activity_task_failed_event_attributes: NotRequired[
        "capo_swf.types.request_cancel_activity_task_failed_event_attributes.RequestCancelActivityTaskFailedEventAttributes"
    ]
    """<p>If the event is of type <code>RequestCancelActivityTaskFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    start_timer_failed_event_attributes: NotRequired[
        "capo_swf.types.start_timer_failed_event_attributes.StartTimerFailedEventAttributes"
    ]
    """<p>If the event is of type <code>StartTimerFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    cancel_timer_failed_event_attributes: NotRequired[
        "capo_swf.types.cancel_timer_failed_event_attributes.CancelTimerFailedEventAttributes"
    ]
    """<p>If the event is of type <code>CancelTimerFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    start_child_workflow_execution_failed_event_attributes: NotRequired[
        "capo_swf.types.start_child_workflow_execution_failed_event_attributes.StartChildWorkflowExecutionFailedEventAttributes"
    ]
    """<p>If the event is of type <code>StartChildWorkflowExecutionFailed</code> then this member is set and provides detailed information about the event. It isn't set for other event types.</p>"""
    lambda_function_scheduled_event_attributes: NotRequired[
        "capo_swf.types.lambda_function_scheduled_event_attributes.LambdaFunctionScheduledEventAttributes"
    ]
    """<p>Provides the details of the <code>LambdaFunctionScheduled</code> event. It isn't set for other event types.</p>"""
    lambda_function_started_event_attributes: NotRequired[
        "capo_swf.types.lambda_function_started_event_attributes.LambdaFunctionStartedEventAttributes"
    ]
    """<p>Provides the details of the <code>LambdaFunctionStarted</code> event. It isn't set for other event types.</p>"""
    lambda_function_completed_event_attributes: NotRequired[
        "capo_swf.types.lambda_function_completed_event_attributes.LambdaFunctionCompletedEventAttributes"
    ]
    """<p>Provides the details of the <code>LambdaFunctionCompleted</code> event. It isn't set for other event types.</p>"""
    lambda_function_failed_event_attributes: NotRequired[
        "capo_swf.types.lambda_function_failed_event_attributes.LambdaFunctionFailedEventAttributes"
    ]
    """<p>Provides the details of the <code>LambdaFunctionFailed</code> event. It isn't set for other event types.</p>"""
    lambda_function_timed_out_event_attributes: NotRequired[
        "capo_swf.types.lambda_function_timed_out_event_attributes.LambdaFunctionTimedOutEventAttributes"
    ]
    """<p>Provides the details of the <code>LambdaFunctionTimedOut</code> event. It isn't set for other event types.</p>"""
    schedule_lambda_function_failed_event_attributes: NotRequired[
        "capo_swf.types.schedule_lambda_function_failed_event_attributes.ScheduleLambdaFunctionFailedEventAttributes"
    ]
    """<p>Provides the details of the <code>ScheduleLambdaFunctionFailed</code> event. It isn't set for other event types.</p>"""
    start_lambda_function_failed_event_attributes: NotRequired[
        "capo_swf.types.start_lambda_function_failed_event_attributes.StartLambdaFunctionFailedEventAttributes"
    ]
    """<p>Provides the details of the <code>StartLambdaFunctionFailed</code> event. It isn't set for other event types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HistoryEvent) -> dict:
    out: dict = {}
    import capo_swf.types.timestamp

    out["eventTimestamp"] = capo_swf.types.timestamp.serialize_aws_json_1_0(
        value["event_timestamp"]
    )
    import capo_swf.types.event_type

    out["eventType"] = capo_swf.types.event_type.serialize_aws_json_1_0(
        value["event_type"]
    )
    out["eventId"] = value.get("event_id", 0)
    if "workflow_execution_started_event_attributes" in value:
        import capo_swf.types.workflow_execution_started_event_attributes

        out["workflowExecutionStartedEventAttributes"] = (
            capo_swf.types.workflow_execution_started_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_started_event_attributes"]
            )
        )
    if "workflow_execution_completed_event_attributes" in value:
        import capo_swf.types.workflow_execution_completed_event_attributes

        out["workflowExecutionCompletedEventAttributes"] = (
            capo_swf.types.workflow_execution_completed_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_completed_event_attributes"]
            )
        )
    if "complete_workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.complete_workflow_execution_failed_event_attributes

        out["completeWorkflowExecutionFailedEventAttributes"] = (
            capo_swf.types.complete_workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value["complete_workflow_execution_failed_event_attributes"]
            )
        )
    if "workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.workflow_execution_failed_event_attributes

        out["workflowExecutionFailedEventAttributes"] = (
            capo_swf.types.workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_failed_event_attributes"]
            )
        )
    if "fail_workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.fail_workflow_execution_failed_event_attributes

        out["failWorkflowExecutionFailedEventAttributes"] = (
            capo_swf.types.fail_workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value["fail_workflow_execution_failed_event_attributes"]
            )
        )
    if "workflow_execution_timed_out_event_attributes" in value:
        import capo_swf.types.workflow_execution_timed_out_event_attributes

        out["workflowExecutionTimedOutEventAttributes"] = (
            capo_swf.types.workflow_execution_timed_out_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_timed_out_event_attributes"]
            )
        )
    if "workflow_execution_canceled_event_attributes" in value:
        import capo_swf.types.workflow_execution_canceled_event_attributes

        out["workflowExecutionCanceledEventAttributes"] = (
            capo_swf.types.workflow_execution_canceled_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_canceled_event_attributes"]
            )
        )
    if "cancel_workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.cancel_workflow_execution_failed_event_attributes

        out["cancelWorkflowExecutionFailedEventAttributes"] = (
            capo_swf.types.cancel_workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value["cancel_workflow_execution_failed_event_attributes"]
            )
        )
    if "workflow_execution_continued_as_new_event_attributes" in value:
        import capo_swf.types.workflow_execution_continued_as_new_event_attributes

        out["workflowExecutionContinuedAsNewEventAttributes"] = (
            capo_swf.types.workflow_execution_continued_as_new_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_continued_as_new_event_attributes"]
            )
        )
    if "continue_as_new_workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.continue_as_new_workflow_execution_failed_event_attributes

        out["continueAsNewWorkflowExecutionFailedEventAttributes"] = (
            capo_swf.types.continue_as_new_workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value["continue_as_new_workflow_execution_failed_event_attributes"]
            )
        )
    if "workflow_execution_terminated_event_attributes" in value:
        import capo_swf.types.workflow_execution_terminated_event_attributes

        out["workflowExecutionTerminatedEventAttributes"] = (
            capo_swf.types.workflow_execution_terminated_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_terminated_event_attributes"]
            )
        )
    if "workflow_execution_cancel_requested_event_attributes" in value:
        import capo_swf.types.workflow_execution_cancel_requested_event_attributes

        out["workflowExecutionCancelRequestedEventAttributes"] = (
            capo_swf.types.workflow_execution_cancel_requested_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_cancel_requested_event_attributes"]
            )
        )
    if "decision_task_scheduled_event_attributes" in value:
        import capo_swf.types.decision_task_scheduled_event_attributes

        out["decisionTaskScheduledEventAttributes"] = (
            capo_swf.types.decision_task_scheduled_event_attributes.serialize_aws_json_1_0(
                value["decision_task_scheduled_event_attributes"]
            )
        )
    if "decision_task_started_event_attributes" in value:
        import capo_swf.types.decision_task_started_event_attributes

        out["decisionTaskStartedEventAttributes"] = (
            capo_swf.types.decision_task_started_event_attributes.serialize_aws_json_1_0(
                value["decision_task_started_event_attributes"]
            )
        )
    if "decision_task_completed_event_attributes" in value:
        import capo_swf.types.decision_task_completed_event_attributes

        out["decisionTaskCompletedEventAttributes"] = (
            capo_swf.types.decision_task_completed_event_attributes.serialize_aws_json_1_0(
                value["decision_task_completed_event_attributes"]
            )
        )
    if "decision_task_timed_out_event_attributes" in value:
        import capo_swf.types.decision_task_timed_out_event_attributes

        out["decisionTaskTimedOutEventAttributes"] = (
            capo_swf.types.decision_task_timed_out_event_attributes.serialize_aws_json_1_0(
                value["decision_task_timed_out_event_attributes"]
            )
        )
    if "activity_task_scheduled_event_attributes" in value:
        import capo_swf.types.activity_task_scheduled_event_attributes

        out["activityTaskScheduledEventAttributes"] = (
            capo_swf.types.activity_task_scheduled_event_attributes.serialize_aws_json_1_0(
                value["activity_task_scheduled_event_attributes"]
            )
        )
    if "activity_task_started_event_attributes" in value:
        import capo_swf.types.activity_task_started_event_attributes

        out["activityTaskStartedEventAttributes"] = (
            capo_swf.types.activity_task_started_event_attributes.serialize_aws_json_1_0(
                value["activity_task_started_event_attributes"]
            )
        )
    if "activity_task_completed_event_attributes" in value:
        import capo_swf.types.activity_task_completed_event_attributes

        out["activityTaskCompletedEventAttributes"] = (
            capo_swf.types.activity_task_completed_event_attributes.serialize_aws_json_1_0(
                value["activity_task_completed_event_attributes"]
            )
        )
    if "activity_task_failed_event_attributes" in value:
        import capo_swf.types.activity_task_failed_event_attributes

        out["activityTaskFailedEventAttributes"] = (
            capo_swf.types.activity_task_failed_event_attributes.serialize_aws_json_1_0(
                value["activity_task_failed_event_attributes"]
            )
        )
    if "activity_task_timed_out_event_attributes" in value:
        import capo_swf.types.activity_task_timed_out_event_attributes

        out["activityTaskTimedOutEventAttributes"] = (
            capo_swf.types.activity_task_timed_out_event_attributes.serialize_aws_json_1_0(
                value["activity_task_timed_out_event_attributes"]
            )
        )
    if "activity_task_canceled_event_attributes" in value:
        import capo_swf.types.activity_task_canceled_event_attributes

        out["activityTaskCanceledEventAttributes"] = (
            capo_swf.types.activity_task_canceled_event_attributes.serialize_aws_json_1_0(
                value["activity_task_canceled_event_attributes"]
            )
        )
    if "activity_task_cancel_requested_event_attributes" in value:
        import capo_swf.types.activity_task_cancel_requested_event_attributes

        out["activityTaskCancelRequestedEventAttributes"] = (
            capo_swf.types.activity_task_cancel_requested_event_attributes.serialize_aws_json_1_0(
                value["activity_task_cancel_requested_event_attributes"]
            )
        )
    if "workflow_execution_signaled_event_attributes" in value:
        import capo_swf.types.workflow_execution_signaled_event_attributes

        out["workflowExecutionSignaledEventAttributes"] = (
            capo_swf.types.workflow_execution_signaled_event_attributes.serialize_aws_json_1_0(
                value["workflow_execution_signaled_event_attributes"]
            )
        )
    if "marker_recorded_event_attributes" in value:
        import capo_swf.types.marker_recorded_event_attributes

        out["markerRecordedEventAttributes"] = (
            capo_swf.types.marker_recorded_event_attributes.serialize_aws_json_1_0(
                value["marker_recorded_event_attributes"]
            )
        )
    if "record_marker_failed_event_attributes" in value:
        import capo_swf.types.record_marker_failed_event_attributes

        out["recordMarkerFailedEventAttributes"] = (
            capo_swf.types.record_marker_failed_event_attributes.serialize_aws_json_1_0(
                value["record_marker_failed_event_attributes"]
            )
        )
    if "timer_started_event_attributes" in value:
        import capo_swf.types.timer_started_event_attributes

        out["timerStartedEventAttributes"] = (
            capo_swf.types.timer_started_event_attributes.serialize_aws_json_1_0(
                value["timer_started_event_attributes"]
            )
        )
    if "timer_fired_event_attributes" in value:
        import capo_swf.types.timer_fired_event_attributes

        out["timerFiredEventAttributes"] = (
            capo_swf.types.timer_fired_event_attributes.serialize_aws_json_1_0(
                value["timer_fired_event_attributes"]
            )
        )
    if "timer_canceled_event_attributes" in value:
        import capo_swf.types.timer_canceled_event_attributes

        out["timerCanceledEventAttributes"] = (
            capo_swf.types.timer_canceled_event_attributes.serialize_aws_json_1_0(
                value["timer_canceled_event_attributes"]
            )
        )
    if "start_child_workflow_execution_initiated_event_attributes" in value:
        import capo_swf.types.start_child_workflow_execution_initiated_event_attributes

        out["startChildWorkflowExecutionInitiatedEventAttributes"] = (
            capo_swf.types.start_child_workflow_execution_initiated_event_attributes.serialize_aws_json_1_0(
                value["start_child_workflow_execution_initiated_event_attributes"]
            )
        )
    if "child_workflow_execution_started_event_attributes" in value:
        import capo_swf.types.child_workflow_execution_started_event_attributes

        out["childWorkflowExecutionStartedEventAttributes"] = (
            capo_swf.types.child_workflow_execution_started_event_attributes.serialize_aws_json_1_0(
                value["child_workflow_execution_started_event_attributes"]
            )
        )
    if "child_workflow_execution_completed_event_attributes" in value:
        import capo_swf.types.child_workflow_execution_completed_event_attributes

        out["childWorkflowExecutionCompletedEventAttributes"] = (
            capo_swf.types.child_workflow_execution_completed_event_attributes.serialize_aws_json_1_0(
                value["child_workflow_execution_completed_event_attributes"]
            )
        )
    if "child_workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.child_workflow_execution_failed_event_attributes

        out["childWorkflowExecutionFailedEventAttributes"] = (
            capo_swf.types.child_workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value["child_workflow_execution_failed_event_attributes"]
            )
        )
    if "child_workflow_execution_timed_out_event_attributes" in value:
        import capo_swf.types.child_workflow_execution_timed_out_event_attributes

        out["childWorkflowExecutionTimedOutEventAttributes"] = (
            capo_swf.types.child_workflow_execution_timed_out_event_attributes.serialize_aws_json_1_0(
                value["child_workflow_execution_timed_out_event_attributes"]
            )
        )
    if "child_workflow_execution_canceled_event_attributes" in value:
        import capo_swf.types.child_workflow_execution_canceled_event_attributes

        out["childWorkflowExecutionCanceledEventAttributes"] = (
            capo_swf.types.child_workflow_execution_canceled_event_attributes.serialize_aws_json_1_0(
                value["child_workflow_execution_canceled_event_attributes"]
            )
        )
    if "child_workflow_execution_terminated_event_attributes" in value:
        import capo_swf.types.child_workflow_execution_terminated_event_attributes

        out["childWorkflowExecutionTerminatedEventAttributes"] = (
            capo_swf.types.child_workflow_execution_terminated_event_attributes.serialize_aws_json_1_0(
                value["child_workflow_execution_terminated_event_attributes"]
            )
        )
    if "signal_external_workflow_execution_initiated_event_attributes" in value:
        import capo_swf.types.signal_external_workflow_execution_initiated_event_attributes

        out["signalExternalWorkflowExecutionInitiatedEventAttributes"] = (
            capo_swf.types.signal_external_workflow_execution_initiated_event_attributes.serialize_aws_json_1_0(
                value["signal_external_workflow_execution_initiated_event_attributes"]
            )
        )
    if "external_workflow_execution_signaled_event_attributes" in value:
        import capo_swf.types.external_workflow_execution_signaled_event_attributes

        out["externalWorkflowExecutionSignaledEventAttributes"] = (
            capo_swf.types.external_workflow_execution_signaled_event_attributes.serialize_aws_json_1_0(
                value["external_workflow_execution_signaled_event_attributes"]
            )
        )
    if "signal_external_workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.signal_external_workflow_execution_failed_event_attributes

        out["signalExternalWorkflowExecutionFailedEventAttributes"] = (
            capo_swf.types.signal_external_workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value["signal_external_workflow_execution_failed_event_attributes"]
            )
        )
    if "external_workflow_execution_cancel_requested_event_attributes" in value:
        import capo_swf.types.external_workflow_execution_cancel_requested_event_attributes

        out["externalWorkflowExecutionCancelRequestedEventAttributes"] = (
            capo_swf.types.external_workflow_execution_cancel_requested_event_attributes.serialize_aws_json_1_0(
                value["external_workflow_execution_cancel_requested_event_attributes"]
            )
        )
    if "request_cancel_external_workflow_execution_initiated_event_attributes" in value:
        import capo_swf.types.request_cancel_external_workflow_execution_initiated_event_attributes

        out["requestCancelExternalWorkflowExecutionInitiatedEventAttributes"] = (
            capo_swf.types.request_cancel_external_workflow_execution_initiated_event_attributes.serialize_aws_json_1_0(
                value[
                    "request_cancel_external_workflow_execution_initiated_event_attributes"
                ]
            )
        )
    if "request_cancel_external_workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.request_cancel_external_workflow_execution_failed_event_attributes

        out["requestCancelExternalWorkflowExecutionFailedEventAttributes"] = (
            capo_swf.types.request_cancel_external_workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value[
                    "request_cancel_external_workflow_execution_failed_event_attributes"
                ]
            )
        )
    if "schedule_activity_task_failed_event_attributes" in value:
        import capo_swf.types.schedule_activity_task_failed_event_attributes

        out["scheduleActivityTaskFailedEventAttributes"] = (
            capo_swf.types.schedule_activity_task_failed_event_attributes.serialize_aws_json_1_0(
                value["schedule_activity_task_failed_event_attributes"]
            )
        )
    if "request_cancel_activity_task_failed_event_attributes" in value:
        import capo_swf.types.request_cancel_activity_task_failed_event_attributes

        out["requestCancelActivityTaskFailedEventAttributes"] = (
            capo_swf.types.request_cancel_activity_task_failed_event_attributes.serialize_aws_json_1_0(
                value["request_cancel_activity_task_failed_event_attributes"]
            )
        )
    if "start_timer_failed_event_attributes" in value:
        import capo_swf.types.start_timer_failed_event_attributes

        out["startTimerFailedEventAttributes"] = (
            capo_swf.types.start_timer_failed_event_attributes.serialize_aws_json_1_0(
                value["start_timer_failed_event_attributes"]
            )
        )
    if "cancel_timer_failed_event_attributes" in value:
        import capo_swf.types.cancel_timer_failed_event_attributes

        out["cancelTimerFailedEventAttributes"] = (
            capo_swf.types.cancel_timer_failed_event_attributes.serialize_aws_json_1_0(
                value["cancel_timer_failed_event_attributes"]
            )
        )
    if "start_child_workflow_execution_failed_event_attributes" in value:
        import capo_swf.types.start_child_workflow_execution_failed_event_attributes

        out["startChildWorkflowExecutionFailedEventAttributes"] = (
            capo_swf.types.start_child_workflow_execution_failed_event_attributes.serialize_aws_json_1_0(
                value["start_child_workflow_execution_failed_event_attributes"]
            )
        )
    if "lambda_function_scheduled_event_attributes" in value:
        import capo_swf.types.lambda_function_scheduled_event_attributes

        out["lambdaFunctionScheduledEventAttributes"] = (
            capo_swf.types.lambda_function_scheduled_event_attributes.serialize_aws_json_1_0(
                value["lambda_function_scheduled_event_attributes"]
            )
        )
    if "lambda_function_started_event_attributes" in value:
        import capo_swf.types.lambda_function_started_event_attributes

        out["lambdaFunctionStartedEventAttributes"] = (
            capo_swf.types.lambda_function_started_event_attributes.serialize_aws_json_1_0(
                value["lambda_function_started_event_attributes"]
            )
        )
    if "lambda_function_completed_event_attributes" in value:
        import capo_swf.types.lambda_function_completed_event_attributes

        out["lambdaFunctionCompletedEventAttributes"] = (
            capo_swf.types.lambda_function_completed_event_attributes.serialize_aws_json_1_0(
                value["lambda_function_completed_event_attributes"]
            )
        )
    if "lambda_function_failed_event_attributes" in value:
        import capo_swf.types.lambda_function_failed_event_attributes

        out["lambdaFunctionFailedEventAttributes"] = (
            capo_swf.types.lambda_function_failed_event_attributes.serialize_aws_json_1_0(
                value["lambda_function_failed_event_attributes"]
            )
        )
    if "lambda_function_timed_out_event_attributes" in value:
        import capo_swf.types.lambda_function_timed_out_event_attributes

        out["lambdaFunctionTimedOutEventAttributes"] = (
            capo_swf.types.lambda_function_timed_out_event_attributes.serialize_aws_json_1_0(
                value["lambda_function_timed_out_event_attributes"]
            )
        )
    if "schedule_lambda_function_failed_event_attributes" in value:
        import capo_swf.types.schedule_lambda_function_failed_event_attributes

        out["scheduleLambdaFunctionFailedEventAttributes"] = (
            capo_swf.types.schedule_lambda_function_failed_event_attributes.serialize_aws_json_1_0(
                value["schedule_lambda_function_failed_event_attributes"]
            )
        )
    if "start_lambda_function_failed_event_attributes" in value:
        import capo_swf.types.start_lambda_function_failed_event_attributes

        out["startLambdaFunctionFailedEventAttributes"] = (
            capo_swf.types.start_lambda_function_failed_event_attributes.serialize_aws_json_1_0(
                value["start_lambda_function_failed_event_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> HistoryEvent:
    out: HistoryEvent = {}  # type: ignore[typeddict-item]
    if data.get("eventTimestamp") is not None:
        import capo_swf.types.timestamp

        out["event_timestamp"] = capo_swf.types.timestamp.deserialize_aws_json_1_0(
            data["eventTimestamp"]
        )
    else:
        import datetime

        out["event_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("eventType") is not None:
        import capo_swf.types.event_type

        out["event_type"] = capo_swf.types.event_type.deserialize_aws_json_1_0(
            data["eventType"]
        )
    else:
        import typing

        out["event_type"] = typing.cast("capo_swf.types.event_type.EventType", "")
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        out["event_id"] = 0
    if data.get("workflowExecutionStartedEventAttributes") is not None:
        import capo_swf.types.workflow_execution_started_event_attributes

        out["workflow_execution_started_event_attributes"] = (
            capo_swf.types.workflow_execution_started_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionStartedEventAttributes"]
            )
        )
    if data.get("workflowExecutionCompletedEventAttributes") is not None:
        import capo_swf.types.workflow_execution_completed_event_attributes

        out["workflow_execution_completed_event_attributes"] = (
            capo_swf.types.workflow_execution_completed_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionCompletedEventAttributes"]
            )
        )
    if data.get("completeWorkflowExecutionFailedEventAttributes") is not None:
        import capo_swf.types.complete_workflow_execution_failed_event_attributes

        out["complete_workflow_execution_failed_event_attributes"] = (
            capo_swf.types.complete_workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["completeWorkflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("workflowExecutionFailedEventAttributes") is not None:
        import capo_swf.types.workflow_execution_failed_event_attributes

        out["workflow_execution_failed_event_attributes"] = (
            capo_swf.types.workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("failWorkflowExecutionFailedEventAttributes") is not None:
        import capo_swf.types.fail_workflow_execution_failed_event_attributes

        out["fail_workflow_execution_failed_event_attributes"] = (
            capo_swf.types.fail_workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["failWorkflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("workflowExecutionTimedOutEventAttributes") is not None:
        import capo_swf.types.workflow_execution_timed_out_event_attributes

        out["workflow_execution_timed_out_event_attributes"] = (
            capo_swf.types.workflow_execution_timed_out_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionTimedOutEventAttributes"]
            )
        )
    if data.get("workflowExecutionCanceledEventAttributes") is not None:
        import capo_swf.types.workflow_execution_canceled_event_attributes

        out["workflow_execution_canceled_event_attributes"] = (
            capo_swf.types.workflow_execution_canceled_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionCanceledEventAttributes"]
            )
        )
    if data.get("cancelWorkflowExecutionFailedEventAttributes") is not None:
        import capo_swf.types.cancel_workflow_execution_failed_event_attributes

        out["cancel_workflow_execution_failed_event_attributes"] = (
            capo_swf.types.cancel_workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["cancelWorkflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("workflowExecutionContinuedAsNewEventAttributes") is not None:
        import capo_swf.types.workflow_execution_continued_as_new_event_attributes

        out["workflow_execution_continued_as_new_event_attributes"] = (
            capo_swf.types.workflow_execution_continued_as_new_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionContinuedAsNewEventAttributes"]
            )
        )
    if data.get("continueAsNewWorkflowExecutionFailedEventAttributes") is not None:
        import capo_swf.types.continue_as_new_workflow_execution_failed_event_attributes

        out["continue_as_new_workflow_execution_failed_event_attributes"] = (
            capo_swf.types.continue_as_new_workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["continueAsNewWorkflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("workflowExecutionTerminatedEventAttributes") is not None:
        import capo_swf.types.workflow_execution_terminated_event_attributes

        out["workflow_execution_terminated_event_attributes"] = (
            capo_swf.types.workflow_execution_terminated_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionTerminatedEventAttributes"]
            )
        )
    if data.get("workflowExecutionCancelRequestedEventAttributes") is not None:
        import capo_swf.types.workflow_execution_cancel_requested_event_attributes

        out["workflow_execution_cancel_requested_event_attributes"] = (
            capo_swf.types.workflow_execution_cancel_requested_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionCancelRequestedEventAttributes"]
            )
        )
    if data.get("decisionTaskScheduledEventAttributes") is not None:
        import capo_swf.types.decision_task_scheduled_event_attributes

        out["decision_task_scheduled_event_attributes"] = (
            capo_swf.types.decision_task_scheduled_event_attributes.deserialize_aws_json_1_0(
                data["decisionTaskScheduledEventAttributes"]
            )
        )
    if data.get("decisionTaskStartedEventAttributes") is not None:
        import capo_swf.types.decision_task_started_event_attributes

        out["decision_task_started_event_attributes"] = (
            capo_swf.types.decision_task_started_event_attributes.deserialize_aws_json_1_0(
                data["decisionTaskStartedEventAttributes"]
            )
        )
    if data.get("decisionTaskCompletedEventAttributes") is not None:
        import capo_swf.types.decision_task_completed_event_attributes

        out["decision_task_completed_event_attributes"] = (
            capo_swf.types.decision_task_completed_event_attributes.deserialize_aws_json_1_0(
                data["decisionTaskCompletedEventAttributes"]
            )
        )
    if data.get("decisionTaskTimedOutEventAttributes") is not None:
        import capo_swf.types.decision_task_timed_out_event_attributes

        out["decision_task_timed_out_event_attributes"] = (
            capo_swf.types.decision_task_timed_out_event_attributes.deserialize_aws_json_1_0(
                data["decisionTaskTimedOutEventAttributes"]
            )
        )
    if data.get("activityTaskScheduledEventAttributes") is not None:
        import capo_swf.types.activity_task_scheduled_event_attributes

        out["activity_task_scheduled_event_attributes"] = (
            capo_swf.types.activity_task_scheduled_event_attributes.deserialize_aws_json_1_0(
                data["activityTaskScheduledEventAttributes"]
            )
        )
    if data.get("activityTaskStartedEventAttributes") is not None:
        import capo_swf.types.activity_task_started_event_attributes

        out["activity_task_started_event_attributes"] = (
            capo_swf.types.activity_task_started_event_attributes.deserialize_aws_json_1_0(
                data["activityTaskStartedEventAttributes"]
            )
        )
    if data.get("activityTaskCompletedEventAttributes") is not None:
        import capo_swf.types.activity_task_completed_event_attributes

        out["activity_task_completed_event_attributes"] = (
            capo_swf.types.activity_task_completed_event_attributes.deserialize_aws_json_1_0(
                data["activityTaskCompletedEventAttributes"]
            )
        )
    if data.get("activityTaskFailedEventAttributes") is not None:
        import capo_swf.types.activity_task_failed_event_attributes

        out["activity_task_failed_event_attributes"] = (
            capo_swf.types.activity_task_failed_event_attributes.deserialize_aws_json_1_0(
                data["activityTaskFailedEventAttributes"]
            )
        )
    if data.get("activityTaskTimedOutEventAttributes") is not None:
        import capo_swf.types.activity_task_timed_out_event_attributes

        out["activity_task_timed_out_event_attributes"] = (
            capo_swf.types.activity_task_timed_out_event_attributes.deserialize_aws_json_1_0(
                data["activityTaskTimedOutEventAttributes"]
            )
        )
    if data.get("activityTaskCanceledEventAttributes") is not None:
        import capo_swf.types.activity_task_canceled_event_attributes

        out["activity_task_canceled_event_attributes"] = (
            capo_swf.types.activity_task_canceled_event_attributes.deserialize_aws_json_1_0(
                data["activityTaskCanceledEventAttributes"]
            )
        )
    if data.get("activityTaskCancelRequestedEventAttributes") is not None:
        import capo_swf.types.activity_task_cancel_requested_event_attributes

        out["activity_task_cancel_requested_event_attributes"] = (
            capo_swf.types.activity_task_cancel_requested_event_attributes.deserialize_aws_json_1_0(
                data["activityTaskCancelRequestedEventAttributes"]
            )
        )
    if data.get("workflowExecutionSignaledEventAttributes") is not None:
        import capo_swf.types.workflow_execution_signaled_event_attributes

        out["workflow_execution_signaled_event_attributes"] = (
            capo_swf.types.workflow_execution_signaled_event_attributes.deserialize_aws_json_1_0(
                data["workflowExecutionSignaledEventAttributes"]
            )
        )
    if data.get("markerRecordedEventAttributes") is not None:
        import capo_swf.types.marker_recorded_event_attributes

        out["marker_recorded_event_attributes"] = (
            capo_swf.types.marker_recorded_event_attributes.deserialize_aws_json_1_0(
                data["markerRecordedEventAttributes"]
            )
        )
    if data.get("recordMarkerFailedEventAttributes") is not None:
        import capo_swf.types.record_marker_failed_event_attributes

        out["record_marker_failed_event_attributes"] = (
            capo_swf.types.record_marker_failed_event_attributes.deserialize_aws_json_1_0(
                data["recordMarkerFailedEventAttributes"]
            )
        )
    if data.get("timerStartedEventAttributes") is not None:
        import capo_swf.types.timer_started_event_attributes

        out["timer_started_event_attributes"] = (
            capo_swf.types.timer_started_event_attributes.deserialize_aws_json_1_0(
                data["timerStartedEventAttributes"]
            )
        )
    if data.get("timerFiredEventAttributes") is not None:
        import capo_swf.types.timer_fired_event_attributes

        out["timer_fired_event_attributes"] = (
            capo_swf.types.timer_fired_event_attributes.deserialize_aws_json_1_0(
                data["timerFiredEventAttributes"]
            )
        )
    if data.get("timerCanceledEventAttributes") is not None:
        import capo_swf.types.timer_canceled_event_attributes

        out["timer_canceled_event_attributes"] = (
            capo_swf.types.timer_canceled_event_attributes.deserialize_aws_json_1_0(
                data["timerCanceledEventAttributes"]
            )
        )
    if data.get("startChildWorkflowExecutionInitiatedEventAttributes") is not None:
        import capo_swf.types.start_child_workflow_execution_initiated_event_attributes

        out["start_child_workflow_execution_initiated_event_attributes"] = (
            capo_swf.types.start_child_workflow_execution_initiated_event_attributes.deserialize_aws_json_1_0(
                data["startChildWorkflowExecutionInitiatedEventAttributes"]
            )
        )
    if data.get("childWorkflowExecutionStartedEventAttributes") is not None:
        import capo_swf.types.child_workflow_execution_started_event_attributes

        out["child_workflow_execution_started_event_attributes"] = (
            capo_swf.types.child_workflow_execution_started_event_attributes.deserialize_aws_json_1_0(
                data["childWorkflowExecutionStartedEventAttributes"]
            )
        )
    if data.get("childWorkflowExecutionCompletedEventAttributes") is not None:
        import capo_swf.types.child_workflow_execution_completed_event_attributes

        out["child_workflow_execution_completed_event_attributes"] = (
            capo_swf.types.child_workflow_execution_completed_event_attributes.deserialize_aws_json_1_0(
                data["childWorkflowExecutionCompletedEventAttributes"]
            )
        )
    if data.get("childWorkflowExecutionFailedEventAttributes") is not None:
        import capo_swf.types.child_workflow_execution_failed_event_attributes

        out["child_workflow_execution_failed_event_attributes"] = (
            capo_swf.types.child_workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["childWorkflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("childWorkflowExecutionTimedOutEventAttributes") is not None:
        import capo_swf.types.child_workflow_execution_timed_out_event_attributes

        out["child_workflow_execution_timed_out_event_attributes"] = (
            capo_swf.types.child_workflow_execution_timed_out_event_attributes.deserialize_aws_json_1_0(
                data["childWorkflowExecutionTimedOutEventAttributes"]
            )
        )
    if data.get("childWorkflowExecutionCanceledEventAttributes") is not None:
        import capo_swf.types.child_workflow_execution_canceled_event_attributes

        out["child_workflow_execution_canceled_event_attributes"] = (
            capo_swf.types.child_workflow_execution_canceled_event_attributes.deserialize_aws_json_1_0(
                data["childWorkflowExecutionCanceledEventAttributes"]
            )
        )
    if data.get("childWorkflowExecutionTerminatedEventAttributes") is not None:
        import capo_swf.types.child_workflow_execution_terminated_event_attributes

        out["child_workflow_execution_terminated_event_attributes"] = (
            capo_swf.types.child_workflow_execution_terminated_event_attributes.deserialize_aws_json_1_0(
                data["childWorkflowExecutionTerminatedEventAttributes"]
            )
        )
    if data.get("signalExternalWorkflowExecutionInitiatedEventAttributes") is not None:
        import capo_swf.types.signal_external_workflow_execution_initiated_event_attributes

        out["signal_external_workflow_execution_initiated_event_attributes"] = (
            capo_swf.types.signal_external_workflow_execution_initiated_event_attributes.deserialize_aws_json_1_0(
                data["signalExternalWorkflowExecutionInitiatedEventAttributes"]
            )
        )
    if data.get("externalWorkflowExecutionSignaledEventAttributes") is not None:
        import capo_swf.types.external_workflow_execution_signaled_event_attributes

        out["external_workflow_execution_signaled_event_attributes"] = (
            capo_swf.types.external_workflow_execution_signaled_event_attributes.deserialize_aws_json_1_0(
                data["externalWorkflowExecutionSignaledEventAttributes"]
            )
        )
    if data.get("signalExternalWorkflowExecutionFailedEventAttributes") is not None:
        import capo_swf.types.signal_external_workflow_execution_failed_event_attributes

        out["signal_external_workflow_execution_failed_event_attributes"] = (
            capo_swf.types.signal_external_workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["signalExternalWorkflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("externalWorkflowExecutionCancelRequestedEventAttributes") is not None:
        import capo_swf.types.external_workflow_execution_cancel_requested_event_attributes

        out["external_workflow_execution_cancel_requested_event_attributes"] = (
            capo_swf.types.external_workflow_execution_cancel_requested_event_attributes.deserialize_aws_json_1_0(
                data["externalWorkflowExecutionCancelRequestedEventAttributes"]
            )
        )
    if (
        data.get("requestCancelExternalWorkflowExecutionInitiatedEventAttributes")
        is not None
    ):
        import capo_swf.types.request_cancel_external_workflow_execution_initiated_event_attributes

        out["request_cancel_external_workflow_execution_initiated_event_attributes"] = (
            capo_swf.types.request_cancel_external_workflow_execution_initiated_event_attributes.deserialize_aws_json_1_0(
                data["requestCancelExternalWorkflowExecutionInitiatedEventAttributes"]
            )
        )
    if (
        data.get("requestCancelExternalWorkflowExecutionFailedEventAttributes")
        is not None
    ):
        import capo_swf.types.request_cancel_external_workflow_execution_failed_event_attributes

        out["request_cancel_external_workflow_execution_failed_event_attributes"] = (
            capo_swf.types.request_cancel_external_workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["requestCancelExternalWorkflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("scheduleActivityTaskFailedEventAttributes") is not None:
        import capo_swf.types.schedule_activity_task_failed_event_attributes

        out["schedule_activity_task_failed_event_attributes"] = (
            capo_swf.types.schedule_activity_task_failed_event_attributes.deserialize_aws_json_1_0(
                data["scheduleActivityTaskFailedEventAttributes"]
            )
        )
    if data.get("requestCancelActivityTaskFailedEventAttributes") is not None:
        import capo_swf.types.request_cancel_activity_task_failed_event_attributes

        out["request_cancel_activity_task_failed_event_attributes"] = (
            capo_swf.types.request_cancel_activity_task_failed_event_attributes.deserialize_aws_json_1_0(
                data["requestCancelActivityTaskFailedEventAttributes"]
            )
        )
    if data.get("startTimerFailedEventAttributes") is not None:
        import capo_swf.types.start_timer_failed_event_attributes

        out["start_timer_failed_event_attributes"] = (
            capo_swf.types.start_timer_failed_event_attributes.deserialize_aws_json_1_0(
                data["startTimerFailedEventAttributes"]
            )
        )
    if data.get("cancelTimerFailedEventAttributes") is not None:
        import capo_swf.types.cancel_timer_failed_event_attributes

        out["cancel_timer_failed_event_attributes"] = (
            capo_swf.types.cancel_timer_failed_event_attributes.deserialize_aws_json_1_0(
                data["cancelTimerFailedEventAttributes"]
            )
        )
    if data.get("startChildWorkflowExecutionFailedEventAttributes") is not None:
        import capo_swf.types.start_child_workflow_execution_failed_event_attributes

        out["start_child_workflow_execution_failed_event_attributes"] = (
            capo_swf.types.start_child_workflow_execution_failed_event_attributes.deserialize_aws_json_1_0(
                data["startChildWorkflowExecutionFailedEventAttributes"]
            )
        )
    if data.get("lambdaFunctionScheduledEventAttributes") is not None:
        import capo_swf.types.lambda_function_scheduled_event_attributes

        out["lambda_function_scheduled_event_attributes"] = (
            capo_swf.types.lambda_function_scheduled_event_attributes.deserialize_aws_json_1_0(
                data["lambdaFunctionScheduledEventAttributes"]
            )
        )
    if data.get("lambdaFunctionStartedEventAttributes") is not None:
        import capo_swf.types.lambda_function_started_event_attributes

        out["lambda_function_started_event_attributes"] = (
            capo_swf.types.lambda_function_started_event_attributes.deserialize_aws_json_1_0(
                data["lambdaFunctionStartedEventAttributes"]
            )
        )
    if data.get("lambdaFunctionCompletedEventAttributes") is not None:
        import capo_swf.types.lambda_function_completed_event_attributes

        out["lambda_function_completed_event_attributes"] = (
            capo_swf.types.lambda_function_completed_event_attributes.deserialize_aws_json_1_0(
                data["lambdaFunctionCompletedEventAttributes"]
            )
        )
    if data.get("lambdaFunctionFailedEventAttributes") is not None:
        import capo_swf.types.lambda_function_failed_event_attributes

        out["lambda_function_failed_event_attributes"] = (
            capo_swf.types.lambda_function_failed_event_attributes.deserialize_aws_json_1_0(
                data["lambdaFunctionFailedEventAttributes"]
            )
        )
    if data.get("lambdaFunctionTimedOutEventAttributes") is not None:
        import capo_swf.types.lambda_function_timed_out_event_attributes

        out["lambda_function_timed_out_event_attributes"] = (
            capo_swf.types.lambda_function_timed_out_event_attributes.deserialize_aws_json_1_0(
                data["lambdaFunctionTimedOutEventAttributes"]
            )
        )
    if data.get("scheduleLambdaFunctionFailedEventAttributes") is not None:
        import capo_swf.types.schedule_lambda_function_failed_event_attributes

        out["schedule_lambda_function_failed_event_attributes"] = (
            capo_swf.types.schedule_lambda_function_failed_event_attributes.deserialize_aws_json_1_0(
                data["scheduleLambdaFunctionFailedEventAttributes"]
            )
        )
    if data.get("startLambdaFunctionFailedEventAttributes") is not None:
        import capo_swf.types.start_lambda_function_failed_event_attributes

        out["start_lambda_function_failed_event_attributes"] = (
            capo_swf.types.start_lambda_function_failed_event_attributes.deserialize_aws_json_1_0(
                data["startLambdaFunctionFailedEventAttributes"]
            )
        )
    return out
