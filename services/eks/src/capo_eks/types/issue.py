"""Generated from Smithy shape ``com.amazonaws.eks#Issue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.nodegroup_issue_code
    import capo_eks.types.string
    import capo_eks.types.string_list


class Issue(TypedDict, closed=True):
    code: NotRequired["capo_eks.types.nodegroup_issue_code.NodegroupIssueCode"]
    """<p>A brief description of the error.</p> <ul> <li> <p> <b>AccessDenied</b>: Amazon EKS or one or more of your managed nodes is failing to authenticate or authorize with your Kubernetes cluster API server.</p> </li> <li> <p> <b>AsgInstanceLaunchFailures</b>: Your Auto Scaling group is experiencing failures while attempting to launch instances.</p> </li> <li> <p> <b>AutoScalingGroupNotFound</b>: We couldn't find the Auto Scaling group associated with the managed node group. You may be able to recreate an Auto Scaling group with the same settings to recover.</p> </li> <li> <p> <b>ClusterUnreachable</b>: Amazon EKS or one or more of your managed nodes is unable to to communicate with your Kubernetes cluster API server. This can happen if there are network disruptions or if API servers are timing out processing requests. </p> </li> <li> <p> <b>Ec2InstanceTypeDoesNotExist</b>: One or more of the supplied Amazon EC2 instance types do not exist. Amazon EKS checked for the instance types that you provided in this Amazon Web Services Region, and one or more aren't available.</p> </li> <li> <p> <b>Ec2LaunchTemplateNotFound</b>: We couldn't find the Amazon EC2 launch template for your managed node group. You may be able to recreate a launch template with the same settings to recover.</p> </li> <li> <p> <b>Ec2LaunchTemplateVersionMismatch</b>: The Amazon EC2 launch template version for your managed node group does not match the version that Amazon EKS created. You may be able to revert to the version that Amazon EKS created to recover.</p> </li> <li> <p> <b>Ec2SecurityGroupDeletionFailure</b>: We could not delete the remote access security group for your managed node group. Remove any dependencies from the security group.</p> </li> <li> <p> <b>Ec2SecurityGroupNotFound</b>: We couldn't find the cluster security group for the cluster. You must recreate your cluster.</p> </li> <li> <p> <b>Ec2SubnetInvalidConfiguration</b>: One or more Amazon EC2 subnets specified for a node group do not automatically assign public IP addresses to instances launched into it. If you want your instances to be assigned a public IP address, then you need to enable the <code>auto-assign public IP address</code> setting for the subnet. See <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#subnet-public-ip">Modifying the public <code>IPv4</code> addressing attribute for your subnet</a> in the <i>Amazon VPC User Guide</i>.</p> </li> <li> <p> <b>IamInstanceProfileNotFound</b>: We couldn't find the IAM instance profile for your managed node group. You may be able to recreate an instance profile with the same settings to recover.</p> </li> <li> <p> <b>IamNodeRoleNotFound</b>: We couldn't find the IAM role for your managed node group. You may be able to recreate an IAM role with the same settings to recover.</p> </li> <li> <p> <b>InstanceLimitExceeded</b>: Your Amazon Web Services account is unable to launch any more instances of the specified instance type. You may be able to request an Amazon EC2 instance limit increase to recover.</p> </li> <li> <p> <b>InsufficientFreeAddresses</b>: One or more of the subnets associated with your managed node group does not have enough available IP addresses for new nodes.</p> </li> <li> <p> <b>InternalFailure</b>: These errors are usually caused by an Amazon EKS server-side issue.</p> </li> <li> <p> <b>NodeCreationFailure</b>: Your launched instances are unable to register with your Amazon EKS cluster. Common causes of this failure are insufficient <a href="https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html">node IAM role</a> permissions or lack of outbound internet access for the nodes. </p> </li> </ul>"""
    message: NotRequired["capo_eks.types.string.String"]
    """<p>The error message associated with the issue.</p>"""
    resource_ids: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The Amazon Web Services resources that are afflicted by this issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Issue) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_eks.types.nodegroup_issue_code

        out["code"] = capo_eks.types.nodegroup_issue_code.serialize_json(value["code"])
    if "message" in value:
        out["message"] = value["message"]
    if "resource_ids" in value:
        import capo_eks.types.string_list

        out["resourceIds"] = capo_eks.types.string_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> Issue:
    out: Issue = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_eks.types.nodegroup_issue_code

        out["code"] = capo_eks.types.nodegroup_issue_code.deserialize_json(data["code"])
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceIds") is not None:
        import capo_eks.types.string_list

        out["resource_ids"] = capo_eks.types.string_list.deserialize_json(
            data["resourceIds"]
        )
    return out
