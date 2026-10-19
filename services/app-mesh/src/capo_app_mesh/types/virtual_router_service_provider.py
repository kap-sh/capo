"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualRouterServiceProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.resource_name


class VirtualRouterServiceProvider(TypedDict, closed=True):
    virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual router that is acting as a service provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualRouterServiceProvider) -> dict:
    out: dict = {}
    out["virtualRouterName"] = value["virtual_router_name"]
    return out


def deserialize_json(data: dict) -> VirtualRouterServiceProvider:
    out: VirtualRouterServiceProvider = {}  # type: ignore[typeddict-item]
    if data.get("virtualRouterName") is not None:
        out["virtual_router_name"] = data["virtualRouterName"]
    else:
        out["virtual_router_name"] = ""
    return out
