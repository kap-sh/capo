"""Generated from Smithy shape ``com.amazonaws.wafregional#PutPermissionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.policy_string
    import capo_waf_regional.types.resource_arn


class PutPermissionPolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_waf_regional.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the RuleGroup to which you want to attach the policy.</p>"""
    policy: "capo_waf_regional.types.policy_string.PolicyString"
    """<p>The policy to attach to the specified RuleGroup.</p>"""


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
        out["resource_arn"] = ""
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out
