"""Generated from Smithy shape ``com.amazonaws.ec2#RunInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.block_device_mapping_request_list
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_specification
    import capo_ec2.types.cpu_options_request
    import capo_ec2.types.credit_specification_request
    import capo_ec2.types.elastic_gpu_specifications
    import capo_ec2.types.elastic_inference_accelerators
    import capo_ec2.types.enclave_options_request
    import capo_ec2.types.hibernation_options_request
    import capo_ec2.types.iam_instance_profile_specification
    import capo_ec2.types.image_id
    import capo_ec2.types.instance_ipv6_address_list
    import capo_ec2.types.instance_maintenance_options_request
    import capo_ec2.types.instance_market_options_request
    import capo_ec2.types.instance_metadata_options_request
    import capo_ec2.types.instance_network_interface_specification_list
    import capo_ec2.types.instance_network_performance_options_request
    import capo_ec2.types.instance_secondary_interface_specification_list_request
    import capo_ec2.types.instance_type
    import capo_ec2.types.integer
    import capo_ec2.types.kernel_id
    import capo_ec2.types.key_pair_name
    import capo_ec2.types.launch_template_specification
    import capo_ec2.types.license_specification_list_request
    import capo_ec2.types.operator_request
    import capo_ec2.types.placement
    import capo_ec2.types.private_dns_name_options_request
    import capo_ec2.types.ramdisk_id
    import capo_ec2.types.run_instances_monitoring_enabled
    import capo_ec2.types.run_instances_user_data
    import capo_ec2.types.security_group_id_string_list
    import capo_ec2.types.security_group_string_list
    import capo_ec2.types.shutdown_behavior
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id
    import capo_ec2.types.tag_specification_list


class RunInstancesRequest(TypedDict, closed=True):
    block_device_mappings: NotRequired[
        "capo_ec2.types.block_device_mapping_request_list.BlockDeviceMappingRequestList"
    ]
    """<p>The block device mapping, which defines the EBS volumes and instance store volumes to attach to the instance at launch. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html">Block device mappings</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI. An AMI ID is required to launch an instance and must be specified here or in a launch template.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html">Amazon EC2 Instance Types Guide</a>.</p>"""
    ipv6_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet. You cannot specify this option and the option to assign specific IPv6 addresses in the same request. You can specify this option if you've specified a minimum number of instances to launch.</p> <p>You cannot specify this option and the network interfaces option in the same request.</p>"""
    ipv6_addresses: NotRequired[
        "capo_ec2.types.instance_ipv6_address_list.InstanceIpv6AddressList"
    ]
    """<p>The IPv6 addresses from the range of the subnet to associate with the primary network interface. You cannot specify this option and the option to assign a number of IPv6 addresses in the same request. You cannot specify this option if you've specified a minimum number of instances to launch.</p> <p>You cannot specify this option and the network interfaces option in the same request.</p>"""
    kernel_id: NotRequired["capo_ec2.types.kernel_id.KernelId"]
    """<p>The ID of the kernel.</p> <important> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html">PV-GRUB</a> in the <i>Amazon EC2 User Guide</i>.</p> </important>"""
    key_name: NotRequired["capo_ec2.types.key_pair_name.KeyPairName"]
    """<p>The name of the key pair. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html">Create a key pair for your EC2 instance</a>.</p> <important> <p>If you do not specify a key pair, you can't connect to the instance unless you choose an AMI that is configured to allow users another way to log in.</p> </important>"""
    max_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of instances to launch. If you specify a value that is more capacity than Amazon EC2 can launch in the target Availability Zone, Amazon EC2 launches the largest possible number of instances above the specified minimum count.</p> <p>Constraints: Between 1 and the quota for the specified instance type for your account for this Region. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html">Amazon EC2 instance type quotas</a>.</p>"""
    min_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The minimum number of instances to launch. If you specify a value that is more capacity than Amazon EC2 can provide in the target Availability Zone, Amazon EC2 does not launch any instances.</p> <p>Constraints: Between 1 and the quota for the specified instance type for your account for this Region. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html">Amazon EC2 instance type quotas</a>.</p>"""
    monitoring: NotRequired[
        "capo_ec2.types.run_instances_monitoring_enabled.RunInstancesMonitoringEnabled"
    ]
    """<p>Specifies whether detailed monitoring is enabled for the instance.</p>"""
    placement: NotRequired["capo_ec2.types.placement.Placement"]
    """<p>The placement for the instance.</p>"""
    ramdisk_id: NotRequired["capo_ec2.types.ramdisk_id.RamdiskId"]
    """<p>The ID of the RAM disk to select. Some kernels require additional drivers at launch. Check the kernel requirements for information about whether you need to specify a RAM disk. To find kernel requirements, go to the Amazon Web Services Resource Center and search for the kernel ID.</p> <important> <p>We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html">PV-GRUB</a> in the <i>Amazon EC2 User Guide</i>.</p> </important>"""
    security_group_ids: NotRequired[
        "capo_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The IDs of the security groups.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p>"""
    security_groups: NotRequired[
        "capo_ec2.types.security_group_string_list.SecurityGroupStringList"
    ]
    """<p>[Default VPC] The names of the security groups.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p> <p>Default: Amazon EC2 uses the default security group.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet to launch the instance into.</p> <p>If you specify a network interface, you must specify any subnets as part of the network interface instead of using this parameter.</p>"""
    user_data: NotRequired[
        "capo_ec2.types.run_instances_user_data.RunInstancesUserData"
    ]
    """<p>The user data to make available to the instance. User data must be base64-encoded. Depending on the tool or SDK that you're using, the base64-encoding might be performed for you. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html">Run commands at launch using instance user data</a>.</p>"""
    elastic_gpu_specification: NotRequired[
        "capo_ec2.types.elastic_gpu_specifications.ElasticGpuSpecifications"
    ]
    """<p>An elastic GPU to associate with the instance.</p> <note> <p>Amazon Elastic Graphics reached end of life on January 8, 2024.</p> </note>"""
    elastic_inference_accelerators: NotRequired[
        "capo_ec2.types.elastic_inference_accelerators.ElasticInferenceAccelerators"
    ]
    """<p>An elastic inference accelerator to associate with the instance.</p> <note> <p>Amazon Elastic Inference is no longer available.</p> </note>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the resources that are created during instance launch.</p> <p>You can specify tags for the following resources only:</p> <ul> <li> <p>Instances</p> </li> <li> <p>Volumes</p> </li> <li> <p>Spot Instance requests</p> </li> <li> <p>Network interfaces</p> </li> </ul> <p>To tag a resource after it has been created, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html">CreateTags</a>.</p>"""
    launch_template: NotRequired[
        "capo_ec2.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>The launch template. Any additional parameters that you specify for the new instance overwrite the corresponding parameters included in the launch template.</p>"""
    instance_market_options: NotRequired[
        "capo_ec2.types.instance_market_options_request.InstanceMarketOptionsRequest"
    ]
    """<p>The market (purchasing) option for the instances.</p> <p>For <a>RunInstances</a>, persistent Spot Instance requests are only supported when <b>InstanceInterruptionBehavior</b> is set to either <code>hibernate</code> or <code>stop</code>.</p>"""
    credit_specification: NotRequired[
        "capo_ec2.types.credit_specification_request.CreditSpecificationRequest"
    ]
    """<p>The credit option for CPU usage of the burstable performance instance. Valid values are <code>standard</code> and <code>unlimited</code>. To change this attribute after launch, use <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html"> ModifyInstanceCreditSpecification</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html">Burstable performance instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>standard</code> (T2 instances) or <code>unlimited</code> (T3/T3a/T4g instances)</p> <p>For T3 instances with <code>host</code> tenancy, only <code>standard</code> is supported.</p>"""
    cpu_options: NotRequired["capo_ec2.types.cpu_options_request.CpuOptionsRequest"]
    """<p>The CPU options for the instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html">Optimize CPU options</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_reservation_specification: NotRequired[
        "capo_ec2.types.capacity_reservation_specification.CapacityReservationSpecification"
    ]
    """<p>Information about the Capacity Reservation targeting option. If you do not specify this parameter, the instance's Capacity Reservation preference defaults to <code>open</code>, which enables it to run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, and tenancy).</p>"""
    hibernation_options: NotRequired[
        "capo_ec2.types.hibernation_options_request.HibernationOptionsRequest"
    ]
    """<p>Indicates whether an instance is enabled for hibernation. This parameter is valid only if the instance meets the <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html">hibernation prerequisites</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html">Hibernate your Amazon EC2 instance</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>You can't enable hibernation and Amazon Web Services Nitro Enclaves on the same instance.</p>"""
    license_specifications: NotRequired[
        "capo_ec2.types.license_specification_list_request.LicenseSpecificationListRequest"
    ]
    """<p>The license configurations.</p>"""
    metadata_options: NotRequired[
        "capo_ec2.types.instance_metadata_options_request.InstanceMetadataOptionsRequest"
    ]
    """<p>The metadata options for the instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html">Configure the Instance Metadata Service options</a>.</p>"""
    enclave_options: NotRequired[
        "capo_ec2.types.enclave_options_request.EnclaveOptionsRequest"
    ]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. For more information, see <a href="https://docs.aws.amazon.com/enclaves/latest/user/">Amazon Web Services Nitro Enclaves User Guide</a>.</p> <p>You can't enable Amazon Web Services Nitro Enclaves and hibernation on the same instance.</p>"""
    private_dns_name_options: NotRequired[
        "capo_ec2.types.private_dns_name_options_request.PrivateDnsNameOptionsRequest"
    ]
    """<p>The options for the instance hostname. The default values are inherited from the subnet. Applies only if creating a network interface, not attaching an existing one.</p>"""
    maintenance_options: NotRequired[
        "capo_ec2.types.instance_maintenance_options_request.InstanceMaintenanceOptionsRequest"
    ]
    """<p>The maintenance and recovery options for the instance.</p>"""
    disable_api_stop: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether an instance is enabled for stop protection. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html">Enable stop protection for your EC2 instances</a>.</p>"""
    enable_primary_ipv6: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If you’re launching an instance into a dual-stack or IPv6-only subnet, you can enable assigning a primary IPv6 address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if an instance relies on its IPv6 address not changing. When you launch the instance, Amazon Web Services will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.</p>"""
    network_performance_options: NotRequired[
        "capo_ec2.types.instance_network_performance_options_request.InstanceNetworkPerformanceOptionsRequest"
    ]
    """<p>Contains settings for the network performance options for the instance.</p>"""
    operator: NotRequired["capo_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    secondary_interfaces: NotRequired[
        "capo_ec2.types.instance_secondary_interface_specification_list_request.InstanceSecondaryInterfaceSpecificationListRequest"
    ]
    """<p>The secondary interfaces to associate with the instance.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    disable_api_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether termination protection is enabled for the instance. The default is <code>false</code>, which means that you can terminate the instance using the Amazon EC2 console, command line tools, or API. You can enable termination protection when you launch an instance, while the instance is running, or while the instance is stopped.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "capo_ec2.types.shutdown_behavior.ShutdownBehavior"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p> <p>Default: <code>stop</code> </p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.</p> <p>Only one private IP address can be designated as primary. You can't specify this option if you've specified the option to designate a private IP address as the primary IP address in a network interface specification. You cannot specify this option if you're launching more than one instance in the request.</p> <p>You cannot specify this option and the network interfaces option in the same request.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p> <p>Constraints: Maximum 64 ASCII characters</p>"""
    additional_info: NotRequired["capo_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    network_interfaces: NotRequired[
        "capo_ec2.types.instance_network_interface_specification_list.InstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces to associate with the instance.</p>"""
    iam_instance_profile: NotRequired[
        "capo_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The name or Amazon Resource Name (ARN) of an IAM instance profile.</p>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.</p> <p>Default: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RunInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "block_device_mappings" in value:
        import capo_ec2.types.block_device_mapping_request_list

        capo_ec2.types.block_device_mapping_request_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMapping"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "ipv6_address_count" in value:
        pairs.append(
            (f"{key_prefix}Ipv6AddressCount", str(value["ipv6_address_count"]))
        )
    if "ipv6_addresses" in value:
        import capo_ec2.types.instance_ipv6_address_list

        capo_ec2.types.instance_ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{key_prefix}Ipv6Address"
        )
    if "kernel_id" in value:
        pairs.append((f"{key_prefix}KernelId", str(value["kernel_id"])))
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "max_count" in value:
        pairs.append((f"{key_prefix}MaxCount", str(value["max_count"])))
    if "min_count" in value:
        pairs.append((f"{key_prefix}MinCount", str(value["min_count"])))
    if "monitoring" in value:
        import capo_ec2.types.run_instances_monitoring_enabled

        capo_ec2.types.run_instances_monitoring_enabled.serialize_ec2_query(
            value["monitoring"], pairs, f"{key_prefix}Monitoring"
        )
    if "placement" in value:
        import capo_ec2.types.placement

        capo_ec2.types.placement.serialize_ec2_query(
            value["placement"], pairs, f"{key_prefix}Placement"
        )
    if "ramdisk_id" in value:
        pairs.append((f"{key_prefix}RamdiskId", str(value["ramdisk_id"])))
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
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "user_data" in value:
        pairs.append((f"{key_prefix}UserData", str(value["user_data"])))
    if "elastic_gpu_specification" in value:
        import capo_ec2.types.elastic_gpu_specifications

        capo_ec2.types.elastic_gpu_specifications.serialize_ec2_query(
            value["elastic_gpu_specification"],
            pairs,
            f"{key_prefix}ElasticGpuSpecification",
        )
    if "elastic_inference_accelerators" in value:
        import capo_ec2.types.elastic_inference_accelerators

        capo_ec2.types.elastic_inference_accelerators.serialize_ec2_query(
            value["elastic_inference_accelerators"],
            pairs,
            f"{key_prefix}ElasticInferenceAccelerator",
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "launch_template" in value:
        import capo_ec2.types.launch_template_specification

        capo_ec2.types.launch_template_specification.serialize_ec2_query(
            value["launch_template"], pairs, f"{key_prefix}LaunchTemplate"
        )
    if "instance_market_options" in value:
        import capo_ec2.types.instance_market_options_request

        capo_ec2.types.instance_market_options_request.serialize_ec2_query(
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
        import capo_ec2.types.cpu_options_request

        capo_ec2.types.cpu_options_request.serialize_ec2_query(
            value["cpu_options"], pairs, f"{key_prefix}CpuOptions"
        )
    if "capacity_reservation_specification" in value:
        import capo_ec2.types.capacity_reservation_specification

        capo_ec2.types.capacity_reservation_specification.serialize_ec2_query(
            value["capacity_reservation_specification"],
            pairs,
            f"{key_prefix}CapacityReservationSpecification",
        )
    if "hibernation_options" in value:
        import capo_ec2.types.hibernation_options_request

        capo_ec2.types.hibernation_options_request.serialize_ec2_query(
            value["hibernation_options"], pairs, f"{key_prefix}HibernationOptions"
        )
    if "license_specifications" in value:
        import capo_ec2.types.license_specification_list_request

        capo_ec2.types.license_specification_list_request.serialize_ec2_query(
            value["license_specifications"], pairs, f"{key_prefix}LicenseSpecification"
        )
    if "metadata_options" in value:
        import capo_ec2.types.instance_metadata_options_request

        capo_ec2.types.instance_metadata_options_request.serialize_ec2_query(
            value["metadata_options"], pairs, f"{key_prefix}MetadataOptions"
        )
    if "enclave_options" in value:
        import capo_ec2.types.enclave_options_request

        capo_ec2.types.enclave_options_request.serialize_ec2_query(
            value["enclave_options"], pairs, f"{key_prefix}EnclaveOptions"
        )
    if "private_dns_name_options" in value:
        import capo_ec2.types.private_dns_name_options_request

        capo_ec2.types.private_dns_name_options_request.serialize_ec2_query(
            value["private_dns_name_options"],
            pairs,
            f"{key_prefix}PrivateDnsNameOptions",
        )
    if "maintenance_options" in value:
        import capo_ec2.types.instance_maintenance_options_request

        capo_ec2.types.instance_maintenance_options_request.serialize_ec2_query(
            value["maintenance_options"], pairs, f"{key_prefix}MaintenanceOptions"
        )
    if "disable_api_stop" in value:
        pairs.append(
            (
                f"{key_prefix}DisableApiStop",
                "true" if value["disable_api_stop"] else "false",
            )
        )
    if "enable_primary_ipv6" in value:
        pairs.append(
            (
                f"{key_prefix}EnablePrimaryIpv6",
                "true" if value["enable_primary_ipv6"] else "false",
            )
        )
    if "network_performance_options" in value:
        import capo_ec2.types.instance_network_performance_options_request

        capo_ec2.types.instance_network_performance_options_request.serialize_ec2_query(
            value["network_performance_options"],
            pairs,
            f"{key_prefix}NetworkPerformanceOptions",
        )
    if "operator" in value:
        import capo_ec2.types.operator_request

        capo_ec2.types.operator_request.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "secondary_interfaces" in value:
        import capo_ec2.types.instance_secondary_interface_specification_list_request

        capo_ec2.types.instance_secondary_interface_specification_list_request.serialize_ec2_query(
            value["secondary_interfaces"], pairs, f"{key_prefix}SecondaryInterface"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
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
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "additional_info" in value:
        pairs.append((f"{key_prefix}AdditionalInfo", str(value["additional_info"])))
    if "network_interfaces" in value:
        import capo_ec2.types.instance_network_interface_specification_list

        capo_ec2.types.instance_network_interface_specification_list.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{key_prefix}NetworkInterface"
        )
    if "iam_instance_profile" in value:
        import capo_ec2.types.iam_instance_profile_specification

        capo_ec2.types.iam_instance_profile_specification.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{key_prefix}EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )


def deserialize_ec2_query(el: Element) -> RunInstancesRequest:
    out: RunInstancesRequest = {}  # type: ignore[typeddict-item]
    child_block_device_mappings = el.find("BlockDeviceMapping")
    if child_block_device_mappings is not None:
        import capo_ec2.types.block_device_mapping_request_list

        out["block_device_mappings"] = (
            capo_ec2.types.block_device_mapping_request_list.deserialize_ec2_query(
                child_block_device_mappings
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
    child_ipv6_address_count = el.find("Ipv6AddressCount")
    if child_ipv6_address_count is not None:
        out["ipv6_address_count"] = int(child_ipv6_address_count.text or "")
    child_ipv6_addresses = el.find("Ipv6Address")
    if child_ipv6_addresses is not None:
        import capo_ec2.types.instance_ipv6_address_list

        out["ipv6_addresses"] = (
            capo_ec2.types.instance_ipv6_address_list.deserialize_ec2_query(
                child_ipv6_addresses
            )
        )
    child_kernel_id = el.find("KernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_max_count = el.find("MaxCount")
    if child_max_count is not None:
        out["max_count"] = int(child_max_count.text or "")
    child_min_count = el.find("MinCount")
    if child_min_count is not None:
        out["min_count"] = int(child_min_count.text or "")
    child_monitoring = el.find("Monitoring")
    if child_monitoring is not None:
        import capo_ec2.types.run_instances_monitoring_enabled

        out["monitoring"] = (
            capo_ec2.types.run_instances_monitoring_enabled.deserialize_ec2_query(
                child_monitoring
            )
        )
    child_placement = el.find("Placement")
    if child_placement is not None:
        import capo_ec2.types.placement

        out["placement"] = capo_ec2.types.placement.deserialize_ec2_query(
            child_placement
        )
    child_ramdisk_id = el.find("RamdiskId")
    if child_ramdisk_id is not None:
        out["ramdisk_id"] = str(child_ramdisk_id.text or "")
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
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_user_data = el.find("UserData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    child_elastic_gpu_specification = el.find("ElasticGpuSpecification")
    if child_elastic_gpu_specification is not None:
        import capo_ec2.types.elastic_gpu_specifications

        out["elastic_gpu_specification"] = (
            capo_ec2.types.elastic_gpu_specifications.deserialize_ec2_query(
                child_elastic_gpu_specification
            )
        )
    child_elastic_inference_accelerators = el.find("ElasticInferenceAccelerator")
    if child_elastic_inference_accelerators is not None:
        import capo_ec2.types.elastic_inference_accelerators

        out["elastic_inference_accelerators"] = (
            capo_ec2.types.elastic_inference_accelerators.deserialize_ec2_query(
                child_elastic_inference_accelerators
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import capo_ec2.types.launch_template_specification

        out["launch_template"] = (
            capo_ec2.types.launch_template_specification.deserialize_ec2_query(
                child_launch_template
            )
        )
    child_instance_market_options = el.find("InstanceMarketOptions")
    if child_instance_market_options is not None:
        import capo_ec2.types.instance_market_options_request

        out["instance_market_options"] = (
            capo_ec2.types.instance_market_options_request.deserialize_ec2_query(
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
        import capo_ec2.types.cpu_options_request

        out["cpu_options"] = capo_ec2.types.cpu_options_request.deserialize_ec2_query(
            child_cpu_options
        )
    child_capacity_reservation_specification = el.find(
        "CapacityReservationSpecification"
    )
    if child_capacity_reservation_specification is not None:
        import capo_ec2.types.capacity_reservation_specification

        out["capacity_reservation_specification"] = (
            capo_ec2.types.capacity_reservation_specification.deserialize_ec2_query(
                child_capacity_reservation_specification
            )
        )
    child_hibernation_options = el.find("HibernationOptions")
    if child_hibernation_options is not None:
        import capo_ec2.types.hibernation_options_request

        out["hibernation_options"] = (
            capo_ec2.types.hibernation_options_request.deserialize_ec2_query(
                child_hibernation_options
            )
        )
    child_license_specifications = el.find("LicenseSpecification")
    if child_license_specifications is not None:
        import capo_ec2.types.license_specification_list_request

        out["license_specifications"] = (
            capo_ec2.types.license_specification_list_request.deserialize_ec2_query(
                child_license_specifications
            )
        )
    child_metadata_options = el.find("MetadataOptions")
    if child_metadata_options is not None:
        import capo_ec2.types.instance_metadata_options_request

        out["metadata_options"] = (
            capo_ec2.types.instance_metadata_options_request.deserialize_ec2_query(
                child_metadata_options
            )
        )
    child_enclave_options = el.find("EnclaveOptions")
    if child_enclave_options is not None:
        import capo_ec2.types.enclave_options_request

        out["enclave_options"] = (
            capo_ec2.types.enclave_options_request.deserialize_ec2_query(
                child_enclave_options
            )
        )
    child_private_dns_name_options = el.find("PrivateDnsNameOptions")
    if child_private_dns_name_options is not None:
        import capo_ec2.types.private_dns_name_options_request

        out["private_dns_name_options"] = (
            capo_ec2.types.private_dns_name_options_request.deserialize_ec2_query(
                child_private_dns_name_options
            )
        )
    child_maintenance_options = el.find("MaintenanceOptions")
    if child_maintenance_options is not None:
        import capo_ec2.types.instance_maintenance_options_request

        out["maintenance_options"] = (
            capo_ec2.types.instance_maintenance_options_request.deserialize_ec2_query(
                child_maintenance_options
            )
        )
    child_disable_api_stop = el.find("DisableApiStop")
    if child_disable_api_stop is not None:
        out["disable_api_stop"] = (child_disable_api_stop.text or "").lower() == "true"
    child_enable_primary_ipv6 = el.find("EnablePrimaryIpv6")
    if child_enable_primary_ipv6 is not None:
        out["enable_primary_ipv6"] = (
            child_enable_primary_ipv6.text or ""
        ).lower() == "true"
    child_network_performance_options = el.find("NetworkPerformanceOptions")
    if child_network_performance_options is not None:
        import capo_ec2.types.instance_network_performance_options_request

        out["network_performance_options"] = (
            capo_ec2.types.instance_network_performance_options_request.deserialize_ec2_query(
                child_network_performance_options
            )
        )
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_request

        out["operator"] = capo_ec2.types.operator_request.deserialize_ec2_query(
            child_operator
        )
    child_secondary_interfaces = el.find("SecondaryInterface")
    if child_secondary_interfaces is not None:
        import capo_ec2.types.instance_secondary_interface_specification_list_request

        out["secondary_interfaces"] = (
            capo_ec2.types.instance_secondary_interface_specification_list_request.deserialize_ec2_query(
                child_secondary_interfaces
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
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
    child_private_ip_address = el.find("privateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_additional_info = el.find("additionalInfo")
    if child_additional_info is not None:
        out["additional_info"] = str(child_additional_info.text or "")
    child_network_interfaces = el.find("networkInterface")
    if child_network_interfaces is not None:
        import capo_ec2.types.instance_network_interface_specification_list

        out["network_interfaces"] = (
            capo_ec2.types.instance_network_interface_specification_list.deserialize_ec2_query(
                child_network_interfaces
            )
        )
    child_iam_instance_profile = el.find("iamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.iam_instance_profile_specification

        out["iam_instance_profile"] = (
            capo_ec2.types.iam_instance_profile_specification.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_ebs_optimized = el.find("ebsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    return out
