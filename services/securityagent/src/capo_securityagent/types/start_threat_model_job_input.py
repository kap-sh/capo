"""Generated from Smithy shape ``com.amazonaws.securityagent#StartThreatModelJobInput``."""

from typing_extensions import TypedDict


class StartThreatModelJobInput(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""
    threat_model_id: "str"
    """<p>The unique identifier of the threat model to start a job for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartThreatModelJobInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["threatModelId"] = value["threat_model_id"]
    return out


def deserialize_json(data: dict) -> StartThreatModelJobInput:
    out: StartThreatModelJobInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("threatModelId") is not None:
        out["threat_model_id"] = data["threatModelId"]
    else:
        out["threat_model_id"] = ""
    return out
