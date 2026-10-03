"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_boolean_value
    import capo_ec2.types.attribute_value
    import capo_ec2.types.boolean
    import capo_ec2.types.enclave_options_request
    import capo_ec2.types.group_id_string_list
    import capo_ec2.types.instance_attribute_name
    import capo_ec2.types.instance_block_device_mapping_specification_list
    import capo_ec2.types.instance_id
    import capo_ec2.types.modify_instance_attribute_value
    import capo_ec2.types.secure_blob_attribute_value


class ModifyInstanceAttributeRequest(TypedDict, closed=True):
    source_dest_check: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is <code>true</code>, source/destination checks are enabled; otherwise, they are disabled. The default value is <code>true</code>. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.</p>"""
    enclave_options: NotRequired[
        "capo_ec2.types.enclave_options_request.EnclaveOptionsRequest"
    ]
    """<p>Enables or disables the instance for Amazon Web Services Nitro Enclaves. For more information, see the <a href="https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html">Amazon Web Services Nitro Enclaves User Guide</a>.</p>"""
    disable_api_stop: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether an instance is enabled for stop protection. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html">Enable stop protection for your instance</a>.</p> <p></p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    attribute: NotRequired[
        "capo_ec2.types.instance_attribute_name.InstanceAttributeName"
    ]
    """<p>The name of the attribute to modify.</p> <note> <p>When changing the instance type: If the original instance type is configured for configurable bandwidth, and the desired instance type doesn't support configurable bandwidth, first set the existing bandwidth configuration to <code>default</code> using the <a>ModifyInstanceNetworkPerformanceOptions</a> operation.</p> </note> <important> <p>You can modify the following attributes only: <code>disableApiTermination</code> | <code>instanceType</code> | <code>kernel</code> | <code>ramdisk</code> | <code>instanceInitiatedShutdownBehavior</code> | <code>blockDeviceMapping</code> | <code>userData</code> | <code>sourceDestCheck</code> | <code>groupSet</code> | <code>ebsOptimized</code> | <code>sriovNetSupport</code> | <code>enaSupport</code> | <code>nvmeSupport</code> | <code>disableApiStop</code> | <code>enclaveOptions</code> </p> </important>"""
    value: NotRequired[
        "capo_ec2.types.modify_instance_attribute_value.ModifyInstanceAttributeValue"
    ]
    """<p>A new value for the attribute. Use only with the <code>kernel</code>, <code>ramdisk</code>, <code>userData</code>, <code>disableApiTermination</code>, or <code>instanceInitiatedShutdownBehavior</code> attribute.</p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.instance_block_device_mapping_specification_list.InstanceBlockDeviceMappingSpecificationList"
    ]
    """<p>Modifies the <code>DeleteOnTermination</code> attribute for volumes that are currently attached. The volume must be owned by the caller. If no value is specified for <code>DeleteOnTermination</code>, the default is <code>true</code> and the volume is deleted when the instance is terminated. You can't modify the <code>DeleteOnTermination</code> attribute for volumes that are attached to Amazon Web Services-managed resources.</p> <p>To add instance store volumes to an Amazon EBS-backed instance, you must add them when you launch the instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#Using_OverridingAMIBDM">Update the block device mapping when launching an instance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    disable_api_termination: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Enable or disable termination protection for the instance. If the value is <code>true</code>, you can't terminate the instance using the Amazon EC2 console, command line interface, or API. You can't enable termination protection for Spot Instances.</p>"""
    instance_type: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>Changes the instance type to the specified value. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Instance types</a> in the <i>Amazon EC2 User Guide</i>. If the instance type is not valid, the error returned is <code>InvalidInstanceAttributeValue</code>.</p>"""
    kernel: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>Changes the instance's kernel to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html">PV-GRUB</a>.</p>"""
    ramdisk: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>Changes the instance's RAM disk to the specified value. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedKernels.html">PV-GRUB</a>.</p>"""
    user_data: NotRequired[
        "capo_ec2.types.secure_blob_attribute_value.SecureBlobAttributeValue"
    ]
    """<p>Changes the instance's user data to the specified value. User data must be base64-encoded. Depending on the tool or SDK that you're using, the base64-encoding might be performed for you. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-add-user-data.html">Work with instance user data</a>.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "capo_ec2.types.attribute_value.AttributeValue"
    ]
    """<p>Specifies whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p>"""
    groups: NotRequired["capo_ec2.types.group_id_string_list.GroupIdStringList"]
    """<p>Replaces the security groups of the instance with the specified security groups. You must specify the ID of at least one security group, even if it's just the default security group for the VPC.</p>"""
    ebs_optimized: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Specifies whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.</p>"""
    sriov_net_support: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>Set to <code>simple</code> to enable enhanced networking with the Intel 82599 Virtual Function interface for the instance.</p> <p>There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time.</p> <p>This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.</p>"""
    ena_support: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Set to <code>true</code> to enable enhanced networking with ENA for the instance.</p> <p>This option is supported only for HVM instances. Specifying this option with a PV instance can make it unreachable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceAttributeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_dest_check" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["source_dest_check"], pairs, f"{key_prefix}SourceDestCheck"
        )
    if "enclave_options" in value:
        import capo_ec2.types.enclave_options_request

        capo_ec2.types.enclave_options_request.serialize_ec2_query(
            value["enclave_options"], pairs, f"{key_prefix}EnclaveOptions"
        )
    if "disable_api_stop" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["disable_api_stop"], pairs, f"{key_prefix}DisableApiStop"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "attribute" in value:
        import capo_ec2.types.instance_attribute_name

        capo_ec2.types.instance_attribute_name.serialize_ec2_query(
            value["attribute"], pairs, f"{key_prefix}Attribute"
        )
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))
    if "block_device_mappings" in value:
        import capo_ec2.types.instance_block_device_mapping_specification_list

        capo_ec2.types.instance_block_device_mapping_specification_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMapping"
        )
    if "disable_api_termination" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["disable_api_termination"],
            pairs,
            f"{key_prefix}DisableApiTermination",
        )
    if "instance_type" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "kernel" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["kernel"], pairs, f"{key_prefix}Kernel"
        )
    if "ramdisk" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["ramdisk"], pairs, f"{key_prefix}Ramdisk"
        )
    if "user_data" in value:
        import capo_ec2.types.secure_blob_attribute_value

        capo_ec2.types.secure_blob_attribute_value.serialize_ec2_query(
            value["user_data"], pairs, f"{key_prefix}UserData"
        )
    if "instance_initiated_shutdown_behavior" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["instance_initiated_shutdown_behavior"],
            pairs,
            f"{key_prefix}InstanceInitiatedShutdownBehavior",
        )
    if "groups" in value:
        import capo_ec2.types.group_id_string_list

        capo_ec2.types.group_id_string_list.serialize_ec2_query(
            value["groups"], pairs, f"{key_prefix}GroupId"
        )
    if "ebs_optimized" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["ebs_optimized"], pairs, f"{key_prefix}EbsOptimized"
        )
    if "sriov_net_support" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["sriov_net_support"], pairs, f"{key_prefix}SriovNetSupport"
        )
    if "ena_support" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["ena_support"], pairs, f"{key_prefix}EnaSupport"
        )


