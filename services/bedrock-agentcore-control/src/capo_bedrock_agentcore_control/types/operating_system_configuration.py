"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OperatingSystemConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.linux_operating_system_configuration


class OperatingSystemConfigurationLinuxMember(TypedDict, closed=True):
    linux: "capo_bedrock_agentcore_control.types.linux_operating_system_configuration.LinuxOperatingSystemConfiguration"


OperatingSystemConfiguration: TypeAlias = (
    OperatingSystemConfigurationLinuxMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OperatingSystemConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OperatingSystemConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "linux" in value:
        import capo_bedrock_agentcore_control.types.linux_operating_system_configuration

        return {
            "linux": capo_bedrock_agentcore_control.types.linux_operating_system_configuration.serialize_json(
                value["linux"]
            )
        }
    else:
        raise SerializationError("OperatingSystemConfiguration: no variant present")


def deserialize_json(data: dict) -> OperatingSystemConfiguration:
    if data.get("linux") is not None:
        import capo_bedrock_agentcore_control.types.linux_operating_system_configuration

        return {
            "linux": capo_bedrock_agentcore_control.types.linux_operating_system_configuration.deserialize_json(
                data["linux"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "OperatingSystemConfiguration: no recognized variant key"
        )
