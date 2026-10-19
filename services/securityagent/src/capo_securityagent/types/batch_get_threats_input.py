"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetThreatsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.threat_id_list


class BatchGetThreatsInput(TypedDict, closed=True):
    threat_ids: "capo_securityagent.types.threat_id_list.ThreatIdList"
    """<p>The list of threat identifiers to retrieve.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetThreatsInput) -> dict:
    out: dict = {}
    import capo_securityagent.types.threat_id_list

    out["threatIds"] = capo_securityagent.types.threat_id_list.serialize_json(
        value["threat_ids"]
    )
    out["agentSpaceId"] = value["agent_space_id"]
    return out


def deserialize_json(data: dict) -> BatchGetThreatsInput:
    out: BatchGetThreatsInput = {}  # type: ignore[typeddict-item]
    if data.get("threatIds") is not None:
        import capo_securityagent.types.threat_id_list

        out["threat_ids"] = capo_securityagent.types.threat_id_list.deserialize_json(
            data["threatIds"]
        )
    else:
        out["threat_ids"] = []
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    return out
