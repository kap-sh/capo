"""Generated from Smithy shape ``com.amazonaws.securityagent#ListActorMessagesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token


class ListActorMessagesInput(TypedDict, closed=True):
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that owns the pentest.</p>"""
    pentest_id: "str"
    """<p>The unique identifier of the pentest that the actor belongs to.</p>"""
    actor_identifier: "str"
    """<p>The identifier of the actor whose messages to list. The identifier is case-insensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActorMessagesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["agentSpaceId"] = value["agent_space_id"]
    out["pentestId"] = value["pentest_id"]
    out["actorIdentifier"] = value["actor_identifier"]
    return out


def deserialize_json(data: dict) -> ListActorMessagesInput:
    out: ListActorMessagesInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("pentestId") is not None:
        out["pentest_id"] = data["pentestId"]
    else:
        out["pentest_id"] = ""
    if data.get("actorIdentifier") is not None:
        out["actor_identifier"] = data["actorIdentifier"]
    else:
        out["actor_identifier"] = ""
    return out
