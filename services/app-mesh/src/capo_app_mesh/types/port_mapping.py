"""Generated from Smithy shape ``com.amazonaws.appmesh#PortMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.port_number
    import capo_app_mesh.types.port_protocol


class PortMapping(TypedDict, closed=True):
    port: "capo_app_mesh.types.port_number.PortNumber"
    """<p>The port used for the port mapping.</p>"""
    protocol: "capo_app_mesh.types.port_protocol.PortProtocol"
    """<p>The protocol used for the port mapping. Specify one protocol.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortMapping) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    out["protocol"] = value["protocol"]
    return out


def deserialize_json(data: dict) -> PortMapping:
    out: PortMapping = {}  # type: ignore[typeddict-item]
    if data.get("port") is not None:
        out["port"] = data["port"]
    else:
        out["port"] = 0
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    else:
        out["protocol"] = ""
    return out
