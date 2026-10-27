"""Generated from Smithy shape ``com.amazonaws.deadline#ListSessionActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_id
    import capo_deadline.types.task_id


class ListSessionActionsRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the session actions list."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID for the session actions list."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID for the session actions list."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """The token for the next set of results, or <code>null</code> to start from the beginning."""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages."""
    session_id: NotRequired["capo_deadline.types.session_id.SessionId"]
    """The session ID to include on the sessions action list."""
    task_id: NotRequired["capo_deadline.types.task_id.TaskId"]
    """The task ID for the session actions list."""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionActionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSessionActionsRequest:
    out: ListSessionActionsRequest = {}  # type: ignore[typeddict-item]
    return out
