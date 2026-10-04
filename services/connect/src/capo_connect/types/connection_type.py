"""Generated from Smithy shape ``com.amazonaws.connect#ConnectionType``."""

from typing import Literal, TypeAlias, cast

ConnectionType: TypeAlias = Literal[
    "WEBSOCKET",
    "CONNECTION_CREDENTIALS",
    "AUTHENTICATION_SESSION",
    "WEBRTC_CONNECTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    return cast(ConnectionType, data)
