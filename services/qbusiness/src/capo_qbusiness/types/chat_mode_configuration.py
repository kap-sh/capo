"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatModeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.plugin_configuration


class ChatModeConfigurationPluginConfigurationMember(TypedDict, closed=True):
    pluginConfiguration: "capo_qbusiness.types.plugin_configuration.PluginConfiguration"


ChatModeConfiguration: TypeAlias = (
    ChatModeConfigurationPluginConfigurationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ChatModeConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ChatModeConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "pluginConfiguration" in value:
        import capo_qbusiness.types.plugin_configuration

        return {
            "pluginConfiguration": capo_qbusiness.types.plugin_configuration.serialize_json(
                value["pluginConfiguration"]
            )
        }
    else:
        raise SerializationError("ChatModeConfiguration: no variant present")


def deserialize_json(data: dict) -> ChatModeConfiguration:
    if data.get("pluginConfiguration") is not None:
        import capo_qbusiness.types.plugin_configuration

        return {
            "pluginConfiguration": capo_qbusiness.types.plugin_configuration.deserialize_json(
                data["pluginConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ChatModeConfiguration: no recognized variant key")
