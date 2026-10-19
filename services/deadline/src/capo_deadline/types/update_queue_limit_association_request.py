"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueLimitAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.limit_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.update_queue_limit_association_status


class UpdateQueueLimitAssociationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The unique identifier of the farm that contains the associated queues and limits.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The unique identifier of the queue associated to the limit.</p>"""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit associated to the queue.</p>"""
    status: "capo_deadline.types.update_queue_limit_association_status.UpdateQueueLimitAssociationStatus"
    """<p>Sets the status of the limit. You can mark the limit active, or you can stop usage of the limit and either complete existing tasks or cancel any existing tasks immediately. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueLimitAssociationRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.update_queue_limit_association_status

    out["status"] = (
        capo_deadline.types.update_queue_limit_association_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQueueLimitAssociationRequest:
    out: UpdateQueueLimitAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_deadline.types.update_queue_limit_association_status

        out["status"] = (
            capo_deadline.types.update_queue_limit_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.update_queue_limit_association_status.UpdateQueueLimitAssociationStatus",
            "",
        )
    return out
