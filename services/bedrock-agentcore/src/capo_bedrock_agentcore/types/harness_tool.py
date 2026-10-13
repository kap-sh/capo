"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessTool``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_tool_configuration
    import capo_bedrock_agentcore.types.harness_tool_name
    import capo_bedrock_agentcore.types.harness_tool_type


class HarnessTool(TypedDict, closed=True):
    type: "capo_bedrock_agentcore.types.harness_tool_type.HarnessToolType"
    """<p>The type of tool.</p>"""
    name: NotRequired["capo_bedrock_agentcore.types.harness_tool_name.HarnessToolName"]
    """<p>Unique name for the tool. If not provided, a name will be inferred or generated.</p>"""
    config: NotRequired[
        "capo_bedrock_agentcore.types.harness_tool_configuration.HarnessToolConfiguration"
    ]
    """<p>Tool-specific configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTool) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.harness_tool_type

    out["type"] = capo_bedrock_agentcore.types.harness_tool_type.serialize_json(
        value["type"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "config" in value:
        import capo_bedrock_agentcore.types.harness_tool_configuration

        out["config"] = (
            capo_bedrock_agentcore.types.harness_tool_configuration.serialize_json(
                value["config"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessTool:
    out: HarnessTool = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agentcore.types.harness_tool_type

        out["type"] = capo_bedrock_agentcore.types.harness_tool_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("HarnessTool.type required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("config") is not None:
        import capo_bedrock_agentcore.types.harness_tool_configuration

        out["config"] = (
            capo_bedrock_agentcore.types.harness_tool_configuration.deserialize_json(
                data["config"]
            )
        )
    return out


def redact_sensitive(value: HarnessTool) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "config" in value:
        import capo_bedrock_agentcore.types.harness_tool_configuration

        out["config"] = (
            capo_bedrock_agentcore.types.harness_tool_configuration.redact_sensitive(
                value["config"]
            )
        )
    return out
