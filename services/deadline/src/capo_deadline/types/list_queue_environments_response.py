"""Generated from Smithy shape ``com.amazonaws.deadline#ListQueueEnvironmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_token
    import capo_deadline.types.queue_environment_summaries


class ListQueueEnvironmentsResponse(TypedDict, closed=True):
    environments: (
        "capo_deadline.types.queue_environment_summaries.QueueEnvironmentSummaries"
    )
    """<p>The environments to include in the queue environments list.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQueueEnvironmentsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.queue_environment_summaries

    out["environments"] = (
        capo_deadline.types.queue_environment_summaries.serialize_json(
            value["environments"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQueueEnvironmentsResponse:
    out: ListQueueEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("environments") is not None:
        import capo_deadline.types.queue_environment_summaries

        out["environments"] = (
            capo_deadline.types.queue_environment_summaries.deserialize_json(
                data["environments"]
            )
        )
    else:
        out["environments"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
