"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchSpecification``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.block_device_mapping_list
    import capo_ec2.types.boolean
    import capo_ec2.types.group_identifier_list
    import capo_ec2.types.iam_instance_profile_specification
    import capo_ec2.types.instance_network_interface_specification_list
    import capo_ec2.types.instance_type
    import capo_ec2.types.run_instances_monitoring_enabled
    import capo_ec2.types.sensitive_user_data
    import capo_ec2.types.spot_placement
    import capo_ec2.types.string


class LaunchSpecification(TypedDict, closed=True):
    user_data: NotRequired["capo_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The base64-encoded user data that instances use when starting up. User data is limited to 16 KB.</p>"""
    addressing_type: NotRequired["capo_ec2.types.string.String"]
    """<p>Deprecated.</p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>The block device mapping entries.</p>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.</p> <p>Default: <code>false</code> </p>"""
    iam_instance_profile: NotRequired[
        "capo_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. Only one instance type can be specified.</p>"""
    kernel_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the kernel.</p>"""
    key_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the key pair.</p>"""
    network_interfaces: NotRequired[
        "capo_ec2.types.instance_network_interface_specification_list.InstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.</p>"""
    placement: NotRequired["capo_ec2.types.spot_placement.SpotPlacement"]
    """<p>The placement information for the instance.</p>"""
    ramdisk_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the RAM disk.</p>"""
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the subnet in which to launch the instance.</p>"""
    security_groups: NotRequired[
        "capo_ec2.types.group_identifier_list.GroupIdentifierList"
    ]
    """<p>The IDs of the security groups.</p>"""
    monitoring: NotRequired[
        "capo_ec2.types.run_instances_monitoring_enabled.RunInstancesMonitoringEnabled"
    ]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_data" in value:
        pairs.append((f"{key_prefix}UserData", str(value["user_data"])))
    if "addressing_type" in value:
        pairs.append((f"{key_prefix}AddressingType", str(value["addressing_type"])))
    if "block_device_mappings" in value:
        import capo_ec2.types.block_device_mapping_list

        capo_ec2.types.block_device_mapping_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMapping"
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{key_prefix}EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "iam_instance_profile" in value:
        import capo_ec2.types.iam_instance_profile_specification

        capo_ec2.types.iam_instance_profile_specification.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "kernel_id" in value:
        pairs.append((f"{key_prefix}KernelId", str(value["kernel_id"])))
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "network_interfaces" in value:
        import capo_ec2.types.instance_network_interface_specification_list

        capo_ec2.types.instance_network_interface_specification_list.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{key_prefix}NetworkInterfaceSet"
        )
    if "placement" in value:
        import capo_ec2.types.spot_placement

        capo_ec2.types.spot_placement.serialize_ec2_query(
            value["placement"], pairs, f"{key_prefix}Placement"
        )
    if "ramdisk_id" in value:
        pairs.append((f"{key_prefix}RamdiskId", str(value["ramdisk_id"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "security_groups" in value:
        import capo_ec2.types.group_identifier_list

        capo_ec2.types.group_identifier_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{key_prefix}GroupSet"
        )
    if "monitoring" in value:
        import capo_ec2.types.run_instances_monitoring_enabled

        capo_ec2.types.run_instances_monitoring_enabled.serialize_ec2_query(
            value["monitoring"], pairs, f"{key_prefix}Monitoring"
        )


def deserialize_ec2_query(el: Element) -> LaunchSpecification:
    out: LaunchSpecification = {}  # type: ignore[typeddict-item]
    child_user_data = el.find("userData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    child_addressing_type = el.find("addressingType")
    if child_addressing_type is not None:
        out["addressing_type"] = str(child_addressing_type.text or "")
    child_block_device_mappings = el.find("blockDeviceMapping")
    if child_block_device_mappings is not None:
        import capo_ec2.types.block_device_mapping_list

        out["block_device_mappings"] = (
            capo_ec2.types.block_device_mapping_list.deserialize_ec2_query(
                child_block_device_mappings
            )
        )
    child_ebs_optimized = el.find("ebsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_iam_instance_profile = el.find("iamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.iam_instance_profile_specification

        out["iam_instance_profile"] = (
            capo_ec2.types.iam_instance_profile_specification.deserialize_ec2_query(
                child_iam_instance_profile
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
    child_kernel_id = el.find("kernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_key_name = el.find("keyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_network_interfaces = el.find("networkInterfaceSet")
    if child_network_interfaces is not None:
        import capo_ec2.types.instance_network_interface_specification_list

        out["network_interfaces"] = (
            capo_ec2.types.instance_network_interface_specification_list.deserialize_ec2_query(
                child_network_interfaces
            )
        )
    child_placement = el.find("placement")
    if child_placement is not None:
        import capo_ec2.types.spot_placement

        out["placement"] = capo_ec2.types.spot_placement.deserialize_ec2_query(
            child_placement
        )
    child_ramdisk_id = el.find("ramdiskId")
    if child_ramdisk_id is not None:
        out["ramdisk_id"] = str(child_ramdisk_id.text or "")
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_security_groups = el.find("groupSet")
    if child_security_groups is not None:
        import capo_ec2.types.group_identifier_list

        out["security_groups"] = (
            capo_ec2.types.group_identifier_list.deserialize_ec2_query(
                child_security_groups
            )
        )
    child_monitoring = el.find("monitoring")
    if child_monitoring is not None:
        import capo_ec2.types.run_instances_monitoring_enabled

        out["monitoring"] = (
            capo_ec2.types.run_instances_monitoring_enabled.deserialize_ec2_query(
                child_monitoring
            )
        )
    return out


def redact_sensitive(value: LaunchSpecification) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_data" in value:
        out["user_data"] = "*** Sensitive Data Redacted ***"
    return out
