"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.audio_block
    import capo_bedrock_runtime.types.cache_point_block
    import capo_bedrock_runtime.types.citations_content_block
    import capo_bedrock_runtime.types.document_block
    import capo_bedrock_runtime.types.guardrail_converse_content_block
    import capo_bedrock_runtime.types.image_block
    import capo_bedrock_runtime.types.reasoning_content_block
    import capo_bedrock_runtime.types.search_result_block
    import capo_bedrock_runtime.types.tool_addition_block
    import capo_bedrock_runtime.types.tool_removal_block
    import capo_bedrock_runtime.types.tool_result_block
    import capo_bedrock_runtime.types.tool_use_block
    import capo_bedrock_runtime.types.video_block


class _ContentBlock_text(TypedDict, closed=True):
    text: "str"


class _ContentBlock_image(TypedDict, closed=True):
    image: "capo_bedrock_runtime.types.image_block.ImageBlock"


class _ContentBlock_document(TypedDict, closed=True):
    document: "capo_bedrock_runtime.types.document_block.DocumentBlock"


class _ContentBlock_video(TypedDict, closed=True):
    video: "capo_bedrock_runtime.types.video_block.VideoBlock"


class _ContentBlock_audio(TypedDict, closed=True):
    audio: "capo_bedrock_runtime.types.audio_block.AudioBlock"


class _ContentBlock_toolUse(TypedDict, closed=True):
    toolUse: "capo_bedrock_runtime.types.tool_use_block.ToolUseBlock"


class _ContentBlock_toolResult(TypedDict, closed=True):
    toolResult: "capo_bedrock_runtime.types.tool_result_block.ToolResultBlock"


class _ContentBlock_guardContent(TypedDict, closed=True):
    guardContent: "capo_bedrock_runtime.types.guardrail_converse_content_block.GuardrailConverseContentBlock"


class _ContentBlock_cachePoint(TypedDict, closed=True):
    cachePoint: "capo_bedrock_runtime.types.cache_point_block.CachePointBlock"


class _ContentBlock_reasoningContent(TypedDict, closed=True):
    reasoningContent: (
        "capo_bedrock_runtime.types.reasoning_content_block.ReasoningContentBlock"
    )


class _ContentBlock_citationsContent(TypedDict, closed=True):
    citationsContent: (
        "capo_bedrock_runtime.types.citations_content_block.CitationsContentBlock"
    )


class _ContentBlock_searchResult(TypedDict, closed=True):
    searchResult: "capo_bedrock_runtime.types.search_result_block.SearchResultBlock"


class _ContentBlock_toolAddition(TypedDict, closed=True):
    toolAddition: "capo_bedrock_runtime.types.tool_addition_block.ToolAdditionBlock"


class _ContentBlock_toolRemoval(TypedDict, closed=True):
    toolRemoval: "capo_bedrock_runtime.types.tool_removal_block.ToolRemovalBlock"


ContentBlock: TypeAlias = (
    _ContentBlock_text
    | _ContentBlock_image
    | _ContentBlock_document
    | _ContentBlock_video
    | _ContentBlock_audio
    | _ContentBlock_toolUse
    | _ContentBlock_toolResult
    | _ContentBlock_guardContent
    | _ContentBlock_cachePoint
    | _ContentBlock_reasoningContent
    | _ContentBlock_citationsContent
    | _ContentBlock_searchResult
    | _ContentBlock_toolAddition
    | _ContentBlock_toolRemoval
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "image" in value:
        import capo_bedrock_runtime.types.image_block

        return {
            "image": capo_bedrock_runtime.types.image_block.serialize_json(
                value["image"]
            )
        }
    elif "document" in value:
        import capo_bedrock_runtime.types.document_block

        return {
            "document": capo_bedrock_runtime.types.document_block.serialize_json(
                value["document"]
            )
        }
    elif "video" in value:
        import capo_bedrock_runtime.types.video_block

        return {
            "video": capo_bedrock_runtime.types.video_block.serialize_json(
                value["video"]
            )
        }
    elif "audio" in value:
        import capo_bedrock_runtime.types.audio_block

        return {
            "audio": capo_bedrock_runtime.types.audio_block.serialize_json(
                value["audio"]
            )
        }
    elif "toolUse" in value:
        import capo_bedrock_runtime.types.tool_use_block

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_runtime.types.tool_result_block

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_block.serialize_json(
                value["toolResult"]
            )
        }
    elif "guardContent" in value:
        import capo_bedrock_runtime.types.guardrail_converse_content_block

        return {
            "guardContent": capo_bedrock_runtime.types.guardrail_converse_content_block.serialize_json(
                value["guardContent"]
            )
        }
    elif "cachePoint" in value:
        import capo_bedrock_runtime.types.cache_point_block

        return {
            "cachePoint": capo_bedrock_runtime.types.cache_point_block.serialize_json(
                value["cachePoint"]
            )
        }
    elif "reasoningContent" in value:
        import capo_bedrock_runtime.types.reasoning_content_block

        return {
            "reasoningContent": capo_bedrock_runtime.types.reasoning_content_block.serialize_json(
                value["reasoningContent"]
            )
        }
    elif "citationsContent" in value:
        import capo_bedrock_runtime.types.citations_content_block

        return {
            "citationsContent": capo_bedrock_runtime.types.citations_content_block.serialize_json(
                value["citationsContent"]
            )
        }
    elif "searchResult" in value:
        import capo_bedrock_runtime.types.search_result_block

        return {
            "searchResult": capo_bedrock_runtime.types.search_result_block.serialize_json(
                value["searchResult"]
            )
        }
    elif "toolAddition" in value:
        import capo_bedrock_runtime.types.tool_addition_block

        return {
            "toolAddition": capo_bedrock_runtime.types.tool_addition_block.serialize_json(
                value["toolAddition"]
            )
        }
    elif "toolRemoval" in value:
        import capo_bedrock_runtime.types.tool_removal_block

        return {
            "toolRemoval": capo_bedrock_runtime.types.tool_removal_block.serialize_json(
                value["toolRemoval"]
            )
        }
    else:
        raise SerializationError("ContentBlock: no variant present")


