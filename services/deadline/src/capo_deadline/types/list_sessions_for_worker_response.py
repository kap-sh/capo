"""Generated from Smithy shape ``com.amazonaws.deadline#ListSessionsForWorkerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.list_sessions_for_worker_summaries
    import capo_deadline.types.next_token


class ListSessionsForWorkerResponse(TypedDict, closed=True):
    sessions: "capo_deadline.types.list_sessions_for_worker_summaries.ListSessionsForWorkerSummaries"
    """<p>The sessions in the response.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsForWorkerResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.list_sessions_for_worker_summaries

    out["sessions"] = (
        capo_deadline.types.list_sessions_for_worker_summaries.serialize_json(
            value["sessions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionsForWorkerResponse:
    out: ListSessionsForWorkerResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessions") is not None:
        import capo_deadline.types.list_sessions_for_worker_summaries

        out["sessions"] = (
            capo_deadline.types.list_sessions_for_worker_summaries.deserialize_json(
                data["sessions"]
            )
        )
    else:
        out["sessions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
