"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteQueueLimitAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.limit_id
    import capo_deadline.types.queue_id


class DeleteQueueLimitAssociationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The unique identifier of the farm that contains the queue and limit to disassociate."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The unique identifier of the queue to disassociate."""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """The unique identifier of the limit to disassociate."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueLimitAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueLimitAssociationRequest:
    out: DeleteQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
