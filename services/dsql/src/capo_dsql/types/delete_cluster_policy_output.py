"""Generated from Smithy shape ``com.amazonaws.dsql#DeleteClusterPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.policy_version


class DeleteClusterPolicyOutput(TypedDict, closed=True):
    policy_version: "capo_dsql.types.policy_version.PolicyVersion"
    """<p>The version of the policy that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterPolicyOutput) -> dict:
    out: dict = {}
    out["policyVersion"] = value["policy_version"]
    return out


def deserialize_json(data: dict) -> DeleteClusterPolicyOutput:
    out: DeleteClusterPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyVersion") is not None:
        out["policy_version"] = data["policyVersion"]
    else:
        out["policy_version"] = ""
    return out
