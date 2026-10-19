"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ReasoningContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.reasoning_text_block


class _ReasoningContentBlock_reasoningText(TypedDict, closed=True):
    reasoningText: (
        "capo_bedrock_agent_runtime.types.reasoning_text_block.ReasoningTextBlock"
    )


class _ReasoningContentBlock_redactedContent(TypedDict, closed=True):
    redactedContent: "bytes"


ReasoningContentBlock: TypeAlias = (
    _ReasoningContentBlock_reasoningText
    | _ReasoningContentBlock_redactedContent
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ReasoningContentBlock) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ReasoningContentBlock: cannot serialize unknown variant {value.name!r}"
        )
    elif "reasoningText" in value:
        import capo_bedrock_agent_runtime.types.reasoning_text_block

        return {
            "reasoningText": capo_bedrock_agent_runtime.types.reasoning_text_block.serialize_json(
                value["reasoningText"]
            )
        }
    elif "redactedContent" in value:
        import capo_bedrock_agent_runtime.types._prelude.blob

        return {
            "redactedContent": capo_bedrock_agent_runtime.types._prelude.blob.serialize_json(
                value["redactedContent"]
            )
        }
    else:
        raise SerializationError("ReasoningContentBlock: no variant present")


def deserialize_json(data: dict) -> ReasoningContentBlock:
    if data.get("reasoningText") is not None:
        import capo_bedrock_agent_runtime.types.reasoning_text_block

        return {
            "reasoningText": capo_bedrock_agent_runtime.types.reasoning_text_block.deserialize_json(
                data["reasoningText"]
            )
        }
    elif data.get("redactedContent") is not None:
        import capo_bedrock_agent_runtime.types._prelude.blob

        return {
            "redactedContent": capo_bedrock_agent_runtime.types._prelude.blob.deserialize_json(
                data["redactedContent"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ReasoningContentBlock: no recognized variant key")