def deserialize_ec2_query(el: Element) -> ModifyInstanceAttributeRequest:
    out: ModifyInstanceAttributeRequest = {}  # type: ignore[typeddict-item]
    child_source_dest_check = el.find("SourceDestCheck")
    if child_source_dest_check is not None:
        import capo_ec2.types.attribute_boolean_value

        out["source_dest_check"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_source_dest_check
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
    child_disable_api_stop = el.find("DisableApiStop")
    if child_disable_api_stop is not None:
        import capo_ec2.types.attribute_boolean_value

        out["disable_api_stop"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_disable_api_stop
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_attribute = el.find("attribute")
    if child_attribute is not None:
        import capo_ec2.types.instance_attribute_name

        out["attribute"] = capo_ec2.types.instance_attribute_name.deserialize_ec2_query(
            child_attribute
        )
    child_value = el.find("value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    child_block_device_mappings = el.find("blockDeviceMapping")
    if child_block_device_mappings is not None:
        import capo_ec2.types.instance_block_device_mapping_specification_list

        out["block_device_mappings"] = (
            capo_ec2.types.instance_block_device_mapping_specification_list.deserialize_ec2_query(
                child_block_device_mappings
            )
        )
    child_disable_api_termination = el.find("disableApiTermination")
    if child_disable_api_termination is not None:
        import capo_ec2.types.attribute_boolean_value

        out["disable_api_termination"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_disable_api_termination
            )
        )
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.attribute_value

        out["instance_type"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_instance_type
        )
    child_kernel = el.find("kernel")
    if child_kernel is not None:
        import capo_ec2.types.attribute_value

        out["kernel"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_kernel
        )
    child_ramdisk = el.find("ramdisk")
    if child_ramdisk is not None:
        import capo_ec2.types.attribute_value

        out["ramdisk"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_ramdisk
        )
    child_user_data = el.find("userData")
    if child_user_data is not None:
        import capo_ec2.types.secure_blob_attribute_value

        out["user_data"] = (
            capo_ec2.types.secure_blob_attribute_value.deserialize_ec2_query(
                child_user_data
            )
        )
    child_instance_initiated_shutdown_behavior = el.find(
        "instanceInitiatedShutdownBehavior"
    )
    if child_instance_initiated_shutdown_behavior is not None:
        import capo_ec2.types.attribute_value

        out["instance_initiated_shutdown_behavior"] = (
            capo_ec2.types.attribute_value.deserialize_ec2_query(
                child_instance_initiated_shutdown_behavior
            )
        )
    child_groups = el.find("GroupId")
    if child_groups is not None:
        import capo_ec2.types.group_id_string_list

        out["groups"] = capo_ec2.types.group_id_string_list.deserialize_ec2_query(
            child_groups
        )
    child_ebs_optimized = el.find("ebsOptimized")
    if child_ebs_optimized is not None:
        import capo_ec2.types.attribute_boolean_value

        out["ebs_optimized"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_ebs_optimized
            )
        )
    child_sriov_net_support = el.find("sriovNetSupport")
    if child_sriov_net_support is not None:
        import capo_ec2.types.attribute_value

        out["sriov_net_support"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_sriov_net_support
        )
    child_ena_support = el.find("enaSupport")
    if child_ena_support is not None:
        import capo_ec2.types.attribute_boolean_value

        out["ena_support"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_ena_support
            )
        )
    return out
