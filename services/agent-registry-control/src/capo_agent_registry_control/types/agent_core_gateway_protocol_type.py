"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AgentCoreGatewayProtocolType``."""

from typing import Literal, TypeAlias, cast

"""The protocol type of an AgentCore Gateway."""
AgentCoreGatewayProtocolType: TypeAlias = Literal["MCP",]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCoreGatewayProtocolType) -> str:
    return value


def deserialize_json(data: str) -> AgentCoreGatewayProtocolType:
    return cast(AgentCoreGatewayProtocolType, data)
