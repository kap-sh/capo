"""Generated from Smithy shape ``com.amazonaws.aiops#PutInvestigationGroupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_aiops.types.investigation_group_identifier
    import capo_aiops.types.investigation_group_policy_document


class PutInvestigationGroupPolicyRequest(TypedDict, closed=True):
    identifier: (
        "capo_aiops.types.investigation_group_identifier.InvestigationGroupIdentifier"
    )
    """<p>Specify either the name or the ARN of the investigation group that you want to assign the policy to.</p>"""
    policy: "capo_aiops.types.investigation_group_policy_document.InvestigationGroupPolicyDocument"
    """<p>The policy, in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutInvestigationGroupPolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutInvestigationGroupPolicyRequest:
    out: PutInvestigationGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    return out
