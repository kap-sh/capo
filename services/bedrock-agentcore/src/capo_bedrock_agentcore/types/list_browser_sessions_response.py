"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListBrowserSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_session_summaries
    import capo_bedrock_agentcore.types.next_token


class ListBrowserSessionsResponse(TypedDict, closed=True):
    items: (
        "capo_bedrock_agentcore.types.browser_session_summaries.BrowserSessionSummaries"
    )
    """<p>The list of browser sessions that match the specified criteria.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore.types.next_token.NextToken"]
    """<p>The token to use in a subsequent <code>ListBrowserSessions</code> request to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBrowserSessionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.browser_session_summaries

    out["items"] = (
        capo_bedrock_agentcore.types.browser_session_summaries.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBrowserSessionsResponse:
    out: ListBrowserSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_bedrock_agentcore.types.browser_session_summaries

        out["items"] = (
            capo_bedrock_agentcore.types.browser_session_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
