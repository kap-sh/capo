"""Generated from Smithy shape ``com.amazonaws.deadline#SessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.ended_at
    import capo_deadline.types.fleet_id
    import capo_deadline.types.session_id
    import capo_deadline.types.session_lifecycle_status
    import capo_deadline.types.session_lifecycle_target_status
    import capo_deadline.types.started_at
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by
    import capo_deadline.types.worker_id


class SessionSummary(TypedDict, closed=True):
    session_id: "capo_deadline.types.session_id.SessionId"
    """The session ID."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID."""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """The worker ID."""
    started_at: "capo_deadline.types.started_at.StartedAt"
    """The date and time the resource started running."""
    lifecycle_status: (
        "capo_deadline.types.session_lifecycle_status.SessionLifecycleStatus"
    )
    """The life cycle status for the session."""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """The date and time the resource ended running."""
    target_lifecycle_status: NotRequired[
        "capo_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus"
    ]
    """The target life cycle status for the session."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The date and time the resource was updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user or system that updated this resource."""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["fleetId"] = value["fleet_id"]
    out["workerId"] = value["worker_id"]
    import capo_deadline.types.started_at

    out["startedAt"] = capo_deadline.types.started_at.serialize_json(
        value["started_at"]
    )
    import capo_deadline.types.session_lifecycle_status

    out["lifecycleStatus"] = (
        capo_deadline.types.session_lifecycle_status.serialize_json(
            value["lifecycle_status"]
        )
    )
    if "ended_at" in value:
        import capo_deadline.types.ended_at

        out["endedAt"] = capo_deadline.types.ended_at.serialize_json(value["ended_at"])
    if "target_lifecycle_status" in value:
        import capo_deadline.types.session_lifecycle_target_status

        out["targetLifecycleStatus"] = (
            capo_deadline.types.session_lifecycle_target_status.serialize_json(
                value["target_lifecycle_status"]
            )
        )
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    if data.get("workerId") is not None:
        out["worker_id"] = data["workerId"]
    else:
        out["worker_id"] = ""
    if data.get("startedAt") is not None:
        import capo_deadline.types.started_at

        out["started_at"] = capo_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lifecycleStatus") is not None:
        import capo_deadline.types.session_lifecycle_status

        out["lifecycle_status"] = (
            capo_deadline.types.session_lifecycle_status.deserialize_json(
                data["lifecycleStatus"]
            )
        )
    else:
        import typing

        out["lifecycle_status"] = typing.cast(
            "capo_deadline.types.session_lifecycle_status.SessionLifecycleStatus", ""
        )
    if data.get("endedAt") is not None:
        import capo_deadline.types.ended_at

        out["ended_at"] = capo_deadline.types.ended_at.deserialize_json(data["endedAt"])
    if data.get("targetLifecycleStatus") is not None:
        import capo_deadline.types.session_lifecycle_target_status

        out["target_lifecycle_status"] = (
            capo_deadline.types.session_lifecycle_target_status.deserialize_json(
                data["targetLifecycleStatus"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    return out
