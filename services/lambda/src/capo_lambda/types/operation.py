"""Generated from Smithy shape ``com.amazonaws.lambda#Operation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.callback_details
    import capo_lambda.types.chained_invoke_details
    import capo_lambda.types.context_details
    import capo_lambda.types.execution_details
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.operation_id
    import capo_lambda.types.operation_name
    import capo_lambda.types.operation_status
    import capo_lambda.types.operation_sub_type
    import capo_lambda.types.operation_type
    import capo_lambda.types.step_details
    import capo_lambda.types.wait_details


class Operation(TypedDict, closed=True):
    id: "capo_lambda.types.operation_id.OperationId"
    """<p>The unique identifier for this operation.</p>"""
    parent_id: NotRequired["capo_lambda.types.operation_id.OperationId"]
    """<p>The unique identifier of the parent operation, if this operation is running within a child context.</p>"""
    name: NotRequired["capo_lambda.types.operation_name.OperationName"]
    """<p>The customer-provided name for this operation.</p>"""
    type: "capo_lambda.types.operation_type.OperationType"
    """<p>The type of operation.</p>"""
    sub_type: NotRequired["capo_lambda.types.operation_sub_type.OperationSubType"]
    """<p>The subtype of the operation, providing additional categorization.</p>"""
    start_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when the operation started, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    end_timestamp: NotRequired[
        "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>The date and time when the operation ended, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    status: "capo_lambda.types.operation_status.OperationStatus"
    """<p>The current status of the operation.</p>"""
    execution_details: NotRequired[
        "capo_lambda.types.execution_details.ExecutionDetails"
    ]
    """<p>Details about the execution, if this operation represents an execution.</p>"""
    context_details: NotRequired["capo_lambda.types.context_details.ContextDetails"]
    """<p>Details about the context, if this operation represents a context.</p>"""
    step_details: NotRequired["capo_lambda.types.step_details.StepDetails"]
    """<p>Details about the step, if this operation represents a step.</p>"""
    wait_details: NotRequired["capo_lambda.types.wait_details.WaitDetails"]
    """<p>Details about the wait operation, if this operation represents a wait.</p>"""
    callback_details: NotRequired["capo_lambda.types.callback_details.CallbackDetails"]
    chained_invoke_details: NotRequired[
        "capo_lambda.types.chained_invoke_details.ChainedInvokeDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Operation) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_lambda.types.operation_type

    out["Type"] = capo_lambda.types.operation_type.serialize_json(value["type"])
    if "sub_type" in value:
        out["SubType"] = value["sub_type"]
    import capo_lambda.types.execution_timestamp

    out["StartTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["start_timestamp"]
    )
    if "end_timestamp" in value:
        import capo_lambda.types.execution_timestamp

        out["EndTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
            value["end_timestamp"]
        )
    import capo_lambda.types.operation_status

    out["Status"] = capo_lambda.types.operation_status.serialize_json(value["status"])
    if "execution_details" in value:
        import capo_lambda.types.execution_details

        out["ExecutionDetails"] = capo_lambda.types.execution_details.serialize_json(
            value["execution_details"]
        )
    if "context_details" in value:
        import capo_lambda.types.context_details

        out["ContextDetails"] = capo_lambda.types.context_details.serialize_json(
            value["context_details"]
        )
    if "step_details" in value:
        import capo_lambda.types.step_details

        out["StepDetails"] = capo_lambda.types.step_details.serialize_json(
            value["step_details"]
        )
    if "wait_details" in value:
        import capo_lambda.types.wait_details

        out["WaitDetails"] = capo_lambda.types.wait_details.serialize_json(
            value["wait_details"]
        )
    if "callback_details" in value:
        import capo_lambda.types.callback_details

        out["CallbackDetails"] = capo_lambda.types.callback_details.serialize_json(
            value["callback_details"]
        )
    if "chained_invoke_details" in value:
        import capo_lambda.types.chained_invoke_details

        out["ChainedInvokeDetails"] = (
            capo_lambda.types.chained_invoke_details.serialize_json(
                value["chained_invoke_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Operation:
    out: Operation = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Operation.id required")
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_lambda.types.operation_type

        out["type"] = capo_lambda.types.operation_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("Operation.type required")
    if data.get("SubType") is not None:
        out["sub_type"] = data["SubType"]
    if data.get("StartTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["start_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["StartTimestamp"]
        )
    else:
        raise DeserializationError("Operation.start_timestamp required")
    if data.get("EndTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["end_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["EndTimestamp"]
        )
    if data.get("Status") is not None:
        import capo_lambda.types.operation_status

        out["status"] = capo_lambda.types.operation_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("Operation.status required")
    if data.get("ExecutionDetails") is not None:
        import capo_lambda.types.execution_details

        out["execution_details"] = capo_lambda.types.execution_details.deserialize_json(
            data["ExecutionDetails"]
        )
    if data.get("ContextDetails") is not None:
        import capo_lambda.types.context_details

        out["context_details"] = capo_lambda.types.context_details.deserialize_json(
            data["ContextDetails"]
        )
    if data.get("StepDetails") is not None:
        import capo_lambda.types.step_details

        out["step_details"] = capo_lambda.types.step_details.deserialize_json(
            data["StepDetails"]
        )
    if data.get("WaitDetails") is not None:
        import capo_lambda.types.wait_details

        out["wait_details"] = capo_lambda.types.wait_details.deserialize_json(
            data["WaitDetails"]
        )
    if data.get("CallbackDetails") is not None:
        import capo_lambda.types.callback_details

        out["callback_details"] = capo_lambda.types.callback_details.deserialize_json(
            data["CallbackDetails"]
        )
    if data.get("ChainedInvokeDetails") is not None:
        import capo_lambda.types.chained_invoke_details

        out["chained_invoke_details"] = (
            capo_lambda.types.chained_invoke_details.deserialize_json(
                data["ChainedInvokeDetails"]
            )
        )
    return out
