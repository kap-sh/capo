"""Generated from Smithy shape ``com.amazonaws.securityagent#ListThreatModelsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token


class ListThreatModelsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space to list threat models for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThreatModelsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> ListThreatModelsInput:
    out: ListThreatModelsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    return out
