"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueLimitAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.limit_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.queue_limit_association_status
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class GetQueueLimitAssociationResponse(TypedDict, closed=True):
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The unique identifier of the queue associated with the limit."""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """The unique identifier of the limit associated with the queue."""
    status: (
        "capo_deadline.types.queue_limit_association_status.QueueLimitAssociationStatus"
    )
    """The current status of the limit."""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """The Unix timestamp of the date and time that the association was created."""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """The user identifier of the person that created the association."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The Unix timestamp of the date and time that the association was last updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user identifier of the person that last updated the association."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueLimitAssociationResponse) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["limitId"] = value["limit_id"]
    import capo_deadline.types.queue_limit_association_status

    out["status"] = capo_deadline.types.queue_limit_association_status.serialize_json(
        value["status"]
    )
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> GetQueueLimitAssociationResponse:
    out: GetQueueLimitAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    if data.get("limitId") is not None:
        out["limit_id"] = data["limitId"]
    else:
        out["limit_id"] = ""
    if data.get("status") is not None:
        import capo_deadline.types.queue_limit_association_status

        out["status"] = (
            capo_deadline.types.queue_limit_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.queue_limit_association_status.QueueLimitAssociationStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    return out
