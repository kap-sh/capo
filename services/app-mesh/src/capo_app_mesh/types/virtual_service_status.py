"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualServiceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_service_status_code


class VirtualServiceStatus(TypedDict, closed=True):
    status: "capo_app_mesh.types.virtual_service_status_code.VirtualServiceStatusCode"
    """<p>The current status of the virtual service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualServiceStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VirtualServiceStatus:
    out: VirtualServiceStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
