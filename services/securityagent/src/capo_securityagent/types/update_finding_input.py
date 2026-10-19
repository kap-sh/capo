"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateFindingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.finding_status
    import capo_securityagent.types.risk_level


class UpdateFindingInput(TypedDict, closed=True):
    finding_id: "str"
    """<p>The unique identifier of the finding to update.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the finding.</p>"""
    name: NotRequired["str"]
    """<p>The updated name for the finding.</p>"""
    description: NotRequired["str"]
    """<p>The updated description for the finding.</p>"""
    risk_type: NotRequired["str"]
    """<p>The updated risk type for the finding.</p>"""
    risk_level: NotRequired["capo_securityagent.types.risk_level.RiskLevel"]
    """<p>The updated risk level for the finding.</p>"""
    risk_score: NotRequired["str"]
    """<p>The updated numerical risk score for the finding.</p>"""
    attack_script: NotRequired["str"]
    """<p>The updated attack script for the finding.</p>"""
    reasoning: NotRequired["str"]
    """<p>The updated reasoning for the finding.</p>"""
    status: NotRequired["capo_securityagent.types.finding_status.FindingStatus"]
    """<p>The updated status for the finding.</p>"""
    customer_note: NotRequired["str"]
    """<p>A customer-provided note on the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFindingInput) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "risk_type" in value:
        out["riskType"] = value["risk_type"]
    if "risk_level" in value:
        import capo_securityagent.types.risk_level

        out["riskLevel"] = capo_securityagent.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "risk_score" in value:
        out["riskScore"] = value["risk_score"]
    if "attack_script" in value:
        out["attackScript"] = value["attack_script"]
    if "reasoning" in value:
        out["reasoning"] = value["reasoning"]
    if "status" in value:
        import capo_securityagent.types.finding_status

        out["status"] = capo_securityagent.types.finding_status.serialize_json(
            value["status"]
        )
    if "customer_note" in value:
        out["customerNote"] = value["customer_note"]
    return out


def deserialize_json(data: dict) -> UpdateFindingInput:
    out: UpdateFindingInput = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("riskType") is not None:
        out["risk_type"] = data["riskType"]
    if data.get("riskLevel") is not None:
        import capo_securityagent.types.risk_level

        out["risk_level"] = capo_securityagent.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if data.get("riskScore") is not None:
        out["risk_score"] = data["riskScore"]
    if data.get("attackScript") is not None:
        out["attack_script"] = data["attackScript"]
    if data.get("reasoning") is not None:
        out["reasoning"] = data["reasoning"]
    if data.get("status") is not None:
        import capo_securityagent.types.finding_status

        out["status"] = capo_securityagent.types.finding_status.deserialize_json(
            data["status"]
        )
    if data.get("customerNote") is not None:
        out["customer_note"] = data["customerNote"]
    return out
