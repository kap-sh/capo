"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockDelta``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.citations_delta
    import capo_bedrock_runtime.types.image_block_delta
    import capo_bedrock_runtime.types.reasoning_content_block_delta
    import capo_bedrock_runtime.types.tool_result_blocks_delta
    import capo_bedrock_runtime.types.tool_use_block_delta


class ContentBlockDeltaTextMember(TypedDict, closed=True):
    text: "str"


class ContentBlockDeltaToolUseMember(TypedDict, closed=True):
    toolUse: "capo_bedrock_runtime.types.tool_use_block_delta.ToolUseBlockDelta"


class ContentBlockDeltaToolResultMember(TypedDict, closed=True):
    toolResult: (
        "capo_bedrock_runtime.types.tool_result_blocks_delta.ToolResultBlocksDelta"
    )


class ContentBlockDeltaReasoningContentMember(TypedDict, closed=True):
    reasoningContent: "capo_bedrock_runtime.types.reasoning_content_block_delta.ReasoningContentBlockDelta"


class ContentBlockDeltaCitationMember(TypedDict, closed=True):
    citation: "capo_bedrock_runtime.types.citations_delta.CitationsDelta"


class ContentBlockDeltaImageMember(TypedDict, closed=True):
    image: "capo_bedrock_runtime.types.image_block_delta.ImageBlockDelta"


ContentBlockDelta: TypeAlias = (
    ContentBlockDeltaTextMember
    | ContentBlockDeltaToolUseMember
    | ContentBlockDeltaToolResultMember
    | ContentBlockDeltaReasoningContentMember
    | ContentBlockDeltaCitationMember
    | ContentBlockDeltaImageMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockDelta) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ContentBlockDelta: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "toolUse" in value:
        import capo_bedrock_runtime.types.tool_use_block_delta

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block_delta.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_runtime.types.tool_result_blocks_delta

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_blocks_delta.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoningContent" in value:
        import capo_bedrock_runtime.types.reasoning_content_block_delta

        return {
            "reasoningContent": capo_bedrock_runtime.types.reasoning_content_block_delta.serialize_json(
                value["reasoningContent"]
            )
        }
    elif "citation" in value:
        import capo_bedrock_runtime.types.citations_delta

        return {
            "citation": capo_bedrock_runtime.types.citations_delta.serialize_json(
                value["citation"]
            )
        }
    elif "image" in value:
        import capo_bedrock_runtime.types.image_block_delta

        return {
            "image": capo_bedrock_runtime.types.image_block_delta.serialize_json(
                value["image"]
            )
        }
    else:
        raise SerializationError("ContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> ContentBlockDelta:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("toolUse") is not None:
        import capo_bedrock_runtime.types.tool_use_block_delta

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block_delta.deserialize_json(
                data["toolUse"]
            )
        }
    elif data.get("toolResult") is not None:
        import capo_bedrock_runtime.types.tool_result_blocks_delta

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_blocks_delta.deserialize_json(
                data["toolResult"]
            )
        }
    elif data.get("reasoningContent") is not None:
        import capo_bedrock_runtime.types.reasoning_content_block_delta

        return {
            "reasoningContent": capo_bedrock_runtime.types.reasoning_content_block_delta.deserialize_json(
                data["reasoningContent"]
            )
        }
    elif data.get("citation") is not None:
        import capo_bedrock_runtime.types.citations_delta

        return {
            "citation": capo_bedrock_runtime.types.citations_delta.deserialize_json(
                data["citation"]
            )
        }
    elif data.get("image") is not None:
        import capo_bedrock_runtime.types.image_block_delta

        return {
            "image": capo_bedrock_runtime.types.image_block_delta.deserialize_json(
                data["image"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ContentBlockDelta: no recognized variant key")


def redact_sensitive(value: ContentBlockDelta) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "reasoningContent" in value:
        out["reasoningContent"] = "*** Sensitive Data Redacted ***"
    if "image" in value:
        import capo_bedrock_runtime.types.image_block_delta

        out["image"] = capo_bedrock_runtime.types.image_block_delta.redact_sensitive(
            value["image"]
        )
    return out
