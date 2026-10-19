"""Generated from Smithy shape ``com.amazonaws.securityagent#ListDiscoveredEndpointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token


class ListDiscoveredEndpointsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    pentest_job_id: "str"
    """<p>The unique identifier of the pentest job to list discovered endpoints for.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    prefix: NotRequired["str"]
    """<p>A prefix to filter discovered endpoints by URI.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoveredEndpointsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    out["pentestJobId"] = value["pentest_job_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDiscoveredEndpointsInput:
    out: ListDiscoveredEndpointsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("pentestJobId") is not None:
        out["pentest_job_id"] = data["pentestJobId"]
    else:
        out["pentest_job_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
