"""Generated from Smithy shape ``com.amazonaws.fms#GetViolationDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.policy_id
    import capo_fms.types.resource_id
    import capo_fms.types.resource_type


class GetViolationDetailsRequest(TypedDict, closed=True):
    policy_id: "capo_fms.types.policy_id.PolicyId"
    """<p>The ID of the Firewall Manager policy that you want the details for. You can get violation details for the following policy types:</p> <ul> <li> <p>WAF</p> </li> <li> <p>DNS Firewall</p> </li> <li> <p>Imported Network Firewall</p> </li> <li> <p>Network Firewall</p> </li> <li> <p>Security group content audit</p> </li> <li> <p>Network ACL</p> </li> <li> <p>Third-party firewall</p> </li> </ul>"""
    member_account: "capo_fms.types.aws_account_id.AWSAccountId"
    """<p>The Amazon Web Services account ID that you want the details for.</p>"""
    resource_id: "capo_fms.types.resource_id.ResourceId"
    """<p>The ID of the resource that has violations.</p>"""
    resource_type: "capo_fms.types.resource_type.ResourceType"
    """<p>The resource type. This is in the format shown in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services Resource Types Reference</a>. Supported resource types are: <code>AWS::WAFv2::WebACL</code>, <code>AWS::EC2::Instance</code>, <code>AWS::EC2::NetworkInterface</code>, <code>AWS::EC2::SecurityGroup</code>, <code>AWS::NetworkFirewall::FirewallPolicy</code>, and <code>AWS::EC2::Subnet</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetViolationDetailsRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    out["MemberAccount"] = value["member_account"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetViolationDetailsRequest:
    out: GetViolationDetailsRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("GetViolationDetailsRequest.policy_id required")
    if data.get("MemberAccount") is not None:
        out["member_account"] = data["MemberAccount"]
    else:
        raise DeserializationError("GetViolationDetailsRequest.member_account required")
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("GetViolationDetailsRequest.resource_id required")
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("GetViolationDetailsRequest.resource_type required")
    return out
