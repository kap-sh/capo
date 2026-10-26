"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.cache_point_block


class _ContentBlock_text(TypedDict, closed=True):
    text: "str"


class _ContentBlock_cachePoint(TypedDict, closed=True):
    cachePoint: "capo_bedrock_agent.types.cache_point_block.CachePointBlock"


ContentBlock: TypeAlias = (
    _ContentBlock_text | _ContentBlock_cachePoint | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
        raise SerializationError("ContentBlock: no variant present")


def deserialize_json(data: dict) -> ContentBlock:
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("ContentBlock: no recognized variant key")
