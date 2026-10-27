"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.queue_id


class GetQueueRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm in the queue."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID for the queue to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueRequest:
    out: GetQueueRequest = {}  # type: ignore[typeddict-item]
    return out
