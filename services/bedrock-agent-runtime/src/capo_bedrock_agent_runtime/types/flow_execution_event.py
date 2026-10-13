"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionEvent``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.condition_result_event
    import capo_bedrock_agent_runtime.types.flow_execution_input_event
    import capo_bedrock_agent_runtime.types.flow_execution_output_event
    import capo_bedrock_agent_runtime.types.flow_failure_event
    import capo_bedrock_agent_runtime.types.node_action_event
    import capo_bedrock_agent_runtime.types.node_dependency_event
    import capo_bedrock_agent_runtime.types.node_failure_event
    import capo_bedrock_agent_runtime.types.node_input_event
    import capo_bedrock_agent_runtime.types.node_output_event


class _FlowExecutionEvent_flowInputEvent(TypedDict, closed=True):
    flowInputEvent: "capo_bedrock_agent_runtime.types.flow_execution_input_event.FlowExecutionInputEvent"


class _FlowExecutionEvent_flowOutputEvent(TypedDict, closed=True):
    flowOutputEvent: "capo_bedrock_agent_runtime.types.flow_execution_output_event.FlowExecutionOutputEvent"


class _FlowExecutionEvent_nodeInputEvent(TypedDict, closed=True):
    nodeInputEvent: "capo_bedrock_agent_runtime.types.node_input_event.NodeInputEvent"


class _FlowExecutionEvent_nodeOutputEvent(TypedDict, closed=True):
    nodeOutputEvent: (
        "capo_bedrock_agent_runtime.types.node_output_event.NodeOutputEvent"
    )


class _FlowExecutionEvent_conditionResultEvent(TypedDict, closed=True):
    conditionResultEvent: (
        "capo_bedrock_agent_runtime.types.condition_result_event.ConditionResultEvent"
    )


class _FlowExecutionEvent_nodeFailureEvent(TypedDict, closed=True):
    nodeFailureEvent: (
        "capo_bedrock_agent_runtime.types.node_failure_event.NodeFailureEvent"
    )


class _FlowExecutionEvent_flowFailureEvent(TypedDict, closed=True):
    flowFailureEvent: (
        "capo_bedrock_agent_runtime.types.flow_failure_event.FlowFailureEvent"
    )


class _FlowExecutionEvent_nodeActionEvent(TypedDict, closed=True):
    nodeActionEvent: (
        "capo_bedrock_agent_runtime.types.node_action_event.NodeActionEvent"
    )


class _FlowExecutionEvent_nodeDependencyEvent(TypedDict, closed=True):
    nodeDependencyEvent: (
        "capo_bedrock_agent_runtime.types.node_dependency_event.NodeDependencyEvent"
    )


FlowExecutionEvent: TypeAlias = (
    _FlowExecutionEvent_flowInputEvent
    | _FlowExecutionEvent_flowOutputEvent
    | _FlowExecutionEvent_nodeInputEvent
    | _FlowExecutionEvent_nodeOutputEvent
    | _FlowExecutionEvent_conditionResultEvent
    | _FlowExecutionEvent_nodeFailureEvent
    | _FlowExecutionEvent_flowFailureEvent
    | _FlowExecutionEvent_nodeActionEvent
    | _FlowExecutionEvent_nodeDependencyEvent
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionEvent) -> dict:
    if "flowInputEvent" in value:
        import capo_bedrock_agent_runtime.types.flow_execution_input_event

        return {
            "flowInputEvent": capo_bedrock_agent_runtime.types.flow_execution_input_event.serialize_json(
                value["flowInputEvent"]
            )
        }
    elif "flowOutputEvent" in value:
        import capo_bedrock_agent_runtime.types.flow_execution_output_event

        return {
            "flowOutputEvent": capo_bedrock_agent_runtime.types.flow_execution_output_event.serialize_json(
                value["flowOutputEvent"]
            )
        }
    elif "nodeInputEvent" in value:
        import capo_bedrock_agent_runtime.types.node_input_event

        return {
            "nodeInputEvent": capo_bedrock_agent_runtime.types.node_input_event.serialize_json(
                value["nodeInputEvent"]
            )
        }
    elif "nodeOutputEvent" in value:
        import capo_bedrock_agent_runtime.types.node_output_event

        return {
            "nodeOutputEvent": capo_bedrock_agent_runtime.types.node_output_event.serialize_json(
                value["nodeOutputEvent"]
            )
        }
    elif "conditionResultEvent" in value:
        import capo_bedrock_agent_runtime.types.condition_result_event

        return {
            "conditionResultEvent": capo_bedrock_agent_runtime.types.condition_result_event.serialize_json(
                value["conditionResultEvent"]
            )
        }
    elif "nodeFailureEvent" in value:
        import capo_bedrock_agent_runtime.types.node_failure_event

        return {
            "nodeFailureEvent": capo_bedrock_agent_runtime.types.node_failure_event.serialize_json(
                value["nodeFailureEvent"]
            )
        }
    elif "flowFailureEvent" in value:
        import capo_bedrock_agent_runtime.types.flow_failure_event

        return {
            "flowFailureEvent": capo_bedrock_agent_runtime.types.flow_failure_event.serialize_json(
                value["flowFailureEvent"]
            )
        }
    elif "nodeActionEvent" in value:
        import capo_bedrock_agent_runtime.types.node_action_event

        return {
            "nodeActionEvent": capo_bedrock_agent_runtime.types.node_action_event.serialize_json(
                value["nodeActionEvent"]
            )
        }
    elif "nodeDependencyEvent" in value:
        import capo_bedrock_agent_runtime.types.node_dependency_event

        return {
            "nodeDependencyEvent": capo_bedrock_agent_runtime.types.node_dependency_event.serialize_json(
                value["nodeDependencyEvent"]
            )
        }
    else:
        raise SerializationError("FlowExecutionEvent: no variant present")


