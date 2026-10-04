"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AgentCoreRuntimeServerProtocol``."""

from typing import Literal, TypeAlias, cast

AgentCoreRuntimeServerProtocol: TypeAlias = Literal[
    "HTTP",
    "A2A",
    "MCP",
    "AGUI",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCoreRuntimeServerProtocol) -> str:
    return value


def deserialize_json(data: str) -> AgentCoreRuntimeServerProtocol:
    return cast(AgentCoreRuntimeServerProtocol, data)
