"""Generated from Smithy shape ``com.amazonaws.deadline#ListQueueFleetAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token
    import capo_deadline.types.queue_id


class ListQueueFleetAssociationsRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the queue-fleet association list.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    queue_id: NotRequired["capo_deadline.types.queue_id.QueueId"]
    """<p>The queue ID for the queue-fleet association list.</p>"""
    fleet_id: NotRequired["capo_deadline.types.fleet_id.FleetId"]
    """<p>The fleet ID for the queue-fleet association list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueueFleetAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQueueFleetAssociationsRequest:
    out: ListQueueFleetAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
