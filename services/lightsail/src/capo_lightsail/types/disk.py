"""Generated from Smithy shape ``com.amazonaws.lightsail#Disk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.add_on_list
    import capo_lightsail.types.auto_mount_status
    import capo_lightsail.types.boolean
    import capo_lightsail.types.disk_state
    import capo_lightsail.types.integer
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class Disk(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The unique name of the disk.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the disk.</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The date when the disk was created.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>The AWS Region and Availability Zone where the disk is located.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The Lightsail resource type (<code>Disk</code>).</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    add_ons: NotRequired["capo_lightsail.types.add_on_list.AddOnList"]
    """<p>An array of objects representing the add-ons enabled on the disk.</p>"""
    size_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The size of the disk in GB.</p>"""
    is_system_disk: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).</p>"""
    iops: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The input/output operations per second (IOPS) of the disk.</p>"""
    path: NotRequired["capo_lightsail.types.string.string"]
    """<p>The disk path.</p>"""
    state: NotRequired["capo_lightsail.types.disk_state.DiskState"]
    """<p>Describes the status of the disk.</p>"""
    attached_to: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The resources to which the disk is attached.</p>"""
    is_attached: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the disk is attached.</p>"""
    attachment_state: NotRequired["capo_lightsail.types.string.string"]
    """<p>(Discontinued) The attachment state of the disk.</p> <note> <p>In releases prior to November 14, 2017, this parameter returned <code>attached</code> for system disks in the API response. It is now discontinued, but still included in the response. Use <code>isAttached</code> instead.</p> </note>"""
    gb_in_use: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>(Discontinued) The number of GB in use by the disk.</p> <note> <p>In releases prior to November 14, 2017, this parameter was not included in the API response. It is now discontinued.</p> </note>"""
    auto_mount_status: NotRequired[
        "capo_lightsail.types.auto_mount_status.AutoMountStatus"
    ]
    """<p>The status of automatically mounting a storage disk to a virtual computer.</p> <important> <p>This parameter only applies to Lightsail for Research resources.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Disk) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "add_ons" in value:
        import capo_lightsail.types.add_on_list

        out["addOns"] = capo_lightsail.types.add_on_list.serialize_aws_json_1_1(
            value["add_ons"]
        )
    if "size_in_gb" in value:
        out["sizeInGb"] = value["size_in_gb"]
    if "is_system_disk" in value:
        out["isSystemDisk"] = value["is_system_disk"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "path" in value:
        out["path"] = value["path"]
    if "state" in value:
        import capo_lightsail.types.disk_state

        out["state"] = capo_lightsail.types.disk_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "attached_to" in value:
        out["attachedTo"] = value["attached_to"]
    if "is_attached" in value:
        out["isAttached"] = value["is_attached"]
    if "attachment_state" in value:
        out["attachmentState"] = value["attachment_state"]
    if "gb_in_use" in value:
        out["gbInUse"] = value["gb_in_use"]
    if "auto_mount_status" in value:
        import capo_lightsail.types.auto_mount_status

        out["autoMountStatus"] = (
            capo_lightsail.types.auto_mount_status.serialize_aws_json_1_1(
                value["auto_mount_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Disk:
    out: Disk = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("addOns") is not None:
        import capo_lightsail.types.add_on_list

        out["add_ons"] = capo_lightsail.types.add_on_list.deserialize_aws_json_1_1(
            data["addOns"]
        )
    if data.get("sizeInGb") is not None:
        out["size_in_gb"] = data["sizeInGb"]
    if data.get("isSystemDisk") is not None:
        out["is_system_disk"] = data["isSystemDisk"]
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("state") is not None:
        import capo_lightsail.types.disk_state

        out["state"] = capo_lightsail.types.disk_state.deserialize_aws_json_1_1(
            data["state"]
        )
    if data.get("attachedTo") is not None:
        out["attached_to"] = data["attachedTo"]
    if data.get("isAttached") is not None:
        out["is_attached"] = data["isAttached"]
    if data.get("attachmentState") is not None:
        out["attachment_state"] = data["attachmentState"]
    if data.get("gbInUse") is not None:
        out["gb_in_use"] = data["gbInUse"]
    if data.get("autoMountStatus") is not None:
        import capo_lightsail.types.auto_mount_status

        out["auto_mount_status"] = (
            capo_lightsail.types.auto_mount_status.deserialize_aws_json_1_1(
                data["autoMountStatus"]
            )
        )
    return out
