"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerSessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.ended_at
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_id
    import capo_deadline.types.session_lifecycle_status
    import capo_deadline.types.session_lifecycle_target_status
    import capo_deadline.types.started_at


class WorkerSessionSummary(TypedDict, closed=True):
    session_id: "capo_deadline.types.session_id.SessionId"
    """<p>The session ID for the session action.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the queue associated to the worker.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID for the job associated with the worker's session.</p>"""
    started_at: "capo_deadline.types.started_at.StartedAt"
    """<p>The date and time the resource started running.</p>"""
    lifecycle_status: (
        "capo_deadline.types.session_lifecycle_status.SessionLifecycleStatus"
    )
    """<p>The life cycle status for the worker's session.</p>"""
    ended_at: NotRequired["capo_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    target_lifecycle_status: NotRequired[
        "capo_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus"
    ]
    """<p>The life cycle status </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerSessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
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
    return out


def deserialize_json(data: dict) -> WorkerSessionSummary:
    out: WorkerSessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
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
    return out
