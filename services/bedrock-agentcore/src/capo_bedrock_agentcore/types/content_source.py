"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ContentSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.inline_memory_content


class _ContentSource_inline(TypedDict, closed=True):
    inline: "capo_bedrock_agentcore.types.inline_memory_content.InlineMemoryContent"


ContentSource: TypeAlias = _ContentSource_inline | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ContentSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ContentSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "inline" in value:
        import capo_bedrock_agentcore.types.inline_memory_content

        return {
            "inline": capo_bedrock_agentcore.types.inline_memory_content.serialize_json(
                value["inline"]
            )
        }
    else:
        raise SerializationError("ContentSource: no variant present")


def deserialize_json(data: dict) -> ContentSource:
    if data.get("inline") is not None:
        import capo_bedrock_agentcore.types.inline_memory_content

        return {
            "inline": capo_bedrock_agentcore.types.inline_memory_content.deserialize_json(
                data["inline"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ContentSource: no recognized variant key")


def redact_sensitive(value: ContentSource) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "inline" in value:
        import capo_bedrock_agentcore.types.inline_memory_content

        out["inline"] = (
            capo_bedrock_agentcore.types.inline_memory_content.redact_sensitive(
                value["inline"]
            )
        )
    return out
