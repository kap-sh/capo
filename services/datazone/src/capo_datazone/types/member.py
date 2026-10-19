"""Generated from Smithy shape ``com.amazonaws.datazone#Member``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember


class _Member_userIdentifier(TypedDict, closed=True):
    userIdentifier: "str"


class _Member_groupIdentifier(TypedDict, closed=True):
    groupIdentifier: "str"


Member: TypeAlias = (
    _Member_userIdentifier | _Member_groupIdentifier | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Member: cannot serialize unknown variant {value.name!r}"
        )
    elif "userIdentifier" in value:
        return {"userIdentifier": value["userIdentifier"]}
    elif "groupIdentifier" in value:
        return {"groupIdentifier": value["groupIdentifier"]}
    else:
        raise SerializationError("Member: no variant present")


def deserialize_json(data: dict) -> Member:
    if data.get("userIdentifier") is not None:
        return {"userIdentifier": data["userIdentifier"]}
    elif data.get("groupIdentifier") is not None:
        return {"groupIdentifier": data["groupIdentifier"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Member: no recognized variant key")
