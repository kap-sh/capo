"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ToolSchema``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.s3_configuration
    import capo_bedrock_agentcore_control.types.tool_definitions


class _ToolSchema_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore_control.types.s3_configuration.S3Configuration"


class _ToolSchema_inlinePayload(TypedDict, closed=True):
    inlinePayload: (
        "capo_bedrock_agentcore_control.types.tool_definitions.ToolDefinitions"
    )


ToolSchema: TypeAlias = _ToolSchema_s3 | _ToolSchema_inlinePayload


# --- restJson1 ser/de ---
def serialize_json(value: ToolSchema) -> dict:
    if "s3" in value:
        import capo_bedrock_agentcore_control.types.s3_configuration

        return {
            "s3": capo_bedrock_agentcore_control.types.s3_configuration.serialize_json(
                value["s3"]
            )
        }
    elif "inlinePayload" in value:
        import capo_bedrock_agentcore_control.types.tool_definitions

        return {
            "inlinePayload": capo_bedrock_agentcore_control.types.tool_definitions.serialize_json(
                value["inlinePayload"]
            )
        }
    else:
        raise SerializationError("ToolSchema: no variant present")


def deserialize_json(data: dict) -> ToolSchema:
    if data.get("s3") is not None:
        import capo_bedrock_agentcore_control.types.s3_configuration

        return {
            "s3": capo_bedrock_agentcore_control.types.s3_configuration.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("inlinePayload") is not None:
        import capo_bedrock_agentcore_control.types.tool_definitions

        return {
            "inlinePayload": capo_bedrock_agentcore_control.types.tool_definitions.deserialize_json(
                data["inlinePayload"]
            )
        }
    else:
        raise DeserializationError("ToolSchema: no recognized variant key")


def redact_sensitive(value: ToolSchema) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inlinePayload" in value:
        import capo_bedrock_agentcore_control.types.tool_definitions

        out["inlinePayload"] = (
            capo_bedrock_agentcore_control.types.tool_definitions.redact_sensitive(
                value["inlinePayload"]
            )
        )
    return out
