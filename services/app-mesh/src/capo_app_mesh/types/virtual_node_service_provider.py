"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualNodeServiceProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.resource_name


class VirtualNodeServiceProvider(TypedDict, closed=True):
    virtual_node_name: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The name of the virtual node that is acting as a service provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualNodeServiceProvider) -> dict:
    out: dict = {}
    out["virtualNodeName"] = value["virtual_node_name"]
    return out


def deserialize_json(data: dict) -> VirtualNodeServiceProvider:
    out: VirtualNodeServiceProvider = {}  # type: ignore[typeddict-item]
    if data.get("virtualNodeName") is not None:
        out["virtual_node_name"] = data["virtualNodeName"]
    else:
        out["virtual_node_name"] = ""
    return out
