"""Generated from Smithy shape ``com.amazonaws.eks#RemoteAccessConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.string_list


class RemoteAccessConfig(TypedDict, closed=True):
    ec2_ssh_key: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon EC2 SSH key name that provides access for SSH communication with the nodes in the managed node group. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html">Amazon EC2 key pairs and Linux instances</a> in the <i>Amazon Elastic Compute Cloud User Guide for Linux Instances</i>. For Windows, an Amazon EC2 SSH key is used to obtain the RDP password. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-key-pairs.html">Amazon EC2 key pairs and Windows instances</a> in the <i>Amazon Elastic Compute Cloud User Guide for Windows Instances</i>.</p>"""
    source_security_groups: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The security group IDs that are allowed SSH access (port 22) to the nodes. For Windows, the port is 3389. If you specify an Amazon EC2 SSH key but don't specify a source security group when you create a managed node group, then the port on the nodes is opened to the internet (<code>0.0.0.0/0</code>). For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html">Security Groups for Your VPC</a> in the <i>Amazon Virtual Private Cloud User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAccessConfig) -> dict:
    out: dict = {}
    if "ec2_ssh_key" in value:
        out["ec2SshKey"] = value["ec2_ssh_key"]
    if "source_security_groups" in value:
        import capo_eks.types.string_list

        out["sourceSecurityGroups"] = capo_eks.types.string_list.serialize_json(
            value["source_security_groups"]
        )
    return out


def deserialize_json(data: dict) -> RemoteAccessConfig:
    out: RemoteAccessConfig = {}  # type: ignore[typeddict-item]
    if data.get("ec2SshKey") is not None:
        out["ec2_ssh_key"] = data["ec2SshKey"]
    if data.get("sourceSecurityGroups") is not None:
        import capo_eks.types.string_list

        out["source_security_groups"] = capo_eks.types.string_list.deserialize_json(
            data["sourceSecurityGroups"]
        )
    return out
