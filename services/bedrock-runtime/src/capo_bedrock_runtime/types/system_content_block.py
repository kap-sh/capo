"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SystemContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.cache_point_block
    import capo_bedrock_runtime.types.guardrail_converse_content_block
    import capo_bedrock_runtime.types.non_empty_string


class _SystemContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_runtime.types.non_empty_string.NonEmptyString"


class _SystemContentBlock_guardContent(TypedDict, closed=True):
    guardContent: "capo_bedrock_runtime.types.guardrail_converse_content_block.GuardrailConverseContentBlock"


class _SystemContentBlock_cachePoint(TypedDict, closed=True):
    cachePoint: "capo_bedrock_runtime.types.cache_point_block.CachePointBlock"


SystemContentBlock: TypeAlias = (
    _SystemContentBlock_text
    | _SystemContentBlock_guardContent
    | _SystemContentBlock_cachePoint
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SystemContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SystemContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
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
    else:
        raise SerializationError("SystemContentBlock: no variant present")


def deserialize_json(data: dict) -> SystemContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
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
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SystemContentBlock: no recognized variant key")


def redact_sensitive(value: SystemContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "guardContent" in value:
        import capo_bedrock_runtime.types.guardrail_converse_content_block

        out["guardContent"] = (
            capo_bedrock_runtime.types.guardrail_converse_content_block.redact_sensitive(
                value["guardContent"]
            )
        )
    return out
