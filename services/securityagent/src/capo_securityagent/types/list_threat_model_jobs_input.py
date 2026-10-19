"""Generated from Smithy shape ``com.amazonaws.securityagent#ListThreatModelJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token


class ListThreatModelJobsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    threat_model_id: "str"
    """<p>The unique identifier of the threat model to list jobs for.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThreatModelJobsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    out["threatModelId"] = value["threat_model_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThreatModelJobsInput:
    out: ListThreatModelJobsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("threatModelId") is not None:
        out["threat_model_id"] = data["threatModelId"]
    else:
        out["threat_model_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
