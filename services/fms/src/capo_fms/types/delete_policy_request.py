"""Generated from Smithy shape ``com.amazonaws.fms#DeletePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.policy_id


class DeletePolicyRequest(TypedDict, closed=True):
    policy_id: "capo_fms.types.policy_id.PolicyId"
    """<p>The ID of the policy that you want to delete. You can retrieve this ID from <code>PutPolicy</code> and <code>ListPolicies</code>.</p>"""
    delete_all_policy_resources: NotRequired["capo_fms.types.boolean.Boolean"]
    """<p>If <code>True</code>, the request performs cleanup according to the policy type. </p> <p>For WAF and Shield Advanced policies, the cleanup does the following:</p> <ul> <li> <p>Deletes rule groups created by Firewall Manager</p> </li> <li> <p>Removes web ACLs from in-scope resources</p> </li> <li> <p>Deletes web ACLs that contain no rules or rule groups</p> </li> </ul> <p>For security group policies, the cleanup does the following for each security group in the policy:</p> <ul> <li> <p>Disassociates the security group from in-scope resources </p> </li> <li> <p>Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy</p> </li> </ul> <note> <p>For security group common policies, even if set to <code>False</code>, Firewall Manager deletes all security groups created by Firewall Manager that aren't associated with any other resources through another policy.</p> </note> <p>After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    if "delete_all_policy_resources" in value:
        out["DeleteAllPolicyResources"] = value["delete_all_policy_resources"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePolicyRequest:
    out: DeletePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        out["policy_id"] = ""
    if data.get("DeleteAllPolicyResources") is not None:
        out["delete_all_policy_resources"] = data["DeleteAllPolicyResources"]
    return out
