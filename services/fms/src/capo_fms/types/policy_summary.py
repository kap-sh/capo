"""Generated from Smithy shape ``com.amazonaws.fms#PolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.customer_policy_status
    import capo_fms.types.policy_id
    import capo_fms.types.resource_arn
    import capo_fms.types.resource_name
    import capo_fms.types.resource_type
    import capo_fms.types.security_service_type


class PolicySummary(TypedDict, closed=True):
    policy_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the specified policy.</p>"""
    policy_id: NotRequired["capo_fms.types.policy_id.PolicyId"]
    """<p>The ID of the specified policy.</p>"""
    policy_name: NotRequired["capo_fms.types.resource_name.ResourceName"]
    """<p>The name of the specified policy.</p>"""
    resource_type: NotRequired["capo_fms.types.resource_type.ResourceType"]
    """<p>The type of resource protected by or in scope of the policy. This is in the format shown in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services Resource Types Reference</a>. </p>"""
    security_service_type: NotRequired[
        "capo_fms.types.security_service_type.SecurityServiceType"
    ]
    """<p>The service that the policy is using to protect the resources. This specifies the type of policy that is created, either an WAF policy, a Shield Advanced policy, or a security group policy.</p>"""
    remediation_enabled: "capo_fms.types.boolean.Boolean"
    """<p>Indicates if the policy should be automatically applied to new resources.</p>"""
    delete_unused_fm_managed_resources: "capo_fms.types.boolean.Boolean"
    """<p>Indicates whether Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope. </p> <p>By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources. </p> <p>This option is not available for Shield Advanced or WAF Classic policies.</p>"""
    policy_status: NotRequired[
        "capo_fms.types.customer_policy_status.CustomerPolicyStatus"
    ]
    """<p>Indicates whether the policy is in or out of an admin's policy or Region scope.</p> <ul> <li> <p> <code>ACTIVE</code> - The administrator can manage and delete the policy.</p> </li> <li> <p> <code>OUT_OF_ADMIN_SCOPE</code> - The administrator can view the policy, but they can't edit or delete the policy. Existing policy protections stay in place. Any new resources that come into scope of the policy won't be protected.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicySummary) -> dict:
    out: dict = {}
    if "policy_arn" in value:
        out["PolicyArn"] = value["policy_arn"]
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "security_service_type" in value:
        import capo_fms.types.security_service_type

        out["SecurityServiceType"] = (
            capo_fms.types.security_service_type.serialize_aws_json_1_1(
                value["security_service_type"]
            )
        )
    out["RemediationEnabled"] = value.get("remediation_enabled", False)
    out["DeleteUnusedFMManagedResources"] = value.get(
        "delete_unused_fm_managed_resources", False
    )
    if "policy_status" in value:
        import capo_fms.types.customer_policy_status

        out["PolicyStatus"] = (
            capo_fms.types.customer_policy_status.serialize_aws_json_1_1(
                value["policy_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicySummary:
    out: PolicySummary = {}  # type: ignore[typeddict-item]
    if data.get("PolicyArn") is not None:
        out["policy_arn"] = data["PolicyArn"]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("SecurityServiceType") is not None:
        import capo_fms.types.security_service_type

        out["security_service_type"] = (
            capo_fms.types.security_service_type.deserialize_aws_json_1_1(
                data["SecurityServiceType"]
            )
        )
    if data.get("RemediationEnabled") is not None:
        out["remediation_enabled"] = data["RemediationEnabled"]
    else:
        out["remediation_enabled"] = False
    if data.get("DeleteUnusedFMManagedResources") is not None:
        out["delete_unused_fm_managed_resources"] = data[
            "DeleteUnusedFMManagedResources"
        ]
    else:
        out["delete_unused_fm_managed_resources"] = False
    if data.get("PolicyStatus") is not None:
        import capo_fms.types.customer_policy_status

        out["policy_status"] = (
            capo_fms.types.customer_policy_status.deserialize_aws_json_1_1(
                data["PolicyStatus"]
            )
        )
    return out
