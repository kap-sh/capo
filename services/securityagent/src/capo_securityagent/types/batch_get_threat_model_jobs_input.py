"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetThreatModelJobsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_job_id_list


class BatchGetThreatModelJobsInput(TypedDict, closed=True):
    threat_model_job_ids: (
        "capo_securityagent.types.threat_model_job_id_list.ThreatModelJobIdList"
    )
    """<p>The list of threat model job identifiers to retrieve.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the threat model jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetThreatModelJobsInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.threat_model_job_id_list

    out["threatModelJobIds"] = (
        capo_securityagent.types.threat_model_job_id_list.serialize_json(
            value["threat_model_job_ids"]
        )
    )
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> BatchGetThreatModelJobsInput:
    out: BatchGetThreatModelJobsInput = {}  # type: ignore[typeddict-item]
    if data.get("threatModelJobIds") is not None:
        import capo_securityagent.types.threat_model_job_id_list

        out["threat_model_job_ids"] = (
            capo_securityagent.types.threat_model_job_id_list.deserialize_json(
                data["threatModelJobIds"]
            )
        )
    else:
        out["threat_model_job_ids"] = []
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    return out
