"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.queue_id


class CreateQueueResponse(TypedDict, closed=True):
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueResponse) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    return out


def deserialize_json(data: dict) -> CreateQueueResponse:
    out: CreateQueueResponse = {}  # type: ignore[typeddict-item]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    return out
