"""Generated from Smithy shape ``com.amazonaws.deadline#ListStepDependenciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.integer
    import capo_deadline.types.job_id
    import capo_deadline.types.next_token
    import capo_deadline.types.queue_id
    import capo_deadline.types.step_id


class ListStepDependenciesRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the step dependencies list.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID for the step dependencies list.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID for the step dependencies list.</p>"""
    step_id: "capo_deadline.types.step_id.StepId"
    """<p>The step ID to include on the list.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: NotRequired["capo_deadline.types.integer.Integer"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStepDependenciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStepDependenciesRequest:
    out: ListStepDependenciesRequest = {}  # type: ignore[typeddict-item]
    return out
