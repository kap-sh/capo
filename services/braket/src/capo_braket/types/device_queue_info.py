"""Generated from Smithy shape ``com.amazonaws.braket#DeviceQueueInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.queue_name
    import capo_braket.types.queue_priority


class DeviceQueueInfo(TypedDict, closed=True):
    queue: "capo_braket.types.queue_name.QueueName"
    """<p>The name of the queue. </p>"""
    queue_size: "str"
    """<p>The number of hybrid jobs or quantum tasks in the queue for a given device. </p>"""
    queue_priority: NotRequired["capo_braket.types.queue_priority.QueuePriority"]
    """<p>Optional. Specifies the priority of the queue. Quantum tasks in a priority queue are processed before the quantum tasks in a normal queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceQueueInfo) -> dict:
    out: dict = {}
    out["queue"] = value["queue"]
    out["queueSize"] = value["queue_size"]
    if "queue_priority" in value:
        out["queuePriority"] = value["queue_priority"]
    return out


def deserialize_json(data: dict) -> DeviceQueueInfo:
    out: DeviceQueueInfo = {}  # type: ignore[typeddict-item]
    if data.get("queue") is not None:
        out["queue"] = data["queue"]
    else:
        out["queue"] = ""
    if data.get("queueSize") is not None:
        out["queue_size"] = data["queueSize"]
    else:
        out["queue_size"] = ""
    if data.get("queuePriority") is not None:
        out["queue_priority"] = data["queuePriority"]
    return out
