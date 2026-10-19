"""Generated from Smithy shape ``com.amazonaws.dsql#PutClusterPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.bypass_policy_lockout_safety_check
    import capo_dsql.types.client_token
    import capo_dsql.types.cluster_id
    import capo_dsql.types.policy_document
    import capo_dsql.types.policy_version


class PutClusterPolicyInput(TypedDict, closed=True):
    identifier: "capo_dsql.types.cluster_id.ClusterId"
    policy: "capo_dsql.types.policy_document.PolicyDocument"
    """<p>The resource-based policy document to attach to the cluster. This should be a valid JSON policy document that defines permissions and conditions.</p>"""
    bypass_policy_lockout_safety_check: NotRequired[
        "capo_dsql.types.bypass_policy_lockout_safety_check.BypassPolicyLockoutSafetyCheck"
    ]
    """<p>A flag that allows you to bypass the policy lockout safety check. When set to true, this parameter allows you to apply a policy that might lock you out of the cluster. Use with caution.</p>"""
    expected_policy_version: NotRequired["capo_dsql.types.policy_version.PolicyVersion"]
    """<p>The expected version of the current policy. This parameter ensures that you're updating the correct version of the policy and helps prevent concurrent modification conflicts.</p>"""
    client_token: NotRequired["capo_dsql.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: PutClusterPolicyInput) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    if "bypass_policy_lockout_safety_check" in value:
        out["bypassPolicyLockoutSafetyCheck"] = value[
            "bypass_policy_lockout_safety_check"
        ]
    if "expected_policy_version" in value:
        out["expectedPolicyVersion"] = value["expected_policy_version"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutClusterPolicyInput:
    out: PutClusterPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("bypassPolicyLockoutSafetyCheck") is not None:
        out["bypass_policy_lockout_safety_check"] = data[
            "bypassPolicyLockoutSafetyCheck"
        ]
    if data.get("expectedPolicyVersion") is not None:
        out["expected_policy_version"] = data["expectedPolicyVersion"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
