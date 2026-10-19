"""Generated from Smithy shape ``com.amazonaws.novaact#CallResultContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError, SerializationError
from capo_nova_act.types._unknown import UnknownUnionMember


class _CallResultContent_text(TypedDict, closed=True):
    text: "str"


CallResultContent: TypeAlias = _CallResultContent_text | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: CallResultContent) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CallResultContent: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("CallResultContent: no variant present")


def deserialize_json(data: dict) -> CallResultContent:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CallResultContent: no recognized variant key")
