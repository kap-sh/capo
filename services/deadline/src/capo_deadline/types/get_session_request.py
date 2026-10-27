"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_id


class GetSessionRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the session."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID for the session."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID for the session."""
    session_id: "capo_deadline.types.session_id.SessionId"
    """The session ID."""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionRequest:
    out: GetSessionRequest = {}  # type: ignore[typeddict-item]
    return out
