"""Generated from Smithy shape ``com.amazonaws.dsql#PutClusterPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.policy_version


class PutClusterPolicyOutput(TypedDict, closed=True):
    policy_version: "capo_dsql.types.policy_version.PolicyVersion"
    """<p>The version of the policy after it has been updated or created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutClusterPolicyOutput) -> dict:
    out: dict = {}
    out["policyVersion"] = value["policy_version"]
    return out


def deserialize_json(data: dict) -> PutClusterPolicyOutput:
    out: PutClusterPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyVersion") is not None:
        out["policy_version"] = data["policyVersion"]
    else:
        out["policy_version"] = ""
    return out
