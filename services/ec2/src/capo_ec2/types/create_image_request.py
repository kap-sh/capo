"""Generated from Smithy shape ``com.amazonaws.ec2#CreateImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.block_device_mapping_request_list
    import capo_ec2.types.boolean
    import capo_ec2.types.boot_mode_override_values
    import capo_ec2.types.image_description_request
    import capo_ec2.types.image_name_request
    import capo_ec2.types.instance_id
    import capo_ec2.types.snapshot_location_enum
    import capo_ec2.types.tag_specification_list


class CreateImageRequest(TypedDict, closed=True):
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the AMI and snapshots on creation. You can tag the AMI, the snapshots, or both.</p> <ul> <li> <p>To tag the AMI, the value for <code>ResourceType</code> must be <code>image</code>.</p> </li> <li> <p>To tag the snapshots that are created of the root volume and of other Amazon EBS volumes that are attached to the instance, the value for <code>ResourceType</code> must be <code>snapshot</code>. The same tag is applied to all of the snapshots that are created.</p> </li> </ul> <p>If you specify other values for <code>ResourceType</code>, the request fails.</p> <p>To tag an AMI or snapshot after it has been created, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html">CreateTags</a>. </p>"""
    snapshot_location: NotRequired[
        "capo_ec2.types.snapshot_location_enum.SnapshotLocationEnum"
    ]
    """<note> <p>Only supported for instances in Local Zones and for instances on Outposts that support local snapshots. If the source instance is not in one of these locations, omit this parameter.</p> </note> <p>The Amazon S3 location where the snapshots will be stored.</p> <ul> <li> <p>To create local snapshots in the same Local Zone or on the same Outpost as the source instance, specify <code>local</code>.</p> </li> <li> <p>To create regional snapshots in the parent Region of the Local Zone or Outpost, specify <code>regional</code>.</p> </li> </ul> <p>If the source instance is in a Local Zone and you omit this parameter, regional snapshots are created in the parent Region of the Local Zone.</p> <p>If the source instance is on an Outpost that supports local snapshots, this parameter is required. If you omit it, the request fails with an <code>InvalidParameterValue</code> error.</p> <p>Default: <code>regional</code> (for instances in Local Zones only)</p>"""
    boot_mode_override: NotRequired[
        "capo_ec2.types.boot_mode_override_values.BootModeOverrideValues"
    ]
    """<p>The boot mode of the new image, which overrides the default boot mode. By default, if you do not specify this parameter, the new image inherits the <code>boot-mode</code> from the source instance.</p> <p>A value of <code>uefi</code> indicates that the image only supports UEFI boot mode. You can specify this parameter only if the <code>current-instance-boot-mode</code> of the source instance is <code>uefi</code>. To find the <code>boot-mode</code> or <code>current-instance-boot-mode</code> of an instance, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html">DescribeInstances</a>.</p> <note> <p>The operating system contained in the AMI must be configured to support the specified boot mode.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html">Instance launch behavior with Amazon EC2 boot modes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    name: NotRequired["capo_ec2.types.image_name_request.ImageNameRequest"]
    """<p>A name for the new image.</p> <p>Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)</p>"""
    description: NotRequired[
        "capo_ec2.types.image_description_request.ImageDescriptionRequest"
    ]
    """<p>A description for the new image.</p>"""
    no_reboot: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether or not the instance should be automatically rebooted before creating the image. Specify one of the following values:</p> <ul> <li> <p> <code>true</code> - The instance is not rebooted before creating the image. This creates crash-consistent snapshots that include only the data that has been written to the volumes at the time the snapshots are created. Buffered data and data in memory that has not yet been written to the volumes is not included in the snapshots.</p> </li> <li> <p> <code>false</code> - The instance is rebooted before creating the image. This ensures that all buffered data and data in memory is written to the volumes before the snapshots are created.</p> </li> </ul> <p>Default: <code>false</code> </p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.block_device_mapping_request_list.BlockDeviceMappingRequestList"
    ]
    """<p>The block device mappings.</p> <p>When using the CreateImage action:</p> <ul> <li> <p>You can't change the volume size using the VolumeSize parameter. If you want a different volume size, you must first change the volume size of the source instance.</p> </li> <li> <p>You can't modify the encryption status of existing volumes or snapshots. To create an AMI with volumes or snapshots that have a different encryption status (for example, where the source volume and snapshots are unencrypted, and you want to create an AMI with encrypted volumes or snapshots), copy the image instead.</p> </li> <li> <p>The only option that can be changed for existing mappings or snapshots is <code>DeleteOnTermination</code>.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateImageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "snapshot_location" in value:
        import capo_ec2.types.snapshot_location_enum

        capo_ec2.types.snapshot_location_enum.serialize_ec2_query(
            value["snapshot_location"], pairs, f"{key_prefix}SnapshotLocation"
        )
    if "boot_mode_override" in value:
        import capo_ec2.types.boot_mode_override_values

        capo_ec2.types.boot_mode_override_values.serialize_ec2_query(
            value["boot_mode_override"], pairs, f"{key_prefix}BootModeOverride"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "no_reboot" in value:
        pairs.append(
            (f"{key_prefix}NoReboot", "true" if value["no_reboot"] else "false")
        )
    if "block_device_mappings" in value:
        import capo_ec2.types.block_device_mapping_request_list

        capo_ec2.types.block_device_mapping_request_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMapping"
        )


def deserialize_ec2_query(el: Element) -> CreateImageRequest:
    out: CreateImageRequest = {}  # type: ignore[typeddict-item]
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_snapshot_location = el.find("SnapshotLocation")
    if child_snapshot_location is not None:
        import capo_ec2.types.snapshot_location_enum

        out["snapshot_location"] = (
            capo_ec2.types.snapshot_location_enum.deserialize_ec2_query(
                child_snapshot_location
            )
        )
    child_boot_mode_override = el.find("BootModeOverride")
    if child_boot_mode_override is not None:
        import capo_ec2.types.boot_mode_override_values

        out["boot_mode_override"] = (
            capo_ec2.types.boot_mode_override_values.deserialize_ec2_query(
                child_boot_mode_override
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_no_reboot = el.find("noReboot")
    if child_no_reboot is not None:
        out["no_reboot"] = (child_no_reboot.text or "").lower() == "true"
    child_block_device_mappings = el.find("blockDeviceMapping")
    if child_block_device_mappings is not None:
        import capo_ec2.types.block_device_mapping_request_list

        out["block_device_mappings"] = (
            capo_ec2.types.block_device_mapping_request_list.deserialize_ec2_query(
                child_block_device_mappings
            )
        )
    return out
