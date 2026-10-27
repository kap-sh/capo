"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.queue_environment_id


class CreateQueueEnvironmentResponse(TypedDict, closed=True):
    queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId"
    """The queue environment ID."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueEnvironmentResponse) -> dict:
    out: dict = {}
    out["queueEnvironmentId"] = value["queue_environment_id"]
    return out


def deserialize_json(data: dict) -> CreateQueueEnvironmentResponse:
    out: CreateQueueEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("queueEnvironmentId") is not None:
        out["queue_environment_id"] = data["queueEnvironmentId"]
    else:
        out["queue_environment_id"] = ""
    return out
