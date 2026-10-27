"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueLimitAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.limit_id
    import capo_deadline.types.queue_id


class GetQueueLimitAssociationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The unique identifier of the farm that contains the associated queue and limit."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The unique identifier of the queue associated with the limit."""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """The unique identifier of the limit associated with the queue."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueLimitAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQueueLimitAssociationRequest:
    out: GetQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
