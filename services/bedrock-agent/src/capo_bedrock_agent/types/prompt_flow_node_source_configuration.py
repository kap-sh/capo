"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptFlowNodeSourceConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_flow_node_inline_configuration
    import capo_bedrock_agent.types.prompt_flow_node_resource_configuration


class _PromptFlowNodeSourceConfiguration_resource(TypedDict, closed=True):
    resource: "capo_bedrock_agent.types.prompt_flow_node_resource_configuration.PromptFlowNodeResourceConfiguration"


class _PromptFlowNodeSourceConfiguration_inline(TypedDict, closed=True):
    inline: "capo_bedrock_agent.types.prompt_flow_node_inline_configuration.PromptFlowNodeInlineConfiguration"


PromptFlowNodeSourceConfiguration: TypeAlias = (
    _PromptFlowNodeSourceConfiguration_resource
    | _PromptFlowNodeSourceConfiguration_inline
)


# --- restJson1 ser/de ---
def serialize_json(value: PromptFlowNodeSourceConfiguration) -> dict:
    if "resource" in value:
        import capo_bedrock_agent.types.prompt_flow_node_resource_configuration

        return {
            "resource": capo_bedrock_agent.types.prompt_flow_node_resource_configuration.serialize_json(
                value["resource"]
            )
        }
    elif "inline" in value:
        import capo_bedrock_agent.types.prompt_flow_node_inline_configuration

        return {
            "inline": capo_bedrock_agent.types.prompt_flow_node_inline_configuration.serialize_json(
                value["inline"]
            )
        }
    else:
        raise SerializationError(
            "PromptFlowNodeSourceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> PromptFlowNodeSourceConfiguration:
    if data.get("resource") is not None:
        import capo_bedrock_agent.types.prompt_flow_node_resource_configuration

        return {
            "resource": capo_bedrock_agent.types.prompt_flow_node_resource_configuration.deserialize_json(
                data["resource"]
            )
        }
    elif data.get("inline") is not None:
        import capo_bedrock_agent.types.prompt_flow_node_inline_configuration

        return {
            "inline": capo_bedrock_agent.types.prompt_flow_node_inline_configuration.deserialize_json(
                data["inline"]
            )
        }
    else:
        raise DeserializationError(
            "PromptFlowNodeSourceConfiguration: no recognized variant key"
        )


def redact_sensitive(value: PromptFlowNodeSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inline" in value:
        import capo_bedrock_agent.types.prompt_flow_node_inline_configuration

        out["inline"] = (
            capo_bedrock_agent.types.prompt_flow_node_inline_configuration.redact_sensitive(
                value["inline"]
            )
        )
    return out
