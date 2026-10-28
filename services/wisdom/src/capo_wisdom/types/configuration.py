"""Generated from Smithy shape ``com.amazonaws.wisdom#Configuration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError
from capo_wisdom.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_wisdom.types.connect_configuration


class ConfigurationConnectConfigurationMember(TypedDict, closed=True):
    connectConfiguration: "capo_wisdom.types.connect_configuration.ConnectConfiguration"


Configuration: TypeAlias = ConfigurationConnectConfigurationMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Configuration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "connectConfiguration" in value:
        import capo_wisdom.types.connect_configuration

        return {
            "connectConfiguration": capo_wisdom.types.connect_configuration.serialize_json(
                value["connectConfiguration"]
            )
        }
    else:
        raise SerializationError("Configuration: no variant present")


def deserialize_json(data: dict) -> Configuration:
    if data.get("connectConfiguration") is not None:
        import capo_wisdom.types.connect_configuration

        return {
            "connectConfiguration": capo_wisdom.types.connect_configuration.deserialize_json(
                data["connectConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Configuration: no recognized variant key")
