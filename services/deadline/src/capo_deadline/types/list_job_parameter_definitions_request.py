"""Generated from Smithy shape ``com.amazonaws.deadline#ListJobParameterDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token
    import capo_deadline.types.queue_id


class ListJobParameterDefinitionsRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the job to list."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID to include on the list."""
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID to include on the list."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """The token for the next set of results, or <code>null</code> to start from the beginning."""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages."""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobParameterDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListJobParameterDefinitionsRequest:
    out: ListJobParameterDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
