"""Generated from Smithy shape ``com.amazonaws.deadline#ListMonitorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.monitor_summaries
    import capo_deadline.types.next_token


class ListMonitorsResponse(TypedDict, closed=True):
    monitors: "capo_deadline.types.monitor_summaries.MonitorSummaries"
    """A list of <code>MonitorSummary</code> objects that describe your monitors in the Deadline Cloud."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error."""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitorsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.monitor_summaries

    out["monitors"] = capo_deadline.types.monitor_summaries.serialize_json(
        value["monitors"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMonitorsResponse:
    out: ListMonitorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("monitors") is not None:
        import capo_deadline.types.monitor_summaries

        out["monitors"] = capo_deadline.types.monitor_summaries.deserialize_json(
            data["monitors"]
        )
    else:
        out["monitors"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
