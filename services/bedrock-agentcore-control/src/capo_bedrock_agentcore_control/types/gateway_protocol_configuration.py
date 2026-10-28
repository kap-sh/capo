"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayProtocolConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.mcp_gateway_configuration


class GatewayProtocolConfigurationMcpMember(TypedDict, closed=True):
    mcp: "capo_bedrock_agentcore_control.types.mcp_gateway_configuration.MCPGatewayConfiguration"


GatewayProtocolConfiguration: TypeAlias = (
    GatewayProtocolConfigurationMcpMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GatewayProtocolConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GatewayProtocolConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "mcp" in value:
        import capo_bedrock_agentcore_control.types.mcp_gateway_configuration

        return {
            "mcp": capo_bedrock_agentcore_control.types.mcp_gateway_configuration.serialize_json(
                value["mcp"]
            )
        }
    else:
        raise SerializationError("GatewayProtocolConfiguration: no variant present")


def deserialize_json(data: dict) -> GatewayProtocolConfiguration:
    if data.get("mcp") is not None:
        import capo_bedrock_agentcore_control.types.mcp_gateway_configuration

        return {
            "mcp": capo_bedrock_agentcore_control.types.mcp_gateway_configuration.deserialize_json(
                data["mcp"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "GatewayProtocolConfiguration: no recognized variant key"
        )


def redact_sensitive(value: GatewayProtocolConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "mcp" in value:
        import capo_bedrock_agentcore_control.types.mcp_gateway_configuration

        out["mcp"] = (
            capo_bedrock_agentcore_control.types.mcp_gateway_configuration.redact_sensitive(
                value["mcp"]
            )
        )
    return out