def deserialize_json(data: dict) -> FlowExecutionEvent:
    if data.get("flowInputEvent") is not None:
        import capo_bedrock_agent_runtime.types.flow_execution_input_event

        return {
            "flowInputEvent": capo_bedrock_agent_runtime.types.flow_execution_input_event.deserialize_json(
                data["flowInputEvent"]
            )
        }
    elif data.get("flowOutputEvent") is not None:
        import capo_bedrock_agent_runtime.types.flow_execution_output_event

        return {
            "flowOutputEvent": capo_bedrock_agent_runtime.types.flow_execution_output_event.deserialize_json(
                data["flowOutputEvent"]
            )
        }
    elif data.get("nodeInputEvent") is not None:
        import capo_bedrock_agent_runtime.types.node_input_event

        return {
            "nodeInputEvent": capo_bedrock_agent_runtime.types.node_input_event.deserialize_json(
                data["nodeInputEvent"]
            )
        }
    elif data.get("nodeOutputEvent") is not None:
        import capo_bedrock_agent_runtime.types.node_output_event

        return {
            "nodeOutputEvent": capo_bedrock_agent_runtime.types.node_output_event.deserialize_json(
                data["nodeOutputEvent"]
            )
        }
    elif data.get("conditionResultEvent") is not None:
        import capo_bedrock_agent_runtime.types.condition_result_event

        return {
            "conditionResultEvent": capo_bedrock_agent_runtime.types.condition_result_event.deserialize_json(
                data["conditionResultEvent"]
            )
        }
    elif data.get("nodeFailureEvent") is not None:
        import capo_bedrock_agent_runtime.types.node_failure_event

        return {
            "nodeFailureEvent": capo_bedrock_agent_runtime.types.node_failure_event.deserialize_json(
                data["nodeFailureEvent"]
            )
        }
    elif data.get("flowFailureEvent") is not None:
        import capo_bedrock_agent_runtime.types.flow_failure_event

        return {
            "flowFailureEvent": capo_bedrock_agent_runtime.types.flow_failure_event.deserialize_json(
                data["flowFailureEvent"]
            )
        }
    elif data.get("nodeActionEvent") is not None:
        import capo_bedrock_agent_runtime.types.node_action_event

        return {
            "nodeActionEvent": capo_bedrock_agent_runtime.types.node_action_event.deserialize_json(
                data["nodeActionEvent"]
            )
        }
    elif data.get("nodeDependencyEvent") is not None:
        import capo_bedrock_agent_runtime.types.node_dependency_event

        return {
            "nodeDependencyEvent": capo_bedrock_agent_runtime.types.node_dependency_event.deserialize_json(
                data["nodeDependencyEvent"]
            )
        }
    else:
        raise DeserializationError("FlowExecutionEvent: no recognized variant key")


def redact_sensitive(value: FlowExecutionEvent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flowInputEvent" in value:
        out["flowInputEvent"] = "*** Sensitive Data Redacted ***"
    if "flowOutputEvent" in value:
        out["flowOutputEvent"] = "*** Sensitive Data Redacted ***"
    if "nodeInputEvent" in value:
        out["nodeInputEvent"] = "*** Sensitive Data Redacted ***"
    if "nodeOutputEvent" in value:
        out["nodeOutputEvent"] = "*** Sensitive Data Redacted ***"
    if "conditionResultEvent" in value:
        out["conditionResultEvent"] = "*** Sensitive Data Redacted ***"
    if "nodeFailureEvent" in value:
        out["nodeFailureEvent"] = "*** Sensitive Data Redacted ***"
    if "flowFailureEvent" in value:
        out["flowFailureEvent"] = "*** Sensitive Data Redacted ***"
    if "nodeActionEvent" in value:
        out["nodeActionEvent"] = "*** Sensitive Data Redacted ***"
    if "nodeDependencyEvent" in value:
        out["nodeDependencyEvent"] = "*** Sensitive Data Redacted ***"
    return out
