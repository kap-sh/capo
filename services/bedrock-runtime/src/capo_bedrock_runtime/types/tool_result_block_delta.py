"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultBlockDelta``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember


class _ToolResultBlockDelta_text(TypedDict, closed=True):
    text: "str"


class _ToolResultBlockDelta_json(TypedDict, closed=True):
    json: "object"


ToolResultBlockDelta: TypeAlias = (
    _ToolResultBlockDelta_text | _ToolResultBlockDelta_json | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultBlockDelta) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ToolResultBlockDelta: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("ToolResultBlockDelta: no variant present")


def deserialize_json(data: dict) -> ToolResultBlockDelta:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("json") is not None:
        return {"json": data["json"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ToolResultBlockDelta: no recognized variant key")
