"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeTcpConnectionPool``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.max_connections


class VirtualNodeTcpConnectionPool(TypedDict, closed=True):
    max_connections: "capo_app_mesh.types.max_connections.MaxConnections"
    """<p>Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeTcpConnectionPool) -> dict:
    out: dict = {}
    out["maxConnections"] = value["max_connections"]
    return out


def deserialize_json(data: dict) -> VirtualNodeTcpConnectionPool:
    out: VirtualNodeTcpConnectionPool = {}  # type: ignore[typeddict-item]
    if data.get("maxConnections") is not None:
        out["max_connections"] = data["maxConnections"]
    else:
        out["max_connections"] = 0
    return out
