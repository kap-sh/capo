"""Generated from Smithy shape ``com.amazonaws.ec2#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.architecture_values
    import capo_ec2.types.block_device_mapping_list
    import capo_ec2.types.boolean
    import capo_ec2.types.boot_mode_values
    import capo_ec2.types.device_type
    import capo_ec2.types.hypervisor_type
    import capo_ec2.types.image_state
    import capo_ec2.types.image_type_values
    import capo_ec2.types.image_watermark_list
    import capo_ec2.types.imds_support_values
    import capo_ec2.types.instance_type_specification
    import capo_ec2.types.platform_values
    import capo_ec2.types.product_code_list
    import capo_ec2.types.state_reason
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.tpm_support_values
    import capo_ec2.types.virtualization_type


class Image(TypedDict, closed=True):
    platform_details: NotRequired["capo_ec2.types.string.String"]
    """<p>The platform details associated with the billing code of the AMI. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html">Understand AMI billing information</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    usage_operation: NotRequired["capo_ec2.types.string.String"]
    """<p>The operation of the Amazon EC2 instance and the billing code that is associated with the AMI. <code>usageOperation</code> corresponds to the <a href="https://docs.aws.amazon.com/cur/latest/userguide/Lineitem-columns.html#Lineitem-details-O-Operation">lineitem/Operation</a> column on your Amazon Web Services Cost and Usage Report and in the <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html">Amazon Web Services Price List API</a>. You can view these fields on the <b>Instances</b> or <b>AMIs</b> pages in the Amazon EC2 console, or in the responses that are returned by the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html">DescribeImages</a> command in the Amazon EC2 API, or the <a href="https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html">describe-images</a> command in the CLI.</p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>Any block device mapping entries.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the AMI that was provided during image creation.</p>"""
    ena_support: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether enhanced networking with ENA is enabled.</p>"""
    hypervisor: NotRequired["capo_ec2.types.hypervisor_type.HypervisorType"]
    """<p>The hypervisor type of the image. Only <code>xen</code> is supported. <code>ovm</code> is not supported.</p>"""
    image_owner_alias: NotRequired["capo_ec2.types.string.String"]
    """<p>The owner alias (<code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code>).</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the AMI that was provided during image creation.</p>"""
    root_device_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The device name of the root device volume (for example, <code>/dev/sda1</code>).</p>"""
    root_device_type: NotRequired["capo_ec2.types.device_type.DeviceType"]
    """<p>The type of root device used by the AMI. The AMI can use an Amazon EBS volume or an instance store volume.</p>"""
    sriov_net_support: NotRequired["capo_ec2.types.string.String"]
    """<p>Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.</p>"""
    state_reason: NotRequired["capo_ec2.types.state_reason.StateReason"]
    """<p>The reason for the state change.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the image.</p>"""
    virtualization_type: NotRequired[
        "capo_ec2.types.virtualization_type.VirtualizationType"
    ]
    """<p>The type of virtualization of the AMI.</p>"""
    boot_mode: NotRequired["capo_ec2.types.boot_mode_values.BootModeValues"]
    """<p>The boot mode of the image. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html">Instance launch behavior with Amazon EC2 boot modes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    tpm_support: NotRequired["capo_ec2.types.tpm_support_values.TpmSupportValues"]
    """<p>If the image is configured for NitroTPM support, the value is <code>v2.0</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html">NitroTPM</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    deprecation_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The date and time to deprecate the AMI, in UTC, in the following format: <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z. If you specified a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.</p>"""
    imds_support: NotRequired["capo_ec2.types.imds_support_values.ImdsSupportValues"]
    """<p>If <code>v2.0</code>, it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have <code>HttpTokens</code> automatically set to <code>required</code> so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, <code>HttpPutResponseHopLimit</code> is set to <code>2</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration">Configure the AMI</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    source_instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance that the AMI was created from if the AMI was created using <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html">CreateImage</a>. This field only appears if the AMI was created using CreateImage.</p>"""
    deregistration_protection: NotRequired["capo_ec2.types.string.String"]
    """<p>Indicates whether deregistration protection is enabled for the AMI.</p>"""
    last_launched_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the AMI was last used to launch an EC2 instance. When the AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.</p> <note> <p> <code>lastLaunchedTime</code> data is available starting April 2017.</p> </note>"""
    image_allowed: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If <code>false</code> and Allowed AMIs is set to <code>enabled</code>, the AMI can't be discovered or used in the account. If <code>false</code> and Allowed AMIs is set to <code>audit-mode</code>, the AMI can be discovered and used in the account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html">Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs</a> in <i>Amazon EC2 User Guide</i>.</p>"""
    source_image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the source AMI from which the AMI was created.</p>"""
    source_image_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region of the source AMI.</p>"""
    free_tier_eligible: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the image is eligible for Amazon Web Services Free Tier.</p> <ul> <li> <p>If <code>true</code>, the AMI is eligible for Free Tier and can be used to launch instances under the Free Tier limits.</p> </li> <li> <p>If <code>false</code>, the AMI is not eligible for Free Tier.</p> </li> </ul>"""
    public_ssm_parameter_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the public Systems Manager parameter that resolves to this AMI, under the <code>aws/service/</code> namespace.</p>"""
    image_watermarks: NotRequired[
        "capo_ec2.types.image_watermark_list.ImageWatermarkList"
    ]
    """<p>The watermarks attached to the AMI.</p>"""
    instance_type_specification: NotRequired[
        "capo_ec2.types.instance_type_specification.InstanceTypeSpecification"
    ]
    """<p>The instance type specification for the AMI, which defines which instance types are compatible with this image.</p>"""
    image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    image_location: NotRequired["capo_ec2.types.string.String"]
    """<p>The location of the AMI.</p>"""
    state: NotRequired["capo_ec2.types.image_state.ImageState"]
    """<p>The current state of the AMI. If the state is <code>available</code>, the image is successfully registered and can be used to launch an instance.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the image.</p>"""
    creation_date: NotRequired["capo_ec2.types.string.String"]
    """<p>The date and time the image was created.</p>"""
    public: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the image has public launch permissions. The value is <code>true</code> if this image has public launch permissions or <code>false</code> if it has only implicit and explicit launch permissions.</p>"""
    product_codes: NotRequired["capo_ec2.types.product_code_list.ProductCodeList"]
    """<p>Any product codes associated with the AMI.</p>"""
    architecture: NotRequired["capo_ec2.types.architecture_values.ArchitectureValues"]
    """<p>The architecture of the image.</p>"""
    image_type: NotRequired["capo_ec2.types.image_type_values.ImageTypeValues"]
    """<p>The type of image.</p>"""
    kernel_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The kernel associated with the image, if any. Only applicable for machine images.</p>"""
    ramdisk_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The RAM disk associated with the image, if any. Only applicable for machine images.</p>"""
    platform: NotRequired["capo_ec2.types.platform_values.PlatformValues"]
    """<p>This value is set to <code>windows</code> for Windows AMIs; otherwise, it is blank.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Image, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "platform_details" in value:
        pairs.append((f"{key_prefix}PlatformDetails", str(value["platform_details"])))
    if "usage_operation" in value:
        pairs.append((f"{key_prefix}UsageOperation", str(value["usage_operation"])))
    if "block_device_mappings" in value:
        import capo_ec2.types.block_device_mapping_list

        capo_ec2.types.block_device_mapping_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMapping"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "ena_support" in value:
        pairs.append(
            (f"{key_prefix}EnaSupport", "true" if value["ena_support"] else "false")
        )
    if "hypervisor" in value:
        import capo_ec2.types.hypervisor_type

        capo_ec2.types.hypervisor_type.serialize_ec2_query(
            value["hypervisor"], pairs, f"{key_prefix}Hypervisor"
        )
    if "image_owner_alias" in value:
        pairs.append((f"{key_prefix}ImageOwnerAlias", str(value["image_owner_alias"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "root_device_name" in value:
        pairs.append((f"{key_prefix}RootDeviceName", str(value["root_device_name"])))
    if "root_device_type" in value:
        import capo_ec2.types.device_type

        capo_ec2.types.device_type.serialize_ec2_query(
            value["root_device_type"], pairs, f"{key_prefix}RootDeviceType"
        )
    if "sriov_net_support" in value:
        pairs.append((f"{key_prefix}SriovNetSupport", str(value["sriov_net_support"])))
    if "state_reason" in value:
        import capo_ec2.types.state_reason

        capo_ec2.types.state_reason.serialize_ec2_query(
            value["state_reason"], pairs, f"{key_prefix}StateReason"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "virtualization_type" in value:
        import capo_ec2.types.virtualization_type

        capo_ec2.types.virtualization_type.serialize_ec2_query(
            value["virtualization_type"], pairs, f"{key_prefix}VirtualizationType"
        )
    if "boot_mode" in value:
        import capo_ec2.types.boot_mode_values

        capo_ec2.types.boot_mode_values.serialize_ec2_query(
            value["boot_mode"], pairs, f"{key_prefix}BootMode"
        )
    if "tpm_support" in value:
        import capo_ec2.types.tpm_support_values

        capo_ec2.types.tpm_support_values.serialize_ec2_query(
            value["tpm_support"], pairs, f"{key_prefix}TpmSupport"
        )
    if "deprecation_time" in value:
        pairs.append((f"{key_prefix}DeprecationTime", str(value["deprecation_time"])))
    if "imds_support" in value:
        import capo_ec2.types.imds_support_values

        capo_ec2.types.imds_support_values.serialize_ec2_query(
            value["imds_support"], pairs, f"{key_prefix}ImdsSupport"
        )
    if "source_instance_id" in value:
        pairs.append(
            (f"{key_prefix}SourceInstanceId", str(value["source_instance_id"]))
        )
    if "deregistration_protection" in value:
        pairs.append(
            (
                f"{key_prefix}DeregistrationProtection",
                str(value["deregistration_protection"]),
            )
        )
    if "last_launched_time" in value:
        pairs.append(
            (f"{key_prefix}LastLaunchedTime", str(value["last_launched_time"]))
        )
    if "image_allowed" in value:
        pairs.append(
            (f"{key_prefix}ImageAllowed", "true" if value["image_allowed"] else "false")
        )
    if "source_image_id" in value:
        pairs.append((f"{key_prefix}SourceImageId", str(value["source_image_id"])))
    if "source_image_region" in value:
        pairs.append(
            (f"{key_prefix}SourceImageRegion", str(value["source_image_region"]))
        )
    if "free_tier_eligible" in value:
        pairs.append(
            (
                f"{key_prefix}FreeTierEligible",
                "true" if value["free_tier_eligible"] else "false",
            )
        )
    if "public_ssm_parameter_name" in value:
        pairs.append(
            (
                f"{key_prefix}PublicSsmParameterName",
                str(value["public_ssm_parameter_name"]),
            )
        )
    if "image_watermarks" in value:
        import capo_ec2.types.image_watermark_list

        capo_ec2.types.image_watermark_list.serialize_ec2_query(
            value["image_watermarks"], pairs, f"{key_prefix}ImageWatermarkSet"
        )
    if "instance_type_specification" in value:
        import capo_ec2.types.instance_type_specification

        capo_ec2.types.instance_type_specification.serialize_ec2_query(
            value["instance_type_specification"],
            pairs,
            f"{key_prefix}InstanceTypeSpecification",
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "image_location" in value:
        pairs.append((f"{key_prefix}ImageLocation", str(value["image_location"])))
    if "state" in value:
        import capo_ec2.types.image_state

        capo_ec2.types.image_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}ImageState"
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}ImageOwnerId", str(value["owner_id"])))
    if "creation_date" in value:
        pairs.append((f"{key_prefix}CreationDate", str(value["creation_date"])))
    if "public" in value:
        pairs.append((f"{key_prefix}IsPublic", "true" if value["public"] else "false"))
    if "product_codes" in value:
        import capo_ec2.types.product_code_list

        capo_ec2.types.product_code_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{key_prefix}ProductCodes"
        )
    if "architecture" in value:
        import capo_ec2.types.architecture_values

        capo_ec2.types.architecture_values.serialize_ec2_query(
            value["architecture"], pairs, f"{key_prefix}Architecture"
        )
    if "image_type" in value:
        import capo_ec2.types.image_type_values

        capo_ec2.types.image_type_values.serialize_ec2_query(
            value["image_type"], pairs, f"{key_prefix}ImageType"
        )
    if "kernel_id" in value:
        pairs.append((f"{key_prefix}KernelId", str(value["kernel_id"])))
    if "ramdisk_id" in value:
        pairs.append((f"{key_prefix}RamdiskId", str(value["ramdisk_id"])))
    if "platform" in value:
        import capo_ec2.types.platform_values

        capo_ec2.types.platform_values.serialize_ec2_query(
            value["platform"], pairs, f"{key_prefix}Platform"
        )


def deserialize_ec2_query(el: Element) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    child_platform_details = el.find("platformDetails")
    if child_platform_details is not None:
        out["platform_details"] = str(child_platform_details.text or "")
    child_usage_operation = el.find("usageOperation")
    if child_usage_operation is not None:
        out["usage_operation"] = str(child_usage_operation.text or "")
    child_block_device_mappings = el.find("blockDeviceMapping")
    if child_block_device_mappings is not None:
        import capo_ec2.types.block_device_mapping_list

        out["block_device_mappings"] = (
            capo_ec2.types.block_device_mapping_list.deserialize_ec2_query(
                child_block_device_mappings
            )
        )
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_ena_support = el.find("enaSupport")
    if child_ena_support is not None:
        out["ena_support"] = (child_ena_support.text or "").lower() == "true"
    child_hypervisor = el.find("hypervisor")
    if child_hypervisor is not None:
        import capo_ec2.types.hypervisor_type

        out["hypervisor"] = capo_ec2.types.hypervisor_type.deserialize_ec2_query(
            child_hypervisor
        )
    child_image_owner_alias = el.find("imageOwnerAlias")
    if child_image_owner_alias is not None:
        out["image_owner_alias"] = str(child_image_owner_alias.text or "")
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_root_device_name = el.find("rootDeviceName")
    if child_root_device_name is not None:
        out["root_device_name"] = str(child_root_device_name.text or "")
    child_root_device_type = el.find("rootDeviceType")
    if child_root_device_type is not None:
        import capo_ec2.types.device_type

        out["root_device_type"] = capo_ec2.types.device_type.deserialize_ec2_query(
            child_root_device_type
        )
    child_sriov_net_support = el.find("sriovNetSupport")
    if child_sriov_net_support is not None:
        out["sriov_net_support"] = str(child_sriov_net_support.text or "")
    child_state_reason = el.find("stateReason")
    if child_state_reason is not None:
        import capo_ec2.types.state_reason

        out["state_reason"] = capo_ec2.types.state_reason.deserialize_ec2_query(
            child_state_reason
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_virtualization_type = el.find("virtualizationType")
    if child_virtualization_type is not None:
        import capo_ec2.types.virtualization_type

        out["virtualization_type"] = (
            capo_ec2.types.virtualization_type.deserialize_ec2_query(
                child_virtualization_type
            )
        )
    child_boot_mode = el.find("bootMode")
    if child_boot_mode is not None:
        import capo_ec2.types.boot_mode_values

        out["boot_mode"] = capo_ec2.types.boot_mode_values.deserialize_ec2_query(
            child_boot_mode
        )
    child_tpm_support = el.find("tpmSupport")
    if child_tpm_support is not None:
        import capo_ec2.types.tpm_support_values

        out["tpm_support"] = capo_ec2.types.tpm_support_values.deserialize_ec2_query(
            child_tpm_support
        )
    child_deprecation_time = el.find("deprecationTime")
    if child_deprecation_time is not None:
        out["deprecation_time"] = str(child_deprecation_time.text or "")
    child_imds_support = el.find("imdsSupport")
    if child_imds_support is not None:
        import capo_ec2.types.imds_support_values

        out["imds_support"] = capo_ec2.types.imds_support_values.deserialize_ec2_query(
            child_imds_support
        )
    child_source_instance_id = el.find("sourceInstanceId")
    if child_source_instance_id is not None:
        out["source_instance_id"] = str(child_source_instance_id.text or "")
    child_deregistration_protection = el.find("deregistrationProtection")
    if child_deregistration_protection is not None:
        out["deregistration_protection"] = str(
            child_deregistration_protection.text or ""
        )
    child_last_launched_time = el.find("lastLaunchedTime")
    if child_last_launched_time is not None:
        out["last_launched_time"] = str(child_last_launched_time.text or "")
    child_image_allowed = el.find("imageAllowed")
    if child_image_allowed is not None:
        out["image_allowed"] = (child_image_allowed.text or "").lower() == "true"
    child_source_image_id = el.find("sourceImageId")
    if child_source_image_id is not None:
        out["source_image_id"] = str(child_source_image_id.text or "")
    child_source_image_region = el.find("sourceImageRegion")
    if child_source_image_region is not None:
        out["source_image_region"] = str(child_source_image_region.text or "")
    child_free_tier_eligible = el.find("freeTierEligible")
    if child_free_tier_eligible is not None:
        out["free_tier_eligible"] = (
            child_free_tier_eligible.text or ""
        ).lower() == "true"
    child_public_ssm_parameter_name = el.find("publicSsmParameterName")
    if child_public_ssm_parameter_name is not None:
        out["public_ssm_parameter_name"] = str(
            child_public_ssm_parameter_name.text or ""
        )
    child_image_watermarks = el.find("imageWatermarkSet")
    if child_image_watermarks is not None:
        import capo_ec2.types.image_watermark_list

        out["image_watermarks"] = (
            capo_ec2.types.image_watermark_list.deserialize_ec2_query(
                child_image_watermarks
            )
        )
    child_instance_type_specification = el.find("instanceTypeSpecification")
    if child_instance_type_specification is not None:
        import capo_ec2.types.instance_type_specification

        out["instance_type_specification"] = (
            capo_ec2.types.instance_type_specification.deserialize_ec2_query(
                child_instance_type_specification
            )
        )
    child_image_id = el.find("imageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_image_location = el.find("imageLocation")
    if child_image_location is not None:
        out["image_location"] = str(child_image_location.text or "")
    child_state = el.find("imageState")
    if child_state is not None:
        import capo_ec2.types.image_state

        out["state"] = capo_ec2.types.image_state.deserialize_ec2_query(child_state)
    child_owner_id = el.find("imageOwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_creation_date = el.find("creationDate")
    if child_creation_date is not None:
        out["creation_date"] = str(child_creation_date.text or "")
    child_public = el.find("isPublic")
    if child_public is not None:
        out["public"] = (child_public.text or "").lower() == "true"
    child_product_codes = el.find("productCodes")
    if child_product_codes is not None:
        import capo_ec2.types.product_code_list

        out["product_codes"] = capo_ec2.types.product_code_list.deserialize_ec2_query(
            child_product_codes
        )
    child_architecture = el.find("architecture")
    if child_architecture is not None:
        import capo_ec2.types.architecture_values

        out["architecture"] = capo_ec2.types.architecture_values.deserialize_ec2_query(
            child_architecture
        )
    child_image_type = el.find("imageType")
    if child_image_type is not None:
        import capo_ec2.types.image_type_values

        out["image_type"] = capo_ec2.types.image_type_values.deserialize_ec2_query(
            child_image_type
        )
    child_kernel_id = el.find("kernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_ramdisk_id = el.find("ramdiskId")
    if child_ramdisk_id is not None:
        out["ramdisk_id"] = str(child_ramdisk_id.text or "")
    child_platform = el.find("platform")
    if child_platform is not None:
        import capo_ec2.types.platform_values

        out["platform"] = capo_ec2.types.platform_values.deserialize_ec2_query(
            child_platform
        )
    return out
