"""Generated from Smithy shape ``com.amazonaws.securityagent#StopThreatModelJobInput``."""

from typing_extensions import TypedDict


class StopThreatModelJobInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    threat_model_job_id: "str"
    """<p>The unique identifier of the threat model job to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopThreatModelJobInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["threatModelJobId"] = value["threat_model_job_id"]
    return out


def deserialize_json(data: dict) -> StopThreatModelJobInput:
    out: StopThreatModelJobInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("threatModelJobId") is not None:
        out["threat_model_job_id"] = data["threatModelJobId"]
    else:
        out["threat_model_job_id"] = ""
    return out
