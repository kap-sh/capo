"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerAuthorizationMethod``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported authorization methods for MCP servers.</p>"""
MCPServerAuthorizationMethod: TypeAlias = Literal[
    "oauth-client-credentials",
    "oauth-3lo",
    "api-key",
    "bearer-token",
]


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerAuthorizationMethod) -> str:
    return value


def deserialize_json(data: str) -> MCPServerAuthorizationMethod:
    return cast(MCPServerAuthorizationMethod, data)
