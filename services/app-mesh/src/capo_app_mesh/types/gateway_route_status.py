"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.gateway_route_status_code


class GatewayRouteStatus(TypedDict, closed=True):
    status: "capo_app_mesh.types.gateway_route_status_code.GatewayRouteStatusCode"
    """<p>The current status for the gateway route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteStatus) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> GatewayRouteStatus:
    out: GatewayRouteStatus = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
