"""Generated from Smithy shape ``com.amazonaws.pcs#CreateComputeNodeGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pcs.types.ami_id
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.compute_node_group_name
    import capo_pcs.types.compute_node_group_slurm_configuration_request
    import capo_pcs.types.custom_launch_template
    import capo_pcs.types.instance_list
    import capo_pcs.types.instance_profile_arn
    import capo_pcs.types.node_lifecycle_actions_request
    import capo_pcs.types.purchase_option
    import capo_pcs.types.request_tag_map
    import capo_pcs.types.sb_client_token
    import capo_pcs.types.scaling_configuration_request
    import capo_pcs.types.spot_options
    import capo_pcs.types.string_list


class CreateComputeNodeGroupRequest(TypedDict, closed=True):
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster to create a compute node group in.</p>"""
    compute_node_group_name: (
        "capo_pcs.types.compute_node_group_name.ComputeNodeGroupName"
    )
    """<p>A name to identify the cluster. Example: <code>MyCluster</code> </p>"""
    ami_id: NotRequired["capo_pcs.types.ami_id.AmiId"]
    """<p> The ID of the Amazon Machine Image (AMI) that PCS uses to launch compute nodes (Amazon EC2 instances). If you don't provide this value, PCS uses the AMI ID specified in the custom launch template.</p>"""
    subnet_ids: "capo_pcs.types.string_list.StringList"
    """<p>The list of subnet IDs where the compute node group launches instances. Subnets must be in the same VPC as the cluster.</p>"""
    purchase_option: NotRequired["capo_pcs.types.purchase_option.PurchaseOption"]
    """<p>Specifies how EC2 instances are purchased on your behalf. PCS supports On-Demand Instances, Spot Instances, Interruptible Capacity Reservations, On-Demand Capacity Reservations, and Amazon EC2 Capacity Blocks for ML. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html">Amazon EC2 billing and purchasing options</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. For more information about PCS support for Capacity Blocks, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html">Using Amazon EC2 Capacity Blocks for ML with PCS</a> in the <i>PCS User Guide</i>. For more information about PCS support for interruptible capacity reservations, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-iodcr.html">Using I-ODCRs with PCS</a> in the <i>PCS User Guide</i>. Choose On-Demand if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html">Using ODCRs with PCS</a>. If you don't provide this option, it defaults to On-Demand.</p>"""
    custom_launch_template: "capo_pcs.types.custom_launch_template.CustomLaunchTemplate"
    iam_instance_profile_arn: "capo_pcs.types.instance_profile_arn.InstanceProfileArn"
    """<p>The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the <code>pcs:RegisterComputeNodeGroupInstance</code> permission and the role name must start with <code>AWSPCS</code> or must have the path <code>/aws-pcs/</code>. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html">IAM instance profiles for PCS</a> in the <i>PCS User Guide</i>.</p>"""
    scaling_configuration: (
        "capo_pcs.types.scaling_configuration_request.ScalingConfigurationRequest"
    )
    """<p>Specifies the boundaries of the compute node group auto scaling.</p>"""
    instance_configs: "capo_pcs.types.instance_list.InstanceList"
    """<p>A list of EC2 instance configurations that PCS can provision in the compute node group.</p>"""
    spot_options: NotRequired["capo_pcs.types.spot_options.SpotOptions"]
    slurm_configuration: NotRequired[
        "capo_pcs.types.compute_node_group_slurm_configuration_request.ComputeNodeGroupSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    node_lifecycle_actions: NotRequired[
        "capo_pcs.types.node_lifecycle_actions_request.NodeLifecycleActionsRequest"
    ]
    """<p>The lifecycle actions to run on compute nodes in the compute node group. Use lifecycle actions to run custom scripts at defined stages of a compute node's lifecycle, such as when a compute node finishes bootstrapping or becomes ready to accept jobs.</p>"""
    client_token: NotRequired["capo_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate 1 for you.</p>"""
    tags: NotRequired["capo_pcs.types.request_tag_map.RequestTagMap"]
    """<p>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateComputeNodeGroupRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["computeNodeGroupName"] = value["compute_node_group_name"]
    if "ami_id" in value:
        out["amiId"] = value["ami_id"]
    import capo_pcs.types.string_list

    out["subnetIds"] = capo_pcs.types.string_list.serialize_aws_json_1_0(
        value["subnet_ids"]
    )
    if "purchase_option" in value:
        import capo_pcs.types.purchase_option

        out["purchaseOption"] = capo_pcs.types.purchase_option.serialize_aws_json_1_0(
            value["purchase_option"]
        )
    import capo_pcs.types.custom_launch_template

    out["customLaunchTemplate"] = (
        capo_pcs.types.custom_launch_template.serialize_aws_json_1_0(
            value["custom_launch_template"]
        )
    )
    out["iamInstanceProfileArn"] = value["iam_instance_profile_arn"]
    import capo_pcs.types.scaling_configuration_request

    out["scalingConfiguration"] = (
        capo_pcs.types.scaling_configuration_request.serialize_aws_json_1_0(
            value["scaling_configuration"]
        )
    )
    import capo_pcs.types.instance_list

    out["instanceConfigs"] = capo_pcs.types.instance_list.serialize_aws_json_1_0(
        value["instance_configs"]
    )
    if "spot_options" in value:
        import capo_pcs.types.spot_options

        out["spotOptions"] = capo_pcs.types.spot_options.serialize_aws_json_1_0(
            value["spot_options"]
        )
    if "slurm_configuration" in value:
        import capo_pcs.types.compute_node_group_slurm_configuration_request

        out["slurmConfiguration"] = (
            capo_pcs.types.compute_node_group_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "node_lifecycle_actions" in value:
        import capo_pcs.types.node_lifecycle_actions_request

        out["nodeLifecycleActions"] = (
            capo_pcs.types.node_lifecycle_actions_request.serialize_aws_json_1_0(
                value["node_lifecycle_actions"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_pcs.types.request_tag_map

        out["tags"] = capo_pcs.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateComputeNodeGroupRequest:
    out: CreateComputeNodeGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError(
            "CreateComputeNodeGroupRequest.cluster_identifier required"
        )
    if data.get("computeNodeGroupName") is not None:
        out["compute_node_group_name"] = data["computeNodeGroupName"]
    else:
        raise DeserializationError(
            "CreateComputeNodeGroupRequest.compute_node_group_name required"
        )
    if data.get("amiId") is not None:
        out["ami_id"] = data["amiId"]
    if data.get("subnetIds") is not None:
        import capo_pcs.types.string_list

        out["subnet_ids"] = capo_pcs.types.string_list.deserialize_aws_json_1_0(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("CreateComputeNodeGroupRequest.subnet_ids required")
    if data.get("purchaseOption") is not None:
        import capo_pcs.types.purchase_option

        out["purchase_option"] = (
            capo_pcs.types.purchase_option.deserialize_aws_json_1_0(
                data["purchaseOption"]
            )
        )
    if data.get("customLaunchTemplate") is not None:
        import capo_pcs.types.custom_launch_template

        out["custom_launch_template"] = (
            capo_pcs.types.custom_launch_template.deserialize_aws_json_1_0(
                data["customLaunchTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateComputeNodeGroupRequest.custom_launch_template required"
        )
    if data.get("iamInstanceProfileArn") is not None:
        out["iam_instance_profile_arn"] = data["iamInstanceProfileArn"]
    else:
        raise DeserializationError(
            "CreateComputeNodeGroupRequest.iam_instance_profile_arn required"
        )
    if data.get("scalingConfiguration") is not None:
        import capo_pcs.types.scaling_configuration_request

        out["scaling_configuration"] = (
            capo_pcs.types.scaling_configuration_request.deserialize_aws_json_1_0(
                data["scalingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateComputeNodeGroupRequest.scaling_configuration required"
        )
    if data.get("instanceConfigs") is not None:
        import capo_pcs.types.instance_list

        out["instance_configs"] = capo_pcs.types.instance_list.deserialize_aws_json_1_0(
            data["instanceConfigs"]
        )
    else:
        raise DeserializationError(
            "CreateComputeNodeGroupRequest.instance_configs required"
        )
    if data.get("spotOptions") is not None:
        import capo_pcs.types.spot_options

        out["spot_options"] = capo_pcs.types.spot_options.deserialize_aws_json_1_0(
            data["spotOptions"]
        )
    if data.get("slurmConfiguration") is not None:
        import capo_pcs.types.compute_node_group_slurm_configuration_request

        out["slurm_configuration"] = (
            capo_pcs.types.compute_node_group_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if data.get("nodeLifecycleActions") is not None:
        import capo_pcs.types.node_lifecycle_actions_request

        out["node_lifecycle_actions"] = (
            capo_pcs.types.node_lifecycle_actions_request.deserialize_aws_json_1_0(
                data["nodeLifecycleActions"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_pcs.types.request_tag_map

        out["tags"] = capo_pcs.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
