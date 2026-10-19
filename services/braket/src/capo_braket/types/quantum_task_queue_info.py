"""Generated from Smithy shape ``com.amazonaws.braket#QuantumTaskQueueInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.queue_name
    import capo_braket.types.queue_priority


class QuantumTaskQueueInfo(TypedDict, closed=True):
    queue: "capo_braket.types.queue_name.QueueName"
    """<p>The name of the queue. </p>"""
    position: "str"
    """<p>Current position of the quantum task in the quantum tasks queue.</p>"""
    queue_priority: NotRequired["capo_braket.types.queue_priority.QueuePriority"]
    """<p>Optional. Specifies the priority of the queue. Quantum tasks in a priority queue are processed before the quantum tasks in a normal queue.</p>"""
    message: NotRequired["str"]
    """<p>Optional. Provides more information about the queue position. For example, if the quantum task is complete and no longer in the queue, the message field contains that information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuantumTaskQueueInfo) -> dict:
    out: dict = {}
    out["queue"] = value["queue"]
    out["position"] = value["position"]
    if "queue_priority" in value:
        out["queuePriority"] = value["queue_priority"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> QuantumTaskQueueInfo:
    out: QuantumTaskQueueInfo = {}  # type: ignore[typeddict-item]
    if data.get("queue") is not None:
        out["queue"] = data["queue"]
    else:
        out["queue"] = ""
    if data.get("position") is not None:
        out["position"] = data["position"]
    else:
        out["position"] = ""
    if data.get("queuePriority") is not None:
        out["queue_priority"] = data["queuePriority"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
