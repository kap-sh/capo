"""Generated from Smithy shape ``com.amazonaws.securityagent#DiscoveredEndpoint``."""

from typing_extensions import NotRequired, TypedDict


class DiscoveredEndpoint(TypedDict, closed=True):
    uri: "str"
    """<p>The URI of the discovered endpoint.</p>"""
    pentest_job_id: "str"
    """<p>The unique identifier of the pentest job that discovered the endpoint.</p>"""
    task_id: "str"
    """<p>The unique identifier of the task that discovered the endpoint.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space associated with the discovered endpoint.</p>"""
    evidence: NotRequired["str"]
    """<p>The evidence that led to the discovery of the endpoint.</p>"""
    operation: NotRequired["str"]
    """<p>The HTTP operation associated with the discovered endpoint.</p>"""
    description: NotRequired["str"]
    """<p>A description of the discovered endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredEndpoint) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    out["pentestJobId"] = value["pentest_job_id"]
    out["taskId"] = value["task_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "evidence" in value:
        out["evidence"] = value["evidence"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> DiscoveredEndpoint:
    out: DiscoveredEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    if data.get("pentestJobId") is not None:
        out["pentest_job_id"] = data["pentestJobId"]
    else:
        out["pentest_job_id"] = ""
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("evidence") is not None:
        out["evidence"] = data["evidence"]
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
