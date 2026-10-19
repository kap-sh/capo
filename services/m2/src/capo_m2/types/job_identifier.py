"""Generated from Smithy shape ``com.amazonaws.m2#JobIdentifier``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember


class _JobIdentifier_fileName(TypedDict, closed=True):
    fileName: "str"


class _JobIdentifier_scriptName(TypedDict, closed=True):
    scriptName: "str"


JobIdentifier: TypeAlias = (
    _JobIdentifier_fileName | _JobIdentifier_scriptName | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: JobIdentifier) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"JobIdentifier: cannot serialize unknown variant {value.name!r}"
        )
    elif "fileName" in value:
        return {"fileName": value["fileName"]}
    elif "scriptName" in value:
        return {"scriptName": value["scriptName"]}
    else:
        raise SerializationError("JobIdentifier: no variant present")


def deserialize_json(data: dict) -> JobIdentifier:
    if data.get("fileName") is not None:
        return {"fileName": data["fileName"]}
    elif data.get("scriptName") is not None:
        return {"scriptName": data["scriptName"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("JobIdentifier: no recognized variant key")
