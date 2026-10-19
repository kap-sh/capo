"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockStart``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_tool_result_block_start
    import capo_bedrock_agentcore.types.harness_tool_use_block_start


class _HarnessContentBlockStart_toolUse(TypedDict, closed=True):
    toolUse: "capo_bedrock_agentcore.types.harness_tool_use_block_start.HarnessToolUseBlockStart"


class _HarnessContentBlockStart_toolResult(TypedDict, closed=True):
    toolResult: "capo_bedrock_agentcore.types.harness_tool_result_block_start.HarnessToolResultBlockStart"


HarnessContentBlockStart: TypeAlias = (
    _HarnessContentBlockStart_toolUse
    | _HarnessContentBlockStart_toolResult
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlockStart) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HarnessContentBlockStart: cannot serialize unknown variant {value.name!r}"
        )
    elif "toolUse" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_block_start

        return {
            "toolUse": capo_bedrock_agentcore.types.harness_tool_use_block_start.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_block_start

        return {
            "toolResult": capo_bedrock_agentcore.types.harness_tool_result_block_start.serialize_json(
                value["toolResult"]
            )
        }
    else:
        raise SerializationError("HarnessContentBlockStart: no variant present")


def deserialize_json(data: dict) -> HarnessContentBlockStart:
    if data.get("toolUse") is not None:
        import capo_bedrock_agentcore.types.harness_tool_use_block_start

        return {
            "toolUse": capo_bedrock_agentcore.types.harness_tool_use_block_start.deserialize_json(
                data["toolUse"]
            )
        }
    elif data.get("toolResult") is not None:
        import capo_bedrock_agentcore.types.harness_tool_result_block_start

        return {
            "toolResult": capo_bedrock_agentcore.types.harness_tool_result_block_start.deserialize_json(
                data["toolResult"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "HarnessContentBlockStart: no recognized variant key"
        )
