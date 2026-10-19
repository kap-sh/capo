"""Generated from Smithy shape ``com.amazonaws.deadline#ListTasksResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_token
    import capo_deadline.types.task_summaries


class ListTasksResponse(TypedDict, closed=True):
    tasks: "capo_deadline.types.task_summaries.TaskSummaries"
    """<p>Tasks for the job.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTasksResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.task_summaries

    out["tasks"] = capo_deadline.types.task_summaries.serialize_json(value["tasks"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTasksResponse:
    out: ListTasksResponse = {}  # type: ignore[typeddict-item]
    if data.get("tasks") is not None:
        import capo_deadline.types.task_summaries

        out["tasks"] = capo_deadline.types.task_summaries.deserialize_json(
            data["tasks"]
        )
    else:
        out["tasks"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListTasksResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tasks" in value:
        import capo_deadline.types.task_summaries

        out["tasks"] = capo_deadline.types.task_summaries.redact_sensitive(
            value["tasks"]
        )
    return out
