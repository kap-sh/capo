"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_node_status_code


class VirtualNodeStatus(TypedDict, closed=True):
    status: "capo_app_mesh.types.virtual_node_status_code.VirtualNodeStatusCode"
    """<p>The current status of the virtual node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VirtualNodeStatus:
    out: VirtualNodeStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
