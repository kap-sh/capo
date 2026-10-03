"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetLaunchSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.block_device_mapping_list
    import capo_ec2.types.boolean
    import capo_ec2.types.double
    import capo_ec2.types.group_identifier_list
    import capo_ec2.types.iam_instance_profile_specification
    import capo_ec2.types.image_id
    import capo_ec2.types.instance_network_interface_specification_list
    import capo_ec2.types.instance_requirements
    import capo_ec2.types.instance_type
    import capo_ec2.types.key_pair_name
    import capo_ec2.types.sensitive_user_data
    import capo_ec2.types.spot_fleet_monitoring
    import capo_ec2.types.spot_fleet_tag_specification_list
    import capo_ec2.types.spot_placement
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id


class SpotFleetLaunchSpecification(TypedDict, closed=True):
    addressing_type: NotRequired["capo_ec2.types.string.String"]
    """<p>Deprecated.</p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>One or more block devices that are mapped to the Spot Instances. You can't specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.</p>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.</p> <p>Default: <code>false</code> </p>"""
    iam_instance_profile: NotRequired[
        "capo_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    kernel_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the kernel.</p>"""
    key_name: NotRequired["capo_ec2.types.key_pair_name.KeyPairName"]
    """<p>The name of the key pair.</p>"""
    monitoring: NotRequired["capo_ec2.types.spot_fleet_monitoring.SpotFleetMonitoring"]
    """<p>Enable or disable monitoring for the instances.</p>"""
    network_interfaces: NotRequired[
        "capo_ec2.types.instance_network_interface_specification_list.InstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces.</p> <note> <p> <code>SpotFleetLaunchSpecification</code> does not support Elastic Fabric Adapter (EFA). You must use <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateConfig.html">LaunchTemplateConfig</a> instead.</p> </note>"""
    placement: NotRequired["capo_ec2.types.spot_placement.SpotPlacement"]
    """<p>The placement information.</p>"""
    ramdisk_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the RAM disk. Some kernels require additional drivers at launch. Check the kernel requirements for information about whether you need to specify a RAM disk. To find kernel requirements, refer to the Amazon Web Services Resource Center and search for the kernel ID.</p>"""
    spot_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The IDs of the subnets in which to launch the instances. To specify multiple subnets, separate them using commas; for example, "subnet-1234abcdeexample1, subnet-0987cdef6example2".</p> <p>If you specify a network interface, you must specify any subnets as part of the network interface instead of using this parameter.</p>"""
    user_data: NotRequired["capo_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The base64-encoded user data that instances use when starting up. User data is limited to 16 KB.</p>"""
    weighted_capacity: NotRequired["capo_ec2.types.double.Double"]
    """<p>The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.</p> <p>If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.</p> <note> <p>When specifying weights, the price used in the <code>lowestPrice</code> and <code>priceCapacityOptimized</code> allocation strategies is per <i>unit</i> hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested <code>TargetCapacity</code>, resulting in only 1 instance being launched, the price used is per <i>instance</i> hour.</p> </note>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.spot_fleet_tag_specification_list.SpotFleetTagSpecificationList"
    ]
    """<p>The tags to apply during creation.</p>"""
    instance_requirements: NotRequired[
        "capo_ec2.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p> <note> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>.</p> </note>"""
    security_groups: NotRequired[
        "capo_ec2.types.group_identifier_list.GroupIdentifierList"
    ]
    """<p>The security groups.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetLaunchSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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
    if "monitoring" in value:
        import capo_ec2.types.spot_fleet_monitoring

        capo_ec2.types.spot_fleet_monitoring.serialize_ec2_query(
            value["monitoring"], pairs, f"{key_prefix}Monitoring"
        )
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
    if "spot_price" in value:
        pairs.append((f"{key_prefix}SpotPrice", str(value["spot_price"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "user_data" in value:
        pairs.append((f"{key_prefix}UserData", str(value["user_data"])))
    if "weighted_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}WeightedCapacity",
                (
                    "NaN"
                    if value["weighted_capacity"] != value["weighted_capacity"]
                    else "Infinity"
                    if value["weighted_capacity"] == float("inf")
                    else "-Infinity"
                    if value["weighted_capacity"] == float("-inf")
                    else str(value["weighted_capacity"])
                ),
            )
        )
    if "tag_specifications" in value:
        import capo_ec2.types.spot_fleet_tag_specification_list

        capo_ec2.types.spot_fleet_tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecificationSet"
        )
    if "instance_requirements" in value:
        import capo_ec2.types.instance_requirements

        capo_ec2.types.instance_requirements.serialize_ec2_query(
            value["instance_requirements"], pairs, f"{key_prefix}InstanceRequirements"
        )
    if "security_groups" in value:
        import capo_ec2.types.group_identifier_list

        capo_ec2.types.group_identifier_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{key_prefix}GroupSet"
        )


def deserialize_ec2_query(el: Element) -> SpotFleetLaunchSpecification:
    out: SpotFleetLaunchSpecification = {}  # type: ignore[typeddict-item]
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
    child_monitoring = el.find("monitoring")
    if child_monitoring is not None:
        import capo_ec2.types.spot_fleet_monitoring

        out["monitoring"] = capo_ec2.types.spot_fleet_monitoring.deserialize_ec2_query(
            child_monitoring
        )
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
    child_spot_price = el.find("spotPrice")
    if child_spot_price is not None:
        out["spot_price"] = str(child_spot_price.text or "")
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_user_data = el.find("userData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    child_weighted_capacity = el.find("weightedCapacity")
    if child_weighted_capacity is not None:
        out["weighted_capacity"] = float(child_weighted_capacity.text or "")
    child_tag_specifications = el.find("tagSpecificationSet")
    if child_tag_specifications is not None:
        import capo_ec2.types.spot_fleet_tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.spot_fleet_tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
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
    child_security_groups = el.find("groupSet")
    if child_security_groups is not None:
        import capo_ec2.types.group_identifier_list

        out["security_groups"] = (
            capo_ec2.types.group_identifier_list.deserialize_ec2_query(
                child_security_groups
            )
        )
    return out
