"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateWorkerScheduleResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.assigned_sessions
    import capo_deadline.types.cancel_session_actions
    import capo_deadline.types.desired_worker_status
    import capo_deadline.types.update_worker_schedule_interval


class UpdateWorkerScheduleResponse(TypedDict, closed=True):
    assigned_sessions: "capo_deadline.types.assigned_sessions.AssignedSessions"
    """<p>The assigned sessions to update.</p>"""
    cancel_session_actions: (
        "capo_deadline.types.cancel_session_actions.CancelSessionActions"
    )
    """<p>The session actions associated with the worker schedule to cancel.</p>"""
    desired_worker_status: NotRequired[
        "capo_deadline.types.desired_worker_status.DesiredWorkerStatus"
    ]
    """<p>The status to update the worker to.</p>"""
    update_interval_seconds: "capo_deadline.types.update_worker_schedule_interval.UpdateWorkerScheduleInterval"
    """<p>Updates the time interval (in seconds) for the schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkerScheduleResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.assigned_sessions

    out["assignedSessions"] = capo_deadline.types.assigned_sessions.serialize_json(
        value["assigned_sessions"]
    )
    import capo_deadline.types.cancel_session_actions

    out["cancelSessionActions"] = (
        capo_deadline.types.cancel_session_actions.serialize_json(
            value["cancel_session_actions"]
        )
    )
    if "desired_worker_status" in value:
        import capo_deadline.types.desired_worker_status

        out["desiredWorkerStatus"] = (
            capo_deadline.types.desired_worker_status.serialize_json(
                value["desired_worker_status"]
            )
        )
    out["updateIntervalSeconds"] = value["update_interval_seconds"]
    return out


def deserialize_json(data: dict) -> UpdateWorkerScheduleResponse:
    out: UpdateWorkerScheduleResponse = {}  # type: ignore[typeddict-item]
    if data.get("assignedSessions") is not None:
        import capo_deadline.types.assigned_sessions

        out["assigned_sessions"] = (
            capo_deadline.types.assigned_sessions.deserialize_json(
                data["assignedSessions"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkerScheduleResponse.assigned_sessions required"
        )
    if data.get("cancelSessionActions") is not None:
        import capo_deadline.types.cancel_session_actions

        out["cancel_session_actions"] = (
            capo_deadline.types.cancel_session_actions.deserialize_json(
                data["cancelSessionActions"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkerScheduleResponse.cancel_session_actions required"
        )
    if data.get("desiredWorkerStatus") is not None:
        import capo_deadline.types.desired_worker_status

        out["desired_worker_status"] = (
            capo_deadline.types.desired_worker_status.deserialize_json(
                data["desiredWorkerStatus"]
            )
        )
    if data.get("updateIntervalSeconds") is not None:
        out["update_interval_seconds"] = data["updateIntervalSeconds"]
    else:
        raise DeserializationError(
            "UpdateWorkerScheduleResponse.update_interval_seconds required"
        )
    return out


def redact_sensitive(value: UpdateWorkerScheduleResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assigned_sessions" in value:
        import capo_deadline.types.assigned_sessions

        out["assigned_sessions"] = (
            capo_deadline.types.assigned_sessions.redact_sensitive(
                value["assigned_sessions"]
            )
        )
    return out
