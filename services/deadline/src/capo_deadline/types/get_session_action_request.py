"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_action_id


class GetSessionActionRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the session action."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID for the session action."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID for the session."""
    session_action_id: "capo_deadline.types.session_action_id.SessionActionId"
    """The session action ID for the session."""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionActionRequest:
    out: GetSessionActionRequest = {}  # type: ignore[typeddict-item]
    return out
