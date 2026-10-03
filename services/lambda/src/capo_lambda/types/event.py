"""Generated from Smithy shape ``com.amazonaws.lambda#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.callback_failed_details
    import capo_lambda.types.callback_started_details
    import capo_lambda.types.callback_succeeded_details
    import capo_lambda.types.callback_timed_out_details
    import capo_lambda.types.chained_invoke_failed_details
    import capo_lambda.types.chained_invoke_started_details
    import capo_lambda.types.chained_invoke_stopped_details
    import capo_lambda.types.chained_invoke_succeeded_details
    import capo_lambda.types.chained_invoke_timed_out_details
    import capo_lambda.types.context_failed_details
    import capo_lambda.types.context_started_details
    import capo_lambda.types.context_succeeded_details
    import capo_lambda.types.event_id
    import capo_lambda.types.event_type
    import capo_lambda.types.execution_failed_details
    import capo_lambda.types.execution_started_details
    import capo_lambda.types.execution_stopped_details
    import capo_lambda.types.execution_succeeded_details
    import capo_lambda.types.execution_timed_out_details
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.invocation_completed_details
    import capo_lambda.types.operation_id
    import capo_lambda.types.operation_name
    import capo_lambda.types.operation_sub_type
    import capo_lambda.types.step_failed_details
    import capo_lambda.types.step_started_details
    import capo_lambda.types.step_succeeded_details
    import capo_lambda.types.wait_cancelled_details
    import capo_lambda.types.wait_started_details
    import capo_lambda.types.wait_succeeded_details


class Event(TypedDict, closed=True):
    event_type: NotRequired["capo_lambda.types.event_type.EventType"]
    """<p>The type of event that occurred.</p>"""
    sub_type: NotRequired["capo_lambda.types.operation_sub_type.OperationSubType"]
    """<p>The subtype of the event, providing additional categorization.</p>"""
    event_id: "capo_lambda.types.event_id.EventId"
    """<p>The unique identifier for this event. Event IDs increment sequentially.</p>"""
    id: NotRequired["capo_lambda.types.operation_id.OperationId"]
    """<p>The unique identifier for this operation.</p>"""
    name: NotRequired["capo_lambda.types.operation_name.OperationName"]
    """<p>The customer-provided name for this operation.</p>"""
    event_timestamp: NotRequired[
        "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>The date and time when this event occurred, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    parent_id: NotRequired["capo_lambda.types.operation_id.OperationId"]
    """<p>The unique identifier of the parent operation, if this operation is running within a child context.</p>"""
    execution_started_details: NotRequired[
        "capo_lambda.types.execution_started_details.ExecutionStartedDetails"
    ]
    """<p>Details about an execution that started.</p>"""
    execution_succeeded_details: NotRequired[
        "capo_lambda.types.execution_succeeded_details.ExecutionSucceededDetails"
    ]
    """<p>Details about an execution that succeeded.</p>"""
    execution_failed_details: NotRequired[
        "capo_lambda.types.execution_failed_details.ExecutionFailedDetails"
    ]
    """<p>Details about an execution that failed.</p>"""
    execution_timed_out_details: NotRequired[
        "capo_lambda.types.execution_timed_out_details.ExecutionTimedOutDetails"
    ]
    """<p>Details about an execution that timed out.</p>"""
    execution_stopped_details: NotRequired[
        "capo_lambda.types.execution_stopped_details.ExecutionStoppedDetails"
    ]
    """<p>Details about an execution that was stopped.</p>"""
    context_started_details: NotRequired[
        "capo_lambda.types.context_started_details.ContextStartedDetails"
    ]
    """<p>Details about a context that started.</p>"""
    context_succeeded_details: NotRequired[
        "capo_lambda.types.context_succeeded_details.ContextSucceededDetails"
    ]
    """<p>Details about a context that succeeded.</p>"""
    context_failed_details: NotRequired[
        "capo_lambda.types.context_failed_details.ContextFailedDetails"
    ]
    """<p>Details about a context that failed.</p>"""
    wait_started_details: NotRequired[
        "capo_lambda.types.wait_started_details.WaitStartedDetails"
    ]
    """<p>Details about a wait operation that started.</p>"""
    wait_succeeded_details: NotRequired[
        "capo_lambda.types.wait_succeeded_details.WaitSucceededDetails"
    ]
    """<p>Details about a wait operation that succeeded.</p>"""
    wait_cancelled_details: NotRequired[
        "capo_lambda.types.wait_cancelled_details.WaitCancelledDetails"
    ]
    """<p>Details about a wait operation that was cancelled.</p>"""
    step_started_details: NotRequired[
        "capo_lambda.types.step_started_details.StepStartedDetails"
    ]
    """<p>Details about a step that started.</p>"""
    step_succeeded_details: NotRequired[
        "capo_lambda.types.step_succeeded_details.StepSucceededDetails"
    ]
    """<p>Details about a step that succeeded.</p>"""
    step_failed_details: NotRequired[
        "capo_lambda.types.step_failed_details.StepFailedDetails"
    ]
    """<p>Details about a step that failed.</p>"""
    chained_invoke_started_details: NotRequired[
        "capo_lambda.types.chained_invoke_started_details.ChainedInvokeStartedDetails"
    ]
    chained_invoke_succeeded_details: NotRequired[
        "capo_lambda.types.chained_invoke_succeeded_details.ChainedInvokeSucceededDetails"
    ]
    """<p>Details about a chained invocation that succeeded.</p>"""
    chained_invoke_failed_details: NotRequired[
        "capo_lambda.types.chained_invoke_failed_details.ChainedInvokeFailedDetails"
    ]
    chained_invoke_timed_out_details: NotRequired[
        "capo_lambda.types.chained_invoke_timed_out_details.ChainedInvokeTimedOutDetails"
    ]
    """<p>Details about a chained invocation that timed out.</p>"""
    chained_invoke_stopped_details: NotRequired[
        "capo_lambda.types.chained_invoke_stopped_details.ChainedInvokeStoppedDetails"
    ]
    """<p>Details about a chained invocation that was stopped.</p>"""
    callback_started_details: NotRequired[
        "capo_lambda.types.callback_started_details.CallbackStartedDetails"
    ]
    callback_succeeded_details: NotRequired[
        "capo_lambda.types.callback_succeeded_details.CallbackSucceededDetails"
    ]
    callback_failed_details: NotRequired[
        "capo_lambda.types.callback_failed_details.CallbackFailedDetails"
    ]
    callback_timed_out_details: NotRequired[
        "capo_lambda.types.callback_timed_out_details.CallbackTimedOutDetails"
    ]
    invocation_completed_details: NotRequired[
        "capo_lambda.types.invocation_completed_details.InvocationCompletedDetails"
    ]
    """<p>Details about a function invocation that completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> dict:
    out: dict = {}
    if "event_type" in value:
        import capo_lambda.types.event_type

        out["EventType"] = capo_lambda.types.event_type.serialize_json(
            value["event_type"]
        )
    if "sub_type" in value:
        out["SubType"] = value["sub_type"]
    out["EventId"] = value.get("event_id", 1)
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_timestamp" in value:
        import capo_lambda.types.execution_timestamp

        out["EventTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
            value["event_timestamp"]
        )
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    if "execution_started_details" in value:
        import capo_lambda.types.execution_started_details

        out["ExecutionStartedDetails"] = (
            capo_lambda.types.execution_started_details.serialize_json(
                value["execution_started_details"]
            )
        )
    if "execution_succeeded_details" in value:
        import capo_lambda.types.execution_succeeded_details

        out["ExecutionSucceededDetails"] = (
            capo_lambda.types.execution_succeeded_details.serialize_json(
                value["execution_succeeded_details"]
            )
        )
    if "execution_failed_details" in value:
        import capo_lambda.types.execution_failed_details

        out["ExecutionFailedDetails"] = (
            capo_lambda.types.execution_failed_details.serialize_json(
                value["execution_failed_details"]
            )
        )
    if "execution_timed_out_details" in value:
        import capo_lambda.types.execution_timed_out_details

        out["ExecutionTimedOutDetails"] = (
            capo_lambda.types.execution_timed_out_details.serialize_json(
                value["execution_timed_out_details"]
            )
        )
    if "execution_stopped_details" in value:
        import capo_lambda.types.execution_stopped_details

        out["ExecutionStoppedDetails"] = (
            capo_lambda.types.execution_stopped_details.serialize_json(
                value["execution_stopped_details"]
            )
        )
    if "context_started_details" in value:
        import capo_lambda.types.context_started_details

        out["ContextStartedDetails"] = (
            capo_lambda.types.context_started_details.serialize_json(
                value["context_started_details"]
            )
        )
    if "context_succeeded_details" in value:
        import capo_lambda.types.context_succeeded_details

        out["ContextSucceededDetails"] = (
            capo_lambda.types.context_succeeded_details.serialize_json(
                value["context_succeeded_details"]
            )
        )
    if "context_failed_details" in value:
        import capo_lambda.types.context_failed_details

        out["ContextFailedDetails"] = (
            capo_lambda.types.context_failed_details.serialize_json(
                value["context_failed_details"]
            )
        )
    if "wait_started_details" in value:
        import capo_lambda.types.wait_started_details

        out["WaitStartedDetails"] = (
            capo_lambda.types.wait_started_details.serialize_json(
                value["wait_started_details"]
            )
        )
    if "wait_succeeded_details" in value:
        import capo_lambda.types.wait_succeeded_details

        out["WaitSucceededDetails"] = (
            capo_lambda.types.wait_succeeded_details.serialize_json(
                value["wait_succeeded_details"]
            )
        )
    if "wait_cancelled_details" in value:
        import capo_lambda.types.wait_cancelled_details

        out["WaitCancelledDetails"] = (
            capo_lambda.types.wait_cancelled_details.serialize_json(
                value["wait_cancelled_details"]
            )
        )
    if "step_started_details" in value:
        import capo_lambda.types.step_started_details

        out["StepStartedDetails"] = (
            capo_lambda.types.step_started_details.serialize_json(
                value["step_started_details"]
            )
        )
    if "step_succeeded_details" in value:
        import capo_lambda.types.step_succeeded_details

        out["StepSucceededDetails"] = (
            capo_lambda.types.step_succeeded_details.serialize_json(
                value["step_succeeded_details"]
            )
        )
    if "step_failed_details" in value:
        import capo_lambda.types.step_failed_details

        out["StepFailedDetails"] = capo_lambda.types.step_failed_details.serialize_json(
            value["step_failed_details"]
        )
    if "chained_invoke_started_details" in value:
        import capo_lambda.types.chained_invoke_started_details

        out["ChainedInvokeStartedDetails"] = (
            capo_lambda.types.chained_invoke_started_details.serialize_json(
                value["chained_invoke_started_details"]
            )
        )
    if "chained_invoke_succeeded_details" in value:
        import capo_lambda.types.chained_invoke_succeeded_details

        out["ChainedInvokeSucceededDetails"] = (
            capo_lambda.types.chained_invoke_succeeded_details.serialize_json(
                value["chained_invoke_succeeded_details"]
            )
        )
    if "chained_invoke_failed_details" in value:
        import capo_lambda.types.chained_invoke_failed_details

        out["ChainedInvokeFailedDetails"] = (
            capo_lambda.types.chained_invoke_failed_details.serialize_json(
                value["chained_invoke_failed_details"]
            )
        )
    if "chained_invoke_timed_out_details" in value:
        import capo_lambda.types.chained_invoke_timed_out_details

        out["ChainedInvokeTimedOutDetails"] = (
            capo_lambda.types.chained_invoke_timed_out_details.serialize_json(
                value["chained_invoke_timed_out_details"]
            )
        )
    if "chained_invoke_stopped_details" in value:
        import capo_lambda.types.chained_invoke_stopped_details

        out["ChainedInvokeStoppedDetails"] = (
            capo_lambda.types.chained_invoke_stopped_details.serialize_json(
                value["chained_invoke_stopped_details"]
            )
        )
    if "callback_started_details" in value:
        import capo_lambda.types.callback_started_details

        out["CallbackStartedDetails"] = (
            capo_lambda.types.callback_started_details.serialize_json(
                value["callback_started_details"]
            )
        )
    if "callback_succeeded_details" in value:
        import capo_lambda.types.callback_succeeded_details

        out["CallbackSucceededDetails"] = (
            capo_lambda.types.callback_succeeded_details.serialize_json(
                value["callback_succeeded_details"]
            )
        )
    if "callback_failed_details" in value:
        import capo_lambda.types.callback_failed_details

        out["CallbackFailedDetails"] = (
            capo_lambda.types.callback_failed_details.serialize_json(
                value["callback_failed_details"]
            )
        )
    if "callback_timed_out_details" in value:
        import capo_lambda.types.callback_timed_out_details

        out["CallbackTimedOutDetails"] = (
            capo_lambda.types.callback_timed_out_details.serialize_json(
                value["callback_timed_out_details"]
            )
        )
    if "invocation_completed_details" in value:
        import capo_lambda.types.invocation_completed_details

        out["InvocationCompletedDetails"] = (
            capo_lambda.types.invocation_completed_details.serialize_json(
                value["invocation_completed_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if data.get("EventType") is not None:
        import capo_lambda.types.event_type

        out["event_type"] = capo_lambda.types.event_type.deserialize_json(
            data["EventType"]
        )
    if data.get("SubType") is not None:
        out["sub_type"] = data["SubType"]
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    else:
        out["event_id"] = 1
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["event_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["EventTimestamp"]
        )
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    if data.get("ExecutionStartedDetails") is not None:
        import capo_lambda.types.execution_started_details

        out["execution_started_details"] = (
            capo_lambda.types.execution_started_details.deserialize_json(
                data["ExecutionStartedDetails"]
            )
        )
    if data.get("ExecutionSucceededDetails") is not None:
        import capo_lambda.types.execution_succeeded_details

        out["execution_succeeded_details"] = (
            capo_lambda.types.execution_succeeded_details.deserialize_json(
                data["ExecutionSucceededDetails"]
            )
        )
    if data.get("ExecutionFailedDetails") is not None:
        import capo_lambda.types.execution_failed_details

        out["execution_failed_details"] = (
            capo_lambda.types.execution_failed_details.deserialize_json(
                data["ExecutionFailedDetails"]
            )
        )
    if data.get("ExecutionTimedOutDetails") is not None:
        import capo_lambda.types.execution_timed_out_details

        out["execution_timed_out_details"] = (
            capo_lambda.types.execution_timed_out_details.deserialize_json(
                data["ExecutionTimedOutDetails"]
            )
        )
    if data.get("ExecutionStoppedDetails") is not None:
        import capo_lambda.types.execution_stopped_details

        out["execution_stopped_details"] = (
            capo_lambda.types.execution_stopped_details.deserialize_json(
                data["ExecutionStoppedDetails"]
            )
        )
    if data.get("ContextStartedDetails") is not None:
        import capo_lambda.types.context_started_details

        out["context_started_details"] = (
            capo_lambda.types.context_started_details.deserialize_json(
                data["ContextStartedDetails"]
            )
        )
    if data.get("ContextSucceededDetails") is not None:
        import capo_lambda.types.context_succeeded_details

        out["context_succeeded_details"] = (
            capo_lambda.types.context_succeeded_details.deserialize_json(
                data["ContextSucceededDetails"]
            )
        )
    if data.get("ContextFailedDetails") is not None:
        import capo_lambda.types.context_failed_details

        out["context_failed_details"] = (
            capo_lambda.types.context_failed_details.deserialize_json(
                data["ContextFailedDetails"]
            )
        )
    if data.get("WaitStartedDetails") is not None:
        import capo_lambda.types.wait_started_details

        out["wait_started_details"] = (
            capo_lambda.types.wait_started_details.deserialize_json(
                data["WaitStartedDetails"]
            )
        )
    if data.get("WaitSucceededDetails") is not None:
        import capo_lambda.types.wait_succeeded_details

        out["wait_succeeded_details"] = (
            capo_lambda.types.wait_succeeded_details.deserialize_json(
                data["WaitSucceededDetails"]
            )
        )
    if data.get("WaitCancelledDetails") is not None:
        import capo_lambda.types.wait_cancelled_details

        out["wait_cancelled_details"] = (
            capo_lambda.types.wait_cancelled_details.deserialize_json(
                data["WaitCancelledDetails"]
            )
        )
    if data.get("StepStartedDetails") is not None:
        import capo_lambda.types.step_started_details

        out["step_started_details"] = (
            capo_lambda.types.step_started_details.deserialize_json(
                data["StepStartedDetails"]
            )
        )
    if data.get("StepSucceededDetails") is not None:
        import capo_lambda.types.step_succeeded_details

        out["step_succeeded_details"] = (
            capo_lambda.types.step_succeeded_details.deserialize_json(
                data["StepSucceededDetails"]
            )
        )
    if data.get("StepFailedDetails") is not None:
        import capo_lambda.types.step_failed_details

        out["step_failed_details"] = (
            capo_lambda.types.step_failed_details.deserialize_json(
                data["StepFailedDetails"]
            )
        )
    if data.get("ChainedInvokeStartedDetails") is not None:
        import capo_lambda.types.chained_invoke_started_details

        out["chained_invoke_started_details"] = (
            capo_lambda.types.chained_invoke_started_details.deserialize_json(
                data["ChainedInvokeStartedDetails"]
            )
        )
    if data.get("ChainedInvokeSucceededDetails") is not None:
        import capo_lambda.types.chained_invoke_succeeded_details

        out["chained_invoke_succeeded_details"] = (
            capo_lambda.types.chained_invoke_succeeded_details.deserialize_json(
                data["ChainedInvokeSucceededDetails"]
            )
        )
    if data.get("ChainedInvokeFailedDetails") is not None:
        import capo_lambda.types.chained_invoke_failed_details

        out["chained_invoke_failed_details"] = (
            capo_lambda.types.chained_invoke_failed_details.deserialize_json(
                data["ChainedInvokeFailedDetails"]
            )
        )
    if data.get("ChainedInvokeTimedOutDetails") is not None:
        import capo_lambda.types.chained_invoke_timed_out_details

        out["chained_invoke_timed_out_details"] = (
            capo_lambda.types.chained_invoke_timed_out_details.deserialize_json(
                data["ChainedInvokeTimedOutDetails"]
            )
        )
    if data.get("ChainedInvokeStoppedDetails") is not None:
        import capo_lambda.types.chained_invoke_stopped_details

        out["chained_invoke_stopped_details"] = (
            capo_lambda.types.chained_invoke_stopped_details.deserialize_json(
                data["ChainedInvokeStoppedDetails"]
            )
        )
    if data.get("CallbackStartedDetails") is not None:
        import capo_lambda.types.callback_started_details

        out["callback_started_details"] = (
            capo_lambda.types.callback_started_details.deserialize_json(
                data["CallbackStartedDetails"]
            )
        )
    if data.get("CallbackSucceededDetails") is not None:
        import capo_lambda.types.callback_succeeded_details

        out["callback_succeeded_details"] = (
            capo_lambda.types.callback_succeeded_details.deserialize_json(
                data["CallbackSucceededDetails"]
            )
        )
    if data.get("CallbackFailedDetails") is not None:
        import capo_lambda.types.callback_failed_details

        out["callback_failed_details"] = (
            capo_lambda.types.callback_failed_details.deserialize_json(
                data["CallbackFailedDetails"]
            )
        )
    if data.get("CallbackTimedOutDetails") is not None:
        import capo_lambda.types.callback_timed_out_details

        out["callback_timed_out_details"] = (
            capo_lambda.types.callback_timed_out_details.deserialize_json(
                data["CallbackTimedOutDetails"]
            )
        )
    if data.get("InvocationCompletedDetails") is not None:
        import capo_lambda.types.invocation_completed_details

        out["invocation_completed_details"] = (
            capo_lambda.types.invocation_completed_details.deserialize_json(
                data["InvocationCompletedDetails"]
            )
        )
    return out
