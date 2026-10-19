"""Generated from Smithy shape ``com.amazonaws.ssmincidents#PutResourcePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.policy_id


class PutResourcePolicyOutput(TypedDict, closed=True):
    policy_id: "capo_ssm_incidents.types.policy_id.PolicyId"
    """<p>The ID of the resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyOutput) -> dict:
    out: dict = {}
    out["policyId"] = value["policy_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyOutput:
    out: PutResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        out["policy_id"] = ""
    return out
