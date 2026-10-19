"""Generated from Smithy shape ``com.amazonaws.deadline#ListStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token
    import capo_deadline.types.queue_id


class ListStepsRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID to include on the list of steps.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID to include on the list of steps.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID to include on the list of steps.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStepsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStepsRequest:
    out: ListStepsRequest = {}  # type: ignore[typeddict-item]
    return out
