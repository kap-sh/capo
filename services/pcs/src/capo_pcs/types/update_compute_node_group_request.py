"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateComputeNodeGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.ami_id_or_empty
    import capo_pcs.types.cluster_identifier
    import capo_pcs.types.compute_node_group_identifier
    import capo_pcs.types.custom_launch_template
    import capo_pcs.types.instance_profile_arn
    import capo_pcs.types.key_pair_name_or_empty
    import capo_pcs.types.launch_template_mode
    import capo_pcs.types.purchase_option
    import capo_pcs.types.sb_client_token
    import capo_pcs.types.scaling_configuration_request
    import capo_pcs.types.security_group_id_list_or_empty
    import capo_pcs.types.spot_options
    import capo_pcs.types.string_list
    import capo_pcs.types.update_compute_node_group_slurm_configuration_request
    import capo_pcs.types.update_node_lifecycle_actions_request


class UpdateComputeNodeGroupRequest(TypedDict, closed=True):
    ami_id: NotRequired["capo_pcs.types.ami_id_or_empty.AmiIdOrEmpty"]
    """<p>The ID of the Amazon Machine Image (AMI) that PCS uses to launch instances. This value overrides the AMI ID in the custom launch template. Specify an empty string (<code>""</code>) to remove the AMI ID from the compute node group and use the AMI ID specified in the custom launch template. Omit this value to leave the current setting unchanged.</p>"""
    security_group_ids: NotRequired[
        "capo_pcs.types.security_group_id_list_or_empty.SecurityGroupIdListOrEmpty"
    ]
    """<p>The IDs of the EC2 security groups to configure directly on the compute node group. The security groups must be in the same VPC as the cluster. PCS uses these security groups instead of the security groups in the custom launch template. You can't specify this value if the custom launch template defines network interfaces. Specify an empty list (<code>[]</code>) to remove the security groups from the compute node group and use the security groups in the custom launch template. Omit this value to leave the current setting unchanged.</p>"""
    ssh_key_name: NotRequired[
        "capo_pcs.types.key_pair_name_or_empty.KeyPairNameOrEmpty"
    ]
    """<p>The name of the EC2 key pair to configure directly on the compute node group. The key pair must exist in your account and Amazon Web Services Region. PCS uses this key pair instead of the key pair in the custom launch template. Specify an empty string (<code>""</code>) to remove the key pair from the compute node group and use the key pair in the custom launch template. Omit this value to leave the current setting unchanged. You must have permission for <code>ec2:DescribeKeyPairs</code> to specify a key pair. If you delete the key pair later, future instance launches can fail.</p>"""
    cluster_identifier: "capo_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster of the compute node group.</p>"""
    compute_node_group_identifier: (
        "capo_pcs.types.compute_node_group_identifier.ComputeNodeGroupIdentifier"
    )
    """<p>The name or ID of the compute node group.</p>"""
    subnet_ids: NotRequired["capo_pcs.types.string_list.StringList"]
    """<p>The list of subnet IDs where the compute node group provisions instances. The subnets must be in the same VPC as the cluster.</p>"""
    launch_template_mode: NotRequired[
        "capo_pcs.types.launch_template_mode.LaunchTemplateMode"
    ]
    """<p>Specifies whether the compute node group uses a custom launch template or a launch template that PCS manages. Omit this value to keep the current mode.</p> <p>Valid values:</p> <ul> <li> <p> <code>CUSTOM</code> – Use a custom launch template. To switch from <code>MANAGED</code>, also provide <code>customLaunchTemplate</code>. If the compute node group already uses <code>CUSTOM</code> and you omit <code>customLaunchTemplate</code>, the existing launch template is unchanged.</p> </li> <li> <p> <code>MANAGED</code> – Use a launch template created and managed by PCS. Omit <code>customLaunchTemplate</code>. Switching to this mode removes the custom launch template association but doesn't delete the launch template.</p> </li> </ul> <p>When switching to <code>MANAGED</code>, the compute node group must have <code>amiId</code> and <code>securityGroupIds</code> configured. You can set these values in the same request.</p>"""
    custom_launch_template: NotRequired[
        "capo_pcs.types.custom_launch_template.CustomLaunchTemplate"
    ]
    """<p>The custom Amazon EC2 launch template to associate with the compute node group. To set or change the custom launch template, specify <code>id</code> and <code>version</code>. If you provide this value and omit <code>launchTemplateMode</code>, the compute node group must already use <code>CUSTOM</code> mode. To switch from <code>MANAGED</code> to <code>CUSTOM</code>, specify <code>launchTemplateMode</code> as <code>CUSTOM</code> and provide this value. If the compute node group already uses <code>CUSTOM</code>, omit this value while also omitting <code>launchTemplateMode</code>, or while specifying <code>CUSTOM</code>, to keep the existing custom launch template. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng_instance-settings-migrate.html">Migrating a compute node group from a custom launch template</a> in the <i>PCS User Guide</i>.</p>"""
    purchase_option: NotRequired["capo_pcs.types.purchase_option.PurchaseOption"]
    """<p>Specifies how EC2 instances are purchased on your behalf. PCS supports On-Demand Instances, Spot Instances, Interruptible Capacity Reservations, On-Demand Capacity Reservations, and Amazon EC2 Capacity Blocks for ML. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html">Amazon EC2 billing and purchasing options</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. For more information about PCS support for Capacity Blocks, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html">Using Amazon EC2 Capacity Blocks for ML with PCS</a> in the <i>PCS User Guide</i>. For more information about PCS support for interruptible capacity reservations, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-iodcr.html">Using I-ODCRs with PCS</a> in the <i>PCS User Guide</i>. Choose On-Demand if you plan to use an On-Demand Capacity Reservation (ODCR). For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html">Using ODCRs with PCS</a>. If you don't provide this option, it defaults to On-Demand.</p>"""
    spot_options: NotRequired["capo_pcs.types.spot_options.SpotOptions"]
    scaling_configuration: NotRequired[
        "capo_pcs.types.scaling_configuration_request.ScalingConfigurationRequest"
    ]
    """<p>Specifies the boundaries of the compute node group auto scaling.</p>"""
    iam_instance_profile_arn: NotRequired[
        "capo_pcs.types.instance_profile_arn.InstanceProfileArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the <code>pcs:RegisterComputeNodeGroupInstance</code> permission and the role name must start with <code>AWSPCS</code> or must have the path <code>/aws-pcs/</code>. For more information, see <a href="https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html">IAM instance profiles for PCS</a> in the <i>PCS User Guide</i>.</p>"""
    slurm_configuration: NotRequired[
        "capo_pcs.types.update_compute_node_group_slurm_configuration_request.UpdateComputeNodeGroupSlurmConfigurationRequest"
    ]
    """<p>Additional options related to the Slurm scheduler.</p>"""
    node_lifecycle_actions: NotRequired[
        "capo_pcs.types.update_node_lifecycle_actions_request.UpdateNodeLifecycleActionsRequest"
    ]
    """<p>The lifecycle actions to run on compute nodes in the compute node group. Use lifecycle actions to run custom scripts at defined stages of a compute node's lifecycle, such as when a compute node finishes bootstrapping or becomes ready to accept jobs.</p>"""
    client_token: NotRequired["capo_pcs.types.sb_client_token.SBClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect. If you don't specify a client token, the CLI and SDK automatically generate one for you.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateComputeNodeGroupRequest) -> dict:
    out: dict = {}
    if "ami_id" in value:
        out["amiId"] = value["ami_id"]
    if "security_group_ids" in value:
        import capo_pcs.types.security_group_id_list_or_empty

        out["securityGroupIds"] = (
            capo_pcs.types.security_group_id_list_or_empty.serialize_aws_json_1_0(
                value["security_group_ids"]
            )
        )
    if "ssh_key_name" in value:
        out["sshKeyName"] = value["ssh_key_name"]
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["computeNodeGroupIdentifier"] = value["compute_node_group_identifier"]
    if "subnet_ids" in value:
        import capo_pcs.types.string_list

        out["subnetIds"] = capo_pcs.types.string_list.serialize_aws_json_1_0(
            value["subnet_ids"]
        )
    if "launch_template_mode" in value:
        import capo_pcs.types.launch_template_mode

        out["launchTemplateMode"] = (
            capo_pcs.types.launch_template_mode.serialize_aws_json_1_0(
                value["launch_template_mode"]
            )
        )
    if "custom_launch_template" in value:
        import capo_pcs.types.custom_launch_template

        out["customLaunchTemplate"] = (
            capo_pcs.types.custom_launch_template.serialize_aws_json_1_0(
                value["custom_launch_template"]
            )
        )
    if "purchase_option" in value:
        import capo_pcs.types.purchase_option

        out["purchaseOption"] = capo_pcs.types.purchase_option.serialize_aws_json_1_0(
            value["purchase_option"]
        )
    if "spot_options" in value:
        import capo_pcs.types.spot_options

        out["spotOptions"] = capo_pcs.types.spot_options.serialize_aws_json_1_0(
            value["spot_options"]
        )
    if "scaling_configuration" in value:
        import capo_pcs.types.scaling_configuration_request

        out["scalingConfiguration"] = (
            capo_pcs.types.scaling_configuration_request.serialize_aws_json_1_0(
                value["scaling_configuration"]
            )
        )
    if "iam_instance_profile_arn" in value:
        out["iamInstanceProfileArn"] = value["iam_instance_profile_arn"]
    if "slurm_configuration" in value:
        import capo_pcs.types.update_compute_node_group_slurm_configuration_request

        out["slurmConfiguration"] = (
            capo_pcs.types.update_compute_node_group_slurm_configuration_request.serialize_aws_json_1_0(
                value["slurm_configuration"]
            )
        )
    if "node_lifecycle_actions" in value:
        import capo_pcs.types.update_node_lifecycle_actions_request

        out["nodeLifecycleActions"] = (
            capo_pcs.types.update_node_lifecycle_actions_request.serialize_aws_json_1_0(
                value["node_lifecycle_actions"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateComputeNodeGroupRequest:
    out: UpdateComputeNodeGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("amiId") is not None:
        out["ami_id"] = data["amiId"]
    if data.get("securityGroupIds") is not None:
        import capo_pcs.types.security_group_id_list_or_empty

        out["security_group_ids"] = (
            capo_pcs.types.security_group_id_list_or_empty.deserialize_aws_json_1_0(
                data["securityGroupIds"]
            )
        )
    if data.get("sshKeyName") is not None:
        out["ssh_key_name"] = data["sshKeyName"]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        out["cluster_identifier"] = ""
    if data.get("computeNodeGroupIdentifier") is not None:
        out["compute_node_group_identifier"] = data["computeNodeGroupIdentifier"]
    else:
        out["compute_node_group_identifier"] = ""
    if data.get("subnetIds") is not None:
        import capo_pcs.types.string_list

        out["subnet_ids"] = capo_pcs.types.string_list.deserialize_aws_json_1_0(
            data["subnetIds"]
        )
    if data.get("launchTemplateMode") is not None:
        import capo_pcs.types.launch_template_mode

        out["launch_template_mode"] = (
            capo_pcs.types.launch_template_mode.deserialize_aws_json_1_0(
                data["launchTemplateMode"]
            )
        )
    if data.get("customLaunchTemplate") is not None:
        import capo_pcs.types.custom_launch_template

        out["custom_launch_template"] = (
            capo_pcs.types.custom_launch_template.deserialize_aws_json_1_0(
                data["customLaunchTemplate"]
            )
        )
    if data.get("purchaseOption") is not None:
        import capo_pcs.types.purchase_option

        out["purchase_option"] = (
            capo_pcs.types.purchase_option.deserialize_aws_json_1_0(
                data["purchaseOption"]
            )
        )
    if data.get("spotOptions") is not None:
        import capo_pcs.types.spot_options

        out["spot_options"] = capo_pcs.types.spot_options.deserialize_aws_json_1_0(
            data["spotOptions"]
        )
    if data.get("scalingConfiguration") is not None:
        import capo_pcs.types.scaling_configuration_request

        out["scaling_configuration"] = (
            capo_pcs.types.scaling_configuration_request.deserialize_aws_json_1_0(
                data["scalingConfiguration"]
            )
        )
    if data.get("iamInstanceProfileArn") is not None:
        out["iam_instance_profile_arn"] = data["iamInstanceProfileArn"]
    if data.get("slurmConfiguration") is not None:
        import capo_pcs.types.update_compute_node_group_slurm_configuration_request

        out["slurm_configuration"] = (
            capo_pcs.types.update_compute_node_group_slurm_configuration_request.deserialize_aws_json_1_0(
                data["slurmConfiguration"]
            )
        )
    if data.get("nodeLifecycleActions") is not None:
        import capo_pcs.types.update_node_lifecycle_actions_request

        out["node_lifecycle_actions"] = (
            capo_pcs.types.update_node_lifecycle_actions_request.deserialize_aws_json_1_0(
                data["nodeLifecycleActions"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
