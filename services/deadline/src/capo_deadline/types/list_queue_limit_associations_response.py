"""Generated from Smithy shape ``com.amazonaws.deadline#ListQueueLimitAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_token
    import capo_deadline.types.queue_limit_association_summaries


class ListQueueLimitAssociationsResponse(TypedDict, closed=True):
    queue_limit_associations: "capo_deadline.types.queue_limit_association_summaries.QueueLimitAssociationSummaries"
    """A list of associations between limits and queues in the farm specified in the request."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error."""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueueLimitAssociationsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.queue_limit_association_summaries

    out["queueLimitAssociations"] = (
        capo_deadline.types.queue_limit_association_summaries.serialize_json(
            value["queue_limit_associations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQueueLimitAssociationsResponse:
    out: ListQueueLimitAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("queueLimitAssociations") is not None:
        import capo_deadline.types.queue_limit_association_summaries

        out["queue_limit_associations"] = (
            capo_deadline.types.queue_limit_association_summaries.deserialize_json(
                data["queueLimitAssociations"]
            )
        )
    else:
        out["queue_limit_associations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
