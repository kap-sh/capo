"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeHttp2ConnectionPool``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.max_requests


class VirtualNodeHttp2ConnectionPool(TypedDict, closed=True):
    max_requests: "capo_app_mesh.types.max_requests.MaxRequests"
    """<p>Maximum number of inflight requests Envoy can concurrently support across hosts in upstream cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeHttp2ConnectionPool) -> dict:
    out: dict = {}
    out["maxRequests"] = value["max_requests"]
    return out


def deserialize_json(data: dict) -> VirtualNodeHttp2ConnectionPool:
    out: VirtualNodeHttp2ConnectionPool = {}  # type: ignore[typeddict-item]
    if data.get("maxRequests") is not None:
        out["max_requests"] = data["maxRequests"]
    else:
        out["max_requests"] = 0
    return out
