"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.associate_public_ip_address
    import capo_auto_scaling.types.block_device_mappings
    import capo_auto_scaling.types.classic_link_vpc_security_groups
    import capo_auto_scaling.types.ebs_optimized
    import capo_auto_scaling.types.instance_metadata_options
    import capo_auto_scaling.types.instance_monitoring
    import capo_auto_scaling.types.resource_name
    import capo_auto_scaling.types.security_groups
    import capo_auto_scaling.types.spot_price
    import capo_auto_scaling.types.timestamp_type
    import capo_auto_scaling.types.xml_string_max_len64
    import capo_auto_scaling.types.xml_string_max_len255
    import capo_auto_scaling.types.xml_string_max_len1600
    import capo_auto_scaling.types.xml_string_user_data


class LaunchConfiguration(TypedDict, closed=True):
    launch_configuration_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the launch configuration.</p>"""
    launch_configuration_arn: NotRequired[
        "capo_auto_scaling.types.resource_name.ResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the launch configuration.</p>"""
    image_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The ID of the Amazon Machine Image (AMI) to use to launch your EC2 instances. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html">Find a Linux AMI</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    key_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the key pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html">Amazon EC2 key pairs and Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    security_groups: NotRequired[
        "capo_auto_scaling.types.security_groups.SecurityGroups"
    ]
    """<p>A list that contains the security groups to assign to the instances in the Auto Scaling group. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html">Control traffic to your Amazon Web Services resources using security groups</a> in the <i>Amazon Virtual Private Cloud User Guide</i>.</p>"""
    classic_link_vpc_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>Available for backward compatibility.</p>"""
    classic_link_vpc_security_groups: NotRequired[
        "capo_auto_scaling.types.classic_link_vpc_security_groups.ClassicLinkVPCSecurityGroups"
    ]
    """<p>Available for backward compatibility.</p>"""
    user_data: NotRequired[
        "capo_auto_scaling.types.xml_string_user_data.XmlStringUserData"
    ]
    """<p>The user data to make available to the launched EC2 instances. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html">Instance metadata and user data</a> in the <i>Amazon EC2 User Guide</i>. If you are using a command line tool, base64-encoding is performed for you, and you can load the text from a file. Otherwise, you must provide base64-encoded text. User data is limited to 16 KB.</p>"""
    instance_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The instance type for the instances. For information about available instance types, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#AvailableInstanceTypes">Available instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    kernel_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The ID of the kernel associated with the AMI.</p>"""
    ramdisk_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The ID of the RAM disk associated with the AMI.</p>"""
    block_device_mappings: NotRequired[
        "capo_auto_scaling.types.block_device_mappings.BlockDeviceMappings"
    ]
    """<p>The block device mapping entries that define the block devices to attach to the instances at launch. By default, the block devices specified in the block device mapping for the AMI are used. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html">Block device mappings</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_monitoring: NotRequired[
        "capo_auto_scaling.types.instance_monitoring.InstanceMonitoring"
    ]
    """<p>Controls whether instances in this group are launched with detailed (<code>true</code>) or basic (<code>false</code>) monitoring.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/latest/userguide/enable-as-instance-metrics.html">Configure monitoring for Auto Scaling instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    spot_price: NotRequired["capo_auto_scaling.types.spot_price.SpotPrice"]
    """<p>The maximum hourly price to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot price. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-template-spot-instances.html">Requesting Spot Instances for fault-tolerant and flexible applications</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    iam_instance_profile: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len1600.XmlStringMaxLen1600"
    ]
    """<p>The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html">IAM role for applications that run on Amazon EC2 instances</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    created_time: NotRequired["capo_auto_scaling.types.timestamp_type.TimestampType"]
    """<p>The creation date and time for the launch configuration.</p>"""
    ebs_optimized: NotRequired["capo_auto_scaling.types.ebs_optimized.EbsOptimized"]
    """<p>Specifies whether the launch configuration is optimized for EBS I/O (<code>true</code>) or not (<code>false</code>). For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html">Amazon EBS-optimized instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    associate_public_ip_address: NotRequired[
        "capo_auto_scaling.types.associate_public_ip_address.AssociatePublicIpAddress"
    ]
    """<p>Specifies whether to assign a public IPv4 address to the group's instances. If the instance is launched into a default subnet, the default is to assign a public IPv4 address, unless you disabled the option to assign a public IPv4 address on the subnet. If the instance is launched into a nondefault subnet, the default is not to assign a public IPv4 address, unless you enabled the option to assign a public IPv4 address on the subnet. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-in-vpc.html">Provide network connectivity for your Auto Scaling instances using Amazon VPC</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    placement_tenancy: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
    ]
    """<p>The tenancy of the instance, either <code>default</code> or <code>dedicated</code>. An instance with <code>dedicated</code> tenancy runs on isolated, single-tenant hardware and can only be launched into a VPC.</p>"""
    metadata_options: NotRequired[
        "capo_auto_scaling.types.instance_metadata_options.InstanceMetadataOptions"
    ]
    """<p>The metadata options for the instances. For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html#launch-configurations-imds">Configure the instance metadata options</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_configuration_name" in value:
        pairs.append(
            (
                f"{key_prefix}LaunchConfigurationName",
                str(value["launch_configuration_name"]),
            )
        )
    if "launch_configuration_arn" in value:
        pairs.append(
            (
                f"{key_prefix}LaunchConfigurationARN",
                str(value["launch_configuration_arn"]),
            )
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "security_groups" in value:
        import capo_auto_scaling.types.security_groups

        capo_auto_scaling.types.security_groups.serialize_query(
            value["security_groups"], pairs, f"{key_prefix}SecurityGroups"
        )
    if "classic_link_vpc_id" in value:
        pairs.append(
            (f"{key_prefix}ClassicLinkVPCId", str(value["classic_link_vpc_id"]))
        )
    if "classic_link_vpc_security_groups" in value:
        import capo_auto_scaling.types.classic_link_vpc_security_groups

        capo_auto_scaling.types.classic_link_vpc_security_groups.serialize_query(
            value["classic_link_vpc_security_groups"],
            pairs,
            f"{key_prefix}ClassicLinkVPCSecurityGroups",
        )
    if "user_data" in value:
        pairs.append((f"{key_prefix}UserData", str(value["user_data"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "kernel_id" in value:
        pairs.append((f"{key_prefix}KernelId", str(value["kernel_id"])))
    if "ramdisk_id" in value:
        pairs.append((f"{key_prefix}RamdiskId", str(value["ramdisk_id"])))
    if "block_device_mappings" in value:
        import capo_auto_scaling.types.block_device_mappings

        capo_auto_scaling.types.block_device_mappings.serialize_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMappings"
        )
    if "instance_monitoring" in value:
        import capo_auto_scaling.types.instance_monitoring

        capo_auto_scaling.types.instance_monitoring.serialize_query(
            value["instance_monitoring"], pairs, f"{key_prefix}InstanceMonitoring"
        )
    if "spot_price" in value:
        pairs.append((f"{key_prefix}SpotPrice", str(value["spot_price"])))
    if "iam_instance_profile" in value:
        pairs.append(
            (f"{key_prefix}IamInstanceProfile", str(value["iam_instance_profile"]))
        )
    if "created_time" in value:
        import capo_auto_scaling.types.timestamp_type

        capo_auto_scaling.types.timestamp_type.serialize_query(
            value["created_time"], pairs, f"{key_prefix}CreatedTime"
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{key_prefix}EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "associate_public_ip_address" in value:
        pairs.append(
            (
                f"{key_prefix}AssociatePublicIpAddress",
                "true" if value["associate_public_ip_address"] else "false",
            )
        )
    if "placement_tenancy" in value:
        pairs.append((f"{key_prefix}PlacementTenancy", str(value["placement_tenancy"])))
    if "metadata_options" in value:
        import capo_auto_scaling.types.instance_metadata_options

        capo_auto_scaling.types.instance_metadata_options.serialize_query(
            value["metadata_options"], pairs, f"{key_prefix}MetadataOptions"
        )


def deserialize_query(el: Element) -> LaunchConfiguration:
    out: LaunchConfiguration = {}  # type: ignore[typeddict-item]
    child_launch_configuration_name = el.find("LaunchConfigurationName")
    if child_launch_configuration_name is not None:
        out["launch_configuration_name"] = str(
            child_launch_configuration_name.text or ""
        )
    child_launch_configuration_arn = el.find("LaunchConfigurationARN")
    if child_launch_configuration_arn is not None:
        out["launch_configuration_arn"] = str(child_launch_configuration_arn.text or "")
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_security_groups = el.find("SecurityGroups")
    if child_security_groups is not None:
        import capo_auto_scaling.types.security_groups

        out["security_groups"] = (
            capo_auto_scaling.types.security_groups.deserialize_query(
                child_security_groups
            )
        )
    child_classic_link_vpc_id = el.find("ClassicLinkVPCId")
    if child_classic_link_vpc_id is not None:
        out["classic_link_vpc_id"] = str(child_classic_link_vpc_id.text or "")
    child_classic_link_vpc_security_groups = el.find("ClassicLinkVPCSecurityGroups")
    if child_classic_link_vpc_security_groups is not None:
        import capo_auto_scaling.types.classic_link_vpc_security_groups

        out["classic_link_vpc_security_groups"] = (
            capo_auto_scaling.types.classic_link_vpc_security_groups.deserialize_query(
                child_classic_link_vpc_security_groups
            )
        )
    child_user_data = el.find("UserData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_kernel_id = el.find("KernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_ramdisk_id = el.find("RamdiskId")
    if child_ramdisk_id is not None:
        out["ramdisk_id"] = str(child_ramdisk_id.text or "")
    child_block_device_mappings = el.find("BlockDeviceMappings")
    if child_block_device_mappings is not None:
        import capo_auto_scaling.types.block_device_mappings

        out["block_device_mappings"] = (
            capo_auto_scaling.types.block_device_mappings.deserialize_query(
                child_block_device_mappings
            )
        )
    child_instance_monitoring = el.find("InstanceMonitoring")
    if child_instance_monitoring is not None:
        import capo_auto_scaling.types.instance_monitoring

        out["instance_monitoring"] = (
            capo_auto_scaling.types.instance_monitoring.deserialize_query(
                child_instance_monitoring
            )
        )
    child_spot_price = el.find("SpotPrice")
    if child_spot_price is not None:
        out["spot_price"] = str(child_spot_price.text or "")
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        out["iam_instance_profile"] = str(child_iam_instance_profile.text or "")
    child_created_time = el.find("CreatedTime")
    if child_created_time is not None:
        import capo_auto_scaling.types.timestamp_type

        out["created_time"] = capo_auto_scaling.types.timestamp_type.deserialize_query(
            child_created_time
        )
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_associate_public_ip_address = el.find("AssociatePublicIpAddress")
    if child_associate_public_ip_address is not None:
        out["associate_public_ip_address"] = (
            child_associate_public_ip_address.text or ""
        ).lower() == "true"
    child_placement_tenancy = el.find("PlacementTenancy")
    if child_placement_tenancy is not None:
        out["placement_tenancy"] = str(child_placement_tenancy.text or "")
    child_metadata_options = el.find("MetadataOptions")
    if child_metadata_options is not None:
        import capo_auto_scaling.types.instance_metadata_options

        out["metadata_options"] = (
            capo_auto_scaling.types.instance_metadata_options.deserialize_query(
                child_metadata_options
            )
        )
    return out
