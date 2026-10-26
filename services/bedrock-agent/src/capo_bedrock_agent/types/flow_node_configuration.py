"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_flow_node_configuration
    import capo_bedrock_agent.types.collector_flow_node_configuration
    import capo_bedrock_agent.types.condition_flow_node_configuration
    import capo_bedrock_agent.types.inline_code_flow_node_configuration
    import capo_bedrock_agent.types.input_flow_node_configuration
    import capo_bedrock_agent.types.iterator_flow_node_configuration
    import capo_bedrock_agent.types.knowledge_base_flow_node_configuration
    import capo_bedrock_agent.types.lambda_function_flow_node_configuration
    import capo_bedrock_agent.types.lex_flow_node_configuration
    import capo_bedrock_agent.types.loop_controller_flow_node_configuration
    import capo_bedrock_agent.types.loop_flow_node_configuration
    import capo_bedrock_agent.types.loop_input_flow_node_configuration
    import capo_bedrock_agent.types.output_flow_node_configuration
    import capo_bedrock_agent.types.prompt_flow_node_configuration
    import capo_bedrock_agent.types.retrieval_flow_node_configuration
    import capo_bedrock_agent.types.storage_flow_node_configuration


class _FlowNodeConfiguration_input(TypedDict, closed=True):
    input: "capo_bedrock_agent.types.input_flow_node_configuration.InputFlowNodeConfiguration"


class _FlowNodeConfiguration_output(TypedDict, closed=True):
    output: "capo_bedrock_agent.types.output_flow_node_configuration.OutputFlowNodeConfiguration"


class _FlowNodeConfiguration_knowledgeBase(TypedDict, closed=True):
    knowledgeBase: "capo_bedrock_agent.types.knowledge_base_flow_node_configuration.KnowledgeBaseFlowNodeConfiguration"


class _FlowNodeConfiguration_condition(TypedDict, closed=True):
    condition: "capo_bedrock_agent.types.condition_flow_node_configuration.ConditionFlowNodeConfiguration"


class _FlowNodeConfiguration_lex(TypedDict, closed=True):
    lex: "capo_bedrock_agent.types.lex_flow_node_configuration.LexFlowNodeConfiguration"


class _FlowNodeConfiguration_prompt(TypedDict, closed=True):
    prompt: "capo_bedrock_agent.types.prompt_flow_node_configuration.PromptFlowNodeConfiguration"


class _FlowNodeConfiguration_lambdaFunction(TypedDict, closed=True):
    lambdaFunction: "capo_bedrock_agent.types.lambda_function_flow_node_configuration.LambdaFunctionFlowNodeConfiguration"


class _FlowNodeConfiguration_storage(TypedDict, closed=True):
    storage: "capo_bedrock_agent.types.storage_flow_node_configuration.StorageFlowNodeConfiguration"


class _FlowNodeConfiguration_agent(TypedDict, closed=True):
    agent: "capo_bedrock_agent.types.agent_flow_node_configuration.AgentFlowNodeConfiguration"


class _FlowNodeConfiguration_retrieval(TypedDict, closed=True):
    retrieval: "capo_bedrock_agent.types.retrieval_flow_node_configuration.RetrievalFlowNodeConfiguration"


class _FlowNodeConfiguration_iterator(TypedDict, closed=True):
    iterator: "capo_bedrock_agent.types.iterator_flow_node_configuration.IteratorFlowNodeConfiguration"


class _FlowNodeConfiguration_collector(TypedDict, closed=True):
    collector: "capo_bedrock_agent.types.collector_flow_node_configuration.CollectorFlowNodeConfiguration"


class _FlowNodeConfiguration_inlineCode(TypedDict, closed=True):
    inlineCode: "capo_bedrock_agent.types.inline_code_flow_node_configuration.InlineCodeFlowNodeConfiguration"


class _FlowNodeConfiguration_loop(TypedDict, closed=True):
    loop: "capo_bedrock_agent.types.loop_flow_node_configuration.LoopFlowNodeConfiguration"


class _FlowNodeConfiguration_loopInput(TypedDict, closed=True):
    loopInput: "capo_bedrock_agent.types.loop_input_flow_node_configuration.LoopInputFlowNodeConfiguration"


class _FlowNodeConfiguration_loopController(TypedDict, closed=True):
    loopController: "capo_bedrock_agent.types.loop_controller_flow_node_configuration.LoopControllerFlowNodeConfiguration"


