"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkProtocol``."""

from typing import Literal, TypeAlias, cast

NetworkProtocol: TypeAlias = Literal[
    "IPv4",
    "DualStack",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkProtocol) -> str:
    return value


def deserialize_json(data: str) -> NetworkProtocol:
    return cast(NetworkProtocol, data)
