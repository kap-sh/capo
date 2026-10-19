"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.session_summaries


class ListSessionsResponse(TypedDict, closed=True):
    session_summaries: (
        "capo_bedrock_agent_runtime.types.session_summaries.SessionSummaries"
    )
    """<p>A list of summaries for each session in your Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.session_summaries

    out["sessionSummaries"] = (
        capo_bedrock_agent_runtime.types.session_summaries.serialize_json(
            value["session_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionsResponse:
    out: ListSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionSummaries") is not None:
        import capo_bedrock_agent_runtime.types.session_summaries

        out["session_summaries"] = (
            capo_bedrock_agent_runtime.types.session_summaries.deserialize_json(
                data["sessionSummaries"]
            )
        )
    else:
        out["session_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
