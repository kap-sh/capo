"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListFlowAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_alias_summaries
    import capo_bedrock_agent.types.next_token


class ListFlowAliasesResponse(TypedDict, closed=True):
    flow_alias_summaries: (
        "capo_bedrock_agent.types.flow_alias_summaries.FlowAliasSummaries"
    )
    """<p>A list, each member of which contains information about an alias.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowAliasesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.flow_alias_summaries

    out["flowAliasSummaries"] = (
        capo_bedrock_agent.types.flow_alias_summaries.serialize_json(
            value["flow_alias_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowAliasesResponse:
    out: ListFlowAliasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("flowAliasSummaries") is not None:
        import capo_bedrock_agent.types.flow_alias_summaries

        out["flow_alias_summaries"] = (
            capo_bedrock_agent.types.flow_alias_summaries.deserialize_json(
                data["flowAliasSummaries"]
            )
        )
    else:
        out["flow_alias_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
