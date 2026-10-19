"""Generated from Smithy shape ``com.amazonaws.quicksight#ListAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agent_summaries


class ListAgentsResponse(TypedDict, closed=True):
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    agent_summaries: "capo_quicksight.types.agent_summaries.AgentSummaries"
    """<p>A list of agent summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    import capo_quicksight.types.agent_summaries

    out["AgentSummaries"] = capo_quicksight.types.agent_summaries.serialize_json(
        value["agent_summaries"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentsResponse:
    out: ListAgentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("AgentSummaries") is not None:
        import capo_quicksight.types.agent_summaries

        out["agent_summaries"] = capo_quicksight.types.agent_summaries.deserialize_json(
            data["AgentSummaries"]
        )
    else:
        out["agent_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