FlowNodeConfiguration: TypeAlias = (
    _FlowNodeConfiguration_input
    | _FlowNodeConfiguration_output
    | _FlowNodeConfiguration_knowledgeBase
    | _FlowNodeConfiguration_condition
    | _FlowNodeConfiguration_lex
    | _FlowNodeConfiguration_prompt
    | _FlowNodeConfiguration_lambdaFunction
    | _FlowNodeConfiguration_storage
    | _FlowNodeConfiguration_agent
    | _FlowNodeConfiguration_retrieval
    | _FlowNodeConfiguration_iterator
    | _FlowNodeConfiguration_collector
    | _FlowNodeConfiguration_inlineCode
    | _FlowNodeConfiguration_loop
    | _FlowNodeConfiguration_loopInput
    | _FlowNodeConfiguration_loopController
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FlowNodeConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "input" in value:
        import capo_bedrock_agent.types.input_flow_node_configuration

        return {
            "input": capo_bedrock_agent.types.input_flow_node_configuration.serialize_json(
                value["input"]
            )
        }
    elif "output" in value:
        import capo_bedrock_agent.types.output_flow_node_configuration

        return {
            "output": capo_bedrock_agent.types.output_flow_node_configuration.serialize_json(
                value["output"]
            )
        }
    elif "knowledgeBase" in value:
        import capo_bedrock_agent.types.knowledge_base_flow_node_configuration

        return {
            "knowledgeBase": capo_bedrock_agent.types.knowledge_base_flow_node_configuration.serialize_json(
                value["knowledgeBase"]
            )
        }
    elif "condition" in value:
        import capo_bedrock_agent.types.condition_flow_node_configuration

        return {
            "condition": capo_bedrock_agent.types.condition_flow_node_configuration.serialize_json(
                value["condition"]
            )
        }
    elif "lex" in value:
        import capo_bedrock_agent.types.lex_flow_node_configuration

        return {
            "lex": capo_bedrock_agent.types.lex_flow_node_configuration.serialize_json(
                value["lex"]
            )
        }
    elif "prompt" in value:
        import capo_bedrock_agent.types.prompt_flow_node_configuration

        return {
            "prompt": capo_bedrock_agent.types.prompt_flow_node_configuration.serialize_json(
                value["prompt"]
            )
        }
    elif "lambdaFunction" in value:
        import capo_bedrock_agent.types.lambda_function_flow_node_configuration

        return {
            "lambdaFunction": capo_bedrock_agent.types.lambda_function_flow_node_configuration.serialize_json(
                value["lambdaFunction"]
            )
        }
    elif "storage" in value:
        import capo_bedrock_agent.types.storage_flow_node_configuration

        return {
            "storage": capo_bedrock_agent.types.storage_flow_node_configuration.serialize_json(
                value["storage"]
            )
        }
    elif "agent" in value:
        import capo_bedrock_agent.types.agent_flow_node_configuration

        return {
            "agent": capo_bedrock_agent.types.agent_flow_node_configuration.serialize_json(
                value["agent"]
            )
        }
    elif "retrieval" in value:
        import capo_bedrock_agent.types.retrieval_flow_node_configuration

        return {
            "retrieval": capo_bedrock_agent.types.retrieval_flow_node_configuration.serialize_json(
                value["retrieval"]
            )
        }
    elif "iterator" in value:
        import capo_bedrock_agent.types.iterator_flow_node_configuration

        return {
            "iterator": capo_bedrock_agent.types.iterator_flow_node_configuration.serialize_json(
                value["iterator"]
            )
        }
    elif "collector" in value:
        import capo_bedrock_agent.types.collector_flow_node_configuration

        return {
            "collector": capo_bedrock_agent.types.collector_flow_node_configuration.serialize_json(
                value["collector"]
            )
        }
    elif "inlineCode" in value:
        import capo_bedrock_agent.types.inline_code_flow_node_configuration

        return {
            "inlineCode": capo_bedrock_agent.types.inline_code_flow_node_configuration.serialize_json(
                value["inlineCode"]
            )
        }
    elif "loop" in value:
        import capo_bedrock_agent.types.loop_flow_node_configuration

        return {
            "loop": capo_bedrock_agent.types.loop_flow_node_configuration.serialize_json(
                value["loop"]
            )
        }
    elif "loopInput" in value:
        import capo_bedrock_agent.types.loop_input_flow_node_configuration

        return {
            "loopInput": capo_bedrock_agent.types.loop_input_flow_node_configuration.serialize_json(
                value["loopInput"]
            )
        }
    elif "loopController" in value:
        import capo_bedrock_agent.types.loop_controller_flow_node_configuration

        return {
            "loopController": capo_bedrock_agent.types.loop_controller_flow_node_configuration.serialize_json(
                value["loopController"]
            )
        }
    else:
        raise SerializationError("FlowNodeConfiguration: no variant present")


def deserialize_json(data: dict) -> FlowNodeConfiguration:
    if data.get("input") is not None:
        import capo_bedrock_agent.types.input_flow_node_configuration

        return {
            "input": capo_bedrock_agent.types.input_flow_node_configuration.deserialize_json(
                data["input"]
            )
        }
    elif data.get("output") is not None:
        import capo_bedrock_agent.types.output_flow_node_configuration

        return {
            "output": capo_bedrock_agent.types.output_flow_node_configuration.deserialize_json(
                data["output"]
            )
        }
    elif data.get("knowledgeBase") is not None:
        import capo_bedrock_agent.types.knowledge_base_flow_node_configuration

        return {
            "knowledgeBase": capo_bedrock_agent.types.knowledge_base_flow_node_configuration.deserialize_json(
                data["knowledgeBase"]
            )
        }
    elif data.get("condition") is not None:
        import capo_bedrock_agent.types.condition_flow_node_configuration

        return {
            "condition": capo_bedrock_agent.types.condition_flow_node_configuration.deserialize_json(
                data["condition"]
            )
        }
    elif data.get("lex") is not None:
        import capo_bedrock_agent.types.lex_flow_node_configuration

        return {
            "lex": capo_bedrock_agent.types.lex_flow_node_configuration.deserialize_json(
                data["lex"]
            )
        }
    elif data.get("prompt") is not None:
        import capo_bedrock_agent.types.prompt_flow_node_configuration

        return {
            "prompt": capo_bedrock_agent.types.prompt_flow_node_configuration.deserialize_json(
                data["prompt"]
            )
        }
    elif data.get("lambdaFunction") is not None:
        import capo_bedrock_agent.types.lambda_function_flow_node_configuration

        return {
            "lambdaFunction": capo_bedrock_agent.types.lambda_function_flow_node_configuration.deserialize_json(
                data["lambdaFunction"]
            )
        }
    elif data.get("storage") is not None:
        import capo_bedrock_agent.types.storage_flow_node_configuration

        return {
            "storage": capo_bedrock_agent.types.storage_flow_node_configuration.deserialize_json(
                data["storage"]
            )
        }
    elif data.get("agent") is not None:
        import capo_bedrock_agent.types.agent_flow_node_configuration

        return {
            "agent": capo_bedrock_agent.types.agent_flow_node_configuration.deserialize_json(
                data["agent"]
            )
        }
    elif data.get("retrieval") is not None:
        import capo_bedrock_agent.types.retrieval_flow_node_configuration

        return {
            "retrieval": capo_bedrock_agent.types.retrieval_flow_node_configuration.deserialize_json(
                data["retrieval"]
            )
        }
    elif data.get("iterator") is not None:
        import capo_bedrock_agent.types.iterator_flow_node_configuration

        return {
            "iterator": capo_bedrock_agent.types.iterator_flow_node_configuration.deserialize_json(
                data["iterator"]
            )
        }
    elif data.get("collector") is not None:
        import capo_bedrock_agent.types.collector_flow_node_configuration

        return {
            "collector": capo_bedrock_agent.types.collector_flow_node_configuration.deserialize_json(
                data["collector"]
            )
        }
    elif data.get("inlineCode") is not None:
        import capo_bedrock_agent.types.inline_code_flow_node_configuration

        return {
            "inlineCode": capo_bedrock_agent.types.inline_code_flow_node_configuration.deserialize_json(
                data["inlineCode"]
            )
        }
    elif data.get("loop") is not None:
        import capo_bedrock_agent.types.loop_flow_node_configuration

        return {
            "loop": capo_bedrock_agent.types.loop_flow_node_configuration.deserialize_json(
                data["loop"]
            )
        }
    elif data.get("loopInput") is not None:
        import capo_bedrock_agent.types.loop_input_flow_node_configuration

        return {
            "loopInput": capo_bedrock_agent.types.loop_input_flow_node_configuration.deserialize_json(
                data["loopInput"]
            )
        }
    elif data.get("loopController") is not None:
        import capo_bedrock_agent.types.loop_controller_flow_node_configuration

        return {
            "loopController": capo_bedrock_agent.types.loop_controller_flow_node_configuration.deserialize_json(
                data["loopController"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FlowNodeConfiguration: no recognized variant key")


def redact_sensitive(value: FlowNodeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "knowledgeBase" in value:
        import capo_bedrock_agent.types.knowledge_base_flow_node_configuration

        out["knowledgeBase"] = (
            capo_bedrock_agent.types.knowledge_base_flow_node_configuration.redact_sensitive(
                value["knowledgeBase"]
            )
        )
    if "condition" in value:
        import capo_bedrock_agent.types.condition_flow_node_configuration

        out["condition"] = (
            capo_bedrock_agent.types.condition_flow_node_configuration.redact_sensitive(
                value["condition"]
            )
        )
    if "prompt" in value:
        import capo_bedrock_agent.types.prompt_flow_node_configuration

        out["prompt"] = (
            capo_bedrock_agent.types.prompt_flow_node_configuration.redact_sensitive(
                value["prompt"]
            )
        )
    if "inlineCode" in value:
        import capo_bedrock_agent.types.inline_code_flow_node_configuration

        out["inlineCode"] = (
            capo_bedrock_agent.types.inline_code_flow_node_configuration.redact_sensitive(
                value["inlineCode"]
            )
        )
    if "loop" in value:
        import capo_bedrock_agent.types.loop_flow_node_configuration

        out["loop"] = (
            capo_bedrock_agent.types.loop_flow_node_configuration.redact_sensitive(
                value["loop"]
            )
        )
    if "loopController" in value:
        import capo_bedrock_agent.types.loop_controller_flow_node_configuration

        out["loopController"] = (
            capo_bedrock_agent.types.loop_controller_flow_node_configuration.redact_sensitive(
                value["loopController"]
            )
        )
    return out
