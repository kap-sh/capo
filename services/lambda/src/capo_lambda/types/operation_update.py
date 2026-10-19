"""Generated from Smithy shape ``com.amazonaws.lambda#OperationUpdate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.callback_options
    import capo_lambda.types.chained_invoke_options
    import capo_lambda.types.context_options
    import capo_lambda.types.error_object
    import capo_lambda.types.operation_action
    import capo_lambda.types.operation_id
    import capo_lambda.types.operation_name
    import capo_lambda.types.operation_payload
    import capo_lambda.types.operation_sub_type
    import capo_lambda.types.operation_type
    import capo_lambda.types.step_options
    import capo_lambda.types.wait_options


class OperationUpdate(TypedDict, closed=True):
    id: "capo_lambda.types.operation_id.OperationId"
    """<p>The unique identifier for this operation.</p>"""
    parent_id: NotRequired["capo_lambda.types.operation_id.OperationId"]
    """<p>The unique identifier of the parent operation, if this operation is running within a child context.</p>"""
    name: NotRequired["capo_lambda.types.operation_name.OperationName"]
    """<p>The customer-provided name for this operation.</p>"""
    type: "capo_lambda.types.operation_type.OperationType"
    """<p>The type of operation to update.</p>"""
    sub_type: NotRequired["capo_lambda.types.operation_sub_type.OperationSubType"]
    """<p>The subtype of the operation, providing additional categorization.</p>"""
    action: "capo_lambda.types.operation_action.OperationAction"
    """<p>The action to take on the operation.</p>"""
    payload: NotRequired["capo_lambda.types.operation_payload.OperationPayload"]
    """<p>The payload for successful operations. The maximum payload size is 6 MB for synchronous <code>EXECUTION</code> operations (RequestResponse invocationType), 1 MB for asynchronous <code>EXECUTION</code> (Event invocationType) and <code>CHAINED_INVOKE</code> operations, and 256 KB for <code>CONTEXT</code>, <code>STEP</code>, <code>WAIT</code>, and <code>CALLBACK</code> operations.</p>"""
    error: NotRequired["capo_lambda.types.error_object.ErrorObject"]
    """<p>The error information for failed operations.</p>"""
    context_options: NotRequired["capo_lambda.types.context_options.ContextOptions"]
    """<p>Options for context operations.</p>"""
    step_options: NotRequired["capo_lambda.types.step_options.StepOptions"]
    """<p>Options for step operations.</p>"""
    wait_options: NotRequired["capo_lambda.types.wait_options.WaitOptions"]
    """<p>Options for wait operations.</p>"""
    callback_options: NotRequired["capo_lambda.types.callback_options.CallbackOptions"]
    chained_invoke_options: NotRequired[
        "capo_lambda.types.chained_invoke_options.ChainedInvokeOptions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OperationUpdate) -> dict:
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
    import capo_lambda.types.operation_action

    out["Action"] = capo_lambda.types.operation_action.serialize_json(value["action"])
    if "payload" in value:
        out["Payload"] = value["payload"]
    if "error" in value:
        import capo_lambda.types.error_object

        out["Error"] = capo_lambda.types.error_object.serialize_json(value["error"])
    if "context_options" in value:
        import capo_lambda.types.context_options

        out["ContextOptions"] = capo_lambda.types.context_options.serialize_json(
            value["context_options"]
        )
    if "step_options" in value:
        import capo_lambda.types.step_options

        out["StepOptions"] = capo_lambda.types.step_options.serialize_json(
            value["step_options"]
        )
    if "wait_options" in value:
        import capo_lambda.types.wait_options

        out["WaitOptions"] = capo_lambda.types.wait_options.serialize_json(
            value["wait_options"]
        )
    if "callback_options" in value:
        import capo_lambda.types.callback_options

        out["CallbackOptions"] = capo_lambda.types.callback_options.serialize_json(
            value["callback_options"]
        )
    if "chained_invoke_options" in value:
        import capo_lambda.types.chained_invoke_options

        out["ChainedInvokeOptions"] = (
            capo_lambda.types.chained_invoke_options.serialize_json(
                value["chained_invoke_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> OperationUpdate:
    out: OperationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("ParentId") is not None:
        out["parent_id"] = data["ParentId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_lambda.types.operation_type

        out["type"] = capo_lambda.types.operation_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_lambda.types.operation_type.OperationType", "")
    if data.get("SubType") is not None:
        out["sub_type"] = data["SubType"]
    if data.get("Action") is not None:
        import capo_lambda.types.operation_action

        out["action"] = capo_lambda.types.operation_action.deserialize_json(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_lambda.types.operation_action.OperationAction", ""
        )
    if data.get("Payload") is not None:
        out["payload"] = data["Payload"]
    if data.get("Error") is not None:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.deserialize_json(data["Error"])
    if data.get("ContextOptions") is not None:
        import capo_lambda.types.context_options

        out["context_options"] = capo_lambda.types.context_options.deserialize_json(
            data["ContextOptions"]
        )
    if data.get("StepOptions") is not None:
        import capo_lambda.types.step_options

        out["step_options"] = capo_lambda.types.step_options.deserialize_json(
            data["StepOptions"]
        )
    if data.get("WaitOptions") is not None:
        import capo_lambda.types.wait_options

        out["wait_options"] = capo_lambda.types.wait_options.deserialize_json(
            data["WaitOptions"]
        )
    if data.get("CallbackOptions") is not None:
        import capo_lambda.types.callback_options

        out["callback_options"] = capo_lambda.types.callback_options.deserialize_json(
            data["CallbackOptions"]
        )
    if data.get("ChainedInvokeOptions") is not None:
        import capo_lambda.types.chained_invoke_options

        out["chained_invoke_options"] = (
            capo_lambda.types.chained_invoke_options.deserialize_json(
                data["ChainedInvokeOptions"]
            )
        )
    return out


def redact_sensitive(value: OperationUpdate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        out["payload"] = "*** Sensitive Data Redacted ***"
    if "error" in value:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.redact_sensitive(value["error"])
    return out
