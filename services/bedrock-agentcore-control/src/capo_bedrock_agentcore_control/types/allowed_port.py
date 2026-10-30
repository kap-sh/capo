"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedPort``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.port
    import capo_bedrock_agentcore_control.types.port_range


class AllowedPortPortMember(TypedDict, closed=True):
    port: "capo_bedrock_agentcore_control.types.port.Port"


class AllowedPortPortRangeMember(TypedDict, closed=True):
    portRange: "capo_bedrock_agentcore_control.types.port_range.PortRange"


AllowedPort: TypeAlias = (
    AllowedPortPortMember | AllowedPortPortRangeMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AllowedPort) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AllowedPort: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "port" in value:
        return {"port": value["port"]}
    elif "portRange" in value:
        import capo_bedrock_agentcore_control.types.port_range

        return {
            "portRange": capo_bedrock_agentcore_control.types.port_range.serialize_json(
                value["portRange"]
            )
        }
    else:
        raise SerializationError("AllowedPort: no variant present")


def deserialize_json(data: dict) -> AllowedPort:
    if data.get("port") is not None:
        return {"port": data["port"]}
    elif data.get("portRange") is not None:
        import capo_bedrock_agentcore_control.types.port_range

        return {
            "portRange": capo_bedrock_agentcore_control.types.port_range.deserialize_json(
                data["portRange"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AllowedPort: no recognized variant key")
