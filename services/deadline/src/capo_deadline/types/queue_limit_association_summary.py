"""Generated from Smithy shape ``com.amazonaws.deadline#QueueLimitAssociationSummary``."""

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


class QueueLimitAssociationSummary(TypedDict, closed=True):
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The unique identifier of the queue in the association.</p>"""
    limit_id: "capo_deadline.types.limit_id.LimitId"
    """<p>The unique identifier of the limit in the association.</p>"""
    status: (
        "capo_deadline.types.queue_limit_association_status.QueueLimitAssociationStatus"
    )
    """<p>The status of task scheduling in the queue-limit association.</p> <ul> <li> <p> <code>ACTIVE</code> - Association is active.</p> </li> <li> <p> <code>STOP_LIMIT_USAGE_AND_COMPLETE_TASKS</code> - Association has stopped scheduling new tasks and is completing current tasks.</p> </li> <li> <p> <code>STOP_LIMIT_USAGE_AND_CANCEL_TASKS</code> - Association has stopped scheduling new tasks and is canceling current tasks.</p> </li> <li> <p> <code>STOPPED</code> - Association has been stopped.</p> </li> </ul>"""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """<p>The Unix timestamp of the date and time that the association was created.</p>"""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """<p>The user identifier of the person that created the association.</p>"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """<p>The Unix timestamp of the date and time that the association was last updated.</p>"""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """<p>The user identifier of the person that updated the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueLimitAssociationSummary) -> dict:
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


def deserialize_json(data: dict) -> QueueLimitAssociationSummary:
    out: QueueLimitAssociationSummary = {}  # type: ignore[typeddict-item]
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
