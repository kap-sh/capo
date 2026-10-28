"""Generated from Smithy shape ``com.amazonaws.devopsagent#DatadogAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.mcp_server_authorization_discovery_config


class DatadogAuthorizationConfigAuthorizationDiscoveryMember(TypedDict, closed=True):
    authorizationDiscovery: "capo_devops_agent.types.mcp_server_authorization_discovery_config.MCPServerAuthorizationDiscoveryConfig"


DatadogAuthorizationConfig: TypeAlias = (
    DatadogAuthorizationConfigAuthorizationDiscoveryMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DatadogAuthorizationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DatadogAuthorizationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "authorizationDiscovery" in value:
        import capo_devops_agent.types.mcp_server_authorization_discovery_config

        return {
            "authorizationDiscovery": capo_devops_agent.types.mcp_server_authorization_discovery_config.serialize_json(
                value["authorizationDiscovery"]
            )
        }
    else:
        raise SerializationError("DatadogAuthorizationConfig: no variant present")


def deserialize_json(data: dict) -> DatadogAuthorizationConfig:
    if data.get("authorizationDiscovery") is not None:
        import capo_devops_agent.types.mcp_server_authorization_discovery_config

        return {
            "authorizationDiscovery": capo_devops_agent.types.mcp_server_authorization_discovery_config.deserialize_json(
                data["authorizationDiscovery"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DatadogAuthorizationConfig: no recognized variant key"
        )
