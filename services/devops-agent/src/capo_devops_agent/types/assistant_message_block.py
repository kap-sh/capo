"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssistantMessageBlock``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember


class _AssistantMessageBlock_text(TypedDict, closed=True):
    text: "str"


class _AssistantMessageBlock_toolUse(TypedDict, closed=True):
    toolUse: "object"


AssistantMessageBlock: TypeAlias = (
    _AssistantMessageBlock_text | _AssistantMessageBlock_toolUse | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantMessageBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AssistantMessageBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "toolUse" in value:
        return {"toolUse": value["toolUse"]}
    else:
        raise SerializationError("AssistantMessageBlock: no variant present")


def deserialize_json(data: dict) -> AssistantMessageBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("toolUse") is not None:
        return {"toolUse": data["toolUse"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AssistantMessageBlock: no recognized variant key")
