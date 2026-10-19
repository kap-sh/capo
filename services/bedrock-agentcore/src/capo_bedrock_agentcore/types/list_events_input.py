"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.actor_id
    import capo_bedrock_agentcore.types.filter_input
    import capo_bedrock_agentcore.types.max_results
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.pagination_token
    import capo_bedrock_agentcore.types.session_id


class ListEventsInput(TypedDict, closed=True):
    memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId"
    """<p>The identifier of the AgentCore Memory resource for which to list events.</p>"""
    session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The identifier of the session for which to list events.</p>"""
    actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor for which to list events.</p>"""
    include_payloads: NotRequired["bool"]
    """<p>Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.</p>"""
    filter: NotRequired["capo_bedrock_agentcore.types.filter_input.FilterInput"]
    """<p>Filter criteria to apply when listing events.</p>"""
    max_results: NotRequired["capo_bedrock_agentcore.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. The default value is 20.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventsInput) -> dict:
    out: dict = {}
    if "include_payloads" in value:
        out["includePayloads"] = value["include_payloads"]
    if "filter" in value:
        import capo_bedrock_agentcore.types.filter_input

        out["filter"] = capo_bedrock_agentcore.types.filter_input.serialize_json(
            value["filter"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventsInput:
    out: ListEventsInput = {}  # type: ignore[typeddict-item]
    if data.get("includePayloads") is not None:
        out["include_payloads"] = data["includePayloads"]
    if data.get("filter") is not None:
        import capo_bedrock_agentcore.types.filter_input

        out["filter"] = capo_bedrock_agentcore.types.filter_input.deserialize_json(
            data["filter"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
