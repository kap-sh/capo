"""Generated from Smithy shape ``com.amazonaws.signin#ClientType``."""

from typing import Literal, TypeAlias, cast

"""Type of OAuth client that created a session"""
ClientType: TypeAlias = Literal[
    "CLI",
    "MCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientType) -> str:
    return value


def deserialize_json(data: str) -> ClientType:
    return cast(ClientType, data)
