"""Generated from Smithy shape ``com.amazonaws.qconnect#Configuration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.connect_configuration


class _Configuration_connectConfiguration(TypedDict, closed=True):
    connectConfiguration: (
        "capo_qconnect.types.connect_configuration.ConnectConfiguration"
    )


Configuration: TypeAlias = _Configuration_connectConfiguration | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Configuration: cannot serialize unknown variant {value.name!r}"
        )
    elif "connectConfiguration" in value:
        import capo_qconnect.types.connect_configuration

        return {
            "connectConfiguration": capo_qconnect.types.connect_configuration.serialize_json(
                value["connectConfiguration"]
            )
        }
    else:
        raise SerializationError("Configuration: no variant present")


def deserialize_json(data: dict) -> Configuration:
    if data.get("connectConfiguration") is not None:
        import capo_qconnect.types.connect_configuration

        return {
            "connectConfiguration": capo_qconnect.types.connect_configuration.deserialize_json(
                data["connectConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Configuration: no recognized variant key")
