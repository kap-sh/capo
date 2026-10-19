"""Generated from Smithy shape ``com.amazonaws.deadline#ListQueuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token
    import capo_deadline.types.queue_status


class ListQueuesRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the queue.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    principal_id: NotRequired[
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    ]
    """<p>The principal IDs to include in the list of queues.</p>"""
    status: NotRequired["capo_deadline.types.queue_status.QueueStatus"]
    """<p>The status of the queues listed.</p> <ul> <li> <p> <code>ACTIVE</code>–The queues are active.</p> </li> <li> <p> <code>SCHEDULING</code>–The queues are scheduling.</p> </li> <li> <p> <code>SCHEDULING_BLOCKED</code>–The queue scheduling is blocked for these queues.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueuesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQueuesRequest:
    out: ListQueuesRequest = {}  # type: ignore[typeddict-item]
    return out
