"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetThreatModelsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.threat_model_id_list


class BatchGetThreatModelsInput(TypedDict, closed=True):
    threat_model_ids: "capo_securityagent.types.threat_model_id_list.ThreatModelIdList"
    """<p>The list of threat model identifiers to retrieve.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the threat models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetThreatModelsInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.threat_model_id_list

    out["threatModelIds"] = (
        capo_securityagent.types.threat_model_id_list.serialize_json(
            value["threat_model_ids"]
        )
    )
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> BatchGetThreatModelsInput:
    out: BatchGetThreatModelsInput = {}  # type: ignore[typeddict-item]
    if data.get("threatModelIds") is not None:
        import capo_securityagent.types.threat_model_id_list

        out["threat_model_ids"] = (
            capo_securityagent.types.threat_model_id_list.deserialize_json(
                data["threatModelIds"]
            )
        )
    else:
        out["threat_model_ids"] = []
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    return out
