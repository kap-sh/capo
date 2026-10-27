"""Generated from Smithy shape ``com.amazonaws.deadline#ListSessionActionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_token
    import capo_deadline.types.session_action_summaries


class ListSessionActionsResponse(TypedDict, closed=True):
    session_actions: (
        "capo_deadline.types.session_action_summaries.SessionActionSummaries"
    )
    """The session actions."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error."""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionActionsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.session_action_summaries

    out["sessionActions"] = capo_deadline.types.session_action_summaries.serialize_json(
        value["session_actions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionActionsResponse:
    out: ListSessionActionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionActions") is not None:
        import capo_deadline.types.session_action_summaries

        out["session_actions"] = (
            capo_deadline.types.session_action_summaries.deserialize_json(
                data["sessionActions"]
            )
        )
    else:
        out["session_actions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSessionActionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session_actions" in value:
        import capo_deadline.types.session_action_summaries

        out["session_actions"] = (
            capo_deadline.types.session_action_summaries.redact_sensitive(
                value["session_actions"]
            )
        )
    return out
