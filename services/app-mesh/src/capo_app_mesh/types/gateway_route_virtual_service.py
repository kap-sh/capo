"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteVirtualService``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.resource_name


class GatewayRouteVirtualService(TypedDict, closed=True):
    virtual_service_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual service that traffic is routed to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteVirtualService) -> dict:
    out: dict = {}
    out["virtualServiceName"] = value["virtual_service_name"]
    return out


def deserialize_json(data: dict) -> GatewayRouteVirtualService:
    out: GatewayRouteVirtualService = {}  # type: ignore[typeddict-item]
    if data.get("virtualServiceName") is not None:
        out["virtual_service_name"] = data["virtualServiceName"]
    else:
        out["virtual_service_name"] = ""
    return out
