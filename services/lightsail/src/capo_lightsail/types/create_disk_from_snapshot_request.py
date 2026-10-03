"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDiskFromSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.add_on_request_list
    import capo_lightsail.types.boolean
    import capo_lightsail.types.integer
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class CreateDiskFromSnapshotRequest(TypedDict, closed=True):
    disk_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The unique Lightsail disk name (<code>my-disk</code>).</p>"""
    disk_snapshot_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the disk snapshot (<code>my-snapshot</code>) from which to create the new storage disk.</p> <p>Constraint:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>source disk name</code> parameter. The <code>disk snapshot name</code> and <code>source disk name</code> parameters are mutually exclusive.</p> </li> </ul>"""
    availability_zone: "capo_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The Availability Zone where you want to create the disk (<code>us-east-2a</code>). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.</p> <p>Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.</p>"""
    size_in_gb: "capo_lightsail.types.integer.integer"
    """<p>The size of the disk in GB (<code>32</code>).</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    add_ons: NotRequired["capo_lightsail.types.add_on_request_list.AddOnRequestList"]
    """<p>An array of objects that represent the add-ons to enable for the new disk.</p>"""
    source_disk_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the source disk from which the source automatic snapshot was created.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>disk snapshot name</code> parameter. The <code>source disk name</code> and <code>disk snapshot name</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    restore_date: NotRequired["capo_lightsail.types.string.string"]
    """<p>The date of the automatic snapshot to use for the new disk. Use the <code>get auto snapshots</code> operation to identify the dates of the available automatic snapshots.</p> <p>Constraints:</p> <ul> <li> <p>Must be specified in <code>YYYY-MM-DD</code> format.</p> </li> <li> <p>This parameter cannot be defined together with the <code>use latest restorable auto snapshot</code> parameter. The <code>restore date</code> and <code>use latest restorable auto snapshot</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""
    use_latest_restorable_auto_snapshot: NotRequired[
        "capo_lightsail.types.boolean.boolean"
    ]
    """<p>A Boolean value to indicate whether to use the latest available automatic snapshot.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>restore date</code> parameter. The <code>use latest restorable auto snapshot</code> and <code>restore date</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDiskFromSnapshotRequest) -> dict:
    out: dict = {}
    out["diskName"] = value["disk_name"]
    if "disk_snapshot_name" in value:
        out["diskSnapshotName"] = value["disk_snapshot_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["sizeInGb"] = value["size_in_gb"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "add_ons" in value:
        import capo_lightsail.types.add_on_request_list

        out["addOns"] = capo_lightsail.types.add_on_request_list.serialize_aws_json_1_1(
            value["add_ons"]
        )
    if "source_disk_name" in value:
        out["sourceDiskName"] = value["source_disk_name"]
    if "restore_date" in value:
        out["restoreDate"] = value["restore_date"]
    if "use_latest_restorable_auto_snapshot" in value:
        out["useLatestRestorableAutoSnapshot"] = value[
            "use_latest_restorable_auto_snapshot"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDiskFromSnapshotRequest:
    out: CreateDiskFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("diskName") is not None:
        out["disk_name"] = data["diskName"]
    else:
        raise DeserializationError("CreateDiskFromSnapshotRequest.disk_name required")
    if data.get("diskSnapshotName") is not None:
        out["disk_snapshot_name"] = data["diskSnapshotName"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError(
            "CreateDiskFromSnapshotRequest.availability_zone required"
        )
    if data.get("sizeInGb") is not None:
        out["size_in_gb"] = data["sizeInGb"]
    else:
        raise DeserializationError("CreateDiskFromSnapshotRequest.size_in_gb required")
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("addOns") is not None:
        import capo_lightsail.types.add_on_request_list

        out["add_ons"] = (
            capo_lightsail.types.add_on_request_list.deserialize_aws_json_1_1(
                data["addOns"]
            )
        )
    if data.get("sourceDiskName") is not None:
        out["source_disk_name"] = data["sourceDiskName"]
    if data.get("restoreDate") is not None:
        out["restore_date"] = data["restoreDate"]
    if data.get("useLatestRestorableAutoSnapshot") is not None:
        out["use_latest_restorable_auto_snapshot"] = data[
            "useLatestRestorableAutoSnapshot"
        ]
    return out
