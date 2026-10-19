"""Generated from Smithy shape ``com.amazonaws.panorama#NodeSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.node_instance_id
    import capo_panorama.types.node_signal_value


class NodeSignal(TypedDict, closed=True):
    node_instance_id: "capo_panorama.types.node_instance_id.NodeInstanceId"
    """<p>The camera node's name, from the application manifest.</p>"""
    signal: "capo_panorama.types.node_signal_value.NodeSignalValue"
    """<p>The signal value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeSignal) -> dict:
    out: dict = {}
    out["NodeInstanceId"] = value["node_instance_id"]
    out["Signal"] = value["signal"]
    return out


def deserialize_json(data: dict) -> NodeSignal:
    out: NodeSignal = {}  # type: ignore[typeddict-item]
    if data.get("NodeInstanceId") is not None:
        out["node_instance_id"] = data["NodeInstanceId"]
    else:
        out["node_instance_id"] = ""
    if data.get("Signal") is not None:
        out["signal"] = data["Signal"]
    else:
        out["signal"] = ""
    return out
