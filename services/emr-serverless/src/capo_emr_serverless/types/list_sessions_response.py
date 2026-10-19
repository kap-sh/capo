"""Generated from Smithy shape ``com.amazonaws.emrserverless#ListSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.next_token
    import capo_emr_serverless.types.sessions


class ListSessionsResponse(TypedDict, closed=True):
    sessions: "capo_emr_serverless.types.sessions.Sessions"
    """<p>The output lists information about the specified sessions.</p>"""
    next_token: NotRequired["capo_emr_serverless.types.next_token.NextToken"]
    """<p>The output displays the token for the next set of session results. This is required for pagination and is available as a response of the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponse) -> dict:
    out: dict = {}
    import capo_emr_serverless.types.sessions

    out["sessions"] = capo_emr_serverless.types.sessions.serialize_json(
        value["sessions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionsResponse:
    out: ListSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessions") is not None:
        import capo_emr_serverless.types.sessions

        out["sessions"] = capo_emr_serverless.types.sessions.deserialize_json(
            data["sessions"]
        )
    else:
        out["sessions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
