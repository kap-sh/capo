"""Generated from Smithy shape ``com.amazonaws.braket#HybridJobQueueInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.queue_name


class HybridJobQueueInfo(TypedDict, closed=True):
    queue: "capo_braket.types.queue_name.QueueName"
    """<p>The name of the queue.</p>"""
    position: "str"
    """<p>Current position of the hybrid job in the jobs queue.</p>"""
    message: NotRequired["str"]
    """<p>Optional. Provides more information about the queue position. For example, if the hybrid job is complete and no longer in the queue, the message field contains that information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HybridJobQueueInfo) -> dict:
    out: dict = {}
    out["queue"] = value["queue"]
    out["position"] = value["position"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> HybridJobQueueInfo:
    out: HybridJobQueueInfo = {}  # type: ignore[typeddict-item]
    if data.get("queue") is not None:
        out["queue"] = data["queue"]
    else:
        out["queue"] = ""
    if data.get("position") is not None:
        out["position"] = data["position"]
    else:
        out["position"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
