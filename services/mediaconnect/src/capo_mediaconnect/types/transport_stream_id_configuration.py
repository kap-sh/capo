"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TransportStreamIdConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.passthrough


class TransportStreamIdConfigurationPassthroughMember(TypedDict, closed=True):
    Passthrough: "capo_mediaconnect.types.passthrough.Passthrough"


class TransportStreamIdConfigurationSetMember(TypedDict, closed=True):
    Set: "int"


TransportStreamIdConfiguration: TypeAlias = (
    TransportStreamIdConfigurationPassthroughMember
    | TransportStreamIdConfigurationSetMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TransportStreamIdConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TransportStreamIdConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
        raise SerializationError("TransportStreamIdConfiguration: no variant present")


def deserialize_json(data: dict) -> TransportStreamIdConfiguration:
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
            "TransportStreamIdConfiguration: no recognized variant key"
        )
