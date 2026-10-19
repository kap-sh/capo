"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_router_status_code


class VirtualRouterStatus(TypedDict, closed=True):
    status: "capo_app_mesh.types.virtual_router_status_code.VirtualRouterStatusCode"
    """<p>The current status of the virtual router.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VirtualRouterStatus:
    out: VirtualRouterStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
