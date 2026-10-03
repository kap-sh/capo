"""Generated from Smithy shape ``com.amazonaws.wafv2#PutPermissionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.policy_string
    import capo_wafv2.types.resource_arn


class PutPermissionPolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the <a>RuleGroup</a> to which you want to attach the policy.</p>"""
    policy: "capo_wafv2.types.policy_string.PolicyString"
    """<p>The policy to attach to the specified rule group. </p> <p>The policy specifications must conform to the following:</p> <ul> <li> <p>The policy must be composed using IAM Policy version 2012-10-17.</p> </li> <li> <p>The policy must include specifications for <code>Effect</code>, <code>Action</code>, and <code>Principal</code>.</p> </li> <li> <p> <code>Effect</code> must specify <code>Allow</code>.</p> </li> <li> <p> <code>Action</code> must specify <code>wafv2:CreateWebACL</code>, <code>wafv2:UpdateWebACL</code>, and <code>wafv2:PutFirewallManagerRuleGroups</code> and may optionally specify <code>wafv2:GetRuleGroup</code>. WAF rejects any extra actions or wildcard actions in the policy.</p> </li> <li> <p>The policy must not include a <code>Resource</code> parameter.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html">IAM Policies</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPermissionPolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPermissionPolicyRequest:
    out: PutPermissionPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutPermissionPolicyRequest.resource_arn required")
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutPermissionPolicyRequest.policy required")
    return out
