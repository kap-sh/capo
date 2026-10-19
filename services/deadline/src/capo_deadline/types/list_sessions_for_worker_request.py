"""Generated from Smithy shape ``com.amazonaws.deadline#ListSessionsForWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token
    import capo_deadline.types.worker_id


class ListSessionsForWorkerRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the session.</p>"""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID for the session.</p>"""
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The worker ID for the session.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsForWorkerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSessionsForWorkerRequest:
    out: ListSessionsForWorkerRequest = {}  # type: ignore[typeddict-item]
    return out
