"""Generated from Smithy shape ``com.amazonaws.eks#Nodegroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.ami_types
    import capo_eks.types.boxed_integer
    import capo_eks.types.capacity_types
    import capo_eks.types.labels_map
    import capo_eks.types.launch_template_specification
    import capo_eks.types.node_repair_config
    import capo_eks.types.nodegroup_health
    import capo_eks.types.nodegroup_resources
    import capo_eks.types.nodegroup_scaling_config
    import capo_eks.types.nodegroup_status
    import capo_eks.types.nodegroup_update_config
    import capo_eks.types.remote_access_config
    import capo_eks.types.string
    import capo_eks.types.string_list
    import capo_eks.types.tag_map
    import capo_eks.types.taints_list
    import capo_eks.types.timestamp
    import capo_eks.types.warm_pool_config


class Nodegroup(TypedDict, closed=True):
    nodegroup_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name associated with an Amazon EKS managed node group.</p>"""
    nodegroup_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) associated with the managed node group.</p>"""
    cluster_name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of your cluster.</p>"""
    version: NotRequired["capo_eks.types.string.String"]
    """<p>The Kubernetes version of the managed node group.</p>"""
    release_version: NotRequired["capo_eks.types.string.String"]
    """<p>If the node group was deployed using a launch template with a custom AMI, then this is the AMI ID that was specified in the launch template. For node groups that weren't deployed using a launch template, this is the version of the Amazon EKS optimized AMI that the node group was deployed with.</p>"""
    created_at: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp at object creation.</p>"""
    modified_at: NotRequired["capo_eks.types.timestamp.Timestamp"]
    """<p>The Unix epoch timestamp for the last modification to the object.</p>"""
    status: NotRequired["capo_eks.types.nodegroup_status.NodegroupStatus"]
    """<p>The current status of the managed node group.</p>"""
    capacity_type: NotRequired["capo_eks.types.capacity_types.CapacityTypes"]
    """<p>The capacity type of your managed node group.</p>"""
    scaling_config: NotRequired[
        "capo_eks.types.nodegroup_scaling_config.NodegroupScalingConfig"
    ]
    """<p>The scaling configuration details for the Auto Scaling group that is associated with your node group.</p>"""
    instance_types: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>If the node group wasn't deployed with a launch template, then this is the instance type that is associated with the node group. If the node group was deployed with a launch template, then this is <code>null</code>.</p>"""
    subnets: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The subnets that were specified for the Auto Scaling group that is associated with your node group.</p>"""
    remote_access: NotRequired["capo_eks.types.remote_access_config.RemoteAccessConfig"]
    """<p>If the node group wasn't deployed with a launch template, then this is the remote access configuration that is associated with the node group. If the node group was deployed with a launch template, then this is <code>null</code>.</p>"""
    ami_type: NotRequired["capo_eks.types.ami_types.AMITypes"]
    """<p>If the node group was deployed using a launch template with a custom AMI, then this is <code>CUSTOM</code>. For node groups that weren't deployed using a launch template, this is the AMI type that was specified in the node group configuration.</p>"""
    node_role: NotRequired["capo_eks.types.string.String"]
    """<p>The IAM role associated with your node group. The Amazon EKS node <code>kubelet</code> daemon makes calls to Amazon Web Services APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies.</p>"""
    labels: NotRequired["capo_eks.types.labels_map.labelsMap"]
    """<p>The Kubernetes <code>labels</code> applied to the nodes in the node group.</p> <note> <p>Only <code>labels</code> that are applied with the Amazon EKS API are shown here. There may be other Kubernetes <code>labels</code> applied to the nodes in this group.</p> </note>"""
    taints: NotRequired["capo_eks.types.taints_list.taintsList"]
    """<p>The Kubernetes taints to be applied to the nodes in the node group when they are created. Effect is one of <code>No_Schedule</code>, <code>Prefer_No_Schedule</code>, or <code>No_Execute</code>. Kubernetes taints can be used together with tolerations to control how workloads are scheduled to your nodes. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html">Node taints on managed node groups</a>.</p>"""
    resources: NotRequired["capo_eks.types.nodegroup_resources.NodegroupResources"]
    """<p>The resources associated with the node group, such as Auto Scaling groups and security groups for remote access.</p>"""
    disk_size: NotRequired["capo_eks.types.boxed_integer.BoxedInteger"]
    """<p>If the node group wasn't deployed with a launch template, then this is the disk size in the node group configuration. If the node group was deployed with a launch template, then this is <code>null</code>.</p>"""
    health: NotRequired["capo_eks.types.nodegroup_health.NodegroupHealth"]
    """<p>The health status of the node group. If there are issues with your node group's health, they are listed here.</p>"""
    update_config: NotRequired[
        "capo_eks.types.nodegroup_update_config.NodegroupUpdateConfig"
    ]
    """<p>The node group update configuration.</p>"""
    node_repair_config: NotRequired[
        "capo_eks.types.node_repair_config.NodeRepairConfig"
    ]
    """<p>The node auto repair configuration for the node group.</p>"""
    launch_template: NotRequired[
        "capo_eks.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>If a launch template was used to create the node group, then this is the launch template that was used.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    warm_pool_config: NotRequired["capo_eks.types.warm_pool_config.WarmPoolConfig"]
    """<p>The warm pool configuration attached to the node group. Amazon EKS manages warm pools throughout the node group lifecycle using the <code>AWSServiceRoleForAmazonEKSNodegroup</code> service-linked role to create, update, and delete warm pool resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Nodegroup) -> dict:
    out: dict = {}
    if "nodegroup_name" in value:
        out["nodegroupName"] = value["nodegroup_name"]
    if "nodegroup_arn" in value:
        out["nodegroupArn"] = value["nodegroup_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "version" in value:
        out["version"] = value["version"]
    if "release_version" in value:
        out["releaseVersion"] = value["release_version"]
    if "created_at" in value:
        import capo_eks.types.timestamp

        out["createdAt"] = capo_eks.types.timestamp.serialize_json(value["created_at"])
    if "modified_at" in value:
        import capo_eks.types.timestamp

        out["modifiedAt"] = capo_eks.types.timestamp.serialize_json(
            value["modified_at"]
        )
    if "status" in value:
        import capo_eks.types.nodegroup_status

        out["status"] = capo_eks.types.nodegroup_status.serialize_json(value["status"])
    if "capacity_type" in value:
        import capo_eks.types.capacity_types

        out["capacityType"] = capo_eks.types.capacity_types.serialize_json(
            value["capacity_type"]
        )
    if "scaling_config" in value:
        import capo_eks.types.nodegroup_scaling_config

        out["scalingConfig"] = capo_eks.types.nodegroup_scaling_config.serialize_json(
            value["scaling_config"]
        )
    if "instance_types" in value:
        import capo_eks.types.string_list

        out["instanceTypes"] = capo_eks.types.string_list.serialize_json(
            value["instance_types"]
        )
    if "subnets" in value:
        import capo_eks.types.string_list

        out["subnets"] = capo_eks.types.string_list.serialize_json(value["subnets"])
    if "remote_access" in value:
        import capo_eks.types.remote_access_config

        out["remoteAccess"] = capo_eks.types.remote_access_config.serialize_json(
            value["remote_access"]
        )
    if "ami_type" in value:
        import capo_eks.types.ami_types

        out["amiType"] = capo_eks.types.ami_types.serialize_json(value["ami_type"])
    if "node_role" in value:
        out["nodeRole"] = value["node_role"]
    if "labels" in value:
        import capo_eks.types.labels_map

        out["labels"] = capo_eks.types.labels_map.serialize_json(value["labels"])
    if "taints" in value:
        import capo_eks.types.taints_list

        out["taints"] = capo_eks.types.taints_list.serialize_json(value["taints"])
    if "resources" in value:
        import capo_eks.types.nodegroup_resources

        out["resources"] = capo_eks.types.nodegroup_resources.serialize_json(
            value["resources"]
        )
    if "disk_size" in value:
        out["diskSize"] = value["disk_size"]
    if "health" in value:
        import capo_eks.types.nodegroup_health

        out["health"] = capo_eks.types.nodegroup_health.serialize_json(value["health"])
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
    if "launch_template" in value:
        import capo_eks.types.launch_template_specification

        out["launchTemplate"] = (
            capo_eks.types.launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    if "warm_pool_config" in value:
        import capo_eks.types.warm_pool_config

        out["warmPoolConfig"] = capo_eks.types.warm_pool_config.serialize_json(
            value["warm_pool_config"]
        )
    return out


def deserialize_json(data: dict) -> Nodegroup:
    out: Nodegroup = {}  # type: ignore[typeddict-item]
    if data.get("nodegroupName") is not None:
        out["nodegroup_name"] = data["nodegroupName"]
    if data.get("nodegroupArn") is not None:
        out["nodegroup_arn"] = data["nodegroupArn"]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("releaseVersion") is not None:
        out["release_version"] = data["releaseVersion"]
    if data.get("createdAt") is not None:
        import capo_eks.types.timestamp

        out["created_at"] = capo_eks.types.timestamp.deserialize_json(data["createdAt"])
    if data.get("modifiedAt") is not None:
        import capo_eks.types.timestamp

        out["modified_at"] = capo_eks.types.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    if data.get("status") is not None:
        import capo_eks.types.nodegroup_status

        out["status"] = capo_eks.types.nodegroup_status.deserialize_json(data["status"])
    if data.get("capacityType") is not None:
        import capo_eks.types.capacity_types

        out["capacity_type"] = capo_eks.types.capacity_types.deserialize_json(
            data["capacityType"]
        )
    if data.get("scalingConfig") is not None:
        import capo_eks.types.nodegroup_scaling_config

        out["scaling_config"] = (
            capo_eks.types.nodegroup_scaling_config.deserialize_json(
                data["scalingConfig"]
            )
        )
    if data.get("instanceTypes") is not None:
        import capo_eks.types.string_list

        out["instance_types"] = capo_eks.types.string_list.deserialize_json(
            data["instanceTypes"]
        )
    if data.get("subnets") is not None:
        import capo_eks.types.string_list

        out["subnets"] = capo_eks.types.string_list.deserialize_json(data["subnets"])
    if data.get("remoteAccess") is not None:
        import capo_eks.types.remote_access_config

        out["remote_access"] = capo_eks.types.remote_access_config.deserialize_json(
            data["remoteAccess"]
        )
    if data.get("amiType") is not None:
        import capo_eks.types.ami_types

        out["ami_type"] = capo_eks.types.ami_types.deserialize_json(data["amiType"])
    if data.get("nodeRole") is not None:
        out["node_role"] = data["nodeRole"]
    if data.get("labels") is not None:
        import capo_eks.types.labels_map

        out["labels"] = capo_eks.types.labels_map.deserialize_json(data["labels"])
    if data.get("taints") is not None:
        import capo_eks.types.taints_list

        out["taints"] = capo_eks.types.taints_list.deserialize_json(data["taints"])
    if data.get("resources") is not None:
        import capo_eks.types.nodegroup_resources

        out["resources"] = capo_eks.types.nodegroup_resources.deserialize_json(
            data["resources"]
        )
    if data.get("diskSize") is not None:
        out["disk_size"] = data["diskSize"]
    if data.get("health") is not None:
        import capo_eks.types.nodegroup_health

        out["health"] = capo_eks.types.nodegroup_health.deserialize_json(data["health"])
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
    if data.get("launchTemplate") is not None:
        import capo_eks.types.launch_template_specification

        out["launch_template"] = (
            capo_eks.types.launch_template_specification.deserialize_json(
                data["launchTemplate"]
            )
        )
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    if data.get("warmPoolConfig") is not None:
        import capo_eks.types.warm_pool_config

        out["warm_pool_config"] = capo_eks.types.warm_pool_config.deserialize_json(
            data["warmPoolConfig"]
        )
    return out
