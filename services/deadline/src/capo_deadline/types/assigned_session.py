"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.assigned_session_actions
    import capo_deadline.types.job_id
    import capo_deadline.types.log_configuration
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_metadata


class AssignedSession(TypedDict, closed=True):
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the assigned session.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID for the assigned session.</p>"""
    session_actions: (
        "capo_deadline.types.assigned_session_actions.AssignedSessionActions"
    )
    """<p>The session actions to apply to the assigned session.</p>"""
    log_configuration: "capo_deadline.types.log_configuration.LogConfiguration"
    """<p>The log configuration for the worker's assigned session.</p>"""
    metadata: NotRequired["capo_deadline.types.session_metadata.SessionMetadata"]
    """<p>Key-value hints that the service provides to guide how the session runs. This value is used by the worker agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSession) -> dict:
    out: dict = {}
    out["queueId"] = value["queue_id"]
    out["jobId"] = value["job_id"]
    import capo_deadline.types.assigned_session_actions

    out["sessionActions"] = capo_deadline.types.assigned_session_actions.serialize_json(
        value["session_actions"]
    )
    import capo_deadline.types.log_configuration

    out["logConfiguration"] = capo_deadline.types.log_configuration.serialize_json(
        value["log_configuration"]
    )
    if "metadata" in value:
        import capo_deadline.types.session_metadata

        out["metadata"] = capo_deadline.types.session_metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> AssignedSession:
    out: AssignedSession = {}  # type: ignore[typeddict-item]
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        raise DeserializationError("AssignedSession.queue_id required")
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("AssignedSession.job_id required")
    if data.get("sessionActions") is not None:
        import capo_deadline.types.assigned_session_actions

        out["session_actions"] = (
            capo_deadline.types.assigned_session_actions.deserialize_json(
                data["sessionActions"]
            )
        )
    else:
        raise DeserializationError("AssignedSession.session_actions required")
    if data.get("logConfiguration") is not None:
        import capo_deadline.types.log_configuration

        out["log_configuration"] = (
            capo_deadline.types.log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    else:
        raise DeserializationError("AssignedSession.log_configuration required")
    if data.get("metadata") is not None:
        import capo_deadline.types.session_metadata

        out["metadata"] = capo_deadline.types.session_metadata.deserialize_json(
            data["metadata"]
        )
    return out
