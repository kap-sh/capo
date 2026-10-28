"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockDelta``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_reasoning_content_block_delta
    import capo_bedrock_agentcore.types.harness_tool_result_blocks_delta
    import capo_bedrock_agentcore.types.harness_tool_result_metadata_block_delta
    import capo_bedrock_agentcore.types.harness_tool_use_block_delta
    import capo_bedrock_agentcore.types.sensitive_text


class HarnessContentBlockDeltaTextMember(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_text.SensitiveText"


class HarnessContentBlockDeltaToolUseMember(TypedDict, closed=True):
    toolUse: "capo_bedrock_agentcore.types.harness_tool_use_block_delta.HarnessToolUseBlockDelta"


class HarnessContentBlockDeltaToolResultMember(TypedDict, closed=True):
    toolResult: "capo_bedrock_agentcore.types.harness_tool_result_blocks_delta.HarnessToolResultBlocksDelta"


class HarnessContentBlockDeltaReasoningContentMember(TypedDict, closed=True):
    reasoningContent: "capo_bedrock_agentcore.types.harness_reasoning_content_block_delta.HarnessReasoningContentBlockDelta"


class HarnessContentBlockDeltaToolResultMetadataMember(TypedDict, closed=True):
    toolResultMetadata: "capo_bedrock_agentcore.types.harness_tool_result_metadata_block_delta.HarnessToolResultMetadataBlockDelta"


HarnessContentBlockDelta: TypeAlias = (
    HarnessContentBlockDeltaTextMember
    | HarnessContentBlockDeltaToolUseMember
    | HarnessContentBlockDeltaToolResultMember
    | HarnessContentBlockDeltaReasoningContentMember
    | HarnessContentBlockDeltaToolResultMetadataMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlockDelta) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessContentBlockDelta: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "toolUse" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_block_delta

        return {
            "toolUse": capo_bedrock_agentcore.types.harness_tool_use_block_delta.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_blocks_delta

        return {
            "toolResult": capo_bedrock_agentcore.types.harness_tool_result_blocks_delta.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoningContent" in value:
        import capo_bedrock_agentcore.types.harness_reasoning_content_block_delta

        return {
            "reasoningContent": capo_bedrock_agentcore.types.harness_reasoning_content_block_delta.serialize_json(
                value["reasoningContent"]
            )
        }
    elif "toolResultMetadata" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_metadata_block_delta

        return {
            "toolResultMetadata": capo_bedrock_agentcore.types.harness_tool_result_metadata_block_delta.serialize_json(
                value["toolResultMetadata"]
            )
        }
    else:
        raise SerializationError("HarnessContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> HarnessContentBlockDelta:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("toolUse") is not None:
        import capo_bedrock_agentcore.types.harness_tool_use_block_delta

        return {
            "toolUse": capo_bedrock_agentcore.types.harness_tool_use_block_delta.deserialize_json(
                data["toolUse"]
            )
        }
    elif data.get("toolResult") is not None:
        import capo_bedrock_agentcore.types.harness_tool_result_blocks_delta

        return {
            "toolResult": capo_bedrock_agentcore.types.harness_tool_result_blocks_delta.deserialize_json(
                data["toolResult"]
            )
        }
    elif data.get("reasoningContent") is not None:
        import capo_bedrock_agentcore.types.harness_reasoning_content_block_delta

        return {
            "reasoningContent": capo_bedrock_agentcore.types.harness_reasoning_content_block_delta.deserialize_json(
                data["reasoningContent"]
            )
        }
    elif data.get("toolResultMetadata") is not None:
        import capo_bedrock_agentcore.types.harness_tool_result_metadata_block_delta

        return {
            "toolResultMetadata": capo_bedrock_agentcore.types.harness_tool_result_metadata_block_delta.deserialize_json(
                data["toolResultMetadata"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "HarnessContentBlockDelta: no recognized variant key"
        )


def redact_sensitive(value: HarnessContentBlockDelta) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "toolUse" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_block_delta

        out["toolUse"] = (
            capo_bedrock_agentcore.types.harness_tool_use_block_delta.redact_sensitive(
                value["toolUse"]
            )
        )
    if "toolResult" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_blocks_delta

        out["toolResult"] = (
            capo_bedrock_agentcore.types.harness_tool_result_blocks_delta.redact_sensitive(
                value["toolResult"]
            )
        )
    if "reasoningContent" in value:
        out["reasoningContent"] = "*** Sensitive Data Redacted ***"
    if "toolResultMetadata" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_metadata_block_delta

        out["toolResultMetadata"] = (
            capo_bedrock_agentcore.types.harness_tool_result_metadata_block_delta.redact_sensitive(
                value["toolResultMetadata"]
            )
        )
    return out
