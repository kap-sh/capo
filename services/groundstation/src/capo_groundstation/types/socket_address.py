"""Generated from Smithy shape ``com.amazonaws.groundstation#SocketAddress``."""

from typing_extensions import TypedDict


class SocketAddress(TypedDict, closed=True):
    name: "str"
    """<p>Name of a socket address.</p>"""
    port: "int"
    """<p>Port of a socket address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SocketAddress) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> SocketAddress:
    out: SocketAddress = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    return out
