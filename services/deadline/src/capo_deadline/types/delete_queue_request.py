"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.queue_id


class DeleteQueueRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The ID of the farm from which to remove the queue."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID of the queue to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueRequest:
    out: DeleteQueueRequest = {}  # type: ignore[typeddict-item]
    return out
