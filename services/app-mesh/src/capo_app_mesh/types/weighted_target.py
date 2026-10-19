"""Generated from Smithy shape ``com.amazonaws.appmesh#WeightedTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.listener_port
    import capo_app_mesh.types.percent_int
    import capo_app_mesh.types.resource_name


class WeightedTarget(TypedDict, closed=True):
    virtual_node: "capo_app_mesh.types.resource_name.ResourceName"
    """<p>The virtual node to associate with the weighted target.</p>"""
    weight: "capo_app_mesh.types.percent_int.PercentInt"
    """<p>The relative weight of the weighted target.</p>"""
    port: NotRequired["capo_app_mesh.types.listener_port.ListenerPort"]
    """<p>The targeted port of the weighted object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedTarget) -> dict:
    out: dict = {}
    out["virtualNode"] = value["virtual_node"]
    out["weight"] = value.get("weight", 0)
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> WeightedTarget:
    out: WeightedTarget = {}  # type: ignore[typeddict-item]
    if data.get("virtualNode") is not None:
        out["virtual_node"] = data["virtualNode"]
    else:
        out["virtual_node"] = ""
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    else:
        out["weight"] = 0
    if data.get("port") is not None:
        out["port"] = data["port"]
    return out
