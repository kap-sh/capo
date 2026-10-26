"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.guardrail_configuration
    import capo_bedrock_agent.types.prompt_flow_node_source_configuration


class PromptFlowNodeConfiguration(TypedDict, closed=True):
    source_configuration: "capo_bedrock_agent.types.prompt_flow_node_source_configuration.PromptFlowNodeSourceConfiguration"
    """<p>Specifies whether the prompt is from Prompt management or defined inline.</p>"""
    guardrail_configuration: NotRequired[
        "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Contains configurations for a guardrail to apply to the prompt in this node and the response generated from it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptFlowNodeConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.prompt_flow_node_source_configuration

    out["sourceConfiguration"] = (
        capo_bedrock_agent.types.prompt_flow_node_source_configuration.serialize_json(
            value["source_configuration"]
        )
    )
    if "guardrail_configuration" in value:
        import capo_bedrock_agent.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            capo_bedrock_agent.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PromptFlowNodeConfiguration:
    out: PromptFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceConfiguration") is not None:
        import capo_bedrock_agent.types.prompt_flow_node_source_configuration

        out["source_configuration"] = (
            capo_bedrock_agent.types.prompt_flow_node_source_configuration.deserialize_json(
                data["sourceConfiguration"]
            )
        )
    else:
        out["source_configuration"] = {"$unknown": {"name": ""}}
    if data.get("guardrailConfiguration") is not None:
        import capo_bedrock_agent.types.guardrail_configuration

        out["guardrail_configuration"] = (
            capo_bedrock_agent.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    return out


def redact_sensitive(value: PromptFlowNodeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_configuration" in value:
        import capo_bedrock_agent.types.prompt_flow_node_source_configuration

        out["source_configuration"] = (
            capo_bedrock_agent.types.prompt_flow_node_source_configuration.redact_sensitive(
                value["source_configuration"]
            )
        )
    return out
