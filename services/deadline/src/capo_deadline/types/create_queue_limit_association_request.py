"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueLimitAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.limit_id
    import capo_deadline.types.queue_id


class CreateQueueLimitAssociationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the queue and limit to associate.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The unique identifier of the queue to associate with the limit.</p>"""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit to associate with the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueLimitAssociationRequest) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["limitId"] = value["limit_id"]
    return out


def deserialize_json(data: dict) -> CreateQueueLimitAssociationRequest:
    out: CreateQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    if data.get("limitId") is not None:
        out["limit_id"] = data["limitId"]
    else:
        out["limit_id"] = ""
    return out