def deserialize_json(data: dict) -> ContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("image") is not None:
        import capo_bedrock_runtime.types.image_block

        return {
            "image": capo_bedrock_runtime.types.image_block.deserialize_json(
                data["image"]
            )
        }
    elif data.get("document") is not None:
        import capo_bedrock_runtime.types.document_block

        return {
            "document": capo_bedrock_runtime.types.document_block.deserialize_json(
                data["document"]
            )
        }
    elif data.get("video") is not None:
        import capo_bedrock_runtime.types.video_block

        return {
            "video": capo_bedrock_runtime.types.video_block.deserialize_json(
                data["video"]
            )
        }
    elif data.get("audio") is not None:
        import capo_bedrock_runtime.types.audio_block

        return {
            "audio": capo_bedrock_runtime.types.audio_block.deserialize_json(
                data["audio"]
            )
        }
    elif data.get("toolUse") is not None:
        import capo_bedrock_runtime.types.tool_use_block

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block.deserialize_json(
                data["toolUse"]
            )
        }
    elif data.get("toolResult") is not None:
        import capo_bedrock_runtime.types.tool_result_block

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_block.deserialize_json(
                data["toolResult"]
            )
        }
    elif data.get("guardContent") is not None:
        import capo_bedrock_runtime.types.guardrail_converse_content_block

        return {
            "guardContent": capo_bedrock_runtime.types.guardrail_converse_content_block.deserialize_json(
                data["guardContent"]
            )
        }
    elif data.get("cachePoint") is not None:
        import capo_bedrock_runtime.types.cache_point_block

        return {
            "cachePoint": capo_bedrock_runtime.types.cache_point_block.deserialize_json(
                data["cachePoint"]
            )
        }
    elif data.get("reasoningContent") is not None:
        import capo_bedrock_runtime.types.reasoning_content_block

        return {
            "reasoningContent": capo_bedrock_runtime.types.reasoning_content_block.deserialize_json(
                data["reasoningContent"]
            )
        }
    elif data.get("citationsContent") is not None:
        import capo_bedrock_runtime.types.citations_content_block

        return {
            "citationsContent": capo_bedrock_runtime.types.citations_content_block.deserialize_json(
                data["citationsContent"]
            )
        }
    elif data.get("searchResult") is not None:
        import capo_bedrock_runtime.types.search_result_block

        return {
            "searchResult": capo_bedrock_runtime.types.search_result_block.deserialize_json(
                data["searchResult"]
            )
        }
    elif data.get("toolAddition") is not None:
        import capo_bedrock_runtime.types.tool_addition_block

        return {
            "toolAddition": capo_bedrock_runtime.types.tool_addition_block.deserialize_json(
                data["toolAddition"]
            )
        }
    elif data.get("toolRemoval") is not None:
        import capo_bedrock_runtime.types.tool_removal_block

        return {
            "toolRemoval": capo_bedrock_runtime.types.tool_removal_block.deserialize_json(
                data["toolRemoval"]
            )
        }
    else:
        raise DeserializationError("ContentBlock: no recognized variant key")


def redact_sensitive(value: ContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image" in value:
        import capo_bedrock_runtime.types.image_block

        out["image"] = capo_bedrock_runtime.types.image_block.redact_sensitive(
            value["image"]
        )
    if "audio" in value:
        import capo_bedrock_runtime.types.audio_block

        out["audio"] = capo_bedrock_runtime.types.audio_block.redact_sensitive(
            value["audio"]
        )
    if "toolResult" in value:
        import capo_bedrock_runtime.types.tool_result_block

        out["toolResult"] = (
            capo_bedrock_runtime.types.tool_result_block.redact_sensitive(
                value["toolResult"]
            )
        )
    if "guardContent" in value:
        import capo_bedrock_runtime.types.guardrail_converse_content_block

        out["guardContent"] = (
            capo_bedrock_runtime.types.guardrail_converse_content_block.redact_sensitive(
                value["guardContent"]
            )
        )
    if "reasoningContent" in value:
        out["reasoningContent"] = "*** Sensitive Data Redacted ***"
    return out
