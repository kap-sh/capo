"""Generated from Smithy shape ``com.amazonaws.dsql#GetClusterPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.policy_document
    import capo_dsql.types.policy_version


class GetClusterPolicyOutput(TypedDict, closed=True):
    policy: "capo_dsql.types.policy_document.PolicyDocument"
    """<p>The resource-based policy document attached to the cluster, returned as a JSON string.</p>"""
    policy_version: "capo_dsql.types.policy_version.PolicyVersion"
    """<p>The version of the policy document. This version number is incremented each time the policy is updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterPolicyOutput) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    out["policyVersion"] = value["policy_version"]
    return out


def deserialize_json(data: dict) -> GetClusterPolicyOutput:
    out: GetClusterPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("policyVersion") is not None:
        out["policy_version"] = data["policyVersion"]
    else:
        out["policy_version"] = ""
    return out
