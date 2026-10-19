"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SystemContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.cache_point_block
    import capo_bedrock_agent.types.non_empty_string


class _SystemContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_agent.types.non_empty_string.NonEmptyString"


class _SystemContentBlock_cachePoint(TypedDict, closed=True):
    cachePoint: "capo_bedrock_agent.types.cache_point_block.CachePointBlock"


SystemContentBlock: TypeAlias = (
    _SystemContentBlock_text | _SystemContentBlock_cachePoint | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SystemContentBlock) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SystemContentBlock: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "cachePoint" in value:
        import capo_bedrock_agent.types.cache_point_block

        return {
            "cachePoint": capo_bedrock_agent.types.cache_point_block.serialize_json(
                value["cachePoint"]
            )
        }
    else:
        raise SerializationError("SystemContentBlock: no variant present")


def deserialize_json(data: dict) -> SystemContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("cachePoint") is not None:
        import capo_bedrock_agent.types.cache_point_block

        return {
            "cachePoint": capo_bedrock_agent.types.cache_point_block.deserialize_json(
                data["cachePoint"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SystemContentBlock: no recognized variant key")
