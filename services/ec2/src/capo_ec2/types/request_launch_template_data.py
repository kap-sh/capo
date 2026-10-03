"""Generated from Smithy shape ``com.amazonaws.ec2#RequestLaunchTemplateData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.credit_specification_request
    import capo_ec2.types.elastic_gpu_specification_list
    import capo_ec2.types.image_id
    import capo_ec2.types.instance_requirements_request
    import capo_ec2.types.instance_type
    import capo_ec2.types.kernel_id
    import capo_ec2.types.key_pair_name
    import capo_ec2.types.launch_template_block_device_mapping_request_list
    import capo_ec2.types.launch_template_capacity_reservation_specification_request
    import capo_ec2.types.launch_template_cpu_options_request
    import capo_ec2.types.launch_template_elastic_inference_accelerator_list
    import capo_ec2.types.launch_template_enclave_options_request
    import capo_ec2.types.launch_template_hibernation_options_request
    import capo_ec2.types.launch_template_iam_instance_profile_specification_request
    import capo_ec2.types.launch_template_instance_maintenance_options_request
    import capo_ec2.types.launch_template_instance_market_options_request
    import capo_ec2.types.launch_template_instance_metadata_options_request
    import capo_ec2.types.launch_template_instance_network_interface_specification_request_list
    import capo_ec2.types.launch_template_instance_secondary_interface_specification_request_list
    import capo_ec2.types.launch_template_license_specification_list_request
    import capo_ec2.types.launch_template_network_performance_options_request
    import capo_ec2.types.launch_template_placement_request
    import capo_ec2.types.launch_template_private_dns_name_options_request
    import capo_ec2.types.launch_template_tag_specification_request_list
    import capo_ec2.types.launch_templates_monitoring_request
    import capo_ec2.types.operator_request
    import capo_ec2.types.ramdisk_id
    import capo_ec2.types.security_group_id_string_list
    import capo_ec2.types.security_group_string_list
    import capo_ec2.types.sensitive_user_data
    import capo_ec2.types.shutdown_behavior


class RequestLaunchTemplateData(TypedDict, closed=True):
    kernel_id: NotRequired["capo_ec2.types.kernel_id.KernelId"]
    """<p>The ID of the kernel.</p> <important> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href="https://docs.aws.amazon.com/linux/al2/ug/UserProvidedKernels.html">User provided kernels</a> in the <i>Amazon Linux 2 User Guide</i>.</p> </important>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.</p>"""
    iam_instance_profile: NotRequired[
        "capo_ec2.types.launch_template_iam_instance_profile_specification_request.LaunchTemplateIamInstanceProfileSpecificationRequest"
    ]
    """<p>The name or Amazon Resource Name (ARN) of an IAM instance profile.</p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.launch_template_block_device_mapping_request_list.LaunchTemplateBlockDeviceMappingRequestList"
    ]
    """<p>The block device mapping.</p>"""
    network_interfaces: NotRequired[
        "capo_ec2.types.launch_template_instance_network_interface_specification_request_list.LaunchTemplateInstanceNetworkInterfaceSpecificationRequestList"
    ]
    """<p>The network interfaces for the instance.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI in the format <code>ami-0ac394d6a3example</code>.</p> <p>Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.</p> <p>To reference a public parameter:</p> <ul> <li> <p> <code>resolve:ssm:<i>public-parameter</i> </code> </p> </li> </ul> <p>To reference a parameter stored in the same account:</p> <ul> <li> <p> <code>resolve:ssm:<i>parameter-name</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-name:version-number</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-name:label</i> </code> </p> </li> </ul> <p>To reference a parameter shared from another Amazon Web Services account:</p> <ul> <li> <p> <code>resolve:ssm:<i>parameter-ARN</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-ARN:version-number</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-ARN:label</i> </code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>If the launch template will be used for an EC2 Fleet or Spot Fleet, note the following:</p> <ul> <li> <p>Only EC2 Fleets of type <code>instant</code> support specifying a Systems Manager parameter.</p> </li> <li> <p>For EC2 Fleets of type <code>maintain</code> or <code>request</code>, or for Spot Fleets, you must specify the AMI ID.</p> </li> </ul> </note>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Amazon EC2 instance types</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>If you specify <code>InstanceType</code>, you can't specify <code>InstanceRequirements</code>.</p>"""
    key_name: NotRequired["capo_ec2.types.key_pair_name.KeyPairName"]
    """<p>The name of the key pair. You can create a key pair using <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html">CreateKeyPair</a> or <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportKeyPair.html">ImportKeyPair</a>.</p> <important> <p>If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.</p> </important>"""
    monitoring: NotRequired[
        "capo_ec2.types.launch_templates_monitoring_request.LaunchTemplatesMonitoringRequest"
    ]
    """<p>The monitoring for the instance.</p>"""
    placement: NotRequired[
        "capo_ec2.types.launch_template_placement_request.LaunchTemplatePlacementRequest"
    ]
    """<p>The placement for the instance.</p>"""
    ram_disk_id: NotRequired["capo_ec2.types.ramdisk_id.RamdiskId"]
    """<p>The ID of the RAM disk.</p> <important> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html">User provided kernels</a> in the <i>Amazon EC2 User Guide</i>.</p> </important>"""
    disable_api_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether termination protection is enabled for the instance. The default is <code>false</code>, which means that you can terminate the instance using the Amazon EC2 console, command line tools, or API. You can enable termination protection when you launch an instance, while the instance is running, or while the instance is stopped.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "capo_ec2.types.shutdown_behavior.ShutdownBehavior"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p> <p>Default: <code>stop</code> </p>"""
    user_data: NotRequired["capo_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The user data to make available to the instance. You must provide base64-encoded text. User data is limited to 16 KB. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html">Run commands when you launch an EC2 instance with user data input</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>If you are creating the launch template for use with Batch, the user data must be provided in the <a href="https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive">MIME multi-part archive format</a>. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html#lt-user-data">Amazon EC2 user data in launch templates</a> in the <i>Batch User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.launch_template_tag_specification_request_list.LaunchTemplateTagSpecificationRequestList"
    ]
    """<p>The tags to apply to the resources that are created during instance launch. These tags are not applied to the launch template.</p>"""
    elastic_gpu_specifications: NotRequired[
        "capo_ec2.types.elastic_gpu_specification_list.ElasticGpuSpecificationList"
    ]
    """<p>Deprecated.</p> <note> <p>Amazon Elastic Graphics reached end of life on January 8, 2024.</p> </note>"""
    elastic_inference_accelerators: NotRequired[
        "capo_ec2.types.launch_template_elastic_inference_accelerator_list.LaunchTemplateElasticInferenceAcceleratorList"
    ]
    """<note> <p>Amazon Elastic Inference is no longer available.</p> </note> <p>An elastic inference accelerator to associate with the instance. Elastic inference accelerators are a resource you can attach to your Amazon EC2 instances to accelerate your Deep Learning (DL) inference workloads.</p> <p>You cannot specify accelerators from different generations in the same request.</p>"""
    security_group_ids: NotRequired[
        "capo_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of the security groups.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p>"""
    security_groups: NotRequired[
        "capo_ec2.types.security_group_string_list.SecurityGroupStringList"
    ]
    """<p>The names of the security groups. For a nondefault VPC, you must use security group IDs instead.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p>"""
    instance_market_options: NotRequired[
        "capo_ec2.types.launch_template_instance_market_options_request.LaunchTemplateInstanceMarketOptionsRequest"
    ]
    """<p>The market (purchasing) option for the instances.</p>"""
    credit_specification: NotRequired[
        "capo_ec2.types.credit_specification_request.CreditSpecificationRequest"
    ]
    """<p>The credit option for CPU usage of the instance. Valid only for T instances.</p>"""
    cpu_options: NotRequired[
        "capo_ec2.types.launch_template_cpu_options_request.LaunchTemplateCpuOptionsRequest"
    ]
    """<p>The CPU options for the instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html">CPU options for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_reservation_specification: NotRequired[
        "capo_ec2.types.launch_template_capacity_reservation_specification_request.LaunchTemplateCapacityReservationSpecificationRequest"
    ]
    """<p>The Capacity Reservation targeting option. If you do not specify this parameter, the instance's Capacity Reservation preference defaults to <code>open</code>, which enables it to run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).</p>"""
    license_specifications: NotRequired[
        "capo_ec2.types.launch_template_license_specification_list_request.LaunchTemplateLicenseSpecificationListRequest"
    ]
    """<p>The license configurations.</p>"""
    hibernation_options: NotRequired[
        "capo_ec2.types.launch_template_hibernation_options_request.LaunchTemplateHibernationOptionsRequest"
    ]
    """<p>Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html">hibernation prerequisites</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html">Hibernate your Amazon EC2 instance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    metadata_options: NotRequired[
        "capo_ec2.types.launch_template_instance_metadata_options_request.LaunchTemplateInstanceMetadataOptionsRequest"
    ]
    """<p>The metadata options for the instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html">Configure the Instance Metadata Service options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    enclave_options: NotRequired[
        "capo_ec2.types.launch_template_enclave_options_request.LaunchTemplateEnclaveOptionsRequest"
    ]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. For more information, see <a href="https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html">What is Nitro Enclaves?</a> in the <i>Amazon Web Services Nitro Enclaves User Guide</i>.</p> <p>You can't enable Amazon Web Services Nitro Enclaves and hibernation on the same instance.</p>"""
    instance_requirements: NotRequired[
        "capo_ec2.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.</p> <p>You must specify <code>VCpuCount</code> and <code>MemoryMiB</code>. All other attributes are optional. Any unspecified optional attribute is set to its default.</p> <p>When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.</p> <p>To limit the list of instance types from which Amazon EC2 can identify matching instance types, you can use one of the following parameters, but not both in the same request:</p> <ul> <li> <p> <code>AllowedInstanceTypes</code> - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.</p> </li> <li> <p> <code>ExcludedInstanceTypes</code> - The instance types to exclude from the list, even if they match your specified attributes.</p> </li> </ul> <note> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>.</p> <p>Attribute-based instance type selection is only supported when using Auto Scaling groups, EC2 Fleet, and Spot Fleet to launch instances. If you plan to use the launch template in the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html">launch instance wizard</a>, or with the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html">RunInstances</a> API or <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html">AWS::EC2::Instance</a> Amazon Web Services CloudFormation resource, you can't specify <code>InstanceRequirements</code>.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html">Specify attributes for instance type selection for EC2 Fleet or Spot Fleet</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html">Spot placement score</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    private_dns_name_options: NotRequired[
        "capo_ec2.types.launch_template_private_dns_name_options_request.LaunchTemplatePrivateDnsNameOptionsRequest"
    ]
    """<p>The options for the instance hostname. The default values are inherited from the subnet.</p>"""
    maintenance_options: NotRequired[
        "capo_ec2.types.launch_template_instance_maintenance_options_request.LaunchTemplateInstanceMaintenanceOptionsRequest"
    ]
    """<p>The maintenance options for the instance.</p>"""
    disable_api_stop: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to enable the instance for stop protection. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html">Enable stop protection for your EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    operator: NotRequired["capo_ec2.types.operator_request.OperatorRequest"]
    """<p>The entity that manages the launch template.</p>"""
    network_performance_options: NotRequired[
        "capo_ec2.types.launch_template_network_performance_options_request.LaunchTemplateNetworkPerformanceOptionsRequest"
    ]
    """<p>Contains launch template settings to boost network performance for the type of workload that runs on your instance.</p>"""
    secondary_interfaces: NotRequired[
        "capo_ec2.types.launch_template_instance_secondary_interface_specification_request_list.LaunchTemplateInstanceSecondaryInterfaceSpecificationRequestList"
    ]
    """<p>The secondary interfaces to associate with instances launched from the template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestLaunchTemplateData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "kernel_id" in value:
        pairs.append((f"{key_prefix}KernelId", str(value["kernel_id"])))
    if "ebs_optimized" in value:
        pairs.append(
            (f"{key_prefix}EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "iam_instance_profile" in value:
        import capo_ec2.types.launch_template_iam_instance_profile_specification_request

        capo_ec2.types.launch_template_iam_instance_profile_specification_request.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "block_device_mappings" in value:
        import capo_ec2.types.launch_template_block_device_mapping_request_list

        capo_ec2.types.launch_template_block_device_mapping_request_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMapping"
        )
    if "network_interfaces" in value:
        import capo_ec2.types.launch_template_instance_network_interface_specification_request_list

        capo_ec2.types.launch_template_instance_network_interface_specification_request_list.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{key_prefix}NetworkInterface"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "monitoring" in value:
        import capo_ec2.types.launch_templates_monitoring_request

        capo_ec2.types.launch_templates_monitoring_request.serialize_ec2_query(
            value["monitoring"], pairs, f"{key_prefix}Monitoring"
        )
    if "placement" in value:
        import capo_ec2.types.launch_template_placement_request

        capo_ec2.types.launch_template_placement_request.serialize_ec2_query(
            value["placement"], pairs, f"{key_prefix}Placement"
        )
    if "ram_disk_id" in value:
        pairs.append((f"{key_prefix}RamDiskId", str(value["ram_disk_id"])))
    if "disable_api_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DisableApiTermination",
                "true" if value["disable_api_termination"] else "false",
            )
        )
    if "instance_initiated_shutdown_behavior" in value:
        import capo_ec2.types.shutdown_behavior

        capo_ec2.types.shutdown_behavior.serialize_ec2_query(
            value["instance_initiated_shutdown_behavior"],
            pairs,
            f"{key_prefix}InstanceInitiatedShutdownBehavior",
        )
    if "user_data" in value:
        pairs.append((f"{key_prefix}UserData", str(value["user_data"])))
    if "tag_specifications" in value:
        import capo_ec2.types.launch_template_tag_specification_request_list

        capo_ec2.types.launch_template_tag_specification_request_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "elastic_gpu_specifications" in value:
        import capo_ec2.types.elastic_gpu_specification_list

        capo_ec2.types.elastic_gpu_specification_list.serialize_ec2_query(
            value["elastic_gpu_specifications"],
            pairs,
            f"{key_prefix}ElasticGpuSpecification",
        )
    if "elastic_inference_accelerators" in value:
        import capo_ec2.types.launch_template_elastic_inference_accelerator_list

        capo_ec2.types.launch_template_elastic_inference_accelerator_list.serialize_ec2_query(
            value["elastic_inference_accelerators"],
            pairs,
            f"{key_prefix}ElasticInferenceAccelerator",
        )
    if "security_group_ids" in value:
        import capo_ec2.types.security_group_id_string_list

        capo_ec2.types.security_group_id_string_list.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupId"
        )
    if "security_groups" in value:
        import capo_ec2.types.security_group_string_list

        capo_ec2.types.security_group_string_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroup"
        )
    if "instance_market_options" in value:
        import capo_ec2.types.launch_template_instance_market_options_request

        capo_ec2.types.launch_template_instance_market_options_request.serialize_ec2_query(
            value["instance_market_options"],
            pairs,
            f"{key_prefix}InstanceMarketOptions",
        )
    if "credit_specification" in value:
        import capo_ec2.types.credit_specification_request

        capo_ec2.types.credit_specification_request.serialize_ec2_query(
            value["credit_specification"], pairs, f"{key_prefix}CreditSpecification"
        )
    if "cpu_options" in value:
        import capo_ec2.types.launch_template_cpu_options_request

        capo_ec2.types.launch_template_cpu_options_request.serialize_ec2_query(
            value["cpu_options"], pairs, f"{key_prefix}CpuOptions"
        )
    if "capacity_reservation_specification" in value:
        import capo_ec2.types.launch_template_capacity_reservation_specification_request

        capo_ec2.types.launch_template_capacity_reservation_specification_request.serialize_ec2_query(
            value["capacity_reservation_specification"],
            pairs,
            f"{key_prefix}CapacityReservationSpecification",
        )
    if "license_specifications" in value:
        import capo_ec2.types.launch_template_license_specification_list_request

        capo_ec2.types.launch_template_license_specification_list_request.serialize_ec2_query(
            value["license_specifications"], pairs, f"{key_prefix}LicenseSpecification"
        )
    if "hibernation_options" in value:
        import capo_ec2.types.launch_template_hibernation_options_request

        capo_ec2.types.launch_template_hibernation_options_request.serialize_ec2_query(
            value["hibernation_options"], pairs, f"{key_prefix}HibernationOptions"
        )
    if "metadata_options" in value:
        import capo_ec2.types.launch_template_instance_metadata_options_request

        capo_ec2.types.launch_template_instance_metadata_options_request.serialize_ec2_query(
            value["metadata_options"], pairs, f"{key_prefix}MetadataOptions"
        )
    if "enclave_options" in value:
        import capo_ec2.types.launch_template_enclave_options_request

        capo_ec2.types.launch_template_enclave_options_request.serialize_ec2_query(
            value["enclave_options"], pairs, f"{key_prefix}EnclaveOptions"
        )
    if "instance_requirements" in value:
        import capo_ec2.types.instance_requirements_request

        capo_ec2.types.instance_requirements_request.serialize_ec2_query(
            value["instance_requirements"], pairs, f"{key_prefix}InstanceRequirements"
        )
    if "private_dns_name_options" in value:
        import capo_ec2.types.launch_template_private_dns_name_options_request

        capo_ec2.types.launch_template_private_dns_name_options_request.serialize_ec2_query(
            value["private_dns_name_options"],
            pairs,
            f"{key_prefix}PrivateDnsNameOptions",
        )
    if "maintenance_options" in value:
        import capo_ec2.types.launch_template_instance_maintenance_options_request

        capo_ec2.types.launch_template_instance_maintenance_options_request.serialize_ec2_query(
            value["maintenance_options"], pairs, f"{key_prefix}MaintenanceOptions"
        )
    if "disable_api_stop" in value:
        pairs.append(
            (
                f"{key_prefix}DisableApiStop",
                "true" if value["disable_api_stop"] else "false",
            )
        )
    if "operator" in value:
        import capo_ec2.types.operator_request

        capo_ec2.types.operator_request.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "network_performance_options" in value:
        import capo_ec2.types.launch_template_network_performance_options_request

        capo_ec2.types.launch_template_network_performance_options_request.serialize_ec2_query(
            value["network_performance_options"],
            pairs,
            f"{key_prefix}NetworkPerformanceOptions",
        )
    if "secondary_interfaces" in value:
        import capo_ec2.types.launch_template_instance_secondary_interface_specification_request_list

        capo_ec2.types.launch_template_instance_secondary_interface_specification_request_list.serialize_ec2_query(
            value["secondary_interfaces"], pairs, f"{key_prefix}SecondaryInterface"
        )


def deserialize_ec2_query(el: Element) -> RequestLaunchTemplateData:
    out: RequestLaunchTemplateData = {}  # type: ignore[typeddict-item]
    child_kernel_id = el.find("KernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.launch_template_iam_instance_profile_specification_request

        out["iam_instance_profile"] = (
            capo_ec2.types.launch_template_iam_instance_profile_specification_request.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_block_device_mappings = el.find("BlockDeviceMapping")
    if child_block_device_mappings is not None:
        import capo_ec2.types.launch_template_block_device_mapping_request_list

        out["block_device_mappings"] = (
            capo_ec2.types.launch_template_block_device_mapping_request_list.deserialize_ec2_query(
                child_block_device_mappings
            )
        )
    child_network_interfaces = el.find("NetworkInterface")
    if child_network_interfaces is not None:
        import capo_ec2.types.launch_template_instance_network_interface_specification_request_list

        out["network_interfaces"] = (
            capo_ec2.types.launch_template_instance_network_interface_specification_request_list.deserialize_ec2_query(
                child_network_interfaces
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_monitoring = el.find("Monitoring")
    if child_monitoring is not None:
        import capo_ec2.types.launch_templates_monitoring_request

        out["monitoring"] = (
            capo_ec2.types.launch_templates_monitoring_request.deserialize_ec2_query(
                child_monitoring
            )
        )
    child_placement = el.find("Placement")
    if child_placement is not None:
        import capo_ec2.types.launch_template_placement_request

        out["placement"] = (
            capo_ec2.types.launch_template_placement_request.deserialize_ec2_query(
                child_placement
            )
        )
    child_ram_disk_id = el.find("RamDiskId")
    if child_ram_disk_id is not None:
        out["ram_disk_id"] = str(child_ram_disk_id.text or "")
    child_disable_api_termination = el.find("DisableApiTermination")
    if child_disable_api_termination is not None:
        out["disable_api_termination"] = (
            child_disable_api_termination.text or ""
        ).lower() == "true"
    child_instance_initiated_shutdown_behavior = el.find(
        "InstanceInitiatedShutdownBehavior"
    )
    if child_instance_initiated_shutdown_behavior is not None:
        import capo_ec2.types.shutdown_behavior

        out["instance_initiated_shutdown_behavior"] = (
            capo_ec2.types.shutdown_behavior.deserialize_ec2_query(
                child_instance_initiated_shutdown_behavior
            )
        )
    child_user_data = el.find("UserData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.launch_template_tag_specification_request_list

        out["tag_specifications"] = (
            capo_ec2.types.launch_template_tag_specification_request_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_elastic_gpu_specifications = el.find("ElasticGpuSpecification")
    if child_elastic_gpu_specifications is not None:
        import capo_ec2.types.elastic_gpu_specification_list

        out["elastic_gpu_specifications"] = (
            capo_ec2.types.elastic_gpu_specification_list.deserialize_ec2_query(
                child_elastic_gpu_specifications
            )
        )
    child_elastic_inference_accelerators = el.find("ElasticInferenceAccelerator")
    if child_elastic_inference_accelerators is not None:
        import capo_ec2.types.launch_template_elastic_inference_accelerator_list

        out["elastic_inference_accelerators"] = (
            capo_ec2.types.launch_template_elastic_inference_accelerator_list.deserialize_ec2_query(
                child_elastic_inference_accelerators
            )
        )
    child_security_group_ids = el.find("SecurityGroupId")
    if child_security_group_ids is not None:
        import capo_ec2.types.security_group_id_string_list

        out["security_group_ids"] = (
            capo_ec2.types.security_group_id_string_list.deserialize_ec2_query(
                child_security_group_ids
            )
        )
    child_security_groups = el.find("SecurityGroup")
    if child_security_groups is not None:
        import capo_ec2.types.security_group_string_list

        out["security_groups"] = (
            capo_ec2.types.security_group_string_list.deserialize_ec2_query(
                child_security_groups
            )
        )
    child_instance_market_options = el.find("InstanceMarketOptions")
    if child_instance_market_options is not None:
        import capo_ec2.types.launch_template_instance_market_options_request

        out["instance_market_options"] = (
            capo_ec2.types.launch_template_instance_market_options_request.deserialize_ec2_query(
                child_instance_market_options
            )
        )
    child_credit_specification = el.find("CreditSpecification")
    if child_credit_specification is not None:
        import capo_ec2.types.credit_specification_request

        out["credit_specification"] = (
            capo_ec2.types.credit_specification_request.deserialize_ec2_query(
                child_credit_specification
            )
        )
    child_cpu_options = el.find("CpuOptions")
    if child_cpu_options is not None:
        import capo_ec2.types.launch_template_cpu_options_request

        out["cpu_options"] = (
            capo_ec2.types.launch_template_cpu_options_request.deserialize_ec2_query(
                child_cpu_options
            )
        )
    child_capacity_reservation_specification = el.find(
        "CapacityReservationSpecification"
    )
    if child_capacity_reservation_specification is not None:
        import capo_ec2.types.launch_template_capacity_reservation_specification_request

        out["capacity_reservation_specification"] = (
            capo_ec2.types.launch_template_capacity_reservation_specification_request.deserialize_ec2_query(
                child_capacity_reservation_specification
            )
        )
    child_license_specifications = el.find("LicenseSpecification")
    if child_license_specifications is not None:
        import capo_ec2.types.launch_template_license_specification_list_request

        out["license_specifications"] = (
            capo_ec2.types.launch_template_license_specification_list_request.deserialize_ec2_query(
                child_license_specifications
            )
        )
    child_hibernation_options = el.find("HibernationOptions")
    if child_hibernation_options is not None:
        import capo_ec2.types.launch_template_hibernation_options_request

        out["hibernation_options"] = (
            capo_ec2.types.launch_template_hibernation_options_request.deserialize_ec2_query(
                child_hibernation_options
            )
        )
    child_metadata_options = el.find("MetadataOptions")
    if child_metadata_options is not None:
        import capo_ec2.types.launch_template_instance_metadata_options_request

        out["metadata_options"] = (
            capo_ec2.types.launch_template_instance_metadata_options_request.deserialize_ec2_query(
                child_metadata_options
            )
        )
    child_enclave_options = el.find("EnclaveOptions")
    if child_enclave_options is not None:
        import capo_ec2.types.launch_template_enclave_options_request

        out["enclave_options"] = (
            capo_ec2.types.launch_template_enclave_options_request.deserialize_ec2_query(
                child_enclave_options
            )
        )
    child_instance_requirements = el.find("InstanceRequirements")
    if child_instance_requirements is not None:
        import capo_ec2.types.instance_requirements_request

        out["instance_requirements"] = (
            capo_ec2.types.instance_requirements_request.deserialize_ec2_query(
                child_instance_requirements
            )
        )
    child_private_dns_name_options = el.find("PrivateDnsNameOptions")
    if child_private_dns_name_options is not None:
        import capo_ec2.types.launch_template_private_dns_name_options_request

        out["private_dns_name_options"] = (
            capo_ec2.types.launch_template_private_dns_name_options_request.deserialize_ec2_query(
                child_private_dns_name_options
            )
        )
    child_maintenance_options = el.find("MaintenanceOptions")
    if child_maintenance_options is not None:
        import capo_ec2.types.launch_template_instance_maintenance_options_request

        out["maintenance_options"] = (
            capo_ec2.types.launch_template_instance_maintenance_options_request.deserialize_ec2_query(
                child_maintenance_options
            )
        )
    child_disable_api_stop = el.find("DisableApiStop")
    if child_disable_api_stop is not None:
        out["disable_api_stop"] = (child_disable_api_stop.text or "").lower() == "true"
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_request

        out["operator"] = capo_ec2.types.operator_request.deserialize_ec2_query(
            child_operator
        )
    child_network_performance_options = el.find("NetworkPerformanceOptions")
    if child_network_performance_options is not None:
        import capo_ec2.types.launch_template_network_performance_options_request

        out["network_performance_options"] = (
            capo_ec2.types.launch_template_network_performance_options_request.deserialize_ec2_query(
                child_network_performance_options
            )
        )
    child_secondary_interfaces = el.find("SecondaryInterface")
    if child_secondary_interfaces is not None:
        import capo_ec2.types.launch_template_instance_secondary_interface_specification_request_list

        out["secondary_interfaces"] = (
            capo_ec2.types.launch_template_instance_secondary_interface_specification_request_list.deserialize_ec2_query(
                child_secondary_interfaces
            )
        )
    return out
