"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_reasoning_content_block
    import capo_bedrock_agentcore.types.harness_tool_result_block
    import capo_bedrock_agentcore.types.harness_tool_use_block
    import capo_bedrock_agentcore.types.sensitive_text


class _HarnessContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_text.SensitiveText"


class _HarnessContentBlock_toolUse(TypedDict, closed=True):
    toolUse: "capo_bedrock_agentcore.types.harness_tool_use_block.HarnessToolUseBlock"


class _HarnessContentBlock_toolResult(TypedDict, closed=True):
    toolResult: (
        "capo_bedrock_agentcore.types.harness_tool_result_block.HarnessToolResultBlock"
    )


class _HarnessContentBlock_reasoningContent(TypedDict, closed=True):
    reasoningContent: "capo_bedrock_agentcore.types.harness_reasoning_content_block.HarnessReasoningContentBlock"


HarnessContentBlock: TypeAlias = (
    _HarnessContentBlock_text
    | _HarnessContentBlock_toolUse
    | _HarnessContentBlock_toolResult
    | _HarnessContentBlock_reasoningContent
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "toolUse" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_block

        return {
            "toolUse": capo_bedrock_agentcore.types.harness_tool_use_block.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_block

        return {
            "toolResult": capo_bedrock_agentcore.types.harness_tool_result_block.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoningContent" in value:
        import capo_bedrock_agentcore.types.harness_reasoning_content_block

        return {
            "reasoningContent": capo_bedrock_agentcore.types.harness_reasoning_content_block.serialize_json(
                value["reasoningContent"]
            )
        }
    else:
        raise SerializationError("HarnessContentBlock: no variant present")


def deserialize_json(data: dict) -> HarnessContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("toolUse") is not None:
        import capo_bedrock_agentcore.types.harness_tool_use_block

        return {
            "toolUse": capo_bedrock_agentcore.types.harness_tool_use_block.deserialize_json(
                data["toolUse"]
            )
        }
    elif data.get("toolResult") is not None:
        import capo_bedrock_agentcore.types.harness_tool_result_block

        return {
            "toolResult": capo_bedrock_agentcore.types.harness_tool_result_block.deserialize_json(
                data["toolResult"]
            )
        }
    elif data.get("reasoningContent") is not None:
        import capo_bedrock_agentcore.types.harness_reasoning_content_block

        return {
            "reasoningContent": capo_bedrock_agentcore.types.harness_reasoning_content_block.deserialize_json(
                data["reasoningContent"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("HarnessContentBlock: no recognized variant key")


def redact_sensitive(value: HarnessContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "toolUse" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_block

        out["toolUse"] = (
            capo_bedrock_agentcore.types.harness_tool_use_block.redact_sensitive(
                value["toolUse"]
            )
        )
    if "toolResult" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_block

        out["toolResult"] = (
            capo_bedrock_agentcore.types.harness_tool_result_block.redact_sensitive(
                value["toolResult"]
            )
        )
    if "reasoningContent" in value:
        out["reasoningContent"] = "*** Sensitive Data Redacted ***"
    return out
