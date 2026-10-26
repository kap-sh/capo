"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessReasoningContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_reasoning_text_block


class _HarnessReasoningContentBlock_reasoningText(TypedDict, closed=True):
    reasoningText: "capo_bedrock_agentcore.types.harness_reasoning_text_block.HarnessReasoningTextBlock"


class _HarnessReasoningContentBlock_redactedContent(TypedDict, closed=True):
    redactedContent: "bytes"


HarnessReasoningContentBlock: TypeAlias = (
    _HarnessReasoningContentBlock_reasoningText
    | _HarnessReasoningContentBlock_redactedContent
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessReasoningContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessReasoningContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "reasoningText" in value:
        import capo_bedrock_agentcore.types.harness_reasoning_text_block

        return {
            "reasoningText": capo_bedrock_agentcore.types.harness_reasoning_text_block.serialize_json(
                value["reasoningText"]
            )
        }
    elif "redactedContent" in value:
        import capo_bedrock_agentcore.types._prelude.blob

        return {
            "redactedContent": capo_bedrock_agentcore.types._prelude.blob.serialize_json(
                value["redactedContent"]
            )
        }
    else:
        raise SerializationError("HarnessReasoningContentBlock: no variant present")


def deserialize_json(data: dict) -> HarnessReasoningContentBlock:
    if data.get("reasoningText") is not None:
        import capo_bedrock_agentcore.types.harness_reasoning_text_block

        return {
            "reasoningText": capo_bedrock_agentcore.types.harness_reasoning_text_block.deserialize_json(
                data["reasoningText"]
            )
        }
    elif data.get("redactedContent") is not None:
        import capo_bedrock_agentcore.types._prelude.blob

        return {
            "redactedContent": capo_bedrock_agentcore.types._prelude.blob.deserialize_json(
                data["redactedContent"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "HarnessReasoningContentBlock: no recognized variant key"
        )
