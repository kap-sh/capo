"""Generated from Smithy shape ``com.amazonaws.wisdom#SearchSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.next_token
    import capo_wisdom.types.session_summaries


class SearchSessionsResponse(TypedDict, closed=True):
    session_summaries: "capo_wisdom.types.session_summaries.SessionSummaries"
    """<p>Summary information about the sessions.</p>"""
    next_token: NotRequired["capo_wisdom.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSessionsResponse) -> dict:
    out: dict = {}
    import capo_wisdom.types.session_summaries

    out["sessionSummaries"] = capo_wisdom.types.session_summaries.serialize_json(
        value["session_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchSessionsResponse:
    out: SearchSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionSummaries") is not None:
        import capo_wisdom.types.session_summaries

        out["session_summaries"] = capo_wisdom.types.session_summaries.deserialize_json(
            data["sessionSummaries"]
        )
    else:
        out["session_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
