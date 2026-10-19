"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionRecommendationConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_traces_config
    import capo_bedrock_agentcore.types.tool_description_source


class ToolDescriptionRecommendationConfig(TypedDict, closed=True):
    tool_description: (
        "capo_bedrock_agentcore.types.tool_description_source.ToolDescriptionSource"
    )
    """<p>The current tool descriptions to optimize.</p>"""
    agent_traces: "capo_bedrock_agentcore.types.agent_traces_config.AgentTracesConfig"
    """<p>The agent traces to analyze for generating tool description recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionRecommendationConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.tool_description_source

    out["toolDescription"] = (
        capo_bedrock_agentcore.types.tool_description_source.serialize_json(
            value["tool_description"]
        )
    )
    import capo_bedrock_agentcore.types.agent_traces_config

    out["agentTraces"] = (
        capo_bedrock_agentcore.types.agent_traces_config.serialize_json(
            value["agent_traces"]
        )
    )
    return out


def deserialize_json(data: dict) -> ToolDescriptionRecommendationConfig:
    out: ToolDescriptionRecommendationConfig = {}  # type: ignore[typeddict-item]
    if data.get("toolDescription") is not None:
        import capo_bedrock_agentcore.types.tool_description_source

        out["tool_description"] = (
            capo_bedrock_agentcore.types.tool_description_source.deserialize_json(
                data["toolDescription"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["tool_description"] = (
            capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
        )
    if data.get("agentTraces") is not None:
        import capo_bedrock_agentcore.types.agent_traces_config

        out["agent_traces"] = (
            capo_bedrock_agentcore.types.agent_traces_config.deserialize_json(
                data["agentTraces"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["agent_traces"] = capo_bedrock_agentcore.types._unknown.UnknownUnionMember(
            ""
        )
    return out


def redact_sensitive(value: ToolDescriptionRecommendationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tool_description" in value:
        import capo_bedrock_agentcore.types.tool_description_source

        out["tool_description"] = (
            capo_bedrock_agentcore.types.tool_description_source.redact_sensitive(
                value["tool_description"]
            )
        )
    if "agent_traces" in value:
        import capo_bedrock_agentcore.types.agent_traces_config

        out["agent_traces"] = (
            capo_bedrock_agentcore.types.agent_traces_config.redact_sensitive(
                value["agent_traces"]
            )
        )
    return out
