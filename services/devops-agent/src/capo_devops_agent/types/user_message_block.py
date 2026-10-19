"""Generated from Smithy shape ``com.amazonaws.devopsagent#UserMessageBlock``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember


class _UserMessageBlock_text(TypedDict, closed=True):
    text: "str"


class _UserMessageBlock_toolResult(TypedDict, closed=True):
    toolResult: "object"


UserMessageBlock: TypeAlias = (
    _UserMessageBlock_text | _UserMessageBlock_toolResult | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UserMessageBlock) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"UserMessageBlock: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "toolResult" in value:
        return {"toolResult": value["toolResult"]}
    else:
        raise SerializationError("UserMessageBlock: no variant present")


def deserialize_json(data: dict) -> UserMessageBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("toolResult") is not None:
        return {"toolResult": data["toolResult"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("UserMessageBlock: no recognized variant key")
