"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ProgramNumberConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.passthrough


class ProgramNumberConfigurationPassthroughMember(TypedDict, closed=True):
    Passthrough: "capo_mediaconnect.types.passthrough.Passthrough"


class ProgramNumberConfigurationSetMember(TypedDict, closed=True):
    Set: "int"


ProgramNumberConfiguration: TypeAlias = (
    ProgramNumberConfigurationPassthroughMember
    | ProgramNumberConfigurationSetMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProgramNumberConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProgramNumberConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Passthrough" in value:
        import capo_mediaconnect.types.passthrough

        return {
            "passthrough": capo_mediaconnect.types.passthrough.serialize_json(
                value["Passthrough"]
            )
        }
    elif "Set" in value:
        return {"set": value["Set"]}
    else:
        raise SerializationError("ProgramNumberConfiguration: no variant present")


def deserialize_json(data: dict) -> ProgramNumberConfiguration:
    if data.get("passthrough") is not None:
        import capo_mediaconnect.types.passthrough

        return {
            "Passthrough": capo_mediaconnect.types.passthrough.deserialize_json(
                data["passthrough"]
            )
        }
    elif data.get("set") is not None:
        return {"Set": data["set"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ProgramNumberConfiguration: no recognized variant key"
        )
