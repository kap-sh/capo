"""Generated from Smithy shape ``com.amazonaws.ec2#ResponseLaunchTemplateData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.credit_specification
    import capo_ec2.types.elastic_gpu_specification_response_list
    import capo_ec2.types.instance_requirements
    import capo_ec2.types.instance_type
    import capo_ec2.types.launch_template_block_device_mapping_list
    import capo_ec2.types.launch_template_capacity_reservation_specification_response
    import capo_ec2.types.launch_template_cpu_options
    import capo_ec2.types.launch_template_elastic_inference_accelerator_response_list
    import capo_ec2.types.launch_template_enclave_options
    import capo_ec2.types.launch_template_hibernation_options
    import capo_ec2.types.launch_template_iam_instance_profile_specification
    import capo_ec2.types.launch_template_instance_maintenance_options
    import capo_ec2.types.launch_template_instance_market_options
    import capo_ec2.types.launch_template_instance_metadata_options
    import capo_ec2.types.launch_template_instance_network_interface_specification_list
    import capo_ec2.types.launch_template_instance_secondary_interface_specification_list
    import capo_ec2.types.launch_template_license_list
    import capo_ec2.types.launch_template_network_performance_options
    import capo_ec2.types.launch_template_placement
    import capo_ec2.types.launch_template_private_dns_name_options
    import capo_ec2.types.launch_template_tag_specification_list
    import capo_ec2.types.launch_templates_monitoring
    import capo_ec2.types.operator_response
    import capo_ec2.types.sensitive_user_data
    import capo_ec2.types.shutdown_behavior
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class ResponseLaunchTemplateData(TypedDict, closed=True):
    kernel_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the kernel, if applicable.</p>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O. </p>"""
    iam_instance_profile: NotRequired[
        "capo_ec2.types.launch_template_iam_instance_profile_specification.LaunchTemplateIamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.launch_template_block_device_mapping_list.LaunchTemplateBlockDeviceMappingList"
    ]
    """<p>The block device mappings.</p>"""
    network_interfaces: NotRequired[
        "capo_ec2.types.launch_template_instance_network_interface_specification_list.LaunchTemplateInstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces.</p>"""
    image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI or a Systems Manager parameter. The Systems Manager parameter will resolve to the ID of the AMI at instance launch.</p> <p>The value depends on what you specified in the request. The possible values are:</p> <ul> <li> <p>If an AMI ID was specified in the request, then this is the AMI ID.</p> </li> <li> <p>If a Systems Manager parameter was specified in the request, and <code>ResolveAlias</code> was configured as <code>true</code>, then this is the AMI ID that the parameter is mapped to in the Parameter Store.</p> </li> <li> <p>If a Systems Manager parameter was specified in the request, and <code>ResolveAlias</code> was configured as <code>false</code>, then this is the parameter value.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    key_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the key pair.</p>"""
    monitoring: NotRequired[
        "capo_ec2.types.launch_templates_monitoring.LaunchTemplatesMonitoring"
    ]
    """<p>The monitoring for the instance.</p>"""
    placement: NotRequired[
        "capo_ec2.types.launch_template_placement.LaunchTemplatePlacement"
    ]
    """<p>The placement of the instance.</p>"""
    ram_disk_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the RAM disk, if applicable.</p>"""
    disable_api_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If set to <code>true</code>, indicates that the instance cannot be terminated using the Amazon EC2 console, command line tool, or API.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "capo_ec2.types.shutdown_behavior.ShutdownBehavior"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p>"""
    user_data: NotRequired["capo_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The user data for the instance. </p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.launch_template_tag_specification_list.LaunchTemplateTagSpecificationList"
    ]
    """<p>The tags that are applied to the resources that are created during instance launch.</p>"""
    elastic_gpu_specifications: NotRequired[
        "capo_ec2.types.elastic_gpu_specification_response_list.ElasticGpuSpecificationResponseList"
    ]
    """<p>Deprecated.</p> <note> <p>Amazon Elastic Graphics reached end of life on January 8, 2024.</p> </note>"""
    elastic_inference_accelerators: NotRequired[
        "capo_ec2.types.launch_template_elastic_inference_accelerator_response_list.LaunchTemplateElasticInferenceAcceleratorResponseList"
    ]
    """<note> <p>Amazon Elastic Inference is no longer available.</p> </note> <p>An elastic inference accelerator to associate with the instance. Elastic inference accelerators are a resource you can attach to your Amazon EC2 instances to accelerate your Deep Learning (DL) inference workloads.</p> <p>You cannot specify accelerators from different generations in the same request.</p>"""
    security_group_ids: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The security group IDs.</p>"""
    security_groups: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The security group names.</p>"""
    instance_market_options: NotRequired[
        "capo_ec2.types.launch_template_instance_market_options.LaunchTemplateInstanceMarketOptions"
    ]
    """<p>The market (purchasing) option for the instances.</p>"""
    credit_specification: NotRequired[
        "capo_ec2.types.credit_specification.CreditSpecification"
    ]
    """<p>The credit option for CPU usage of the instance.</p>"""
    cpu_options: NotRequired[
        "capo_ec2.types.launch_template_cpu_options.LaunchTemplateCpuOptions"
    ]
    """<p>The CPU options for the instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html">CPU options for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_reservation_specification: NotRequired[
        "capo_ec2.types.launch_template_capacity_reservation_specification_response.LaunchTemplateCapacityReservationSpecificationResponse"
    ]
    """<p>Information about the Capacity Reservation targeting option.</p>"""
    license_specifications: NotRequired[
        "capo_ec2.types.launch_template_license_list.LaunchTemplateLicenseList"
    ]
    """<p>The license configurations.</p>"""
    hibernation_options: NotRequired[
        "capo_ec2.types.launch_template_hibernation_options.LaunchTemplateHibernationOptions"
    ]
    """<p>Indicates whether an instance is configured for hibernation. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html">Hibernate your Amazon EC2 instance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    metadata_options: NotRequired[
        "capo_ec2.types.launch_template_instance_metadata_options.LaunchTemplateInstanceMetadataOptions"
    ]
    """<p>The metadata options for the instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html">Configure the Instance Metadata Service options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    enclave_options: NotRequired[
        "capo_ec2.types.launch_template_enclave_options.LaunchTemplateEnclaveOptions"
    ]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.</p>"""
    instance_requirements: NotRequired[
        "capo_ec2.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with these attributes.</p> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceTypes</code>.</p>"""
    private_dns_name_options: NotRequired[
        "capo_ec2.types.launch_template_private_dns_name_options.LaunchTemplatePrivateDnsNameOptions"
    ]
    """<p>The options for the instance hostname.</p>"""
    maintenance_options: NotRequired[
        "capo_ec2.types.launch_template_instance_maintenance_options.LaunchTemplateInstanceMaintenanceOptions"
    ]
    """<p>The maintenance options for your instance.</p>"""
    disable_api_stop: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is enabled for stop protection. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html">Enable stop protection for your EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The entity that manages the launch template.</p>"""
    network_performance_options: NotRequired[
        "capo_ec2.types.launch_template_network_performance_options.LaunchTemplateNetworkPerformanceOptions"
    ]
    """<p>Contains the launch template settings for network performance options for your instance.</p>"""
    secondary_interfaces: NotRequired[
        "capo_ec2.types.launch_template_instance_secondary_interface_specification_list.LaunchTemplateInstanceSecondaryInterfaceSpecificationList"
    ]
    """<p>The secondary interfaces associated with the launch template.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResponseLaunchTemplateData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "kernel_id" in value:
        pairs.append((f"{key_prefix}KernelId", str(value["kernel_id"])))
    if "ebs_optimized" in value:
        pairs.append(
            (f"{key_prefix}EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "iam_instance_profile" in value:
        import capo_ec2.types.launch_template_iam_instance_profile_specification

        capo_ec2.types.launch_template_iam_instance_profile_specification.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "block_device_mappings" in value:
        import capo_ec2.types.launch_template_block_device_mapping_list

        capo_ec2.types.launch_template_block_device_mapping_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMappingSet"
        )
    if "network_interfaces" in value:
        import capo_ec2.types.launch_template_instance_network_interface_specification_list

        capo_ec2.types.launch_template_instance_network_interface_specification_list.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{key_prefix}NetworkInterfaceSet"
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
        import capo_ec2.types.launch_templates_monitoring

        capo_ec2.types.launch_templates_monitoring.serialize_ec2_query(
            value["monitoring"], pairs, f"{key_prefix}Monitoring"
        )
    if "placement" in value:
        import capo_ec2.types.launch_template_placement

        capo_ec2.types.launch_template_placement.serialize_ec2_query(
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
        import capo_ec2.types.launch_template_tag_specification_list

        capo_ec2.types.launch_template_tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecificationSet"
        )
    if "elastic_gpu_specifications" in value:
        import capo_ec2.types.elastic_gpu_specification_response_list

        capo_ec2.types.elastic_gpu_specification_response_list.serialize_ec2_query(
            value["elastic_gpu_specifications"],
            pairs,
            f"{key_prefix}ElasticGpuSpecificationSet",
        )
    if "elastic_inference_accelerators" in value:
        import capo_ec2.types.launch_template_elastic_inference_accelerator_response_list

        capo_ec2.types.launch_template_elastic_inference_accelerator_response_list.serialize_ec2_query(
            value["elastic_inference_accelerators"],
            pairs,
            f"{key_prefix}ElasticInferenceAcceleratorSet",
        )
    if "security_group_ids" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupIdSet"
        )
    if "security_groups" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroupSet"
        )
    if "instance_market_options" in value:
        import capo_ec2.types.launch_template_instance_market_options

        capo_ec2.types.launch_template_instance_market_options.serialize_ec2_query(
            value["instance_market_options"],
            pairs,
            f"{key_prefix}InstanceMarketOptions",
        )
    if "credit_specification" in value:
        import capo_ec2.types.credit_specification

        capo_ec2.types.credit_specification.serialize_ec2_query(
            value["credit_specification"], pairs, f"{key_prefix}CreditSpecification"
        )
    if "cpu_options" in value:
        import capo_ec2.types.launch_template_cpu_options

        capo_ec2.types.launch_template_cpu_options.serialize_ec2_query(
            value["cpu_options"], pairs, f"{key_prefix}CpuOptions"
        )
    if "capacity_reservation_specification" in value:
        import capo_ec2.types.launch_template_capacity_reservation_specification_response

        capo_ec2.types.launch_template_capacity_reservation_specification_response.serialize_ec2_query(
            value["capacity_reservation_specification"],
            pairs,
            f"{key_prefix}CapacityReservationSpecification",
        )
    if "license_specifications" in value:
        import capo_ec2.types.launch_template_license_list

        capo_ec2.types.launch_template_license_list.serialize_ec2_query(
            value["license_specifications"], pairs, f"{key_prefix}LicenseSet"
        )
    if "hibernation_options" in value:
        import capo_ec2.types.launch_template_hibernation_options

        capo_ec2.types.launch_template_hibernation_options.serialize_ec2_query(
            value["hibernation_options"], pairs, f"{key_prefix}HibernationOptions"
        )
    if "metadata_options" in value:
        import capo_ec2.types.launch_template_instance_metadata_options

        capo_ec2.types.launch_template_instance_metadata_options.serialize_ec2_query(
            value["metadata_options"], pairs, f"{key_prefix}MetadataOptions"
        )
    if "enclave_options" in value:
        import capo_ec2.types.launch_template_enclave_options

        capo_ec2.types.launch_template_enclave_options.serialize_ec2_query(
            value["enclave_options"], pairs, f"{key_prefix}EnclaveOptions"
        )
    if "instance_requirements" in value:
        import capo_ec2.types.instance_requirements

        capo_ec2.types.instance_requirements.serialize_ec2_query(
            value["instance_requirements"], pairs, f"{key_prefix}InstanceRequirements"
        )
    if "private_dns_name_options" in value:
        import capo_ec2.types.launch_template_private_dns_name_options

        capo_ec2.types.launch_template_private_dns_name_options.serialize_ec2_query(
            value["private_dns_name_options"],
            pairs,
            f"{key_prefix}PrivateDnsNameOptions",
        )
    if "maintenance_options" in value:
        import capo_ec2.types.launch_template_instance_maintenance_options

        capo_ec2.types.launch_template_instance_maintenance_options.serialize_ec2_query(
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
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "network_performance_options" in value:
        import capo_ec2.types.launch_template_network_performance_options

        capo_ec2.types.launch_template_network_performance_options.serialize_ec2_query(
            value["network_performance_options"],
            pairs,
            f"{key_prefix}NetworkPerformanceOptions",
        )
    if "secondary_interfaces" in value:
        import capo_ec2.types.launch_template_instance_secondary_interface_specification_list

        capo_ec2.types.launch_template_instance_secondary_interface_specification_list.serialize_ec2_query(
            value["secondary_interfaces"], pairs, f"{key_prefix}SecondaryInterfaceSet"
        )


def deserialize_ec2_query(el: Element) -> ResponseLaunchTemplateData:
    out: ResponseLaunchTemplateData = {}  # type: ignore[typeddict-item]
    child_kernel_id = el.find("kernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_ebs_optimized = el.find("ebsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_iam_instance_profile = el.find("iamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.launch_template_iam_instance_profile_specification

        out["iam_instance_profile"] = (
            capo_ec2.types.launch_template_iam_instance_profile_specification.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_block_device_mappings = el.find("blockDeviceMappingSet")
    if child_block_device_mappings is not None:
        import capo_ec2.types.launch_template_block_device_mapping_list

        out["block_device_mappings"] = (
            capo_ec2.types.launch_template_block_device_mapping_list.deserialize_ec2_query(
                child_block_device_mappings
            )
        )
    child_network_interfaces = el.find("networkInterfaceSet")
    if child_network_interfaces is not None:
        import capo_ec2.types.launch_template_instance_network_interface_specification_list

        out["network_interfaces"] = (
            capo_ec2.types.launch_template_instance_network_interface_specification_list.deserialize_ec2_query(
                child_network_interfaces
            )
        )
    child_image_id = el.find("imageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_key_name = el.find("keyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_monitoring = el.find("monitoring")
    if child_monitoring is not None:
        import capo_ec2.types.launch_templates_monitoring

        out["monitoring"] = (
            capo_ec2.types.launch_templates_monitoring.deserialize_ec2_query(
                child_monitoring
            )
        )
    child_placement = el.find("placement")
    if child_placement is not None:
        import capo_ec2.types.launch_template_placement

        out["placement"] = (
            capo_ec2.types.launch_template_placement.deserialize_ec2_query(
                child_placement
            )
        )
    child_ram_disk_id = el.find("ramDiskId")
    if child_ram_disk_id is not None:
        out["ram_disk_id"] = str(child_ram_disk_id.text or "")
    child_disable_api_termination = el.find("disableApiTermination")
    if child_disable_api_termination is not None:
        out["disable_api_termination"] = (
            child_disable_api_termination.text or ""
        ).lower() == "true"
    child_instance_initiated_shutdown_behavior = el.find(
        "instanceInitiatedShutdownBehavior"
    )
    if child_instance_initiated_shutdown_behavior is not None:
        import capo_ec2.types.shutdown_behavior

        out["instance_initiated_shutdown_behavior"] = (
            capo_ec2.types.shutdown_behavior.deserialize_ec2_query(
                child_instance_initiated_shutdown_behavior
            )
        )
    child_user_data = el.find("userData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    child_tag_specifications = el.find("tagSpecificationSet")
    if child_tag_specifications is not None:
        import capo_ec2.types.launch_template_tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.launch_template_tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_elastic_gpu_specifications = el.find("elasticGpuSpecificationSet")
    if child_elastic_gpu_specifications is not None:
        import capo_ec2.types.elastic_gpu_specification_response_list

        out["elastic_gpu_specifications"] = (
            capo_ec2.types.elastic_gpu_specification_response_list.deserialize_ec2_query(
                child_elastic_gpu_specifications
            )
        )
    child_elastic_inference_accelerators = el.find("elasticInferenceAcceleratorSet")
    if child_elastic_inference_accelerators is not None:
        import capo_ec2.types.launch_template_elastic_inference_accelerator_response_list

        out["elastic_inference_accelerators"] = (
            capo_ec2.types.launch_template_elastic_inference_accelerator_response_list.deserialize_ec2_query(
                child_elastic_inference_accelerators
            )
        )
    child_security_group_ids = el.find("securityGroupIdSet")
    if child_security_group_ids is not None:
        import capo_ec2.types.value_string_list

        out["security_group_ids"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_security_group_ids
            )
        )
    child_security_groups = el.find("securityGroupSet")
    if child_security_groups is not None:
        import capo_ec2.types.value_string_list

        out["security_groups"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            child_security_groups
        )
    child_instance_market_options = el.find("instanceMarketOptions")
    if child_instance_market_options is not None:
        import capo_ec2.types.launch_template_instance_market_options

        out["instance_market_options"] = (
            capo_ec2.types.launch_template_instance_market_options.deserialize_ec2_query(
                child_instance_market_options
            )
        )
    child_credit_specification = el.find("creditSpecification")
    if child_credit_specification is not None:
        import capo_ec2.types.credit_specification

        out["credit_specification"] = (
            capo_ec2.types.credit_specification.deserialize_ec2_query(
                child_credit_specification
            )
        )
    child_cpu_options = el.find("cpuOptions")
    if child_cpu_options is not None:
        import capo_ec2.types.launch_template_cpu_options

        out["cpu_options"] = (
            capo_ec2.types.launch_template_cpu_options.deserialize_ec2_query(
                child_cpu_options
            )
        )
    child_capacity_reservation_specification = el.find(
        "capacityReservationSpecification"
    )
    if child_capacity_reservation_specification is not None:
        import capo_ec2.types.launch_template_capacity_reservation_specification_response

        out["capacity_reservation_specification"] = (
            capo_ec2.types.launch_template_capacity_reservation_specification_response.deserialize_ec2_query(
                child_capacity_reservation_specification
            )
        )
    child_license_specifications = el.find("licenseSet")
    if child_license_specifications is not None:
        import capo_ec2.types.launch_template_license_list

        out["license_specifications"] = (
            capo_ec2.types.launch_template_license_list.deserialize_ec2_query(
                child_license_specifications
            )
        )
    child_hibernation_options = el.find("hibernationOptions")
    if child_hibernation_options is not None:
        import capo_ec2.types.launch_template_hibernation_options

        out["hibernation_options"] = (
            capo_ec2.types.launch_template_hibernation_options.deserialize_ec2_query(
                child_hibernation_options
            )
        )
    child_metadata_options = el.find("metadataOptions")
    if child_metadata_options is not None:
        import capo_ec2.types.launch_template_instance_metadata_options

        out["metadata_options"] = (
            capo_ec2.types.launch_template_instance_metadata_options.deserialize_ec2_query(
                child_metadata_options
            )
        )
    child_enclave_options = el.find("enclaveOptions")
    if child_enclave_options is not None:
        import capo_ec2.types.launch_template_enclave_options

        out["enclave_options"] = (
            capo_ec2.types.launch_template_enclave_options.deserialize_ec2_query(
                child_enclave_options
            )
        )
    child_instance_requirements = el.find("instanceRequirements")
    if child_instance_requirements is not None:
        import capo_ec2.types.instance_requirements

        out["instance_requirements"] = (
            capo_ec2.types.instance_requirements.deserialize_ec2_query(
                child_instance_requirements
            )
        )
    child_private_dns_name_options = el.find("privateDnsNameOptions")
    if child_private_dns_name_options is not None:
        import capo_ec2.types.launch_template_private_dns_name_options

        out["private_dns_name_options"] = (
            capo_ec2.types.launch_template_private_dns_name_options.deserialize_ec2_query(
                child_private_dns_name_options
            )
        )
    child_maintenance_options = el.find("maintenanceOptions")
    if child_maintenance_options is not None:
        import capo_ec2.types.launch_template_instance_maintenance_options

        out["maintenance_options"] = (
            capo_ec2.types.launch_template_instance_maintenance_options.deserialize_ec2_query(
                child_maintenance_options
            )
        )
    child_disable_api_stop = el.find("disableApiStop")
    if child_disable_api_stop is not None:
        out["disable_api_stop"] = (child_disable_api_stop.text or "").lower() == "true"
    child_operator = el.find("operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    child_network_performance_options = el.find("networkPerformanceOptions")
    if child_network_performance_options is not None:
        import capo_ec2.types.launch_template_network_performance_options

        out["network_performance_options"] = (
            capo_ec2.types.launch_template_network_performance_options.deserialize_ec2_query(
                child_network_performance_options
            )
        )
    child_secondary_interfaces = el.find("secondaryInterfaceSet")
    if child_secondary_interfaces is not None:
        import capo_ec2.types.launch_template_instance_secondary_interface_specification_list

        out["secondary_interfaces"] = (
            capo_ec2.types.launch_template_instance_secondary_interface_specification_list.deserialize_ec2_query(
                child_secondary_interfaces
            )
        )
    return out
