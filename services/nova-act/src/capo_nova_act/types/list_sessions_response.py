"""Generated from Smithy shape ``com.amazonaws.novaact#ListSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.next_token
    import capo_nova_act.types.session_summaries


class ListSessionsResponse(TypedDict, closed=True):
    session_summaries: "capo_nova_act.types.session_summaries.SessionSummaries"
    """<p>A list of summary information for sessions in the workflow run.</p>"""
    next_token: NotRequired["capo_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponse) -> dict:
    out: dict = {}
    import capo_nova_act.types.session_summaries

    out["sessionSummaries"] = capo_nova_act.types.session_summaries.serialize_json(
        value["session_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionsResponse:
    out: ListSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionSummaries") is not None:
        import capo_nova_act.types.session_summaries

        out["session_summaries"] = (
            capo_nova_act.types.session_summaries.deserialize_json(
                data["sessionSummaries"]
            )
        )
    else:
        out["session_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
