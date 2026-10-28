"""Generated from Smithy shape ``com.amazonaws.devopsagent#UserMessageBlock``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember


class UserMessageBlockTextMember(TypedDict, closed=True):
    text: "str"


class UserMessageBlockToolResultMember(TypedDict, closed=True):
    toolResult: "object"


UserMessageBlock: TypeAlias = (
    UserMessageBlockTextMember | UserMessageBlockToolResultMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UserMessageBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UserMessageBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("UserMessageBlock: no recognized variant key")
