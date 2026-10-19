"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_status_code


class VirtualGatewayStatus(TypedDict, closed=True):
    status: "capo_app_mesh.types.virtual_gateway_status_code.VirtualGatewayStatusCode"
    """<p>The current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> VirtualGatewayStatus:
    out: VirtualGatewayStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
