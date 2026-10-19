"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayHttpConnectionPool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.max_connections
    import capo_app_mesh.types.max_pending_requests


class VirtualGatewayHttpConnectionPool(TypedDict, closed=True):
    max_connections: "capo_app_mesh.types.max_connections.MaxConnections"
    """<p>Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.</p>"""
    max_pending_requests: NotRequired[
        "capo_app_mesh.types.max_pending_requests.MaxPendingRequests"
    ]
    """<p>Number of overflowing requests after <code>max_connections</code> Envoy will queue to upstream cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayHttpConnectionPool) -> dict:
    out: dict = {}
    out["maxConnections"] = value["max_connections"]
    if "max_pending_requests" in value:
        out["maxPendingRequests"] = value["max_pending_requests"]
    return out


def deserialize_json(data: dict) -> VirtualGatewayHttpConnectionPool:
    out: VirtualGatewayHttpConnectionPool = {}  # type: ignore[typeddict-item]
    if data.get("maxConnections") is not None:
        out["max_connections"] = data["maxConnections"]
    else:
        out["max_connections"] = 0
    if data.get("maxPendingRequests") is not None:
        out["max_pending_requests"] = data["maxPendingRequests"]
    return out
