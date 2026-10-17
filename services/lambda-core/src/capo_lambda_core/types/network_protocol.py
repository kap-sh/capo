"""Generated from Smithy shape ``com.amazonaws.lambdacore#NetworkProtocol``."""

from typing import Literal, TypeAlias, cast

"""<p>The network protocol for a connector. <code>IPv4</code> enables IPv4-only networking; <code>DualStack</code> enables both IPv4 and IPv6.</p>"""
NetworkProtocol: TypeAlias = Literal[
    "IPv4",
    "DualStack",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkProtocol) -> str:
    return value


def deserialize_json(data: str) -> NetworkProtocol:
    return cast(NetworkProtocol, data)
