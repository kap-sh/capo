"""Generated from Smithy shape ``com.amazonaws.mpa#ListSessionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.list_sessions_response_sessions
    import capo_mpa.types.token


class ListSessionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    sessions: NotRequired[
        "capo_mpa.types.list_sessions_response_sessions.ListSessionsResponseSessions"
    ]
    """<p>An array of <code>ListSessionsResponseSession</code> objects. Contains details for the sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sessions" in value:
        import capo_mpa.types.list_sessions_response_sessions

        out["Sessions"] = capo_mpa.types.list_sessions_response_sessions.serialize_json(
            value["sessions"]
        )
    return out


def deserialize_json(data: dict) -> ListSessionsResponse:
    out: ListSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Sessions") is not None:
        import capo_mpa.types.list_sessions_response_sessions

        out["sessions"] = (
            capo_mpa.types.list_sessions_response_sessions.deserialize_json(
                data["Sessions"]
            )
        )
    return out


def redact_sensitive(value: ListSessionsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sessions" in value:
        import capo_mpa.types.list_sessions_response_sessions

        out["sessions"] = (
            capo_mpa.types.list_sessions_response_sessions.redact_sensitive(
                value["sessions"]
            )
        )
    return out
