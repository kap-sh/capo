"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.document_block
    import capo_bedrock_runtime.types.image_block
    import capo_bedrock_runtime.types.search_result_block
    import capo_bedrock_runtime.types.video_block


class ToolResultContentBlockJsonMember(TypedDict, closed=True):
    json: "object"


class ToolResultContentBlockTextMember(TypedDict, closed=True):
    text: "str"


class ToolResultContentBlockImageMember(TypedDict, closed=True):
    image: "capo_bedrock_runtime.types.image_block.ImageBlock"


class ToolResultContentBlockDocumentMember(TypedDict, closed=True):
    document: "capo_bedrock_runtime.types.document_block.DocumentBlock"


class ToolResultContentBlockVideoMember(TypedDict, closed=True):
    video: "capo_bedrock_runtime.types.video_block.VideoBlock"


class ToolResultContentBlockSearchResultMember(TypedDict, closed=True):
    searchResult: "capo_bedrock_runtime.types.search_result_block.SearchResultBlock"


ToolResultContentBlock: TypeAlias = (
    ToolResultContentBlockJsonMember
    | ToolResultContentBlockTextMember
    | ToolResultContentBlockImageMember
    | ToolResultContentBlockDocumentMember
    | ToolResultContentBlockVideoMember
    | ToolResultContentBlockSearchResultMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ToolResultContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "json" in value:
        return {"json": value["json"]}
    elif "text" in value:
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
    elif "searchResult" in value:
        import capo_bedrock_runtime.types.search_result_block

        return {
            "searchResult": capo_bedrock_runtime.types.search_result_block.serialize_json(
                value["searchResult"]
            )
        }
    else:
        raise SerializationError("ToolResultContentBlock: no variant present")


def deserialize_json(data: dict) -> ToolResultContentBlock:
    if data.get("json") is not None:
        return {"json": data["json"]}
    elif data.get("text") is not None:
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
    elif data.get("searchResult") is not None:
        import capo_bedrock_runtime.types.search_result_block

        return {
            "searchResult": capo_bedrock_runtime.types.search_result_block.deserialize_json(
                data["searchResult"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ToolResultContentBlock: no recognized variant key")


def redact_sensitive(value: ToolResultContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image" in value:
        import capo_bedrock_runtime.types.image_block

        out["image"] = capo_bedrock_runtime.types.image_block.redact_sensitive(
            value["image"]
        )
    return out
