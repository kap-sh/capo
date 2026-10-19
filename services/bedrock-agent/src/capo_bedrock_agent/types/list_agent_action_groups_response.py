"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentActionGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.action_group_summaries
    import capo_bedrock_agent.types.next_token


class ListAgentActionGroupsResponse(TypedDict, closed=True):
    action_group_summaries: (
        "capo_bedrock_agent.types.action_group_summaries.ActionGroupSummaries"
    )
    """<p>A list of objects, each of which contains information about an action group.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentActionGroupsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.action_group_summaries

    out["actionGroupSummaries"] = (
        capo_bedrock_agent.types.action_group_summaries.serialize_json(
            value["action_group_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentActionGroupsResponse:
    out: ListAgentActionGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("actionGroupSummaries") is not None:
        import capo_bedrock_agent.types.action_group_summaries

        out["action_group_summaries"] = (
            capo_bedrock_agent.types.action_group_summaries.deserialize_json(
                data["actionGroupSummaries"]
            )
        )
    else:
        out["action_group_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
