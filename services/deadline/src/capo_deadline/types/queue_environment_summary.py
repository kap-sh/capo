"""Generated from Smithy shape ``com.amazonaws.deadline#QueueEnvironmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.environment_name
    import capo_deadline.types.priority
    import capo_deadline.types.queue_environment_id


class QueueEnvironmentSummary(TypedDict, closed=True):
    queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId"
    """<p>The queue environment ID.</p>"""
    name: "capo_deadline.types.environment_name.EnvironmentName"
    """<p>The name of the queue environment.</p>"""
    priority: "capo_deadline.types.priority.Priority"
    """<p>The queue environment's priority.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueEnvironmentSummary) -> dict:
    out: dict = {}
    out["queueEnvironmentId"] = value["queue_environment_id"]
    out["name"] = value["name"]
    out["priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> QueueEnvironmentSummary:
    out: QueueEnvironmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("queueEnvironmentId") is not None:
        out["queue_environment_id"] = data["queueEnvironmentId"]
    else:
        out["queue_environment_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        out["priority"] = 0
    return out
