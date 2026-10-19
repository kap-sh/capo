"""Generated from Smithy shape ``com.amazonaws.wafv2#DeleteFirewallManagerRuleGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.lock_token
    import capo_wafv2.types.resource_arn


class DeleteFirewallManagerRuleGroupsRequest(TypedDict, closed=True):
    web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL.</p>"""
    web_acl_lock_token: "capo_wafv2.types.lock_token.LockToken"
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallManagerRuleGroupsRequest) -> dict:
    out: dict = {}
    out["WebACLArn"] = value["web_acl_arn"]
    out["WebACLLockToken"] = value["web_acl_lock_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFirewallManagerRuleGroupsRequest:
    out: DeleteFirewallManagerRuleGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebACLArn") is not None:
        out["web_acl_arn"] = data["WebACLArn"]
    else:
        out["web_acl_arn"] = ""
    if data.get("WebACLLockToken") is not None:
        out["web_acl_lock_token"] = data["WebACLLockToken"]
    else:
        out["web_acl_lock_token"] = ""
    return out
