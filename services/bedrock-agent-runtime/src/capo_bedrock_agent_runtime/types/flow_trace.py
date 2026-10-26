"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTrace``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_trace_condition_node_result_event
    import capo_bedrock_agent_runtime.types.flow_trace_dependency_event
    import capo_bedrock_agent_runtime.types.flow_trace_node_action_event
    import capo_bedrock_agent_runtime.types.flow_trace_node_input_event
    import capo_bedrock_agent_runtime.types.flow_trace_node_output_event


class _FlowTrace_nodeInputTrace(TypedDict, closed=True):
    nodeInputTrace: "capo_bedrock_agent_runtime.types.flow_trace_node_input_event.FlowTraceNodeInputEvent"


class _FlowTrace_nodeOutputTrace(TypedDict, closed=True):
    nodeOutputTrace: "capo_bedrock_agent_runtime.types.flow_trace_node_output_event.FlowTraceNodeOutputEvent"


class _FlowTrace_conditionNodeResultTrace(TypedDict, closed=True):
    conditionNodeResultTrace: "capo_bedrock_agent_runtime.types.flow_trace_condition_node_result_event.FlowTraceConditionNodeResultEvent"


class _FlowTrace_nodeActionTrace(TypedDict, closed=True):
    nodeActionTrace: "capo_bedrock_agent_runtime.types.flow_trace_node_action_event.FlowTraceNodeActionEvent"


class _FlowTrace_nodeDependencyTrace(TypedDict, closed=True):
    nodeDependencyTrace: "capo_bedrock_agent_runtime.types.flow_trace_dependency_event.FlowTraceDependencyEvent"


FlowTrace: TypeAlias = (
    _FlowTrace_nodeInputTrace
    | _FlowTrace_nodeOutputTrace
    | _FlowTrace_conditionNodeResultTrace
    | _FlowTrace_nodeActionTrace
    | _FlowTrace_nodeDependencyTrace
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowTrace) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FlowTrace: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "nodeInputTrace" in value:
        import capo_bedrock_agent_runtime.types.flow_trace_node_input_event

        return {
            "nodeInputTrace": capo_bedrock_agent_runtime.types.flow_trace_node_input_event.serialize_json(
                value["nodeInputTrace"]
            )
        }
    elif "nodeOutputTrace" in value:
        import capo_bedrock_agent_runtime.types.flow_trace_node_output_event

        return {
            "nodeOutputTrace": capo_bedrock_agent_runtime.types.flow_trace_node_output_event.serialize_json(
                value["nodeOutputTrace"]
            )
        }
    elif "conditionNodeResultTrace" in value:
        import capo_bedrock_agent_runtime.types.flow_trace_condition_node_result_event

        return {
            "conditionNodeResultTrace": capo_bedrock_agent_runtime.types.flow_trace_condition_node_result_event.serialize_json(
                value["conditionNodeResultTrace"]
            )
        }
    elif "nodeActionTrace" in value:
        import capo_bedrock_agent_runtime.types.flow_trace_node_action_event

        return {
            "nodeActionTrace": capo_bedrock_agent_runtime.types.flow_trace_node_action_event.serialize_json(
                value["nodeActionTrace"]
            )
        }
    elif "nodeDependencyTrace" in value:
        import capo_bedrock_agent_runtime.types.flow_trace_dependency_event

        return {
            "nodeDependencyTrace": capo_bedrock_agent_runtime.types.flow_trace_dependency_event.serialize_json(
                value["nodeDependencyTrace"]
            )
        }
    else:
        raise SerializationError("FlowTrace: no variant present")


def deserialize_json(data: dict) -> FlowTrace:
    if data.get("nodeInputTrace") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_input_event

        return {
            "nodeInputTrace": capo_bedrock_agent_runtime.types.flow_trace_node_input_event.deserialize_json(
                data["nodeInputTrace"]
            )
        }
    elif data.get("nodeOutputTrace") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_output_event

        return {
            "nodeOutputTrace": capo_bedrock_agent_runtime.types.flow_trace_node_output_event.deserialize_json(
                data["nodeOutputTrace"]
            )
        }
    elif data.get("conditionNodeResultTrace") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_condition_node_result_event

        return {
            "conditionNodeResultTrace": capo_bedrock_agent_runtime.types.flow_trace_condition_node_result_event.deserialize_json(
                data["conditionNodeResultTrace"]
            )
        }
    elif data.get("nodeActionTrace") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_node_action_event

        return {
            "nodeActionTrace": capo_bedrock_agent_runtime.types.flow_trace_node_action_event.deserialize_json(
                data["nodeActionTrace"]
            )
        }
    elif data.get("nodeDependencyTrace") is not None:
        import capo_bedrock_agent_runtime.types.flow_trace_dependency_event

        return {
            "nodeDependencyTrace": capo_bedrock_agent_runtime.types.flow_trace_dependency_event.deserialize_json(
                data["nodeDependencyTrace"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FlowTrace: no recognized variant key")
