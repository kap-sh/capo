"""Generated from Smithy shape ``com.amazonaws.eks#CreateNodegroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.ami_types
    import capo_eks.types.boxed_integer
    import capo_eks.types.capacity_types
    import capo_eks.types.labels_map
    import capo_eks.types.launch_template_specification
    import capo_eks.types.node_repair_config
    import capo_eks.types.nodegroup_scaling_config
    import capo_eks.types.nodegroup_update_config
    import capo_eks.types.remote_access_config
    import capo_eks.types.string
    import capo_eks.types.string_list
    import capo_eks.types.tag_map
    import capo_eks.types.taints_list
    import capo_eks.types.warm_pool_config


class CreateNodegroupRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    nodegroup_name: "capo_eks.types.string.String"
    """<p>The unique name to give your node group.</p>"""
    scaling_config: NotRequired[
        "capo_eks.types.nodegroup_scaling_config.NodegroupScalingConfig"
    ]
    """<p>The scaling configuration details for the Auto Scaling group that is created for your node group.</p>"""
    disk_size: NotRequired["capo_eks.types.boxed_integer.BoxedInteger"]
    """<p>The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB for Linux and Bottlerocket. The default disk size is 50 GiB for Windows. If you specify <code>launchTemplate</code>, then don't specify <code>diskSize</code>, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    subnets: "capo_eks.types.string_list.StringList"
    """<p>The subnets to use for the Auto Scaling group that is created for your node group. If you specify <code>launchTemplate</code>, then don't specify <code> <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html">SubnetId</a> </code> in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    instance_types: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>Specify the instance types for a node group. If you specify a GPU instance type, make sure to also specify an applicable GPU AMI type with the <code>amiType</code> parameter. If you specify <code>launchTemplate</code>, then you can specify zero or one instance type in your launch template <i>or</i> you can specify 0-20 instance types for <code>instanceTypes</code>. If however, you specify an instance type in your launch template <i>and</i> specify any <code>instanceTypes</code>, the node group deployment will fail. If you don't specify an instance type in a launch template or for <code>instanceTypes</code>, then <code>t3.medium</code> is used, by default. If you specify <code>Spot</code> for <code>capacityType</code>, then we recommend specifying multiple values for <code>instanceTypes</code>. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html#managed-node-group-capacity-types">Managed node group capacity types</a> and <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    ami_type: NotRequired["capo_eks.types.ami_types.AMITypes"]
    """<p>The AMI type for your node group. If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>amiType</code>, or the node group deployment will fail. If your launch template uses a Windows custom AMI, then add <code>eks:kube-proxy-windows</code> to your Windows nodes <code>rolearn</code> in the <code>aws-auth</code> <code>ConfigMap</code>. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    remote_access: NotRequired["capo_eks.types.remote_access_config.RemoteAccessConfig"]
    """<p>The remote access configuration to use with your node group. For Linux, the protocol is SSH. For Windows, the protocol is RDP. If you specify <code>launchTemplate</code>, then don't specify <code>remoteAccess</code>, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    node_role: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with your node group. The Amazon EKS worker node <code>kubelet</code> daemon makes calls to Amazon Web Services APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch nodes and register them into a cluster, you must create an IAM role for those nodes to use when they are launched. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html">Amazon EKS node IAM role</a> in the <i> <i>Amazon EKS User Guide</i> </i>. If you specify <code>launchTemplate</code>, then don't specify <code> <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html">IamInstanceProfile</a> </code> in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    labels: NotRequired["capo_eks.types.labels_map.labelsMap"]
    """<p>The Kubernetes <code>labels</code> to apply to the nodes in the node group when they are created.</p>"""
    taints: NotRequired["capo_eks.types.taints_list.taintsList"]
    """<p>The Kubernetes taints to be applied to the nodes in the node group. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html">Node taints on managed node groups</a>.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    launch_template: NotRequired[
        "capo_eks.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>An object representing a node group's launch template specification. When using this object, don't directly specify <code>instanceTypes</code>, <code>diskSize</code>, or <code>remoteAccess</code>. You cannot later specify a different launch template ID or name than what was used to create the node group.</p> <p>Make sure that the launch template meets the requirements in <code>launchTemplateSpecification</code>. Also refer to <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    update_config: NotRequired[
        "capo_eks.types.nodegroup_update_config.NodegroupUpdateConfig"
    ]
    """<p>The node group update configuration.</p>"""
    node_repair_config: NotRequired[
        "capo_eks.types.node_repair_config.NodeRepairConfig"
    ]
    """<p>The node auto repair configuration for the node group.</p>"""
    capacity_type: NotRequired["capo_eks.types.capacity_types.CapacityTypes"]
    """<p>The capacity type for your node group.</p>"""
    version: NotRequired["capo_eks.types.string.String"]
    """<p>The Kubernetes version to use for your managed nodes. By default, the Kubernetes version of the cluster is used, and this is the only accepted specified value. If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>version</code>, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    release_version: NotRequired["capo_eks.types.string.String"]
    """<p>The AMI version of the Amazon EKS optimized AMI to use with your node group. By default, the latest available AMI version for the node group's current Kubernetes version is used. For information about Linux versions, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html">Amazon EKS optimized Amazon Linux AMI versions</a> in the <i>Amazon EKS User Guide</i>. Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html">Amazon EKS optimized Windows AMI versions</a> in the <i>Amazon EKS User Guide</i>.</p> <p>If you specify <code>launchTemplate</code>, and your launch template uses a custom AMI, then don't specify <code>releaseVersion</code>, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html">Customizing managed nodes with launch templates</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    warm_pool_config: NotRequired["capo_eks.types.warm_pool_config.WarmPoolConfig"]
    """<p>The warm pool configuration for the node group. Warm pools maintain pre-initialized EC2 instances that can quickly join your cluster during scale-out events, improving application scaling performance and reducing costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodegroupRequest) -> dict:
    out: dict = {}
    out["nodegroupName"] = value["nodegroup_name"]
    if "scaling_config" in value:
        import capo_eks.types.nodegroup_scaling_config

        out["scalingConfig"] = capo_eks.types.nodegroup_scaling_config.serialize_json(
            value["scaling_config"]
        )
    if "disk_size" in value:
        out["diskSize"] = value["disk_size"]
    import capo_eks.types.string_list

    out["subnets"] = capo_eks.types.string_list.serialize_json(value["subnets"])
    if "instance_types" in value:
        import capo_eks.types.string_list

        out["instanceTypes"] = capo_eks.types.string_list.serialize_json(
            value["instance_types"]
        )
    if "ami_type" in value:
        import capo_eks.types.ami_types

        out["amiType"] = capo_eks.types.ami_types.serialize_json(value["ami_type"])
    if "remote_access" in value:
        import capo_eks.types.remote_access_config

        out["remoteAccess"] = capo_eks.types.remote_access_config.serialize_json(
            value["remote_access"]
        )
    out["nodeRole"] = value["node_role"]
    if "labels" in value:
        import capo_eks.types.labels_map

        out["labels"] = capo_eks.types.labels_map.serialize_json(value["labels"])
    if "taints" in value:
        import capo_eks.types.taints_list

        out["taints"] = capo_eks.types.taints_list.serialize_json(value["taints"])
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "launch_template" in value:
        import capo_eks.types.launch_template_specification

        out["launchTemplate"] = (
            capo_eks.types.launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    if "update_config" in value:
        import capo_eks.types.nodegroup_update_config

        out["updateConfig"] = capo_eks.types.nodegroup_update_config.serialize_json(
            value["update_config"]
        )
    if "node_repair_config" in value:
        import capo_eks.types.node_repair_config

        out["nodeRepairConfig"] = capo_eks.types.node_repair_config.serialize_json(
            value["node_repair_config"]
        )
    if "capacity_type" in value:
        import capo_eks.types.capacity_types

        out["capacityType"] = capo_eks.types.capacity_types.serialize_json(
            value["capacity_type"]
        )
    if "version" in value:
        out["version"] = value["version"]
    if "release_version" in value:
        out["releaseVersion"] = value["release_version"]
    if "warm_pool_config" in value:
        import capo_eks.types.warm_pool_config

        out["warmPoolConfig"] = capo_eks.types.warm_pool_config.serialize_json(
            value["warm_pool_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateNodegroupRequest:
    out: CreateNodegroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("nodegroupName") is not None:
        out["nodegroup_name"] = data["nodegroupName"]
    else:
        raise DeserializationError("CreateNodegroupRequest.nodegroup_name required")
    if data.get("scalingConfig") is not None:
        import capo_eks.types.nodegroup_scaling_config

        out["scaling_config"] = (
            capo_eks.types.nodegroup_scaling_config.deserialize_json(
                data["scalingConfig"]
            )
        )
    if data.get("diskSize") is not None:
        out["disk_size"] = data["diskSize"]
    if data.get("subnets") is not None:
        import capo_eks.types.string_list

        out["subnets"] = capo_eks.types.string_list.deserialize_json(data["subnets"])
    else:
        raise DeserializationError("CreateNodegroupRequest.subnets required")
    if data.get("instanceTypes") is not None:
        import capo_eks.types.string_list

        out["instance_types"] = capo_eks.types.string_list.deserialize_json(
            data["instanceTypes"]
        )
    if data.get("amiType") is not None:
        import capo_eks.types.ami_types

        out["ami_type"] = capo_eks.types.ami_types.deserialize_json(data["amiType"])
    if data.get("remoteAccess") is not None:
        import capo_eks.types.remote_access_config

        out["remote_access"] = capo_eks.types.remote_access_config.deserialize_json(
            data["remoteAccess"]
        )
    if data.get("nodeRole") is not None:
        out["node_role"] = data["nodeRole"]
    else:
        raise DeserializationError("CreateNodegroupRequest.node_role required")
    if data.get("labels") is not None:
        import capo_eks.types.labels_map

        out["labels"] = capo_eks.types.labels_map.deserialize_json(data["labels"])
    if data.get("taints") is not None:
        import capo_eks.types.taints_list

        out["taints"] = capo_eks.types.taints_list.deserialize_json(data["taints"])
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("launchTemplate") is not None:
        import capo_eks.types.launch_template_specification

        out["launch_template"] = (
            capo_eks.types.launch_template_specification.deserialize_json(
                data["launchTemplate"]
            )
        )
    if data.get("updateConfig") is not None:
        import capo_eks.types.nodegroup_update_config

        out["update_config"] = capo_eks.types.nodegroup_update_config.deserialize_json(
            data["updateConfig"]
        )
    if data.get("nodeRepairConfig") is not None:
        import capo_eks.types.node_repair_config

        out["node_repair_config"] = capo_eks.types.node_repair_config.deserialize_json(
            data["nodeRepairConfig"]
        )
    if data.get("capacityType") is not None:
        import capo_eks.types.capacity_types

        out["capacity_type"] = capo_eks.types.capacity_types.deserialize_json(
            data["capacityType"]
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("releaseVersion") is not None:
        out["release_version"] = data["releaseVersion"]
    if data.get("warmPoolConfig") is not None:
        import capo_eks.types.warm_pool_config

        out["warm_pool_config"] = capo_eks.types.warm_pool_config.deserialize_json(
            data["warmPoolConfig"]
        )
    return out
