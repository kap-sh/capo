"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListFlowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_summaries
    import capo_bedrock_agent.types.next_token


class ListFlowsResponse(TypedDict, closed=True):
    flow_summaries: "capo_bedrock_agent.types.flow_summaries.FlowSummaries"
    """<p>A list, each member of which contains information about a flow.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.flow_summaries

    out["flowSummaries"] = capo_bedrock_agent.types.flow_summaries.serialize_json(
        value["flow_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowsResponse:
    out: ListFlowsResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowSummaries") is not None:
        import capo_bedrock_agent.types.flow_summaries

        out["flow_summaries"] = (
            capo_bedrock_agent.types.flow_summaries.deserialize_json(
                data["flowSummaries"]
            )
        )
    else:
        out["flow_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
